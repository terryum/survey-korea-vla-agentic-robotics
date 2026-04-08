# 논문 간 영향 관계 맵

> Critical Analyst 산출물 | 2026-04-08
> Core 10 papers + Curated 40+ papers의 인용/영향 관계 분석

---

## 1. 핵심 흐름 다이어그램

```
                    ┌─────────────────────────────────────────────────┐
                    │            FLOW 1: Code-as-Policy 계보          │
                    │                                                 │
                    │  CaP (2022) ──→ Code-as-Symbolic-Planner (2025)│
                    │      │              │                           │
                    │      │              ▼                           │
                    │      └────────→ CaP-X (2026)                   │
                    │                  [벤치마크화]                    │
                    └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────────────┐
                    │            FLOW 2: VLA 메인스트림               │
                    │                                                 │
                    │  PaLM-E (2023) ──→ RT-2 (2023)                 │
                    │       │               │                         │
                    │       │               ▼                         │
                    │       │         Open X-Embodiment (2023)        │
                    │       │           │          │                  │
                    │       │           ▼          ▼                  │
                    │       │      Octo (2024)  OpenVLA (2024)       │
                    │       │           │          │                  │
                    │       │           └────┬─────┘                  │
                    │       │                ▼                        │
                    │       │          pi0 (2024) → pi0.5 (2025)     │
                    │       │                │                        │
                    │       │                ▼                        │
                    │       └──────→ GR00T N1 (2025)                 │
                    └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────────────┐
                    │          FLOW 3: Grounding & Planning           │
                    │                                                 │
                    │  LLM as Planners (2022) ──→ SayCan (2022)      │
                    │         │                       │               │
                    │         ▼                       ▼               │
                    │   AutoTAMP (2023)         SayPlan (2023)       │
                    │         │                       │               │
                    │         ▼                       ▼               │
                    │    RT-H (2024)           RoboEXP (2024)        │
                    │         │                       │               │
                    │         ▼                       ▼               │
                    │   HAMSTER (2025)         MoMa-LLM (2024)       │
                    │         │                                       │
                    │         ▼                                       │
                    │   Hi Robot (2025)                               │
                    └─────────────────────────────────────────────────┘

                    ┌─────────────────────────────────────────────────┐
                    │          FLOW 4: Agentic Closed-Loop            │
                    │                                                 │
                    │  REFLECT (2023) ──→ AutoRT (2024)              │
                    │        │                │                       │
                    │        ▼                ▼                       │
                    │   BUMBLE (2024)   PragmaBot (2025)             │
                    │        │                │                       │
                    │        └───────┬────────┘                       │
                    │                ▼                                │
                    │          CaP-X (2026)                          │
                    │     [Code + Agentic 통합]                      │
                    └─────────────────────────────────────────────────┘
```

---

## 2. 핵심 영향 관계 상세

### 2.1 SayCan → 전체 분야의 기초

**SayCan [Ahn et al., 2022]** 은 이 분야의 가장 중요한 기초 논문 중 하나.

직접적 영향:
- **AutoTAMP [2023]**: SayCan의 affordance scoring을 formal verification으로 확장. "LLM 계획이 실행 가능한지 형식적으로 검증"
- **SayPlan [2023]**: SayCan의 grounding 아이디어를 3D scene graph로 확장. 단일 방 → 전체 건물 규모로 스케일링
- **RT-2 [2023]**: SayCan이 보인 "언어-행동 연결"을 end-to-end 모델로 내재화
- **AutoRT [2024]**: SayCan의 affordance 개념을 fleet 규모로 확장. 로봇 자율 지시 시스템

간접적 영향:
- "LLM은 가능한 행동 중에서 선택해야 한다"는 원칙이 이후 모든 LLM-robot 시스템의 기본 가정

### 2.2 Code as Policies → Code-centric Robotics 계보

**CaP [Liang et al., 2022]** 는 Code-as-Policy 패러다임의 원형.

직접적 영향:
- **Code-as-Symbolic-Planner [2025]**: CaP의 "코드로 로봇 제어"를 "코드가 symbolic planning 수행"으로 확장. 단순 API glue → solver/checker
- **CaP-X [2026]**: CaP를 agentic 벤치마크로 발전. "코드 에이전트가 로봇 조작을 얼마나 잘 하는가"를 측정
- **RL-GPT [2024]**: CaP의 code-as-policy를 RL과 결합. slow code agent + fast RL agent

핵심 아이디어 전파:
- "코드는 자연어보다 정확하고 실행 가능한 표현" → 이후 planning 논문에서 코드 생성이 표준 접근으로 자리잡음

### 2.3 PaLM-E → RT-2 → Open VLA 체인

가장 명확한 계보 관계:

```
PaLM-E (2023): "멀티모달 LM이 로봇 상태를 이해할 수 있다"
    │
    ▼
RT-2 (2023): "VLM을 action token으로 fine-tune하면 VLA가 된다"
    │
    ▼
Open X-Embodiment (2023): "대규모 cross-embodiment 데이터로 일반화"
    │
    ├──→ Octo (2024): "오픈소스 generalist policy"
    │
    ├──→ OpenVLA (2024): "오픈소스 VLA, fine-tuning 가능"
    │
    └──→ pi0 (2024): "flow-matching으로 더 나은 action 생성"
              │
              └──→ pi0.5 (2025): "open-world generalization"
```

이 체인의 특징:
1. 모델 크기 감소: 562B → 55B → 7B → 경량화 지속
2. 접근성 증가: Google 독점 → 오픈소스
3. 방법론 진화: auto-regressive → flow-matching/diffusion

### 2.4 REFLECT → Agentic Loop 형성

