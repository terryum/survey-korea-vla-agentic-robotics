# 연구 그룹 매핑 & 시간축 흐름 — 종합 서베이

> 이 문서는 2022-2026년 LLM/VLA/Agentic Robotics 연구의 그룹별 기여와 시간축 흐름을 정리한다.

---

## 1. 핵심 연구 그룹 매핑

### 1.1 Google DeepMind / Google Research (Robotics)

**핵심 인물**: Michael Ahn, Anthony Brohan, Fei Xia, Wenlong Huang, Karol Hausman (→ Physical Intelligence), Brian Ichter (→ Physical Intelligence), Pete Florence, Andy Zeng, Danny Driess

**논문 흐름**:
```
SayCan (2022.04) → PaLM-E (2023.03) → RT-2 (2023.07)
    │                                       │
Code as Policies (2022.09)            RT-H (2024.03)
    │                                       │
AutoRT (2024.01)                    Open X-Embodiment (2023.10)
```

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| SayCan | 2022 | Affordance grounding (Say + Can) |
| Code as Policies | 2022 | 코드 기반 로봇 제어 패러다임 |
| PaLM-E | 2023 | 562B 멀티모달 embodied LM |
| RT-2 | 2023 | VLA 개념 확립, web→robot 전이 |
| Open X-Embodiment | 2023 | 1M+ 궤적, cross-embodiment 데이터 |
| RT-H | 2024 | Language motion hierarchy |
| AutoRT | 2024 | 대규모 로봇 관리 + Robot Constitution |

**특징**: 대규모 모델 + 대규모 데이터 + 대규모 인프라. VLA 개념의 원조. 2024년 핵심 인력의 Physical Intelligence 이직으로 연구 방향 변화 가능.

---

### 1.2 Physical Intelligence (π)

**핵심 인물**: Karol Hausman (CEO, ex-Google), Sergey Levine (Chief Scientist, UC Berkeley), Chelsea Finn (Research Lead, Stanford), Brian Ichter (ex-Google), Kevin Black

**창립**: 2024년
**자금**: $70M seed (2024.03) → $400M Series A (2024.11, $2.4B 기업가치) → $600M Series B (2025.11, $5.6B 기업가치) → 총 $1.1B+
**주요 투자자**: OpenAI, Jeff Bezos, Thrive Capital, Lux Capital, Sequoia Capital, NVIDIA NVentures

**논문 흐름**:
```
π0 (2024.10) → FAST (2025.01) → π0.5 (2025.04)
                                      │
                                Hi Robot (2025.02)
```

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| π0 | 2024 | Flow matching VLA, dexterous 조작 |
| FAST | 2025 | DCT 기반 action tokenization, 5x 학습 가속 |
| π0.5 | 2025 | Open-world generalization |
| Hi Robot | 2025 | 계층적 VLA, 인간 피드백 통합 |

**특징**: Google DeepMind에서 분사한 핵심 인력이 주도. Flow matching 기반 VLA에 집중. 상용화 지향. 가장 강력한 자금력 ($1.1B+).

---

### 1.3 UC Berkeley (RAIL Lab, BAIR)

**핵심 인물**: Sergey Levine (겸 Physical Intelligence), Pieter Abbeel, Karl Pertsch, Moo Jin Kim

**논문 흐름**:
```
LLM as Planners (2022.01)
    │
DROID (2024.03) → Octo (2024.05) → OpenVLA (2024.06)
```

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| LLM as Planners | 2022 | LLM 로봇 계획의 기점 |
| DROID | 2024 | 76K 궤적, 564 씬, in-the-wild 데이터셋 |
| Octo | 2024 | 오픈소스 generalist policy 기준점 |
| OpenVLA | 2024 | 7B 오픈소스 VLA, RT-2-X +16.5% |

**특징**: 오픈소스 생태계의 핵심 주도자. DROID 데이터셋 + Octo/OpenVLA 모델로 커뮤니티 기반 구축. 학술-실무 연결 강점.

---

### 1.4 Stanford University

**핵심 인물**: Chelsea Finn (겸 Physical Intelligence), Dorsa Sadigh, Shuran Song

**논문 흐름**:
```
Code as Policies (2022.09, Google와 공동)
    │
REFLECT (2023.06)
    │
OpenVLA (2024.06, Berkeley와 공동)
    │
CaP-X (2026.03, Microsoft와 공동)
```

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| REFLECT | 2023 | 실패 분석 프레임워크 |
| OpenVLA | 2024 | 오픈소스 VLA (Berkeley와 공동) |
| CaP-X | 2026 | Code as Policy 벤치마크 |

**특징**: 다양한 그룹과의 협력 연구 강점. 벤치마크와 오픈소스 기여. Physical Intelligence와 이중 소속.

