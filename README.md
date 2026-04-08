English | [한국어](README_ko.md)

# From LLM Planners to Agentic Robotics: The Future of Physical AI

A bilingual (Korean/English) survey book tracing the evolution from LLM-based robot planning through VLA and Code as Policy to agentic robotics — comparing agentic coding and agentic robotics to illuminate the fundamental differences in the physical world.

**First published**: 2026-04-08 | **Last updated**: 2026-04-08

## Outputs

| Output | Format | Path |
|--------|--------|------|
| Korean Book | Markdown (10 chapters) | `book/ko/` |
| English Book | Markdown (10 chapters) | `book/en/` |
| Web Viewer | Static HTML/CSS/JS (dark mode) | `docs/` |
| References | BibTeX (50+ entries) | `book/references.bib` |

## Table of Contents

### Part I: Foundations — LLM Meets Robotics
1. **Introduction** — From Agentic Coding to Agentic Robotics
2. **LLM as Planner** — Zero-Shot Planning and Grounding
3. **Code as Policies** — Programming Robot Control

### Part II: The VLA Revolution
4. **The Rise of Vision-Language-Action Models**
5. **Hierarchical Planning** — From High-Level to Low-Level
6. **Low-Level Control** — Diffusion Policy and 3D Representations

### Part III: Toward Agentic Robotics
7. **Memory and World Representation**
8. **Closed-Loop Agentic Systems**
9. **Sim-to-Real Transfer and Evaluation**

### Part IV: Fundamental Differences
10. **Agentic Coding vs Agentic Robotics** — The Gap and the Future

## Key Theme: 7-Dimension Comparison

| Dimension | Agentic Coding | Agentic Robotics |
|-----------|---------------|-----------------|
| Error Feedback | Stack trace, test output | Noisy sensor, partial observability |
| Execution | Deterministic, reproducible | Stochastic, irreversible |
| State Representation | Code, file system, screen | Scene graph, point cloud, tactile |
| Memory | Long context, persistent files | Real-time constraint, spatial memory |
| Action Space | API calls, code edits | Continuous motor commands |
| Verification | Unit tests, CI/CD | Physical trial, sim2real gap |
| Recovery | Undo, rollback | Cannot "undo" physical action |

## Tech Stack

- **Book**: Markdown with YAML frontmatter, APA citations
- **Website**: Vanilla HTML/CSS/JS, GSAP ScrollTrigger, Canvas particle background
- **Build**: `python3 build_site.py` (Markdown → HTML with citation linking)
- **Deploy**: Vercel (static)
- **Authoring**: Claude Code agent team (deep-researcher, critical-analyst, book-writer, fact-checker)

## Local Development

```bash
# View website locally
cd docs && python3 -m http.server 8000
# → http://localhost:8000

# Rebuild HTML from markdown
python3 build_site.py
```

## Project Structure

```
├── book/
│   ├── ko/          # Korean chapters (ch01-ch10, toc)
│   ├── en/          # English chapters (ch01-ch10, toc)
│   └── references.bib
├── docs/            # Static website (Vercel)
│   ├── ko/          # Korean pages
│   ├── en/          # English pages
│   ├── css/         # Dark mode glassmorphism styles
│   └── js/          # Particles, GSAP, shared header
├── assets/figures/  # Paper figures
├── build_site.py    # Markdown → HTML builder
├── _workspace/      # Agent intermediate outputs
└── .claude/         # Agent definitions + skills (harness)
    ├── agents/      # 4 agents (researcher, analyst, writer, checker)
    └── skills/      # 5 skills (research, analysis, writing, checking, orchestrator)
```

## Contributors

> Sorted by contribution amount. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute.

<!-- CONTRIBUTORS-START -->
| Avatar | Contributor | Contributions |
|:------:|:-----------:|:-------------|
| <img src="https://github.com/revfactory.png" width="50"> | [@revfactory](https://github.com/revfactory) | :wrench: [Harness](https://github.com/revfactory/harness) agent framework, :art: [Web design](https://github.com/revfactory/ai-trend-onboarding) patterns |
| <img src="https://github.com/sjchoi86.png" width="50"> | [@sjchoi86](https://github.com/sjchoi86) | :bulb: Inspiration and seminar reference papers for agentic robotics survey |
<!-- CONTRIBUTORS-END -->

## Acknowledgment

This project was built using [Harness](https://github.com/revfactory/harness) (Apache 2.0) by Minho Hwang. The website structure was adapted from [AI Trend Onboarding](https://github.com/revfactory/ai-trend-onboarding) ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)) by Minho Hwang — the design, layout patterns, and agent architecture were modified for this project's domain. Special thanks to Minho Hwang for creating these excellent tools.

This survey was inspired by the seminar presentation of Chanwoo Kim (PhD candidate, Korea University), and the reference papers from his seminar formed the foundation of this work. Special thanks to Prof. Sungjoon Choi (Korea University) and Chanwoo Kim for their invaluable contributions to the initial paper curation and research direction.

AI tools were used in the production of this work: Claude (Opus 4.6) for literature survey, content generation, and manuscript preparation.

## License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). You are free to share and adapt the material for non-commercial purposes with attribution. See [LICENSE](LICENSE) for details.
