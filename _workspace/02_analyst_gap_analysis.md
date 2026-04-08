# 7대 차원 간극 분석: Agentic Coding vs Agentic Robotics

> Critical Analyst 산출물 | 2026-04-08
> 근거 논문: Core 10 + Curated 40+ papers (docs/ 기반)

---

## 분석 목적

Agentic Coding(Claude Code, Cursor, Devin 등)은 code → tool → execution → error → LLM 루프로 자율적 소프트웨어 개발을 달성하고 있다. 이 루프를 물리 세계로 옮기려 할 때, 7대 차원에서 근본적 간극이 발생한다. 본 문서는 각 차원을 심층 분석한다.

---

## 1. Error Feedback Loop — 피드백의 질과 속도

### Agentic Coding의 현재 수준
- **Stack trace**: 정확한 파일명, 라인 번호, 에러 타입, 콜스택 제공
- **Test output**: pytest, jest 등이 expected vs actual을 명시적으로 제시
- **LSP/Type checker**: 실행 전에 타입 에러, 문법 에러를 즉시 감지
- **CI/CD pipeline**: 수분 내 통합 테스트 결과 반환
- **사례**: Claude Code는 코드 실행 → 에러 → 자동 수정 → 재실행 루프를 수초 단위로 반복

### Agentic Robotics의 현재 수준
- **센서 노이즈**: force/torque 센서의 측정 오차, 카메라의 occlusion
- **실패 원인 모호성**: gripper가 물체를 놓쳤을 때 — 힘이 부족? 물체가 미끄러움? 위치 오차? 물체 형상 변화?
- **지연된 피드백**: 행동 결과가 수초~수분 후에야 관측 가능 (예: 조립 실패는 다음 단계에서 발견)
- **REFLECT [Liu et al., 2023]**: VLM을 활용하여 로봇 실패 경험을 텍스트로 요약하고 원인을 추론. 그러나 실패 원인의 정확도는 인간 판단 대비 ~60% 수준
- **VeriGraph [2024]**: scene graph를 중간 표현으로 사용하여 plan execution을 검증. 그래프 기반 검증으로 피드백 구조화 시도

### 근본적 차이의 원인
1. **정보 채널의 대역폭**: 코드 에러는 structured text → 무한 대역폭. 물리 에러는 noisy sensor → 제한된 대역폭
2. **인과관계의 명확성**: 코드에서 에러와 원인은 1:1 대응. 물리 세계에서 하나의 실패에 다수 원인 가능
3. **관측의 완전성**: 코드 상태는 완전 관측 가능(full observability). 물리 세계는 부분 관측(partial observability)

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| VLM 기반 실패 설명 | REFLECT (2023) | VLM이 실패 장면을 보고 원인을 자연어로 설명 | 추론 정확도 한계, hallucination 위험 |
| Scene graph 검증 | VeriGraph (2024) | 행동 전후 scene graph 비교로 성공/실패 판정 | 세밀한 조작(grasping force 등) 미반영 |
| 실시간 재계획 | BUMBLE (2024) | VLM이 행동 결과를 관찰하고 즉시 재계획 | 빌딩 규모에서 피드백 지연 여전히 큼 |

### Gap 심각도: ★★★★★ (5/5)
이 차원이 가장 근본적인 병목. 물리 세계의 에러 피드백을 코드 수준의 명확성으로 변환하는 것이 Agentic Robotics의 핵심 과제.

---

## 2. Execution Determinism — 동일 명령, 다른 결과

### Agentic Coding의 현재 수준
- **결정론적 실행**: 동일 코드 + 동일 입력 = 동일 결과 (race condition 등 예외 존재하나 일반적으로 재현 가능)
- **환경 격리**: Docker, venv, nix 등으로 실행 환경을 완벽히 통제
- **재현 가능성**: CI에서 실패한 테스트를 로컬에서 동일하게 재현 가능

### Agentic Robotics의 현재 수준
- **확률적 실행**: 동일한 pick-and-place 명령도 물체 위치, 표면 마찰, 조명 변화에 따라 다른 결과
- **Diffusion Policy [Chi et al., 2023]**: 명시적으로 확률적 정책을 학습. 동일 관측에서 다수의 가능한 action trajectory를 모델링
- **DROID [Khazatsky et al., 2024]**: 76개 기관, 564개 장면에서 수집한 데이터. 환경 다양성 자체를 학습에 내재화하려는 시도
- **Open X-Embodiment [2023]**: cross-embodiment 데이터로 일반화 추구. 그러나 새 환경에서의 성능 편차 여전