---

### 1.5 MIT REALM Lab

**핵심 인물**: Chuchu Fan, Yongchao Chen

**논문 흐름**:
```
AutoTAMP (2023.06) → Code-as-Symbolic-Planner (2025.03)
```

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| AutoTAMP | 2023 | LLM을 translator+checker로 활용 |
| Code-as-Symbolic-Planner | 2025 | 코드를 solver/planner/checker로 확장 |

**특징**: 형식 검증(formal verification) + LLM 결합. "코드를 추론 도구로" 패러다임. 안전성과 정확성 중시.

---

### 1.6 NVIDIA

**핵심 인물**: NVIDIA Isaac 팀

**논문 흐름**:
```
GR00T N1 (2025.03)
```

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| GR00T N1 | 2025 | Dual-system VLA, humanoid, 오픈소스 |

**특징**: 하드웨어(GPU)+시뮬레이션(Isaac Sim)+모델(GR00T N1) 수직 통합. Humanoid 초점. 합성 데이터 강점.

---

### 1.7 QUT (Queensland University of Technology)

**핵심 인물**: Krishan Rana, Niko Sünderhauf

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| SayPlan | 2023 | 3D 씬 그래프 + LLM 계획 |

**특징**: 대규모 환경에서의 씬 그래프 기반 계획. 호주 기반.

---

### 1.8 CMU (Carnegie Mellon University)

**핵심 인물**: Ruslan Salakhutdinov, Yonatan Bisk

| 논문 | 연도 | 핵심 기여 |
|------|-----|---------|
| Embodied-RAG | 2024 | 물리 세계 RAG |
| Octo | 2024 | (Berkeley와 공동) |

**특징**: 기억/검색 시스템의 물리 세계 확장.

---

## 2. 그룹 간 인력 이동 맵

```
Google DeepMind ──(2024)──→ Physical Intelligence
  Karol Hausman (CEO)
  Brian Ichter
  
UC Berkeley ←────(겸직)────→ Physical Intelligence
  Sergey Levine (Chief Scientist)
  
Stanford ←────(겸직)────→ Physical Intelligence
  Chelsea Finn (Research Lead)

UC Berkeley ←───(공동연구)───→ Stanford
  OpenVLA, DROID, Octo

Stanford ←───(공동연구)───→ Microsoft
  CaP-X
```

**핵심 관찰**: Physical Intelligence는 Google DeepMind + UC Berkeley + Stanford의 핵심 인력을 흡수하여 형성. 이는 학술(개방형 연구) → 산업(상용화)으로의 인재 이동 패턴을 보여주며, OpenVLA/Octo 같은 오픈소스 프로젝트와 π0 같은 비공개 프로젝트 사이의 긴장을 만든다.

---

## 3. 시간축 흐름 (2022-2026)

### 3.1 연도별 패러다임 전환

```
2022 ─── "LLM이 로봇을 계획할 수 있다" ────────────────────────
  │   LLM as Planners (2022.01) — 최초 입증
  │   SayCan (2022.04) — affordance grounding
  │   Code as Policies (2022.09) — 코드 생성 패러다임
  │
2023 ─── "VLM이 로봇을 직접 제어할 수 있다" ──────────────────
  │   PaLM-E (2023.03) — 멀티모달 embodied LM
  │   Diffusion Policy (2023.03) — 확산 기반 저수준 정책
  │   AutoTAMP (2023.06) — LLM as translator+checker
  │   REFLECT (2023.06) — 실패 분석 프레임워크
  │   SayPlan (2023.07) — 3D 씬 그래프 + LLM
  │   RT-2 (2023.07) — ★ VLA 개념 확립
  │   Open X-Embodiment (2023.10) — cross-embodiment 데이터
  │
2024 ─── "오픈소스 VLA와 에이전틱 시스템의 출현" ──────────────
  │   AutoRT (2024.01) — 대규모 로봇 관리
  │   RoboEXP (2024.02) — action-conditioned 씬 그래프
  │   RT-H (2024.03) — language hierarchy
  │   DROID (2024.03) — 76K 궤적 in-the-wild 데이터
  │   SIMPLER (2024.05) — 시뮬레이션 평가 프레임워크
  │   Octo (2024.05) — 오픈소스 generalist policy
  │   OpenVLA (2024.06) — ★ 7B 오픈소스 VLA
  │   TinyVLA (2024.09) — <1B 경량 VLA
  │   KARMA (2024.09) — 장기/단기 기억 시스템
  │   Embodied-RAG (2024.09) — 물리 세계 RAG
  │   π0 (2024.10) — ★ flow matching VLA
  │   BUMBLE (2024.10) — 건물 규모 에이전틱 시스템
  │   VeriGraph (2024.11) — 검증용 씬 그래프
  │
2025 ─── "open-world, 계층적, 경험 학습" ──────────────────────
  │   FAST (2025.01) — DCT action tokenization
  │   HAMSTER (2025.02) — 계층적 VLA + off-domain 데이터
  │   Hi Robot (2025.02) — 계층적 VLA + 인간 피드백
  │   Code-as-Symbolic-Planner (2025.03) — 코드=추론도구
  │   GR00T N1 (2025.03) — ★ dual-system humanoid VLA
  │   π0.5 (2025.04) — ★ open-world generalization
  │   PragmaBot (2025.07) — 경험 기반 에이전틱 학습
  │
2026 ─── "벤치마크화와 산업 적용" ────────────────────────────
      CaP-X (2026.03) — ★ 에이전틱 코딩 에이전트 벤치마크
```

