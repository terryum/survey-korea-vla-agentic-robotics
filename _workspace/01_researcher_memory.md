# Memory & World Representation — 심층 서베이

> 카테고리 핵심 질문: **로봇이 장기 작업을 수행하려면 무엇을 기억해야 하는가?**

단발성 조작("컵을 집어")과 달리, 실세계 작업("주방을 정리해")은 수십~수백 단계에 걸쳐 환경의 변화를 추적하고, 과거 행동을 기억하며, 미래를 계획해야 한다. 이 카테고리는 로봇이 물리 세계를 어떻게 표현(represent)하고 기억(remember)해야 하는지를 다룬다.

---

## 1. 핵심 논문 분석

### 1.1 KARMA: Long-and-short Term Memory Systems (2024)

- **arXiv**: https://arxiv.org/abs/2409.14908
- **저자**: Zixuan Wang et al.
- **학회**: AAAI 2025

#### 핵심 Contribution
Embodied AI 에이전트에 **장기 기억(long-term) + 단기 기억(short-term)** 시스템을 통합. 장기 기억은 **3D 씬 그래프**로 환경 전체를 포착하고, 단기 기억은 객체의 위치/상태 변화를 동적으로 기록.

#### 방법론
- **Long-term Memory**: 환경의 포괄적 3D 씬 그래프 (공간 구조, 객체 관계)
- **Short-term Memory**: 객체 위치/상태 변화를 실시간 기록
- **Memory-augmented Prompting**: 기억 시스템의 정보로 LLM 프롬프트를 보강하여 계획 품질 향상
- **Plug-and-play**: 모바일 조작 플랫폼 등 실제 로봇에 바로 적용 가능

#### 주요 결과 (AI2-THOR 시뮬레이터)
| 작업 유형 | 성공률 향상 | 실행 효율 향상 |
|----------|-----------|-------------|
| Composite Tasks | **1.3배** | **3.4배** |
| Complex Tasks | **2.3배** | **62.7배** |
| 안전 작업 완료율 | **70%** (SafeAgentBench) |

- 장기 작업에서 효율 향상이 극적 (Complex Tasks에서 62.7배)

#### 한계점
- 3D 씬 그래프 구축의 초기 비용이 높음
- 동적 환경에서 씬 그래프 업데이트 전략이 아직 단순
- AI2-THOR 시뮬레이터 환경에서의 평가 → 실세계 검증 제한

#### 영향
- SayPlan의 3D 씬 그래프 개념을 기억 시스템으로 확장
- Embodied-RAG와 함께 "로봇을 위한 기억 아키텍처" 연구의 대표

#### Agentic Coding 대비
Agentic Coding에서도 장기/단기 기억이 필요하다 — 장기 기억은 프로젝트 구조와 코딩 컨벤션(CLAUDE.md), 단기 기억은 현재 세션의 컨텍스트 윈도우. KARMA의 3D 씬 그래프는 코드베이스의 파일 트리 + 심볼 테이블에 대응. 핵심 차이: 코드베이스는 정적(파일이 저절로 바뀌지 않음)이지만, 물리 환경은 동적(다른 사람/로봇이 물건을 옮김).

---

### 1.2 Embodied-RAG: Non-parametric Embodied Memory (2024)

- **arXiv**: https://arxiv.org/abs/2409.18313
- **저자**: Quanting Xie, So Yeon Min et al. (CMU)

#### 핵심 Contribution
Embodied agent를 위한 **비파라메트릭(non-parametric) RAG** 프레임워크. 텍스트 문서 검색이 아니라 **공간-의미 계층(spatial-semantic hierarchy)**으로 환경을 구조화하여 검색·생성.

#### 방법론
- **Topological Map**: 환경의 토폴로지 구조 (방-복도-건물 수준)
- **Semantic Forest**: 계층적 의미 표현 (전체 분위기 → 영역 → 개별 객체)
- **Retrieval-augmented Navigation + Reasoning**: 쿼리에 맞는 공간-의미 수준에서 정보 검색
- 특정 객체부터 전체 분위기까지 다양한 해상도의 쿼리 처리

#### 주요 결과
- 다양한 환경과 쿼리 유형에 걸쳐 공간-의미 해상도의 전 범위 처리
- 네비게이션 + 언어 생성 모두에서 기존 RAG 대비 개선
- 멀티모달 embodied 도메인에 특화된 RAG 설계

#### 한계점
- 메모리 구축 자체의 탐색 비용
- 대규모 환경에서의 스케일러빌리티 미검증
- 동적 환경 변화에 대한 메모리 업데이트 전략 미비

