# 미해결 문제 식별: Agentic Robotics의 핵심 과제

> Critical Analyst 산출물 | 2026-04-08
> 7대 차원 간극 분석과 패러다임 전환 분석을 종합하여 도출

---

## 분류 체계

미해결 문제를 세 등급으로 분류한다:
- **[근본적]**: 물리 세계의 본질적 속성에서 비롯. 완전 해결 불가능 — 적응 전략 필요
- **[구조적]**: 현재 아키텍처/방법론의 한계. 새로운 접근으로 해결 가능성 있음
- **[실용적]**: 엔지니어링 노력과 자원으로 해결 가능. 시간 문제

---

## 문제 1: 물리적 피드백의 의미 변환 [근본적]

### 문제 정의
로봇의 센서 데이터(force/torque, 이미지, point cloud)를 LLM이 이해할 수 있는 "의미 있는 피드백"으로 변환하는 것. Stack trace처럼 명확한 인과관계를 가진 피드백 체계가 물리 세계에 존재하지 않음.

### 현재 상태
- REFLECT [2023]: VLM이 실패 장면을 보고 원인을 자연어로 설명. 그러나 정확도 한계
- VeriGraph [2024]: scene graph 비교로 성공/실패 판정. 구조적 피드백이나 세밀도 부족

### 왜 어려운가
1. **인과관계의 다대다 매핑**: 하나의 실패에 여러 원인이 가능하고, 하나의 원인이 여러 실패를 유발
2. **관측의 부분성**: 실패 원인이 카메라 시야 밖에 있을 수 있음
3. **피드백 지연**: 행동과 결과 사이의 시간 간격이 인과 추론을 어렵게 함

### 필요한 돌파구
- 물리 시뮬레이션 기반 "counterfactual reasoning": "만약 더 세게 잡았다면?"을 시뮬레이션
- 촉각/힘 센서 + VLM의 멀티모달 실패 진단 통합
- 실패 경험 데이터베이스와 유사 상황 검색 (failure RAG)

### 관련 논문
REFLECT, VeriGraph, BUMBLE (재계획), CaP-X (코드 수준 디버깅)

---

## 문제 2: 실시간 세계 모델(World Model) [구조적]

### 문제 정의
로봇이 행동 전에 결과를 예측하는 내부 모델. "이 물체를 이렇게 잡으면 어떻게 될까?"를 실시간으로 시뮬레이션하는 능력.

### 현재 상태
- VLA 모델은 반응적(reactive): 현재 관측 → 즉시 행동. 미래 예측 없음
- GR00T N1 [2025]: dual-system(System 2 reasoning + System 1 action)을 제안했으나, System 2가 진정한 물리 예측을 수행하는지는 불명확
- Video prediction 모델(UniSim, Genie 등)이 시각적 미래 예측을 시도하나, 정확도와 속도 모두 부족

### 왜 어려운가
1. **물리 시뮬레이션의 연산 비용**: 정밀한 접촉 역학 시뮬레이션은 실시간 불가
2. **모델 학습 데이터**: "행동→결과" 쌍 데이터가 대규모로 필요
3. **불확실성 표현**: 예측의 확신도를 정량화하고 의사결정에 반영해야 함

### 필요한 돌파구
- 학습된 물리 시뮬레이터(learned physics simulator)의 실시간화
- 불확실성을 명시적으로 모델링하는 세계 모델
- 예측 실패 시 보수적 행동으로 전환하는 메커니즘

### 관련 논문
GR00T N1, Diffusion Policy (확률적 미래), pi0 (flow-matching)

---

## 문제 3: Cross-Embodiment 일반화 [구조적]

### 문제 정의
하나의 정책/모델이 다양한 로봇 하드웨어에서 작동하는 것. 인간의 손, 로봇 그리퍼, 2-finger, dexterous hand 등 형태가 다른 로봇에 동일 능력을 전이.

