# Tasks: Physical AI Capstone Quarter Research Paper

**Input**: Design documents from `/specs/001-physical-ai-capstone/`
**Prerequisites**: plan.md (required), spec.md (required), data-model.md, outline.md, research.md, quickstart.md

**Note**: This is a research paper project. Tasks focus on literature search, content creation, citation management, and quality validation rather than code implementation.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (independent sections, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US6)
- Include exact file paths in `paper/` directory

## Path Conventions

Research paper uses content-based structure:
- `paper/00-metadata/` - Title page, abstract
- `paper/01-introduction/` - Introduction section
- `paper/02-literature-review/` - P1 (US1) content
- `paper/03-curriculum-design/` - P2 (US2) content
- `paper/04-ros2-technical/` - P3 (US3) content
- `paper/05-simulation-platforms/` - P4 (US4) content
- `paper/06-ai-integration/` - P5 (US5) content
- `paper/07-evaluation/` - P6 (US6) content
- `paper/08-conclusion/` - Conclusion section
- `paper/09-references/` - Bibliography
- `paper/final/` - Compiled PDF

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Tool setup and directory initialization

- [ ] T001 Install and configure Zotero citation manager (zotero.org)
- [ ] T002 Install Zotero browser connector for source import
- [ ] T003 Create Zotero library "Physical AI Capstone Paper"
- [ ] T004 Create Zotero collections: P1_Literature_Review, P2_Curriculum_Design, P3_ROS2_Technical, P4_Simulation_Comparison, P5_AI_Integration, P6_Evaluation
- [ ] T005 Install Zotero Word plugin for citation insertion
- [ ] T006 Create paper directory structure: paper/{00-metadata,01-introduction,02-literature-review,03-curriculum-design,04-ros2-technical,05-simulation-platforms,06-ai-integration,07-evaluation,08-conclusion,09-references,final}
- [ ] T007 Initialize Git tracking for paper directory
- [ ] T008 Download APA 7th edition CSL style file for Zotero
- [ ] T009 Verify access to academic databases (IEEE Xplore, ACM DL, ScienceDirect)
- [ ] T010 Set up readability checker (MS Word or online tool)

---

## Phase 2: Literature Search (Foundational - Blocks All User Stories)

**Purpose**: Identify and acquire all sources before writing begins

**⚠️ CRITICAL**: No content writing can begin until minimum source threshold met (≥15 total, ≥8 peer-reviewed)

### Phase 2.1: Peer-Reviewed Source Search

- [ ] T011 [P] Execute IEEE Xplore search: "Physical AI" OR "embodied AI" AND robotics (filter: ICRA, IROS, RSS conferences)
- [ ] T012 [P] Execute IEEE Xplore search: "ROS 2" AND middleware AND architecture
- [ ] T013 [P] Execute IEEE Xplore search: robotics AND simulation AND (Gazebo OR "Isaac Sim")
- [ ] T014 [P] Execute IEEE Xplore search: "VSLAM" OR "visual SLAM" AND robotics
- [ ] T015 [P] Execute IEEE Xplore search: "vision language action" OR "VLA" AND robotics
- [ ] T016 [P] Execute ACM DL search: robotics AND education AND curriculum (filter: SIGCSE, FIE)
- [ ] T017 [P] Execute ACM DL search: "project-based learning" AND engineering AND robotics
- [ ] T018 [P] Execute ScienceDirect search: robotics education AND pedagogy
- [ ] T019 [P] Execute Google Scholar search: "Physical AI" OR "embodied AI" filetype:pdf
- [ ] T020 [P] Execute Google Scholar search: RT-1 RT-2 vision language action robotics

### Phase 2.2: Technical Documentation Collection

- [ ] T021 [P] Collect ROS 2 Documentation (docs.ros.org) - save URLs and version info
- [ ] T022 [P] Collect Gazebo Documentation (gazebosim.org)
- [ ] T023 [P] Collect Unity Robotics Hub documentation (GitHub, Unity Learn)
- [ ] T024 [P] Collect NVIDIA Isaac Sim documentation (docs.omniverse.nvidia.com/isaacsim)
- [ ] T025 [P] Collect Isaac ROS documentation (nvidia-isaac-ros.github.io)
- [ ] T026 [P] Collect rclpy API reference (docs.ros.org)
- [ ] T027 [P] Collect URDF specification (wiki.ros.org)

