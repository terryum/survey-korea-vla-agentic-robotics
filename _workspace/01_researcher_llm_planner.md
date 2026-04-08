# LLM as Planner & Grounding — 심층 서베이

> 카테고리 핵심 질문: **LLM이 로봇 계획(planning)에 어떻게 사용되기 시작했는가?**

이 카테고리는 2022년 초를 기점으로 LLM의 세계 지식(world knowledge)을 로봇의 고수준 계획에 활용하려는 초기 시도들을 다룬다. "LLM은 계획을 세울 수 있는가?"라는 질문에서 출발해, "어떻게 물리 세계에 접지(ground)시킬 것인가?"로 연구가 발전했다.

---

## 1. 핵심 논문 분석

### 1.1 Language Models as Zero-Shot Planners (2022)

- **arXiv**: https://arxiv.org/abs/2201.07207
- **저자**: Wenlong Huang, Pieter Abbeel, Deepak Pathak, Igor Mordatch (UC Berkeley, CMU, Google Brain)
- **학회**: ICML 2022 (Spotlight)

#### 핵심 Contribution
사전학습된 LLM이 충분히 크고 적절히 프롬프트되면, 고수준 자연어 작업("make breakfast")을 중간 수준 행동 단계("open fridge", "grab milk" 등)로 zero-shot 분해할 수 있음을 최초로 체계적으로 입증했다.

#### 방법론
1. **Admissible Action Parsing by Semantic Translation**: LLM이 생성한 자유 형식 텍스트를 VirtualHome 환경의 허용 가능한 행동 집합에 의미론적으로 매핑
2. **Autoregressive Trajectory Correction**: 이전 행동 결과를 피드백으로 활용해 다음 행동을 자기회귀적으로 수정
3. **Dynamic Example Selection**: 가장 유사한 예제를 동적으로 선택하여 few-shot 프롬프트 구성

#### 주요 결과 (VirtualHome 환경)
| 메트릭 | Baseline LLM | Translated LLM (제안 방법) |
|--------|-------------|--------------------------|
| Executability | 18% | **79%** |
| Correctness (LCS) | — | **32.87%** |

- Executability를 18% → 79%로 대폭 향상시켰으나, correctness는 여전히 낮은 수준
- **Trade-off**: 실행 가능성(executability)을 높이면 정확성(correctness)이 다소 하락하는 경향

#### 한계점
- **Correctness 한계**: 실행은 가능해도 의미적으로 올바른 계획인지는 별개 문제 (LCS 32.87%)
- **시뮬레이션 한정**: VirtualHome이라는 제한된 환경에서만 평가
- **접지 부재**: LLM이 물리적 환경 상태를 직접 관찰하지 못함 → 실제 로봇 적용에 근본적 한계
- **폐루프 부재**: 환경 피드백이 제한적이며, 실패 시 복구 메커니즘 미비

#### 영향
- LLM을 로봇 계획에 활용하는 연구의 **기점(origin point)**
- SayCan, Code as Policies, SayPlan 등 후속 연구에 직접적 영향
- "LLM의 세계 지식을 어떻게 접지시킬 것인가?"라는 핵심 연구 질문을 촉발

#### Agentic Coding 대비
디지털 에이전트(예: Claude Code)에서 LLM은 코드 실행 결과를 즉시 관찰하고 수정할 수 있다(REPL 루프). 반면 이 논문에서 LLM은 물리 환경의 상태를 직접 관찰하지 못하며, semantic translation이라는 추가 단계가 필요하다. **관찰-행동 간 간극(observation-action gap)**이 로봇 계획의 근본적 난점임을 보여주는 초기 사례.

---

### 1.2 SayCan: Grounding Language in Robotic Affordances (2022)

- **arXiv**: https://arxiv.org/abs/2204.01691
- **저자**: Michael Ahn, Anthony Brohan, Noah Brown, ... (Google Research, Everyday Robots)
- **학회**: CoRL 2022

#### 핵심 Contribution
LLM의 의미적 지식("Say")과 로봇의 행동 가능성 함수("Can", affordance function)를 결합하여, LLM이 생성한 계획을 실제 로봇이 물리 환경에서 실행 가능한 수준으로 접지(ground)시키는 프레임워크를 제안했다.

#### 방법론
- **핵심 아이디어**: `P(action | instruction) = P_LLM(useful | instruction, action) × P_affordance(feasible | state, action)`
  - **Say (Task Grounding)**: LLM이 주어진 지시에 대해 각 스킬의 유용성을 점수화
  - **Can (World Grounding)**: 사전학습된 affordance 함수가 현재 환경 상태에서 각 스킬의 실행 가능성을 점수화
  - 두 확률의 곱으로 최적 행동 선택
- **사전학습 스킬**: 551개의 로봇 조작 스킬을 자연어로 기술하고 사전학습
- **LLM**: 초기 버전에서 FLAN, 후속 업데이트에서 PaLM 540B 사용

