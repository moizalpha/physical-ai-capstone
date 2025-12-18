# Research Strategy: Physical AI Capstone Quarter Paper

**Phase**: 0 (Research & Source Identification)
**Date**: 2025-12-17
**Purpose**: Systematically identify and evaluate sources for all user stories (P1-P6), ensuring constitutional compliance with peer-reviewed source requirements

## Research Questions

### Primary Research Questions
1. **What is Physical AI and how has it evolved from traditional robotics?** (P1)
2. **What are the key architectural components of ROS 2 and how do they support humanoid robotics?** (P1, P3)
3. **What pedagogical approaches are most effective for teaching robotics and embodied AI?** (P2)
4. **How do Gazebo, Unity, and NVIDIA Isaac compare for robotics simulation?** (P1, P4)
5. **What are the state-of-the-art approaches for AI-robot integration (VSLAM, VLA, multi-modal perception)?** (P5)
6. **How can robotics curricula be evaluated for effectiveness?** (P6)

### Secondary Research Questions
7. What are the performance benchmarks for ROS 2 middleware? (P3)
8. What are the sim-to-real transfer challenges in robotics simulation? (P4)
9. How have LLMs been integrated with robotic systems for natural interaction? (P5)
10. What are the implementation barriers for Physical AI education in academic settings? (P6)

## Literature Search Strategy

### Phase 0.1: Peer-Reviewed Source Identification (Priority)

**Target**: Identify ≥10 peer-reviewed sources initially (exceeds 8 minimum; provides buffer)

#### Search Query Templates

**Database: IEEE Xplore**
- Query 1: `("Physical AI" OR "embodied AI" OR "embodied intelligence") AND robotics`
- Query 2: `"ROS 2" AND (middleware OR architecture OR "DDS")`
- Query 3: `robotics AND simulation AND (Gazebo OR "Isaac Sim")`
- Query 4: `"VSLAM" OR "visual SLAM" AND robotics AND navigation`
- Query 5: `"vision language action" OR "VLA" AND robotics`
- Filters: Conferences (ICRA, IROS, RSS, Humanoids), Journals (T-RO, RA-L)
- Date Range: 2020-2025 (prefer recent; foundational works can be older)

**Database: ACM Digital Library**
- Query 1: `robotics AND education AND curriculum`
- Query 2: `"project-based learning" AND engineering AND robotics`
- Query 3: `ROS AND middleware AND performance`
- Filters: Journals (TOCE, SIGCSE), Conferences (SIGCSE, ITiCSE, FIE)
- Date Range: 2018-2025

**Database: ScienceDirect (Education Focus)**
- Query 1: `robotics education AND pedagogy AND "hands-on"`
- Query 2: `"constructivist learning" AND engineering education`
- Query 3: `STEM education AND robotics AND assessment`
- Filters: Journals in Education, Computer Science, Engineering
- Date Range: 2019-2025

**Database: Google Scholar (Broad Coverage)**
- Query 1: `"Physical AI" OR "embodied AI" filetype:pdf`
- Query 2: `ROS2 architecture DDS middleware performance`
- Query 3: `Unity robotics simulation "digital twin"`
- Query 4: `NVIDIA Isaac Sim synthetic data robotics`
- Query 5: `RT-1 RT-2 vision language action robotics`
- Filters: Sort by relevance, check "cited by" counts, verify peer-review status
- Date Range: 2020-2025

#### Peer-Reviewed Source Allocation by User Story

- **P1 (Literature Review)**: 4-5 peer-reviewed sources
  - Physical AI definitions and evolution: 1-2 sources
  - ROS 2 architecture and middleware: 1 source
  - Simulation technologies (Gazebo, Isaac): 1 source
  - Robotics education overview: 1 source

- **P2 (Curriculum Design)**: 2-3 peer-reviewed sources
  - Educational theory (cognitive load, scaffolding, PBL): 1-2 sources
  - Robotics curriculum case studies: 1 source

- **P3 (ROS 2 Technical)**: 1-2 peer-reviewed sources
  - ROS 2 middleware performance: 1 source
  - URDF and robot modeling: 1 source (or reference textbook)

