# Survey: From LLM Planners to Agentic Robotics

## Project Purpose

한국어/영어 이중언어 서베이 책. LLM이 로봇의 high-level planner로 등장한 시점(2022)부터 VLA, Code as Policy를 거쳐 Agentic Robotics까지의 연구 흐름을 추적한다.

**핵심 관점**: Agentic Coding(code→tool→execution→error→LLM→code)과 Agentic Robotics를 대비하며, 물리 세계에서 동일한 만족도를 달성하기 위해 극복해야 할 근본적 차이를 조명한다.

## Book Title

- KO: "LLM 플래너에서 에이전틱 로보틱스까지 — Physical AI의 미래"
- EN: "From LLM Planners to Agentic Robotics — The Future of Physical AI"

## Target Audience

로보틱스/AI 연구자 및 엔지니어. LLM과 로봇의 교차점에 관심 있는 전문가. Agentic AI를 물리 세계로 확장하려는 실무자.

## Chapter Structure (10 chapters, 4 parts)

### Part I: 기초 — LLM이 로봇을 만나다
- **Ch 1**: 서론 — Agentic Coding에서 Agentic Robotics로 (비유와 핵심 질문)
- **Ch 2**: LLM as Planner — 제로샷 계획과 그라운딩 (LLM as Planners, SayCan)
- **Ch 3**: Code as Policies — 코드로 로봇을 제어하다 (CaP, Code-as-Symbolic-Planner, CaP-X)

### Part II: VLA 혁명
- **Ch 4**: Vision-Language-Action 모델의 부상 (PaLM-E, RT-2, OpenVLA, pi0)
- **Ch 5**: 계층적 계획 — 고수준에서 저수준으로 (AutoTAMP, Hi Robot, HAMSTER, RT-H)
- **Ch 6**: 저수준 제어 — Diffusion Policy와 3D 표현 (Diffusion Policy, 3D Diffuser Actor, DROID)

### Part III: 에이전틱 로보틱스를 향하여
- **Ch 7**: 메모리와 세계 표현 (KARMA, Embodied-RAG, Scene Graph)
- **Ch 8**: 폐루프 에이전틱 시스템 (REFLECT, BUMBLE, AutoRT, PragmaBot)
- **Ch 9**: Sim-to-Real 전이와 평가 (SIMPLER, Natural Language Sim2Real)

### Part IV: 근본적 차이 — 디지털 에이전트 vs 물리 에이전트
- **Ch 10**: Agentic Coding vs Agentic Robotics — 간극과 미래 (종합 분석)

## Work Principles

- **흐름 중심**: 개별 논문 나열이 아닌 연구 흐름의 변화와 패러다임 전환을 강조
- **대비 구조**: 각 챕터에서 agentic coding의 대응 개념을 짚어 차이를 부각
- **수치 기반**: 주장은 논문의 구체적 수치와 실험 결과로 뒷받침
- **비판적 시각**: 각 접근의 한계와 미해결 문제를 명확히 지적
- **실용적 관점**: 이론뿐 아니라 실제 시스템 구현과 배포 가능성을 논의

## Key Contrasts: Agentic Coding vs Agentic Robotics

| Dimension | Agentic Coding | Agentic Robotics |
|-----------|---------------|-----------------|
| Error feedback | Stack trace, test output | Noisy sensor, partial observability |
| Execution | Deterministic, reproducible | Stochastic, irreversible |
| State representation | Code, file system, screen | Scene graph, point cloud, tactile |
| Memory | Long context, persistent files | Real-time constraint, spatial memory |
| Action space | API calls, code edits | Continuous motor commands |
| Verification | Unit tests, CI/CD | Physical trial, sim2real gap |
| Recovery | Undo, rollback | Cannot "undo" physical action |

## Harness Agents

| Agent | Role |
|-------|------|
| `deep-researcher` | 논문 심층 서베이, 연구 그룹 매핑, 인용 분석 |
| `critical-analyst` | Agentic coding vs robotics 간극 분석, 패러다임 전환 포착 |
| `book-writer` | 양국어 챕터 집필 (KO/EN) |
| `fact-checker` | 수치/인용 교차 검증 |

## Harness Skills

| Skill | Agent |
|-------|-------|
| `deep-literature-research` | deep-researcher |
| `critical-analysis` | critical-analyst |
| `expert-book-write` | book-writer |
| `fact-check` | fact-checker |
| `research-book-orchestrator` | (orchestrator) |

## Paper Sources

- Core 10 papers: `docs/robotics_vla_agentic_llm_papers.md`
- Extended curated papers: `docs/agentic_robotics_llm_vla_curated_papers_2023_2025.md`

## Directory Layout

```
book/ko/         — 한글 원고 (ch01.md ~ ch10.md, toc.md)
book/en/         — 영문 원고
book/references.bib — 통합 BibTeX
docs/            — 빌드 산출물 (정적 HTML)
_workspace/      — 에이전트 중간 산출물
assets/figures/  — 논문 figure 이미지
scripts/         — 빌드 스크립트
```

## Chapter Frontmatter

```yaml
---
chapter: N
title: "한글 제목"
subtitle: "English Subtitle"
part: "Part X: 파트명"
date: "YYYY-MM-DD"
last_updated: "YYYY-MM-DD"
---
```

## Bilingual System

- `book/ko/`, `book/en/` 별도 디렉토리 — 완전 독립 파일
- `docs/index.html`: `navigator.language` + `localStorage` 기반 자동 리다이렉트
- CSS: `body.lang-en` 클래스로 폰트 전환 (ko=Noto Sans KR, en=Inter)
- 빌드: `build_site.py`에서 ko/en 두 번 패스

## Citation Rules

- 마크다운 인용: `[Author et al., Year]` 평문
- 빌드 시 자동: `<sup><a class="cite-link" href="#chN-ref-M">[M]</a></sup>`
- 각 챕터 하단 `## 참고문헌` / `## References` 번호 리스트 필수
- 교차참조: `(→ Chapter N)` → 빌드 시 링크 변환
- `et al.` 기준: 저자 3명 이상이면 첫 저자 + et al.

## KaTeX Math

- 인라인: `$...$` → `<span class="math-inline">`
- 블록: `$$...$$` (한 줄 완결) → `<div class="math-block">`
- `$` 뒤 첫 글자가 숫자면 가격으로 판단 (수식 변환 건너뜀)
- auto-render.min.js 사용 금지 — `katex.render()`만 명시적 호출