#### 주요 결과 (실제 주방 환경, 101 tasks)
| LLM backbone | Plan Success Rate | Execution Success Rate |
|-------------|-------------------|----------------------|
| FLAN-SayCan | 70% | 61% |
| **PaLM-SayCan** | **84%** | **74%** |

- PaLM 적용 시 FLAN 대비 오류율 **50% 감소**
- 최대 8단계의 long-horizon 작업 성공 수행 (예: "나 콜라를 테이블에 쏟았어, 어떻게 치워줄 수 있어?")
- 다국어 쿼리, chain-of-thought 추론 활용 가능

#### 한계점
- **폐쇄형 스킬 세트**: 551개 사전학습 스킬에 한정 → 새로운 스킬 추가 시 추가 학습 필요
- **정적 affordance**: 환경 변화를 실시간으로 반영하지 못함
- **스케일 한계**: 주방이라는 제한된 공간, 제한된 객체 집합
- **단방향 계획**: 실패 시 재계획(replanning) 메커니즘이 제한적
- **느린 추론**: 매 단계마다 모든 스킬의 affordance를 계산해야 함

#### 영향
- **"Say + Can" 패러다임**의 확립: LLM의 의미 지식 + 물리 접지의 조합이 후속 연구의 표준 프레임워크가 됨
- RT-1, RT-2, PaLM-E 등 Google의 로봇 파운데이션 모델 계열의 직접적 전신
- AutoRT(2024)에서 대규모 로봇 관리 시스템으로 확장
- 인용 수 1000+로 이 분야의 가장 영향력 있는 논문 중 하나

#### Agentic Coding 대비
Agentic Coding에서 "도구 사용 가능 여부(tool availability)"는 API 문서나 타입 시그니처로 즉시 확인 가능하다. 반면 SayCan에서 "로봇 스킬 실행 가능 여부"는 물리 환경 상태에 따라 달라지며, 별도의 affordance 모델 학습이 필요하다. **디지털 세계의 도구 호출은 결정론적이지만, 물리 세계의 스킬 실행은 확률적**이라는 근본적 차이를 보여준다.

---

### 1.3 SayPlan: Grounding LLMs using 3D Scene Graphs (2023)

- **arXiv**: https://arxiv.org/abs/2307.06135
- **저자**: Krishan Rana, Jesse Haviland, Sourav Garg, Jad Abou-Chakra, Ian Reid, Niko Sünderhauf (QUT, University of Adelaide)
- **학회**: CoRL 2023 (Oral)

#### 핵심 Contribution
3D 씬 그래프(3DSG)의 계층적 구조를 활용하여 LLM 기반 계획을 대규모(multi-floor, multi-room) 환경으로 확장하는 방법을 제안했다. SayCan의 스케일 한계를 직접적으로 해결한다.

#### 방법론
1. **Hierarchical Semantic Search**: 3DSG의 계층 구조(building → floor → room → object)를 활용해 전체 그래프를 축소(collapse)한 뒤, 작업에 관련된 하위 그래프만 선택적으로 확장
2. **Classical Path Planner 통합**: LLM의 planning horizon을 줄이기 위해 고전적 경로 계획기와 결합
3. **Iterative Replanning Pipeline**: 씬 그래프 시뮬레이터에서 피드백을 받아 비실행 가능한 행동을 수정하고 재계획

#### 주요 결과
| 환경 규모 | 세부 사항 |
|----------|---------|
| 환경 1 | 2층, 18개 방 |
| 환경 2 | 3층, **36개 방, 140+ 에셋/객체** |

- 대규모 multi-room 환경에서 long-horizon 작업 계획 및 실행 성공
- Iterative replanning으로 환각(hallucination) 오류 대부분 교정
- 단, **6.67%의 작업에서 환각된 노드 교정 실패**

#### 한계점
- **사전 구축된 3DSG 필요**: 동적 환경 변화를 반영하지 못함 (객체가 이동한 후 그래프 업데이트 미지원)
- **LLM의 그래프 추론 한계**: 노드 부정(negation), 노드 개수 기반 추론, 거리 기반 추론에서 실패
- **환각 잔존**: iterative replanning으로도 완전히 제거되지 않음 (6.67%)
- **실제 로봇 검증 제한**: 시뮬레이션 기반 평가가 주, 실제 로봇에서의 대규모 검증은 제한적

#### 영향
- **씬 그래프 + LLM 계획**의 표준을 확립 → KARMA, VeriGraph, Embodied-RAG 등 memory/representation 연구에 직접적 영향
- "환경 표현(representation)이 LLM 계획의 스케일을 결정한다"는 통찰 제공
- 계층적 구조화된 입력이 LLM의 long-context 한계를 우회하는 효과적 전략임을 입증

