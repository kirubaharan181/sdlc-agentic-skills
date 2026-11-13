"""Compatibility entry point for deterministic library regeneration.

Canonical structured content lives in registries plus `rebuild_library.py`; this
entry point intentionally never falls back to the former generic templates.
"""
import argparse
from pathlib import Path
from rebuild_library import main

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Regenerate canonical specialist library artifacts.')
    parser.add_argument('--check', action='store_true', help='Validate generator import; use validate.py for full checks.')
    args = parser.parse_args()
    if not args.check:
        main()
    else:
        root = Path(__file__).resolve().parents[1]
        tracked = [root/'registry/SDLC_STAGE_REGISTRY.yaml', root/'registry/AGENT_REGISTRY.yaml', root/'registry/WORKFLOW_REGISTRY.yaml']
        tracked += list((root/'agents').glob('*.md')) + list((root/'workflows').glob('*.md')) + list((root/'skills').rglob('SKILL.md')) + list((root/'skills').rglob('STAGE_PLAYBOOK.md'))
        before = {p: p.read_bytes() for p in tracked if p.exists()}
        main()
        after_paths = set(tracked) | {root/'registry/SDLC_STAGE_REGISTRY.yaml', root/'registry/AGENT_REGISTRY.yaml', root/'registry/WORKFLOW_REGISTRY.yaml'}
        changed = [p for p in after_paths if p.exists() and before.get(p) != p.read_bytes()]
        for p, data in before.items(): p.write_bytes(data)
        for p in after_paths - set(before):
            if p.exists(): p.unlink()
        if changed:
            raise SystemExit('GENERATOR CHECK FAILED: generated content differs: ' + ', '.join(str(p.relative_to(root)) for p in changed[:8]))
        print('GENERATOR CHECK PASSED: regeneration is deterministic and left no changes.')
