# Phase 3 Consistency Check

> 2026-04-08 | Critical Analyst

## 1. 논문 커버리지 확인

### Core 10 Papers (docs/robotics_vla_agentic_llm_papers.md)

| # | 논문 | toc.md | researcher | analyst | references.bib |
|---|------|--------|-----------|---------|---------------|
| 1 | LLM as Planners (2022) | Ch 2.2 | 01_llm_planner | gap/paradigm | huang2022llmplanners |
| 2 | SayCan (2022) | Ch 2.3 | 01_llm_planner | gap/paradigm/connections | ahn2022saycan |
| 3 | CaP (2022) | Ch 3.2 | 01_code_policy | gap/paradigm/connections | liang2022cap |
| 4 | REFLECT (2023) | Ch 8.2 | (agentic 서베이 진행중) | gap/connections | liu2023reflect |
| 5 | AutoTAMP (2023) | Ch 5.2 | 01_hierarchy | connections | chen2023autotamp |
| 6 | AutoRT (2024) | Ch 8.3 | (agentic 서베이 진행중) | gap/paradigm/open_problems | brohan2024autort |
| 7 | BUMBLE (2024) | Ch 8.4 | (agentic 서베이 진행중) | gap/paradigm/open_problems | garrett2024bumble |
| 8 | Code-as-Symbolic-Planner (2025) | Ch 3.3 | 01_code_policy | paradigm/connections | chen2025codesymbolic |
| 9 | PragmaBot (2025) | Ch 8.5 | (agentic 서베이 진행중) | gap/paradigm | pragmabot2025 |
| 10 | CaP-X (2026) | Ch 3.4 | 01_code_policy | paradigm/connections | fu2026capx |

**상태**: 10/10 핵심 논문 모두 toc, analyst, references.bib에 포함. Researcher 서베이 중 #4,6,7,9는 Task #6(Agentic Systems) 진행 중.

### Curated Papers (docs/agentic_robotics_llm_vla_curated_papers_2023_2025.md)

**[S] 등급 논문 커버리지**:

| 논문 | toc.md | references.bib |
|------|--------|---------------|
| PaLM-E | Ch 4.2 | driess2023palme |
| RT-2 | Ch 4.3 | brohan2023rt2 |
| Open X-Embodiment | Ch 4.4 | oxe2023 |
| Octo | Ch 4.5 | ghosh2024octo |
| OpenVLA | Ch 4.6 | kim2024openvla |
| pi0 | Ch 4.7 | black2024pi0 |
| Diffusion Policy | Ch 6.2 | chi2023diffusionpolicy |
| DROID | Ch 6.4 | khazatsky2024droid |
| KARMA | Ch 7.2 | wang2024karma |
| Embodied-RAG | Ch 7.3 | xie2024embodiedrag |
| RoboEXP | Ch 7.4 | jiang2024roboexp |
| SIMPLER | Ch 9.2 | li2024simpler |
| SayPlan | Ch 2.4 | rana2023sayplan |
| AutoTAMP | Ch 5.2 | chen2023autotamp |
| Code-as-Symbolic-Planner | Ch 3.3 | chen2025codesymbolic |
| TAMP+LLM (Object Rearrangement) | 언급 | ding2023tamprearrange |

**상태**: [S] 등급 16편 모두 커버.

**[A] 등급 논문 커버리지**:

| 논문 | toc.md | references.bib |
|------|--------|---------------|
| RT-H | Ch 5.3 | belkhale2024rth |
| Hi Robot | Ch 5.4 | shi2025hirobot |
| HAMSTER | Ch 5.5 | li2025hamster |
| pi0.5 | Ch 4.7 | pi05_2025 |
| GR00T N1 | Ch 4.8 | nvidia2025groot |
| FAST | Ch 6.6 | kim2025fast |
| 3D Diffuser Actor | Ch 6.3 | ke2024diffuseractor |
| VeriGraph | Ch 7.5 | ekpo2024verigraph |
| MoMa-LLM | Ch 7.6 | lang2024momallm |
| NL Sim2Real | Ch 9.3 | yu2024nlsim2real |
| What Matters in VLA | Ch 4.10 | pertsch2024whatmatters |
| NLaP | Ch 3 (언급) | mikami2024nlap |
| Bridging Sim2Real | Ch 9.4 | hansen2025sim2real |

**상태**: [A] 등급 13편 모두 커버.

**[B] 등급 논문 커버리지**:

| 논문 | toc.md | references.bib |
|------|--------|---------------|
| TinyVLA | Ch 6.5 | wu2024tinyvla |
| RL-GPT | Ch 3.5 | liu2024rlgpt |
| 3D-Mem | Ch 7.6 | 3dmem2024 |
| RoboMemory | Ch 7.6 | robomemory2025 |
| LLM-Embodied Agent | Ch 7.6 | llmembodied2025 |
| Sim-to-Real RL Survey | 참조 | sim2rlsurvey2025 |

**상태**: [B] 등급 6편 모두 커버.