### Phase 2.3: Source Curation and Import

- [ ] T028 Review search results and identify ≥10 peer-reviewed sources (prioritize recent 2020-2025)
- [ ] T029 Import peer-reviewed sources to Zotero with complete metadata (authors, year, DOI, journal/conference)
- [ ] T030 Import technical documentation sources to Zotero with version numbers and URLs
- [ ] T031 Tag sources by topic: physical-ai, ros2, simulation, education, vslam, vla, pedagogy
- [ ] T032 Tag sources by type: peer-reviewed, technical-doc
- [ ] T033 Verify total source count ≥15 with peer-reviewed count ≥8 (53%+ threshold)
- [ ] T034 Read and annotate each source in Zotero (highlight key findings relevant to user stories)
- [ ] T035 Update specs/001-physical-ai-capstone/research.md with source inventory (ID, title, authors, relevance)
- [ ] T036 Export initial bibliography from Zotero to paper/09-references/references.bib (BibTeX format)

**Checkpoint**: Foundation ready - content writing can now begin in parallel for user stories

---

## Phase 3: User Story 1 - Literature Review (Priority: P1) 🎯 MVP

**Goal**: Draft comprehensive literature review section establishing theoretical foundation (Section 2, ~1,500 words)

**Independent Test**: Verify all claims about Physical AI, ROS 2, Gazebo, Unity, Isaac traced to peer-reviewed or technical documentation sources

### Content Drafting for US1

- [ ] T037 [P] [US1] Draft subsection: Physical AI definitions and evolution in paper/02-literature-review/physical-ai-definitions.md (~400 words, 4-5 peer-reviewed citations)
- [ ] T038 [P] [US1] Draft subsection: ROS 2 middleware research in paper/02-literature-review/ros2-middleware-research.md (~400 words, 1-2 peer-reviewed + ROS 2 docs)
- [ ] T039 [P] [US1] Draft subsection: Simulation technologies landscape in paper/02-literature-review/simulation-technologies.md (~400 words, 1 peer-reviewed + Gazebo/Unity/Isaac docs)
- [ ] T040 [P] [US1] Draft subsection: Robotics education pedagogy in paper/02-literature-review/robotics-education-pedagogy.md (~300 words, 1-2 peer-reviewed)

### Citation and Quality for US1

- [ ] T041 [US1] Insert in-text citations in APA format (Author, Year) for all factual claims in US1 subsections
- [ ] T042 [US1] Define all technical terms on first use: Physical AI, embodied AI, ROS 2, DDS, Gazebo, Unity, Isaac Sim
- [ ] T043 [US1] Check word count for US1 section (target: 1,300-1,700 words)
- [ ] T044 [US1] Run readability check on US1 content (target: Flesch-Kincaid grade 10-12)
- [ ] T045 [US1] Adjust language if FK score outside target range (simplify sentences, reduce passive voice)
- [ ] T046 [US1] Verify ≥4 peer-reviewed sources cited in US1 section
- [ ] T047 [US1] Run first plagiarism check on US1 draft (Turnitin or Copyscape)
- [ ] T048 [US1] Address any plagiarism flags (rewrite passages, add more citations)

**Checkpoint**: US1 complete - can proceed to US2 (P2) while US1 is in review/revision

---

## Phase 4: User Story 2 - Curriculum Design Analysis (Priority: P2)

**Goal**: Draft curriculum design and pedagogical framework section (Section 3, ~1,200 words)