### 현재 상태
- Open X-Embodiment [2023]: 22개 embodiment 통합 데이터셋. RT-1-X가 일부 cross-embodiment 전이 성공
- Octo [2024]: 9개 로봇에서 out-of-the-box 작동. 그러나 fine-tuning 없이는 성능 저하
- OpenVLA [2024]: 단일 모델이 여러 로봇에 적용 가능하나, embodiment 간 성능 편차 큼
- HAMSTER [2025]: off-domain data 활용으로 일반화 확장 시도

### 왜 어려운가
1. **Action space의 이질성**: 7-DoF 로봇 팔, 2-finger gripper, 5-finger hand의 action space가 근본적으로 다름
2. **Morphology gap**: 같은 "잡기"도 embodiment에 따라 전혀 다른 motor command
3. **센서 구성의 차이**: 카메라 위치, 해상도, FOV가 로봇마다 다름

### 필요한 돌파구
- Embodiment-agnostic action representation (자연어? 코드? 중간 표현?)
- Foundation model이 morphology를 "이해"하고 적응하는 메커니즘
- 소량 데이터로 새 embodiment에 빠르게 적응하는 few-shot 전이

### Agentic Coding 대비
코드 에이전트는 언어/프레임워크가 달라도 자연어 reasoning이 공통 → 일반화가 자연스러움. 로봇은 "body가 다르면 모든 것이 다름" → 훨씬 어려운 문제.

### 관련 논문
Open X-Embodiment, Octo, OpenVLA, HAMSTER, GR00T N1

---

## 문제 4: Long-Horizon 작업의 누적 에러 [구조적]

### 문제 정의
수십~수백 단계의 연쇄 작업에서 개별 단계의 작은 에러가 누적되어 최종 실패로 이어지는 문제. "아침 식사 준비"는 20+ 단계, 각 단계 95% 성공률이라도 전체 성공률은 0.95^20 ≈ 36%.

### 현재 상태
- BUMBLE [2024]: building-scale에서 navigation + manipulation을 연쇄. 실패 감지와 재계획으로 누적 에러 완화
- SayPlan [2023]: 3D scene graph로 large-scale planning. 그러나 실행 단계에서의 에러 누적은 미해결
- KARMA [2024]: 장기 메모리로 과거 경험 참조 → 유사 상황에서 에러 회피
- Hi Robot [2025]: 인간 실시간 보정으로 누적 에러 방지. 그러나 자율성 포기

### 왜 어려운가
1. **에러 전파**: 초기 단계의 작은 위치 오차가 후속 단계에서 증폭
2. **상태 추적**: 20단계 후의 환경 상태를 정확히 추적하기 어려움
3. **재계획 비용**: 매 단계 재계획하면 속도 저하, 안 하면 에러 누적

### 필요한 돌파구
- 중간 검증 포인트(checkpoint): 코드의 unit test처럼 작업 중간에 상태 검증
- 적응적 재계획 빈도: 상황에 따라 재계획 여부를 동적 결정
- 에러에 강건한 skill primitive: 개별 skill의 성공률을 99%+ 수준으로 향상

### 관련 논문
BUMBLE, SayPlan, KARMA, Hi Robot, PragmaBot

---

## 문제 5: Safety와 Autonomy의 균형 [근본적]

### 문제 정의
자율적인 행동을 허용하면서도 인간과 환경에 대한 안전을 보장하는 것. Agentic Coding에서는 sandbox/rollback으로 해결되지만, 물리 세계에서는 근본적 딜레마.

### 현재 상태
- AutoRT [2024]: LLM이 "robot constitution"을 생성. "인간에게 해를 끼치는 행동 금지" 등 규칙 기반 안전
- PragmaBot [2025]: 보수적 행동 전략. 불확실할 때 행동하지 않음
- BUMBLE [2024]: 실패 감지 시 즉시 중단 및 재계획

