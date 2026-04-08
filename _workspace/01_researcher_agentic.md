# Agentic Systems & Sim2Real — 심층 서베이

> 카테고리 핵심 질문: **폐루프 에이전틱 시스템은 어떻게 작동하며, 시뮬레이션-현실 간극을 어떻게 극복하는가?**

이 카테고리는 두 축을 다룬다: (1) 실패를 감지·분석·복구하는 **폐루프(closed-loop) 에이전틱 시스템**, (2) 시뮬레이션에서 학습한 정책을 실제 로봇으로 전이하는 **Sim2Real** 연구. 두 축은 "실세계에서 오래 일하는 로봇"이라는 목표에서 만난다.

---

## 1. 에이전틱 시스템 논문

### 1.1 REFLECT: Failure Explanation and Correction (2023)

- **arXiv**: https://arxiv.org/abs/2306.15724
- **저자**: Zeyi Liu, Arpit Bahety, Shuran Song (Stanford, Columbia)
- **학회**: CoRL 2023

#### 핵심 Contribution
다중 감각(multisensory) 관찰을 기반으로 로봇 과거 경험의 **계층적 요약(hierarchical summary)**을 생성하고, LLM에 쿼리하여 **실패 원인을 설명**하며, 이를 활용해 **재계획**하는 프레임워크.

#### 방법론
- 다중 감각 데이터 → 계층적 경험 요약 (시간적·의미적 추상화)
- **Progressive Failure Explanation**: LLM이 요약을 점진적으로 분석하여 실패 원인 추론
- 실패 설명 → 언어 기반 플래너가 교정 계획 생성
- **RoboFail Dataset**: 다양한 작업과 실패 시나리오를 포함한 평가 데이터셋

#### 주요 결과
- LLM이 생성한 실패 설명이 성공적인 교정 계획을 유도
- 다양한 작업 및 실패 유형에 걸쳐 일반화
- 계층적 요약이 flat 요약 대비 정보량과 정확도 모두 우수

#### 한계점
- LLM의 실패 원인 추론이 항상 정확하지는 않음 (환각 가능)
- 물리적 원인(마찰, 미끄러짐 등)에 대한 추론 한계
- 실시간 교정이 아닌 사후 분석 중심

#### 영향
- "로봇이 왜 실패했는지 설명하고 고친다"는 에이전틱 루프의 핵심 구성요소
- PragmaBot, BUMBLE 등 후속 에이전틱 시스템에 영향

#### Agentic Coding 대비
REFLECT는 Agentic Coding의 **에러 분석 → 디버깅 → 수정** 루프와 직접 대응된다. 차이점: 코드 에러는 스택 트레이스와 로그로 원인이 비교적 명확하지만, 로봇 실패는 시각·힘·위치 등 다중 감각 데이터에서 원인을 추론해야 한다. "왜 실패했는지" 판단 자체가 로봇에서 훨씬 어렵다.

---

### 1.2 AutoRT: Large Scale Orchestration of Robotic Agents (2024)

- **arXiv**: https://arxiv.org/abs/2401.12963
- **저자**: Michael Ahn, Debidatta Dwibedi et al. (Google DeepMind)

#### 핵심 Contribution
VLM(씬 이해) + LLM(작업 제안) + **Robot Constitution(로봇 헌법)**으로 **다수의 로봇을 대규모로 자율 관리**하는 시스템. 단일 인간이 5대 로봇을 감독.

#### 방법론
- **VLM**: 환경 씬 이해 및 grounding
- **LLM**: 다양하고 새로운 작업 지시 생성
- **Robot Constitution**: Asimov의 로봇 3원칙에서 영감 받은 안전 가이드라인
  - 기본 안전 규칙 + embodiment 제약 + 작업별 제한
- 자율 + 원격조종 하이브리드로 데이터 수집

#### 주요 결과
| 메트릭 | 수치 |
|-------|------|
| 수집 기간 | **7개월** |
| 로봇 수 | **20대 이상** |
| 건물 수 | **4개** |
| 시연 데이터 | **77,000개** |
| 인간:로봇 비율 | **1:5** |

- 유용하고 다양한 대규모 데이터 수집 달성
- Robot Constitution이 안전 위반을 효과적으로 방지

#### 한계점
- Google 내부 인프라에 의존 (재현 어려움)
- Robot Constitution의 범용성 미검증 (새로운 환경/작업에서의 적용)
- 수집된 데이터의 품질 관리 메커니즘 상세 미공개