### 근본적 차이의 원인
1. **물리 법칙의 연속성**: 접촉 역학은 미세한 초기 조건 변화에 민감 (chaotic dynamics)
2. **환경의 비정상성(non-stationarity)**: 온도, 습도, 물체 변형, 마모 등 지속적 변화
3. **센서-액추에이터 갭**: 명령한 것과 실행된 것의 괴리가 항상 존재 (backlash, compliance)

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| 확률적 정책 학습 | Diffusion Policy (2023) | multimodal action distribution 학습 | 실시간 추론 속도, 안전성 보장 어려움 |
| 대규모 다양 환경 | DROID (2024) | 환경 분산을 데이터로 커버 | 데이터 수집 비용 막대 |
| Sim-augmented training | SIMPLER (2024) | 시뮬레이션에서 정책 평가 후 실환경 보정 | sim2real gap이 결국 남음 |

### Gap 심각도: ★★★★☆ (4/5)
확률적 정책과 대규모 데이터가 간극을 줄이고 있으나, 결정론적 재현성을 물리 세계에서 달성하는 것은 원리적으로 불가능. 핵심은 "확률적이지만 안정적인(robust)" 시스템 설계.

---

## 3. State Representation — 세계를 어떻게 보는가

### Agentic Coding의 현재 수준
- **코드/파일 시스템**: 텍스트 기반, 구조적, 검색 가능, 완전 관측
- **AST(Abstract Syntax Tree)**: 코드의 의미 구조를 정확히 표현
- **스크린샷/DOM**: UI 상태를 이미지 또는 구조적 데이터로 표현
- **Git 히스토리**: 모든 상태 변화의 완전한 기록

### Agentic Robotics의 현재 수준
- **3D Scene Graph**: 물체 간 관계(위에, 안에, 옆에)를 그래프로 표현
  - **SayPlan [Rana et al., 2023]**: 3D scene graph로 large-scale 환경의 planning 확장. multi-floor 건물에서도 계획 가능
  - **RoboEXP [2024]**: interactive exploration으로 action-conditioned scene graph 구축. "열 수 있는", "잡을 수 있는" 등 affordance 포함
  - **MoMa-LLM [2024]**: language-grounded dynamic scene graph. 변화하는 환경을 실시간 반영
- **Point Cloud / Depth**: 3D 기하학적 정보. 3D Diffuser Actor [2024]가 이를 정책 입력으로 활용
- **Tactile Sensor**: 접촉 기반 정보. force/torque, 미끄러짐 감지

### 근본적 차이의 원인
1. **관측의 불완전성**: 코드는 모든 변수의 현재 값을 조회 가능. 로봇은 가려진 물체, 내부 상태를 모름
2. **표현의 다양성**: 코드는 텍스트라는 단일 모달리티. 로봇은 RGB, depth, force, proprioception, language를 동시 처리
3. **상태 공간의 차원**: 코드 상태는 유한 심볼. 물리 상태는 연속적이고 고차원

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| 3D Scene Graph | SayPlan (2023) | 구조적 세계 표현 → LLM grounding | 동적 환경 추적 비용 |
| Action-conditioned Graph | RoboEXP (2024) | affordance 포함 scene graph | 새 물체 범주 일반화 한계 |
| Language-grounded DSG | MoMa-LLM (2024) | 자연어 기반 scene graph 쿼리 | 세밀한 기하학 정보 손실 |
| Embodied-RAG | Embodied-RAG (2024) | spatial-semantic hierarchy로 메모리 검색 | 실시간 업데이트 비용 |

### Gap 심각도: ★★★★☆ (4/5)
Scene graph 계열이 유망하나, "코드를 읽듯 세계를 읽는" 수준까지는 먼 거리. 특히 동적 환경에서의 실시간 상태 추적이 병목.

---

## 4. Memory Architecture — 무엇을 기억하고 어떻게 꺼내는가

### Agentic Coding의 현재 수준
- **Long context window**: Claude 200K+, GPT-4 128K 토큰. 전체 코드베이스를 한 번에 참조 가능
- **Persistent files**: 코드, 문서, 설정이 파일로 영구 보존. 검색도 즉시 가능
- **Git history**: 모든 변경의 시간축 기록
- **RAG**: 코드베이스 인덱싱 + 벡터 검색으로 관련 코드 조회
- **시간 제약 없음**: 코드를 분석하는 데 수분이 걸려도 무방

