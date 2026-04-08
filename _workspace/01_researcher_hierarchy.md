# Hierarchical Planning & Control — 심층 서베이

> 카테고리 핵심 질문: **고수준 계획과 저수준 제어를 어떻게 연결하는가?**

"생각하는 것"과 "실행하는 것" 사이에는 근본적인 추상화 간극이 있다. LLM Planner는 고수준 계획을 잘 세우지만 정밀한 모터 제어를 할 수 없고, VLA는 행동을 직접 출력하지만 복잡한 추론이 어렵다. 이 카테고리는 이 두 세계를 **계층적으로 연결**하는 연구를 다룬다.

---

## 1. 핵심 논문 분석

### 1.1 AutoTAMP: LLMs as Translators and Checkers (2023)

- **arXiv**: https://arxiv.org/abs/2306.06531
- **저자**: Yongchao Chen, Jacob Arkin, Yang Zhang, Nicholas Roy, Chuchu Fan (MIT)
- **학회**: ICRA 2024

#### 핵심 Contribution
LLM을 **직접적인 플래너**가 아니라 자연어 → 형식 명세(formal specification) **번역기(translator)** 및 **검증기(checker)**로 사용하는 TAMP 프레임워크. "LLM을 플래너 그 자체보다 플래너의 전처리기+검증기로 쓰는 편이 낫다"는 핵심 통찰.

#### 방법론
- LLM이 자연어 작업 기술을 **Signal Temporal Logic (STL)** 같은 형식 표현으로 번역
- **Autoregressive Re-prompting**: 구문적(syntactic) 오류와 의미적(semantic) 오류를 자동 감지·수정
- 번역된 형식 명세를 전통적 TAMP 알고리즘이 소비하여 작업+경로 계획

#### 주요 결과
| 설정 | GPT-4 + AutoTAMP (구문+의미 수정) |
|------|--------------------------------|
| 단일 에이전트 | **82.5% ~ 87.7%** 성공률 |
| 다중 에이전트 (구문 수정) | **94%** |
| 다중 에이전트 (전체 AutoTAMP) | **100%** |

- 직접 LLM 계획 대비 기하학적·시간적 제약이 있는 작업에서 유의미한 우위
- 2D 작업 도메인에서 단일/다중 에이전트 시나리오 평가

#### 한계점
- 2D 환경에서의 평가에 한정
- STL 변환의 표현력이 모든 작업을 커버하지 못할 수 있음
- 실제 3D 로봇 환경으로의 확장 미검증

#### 영향
- Code-as-Symbolic-Planner (2025)의 직접적 전신: "LLM을 translator+checker로 쓴다" 아이디어
- "LLM을 단독 플래너로 쓰지 말고, 전통 계획기와 결합하라"는 하이브리드 접근의 대표

#### Agentic Coding 대비
AutoTAMP의 "LLM이 형식 명세로 번역하고 검증기가 확인한다"는 패턴은, Agentic Coding에서 "LLM이 코드를 생성하고 린터/컴파일러/테스트가 검증한다"는 것과 구조적으로 동일하다. 차이점: 코드의 형식 검증은 성숙한 도구체인이 있지만, 로봇 TAMP의 형식 검증은 아직 초기 단계.

---

### 1.2 RT-H: Action Hierarchies Using Language (2024)

- **arXiv**: https://arxiv.org/abs/2403.01823
- **저자**: Suneel Belkhale, Dorsa Sadigh et al. (Google DeepMind, Stanford)

#### 핵심 Contribution
**언어 모션(language motion)**을 고수준 작업과 저수준 행동 사이의 **중간 표현(intermediate representation)**으로 사용하는 계층적 action hierarchy. "move arm forward" 같은 세밀한 언어 기술이 다양한 작업 간 저수준 모션의 공유 구조를 학습하게 한다.

#### 방법론
- **고수준**: 작업 지시 ("pick coke can")
- **중간 수준**: language motion 예측 ("move arm forward", "close gripper")
- **저수준**: language motion에 조건화된 행동 출력
- 시각적 맥락(visual context)이 모든 단계에서 활용

#### 핵심 통찰
- 의미적으로 다른 작업 ("pick coke can" vs "pour cup")도 저수준 모션은 유사할 수 있음
- Language motion이 이 공유 구조를 명시적으로 드러냄 → 데이터 효율 향상
- **실행 중 인간 교정 가능**: 사용자가 language motion으로 로봇 행동을 실시간 수정