---

## 2. toc.md KO/EN 일관성 확인

| 항목 | KO | EN | 일치 |
|------|----|----|------|
| 챕터 수 | 10 | 10 | OK |
| Part 수 | 4 | 4 | OK |
| 섹션 번호 체계 | N.M 형식 | N.M 형식 | OK |
| 논문 인용 형식 | [Author et al., Year] | [Author et al., Year] | OK |
| Ch 10 구조 | 7대 차원 + 패러다임 + 미해결 + 미래 | 동일 | OK |

---

## 3. Analyst 산출물 간 일관성 확인

### 02_analyst_gap_analysis.md ↔ 02_analyst_open_problems.md

| gap_analysis 차원 | open_problems 대응 | 일관성 |
|-----------------|-------------------|-------|
| Error Feedback (★5) | 문제 1: 물리적 피드백 의미 변환 [근본적] | OK |
| Execution Determinism (★4) | 문제 2,6에 반영 | OK |
| State Representation (★4) | 문제 2: 세계 모델에 포함 | OK |
| Memory Architecture (★3) | 문제 4: Long-horizon에 포함 | OK |
| Action Space (★4) | 문제 3,7에 반영 | OK |
| Verification (★5) | 문제 8: 평가 표준 부재 | OK |
| Recoverability (★5) | 문제 5: Safety-Autonomy 균형 | OK |

### 02_analyst_paradigm_shifts.md ↔ 02_analyst_paper_connections.md

| paradigm_shifts 전환 | paper_connections 흐름 | 일관성 |
|---------------------|---------------------|-------|
| 전환 1 (LLM Planner) | Flow 3: Grounding & Planning | OK |
| 전환 2 (Multimodal VLA) | Flow 2: VLA 메인스트림 | OK |
| 전환 3 (Open VLA) | Flow 2 하위 | OK |
| 전환 4 (Agentic Closed-Loop) | Flow 4: Agentic Closed-Loop | OK |
| Code-as-Policy 계보 | Flow 1: Code-as-Policy | OK |

---

## 4. Researcher ↔ Analyst 교차 검증

### 수치 일관성

| 수치 | Researcher 출처 | Analyst 사용 | 일치 |
|------|---------------|-------------|------|
| SayCan PaLM 84% | 01_llm_planner | gap_analysis | OK |
| LLM Planners Exec 79% | 01_llm_planner | paradigm_shifts | OK |
| OpenVLA +16.5% vs RT-2-X | 01_vla | paradigm_shifts | OK |
| CaP-Symbolic +24.1% | 01_code_policy | gap_analysis | OK |
| KARMA Complex 2.3x/62.7x | 01_memory | gap_analysis | OK |
| VeriGraph +58%/+30% | 01_memory | gap_analysis | OK |
| HAMSTER +20% vs OpenVLA | 01_hierarchy | gap_analysis | OK |
| Diffusion Policy +46.9% avg | 01_vla | toc.md | OK |

---

## 5. 누락/불일치 항목

### 5.1 Researcher Task #6 (Agentic Systems & Sim2Real) 미완료
- **영향**: REFLECT, AutoRT, BUMBLE, PragmaBot, SIMPLER의 상세 서베이가 아직 없음
- **현재 대응**: Analyst가 docs/ 기반으로 초기 분석을 수행. researcher 완료 시 보강 필요
- **상태**: Task #6 in_progress (deep-researcher)

### 5.2 Researcher Task #7 (연구 그룹 매핑) 미완료
- **영향**: 02_analyst_paper_connections.md의 연구 그룹 섹션이 약식
- **현재 대응**: 각 researcher 서베이의 연구 그룹 매핑을 참조하여 기본 정보 포함
- **상태**: Task #7 pending

### 5.3 references.bib 저자 정보 불완전
- 일부 BibTeX 엔트리에서 `others`로 축약된 저자 목록이 있음
- 최종 출판 전에 전체 저자 목록으로 보완 필요
- **우선순위**: 낮음 (빌드 단계에서 보완)

---

## 6. 종합 판정

| 항목 | 상태 |
|------|------|
| Core 10 논문 커버리지 | **완전** (10/10) |
| [S] 등급 논문 커버리지 | **완전** (16/16) |
| [A] 등급 논문 커버리지 | **완전** (13/13) |
| [B] 등급 논문 커버리지 | **완전** (6/6) |
| toc.md KO/EN 구조 일치 | **일치** |
| Analyst 산출물 간 일관성 | **일관** |
| Researcher ↔ Analyst 수치 | **일치** (8/8 확인) |
| references.bib 완전성 | **기본 완전** (저자 약식 일부 존재) |
| 누락 서베이 | Task #6, #7 진행/대기 중 |

**결론**: Phase 3 통합은 현재 가용 데이터 기준으로 **완전하고 일관적**. Task #6, #7 완료 후 Agentic Systems 챕터(Ch 8, 9)와 연구 그룹 매핑 보강 필요.