#### 영향
- "문서 RAG → 물리 세계 RAG"로 패러다임 확장
- KARMA와 상보적: KARMA=씬 그래프 기반, Embodied-RAG=토폴로지+의미 기반

#### Agentic Coding 대비
Agentic Coding의 RAG(코드베이스 검색)와 직접 대응되지만, 근본적 차이가 있다:
- **코드 RAG**: 텍스트 임베딩 기반, 파일 시스템 경로로 정확한 위치 지정
- **Embodied RAG**: 공간 좌표 + 의미 계층, 물리 탐색이 필요

---

### 1.3 RoboEXP: Action-Conditioned Scene Graph (2024)

- **arXiv**: https://arxiv.org/abs/2402.15487
- **저자**: Hanxiao Jiang et al.
- **학회**: CoRL 2024

#### 핵심 Contribution
단순한 "보이는 것" 그래프가 아니라, **"어떻게 조작할 수 있는가"까지 포함한 Action-Conditioned Scene Graph (ACSG)**를 로봇이 **자율적 탐색**을 통해 구축.

#### 방법론
- **Interactive Exploration**: 로봇이 환경을 능동적으로 탐색하며 ACSG 구축
- **4개 모듈**: Perception, Memory, Decision-making, Action
- **ACSG**: 저수준(기하학, 의미론) + 고수준(행동 조건 관계) 정보 통합
- Large Multimodal Model (LMM) + 명시적 메모리 설계

#### 주요 결과
- Rigid, articulated, nested, deformable 객체에 걸쳐 다양한 조작 작업 성공
- **Zero-shot** 탐색 및 복잡한 ACSG 구축
- 가리는 객체(obstructing objects)와 다단계 추론이 필요한 시나리오 처리
- 실제 로봇에서 검증

#### 한계점
- 탐색 시간이 작업 실행에 추가되는 오버헤드
- 완전히 새로운 객체 카테고리에서의 일반화 한계
- 대규모 환경에서의 탐색 효율 미검증

#### 영향
- "정적 씬 그래프"에서 "행동 조건 씬 그래프"로 패러다임 전환
- "로봇이 관찰만 하지 않고, 탐색을 통해 세계 모델을 구축한다"는 핵심 원칙

#### Agentic Coding 대비
RoboEXP의 "action-conditioned scene graph"는 코드에서 **동적 분석(dynamic analysis)**에 대응된다. 정적 분석(코드를 읽기만)이 아니라 실제 실행해보며 런타임 정보(어떤 함수가 어떤 값을 반환하는지)를 수집하는 것과 유사하다. 로봇의 "만져봐야 안다"는 물리 세계의 동적 분석.

---

### 1.4 VeriGraph: Execution Verifiable Robot Planning (2024)

- **arXiv**: https://arxiv.org/abs/2411.10446
- **저자**: Daniel Ekpo, Mara Levy et al.

#### 핵심 Contribution
씬 그래프를 **계획 검증(verification)** 도구로 활용. VLM이 생성한 행동 시퀀스의 실행 가능성을 씬 그래프 기반으로 반복 검증·수정.

#### 방법론
- 입력 이미지에서 씬 그래프 생성 (객체 + 관계)
- LLM 기반 task planner가 행동 시퀀스 생성
- **Iterative Verification Loop**: 제안된 행동이 씬 그래프 제약을 위반하면 재생성, 아니면 실행
- 환경이 목표 씬과 일치할 때까지 반복

#### 주요 결과
| 작업 유형 | Baseline 대비 성능 향상 |
|----------|---------------------|
| Language-based tasks | **+58%** |
| Image-based tasks | **+30%** |

#### 한계점
- 씬 그래프 생성기의 정확도에 의존
- 반복 검증의 계산 비용
- 매우 복잡한 다단계 작업에서의 스케일러빌리티 미검증

#### 영향
- AutoTAMP의 "LLM을 checker로 쓰기" 아이디어를 씬 그래프 기반으로 확장
- "실행 전 검증"의 중요성을 씬 그래프 도메인에서 입증

#### Agentic Coding 대비
VeriGraph의 "반복 검증 루프"는 Agentic Coding의 **CI/CD 파이프라인**에 정확히 대응된다: 코드 생성 → 테스트 실행 → 실패 시 수정 → 재시도. 차이점: 코드 테스트는 밀리초 단위지만, 로봇 행동 검증은 물리 시뮬레이션 또는 실행이 필요하여 훨씬 느리다.

---

### 1.5 보조 논문 요약

#### MoMa-LLM: Language-Grounded Dynamic Scene Graphs (2024)
- **arXiv**: https://arxiv.org/abs/2403.08605
- Language-grounded scene graph + mobile manipulation + object-centric action space
- 씬 그래프가 LLM grounding의 실질적 인터페이스가 될 수 있음을 입증