- **P4 (Simulation Comparison)**: 1 peer-reviewed source
  - Simulation benchmarking or sim-to-real transfer: 1 source

- **P5 (AI Integration)**: 2-3 peer-reviewed sources
  - VSLAM algorithms (ORB-SLAM3, etc.): 1 source
  - VLA models (RT-1, RT-2, etc.): 1-2 sources

- **P6 (Evaluation)**: 1 peer-reviewed source
  - Curriculum evaluation frameworks: 1 source

**Total Peer-Reviewed Target**: 11-15 sources (exceeds 8 minimum)

### Phase 0.2: Technical Documentation Sources (Up to 50%)

**Target**: Identify 5-7 authoritative technical documentation sources

#### Primary Technical Sources

1. **ROS 2 Documentation** (docs.ros.org)
   - ROS 2 Design Documents
   - rclpy API Reference
   - URDF XML Specification
   - Version: ROS 2 Humble (LTS) or Rolling
   - Citation: Open Robotics (2025). ROS 2 Documentation. https://docs.ros.org/

2. **NVIDIA Isaac Documentation**
   - Isaac Sim User Manual
   - Isaac ROS Developer Guide
   - Omniverse Platform Documentation
   - Version: Isaac Sim 2023.1.1 or later
   - Citation: NVIDIA Corporation (2025). NVIDIA Isaac Platform Documentation.

3. **Gazebo Documentation**
   - Gazebo Classic vs. Gazebo (Ignition/Gz) comparison
   - ros_gz_bridge Integration Guide
   - Physics Engine Configuration
   - Version: Gazebo Fortress or Garden
   - Citation: Open Robotics (2025). Gazebo Simulation Documentation.

4. **Unity Robotics Hub**
   - Unity Robotics Hub GitHub Repository
   - ROS-TCP-Connector Documentation
   - URDF Importer Guide
   - Version: Unity 2022 LTS
   - Citation: Unity Technologies (2024). Unity Robotics Hub. https://github.com/Unity-Technologies/Unity-Robotics-Hub

5. **OpenAI Whisper** (if discussing speech processing)
   - OpenAI Whisper Technical Report
   - Model Architecture and Performance
   - Citation: Radford, A., et al. (2022). Robust Speech Recognition via Large-Scale Weak Supervision. OpenAI.

6. **DDS Middleware Standards** (if discussing ROS 2 internals)
   - OMG DDS Specification
   - RTI Connext, eProsima Fast DDS documentation
   - Citation: Object Management Group (OMG). Data Distribution Service (DDS) Specification.

7. **ABET Criteria** (for engineering education standards)
   - ABET Accreditation Criteria for Computer Science and Engineering
   - Citation: ABET (2024). Criteria for Accrediting Computing Programs.

#### Source Selection Criteria

**Peer-Reviewed Sources Must**:
- ✅ Appear in recognized conference proceedings or journals
- ✅ Have clear author affiliations and publication dates
- ✅ Provide DOI or stable URL
- ✅ Present original research, systematic reviews, or pedagogical studies

**Technical Documentation Must**:
- ✅ Come from authoritative sources (Open Robotics, NVIDIA, Unity, OpenAI, OMG)
- ✅ Specify version numbers and publication/update dates
- ✅ Be publicly accessible (no paywalls for core documentation)
- ✅ Provide stable URLs or archivable links

**Reject**:
- ❌ Blog posts without institutional backing (unless exceptional and clearly marked)
- ❌ Wikipedia or crowdsourced wikis (use only for initial exploration, not citation)
- ❌ Preprints without peer review (arXiv acceptable only if no peer-reviewed alternative exists)
- ❌ Marketing materials or product brochures (technical whitepapers acceptable if substantial)

## Source Tracking and Organization

### Citation Management Setup

**Tool Recommendation**: Zotero (free, open-source, excellent APA 7th support)

**Workflow**:
1. Create Zotero library: "Physical AI Capstone Paper"
2. Create collections by user story:
   - P1_Literature_Review
   - P2_Curriculum_Design
   - P3_ROS2_Technical
   - P4_Simulation_Comparison
   - P5_AI_Integration
   - P6_Evaluation_Framework