#### 영향
- **"로봇 헌법(Robot Constitution)"** 개념의 최초 도입 → 안전한 자율 로봇 시스템의 기초
- SayCan → AutoRT로 이어지는 Google의 로봇 시스템 진화 완성
- 대규모 로봇 데이터 수집의 새로운 패러다임 제시

#### Agentic Coding 대비
AutoRT의 "Robot Constitution"은 Agentic Coding의 **시스템 프롬프트/안전 가드레일**에 대응된다. Claude Code가 "파괴적 작업 전 확인", "보안 취약점 방지" 규칙을 따르듯, AutoRT의 로봇은 Robot Constitution을 따른다. 핵심 차이: 코드에서 안전 위반은 되돌릴 수 있지만(git revert), 로봇의 물리적 사고는 되돌릴 수 없다.

---

### 1.3 BUMBLE: Building-wide Mobile Manipulation (2024)

- **arXiv**: https://arxiv.org/abs/2410.06237
- **저자**: Mujin Shah et al.
- **학회**: AAAI 2025

#### 핵심 Contribution
VLM 기반으로 추론(reasoning)과 행동(acting)을 통합하여, 여러 방·여러 층에 걸친 **건물 규모(building-wide)** 모바일 조작을 수행하는 에이전틱 프레임워크.

#### 방법론
- **VLM 중심 통합**: RGBD 인식, 다양한 조작 스킬 라이브러리, 이중층 메모리(dual-layered memory)를 단일 VLM이 관리
- **Free-form 언어 지시**: 자유 형식 자연어 작업 입력
- **Parameterized Skill Library**: 네비게이션+상호작용 스킬을 파라미터화하여 다양한 씬에 적응
- **Dual-layered Memory**: 과거 경험과 현재 상태를 분리 관리

#### 주요 결과 (90+ 시간 평가)
| 메트릭 | 수치 |
|-------|------|
| 시험 횟수 | 70회 (다양한 건물, 작업, 레이아웃) |
| 평균 성공률 | **47.1%** |
| 최대 스킬 시퀀스 | **12단계** |
| 시행당 시간 | **~15분** |
| 사용자 만족도 | Baseline 대비 **+22%** |

- 주요 실패: VLM 추론 오류 (충돌 예측 실패, 20-25개 distractors에서 오객체 선택, 엘리베이터 버튼 오인식)

#### 한계점
- 47.1% 성공률 → 아직 현장 배포에는 부족
- VLM 추론 오류가 주요 실패 원인 → VLM 자체의 한계가 시스템 한계
- 건물 규모이지만 단일 건물 유형(오피스)에서 평가

#### 영향
- "building-wide agentic robotics"의 가장 포괄적인 실험 결과
- VLM 추론 오류 분석이 향후 연구 방향을 제시

#### Agentic Coding 대비
BUMBLE의 "건물 규모" 작업은 Agentic Coding에서 "대규모 코드베이스 리팩토링"에 대응. 여러 파일(방)을 넘나들며, 의존성(복도)을 추적하고, 전체 시스템(건물)의 일관성을 유지해야 한다. 47.1%의 성공률은, 대규모 코드 변경에서도 CI/CD 없이는 비슷한 실패율을 보일 수 있음을 시사.

---

### 1.4 PragmaBot: Learning to Plan by Experiencing (2025)

- **arXiv**: https://arxiv.org/abs/2507.16713
- **저자**: (multiple authors)

#### 핵심 Contribution
**Verbal Reinforcement Learning** 패러다임: LLM 에이전트가 파라미터 업데이트 없이 **자기 반성(self-reflection)**과 **few-shot 학습**으로 경험에서 배우는 에이전틱 로봇.

#### 방법론
- VLM을 로봇의 "뇌"와 "눈"으로 활용: (i) 행동 계획, (ii) 행동 성공 검증, (iii) 경험 요약
- **Short-term Memory (STM)**: 실행된 행동과 피드백 신호 추적
- **Long-term Memory (LTM)**: 과거 성공 경험에서 배운 교훈 저장
- **RAG**: 유사 작업 시 LTM에서 관련 지식 검색하여 계획에 활용

#### 주요 결과
| 조건 | 성공률 |
|------|-------|
| Baseline (STM 없음) | 35% |
| STM 기반 자기 반성 | **84%** |
| LTM + RAG (새 작업 12개) | **80%** (단일 시행) |
| Naive prompting (RAG 없음) | 22% |