### Agentic Robotics의 현재 수준
- **KARMA [2024]**: long-term memory (3D scene graph 기반)와 short-term memory (최근 행동 버퍼)를 명시적으로 분리. Open-vocabulary 환경에서 120개 물체를 추적하는 실험
- **Embodied-RAG [2024]**: spatial-semantic hierarchy를 구축하여 "어디에 무엇이 있었는지"를 검색. 문서 RAG와 달리 3D 공간 좌표 기반
- **3D-Mem [2024]**: 탐험(exploration) 과정의 3D scene memory를 유지하여 재방문 없이 추론
- **RoboMemory [2025]**: brain-inspired multi-memory (episodic, semantic, procedural) 아키텍처. lifelong learning 지향

### 근본적 차이의 원인
1. **시간 제약**: 코드는 "생각할 시간"이 풍부. 로봇은 실시간(10-100Hz) 제어 루프 안에서 메모리 조회
2. **공간적 메모리의 필요성**: 코드는 "어디"가 중요하지 않음. 로봇은 "무엇이 어디에 있는지"가 핵심
3. **메모리 용량 vs 속도 트레이드오프**: 풍부한 3D 표현은 저장/검색이 비싸고, 압축하면 정보 손실

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| LTM/STM 분리 | KARMA (2024) | scene graph LTM + action buffer STM | 실시간 scene graph 업데이트 비용 |
| Spatial RAG | Embodied-RAG (2024) | 3D 공간 좌표 기반 검색 | 대규모 환경 스케일링 |
| Multi-memory | RoboMemory (2025) | episodic/semantic/procedural 분리 | 아직 초기 연구, 실환경 검증 부족 |
| Memory-augmented planning | LLM-Embodied Agent (2025) | 로컬 LLM + 메모리 기반 task planning | lightweight LLM의 능력 한계 |

### Gap 심각도: ★★★☆☆ (3/5)
메모리 아키텍처는 빠르게 발전 중. KARMA, Embodied-RAG 등이 실용적 경로를 제시. 그러나 실시간 제약과 대규모 환경 확장이 과제.

---

## 5. Action Space — 무엇을 할 수 있는가

### Agentic Coding의 현재 수준
- **이산적(discrete)**: 파일 읽기, 파일 쓰기, 함수 호출, 터미널 명령 — 명확한 경계
- **조합적(compositional)**: API 호출을 자유롭게 조합하여 새 동작 생성
- **확장 가능**: 새 도구/API를 tool description으로 즉시 추가
- **원자적(atomic)**: 각 action의 시작/끝이 명확. "파일 저장 완료"

### Agentic Robotics의 현재 수준
- **연속적(continuous)**: 6-7 DoF 관절 각도/토크를 Hz 단위로 출력
- **RT-H [2024]**: language motion을 intermediate representation으로 사용하여 고수준 의도와 저수준 모터 명령 사이를 연결. "carefully pick up"과 같은 자연어가 행동 스타일을 제어
- **HAMSTER [2025]**: high-level VLM이 coarse path를 생성하고, low-level policy가 precise control 수행. 계층적 분리로 action space 관리
- **Hi Robot [2025]**: open-ended instruction을 hierarchical VLA로 처리. 사용자 실시간 보정(correction) 수용
- **Code-as-Symbolic-Planner [2025]**: LLM이 생성한 코드가 symbolic planner 역할. action space를 코드로 추상화

### 근본적 차이의 원인
1. **연속 vs 이산**: 코드 에이전트의 action은 본질적으로 이산 심볼. 로봇은 연속 값 제어
2. **Temporal extent**: 코드 action은 "즉시" 완료. 로봇 action은 시간에 걸쳐 전개 (trajectory)
3. **접촉 역학**: 코드는 "접촉"이 없음. 로봇은 물체와의 물리적 상호작용이 action의 핵심
4. **Action boundary의 모호성**: "컵을 잡았다"의 완료 시점이 불명확

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| Language-conditioned hierarchy | RT-H (2024) | 자연어로 action style 제어 | 표현력의 한계, 미세 제어 불가 |
| Hierarchical VLA | HAMSTER (2025) | coarse VLM + precise policy | 계층 간 정보 손실 |
| Code as action abstraction | Code-as-Symbolic-Planner (2025) | 코드가 planning을 수행, skill primitives 호출 | primitive library에 의존 |
| Open-ended + correction | Hi Robot (2025) | 실시간 사용자 보정 수용 | 자율성 한계 — 인간 의존 |

### Gap 심각도: ★★★★☆ (4/5)
계층적 추상화(hierarchical abstraction)가 핵심 해결 방향. Code-as-Symbolic-Planner가 Agentic Coding의 이산적 장점을 Robotics에 이식하려는 가장 직접적인 시도.

---

## 6. Verification & Testing — 어떻게 검증하는가