#### 주요 결과
- 의미적으로 다양한 작업 간 데이터 공유 효율 향상
- 인간이 language motion으로 실행 중 개입 가능한 새로운 패러다임
- 데모 데이터 요구량 감소

#### 한계점
- Language motion 어노테이션 필요 → 데이터 준비 비용
- 정밀한 연속 제어에서 언어의 이산성이 한계가 될 수 있음
- 규모 확장성 미검증

#### 영향
- Hi Robot, HAMSTER 등 계층적 VLA의 직접적 영감
- "언어를 중간 표현으로 사용하는 계층적 정책"의 개념 확립
- 인간-로봇 상호작용(HRI)에서 실시간 언어 교정의 가능성 제시

#### Agentic Coding 대비
RT-H의 "language motion"은 Agentic Coding에서 "의사코드(pseudocode)"에 해당한다. 프로그래머가 "이 함수에서 데이터를 필터링하고 변환해" 같은 중간 수준 지시를 내리면, LLM이 구체적 코드로 변환하는 것처럼, RT-H에서 "move arm forward"가 구체적 모터 명령으로 변환된다.

---

### 1.3 Hi Robot: Hierarchical VLA for Open-Ended Instructions (2025)

- **arXiv**: https://arxiv.org/abs/2502.19417
- **저자**: Lucy Xiaoyang Shi et al. (Physical Intelligence, Stanford)

#### 핵심 Contribution
복잡한 지시, 사용자 피드백, 다단계 명령을 처리할 수 있는 **고수준/저수준 분리형 계층적 VLA**. 인간 의도와의 정렬(alignment)을 명시적으로 다룬다.

#### 방법론
- **고수준 (VLM)**: 현재 관찰과 사용자 발화를 해석 → 언어 응답 생성 + 원자적 명령(atomic command) 생성 (예: "grasp the cup")
- **저수준 (Policy)**: 원자적 명령을 받아 실제 행동 실행
- **실시간 언어 피드백 통합**: "그거 말고" 같은 사용자 교정에 대응

#### 주요 결과
- 단일팔, 양팔, 모바일 플랫폼 등 **다양한 로봇**에서 평가
- 테이블 정리, 샌드위치 만들기, 장보기 등 **시나리오 기반 작업**
- API-based VLM 및 flat VLA 대비 **인간 의도 정렬 및 작업 성공률 모두 우수**

#### 한계점
- VLM의 추론 지연이 실시간 반응에 영향
- "원자적 명령"의 범위가 사전 정의된 스킬에 의존
- 완전히 새로운 스킬은 학습 불가

#### 영향
- **Agentic Robotics의 핵심 요소**인 "인간 피드백 실시간 통합"을 계층적 구조로 해결
- pi0.5와 함께 Physical Intelligence의 계층적 VLA 라인 형성

#### Agentic Coding 대비
Hi Robot의 "사용자 피드백 실시간 통합"은 Agentic Coding에서 "사용자가 코드 생성 중 방향을 수정"하는 것과 동일하다. 핵심 차이: 코드는 수정해도 비용이 없지만, 로봇은 이미 실행한 물리적 행동을 되돌릴 수 없으므로 피드백 타이밍이 더 중요하다.

---

### 1.4 HAMSTER: Hierarchical VLA for Open-World Manipulation (2025)

- **arXiv**: https://arxiv.org/abs/2502.05485
- **저자**: Jingyun Li et al.

#### 핵심 Contribution
계층적 VLA가 표준 monolithic VLA보다 **off-domain 데이터 활용에 더 효과적**임을 입증. 고수준 VLM이 2D 경로를 예측하고, 저수준 3D-aware policy가 정밀 제어를 수행.

#### 방법론
- **고수준**: VLM이 RGB 이미지 + 작업 기술 → 2D end-effector 경로(coarse path) 예측
- **저수준**: 3D-aware control policy가 2D 경로를 따라 정밀 조작 수행
- **Off-domain 데이터 활용**: 행동 없는 비디오, 손 그림 스케치, 시뮬레이션 데이터로 고수준 VLM 파인튜닝

#### 주요 결과
- 실제 로봇에서 OpenVLA 대비 평균 **+20% 성공률** (7개 일반화 축), **50% 상대적 향상**
- Off-domain 데이터로 파인튜닝해도 실제 로봇에서 유의미한 전이
- 도메인 간 간극(embodiment, dynamics, 시각적 외관, 작업 의미) 극복

