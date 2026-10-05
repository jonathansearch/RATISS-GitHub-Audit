# RATISS GitHub Audit

## Global audit of the `jonathansearch` account

This repository centralizes the professional audit of the GitHub account `jonathansearch`, carried out according to the **RATISS-Framework** method, layer 1 of RATISS Labs. It serves as a public registry of the controls, of the non-destructive corrections, of the confirmed deletions and of the retention decisions.

> **Scope.** The audit relies on the global report dated **2026-09-15**. The report states **45 audited repositories**, an average score of **77/100**, **3 grade-A repositories**, **33 grade B**, **9 grade C**, **0 grade D** and **0 grade F**.

## Executive summary

The report identifies **0 true secret**, **0 true `.env` file** and **0 private email address** in the analyzed scope. The main observed risk is the public presentation: generic descriptions, licenses insufficiently detected by GitHub, copied or rebranded repositories, project duplicates and a few missing pieces of document structure.

The `RATISS-Framework` and `RATISS-LABS-GTT` repositories are the main technical references. They obtained **100/100** in the report. This repository complements those two projects by documenting the governance and the public hygiene of the account as a whole.

## Confirmed actions executed

The following deletions were requested and confirmed by the account owner, then executed:

| Repository | Action | State |
|---|---|---|
| `open-webui` | deletion confirmed | deleted |
| `ratiss-cypher-odv-scientist` | deletion confirmed | deleted |
| `openhands` | deletion confirmed | deleted |
| `robot-Ratiss-` | deletion confirmed | deleted |
| `evinajonathan13-max` | deletion confirmed | deleted |

The only official website of RATISS Labs is **[https://jonathansearch.github.io/ratiss-labs-site/](https://jonathansearch.github.io/ratiss-labs-site/)**, published from the [`ratiss-labs-site`](https://github.com/jonathansearch/ratiss-labs-site) repository. The `ratiss-labs-website` repository **is not official**; it was **archived**, not deleted, solely to keep a historical reference and a recovery option.

The misspelled repository `sciece-2` was renamed to [`science-2`](https://github.com/jonathansearch/science-2). This operation preserves the repository history and benefits from GitHub redirects.

## RATISS-Framework method

The audit is documented according to principles R4 to R7: results are separated from hypotheses, values are tied to their scope, discrepancies are kept and claims must remain replayable. The reference report specifies that the audit was executed following a process of clone, scan, verification of READMEs, licenses, secrets, large files, `.env` files and authors, with human verification of sensitive clues.

The method repository is available in [`RATISS-Framework`](https://github.com/jonathansearch/RATISS-Framework). The corresponding experimental platform is [`RATISS-LABS-GTT`](https://github.com/jonathansearch/RATISS-LABS-GTT).

## File list

| File | Function |
|---|---|
| [`RAPPORT-GLOBAL.md`](RAPPORT-GLOBAL.md) | global report of the account audit, with scores, findings, limits and correction plan |
| [`AUDIT.md`](AUDIT.md) | professional registry of the executed controls, of the decisions taken and of the remaining actions |
| [`resultats.json`](resultats.json) | structured summary of the scores and categories reported in the report |
| [`rejouer.sh`](rejouer.sh) | helper for the local reproduction of the audit and for the verification of the reference repositories |
| [`LICENSE`](LICENSE) | license of this documentary registry |

This registry is itself documented as an artifact audited by **RATISS-Framework**. It does not replace an independent audit: its status is that of a disclosed self-audit, in accordance with rule N2.

## Non-destructive corrections

The public descriptions of the retained repositories are normalized to avoid the repetitive wording "RATISS Labs professional repository". The descriptions now state the role of the repository or, when no reliable specialization is available in the report, its membership in the research and engineering portfolio of RATISS Labs.

The recommended future corrections concern the presence of licenses recognized by GitHub, the missing READMEs, the `.gitignore` files, the documentation of vendored copies and the harmonization of branches. These corrections must be applied repository by repository so as not to unintentionally alter code or scientific evidence.

## Declared limits

The source report states that the clones were performed with `--depth 1`. The deep history was therefore not fully scanned. The audit is a self-audit executed with the RATISS Labs tools; validation by an independent auditor remains to be obtained.

## Contact and official website

The reference public website is [ratiss-labs-site](https://jonathansearch.github.io/ratiss-labs-site/). The GitHub account is [jonathansearch](https://github.com/jonathansearch). The RATISS Labs laboratory is presented in the reference repositories.

## References

[1]: https://github.com/jonathansearch/RATISS-Framework "RATISS-Framework — executable scientific audit protocol"
[2]: https://github.com/jonathansearch/RATISS-LABS-GTT "RATISS-LABS-GTT — main experimental platform"
[3]: https://jonathansearch.github.io/ratiss-labs-site/ "Official website of RATISS Labs"