### Agentic Coding의 현재 수준
- **Unit test**: 수밀리초 내 개별 함수 검증. 수천 개 테스트를 수분 내 실행
- **Integration test**: API 엔드포인트, DB 연동 등 시스템 수준 검증
- **CI/CD**: PR마다 자동 검증. 전체 파이프라인 수분~수십분
- **Simulation ≈ Production**: 코드의 로컬 실행 결과는 프로덕션과 (거의) 동일
- **비용**: 사실상 무료. 클라우드 CI 비용은 미미

### Agentic Robotics의 현재 수준
- **Physical trial**: 한 번의 실험에 수분~수시간. 인간 감독 필요. 로봇 파손 위험
- **SIMPLER [Li et al., 2024]**: 시뮬레이션에서 real-world policy를 평가. RT-2, Octo 등을 SIMPLER로 비교. 그러나 sim2real 상관관계가 항상 성립하지는 않음
- **Natural Language Sim2Real [2024]**: language description을 중간 의미 표현으로 사용하여 sim-real 갭 완화. 픽셀 매칭 대신 의미 매칭
- **AutoRT [2024]**: 대규모 로봇 fleet 운영으로 검증 처리량(throughput) 증가. 20+ 로봇 동시 운영. safety constraint를 LLM이 생성

### 근본적 차이의 원인
1. **Sim2Real Gap**: 시뮬레이션이 완벽하지 않음. 접촉, 변형, 유체 등의 물리 시뮬레이션은 근사(approximation)
2. **검증 비용**: 물리 실험은 시간, 에너지, 인력, 장비 파손 위험을 동반
3. **Safety**: 잘못된 코드는 프로세스를 죽이면 됨. 잘못된 로봇 동작은 물리적 피해 가능
4. **환경 재현**: 코드 테스트 환경은 완벽 재현 가능. 물리 환경의 정확한 재현은 불가능

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| Sim evaluation benchmark | SIMPLER (2024) | 표준화된 sim 환경에서 정책 비교 | sim-real 상관 불완전 |
| Language bridging | NL Sim2Real (2024) | 의미 수준에서 sim-real 매칭 | 세밀한 물리 현상 미반영 |
| Fleet-scale testing | AutoRT (2024) | 다수 로봇 동시 운영으로 처리량 증가 | 인프라 비용 막대 (Google 규모) |
| Vision encoder transfer | Bridging Sim2Real (2025) | pre-trained encoder로 전이 효율 향상 | 도메인 특화 성능 편차 |

### Gap 심각도: ★★★★★ (5/5)
Error Feedback과 함께 가장 심각한 간극. "로봇 단위 테스트"에 해당하는 것이 존재하지 않음. SIMPLER류의 sim benchmark가 발전하고 있으나, 물리 검증을 완전히 대체하기는 원리적으로 어려움.

---

## 7. Recoverability — 실패에서 어떻게 복구하는가

### Agentic Coding의 현재 수준
- **git revert/reset**: 모든 코드 변경을 완벽하게 되돌림
- **Undo**: 에디터 수준에서 무한 undo
- **Sandbox**: 격리된 환경에서 실험 → 실패해도 프로덕션 무영향
- **실험 비용**: 사실상 0. "일단 해보고 안 되면 되돌리자"가 합리적 전략
- **Claude Code**: 자동으로 시도 → 실패 → 되돌림 → 다른 접근 반복

### Agentic Robotics의 현재 수준
- **비가역성**: 깨진 컵은 원상복구 불가. 쏟아진 액체는 되돌릴 수 없음
- **Safety constraint**: 실패 자체를 예방해야 함 (사후 복구 불가)
- **AutoRT [2024]**: LLM이 안전 규칙(robot constitution)을 생성하여 위험한 행동을 사전 차단. "물체를 인간에게 던지지 말 것" 등의 규칙
- **BUMBLE [2024]**: building-wide mobile manipulation. 실패 시 전체 경로를 재계획하지만, 이미 수행된 물리적 행동(물체 이동 등)은 복구 불가
- **PragmaBot [2025]**: 실세계 경험으로부터 학습하여 실패 확률 자체를 줄임. "일단 안전한 것만 시도"하는 보수적 전략

### 근본적 차이의 원인
1. **물리적 비가역성**: 열역학 제2법칙. 엔트로피는 증가한다
2. **안전 비용**: 코드 실패 = 프로세스 중단. 로봇 실패 = 물리적 손상, 인간 위험
3. **실험의 비대칭적 비용**: 코드는 시도 비용 ≈ 0. 로봇은 시도 비용 >> 0
4. **보수적 정책의 필요성**: "일단 해보자"가 아닌 "안전한 것만 해보자"