#### 한계점
- 2D 경로 표현이 3D 공간의 복잡한 조작을 완전히 포착하지 못할 수 있음
- 고수준/저수준 분리가 일부 작업에서는 비효율적
- Off-domain 데이터의 품질 관리 기준이 명확하지 않음

#### 영향
- **"Off-domain 데이터를 활용하려면 계층적 구조가 필요하다"**는 핵심 메시지
- 비싼 로봇 데이터 대신 저렴한 비디오/스케치/시뮬레이션을 활용하는 경로 제시
- 산업 현장 적용에 특히 중요: 실제 로봇 데이터 수집 비용을 줄이는 실용적 방법

#### Agentic Coding 대비
HAMSTER의 "off-domain 데이터 활용"은 Agentic Coding에서 "다른 언어/프레임워크의 코드 패턴을 새 환경에 전이"하는 것과 유사하다. 차이점: 코드 간 전이는 구문적 변환이지만, 로봇에서의 off-domain 전이는 물리적 차이(embodiment, dynamics)를 극복해야 한다. HAMSTER는 계층적 분리가 이 극복을 가능하게 함을 보였다.

---

## 2. 카테고리 종합 분석

### 2.1 계층적 분리의 세 가지 형태

| 형태 | 고수준 | 중간 수준 | 저수준 | 대표 |
|------|-------|----------|-------|------|
| **형식 명세 경유** | LLM → STL/PDDL | — | TAMP solver | AutoTAMP |
| **언어 모션 경유** | 작업 지시 | Language motion | 행동 | RT-H |
| **2D 경로 경유** | VLM → 2D path | — | 3D-aware policy | HAMSTER |
| **원자적 명령 경유** | VLM → atomic cmd | — | Low-level policy | Hi Robot |

### 2.2 진화 경로

```
AutoTAMP (2023.06)          RT-H (2024.03)
    │                            │
    │ LLM = translator         │ language = 중간표현
    │ + checker                  │
    │                            │
    ▼                            ▼
Code-as-Symbolic-Planner    Hi Robot (2025.02)    HAMSTER (2025.02)
(코드 = solver/checker)     (VLM+policy 분리)      (off-domain 활용)
```

### 2.3 "왜 계층적 분리가 필요한가?"에 대한 수렴적 답변

모든 논문이 공통으로 지적하는 이유:

1. **추상화 수준 불일치**: 자연어 지시("샌드위치 만들어")와 모터 명령(관절 토크) 사이의 간극이 너무 큼
2. **데이터 효율**: 고수준 의미와 저수준 제어를 분리하면 각각 적합한 데이터로 학습 가능
3. **Off-domain 데이터 활용**: 계층 분리 시 고수준은 비디오/텍스트, 저수준은 로봇 데이터로 따로 학습 가능
4. **인간 개입 용이**: 계층이 있으면 적절한 추상 수준에서 인간이 교정 가능
5. **디버깅/해석**: 중간 표현이 있으면 어디서 실패했는지 진단 가능

### 2.4 GR00T N1의 Dual-System과의 관계

GR00T N1의 System 2 (VLM) / System 1 (Diffusion Transformer) 구조는 이 카테고리의 계층적 분리를 **아키텍처 수준에서 구현**한 것이다:
- System 2 ≈ Hi Robot의 고수준 VLM ≈ HAMSTER의 고수준 VLM
- System 1 ≈ Hi Robot의 저수준 policy ≈ HAMSTER의 3D-aware policy

---

## 3. 인용 네트워크

```
SayCan (2022) ──→ AutoTAMP (2023.06, ICRA'24)
                       │
LLM as Planners (2022) ──→ AutoTAMP
                       │
                       └──→ Code-as-Symbolic-Planner (2025.03)

RT-2 (2023.07) ──→ RT-H (2024.03)
                       │
                       └──→ Hi Robot (2025.02)
                       └──→ HAMSTER (2025.02)

Diffusion Policy (2023.03) ──→ HAMSTER (low-level policy)
```

---

## 4. 연구 그룹 매핑

| 그룹 | 논문 | 특징 |
|------|-----|------|
| MIT REALM (Chuchu Fan) | AutoTAMP, Code-as-Symbolic-Planner | 형식 검증 + LLM 결합 |
| Google DeepMind | RT-H | Language hierarchy |
| Physical Intelligence + Stanford | Hi Robot | 인간 피드백 통합 |
| (다기관) | HAMSTER | Off-domain 데이터 활용 |

---

*작성일: 2026-04-08*
*서베이 범위: 2023.06 ~ 2025.02*
