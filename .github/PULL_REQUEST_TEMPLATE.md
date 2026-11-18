## What and why

## Type
- [ ] Stage content  - [ ] Skill content  - [ ] Governance or templates  - [ ] Scripts or CI  - [ ] Docs only

## Checklist
- [ ] `make all` passes locally (paste the last lines)
- [ ] I edited sources, not generated files
- [ ] Stage IDs and names are unchanged
- [ ] No fabricated evidence; examples are labelled `ILLUSTRATIVE`
- [ ] README or docs claims I added can be reproduced by a command
- [ ] **Skill change:** I bumped `version` in `registry/skill-content/<skill>.json`, ran `python3 scripts/check_skill_versions.py --update`, and added a `CHANGELOG.md` line
- [ ] **Quality scores:** I recorded scores only from a real SkillEvaluator run (`scripts/check_quality_regression.py --add`), or I did not touch scores
- [ ] **Approvals or risk tiers:** I updated `registry/risk-tiers.json` and the governance docs together, and named the human approver
- [ ] No secrets, tokens or personal data in the diff