3. Import sources with browser connector or DOI
4. Tag sources: `peer-reviewed`, `technical-doc`, `ros2`, `simulation`, `education`, etc.
5. Export to BibTeX for Pandoc or Word bibliography

### Source Inventory Template

For each identified source, record:

```markdown
## Source ID: [P#-##] (e.g., P1-01)

**Title**: [Full title]
**Authors**: [Author list]
**Publication**: [Journal/Conference/Publisher]
**Year**: [Publication year]
**Type**: [Peer-Reviewed / Technical Documentation / Book / White Paper]
**DOI/URL**: [Stable identifier]
**Relevance**: [Which user story(ies) and specific claims this source supports]
**Key Findings**: [2-3 sentence summary of relevant content]
**Citation Status**: [Not Yet Cited / Cited in Draft / Included in References]
```

### Minimum Source Inventory (Constitutional Compliance)

**Checkpoint at End of Phase 0**:
- [ ] **Total Sources**: ≥15 identified
- [ ] **Peer-Reviewed**: ≥8 identified (journal articles, conference papers, academic books)
- [ ] **Technical Docs**: 5-7 authoritative documentation sources
- [ ] **Source Diversity**: Coverage across all 6 user stories
- [ ] **Accessibility**: All sources accessible (institutional access, open access, or public docs)
- [ ] **Currency**: Prefer sources from 2020-2025; foundational works may be older
- [ ] **Zotero Setup**: All sources imported with complete metadata

## Research Findings and Decisions

### Decision Log Format

For each research question requiring a decision:

```markdown
### Decision: [What was chosen]

**Research Question**: [Which RQ this addresses]
**Options Considered**:
- Option A: [description]
- Option B: [description]

**Rationale**: [Why chosen option selected, supported by sources]
**Supporting Sources**: [P#-## citations]
**Alternatives Rejected**: [Why other options not pursued]
**Implications**: [How this decision affects paper content or structure]
```

### Example Decision (Placeholder - to be filled during research execution)

### Decision: Define "Physical AI" as AI systems with embodied interaction in physical environments

**Research Question**: RQ1 - What is Physical AI and how has it evolved?
**Options Considered**:
- Option A: Use "embodied AI" terminology (established in cognitive science literature)
- Option B: Use "Physical AI" terminology (emerging in robotics and AI communities)
- Option C: Use both terms interchangeably with clear definition

**Rationale**: "Physical AI" emphasizes real-world interaction and physical laws comprehension, distinguishing it from purely simulated embodied agents. Emerging usage in industry (NVIDIA, robotics startups) and alignment with curriculum title. Will define on first use with reference to embodied AI lineage.

**Supporting Sources**: [To be identified - expecting sources from ICRA, IROS, or recent survey papers]
**Alternatives Rejected**: "Embodied AI" alone may be too broad (includes VR agents); "Physical AI" better scopes to robotics context
**Implications**: Introduction and P1 will establish terminology with citations tracing evolution from traditional robotics → embodied AI → Physical AI

---

## Research Execution Checklist

**Phase 0 Deliverables**:
- [ ] Execute all search queries across IEEE Xplore, ACM DL, ScienceDirect, Google Scholar
- [ ] Identify ≥15 total sources (≥8 peer-reviewed, 5-7 technical docs)
- [ ] Import all sources to Zotero with complete metadata
- [ ] Fill source inventory for each identified source
- [ ] Document key decisions with supporting citations
- [ ] Verify all URLs/DOIs functional
- [ ] Tag sources by user story and topic
- [ ] Export initial bibliography to BibTeX
- [ ] Validate: Peer-reviewed percentage ≥50% (Principle III compliance)
- [ ] Validate: All sources accessible and verifiable (Principle I compliance)

**Estimated Time**: 8-12 hours of focused literature search and source evaluation

**Output**: research.md (this file) with complete source inventory and decision log, plus Zotero library ready for citation

**Next Phase**: Phase 1 (data-model.md, outline.md, quickstart.md) will structure content based on identified sources