### 3.2 네 번의 패러다임 전환

| 전환 | 시기 | 핵심 논문 | 의미 |
|------|-----|----------|------|
| **1차: LLM→Robot** | 2022.01~04 | LLM as Planners, SayCan | LLM의 세계 지식을 로봇에 활용 가능 |
| **2차: VLA 확립** | 2023.03~07 | PaLM-E, RT-2 | VLM이 직접 로봇 행동을 출력 |
| **3차: 오픈소스 VLA** | 2024.05~10 | OpenVLA, Octo, π0 | 커뮤니티 접근 가능한 VLA 생태계 |
| **4차: Agentic+Open-world** | 2025.02~07 | π0.5, Hi Robot, PragmaBot | 경험 학습 + open-world + 인간 피드백 |

### 3.3 기술 스택의 수렴

2025-2026년에 관찰되는 수렴 방향:

```
         VLA 메인스트림          계층적 접근           에이전틱 루프
              │                     │                     │
              └─────────┬───────────┘                     │
                        │                                 │
                  Dual-System VLA                         │
              (GR00T N1, Hi Robot)                        │
                        │                                 │
                        └──────────────┬──────────────────┘
                                       │
                              Agentic VLA System
                        (관찰+계획+실행+검증+기억+학습)
```

---

## 4. 핵심 데이터셋 흐름

| 데이터셋 | 연도 | 규모 | 특징 | 활용 |
|---------|-----|------|------|------|
| RT-1 Data | 2022 | ~130K 에피소드 | Google 로봇, 주방 | SayCan, RT-1, RT-2 |
| Open X-Embodiment | 2023 | **1M+ 궤적, 22 로봇** | Cross-embodiment | Octo, OpenVLA |
| DROID | 2024 | **76K 궤적, 564 씬** | In-the-wild, 다대륙 | Octo, OpenVLA |
| AutoRT Data | 2024 | **77K 시연** | 자율 수집, 4 건물 | 로봇 학습 |
| π0 Data | 2024 | 비공개 | 7 로봇 구성, 68 작업 | π0, π0.5 |
| FAST+ | 2025 | **1M 궤적** | 범용 action tokenizer | FAST+ |

---

## 5. 경쟁과 협력의 역학

### 5.1 오픈소스 vs 비공개

| 진영 | 대표 | 모델 공개 | 데이터 공개 |
|------|-----|---------|-----------|
| **오픈소스** | Berkeley(OpenVLA, Octo, DROID), NVIDIA(GR00T N1) | ✓ | ✓ |
| **비공개** | Physical Intelligence(π0, π0.5) | ✗ | ✗ |
| **하이브리드** | Google(RT-2 비공개, OXE 공개) | 일부 | 일부 |

### 5.2 학술 vs 산업

- **학술 주도**: 2022-2023 (LLM as Planners, SayCan, CaP, SayPlan → 대학 주도)
- **산업 주도**: 2024-2026 (Physical Intelligence $1.1B, NVIDIA GR00T → 기업 주도)
- **핵심 긴장**: 오픈소스 연구의 재현성 vs 상용화를 위한 비공개

---

## 6. 지역별 분포

| 지역 | 그룹 | 강점 |
|------|-----|------|
| **미국 (Bay Area)** | Google, Physical Intelligence, Stanford, Berkeley | VLA 메인스트림, 자금력 |
| **미국 (동부)** | MIT REALM, CMU, Columbia | 형식 검증, 메모리, 실패 분석 |
| **미국 (기타)** | UT Austin, UC San Diego | Sim2Real, 평가 |
| **호주** | QUT | 씬 그래프 기반 계획 |
| **유럽** | (DROID 데이터 수집 참여) | 데이터 기여 |
| **동아시아** | (DROID 데이터 수집 참여), TinyVLA | 경량화 VLA |

---

*작성일: 2026-04-08*
*서베이 범위: 2022.01 ~ 2026.03*
