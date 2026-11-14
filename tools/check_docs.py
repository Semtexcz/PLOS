#!/usr/bin/env python3
"""Strukturální kontrola dokumentace PLOS.

Pomocný nástroj pro kontrolu dokumentace, nikoli součást metodiky PLOS.
Kontroluje uzavření zdrojových bloků, šířky tabulek, relativní odkazy včetně
kotev, definice a odkazy identifikátorů, deklarované doménové asociace a
násobnosti a pokrytí sémantických případů. Není to parser gramatiky Mermaid,
renderer ani validátor UML metamodelu.

Použití:
    python3 tools/check_docs.py [--json PATH]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIAGRAMS = ROOT / "04-diagrams"
DOMAIN_MODEL = ROOT / "03-architecture/preliminary-domain-model.md"
SEMANTIC_REPORT = ROOT / "07-review/semantic-validation-report.md"

CANONICAL_SOURCES = {
    "DC": ROOT / "glossary.md",
    "DR": DOMAIN_MODEL,
    "INV": DOMAIN_MODEL,
    "SV": SEMANTIC_REPORT,
}
EXPECTED_DEFINITIONS = {"DC": 36, "DR": 40, "INV": 18, "SV": 14}
EXPECTED_CLASSIFICATIONS = {
    "Core": 12,
    "Contextual": 9,
    "Optional": 6,
    "Derived": 9,
}


def anchors(text: str) -> set[str]:
    out: set[str] = set()
    seen: dict[str, int] = {}
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        out.add(slug + (f"-{n}" if n else ""))
    out.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    return out


def check_markdown(files: list[Path], errors: list[str]) -> tuple[int, int]:
    links = 0
    blocks = 0
    for p in files:
        s = p.read_text()
        fences = re.findall(r"^```.*$", s, re.M)
        if len(fences) % 2:
            errors.append(f"{p.name}: unclosed fence")
        blocks += len(re.findall(r"^```mermaid$", s, re.M))
        width = None
        inside = False
        for i, line in enumerate(s.splitlines(), 1):
            if line.startswith("```"):
                inside = not inside
            if not inside and line.startswith("|"):
                n = len(re.split(r"(?<!\\)\|", line))
                if width is not None and width != n:
                    errors.append(f"{p.name}:{i}: table width {n}, expected {width}")
                width = n
            else:
                width = None
            if line.rstrip() != line:
                errors.append(f"{p.name}:{i}: trailing whitespace")
        for dest in re.findall(r"\]\(([^)]+)\)", s):
            if re.match(r"\w+://|mailto:", dest):
                continue
            links += 1
            dest = dest.strip("<>")
            path, _, frag = dest.partition("#")
            q = p.parent / path if path else p
            if not q.exists():
                errors.append(f"{p.name}: missing {dest}")
            elif frag and frag not in anchors(q.read_text()):
                errors.append(f"{p.name}: missing anchor {dest}")
    return links, blocks


def check_identifiers(files: list[Path], errors: list[str]) -> dict[str, set[str]]:
    ids: dict[str, set[str]] = {}
    for pref, p in CANONICAL_SOURCES.items():
        defs = re.findall(r"^\| (" + pref + r"-\d+)\b", p.read_text(), re.M)
        ids[pref] = set(defs)
        if len(defs) != len(set(defs)):
            errors.append(f"{pref}: duplicate definition")
        want = {f"{pref}-{n:02}" for n in range(1, EXPECTED_DEFINITIONS[pref] + 1)}
        if set(defs) != want:
            errors.append(f"{pref}: unexpected definitions {set(defs) ^ want}")
    for p in files:
        for pref, valid in ids.items():
            for token in re.findall(r"\b" + pref + r"-\d+\b", p.read_text()):
                if token not in valid:
                    errors.append(f"{p.name}: undefined {token}")
    return ids


def domain_relations(dom: str) -> dict[str, tuple[set[str], set[str]]]:
    normalize = lambda x: re.sub(r"\s+", "", x)
    relations: dict[str, tuple[set[str], set[str]]] = {}
    for rid, ends in re.findall(r"^\| (DR-\d+) \| (.*?) / ", dom, re.M):
        left, right = ends.split(" → ")
        relations[rid] = (
            {normalize(x) for x in left.split(", ")},
            {normalize(x) for x in right.split(", ")},
        )
    return relations


def check_diagrams(errors: list[str]) -> int:
    dom = DOMAIN_MODEL.read_text()
    relations = domain_relations(dom)
    edges = 0
    for p in sorted(DIAGRAMS.glob("DG-*.md")):
        for block in re.findall(r"```mermaid\n(.*?)```", p.read_text(), re.S):
            if not block.startswith("classDiagram"):
                continue
            for line in block.splitlines()[1:]:
                if not line.strip() or line.strip().startswith("direction"):
                    continue
                m = re.fullmatch(
                    r'\s*(\w+) "([^"]+)" --> "([^"]+)" (\w+) : (DR-\d+) .+', line
                )
                if not m:
                    errors.append(f"{p.name}: unexpected association syntax {line}")
                    continue
                a, ma, mb, b, rid = m.groups()
                edges += 1
                if a not in relations[rid][0] or b not in relations[rid][1]:
                    errors.append(f"{p.name}: DR mismatch {line}")
                if rid == "DR-01":
                    exp = ("0..*", "1..*")
                elif rid == "DR-24":
                    exp = ("1", "0..*")
                elif rid == "DR-31":
                    exp = ("0..*", "1")
                else:
                    exp = ("0..*", "0..*")
                if (ma, mb) != exp:
                    errors.append(f"{p.name}: multiplicity mismatch {line}")
    return edges


def check_semantics(ids: dict[str, set[str]], errors: list[str]) -> tuple[int, int]:
    sem = SEMANTIC_REPORT.read_text()
    cases = re.findall(r"^\| ((?:UC|SV)-\d+) —", sem, re.M)
    if len(cases) != 22 or len(set(cases)) != 22:
        errors.append(f"case count {len(cases)}")
    used: set[str] = set()
    for row in sem.splitlines():
        if re.match(r"^\| (UC|SV)-", row):
            for first, rest in re.findall(r"INV-(\d+)((?:/\d+)*)", row):
                used.add("INV-" + first)
                used.update("INV-" + n for n in rest.split("/") if n)
    if used != ids["INV"]:
        errors.append(f"invariants not exercised {ids['INV'] - used}")
    return len(cases), len(used)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--json", type=Path, metavar="PATH", help="zapsat JSON report do souboru"
    )
    args = parser.parse_args(argv)

    files = sorted(ROOT.rglob("*.md"))
    errors: list[str] = []
    links, blocks = check_markdown(files, errors)
    ids = check_identifiers(files, errors)

    dom = DOMAIN_MODEL.read_text()
    classifications = re.findall(
        r"^\| DC-\d+ .*?\| (Core|Contextual|Optional|Derived) ", dom, re.M
    )
    counts = {k: classifications.count(k) for k in EXPECTED_CLASSIFICATIONS}
    if counts != EXPECTED_CLASSIFICATIONS:
        errors.append(f"classification count {counts}")

    edges = check_diagrams(errors)
    cases, exercised = check_semantics(ids, errors)

    report = {
        "markdown_files": len(files),
        "relative_links": links,
        "mermaid_blocks": blocks,
        "class_associations_checked": edges,
        "definitions": {k: len(v) for k, v in ids.items()},
        "classifications": counts,
        "semantic_cases": cases,
        "invariants_exercised": exercised,
        "errors": errors,
        "limitations": (
            "Structural and declared-relation checks only; not a Mermaid grammar "
            "parser, renderer, or UML metamodel validator."
        ),
    }
    output = json.dumps(report, ensure_ascii=False, indent=2)
    print(output)
    if args.json:
        args.json.write_text(output + "\n")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