### 간극을 줄이기 위한 최근 시도
| 접근 | 논문 | 핵심 아이디어 | 한계 |
|------|------|-------------|------|
| Robot constitution | AutoRT (2024) | LLM이 안전 규칙 생성 | 규칙의 완전성 보장 불가 |
| Conservative planning | PragmaBot (2025) | 경험 기반 보수적 행동 선택 | 과도한 보수성 → 비효율 |
| Hierarchical recovery | BUMBLE (2024) | 실패 감지 → 재계획 (물리 복구는 불가) | 복구가 아닌 우회(workaround) |
| Sim pre-verification | SIMPLER (2024) | 실행 전 시뮬레이션 검증 | sim2real gap으로 보장 불완전 |

### Gap 심각도: ★★★★★ (5/5)
원리적으로 해소 불가능한 간극. Agentic Robotics는 "undo 없는 세계"에서 작동해야 한다는 근본 제약. 해결 방향은 "복구" 대신 "예방"과 "우아한 실패(graceful degradation)".

---

## 종합 간극 매트릭스

| 차원 | Gap 심각도 | 핵심 병목 | 가장 유망한 접근 | Agentic Coding 대응 |
|------|-----------|----------|----------------|-------------------|
| 1. Error Feedback | ★★★★★ | 피드백의 질과 명확성 | VLM 기반 실패 진단 (REFLECT) | Stack trace, test output |
| 2. Execution Determinism | ★★★★☆ | 확률적 물리 세계 | Diffusion Policy, 대규모 데이터 | Docker, deterministic build |
| 3. State Representation | ★★★★☆ | 부분 관측, 멀티모달 | 3D Scene Graph (SayPlan) | AST, file system, DOM |
| 4. Memory Architecture | ★★★☆☆ | 실시간 + 대규모 | KARMA, Embodied-RAG | Long context, persistent files |
| 5. Action Space | ★★★★☆ | 연속 + 접촉 역학 | Hierarchical VLA (HAMSTER) | API calls, code edits |
| 6. Verification | ★★★★★ | Sim2Real gap, 비용 | SIMPLER, Fleet testing | Unit test, CI/CD |
| 7. Recoverability | ★★★★★ | 물리적 비가역성 | Safety constraints (AutoRT) | git revert, undo |

## 핵심 통찰

### 1. 세 개의 "해소 불가능 간극"
Error Feedback, Verification, Recoverability는 물리 세계의 근본 속성에서 비롯되어 완전 해소가 원리적으로 불가능하다. 이 세 차원은 "극복"이 아닌 "적응" 전략이 필요하다.

### 2. Code-as-Policy 패러다임의 전략적 가치
Code-as-Symbolic-Planner, CaP, CaP-X가 보여주는 "코드를 중간 표현으로 사용" 접근은 Action Space와 Verification 간극을 동시에 줄인다. 코드는 이산적이고 검증 가능하며 재사용 가능하다.

### 3. Hierarchical Abstraction이 공통 해결 방향
거의 모든 차원에서 "계층적 추상화"가 유망한 접근으로 등장한다:
- Action Space: HAMSTER의 coarse-to-precise 계층
- Memory: KARMA의 LTM/STM 분리
- Verification: SIMPLER의 sim→real 계층
- Error Feedback: REFLECT의 raw observation→symbolic explanation 계층

### 4. Agentic Coding의 성공 요인을 Robotics에 이식하기
Agentic Coding이 작동하는 핵심 이유:
1. **빠르고 정확한 피드백** → Robotics에선 VLM 기반 피드백 강화
2. **저비용 실험** → Robotics에선 sim 환경 고도화
3. **쉬운 복구** → Robotics에선 safety-first 설계
4. **구조화된 상태** → Robotics에선 scene graph 채택

이 4가지 이식이 Agentic Robotics의 성숙도를 결정한다.

---

## 추가 조사 필요 영역

1. **Tactile feedback의 에러 피드백 기여**: 촉각 센서가 Error Feedback 간극을 얼마나 줄이는지에 대한 정량적 연구 필요
2. **Real-time memory의 latency benchmark**: KARMA, Embodied-RAG 등의 실제 추론 지연 시간 비교
3. **CaP-X (2026)의 구체적 성과**: Agentic Coding 벤치마킹 프레임워크의 최신 결과
4. **GR00T N1의 dual-system 아키텍처**: System 2 reasoning + System 1 action이 7대 차원에 미치는 영향

> researcher에게 요청: 위 4개 영역에 대한 추가 조사 부탁
