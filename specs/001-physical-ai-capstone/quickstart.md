# Quickstart Guide: Physical AI Capstone Paper Writing Workflow

**Phase**: 1 (Design & Tool Setup)
**Date**: 2025-12-17
**Purpose**: Guide for setting up tools, writing workflow, and executing the implementation plan

## Prerequisites

- [ ] Markdown editor (VS Code, Typora, or Obsidian)
- [ ] Citation manager (Zotero recommended - free, open-source)
- [ ] Word processor (MS Word or LibreOffice for final PDF)
- [ ] Plagiarism checker access (Turnitin, iThenticate, or Copyscape)
- [ ] Academic database access (IEEE Xplore, ACM DL, ScienceDirect via institution)

## Setup Steps

### 1. Citation Management (Zotero)

```bash
# Download from zotero.org
# Install browser connector for easy import
# Create library: "Physical AI Capstone Paper"
# Create collections: P1_Literature_Review, P2_Curriculum_Design, etc.
# Install Zotero Word plugin for in-document citations
```

### 2. Directory Structure

```bash
# From repo root
mkdir -p paper/{00-metadata,01-introduction,02-literature-review,03-curriculum-design,04-ros2-technical,05-simulation-platforms,06-ai-integration,07-evaluation,08-conclusion,09-references,final}
```

### 3. Git Version Control

```bash
git add specs/001-physical-ai-capstone/
git commit -m "docs: initial planning artifacts for Physical AI paper"
git add paper/
git commit -m "docs: initialize paper directory structure"
```

## Writing Workflow

### Phase 0: Research (research.md)
1. Execute search queries (IEEE, ACM, Scholar)
2. Import sources to Zotero (≥15 total, ≥8 peer-reviewed)
3. Read and tag sources
4. Update research.md with source inventory

### Phase 1: Drafting Sections (P1-P6)
1. Start with P1 (Literature Review) - foundational
2. Draft in Markdown: `paper/02-literature-review/physical-ai-definitions.md`
3. Insert citations: `(Author, Year)` → track in Zotero
4. Track word count per section
5. Proceed to P2-P6 sequentially or in parallel (P2-P5 after P1 drafted)

### Phase 2: Checkpoints
- **25%**: P1 drafted, ≥4 peer-reviewed sources cited, first plagiarism check
- **50%**: P1-P3 drafted, ≥6 peer-reviewed, readability check (FK 10-12)
- **75%**: P1-P5 drafted, ≥8 peer-reviewed, full citation audit
- **100%**: All sections complete, all 5 constitutional gates passed

### Phase 3: Assembly
1. Combine Markdown files (Pandoc or manual copy to Word)
2. Insert Zotero citations using Word plugin
3. Format per APA 7th edition template
4. Generate references automatically from Zotero
5. Export to PDF with hyperlinks

## Quality Gates (from constitution.md)

1. **Source Verification**: Every claim traced to source
2. **Citation Integrity**: APA 7th edition, complete references
3. **Peer-Review Threshold**: ≥8 of 15+ sources peer-reviewed
4. **Plagiarism Check**: 0% similarity (excluding citations)
5. **Writing Quality**: FK grade 10-12, all terms defined
6. **Reproducibility**: Claims linked to specific source locations

## Quick Commands

```bash
# Word count per section
wc -w paper/02-literature-review/*.md

# Check all word counts
find paper -name "*.md" -exec wc -w {} +

# Combine all sections for review
cat paper/*/*.md > paper/final/draft-combined.md

# Git commit after section
git add paper/02-literature-review/
git commit -m "docs(P1): draft Physical AI definitions subsection"
```

## Validation Tools

- **Readability**: MS Word (Review → Readability Statistics) or https://readabilityformulas.com
- **Plagiarism**: Submit draft to institutional Turnitin or use Copyscape
- **Citation Check**: Zotero report, manually verify in-text ↔ references
- **APA Format**: Use APA template in Word, Zotero auto-formats references

## Troubleshooting

**Issue**: Word count exceeds 7,000
**Solution**: Prioritize P1-P4 (core content ~4,500 words), condense P5-P6

**Issue**: <50% peer-reviewed sources
**Solution**: Replace technical docs with academic papers where possible (ROS 2 → middleware performance study, simulation → benchmarking paper)

**Issue**: Plagiarism check flags passages
**Solution**: Rewrite in own words, ensure paraphrasing substantial, add more citations

**Issue**: FK score >12 (too complex)
**Solution**: Simplify sentence structure, reduce passive voice, define jargon

## Timeline Estimate

- Research (Phase 0): 8-12 hours
- P1 Drafting: 8-10 hours
- P2-P6 Drafting: 15-20 hours
- Revision & Citation Audit: 6-8 hours
- Final Assembly & Formatting: 4-6 hours
- **Total**: 41-56 hours (~1-2 weeks full-time, 4-6 weeks part-time)

## Next Steps

1. Execute research.md literature search
2. Begin P1 drafting (literature review)
3. Run /sp.tasks to generate detailed task list
4. Commit progress regularly to Git
5. Validate at each checkpoint (25%, 50%, 75%, 100%)

**Status**: Ready to begin research phase