- STM으로 35% → 84% (2.4배 향상)
- LTM+RAG로 새로운 작업에서 22% → 80% (3.6배 향상)
- **Emergent intelligent object interactions**: 예상하지 못한 창의적 물체 사용 행동 출현

#### 한계점
- 경험 축적에 시간이 필요 (cold start 문제)
- LTM의 검색 품질이 RAG의 한계에 의존
- 완전히 새로운 작업 유형에서의 일반화 한계

#### 영향
- **경험 기반 학습 + 에이전틱 루프**의 가장 완성된 형태
- REFLECT의 "실패 분석" + KARMA의 "기억 시스템" + RAG를 통합

#### Agentic Coding 대비
PragmaBot은 Agentic Coding에서의 **"실패에서 배우는 에이전트"**와 가장 유사하다. Claude Code가 에러를 만나면 에러 메시지를 분석하고, 이전 성공 패턴을 참조하여 수정하는 것처럼, PragmaBot은 실패를 관찰하고, 과거 성공 경험(LTM)을 참조하여 재시도한다. 핵심 차이: 코드 에러는 즉시 재시도 가능하지만, 로봇 실패는 환경 리셋이 필요하므로 시행착오 비용이 훨씬 높다.

---

## 2. Sim2Real 논문

### 2.1 SIMPLER: Evaluating Robot Policies in Simulation (2024)

- **arXiv**: https://arxiv.org/abs/2405.05941
- **저자**: Xuanlin Li et al. (UC San Diego, Stanford, Berkeley)
- **학회**: CoRL 2024

#### 핵심 Contribution
실세계 로봇 조작 정책을 **시뮬레이션에서 신뢰성 있게 평가**할 수 있는 오픈소스 환경 모음. 실세계 평가의 스케일러빌리티·재현성 문제를 해결.

#### 방법론
- Google Robot 및 WidowX BridgeV2 환경의 시뮬레이션 구현
- 제어 불일치(control disparity)와 시각 불일치(visual disparity) 식별 및 완화
- 완전한 digital twin 없이도 신뢰성 있는 평가 가능

#### 주요 결과
- 시뮬레이션 성능과 실세계 성능 간 **강한 상관관계** 입증
- 분포 이동(distribution shift)에 대한 정책 민감도를 정확히 반영
- RT-1, RT-1-X, Octo 등 generalist policy 평가 지원

#### Agentic Coding 대비
SIMPLER는 Agentic Coding의 **테스트/스테이징 환경**에 대응. 코드를 프로덕션에 배포하기 전 테스트 환경에서 검증하듯, 로봇 정책을 실세계에 배포하기 전 시뮬레이션에서 검증. 차이점: 코드 테스트 환경은 프로덕션과 거의 동일하게 만들 수 있지만(Docker), 로봇 시뮬레이션은 물리 세계와의 간극(sim2real gap)이 존재.

---

### 2.2 Natural Language Can Help Bridge the Sim2Real Gap (2024)

- **arXiv**: https://arxiv.org/abs/2405.10020
- **저자**: (UT Austin)
- **학회**: RSS 2024

#### 핵심 Contribution
시뮬레이션과 실세계의 시각적 간극을 **자연어 기술(description)**을 공통 의미 표현으로 사용하여 극복.

#### 방법론
- 이미지 인코더를 자연어 기술 예측으로 사전학습 → 도메인 불변 표현 학습
- 소량의 실세계 데모 + 대량의 시뮬레이션 데모로 동시 학습

#### 주요 결과
- CLIP, R3M 대비 **25~40% 향상**
- 수백 개의 이미지-언어 쌍 사전학습만으로 인터넷 규모 사전학습(CLIP, R3M) 초과

#### Agentic Coding 대비
"언어를 중간 표현으로 사용하여 도메인 간극을 극복한다"는 아이디어는 흥미롭다. Agentic Coding에서 "자연어 의사코드로 알고리즘을 기술하면 언어에 무관하게 구현 가능"한 것과 유사한 구조.

---

## 3. 카테고리 종합 분석

### 3.1 에이전틱 로보틱스의 핵심 루프

```
┌──────────────────────────────────────────────┐
│              에이전틱 로보틱스 루프             │
│                                              │
│  관찰(Perceive) → 계획(Plan) → 실행(Act)     │
│       ↑                            │         │
│       │                            ▼         │
│  기억(Remember)  ←  반성(Reflect)            │
│       │                            │         │
│       └── 검증(Verify) ←──────────┘         │
└──────────────────────────────────────────────┘
```