**REFLECT [Liu et al., 2023]** 는 "로봇이 실패에서 배우는" 패러다임의 시작.

직접적 영향:
- **BUMBLE [2024]**: REFLECT의 실패 분석을 building-scale로 확장. VLM이 실시간으로 실패를 감지하고 재계획
- **PragmaBot [2025]**: REFLECT의 "경험에서 배우기"를 체계화. 실세계 경험의 체계적 축적

간접적 영향:
- AutoRT [2024]: fleet 수준에서 실패 경험을 공유하고 안전 규칙을 업데이트

### 2.5 Scene Graph 계보

```
SayPlan (2023): 3D scene graph + LLM planning
    │
    ├──→ RoboEXP (2024): action-conditioned scene graph
    │
    ├──→ MoMa-LLM (2024): language-grounded dynamic scene graph
    │
    ├──→ VeriGraph (2024): scene graph for plan verification
    │
    └──→ KARMA (2024): scene graph as long-term memory
```

공통 통찰: Scene graph가 LLM과 물리 세계를 잇는 "구조적 인터페이스" 역할.

### 2.6 Memory 계보

```
KARMA (2024): LTM (scene graph) + STM (action buffer)
    │
    ├──→ Embodied-RAG (2024): spatial-semantic hierarchy for retrieval
    │
    ├──→ 3D-Mem (2024): 3D scene memory for exploration
    │
    └──→ RoboMemory (2025): brain-inspired multi-memory
              [episodic + semantic + procedural]
```

진화 방향: 단순 기록 → 구조적 기록 → 다중 메모리 시스템

---

## 3. 흐름 간 교차점 (Cross-Flow Connections)

### 3.1 Code + VLA 수렴
- CaP (Code) + RT-2 (VLA) → **HAMSTER [2025]**: VLM이 high-level code-like plan, VLA가 low-level control
- CaP (Code) + Agentic Loop → **CaP-X [2026]**: 코드 에이전트가 VLA를 벤치마킹

### 3.2 Scene Graph + Memory 수렴
- SayPlan (Scene Graph) + KARMA (Memory) → scene graph가 동시에 planning 인터페이스이자 long-term memory로 기능

### 3.3 Planning + Safety 수렴
- AutoTAMP (formal verification) + AutoRT (safety constraints) → 안전한 자율 계획의 양축

### 3.4 VLA + Agentic 수렴
- OpenVLA/pi0 (VLA) + BUMBLE (Agentic) → VLA 정책을 closed-loop 에이전트 내에서 실행

---

## 4. 연구 그룹별 영향력

### Google DeepMind / Robotics
- SayCan → RT-2 → Open X-Embodiment → AutoRT
- 이 분야의 가장 큰 연구 체인. 데이터/컴퓨팅 자원이 핵심 차별화 요소

### UC Berkeley (BAIR)
- Octo, DROID 참여
- 오픈소스 생태계의 중심. 데이터셋과 모델 공개에 적극적

### Stanford
- Diffusion Policy, CaP, SayPlan, VeriGraph 등 다수 논문
- 방법론(diffusion, scene graph)에서 영향력

### Physical Intelligence (pi)
- pi0, pi0.5
- 산업 수준 VLA. 스타트업으로서 가장 공격적인 접근

### NVIDIA
- GR00T N1
- Humanoid 로봇 + dual-system. 하드웨어-소프트웨어 수직 통합

---

## 5. 책 챕터와의 매핑

| 챕터 | 핵심 논문 계보 | 흐름 |
|------|--------------|------|
| Ch 2: LLM as Planner | LLM as Planners → SayCan | Flow 3 |
| Ch 3: Code as Policies | CaP → Code-as-Symbolic-Planner → CaP-X | Flow 1 |
| Ch 4: VLA 부상 | PaLM-E → RT-2 → OpenVLA → pi0 | Flow 2 |
| Ch 5: 계층적 계획 | AutoTAMP → RT-H → HAMSTER → Hi Robot | Flow 3 |
| Ch 6: 저수준 제어 | Diffusion Policy → 3D Diffuser Actor → DROID | Flow 2 하위 |
| Ch 7: 메모리/세계표현 | SayPlan → KARMA → Embodied-RAG | Scene Graph + Memory |
| Ch 8: 폐루프 시스템 | REFLECT → BUMBLE → AutoRT → PragmaBot | Flow 4 |
| Ch 9: Sim2Real | SIMPLER → NL Sim2Real → Bridging Sim2Real | 횡단적 |
| Ch 10: 종합 비교 | 전체 흐름 수렴 + CaP-X | 전체 통합 |

---

## 6. 핵심 "허브(Hub)" 논문

인용 네트워크에서 가장 많은 연결을 가진 논문:

1. **SayCan (2022)** — 4개 흐름 모두에 영향. Grounding의 출발점
2. **RT-2 (2023)** — VLA 패러다임 정의. 후속 모든 VLA의 기준
3. **Open X-Embodiment (2023)** — 데이터 허브. Octo, OpenVLA, pi0의 공통 기반
4. **CaP (2022)** — Code-centric 접근의 원형. Code-as-Symbolic-Planner, CaP-X로 발전
5. **Diffusion Policy (2023)** — 저수준 제어의 표준. 3D Diffuser Actor, DROID 등에 영향

이 5편이 전체 연구 지형의 "교차로" 역할.

---

## 7. 추가 조사 필요

- researcher가 연구 그룹 매핑(Task #7)을 완료하면, 그룹별 영향력 섹션을 보강 예정
- 각 논문의 실제 citation count와 인용 관계 확인 필요
- 2026년 최신 논문(CaP-X 등)의 실제 영향력은 시간이 필요