### 왜 어려운가
1. **Safety-Autonomy 트레이드오프**: 안전할수록 보수적 → 유용성 감소
2. **Long-tail 위험**: 학습 데이터에 없는 위험 상황(OOD)에서의 안전 보장 불가
3. **규칙의 불완전성**: "인간에게 해를 끼치지 말 것"의 모든 경우를 열거 불가
4. **실시간 제약**: 안전 판단을 밀리초 내에 수행해야 함

### 필요한 돌파구
- 계층적 안전 아키텍처: 하드웨어 수준 → 반사적 안전 (즉시), 소프트웨어 수준 → 추론적 안전 (숙고)
- 불확실성 기반 보수성: 모델이 "모른다"는 것을 인식하고 자동으로 보수적 행동 전환
- 인간 감독의 점진적 감소: 초기에는 인간 감독, 경험 축적에 따라 자율성 증가

### 관련 논문
AutoRT, PragmaBot, BUMBLE

---

## 문제 6: 데이터 효율성 — 물리 데이터의 희소성 [실용적]

### 문제 정의
웹 텍스트/이미지 데이터는 수조 토큰. 로봇 action 데이터는 수백만 에피소드에 불과. 이 데이터 격차를 어떻게 해소하는가.

### 현재 상태
- DROID [2024]: 76개 기관 참여로 대규모 데이터 수집. 그러나 웹 데이터 대비 여전히 미미
- Open X-Embodiment [2023]: 100만+ 에피소드. 가장 큰 로봇 데이터셋이나 다양성 한계
- TinyVLA [2024]: 적은 데이터로 효율적 VLA 학습 시도
- FAST [2025]: action tokenization 효율화로 동일 데이터에서 더 많이 학습
- Simulation data: 무한 생성 가능하나 sim2real gap 문제

### 왜 어려운가
1. **수집 비용**: 물리 데이터 1에피소드 ≈ 수분의 실시간 로봇 운영
2. **안전 제약**: 학습용 데이터 수집 중에도 안전 감독 필요
3. **다양성 부족**: 단일 환경에서 수집한 데이터는 일반화에 한계
4. **Annotation 비용**: 자연어 지시, task success 판정 등 레이블링 필요

### 필요한 돌파구
- Sim-to-real 전이 고도화 (SIMPLER, NL Sim2Real 등의 발전)
- 인터넷 비디오(YouTube 등)에서 로봇 action 데이터 추출
- Human demonstration의 효율적 활용 (one-shot imitation)
- 자기 지도 학습(self-supervised)으로 label 없이 학습

### 관련 논문
DROID, Open X-Embodiment, TinyVLA, FAST, SIMPLER, NL Sim2Real, Bridging Sim2Real

---

## 문제 7: 실시간 추론 — 모델 크기 vs 제어 주기 [실용적]

### 문제 정의
VLA 모델(수십억 파라미터)의 추론 속도와 로봇의 제어 주기(10-1000Hz) 사이의 괴리.

### 현재 상태
- PaLM-E (562B): 추론에 수초 → 실시간 제어 불가
- OpenVLA (7B): 경량화 시도, 그러나 여전히 100Hz 제어에 부적합
- TinyVLA [2024]: 더 작은 모델로 효율화
- FAST [2025]: action tokenization 최적화로 추론 속도 향상
- Hierarchical 접근: high-level VLM은 느리게(1-10Hz), low-level policy는 빠르게(100Hz+)

### 왜 어려운가
1. **Transformer 추론 비용**: 파라미터 수에 비례하여 증가
2. **Auto-regressive 생성**: action을 토큰 단위로 순차 생성 → 지연
3. **배포 환경**: 로봇 onboard 컴퓨팅은 데이터센터보다 제한적

### 필요한 돌파구
- 계층적 아키텍처의 표준화: HAMSTER, Hi Robot 류의 분리가 사실상 필수
- Action chunking: 한 번 추론으로 여러 timestep의 action을 동시 출력 (Diffusion Policy 방식)
- Edge 추론 최적화: 모델 양자화, pruning, distillation
- Flow-matching (pi0): diffusion보다 빠른 생성 가능