각 구성요소와 대표 논문:
| 구성요소 | 대표 논문 | 역할 |
|---------|----------|------|
| 관찰 | VLM (모든 논문) | 환경 인식 |
| 계획 | LLM Planner, Code as Policy | 행동 시퀀스 생성 |
| 실행 | VLA, Low-level Policy | 물리적 행동 수행 |
| 반성 | **REFLECT** | 실패 원인 분석 |
| 기억 | **KARMA**, **PragmaBot** | 경험 축적·검색 |
| 검증 | **VeriGraph**, **SIMPLER** | 실행 전/후 검증 |
| 조율 | **AutoRT** | 다중 에이전트 관리 |
| 통합 | **BUMBLE** | 전체 루프 통합 |

### 3.2 "에이전틱"의 진화 단계

```
Stage 1: 개루프 (2022)           Stage 2: 반성 (2023)
  LLM → Plan → Execute            LLM → Plan → Execute → Reflect
  (SayCan, CaP)                    (REFLECT)

Stage 3: 기억 (2024)             Stage 4: 완전 폐루프 (2025)
  Plan → Execute → Reflect         Plan → Execute → Reflect
  → Remember → Plan                → Remember → Learn → Plan
  (KARMA, BUMBLE)                  (PragmaBot)
```

### 3.3 Sim2Real: 간극의 세 차원

| 간극 차원 | 설명 | 해결 접근 |
|----------|------|----------|
| **시각적 간극** | 렌더링 vs 실제 이미지 | 언어 중간표현 (Lang4Sim2Real), 도메인 랜덤화 |
| **물리적 간극** | 시뮬레이션 물리 vs 실제 물리 | 시스템 식별, 도메인 랜덤화 |
| **제어 간극** | 시뮬레이션 제어 vs 실제 제어 | SIMPLER의 제어 불일치 완화 |

---

## 4. Agentic Coding ↔ Agentic Robotics: 루프 비교

| 에이전틱 루프 단계 | Agentic Coding | Agentic Robotics |
|-----------------|---------------|------------------|
| **관찰** | 파일 읽기, grep (즉시) | 카메라, 센서 (노이즈) |
| **계획** | 코드 생성 | 행동 시퀀스 생성 |
| **실행** | 코드 실행 (ms, 결정론적) | 물리 행동 (s~min, 확률적) |
| **검증** | 테스트/린터 (ms) | 시뮬레이션/관찰 (s~min) |
| **반성** | 에러 분석 (스택 트레이스) | 실패 분석 (다중 감각) |
| **기억** | 컨텍스트 윈도우, 파일 | STM/LTM, 씬 그래프 |
| **되돌리기** | git revert ✓ | 불가능 ✗ |
| **시행착오 비용** | ~무료 | 높음 (시간, 안전) |
| **안전** | sandbox 가능 | 물리적 위험 |

**핵심 통찰**: 에이전틱 루프의 **구조**는 동일하지만, 물리 세계의 비결정성·비가역성·비용이 각 단계의 난이도를 근본적으로 다르게 만든다. PragmaBot(35%→84%)과 같은 개선이 가능한 것은 에이전틱 루프의 보편성을 보여주지만, 47.1%(BUMBLE)에 머무는 것은 물리 세계의 추가적 난점을 보여준다.

---

## 5. 인용 네트워크

```
SayCan (2022) ──→ AutoRT (2024.01) ──→ Robot Constitution 개념
                                        ↓
LLM as Planners (2022) ──→ REFLECT (2023.06)
                                   ↓
                              PragmaBot (2025.07)
                              BUMBLE (2024.10)

SIMPLER (2024.05) ← RT-1, RT-1-X, Octo 정책 평가
Lang4Sim2Real (2024.05) ← CLIP, R3M 대안 제시
```

---

## 6. 연구 그룹 매핑

| 그룹 | 논문 | 특징 |
|------|-----|------|
| Google DeepMind | AutoRT | 대규모 로봇 관리, Robot Constitution |
| Stanford (Shuran Song) | REFLECT | 실패 분석 프레임워크 |
| CMU/UT Austin | BUMBLE, Lang4Sim2Real | 건물 규모 + Sim2Real |
| UC San Diego + Stanford | SIMPLER | 시뮬레이션 평가 프레임워크 |

---

*작성일: 2026-04-08*
*서베이 범위: 2023.06 ~ 2025.07*