**Independent Test**: Verify curriculum design decisions justified with educational theory citations (Bloom's, constructivism, PBL)

### Content Drafting for US2

- [ ] T049 [P] [US2] Draft subsection: Module structure analysis in paper/03-curriculum-design/module-structure-analysis.md (~450 words, cite Bloom's taxonomy, cognitive load theory)
- [ ] T050 [P] [US2] Draft subsection: Pedagogical framework in paper/03-curriculum-design/pedagogical-framework.md (~400 words, cite constructivism, project-based learning)
- [ ] T051 [P] [US2] Draft subsection: Technology selection rationale in paper/03-curriculum-design/technology-selection-rationale.md (~350 words, cite industry adoption, educational suitability)

### Citation and Quality for US2

- [ ] T052 [US2] Insert in-text citations for all pedagogical claims (educational theory sources)
- [ ] T053 [US2] Define educational terms on first use: Bloom's taxonomy, scaffolding, constructivism, PBL
- [ ] T054 [US2] Check word count for US2 section (target: 1,000-1,400 words)
- [ ] T055 [US2] Run readability check on US2 content (FK 10-12)
- [ ] T056 [US2] Verify ≥2 peer-reviewed sources cited in US2 section
- [ ] T057 [US2] Commit US2 draft to Git

**Checkpoint**: US2 complete - US1 and US2 now form coherent foundation (P1 + P2)

---

## Phase 5: User Story 3 - ROS 2 Technical Deep-Dive (Priority: P3)

**Goal**: Draft ROS 2 architecture technical analysis section (Section 4, ~1,000 words)

**Independent Test**: Verify technical claims about ROS 2 architecture, rclpy, URDF traceable to official docs or technical papers

### Content Drafting for US3

- [ ] T058 [P] [US3] Draft subsection: ROS 2 architecture in paper/04-ros2-technical/ros2-architecture.md (~400 words, cite ROS 2 design docs, DDS papers)
- [ ] T059 [P] [US3] Draft subsection: Python integration with rclpy in paper/04-ros2-technical/python-integration.md (~300 words, cite rclpy docs)
- [ ] T060 [P] [US3] Draft subsection: URDF robot modeling in paper/04-ros2-technical/urdf-modeling.md (~300 words, cite URDF spec, robotics textbook)

### Citation and Quality for US3

- [ ] T061 [US3] Insert in-text citations for all technical claims (ROS 2 docs, middleware papers)
- [ ] T062 [US3] Define technical terms: nodes, topics, services, actions, DDS, rclpy, URDF, TF2
- [ ] T063 [US3] Check word count for US3 section (target: 850-1,150 words)
- [ ] T064 [US3] Run readability check on US3 content (FK 10-12)
- [ ] T065 [US3] Verify ≥1 peer-reviewed source cited in US3 section
- [ ] T066 [US3] Commit US3 draft to Git

**Checkpoint**: Core technical content complete (P1-P3 drafted, ~3,700 words)

---

## Phase 6: 25% Completion Checkpoint

**Purpose**: Validate progress and adjust course if needed

- [ ] T067 Verify P1 (US1) drafted and in acceptable state
- [ ] T068 Verify ≥4 peer-reviewed sources cited so far
- [ ] T069 Run combined plagiarism check on P1-P2 content
- [ ] T070 Verify plagiarism score 0% (excluding proper citations)
- [ ] T071 Calculate current word count (target: ~1,500 for P1 alone or ~2,700 for P1-P2)
- [ ] T072 Review outline.md and confirm P4-P6 sections still achievable within 7,000 word limit
- [ ] T073 Adjust P4-P6 word count targets if needed (condense P5-P6 if word count trending high)

---

## Phase 7: User Story 4 - Simulation Comparison (Priority: P4)

**Goal**: Draft simulation platform comparison section (Section 5, ~800 words)

**Independent Test**: Verify comparative claims supported by benchmarking studies, technical specs, or reproducible experiments

### Content Drafting for US4

- [ ] T074 [P] [US4] Draft subsection: Gazebo analysis in paper/05-simulation-platforms/gazebo-analysis.md (~250 words, cite Gazebo docs, benchmarking paper)
- [ ] T075 [P] [US4] Draft subsection: Unity analysis in paper/05-simulation-platforms/unity-analysis.md (~250 words, cite Unity Robotics Hub docs)
- [ ] T076 [P] [US4] Draft subsection: NVIDIA Isaac comparison in paper/05-simulation-platforms/isaac-comparison.md (~300 words, cite Isaac docs, sim-to-real paper)

### Citation and Quality for US4

- [ ] T077 [US4] Insert in-text citations for all comparative claims
- [ ] T078 [US4] Define simulation terms: physics engine, sensor simulation, sim-to-real transfer
- [ ] T079 [US4] Check word count for US4 section (target: 700-900 words)
- [ ] T080 [US4] Run readability check on US4 content (FK 10-12)
- [ ] T081 [US4] Verify ≥1 peer-reviewed source cited in US4 section
- [ ] T082 [US4] Commit US4 draft to Git

**Checkpoint**: P1-P4 complete (~4,500 words) - core paper content established

---

## Phase 8: 50% Completion Checkpoint

**Purpose**: Mid-point validation before proceeding to advanced topics (P5-P6)

- [ ] T083 Verify P1-P3 drafted and polished
- [ ] T084 Verify total word count 4,000-5,500 (on track for 5,000-7,000 target)
- [ ] T085 Verify ≥6 peer-reviewed sources cited across P1-P4
- [ ] T086 Run full readability analysis on P1-P4 combined (target FK 10-12)
- [ ] T087 Adjust sentence complexity if FK score outside range
- [ ] T088 Run citation format audit: verify all in-text citations have (Author, Year) format
- [ ] T089 Run second plagiarism check on P1-P4 content
- [ ] T090 Address any plagiarism flags
- [ ] T091 Draft abstract in paper/00-metadata/abstract.md (150-250 words summarizing P1-P4 content)
- [ ] T092 Draft introduction in paper/01-introduction/introduction.md (~300 words: motivation, research questions, paper structure)

---

## Phase 9: User Story 5 - AI-Robot Integration (Priority: P5)

**Goal**: Draft AI integration patterns section (Section 6, ~700 words)

**Independent Test**: Verify claims about VSLAM, VLA, multi-modal perception traceable to recent AI/robotics papers (2022-2025)

### Content Drafting for US5

- [ ] T093 [P] [US5] Draft subsection: VSLAM navigation in paper/06-ai-integration/vslam-navigation.md (~250 words, cite ORB-SLAM3 paper, Isaac ROS docs)
- [ ] T094 [P] [US5] Draft subsection: Vision-Language-Action models in paper/06-ai-integration/vla-models.md (~250 words, cite RT-1, RT-2, or PaLM-E papers)
- [ ] T095 [P] [US5] Draft subsection: Multi-modal perception in paper/06-ai-integration/multimodal-perception.md (~200 words, cite sensor fusion paper)

### Citation and Quality for US5

- [ ] T096 [US5] Insert in-text citations for all AI/robotics claims (prioritize 2022-2025 papers)
- [ ] T097 [US5] Define AI terms: VSLAM, VLA, ORB-SLAM3, RT-1, RT-2, sensor fusion, Kalman filter
- [ ] T098 [US5] Check word count for US5 section (target: 600-800 words)
- [ ] T099 [US5] Run readability check on US5 content (FK 10-12)
- [ ] T100 [US5] Verify ≥2 peer-reviewed sources cited in US5 section
- [ ] T101 [US5] Commit US5 draft to Git

**Checkpoint**: P1-P5 complete (~5,200 words) - advanced AI content added

---

## Phase 10: User Story 6 - Evaluation Framework (Priority: P6)

**Goal**: Draft evaluation and future directions section (Section 7, ~600 words)

**Independent Test**: Verify evaluation frameworks cite educational assessment literature and future directions cite recent trends

### Content Drafting for US6

- [ ] T102 [P] [US6] Draft subsection: Assessment framework in paper/07-evaluation/assessment-framework.md (~250 words, cite capstone assessment paper, ABET criteria)
- [ ] T103 [P] [US6] Draft subsection: Implementation challenges in paper/07-evaluation/implementation-challenges.md (~200 words, cite robotics education challenges)
- [ ] T104 [P] [US6] Draft subsection: Future directions in paper/07-evaluation/future-directions.md (~150 words, cite emerging robotics/AI trends)

### Citation and Quality for US6

- [ ] T105 [US6] Insert in-text citations for evaluation frameworks and future trends
- [ ] T106 [US6] Define evaluation terms: rubric, formative assessment, summative assessment
- [ ] T107 [US6] Check word count for US6 section (target: 500-700 words)
- [ ] T108 [US6] Run readability check on US6 content (FK 10-12)
- [ ] T109 [US6] Verify ≥1 peer-reviewed source cited in US6 section
- [ ] T110 [US6] Commit US6 draft to Git

**Checkpoint**: All content sections P1-P6 drafted (~5,800 words body content)

---

## Phase 11: 75% Completion Checkpoint

**Purpose**: Final content validation before conclusion and assembly

- [ ] T111 Verify all content sections P1-P6 drafted
- [ ] T112 Verify total word count 5,000-6,500 (body content only, excluding intro/conclusion/references)
- [ ] T113 Verify ≥8 peer-reviewed sources cited across all sections
- [ ] T114 Calculate peer-reviewed percentage (should be ≥53% of total sources)
- [ ] T115 Run full citation-reference audit: verify every in-text citation has corresponding reference entry
- [ ] T116 Run full reference-citation audit: verify no orphan references (references without in-text citations)
- [ ] T117 Fix any citation-reference mismatches
- [ ] T118 Run third plagiarism check on full P1-P6 content
- [ ] T119 Address any plagiarism flags (final opportunity before submission)
- [ ] T120 Review introduction draft and update with final paper structure
- [ ] T121 Draft conclusion in paper/08-conclusion/conclusion.md (~200 words: summary, significance, call to action)

---

## Phase 12: Final Assembly and Validation

**Purpose**: Compile all sections, format per APA 7th edition, generate PDF

### Content Assembly

- [ ] T122 Combine all Markdown files into single document: cat paper/*/*.md > paper/final/draft-combined.md
- [ ] T123 Copy combined content to MS Word or open in Pandoc for formatting
- [ ] T124 Apply APA 7th edition template (title page, headers, page numbers, font: Times New Roman 12pt, double-spacing)
- [ ] T125 Insert Zotero citations into Word document using Word plugin (convert (Author, Year) to proper APA in-text format)
- [ ] T126 Generate references section automatically from Zotero (Insert Bibliography)
- [ ] T127 Verify references in APA 7th edition format (hanging indent, alphabetical order)
- [ ] T128 Format title page: title, subtitle, author(s), affiliation, date
- [ ] T129 Format abstract: centered "Abstract" heading, 150-250 words, no indent
- [ ] T130 Add section headings (Level 1: centered bold, Level 2: left-aligned bold, Level 3: left-aligned bold italic)
- [ ] T131 Add page numbers (top right corner, starting after title page)

### Final Validation (100% Checkpoint - All Constitutional Gates)

- [ ] T132 **Gate 1: Source Verification** - Verify every factual claim traced to source (manual review of random sample)
- [ ] T133 **Gate 1: Source Verification** - Verify all sources accessible and verifiable (check URLs/DOIs)
- [ ] T134 **Gate 1: Source Verification** - Verify ≥8 peer-reviewed sources cited
- [ ] T135 **Gate 1: Source Verification** - Verify minimum 15 total sources met
- [ ] T136 **Gate 2: Citation Compliance** - Verify all in-text citations APA 7th edition format
- [ ] T137 **Gate 2: Citation Compliance** - Verify reference list complete with DOI/URL for electronic sources
- [ ] T138 **Gate 2: Citation Compliance** - Verify 100% citation-reference match (no mismatches)
- [ ] T139 **Gate 2: Citation Compliance** - Validate all URLs and DOIs functional (click each link)
- [ ] T140 **Gate 3: Plagiarism Check** - Run final plagiarism detection (Turnitin or iThenticate)
- [ ] T141 **Gate 3: Plagiarism Check** - Verify 0% similarity score (excluding properly cited quotations)
- [ ] T142 **Gate 4: Writing Quality** - Run Flesch-Kincaid readability analysis on full paper
- [ ] T143 **Gate 4: Writing Quality** - Verify FK grade level 10-12 (adjust language if needed)
- [ ] T144 **Gate 4: Writing Quality** - Verify all technical terms defined on first use (manual checklist review)
- [ ] T145 **Gate 4: Writing Quality** - Run grammar and spelling check (MS Word or Grammarly)
- [ ] T146 **Gate 4: Writing Quality** - Verify word count 5,000-7,000 (excluding title, abstract, references)
- [ ] T147 **Gate 5: Reproducibility** - Verify claims linked to specific source locations (page numbers in citations where needed)
- [ ] T148 **Gate 5: Reproducibility** - Verify methodology documented sufficiently (literature search strategy reproducible from research.md)

### PDF Generation and Final Review

- [ ] T149 Export Word document to PDF: paper/final/physical-ai-capstone-paper.pdf
- [ ] T150 Verify PDF has working hyperlinks (DOIs, URLs in references)
- [ ] T151 Verify PDF embedded fonts and proper formatting
- [ ] T152 Open PDF and read through for final proofreading (typos, formatting glitches)
- [ ] T153 Fix any issues found in proofreading
- [ ] T154 Regenerate PDF after fixes
- [ ] T155 Create final Git commit: "docs: complete Physical AI Capstone research paper v1.0"
- [ ] T156 Tag Git repository: git tag v1.0-submission

**Checkpoint**: All 5 constitutional gates passed, paper ready for submission

---

## Phase 13: Optional Enhancements (Post-Submission)

**Purpose**: Improvements that can be made after meeting all requirements

- [ ] T157 [P] Add figures/diagrams: ROS 2 architecture diagram, simulation platform comparison table
- [ ] T158 [P] Create supplementary materials: detailed literature search log, extended bibliography
- [ ] T159 [P] Request peer review from advisor or colleague
- [ ] T160 [P] Incorporate peer review feedback (if time permits)
- [ ] T161 [P] Prepare conference poster or presentation slides (if submitting to conference)
- [ ] T162 [P] Submit to academic conference (ASEE, IEEE FIE, SIGCSE) or journal

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Literature Search (Phase 2)**: Depends on Setup - BLOCKS all user stories until ≥15 sources acquired
- **User Stories (Phases 3-10)**: All depend on Literature Search completion
  - US1 (P1) can start immediately after Phase 2
  - US2 (P2) can start after US1 drafted (or in parallel if author comfortable)
  - US3-US6 (P3-P6) can proceed sequentially or in parallel after US1 complete
- **Checkpoints (Phases 6, 8, 11)**: Validate progress at 25%, 50%, 75% completion
- **Final Assembly (Phase 12)**: Depends on all user stories (P1-P6) complete

### User Story Dependencies

- **US1 (P1) - Literature Review**: No dependencies - foundational section
- **US2 (P2) - Curriculum Design**: Minimal dependency on US1 (references P1 context)
- **US3 (P3) - ROS 2 Technical**: Minimal dependency on US1 (builds on ROS 2 intro from P1)
- **US4 (P4) - Simulation Comparison**: Minimal dependency on US1 (builds on simulation intro from P1)
- **US5 (P5) - AI Integration**: Minimal dependency on US1 (builds on AI intro from P1)
- **US6 (P6) - Evaluation**: Depends on US2 (references curriculum design), but can be drafted in parallel

### Parallel Opportunities

- **Phase 2 (Literature Search)**: Tasks T011-T027 can all run in parallel (independent database searches)
- **Phase 3 (US1)**: Tasks T037-T040 can run in parallel (independent subsections)
- **Phase 4 (US2)**: Tasks T049-T051 can run in parallel (independent subsections)
- **Phase 5 (US3)**: Tasks T058-T060 can run in parallel (independent subsections)
- **Phase 7 (US4)**: Tasks T074-T076 can run in parallel (independent subsections)
- **Phase 9 (US5)**: Tasks T093-T095 can run in parallel (independent subsections)
- **Phase 10 (US6)**: Tasks T102-T104 can run in parallel (independent subsections)

**Note**: In practice, for single-author research papers, "parallel" means "can be worked on in any order during a writing session" rather than truly concurrent execution.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T010)
2. Complete Phase 2: Literature Search (T011-T036) - CRITICAL prerequisite
3. Complete Phase 3: User Story 1 (T037-T048)
4. **STOP and VALIDATE**: Verify US1 meets all acceptance criteria (P1 content complete, ≥4 peer-reviewed sources, plagiarism check passed)
5. **Deliverable**: Standalone literature review section (~1,500 words, properly cited)

This MVP establishes the theoretical foundation and demonstrates feasibility.

### Incremental Delivery

1. **MVP (US1)**: Literature review complete (~1,500 words) → Foundation established
2. **+US2 (P2)**: Add curriculum design analysis (~1,200 words) → Practical contribution added
3. **+US3 (P3)**: Add ROS 2 technical depth (~1,000 words) → Technical expertise demonstrated
4. **+US4 (P4)**: Add simulation comparison (~800 words) → Comprehensive platform coverage
5. **+US5 (P5)**: Add AI integration (~700 words) → Cutting-edge content included
6. **+US6 (P6)**: Add evaluation framework (~600 words) → Paper complete with future directions
7. **Final Assembly**: Add intro/conclusion, format APA, validate gates, generate PDF

Each increment adds value and maintains coherent paper structure. Can stop at any point if word count approaches 7,000 limit.

### Sequential vs. Parallel Strategy

**Sequential (Recommended for Single Author)**:
1. Complete US1 → validate → proceed to US2
2. Complete US2 → validate → proceed to US3
3. Continue through US6
4. Less context-switching, focused writing, easier to maintain narrative flow

**Parallel (If Multiple Authors or High Confidence)**:
1. After Phase 2 (literature search), assign US2-US6 to different authors or writing sessions
2. Each user story can be drafted independently using outline.md
3. Final integration required to ensure consistent voice and transitions

---

## Notes

- **Tests**: No code tests for research paper; validation via constitutional gates (plagiarism, citations, readability)
- **Word Count Tracking**: Run `wc -w paper/*/*.md` after each phase to monitor progress
- **Citation Management**: Use Zotero throughout; do not manually type references
- **Commit Frequency**: Commit after each user story completion (T048, T057, T066, T082, T101, T110) and after major checkpoints
- **Flexibility**: If word count trending toward 7,000 limit by 75% checkpoint, condense US5-US6 or move detail to supplementary materials
- **Quality over Speed**: Better to write fewer user stories well than rush all six and fail plagiarism/readability gates

---

## Task Summary

**Total Tasks**: 162 (T001-T162)
- **Phase 1 (Setup)**: 10 tasks
- **Phase 2 (Literature Search)**: 26 tasks (foundational, blocks all user stories)
- **Phase 3 (US1 - P1)**: 12 tasks (~1,500 words)
- **Phase 4 (US2 - P2)**: 9 tasks (~1,200 words)
- **Phase 5 (US3 - P3)**: 9 tasks (~1,000 words)
- **Phase 6 (25% Checkpoint)**: 7 tasks
- **Phase 7 (US4 - P4)**: 9 tasks (~800 words)
- **Phase 8 (50% Checkpoint)**: 10 tasks
- **Phase 9 (US5 - P5)**: 9 tasks (~700 words)
- **Phase 10 (US6 - P6)**: 9 tasks (~600 words)
- **Phase 11 (75% Checkpoint)**: 11 tasks
- **Phase 12 (Final Assembly)**: 35 tasks (assembly + 5 constitutional gates validation)
- **Phase 13 (Optional)**: 6 tasks (post-submission enhancements)

**Parallel Opportunities**: 30+ tasks marked [P] across literature search and subsection drafting phases

**MVP Scope**: Phase 1-3 (48 tasks) delivers standalone literature review (~1,500 words, properly cited)

**Format Validation**: ✅ All tasks follow checklist format with checkbox, ID, optional [P] and [Story] labels, and file paths where applicable