#### Agentic Coding 대비
Agentic Coding에서 코드베이스도 파일-디렉토리의 계층 구조를 갖지만, `grep`, `find` 등으로 즉시 탐색 가능하다. SayPlan이 3DSG를 계층적으로 축소/확장하는 것은, 에이전틱 코딩에서 코드베이스를 `tree` → 특정 파일 → 특정 함수로 drill-down하는 것과 구조적으로 유사하다. 차이점은 물리 환경의 씬 그래프 구축 자체가 비용이 높고, 환경 변화에 따라 갱신이 필요하다는 점이다.

---

## 2. 관련 서베이 논문 요약

### 2.1 Large Language Models for Robotics: A Survey (2023)
- **arXiv**: https://arxiv.org/abs/2311.07226
- LLM의 로봇 활용을 perception / planning / control / interaction의 4축으로 정리
- **핵심 통찰**: text-only LLM은 embodied task에서 시각적 지각과의 호환성 부족이 근본적 한계
- 이 카테고리의 논문들이 정확히 이 한계를 해결하려는 시도임을 확인

### 2.2 A Survey on Large Language Models for Automated Planning (2025)
- **arXiv**: https://arxiv.org/abs/2502.12435
- **핵심 결론**: LLM은 단독 플래너로 부적합하지만, 전통적 계획 방법과 결합하면 강력
- LLM의 계획 한계 3가지: (1) 도메인 특화 지식 부족 → 환각, (2) long-horizon 추론 한계, (3) 높은 연산 비용
- **권고**: LLM의 유연성 + 전통적 계획의 엄밀성을 결합하는 하이브리드 접근

---

## 3. 카테고리 종합 분석

### 3.1 진화 경로: "생성" → "접지" → "구조화"

```
LLM as Planners (2022.01)     SayCan (2022.04)          SayPlan (2023.07)
    │                              │                          │
    │ LLM이 계획을               │ 물리 세계에             │ 환경 표현을
    │ 생성할 수 있다             │ 접지시킨다              │ 구조화한다
    │                              │                          │
    ▼                              ▼                          ▼
  Zero-shot plan         Affordance grounding        3D Scene Graph
  generation              (Say + Can)                 + Hierarchical search
```

### 3.2 핵심 한계의 누적

| 한계 | LLM as Planners | SayCan | SayPlan |
|------|-----------------|--------|---------|
| 물리 접지(grounding) | ✗ 없음 | △ affordance 함수 | △ 씬 그래프 |
| 스케일 | 작음 (VirtualHome) | 중간 (주방) | 큼 (36방) |
| 폐루프 재계획 | ✗ | ✗ 제한적 | △ iterative replanning |
| 동적 환경 대응 | ✗ | ✗ | ✗ (정적 그래프) |
| 환각(hallucination) | 높음 | 중간 | 낮지만 잔존 (6.67%) |

### 3.3 이 카테고리가 남긴 미해결 과제 → 후속 카테고리로

1. **"계획을 코드로 표현하면?"** → Code as Policy 카테고리 (CaP, Code-as-Symbolic-Planner)
2. **"LLM이 직접 행동을 출력하면?"** → VLA 카테고리 (RT-2, OpenVLA, pi0)
3. **"고수준 계획 + 저수준 제어를 분리하면?"** → Hierarchical Planning 카테고리 (RT-H, Hi Robot, HAMSTER)
4. **"동적 환경을 기억하려면?"** → Memory & Scene Graph 카테고리 (KARMA, Embodied-RAG)
5. **"실패를 감지하고 복구하려면?"** → Agentic Systems 카테고리 (REFLECT, BUMBLE, AutoRT)

---

## 4. 인용 네트워크

```
LLM as Planners (2022.01, ICML)
    ├──→ SayCan (2022.04, CoRL) ──→ RT-1 ──→ RT-2 ──→ AutoRT
    ├──→ Code as Policies (2022.09)
    ├──→ SayPlan (2023.07, CoRL) ──→ KARMA, VeriGraph
    └──→ REFLECT (2023.06)
    
SayCan
    ├──→ PaLM-E (2023) ──→ RT-2 (2023)
    ├──→ AutoTAMP (2023)
    └──→ Inner Monologue (2022)

SayPlan
    ├──→ KARMA (2024)
    ├──→ Embodied-RAG (2024)
    └──→ VeriGraph (2024)
```

---

## 5. 연구 그룹 매핑

| 그룹 | 소속 | 핵심 기여 |
|------|-----|---------|
| Wenlong Huang et al. | UC Berkeley → Google DeepMind | LLM as Planners, Inner Monologue, Eureka |
| Google Robotics / Everyday Robots | Google Research | SayCan, RT-1, RT-2, PaLM-E, AutoRT |
| QUT Robotics & AI | Queensland Univ. of Technology | SayPlan |

---

*작성일: 2026-04-08*
*서베이 범위: 2022.01 ~ 2023.12 (이 카테고리의 핵심 논문 시기)*