#### 3D-Mem: 3D Scene Memory for Embodied Exploration (2024)
- **arXiv**: https://arxiv.org/abs/2411.17735
- 조작보다 넓은 embodied reasoning 관점의 3D 씬 메모리

#### RoboMemory: Multi-memory Agentic Framework (2025)
- **arXiv**: https://arxiv.org/abs/2508.01415
- Brain-inspired multi-memory architecture for lifelong learning
- 아직 초기 단계이지만 "agentic memory stack"을 로봇에 심는 관점

#### LLM-Empowered Embodied Agent for Memory-Augmented Task Planning (2025)
- **arXiv**: https://arxiv.org/abs/2504.21716
- Local lightweight LLM 기반 agent orchestration + memory-augmented planning
- 실제 household robotics stack에 가까운 구현 감각

---

## 2. 카테고리 종합 분석

### 2.1 메모리/표현의 네 가지 축

| 축 | 방법 | 대표 논문 | 강점 |
|----|------|----------|------|
| **3D 씬 그래프** | 계층적 공간-객체 관계 | KARMA, SayPlan | 구조화된 관계 표현 |
| **Action-Conditioned** | 행동 가능성 포함 | RoboEXP | 조작 관련 정보 포착 |
| **토폴로지+의미** | 공간-의미 계층 | Embodied-RAG | 다해상도 검색 |
| **검증용 그래프** | 계획 검증 도구 | VeriGraph | 실행 전 오류 방지 |

### 2.2 "왜 메모리가 필요한가?" — 물리 세계의 고유 특성

1. **부분 관찰성**: 로봇은 카메라 시야 내의 것만 본다 → 시야 밖 정보를 기억해야 함
2. **환경 동적성**: 다른 에이전트/사람이 환경을 변경 → 변화를 추적해야 함
3. **작업 장기성**: 수십~수백 단계 작업 → 이미 한 것/아직 할 것을 추적
4. **비가역성**: 실행한 행동은 되돌릴 수 없음 → 실행 전 검증이 중요

이 네 가지는 모두 **Agentic Coding에서는 약화되거나 부재**하다:
- 코드베이스는 완전 관찰 가능 (파일 시스템)
- 혼자 작업 시 환경이 변하지 않음
- git으로 되돌리기 가능
- 코드 실행은 즉시·저비용으로 "시험 삼아" 실행 가능

### 2.3 씬 그래프의 진화

```
SayPlan (2023.07)         RoboEXP (2024.02)         KARMA (2024.09)
정적 3D 씬 그래프       action-conditioned        장기/단기 기억
+ 계층적 탐색           씬 그래프                 + 씬 그래프

VeriGraph (2024.11)       Embodied-RAG (2024.09)
검증용 씬 그래프        토폴로지+의미 계층
                          (비그래프 메모리)
```

---

## 3. 인용 네트워크

```
SayPlan (2023) ──→ KARMA (2024)
              ──→ VeriGraph (2024)

RoboEXP (2024) ── MoMa-LLM (2024)와 병행 발전

Embodied-RAG (2024) ← RAG (Retrieval-Augmented Generation) 개념의 로봇 적용

KARMA + Embodied-RAG → RoboMemory (2025) (두 방향 통합 시도)
```

---

## 4. 연구 그룹 매핑

| 그룹 | 논문 | 특징 |
|------|-----|------|
| CMU (Salakhutdinov, Bisk) | Embodied-RAG | RAG의 물리 세계 확장 |
| QUT (Sünderhauf) | SayPlan | 3D 씬 그래프 + LLM |
| CoRL/AAAI community | RoboEXP, KARMA, VeriGraph | 메모리 시스템 다양화 |

---

## 5. Agentic Coding ↔ Memory: 핵심 대비

| 차원 | Agentic Coding | Embodied Robotics |
|------|---------------|-------------------|
| 장기 기억 | CLAUDE.md, 프로젝트 문서 | 3D 씬 그래프 (KARMA) |
| 단기 기억 | Context window | Short-term state changes |
| 검색 | 텍스트 임베딩, grep | 공간-의미 계층 (E-RAG) |
| 탐색 | 파일 읽기 (즉시, 무비용) | 물리 탐색 (시간, 에너지 소요) |
| 갱신 | 파일 수정 시 자동 | 재탐색/재관찰 필요 |
| 검증 | 테스트 실행 (ms) | 물리 시뮬레이션/실행 (s~min) |

---

*작성일: 2026-04-08*
*서베이 범위: 2024.02 ~ 2025*