### 관련 논문
OpenVLA, TinyVLA, FAST, HAMSTER, Hi Robot, pi0, Diffusion Policy

---

## 문제 8: 평가 표준의 부재 [실용적]

### 문제 정의
Agentic Robotics의 능력을 공정하고 재현 가능하게 비교하는 벤치마크가 없음. Agentic Coding의 SWE-bench에 해당하는 것이 로봇에 존재하지 않음.

### 현재 상태
- SIMPLER [2024]: 시뮬레이션 기반 정책 비교. 그러나 sim-real 상관이 불완전
- CaP-X [2026]: Agentic Coding 벤치마크를 로봇 조작에 처음 적용. 초기 단계
- 각 논문이 자체 환경/메트릭으로 평가 → 직접 비교 불가
- 실환경 벤치마크는 재현성 문제 (동일 물체, 동일 배치 보장 불가)

### 왜 어려운가
1. **환경 재현 불가**: 물리 환경을 정확히 재현하는 것이 원리적으로 불가
2. **메트릭의 다양성**: task success rate, execution time, safety violation, generalization 등 다축 평가 필요
3. **Embodiment 다양성**: 로봇마다 action space가 달라 공정 비교 어려움
4. **비용**: 대규모 물리 실험은 비용이 막대

### 필요한 돌파구
- 표준화된 sim 벤치마크 스위트 (SIMPLER 확장)
- 실환경 벤치마크 프로토콜 (물체 세트, 배치 규칙, 평가 메트릭 표준화)
- Cross-embodiment 비교 메트릭 (embodiment-invariant task success)
- CaP-X류의 "Agentic 벤치마크"가 표준으로 채택

### 관련 논문
SIMPLER, CaP-X, Open X-Embodiment

---

## 종합: 미해결 문제 우선순위 매트릭스

| # | 문제 | 등급 | 현재 진전 | 해결 시급성 | 핵심 논문 |
|---|------|------|----------|-----------|----------|
| 1 | 물리적 피드백 의미 변환 | 근본적 | 초기 | ★★★★★ | REFLECT, VeriGraph |
| 2 | 실시간 세계 모델 | 구조적 | 미시작 | ★★★★☆ | GR00T N1 |
| 3 | Cross-embodiment 일반화 | 구조적 | 중기 | ★★★★☆ | OXE, Octo, OpenVLA |
| 4 | Long-horizon 누적 에러 | 구조적 | 중기 | ★★★★★ | BUMBLE, KARMA |
| 5 | Safety-Autonomy 균형 | 근본적 | 초기 | ★★★★★ | AutoRT |
| 6 | 데이터 효율성 | 실용적 | 중기 | ★★★☆☆ | DROID, SIMPLER |
| 7 | 실시간 추론 | 실용적 | 진행중 | ★★★☆☆ | HAMSTER, FAST |
| 8 | 평가 표준 | 실용적 | 초기 | ★★★★☆ | SIMPLER, CaP-X |

### 핵심 관찰

**가장 시급한 3대 문제**: (1) 물리적 피드백 변환, (4) Long-horizon 누적 에러, (5) Safety-Autonomy 균형. 이 세 문제가 해결되지 않으면 Agentic Robotics는 연구실(lab demo)을 벗어나지 못한다.

**가장 빠르게 해결될 문제**: (7) 실시간 추론. 하드웨어 발전(GPU, 엣지 칩)과 모델 경량화 기술이 빠르게 진전 중.

**Agentic Coding에서 이식 가능한 해결책**: (8) 평가 표준. SWE-bench가 Agentic Coding을 가속화한 것처럼, CaP-X류의 벤치마크가 Agentic Robotics의 발전을 가속할 수 있다.
