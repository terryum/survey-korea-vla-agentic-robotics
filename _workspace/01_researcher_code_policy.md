# Code as Policy — 심층 서베이

> 카테고리 핵심 질문: **코드가 왜 자연어보다 나은 로봇 제어 인터페이스인가?**

이 카테고리는 LLM이 자연어 대신 **코드를 생성하여** 로봇을 제어하는 패러다임을 다룬다. 코드는 자연어 대비 (1) 정밀한 수치 표현, (2) 조건/반복 등 제어 흐름, (3) 외부 라이브러리 활용, (4) 실행·검증 가능성이라는 장점을 가진다. 이 흐름은 2022년 CaP에서 시작하여 2025년 심볼릭 플래너, 2026년 에이전틱 벤치마크까지 발전했다.

---

## 1. 핵심 논문 분석

### 1.1 Code as Policies (CaP) (2022)

- **arXiv**: https://arxiv.org/abs/2209.07753
- **저자**: Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, Andy Zeng (Google Research)
- **학회**: ICRA 2023

#### 핵심 Contribution
LLM(코드 완성용으로 학습된)을 재활용하여 자연어 명령에서 **로봇 정책 코드**를 직접 생성하는 패러다임을 확립했다. 코드가 perception API 호출, 제어 파라미터화, 피드백 루프를 표현할 수 있음을 보였다.

#### 방법론
- **Policy Code**: LLM이 생성한 코드가 object detector 출력을 처리하고, 제어 primitive API를 파라미터화
- **Few-shot Prompting**: 자연어 명령(주석)과 대응하는 정책 코드 예시를 프롬프트로 제공
- **Third-party Library 활용**: NumPy, Shapely 등을 참조하여 공간-기하학적 추론 수행
- **Hierarchical Code Generation**: 복잡한 작업을 함수 호출 계층으로 분해

#### 주요 결과
| 평가 조건 | 성공률 |
|----------|-------|
| Seen instructions/attributes (시뮬레이션) | **>90%** |
| Unseen instructions/attributes | Supervised IL baseline 대비 우수 |
| Spatial reasoning 작업 | Language-only planning 대비 유의미하게 우수 |

- 실제 로봇 데모: 모바일 로봇 주방 내비게이션/조작, 로봇팔 도형 그리기, pick-and-place, tabletop 조작
- 공간-기하학적 추론, 새로운 지시 일반화, 정밀한 수치 지정 능력 입증

#### 한계점
- **추상 수준 불일치**: 프롬프트와 새 명령의 추상 수준이 다르면 성능 저하 (예: "복잡한 구조물 조립"처럼 추상 수준이 높은 작업)
- **Greedy Decoding 한계**: LLM의 greedy decoding이 복잡한 구조 생성에 어려움
- **Error Recovery 부재**: 생성된 코드가 실행 시 실패하면 자동 수정 메커니즘 없음
- **사전 정의된 API 의존**: perception/control primitive API가 사전에 설계되어야 함

#### 영향
- **"Code as Policy" 패러다임**의 명명과 확립
- Code-as-Symbolic-Planner, CaP-X, RL-GPT 등 직접 후속 연구
- Agentic Coding의 "도구 사용(tool use)" 패턴과 구조적으로 동일 → 로봇 도메인에서의 tool use
- 인용 수 500+

#### Agentic Coding 대비
CaP는 **Agentic Coding과 가장 직접적으로 대응**되는 로봇 패러다임이다. Claude Code가 bash/python 코드를 생성하고 실행하여 결과를 관찰하는 것처럼, CaP는 LLM이 로봇 제어 코드를 생성하고 실행한다. 핵심 차이: (1) 디지털 환경은 결정론적이고 즉시 관찰 가능하지만, 로봇 환경은 확률적이고 센서 노이즈가 있다. (2) 코드 실행 실패 시 디지털에서는 에러 메시지가 명확하지만, 로봇에서는 "왜 실패했는지" 판단 자체가 어렵다.

---

### 1.2 Code-as-Symbolic-Planner (2025)

- **arXiv**: https://arxiv.org/abs/2503.01700
- **저자**: Yongchao Chen, Yilun Hao, Yang Zhang, Chuchu Fan (MIT)
- **학회**: IROS 2025

#### 핵심 Contribution
LLM이 코드를 단순한 API 접착제(glue)가 아니라 **solver, planner, checker**로 사용하도록 유도하는 접근. 심볼릭 계산이 필요한 TAMP 문제에서 텍스트 추론만으로는 불충분한 부분을 코드 생성으로 보완한다.

#### 방법론
- LLM이 **최적화 코드**(solver)를 생성하여 제약 조건 하의 계획 문제를 풀도록 함
- 텍스트 추론(common sense)과 코드 생성(symbolic computing)을 결합
- 코드가 **제약 검증(checker)** 역할도 수행 → 자기 검증 루프

#### 주요 결과
- 최고 baseline 대비 평균 **24.1% 성공률 향상**
- 복잡도가 높은 작업에서 특히 **스케일러빌리티** 우수
- 단순 코드 생성(CaP 스타일)과 달리, 코드가 "사고의 도구"로 작동

#### 한계점
- LLM의 코드 생성 품질에 크게 의존
- solver 코드의 정확성 보장이 어려움 (특히 복잡한 최적화 문제)
- 실제 로봇 환경에서의 검증이 제한적

#### 영향
- CaP의 "코드 = API 호출"에서 "코드 = 추론 도구"로 패러다임 확장
- LLM이 코드를 통해 수학적/논리적 추론을 보강할 수 있음을 입증
- AutoTAMP(2023)의 "LLM을 translator+checker로 쓴다"는 아이디어와 합류

#### Agentic Coding 대비
Agentic Coding에서 LLM은 이미 코드를 "사고의 도구"로 사용한다 — 예를 들어 정규식을 생성하여 패턴을 검증하거나, 스크립트를 작성하여 데이터를 분석한다. Code-as-Symbolic-Planner는 이와 동일한 패턴을 로봇 TAMP에 적용한 것이다. 차이점은 로봇에서의 "실행"이 물리 세계와 상호작용해야 한다는 점.

---

### 1.3 CaP-X: Benchmarking Coding Agents for Robot Manipulation (2026)

- **arXiv**: https://arxiv.org/abs/2603.22435
- **저자**: Max Fu et al. (Stanford, Microsoft Research)
- **공개**: 2026년 3월

#### 핵심 Contribution
Code-as-Policy 에이전트를 **체계적으로 연구하고 벤치마킹**하는 오픈소스 프레임워크를 제공한다. 이 분야에서 가장 포괄적인 평가 프레임워크.

#### 방법론 (4개 구성요소)
1. **CaP-Gym**: RoboSuite, LIBERO-PRO, BEHAVIOR 등에서 **187개 작업**을 통합한 인터랙티브 환경. 시뮬레이션과 실제 로봇 모두 호환 가능한 primitive 설계.
2. **CaP-Bench**: 3축 평가 체계:
   - **Abstraction Level**: human-crafted macro → atomic primitive까지 행동 공간 변화
   - **Temporal Interaction**: zero-shot single-turn vs multi-turn interaction
   - **Perceptual Grounding**: 시각 피드백 모달리티의 영향
3. **CaP-Agent0**: 학습 없이(training-free) 여러 조작 작업에서 **인간 수준의 신뢰성** 달성
4. **CaP-RL**: 검증 가능한 보상을 활용한 RL로 성공률 향상, sim2real 전이도 최소 격차

#### 주요 결과 (12개 모델 평가)
- **핵심 발견**: 성능은 human-crafted abstraction과 함께 향상되지만, 이 사전 정의된 추상화가 제거되면 성능이 **급격히 저하**
- **에이전틱 스캐폴딩으로 격차 해소**: multi-turn interaction, structured execution feedback, visual differencing, automatic skill synthesis, ensembled reasoning을 통해 low-level primitive에서도 성능 회복 가능
- CaP-Agent0: 시뮬레이션 및 실제 로봇에서 인간 수준 신뢰성
- CaP-RL: sim2real 전이 시 최소 격차

#### 한계점
- 187개 작업이 실제 산업 현장의 다양성을 완전히 커버하지는 않음
- CaP-Agent0의 "인간 수준 신뢰성"은 특정 작업 집합에 한정
- 에이전틱 스캐폴딩의 연산 비용이 높을 수 있음

#### 영향
- Code-as-Policy 연구의 **벤치마크 표준** 확립
- "에이전틱 test-time computation"이 human-crafted abstraction을 대체할 수 있다는 증거
- Agentic Coding ↔ Agentic Robotics 연결의 가장 직접적인 다리

#### Agentic Coding 대비
CaP-X의 핵심 발견 — **human-crafted abstraction 없이는 성능이 급락하지만, 에이전틱 스캐폴딩으로 회복 가능** — 은 Agentic Coding에서도 관찰되는 패턴이다. 잘 설계된 API/SDK 없이 raw system call만으로 코딩하면 어렵지만, 에이전트가 반복적으로 시도하고 피드백을 받으면 결국 해결 가능하다. CaP-X는 이 대응관계를 **정량적으로 입증**한 첫 번째 연구이다.

---

### 1.4 RL-GPT: Integrating RL and Code-as-Policy (2024)

- **arXiv**: https://arxiv.org/abs/2402.19299
- **저자**: (Google Research 등)
- **학회**: NeurIPS 2024

#### 핵심 Contribution
코드 기반 "느린 에이전트(slow agent)"와 RL 기반 "빠른 에이전트(fast agent)"의 **2단계 계층 프레임워크**를 제안. 코딩 가능한 고수준 행동은 코드로, 정밀 제어가 필요한 저수준 행동은 RL로 처리.

#### 방법론
- **Slow Agent**: 작업을 분석하고 코딩 가능한 행동을 식별
- **Fast Agent**: 코딩 태스크를 실행하며, 단순 행동은 직접 코드로, 복잡한 행동은 코드 + RL 결합
- Minecraft 환경에서 평가

#### 주요 결과
- 전통적 RL 및 기존 GPT 에이전트 대비 **우수한 효율**
- Minecraft에서 RTX3090 단일 GPU로 **1일 내 다이아몬드 획득**

#### 한계점
- Minecraft 환경에 특화된 평가
- 실제 로봇으로의 전이 검증 부재
- Slow/Fast 분리의 최적 기준이 수동 설계됨

#### 영향
- "코드로 할 수 있는 것 vs RL이 필요한 것"의 분리 기준 제시
- Hierarchical Planning 카테고리의 RT-H, Hi Robot과 동일한 "고수준/저수준 분리" 철학

#### Agentic Coding 대비
Agentic Coding에서는 모든 행동이 코드로 표현 가능하므로 slow/fast 분리가 불필요하다. 반면 로봇에서는 "코드로 표현 가능한 이산적 행동"과 "연속적 모터 제어"의 경계가 존재한다. RL-GPT는 이 경계를 명시적으로 다룬 연구.

---

### 1.5 Natural Language as Policies (NLaP) (2024)

- **arXiv**: https://arxiv.org/abs/2403.13801
- **저자**: Yusuke Mikami, Andrew Melnik, Jun Miura, Ville Hautamäki

#### 핵심 Contribution
코드 대신 **자연어 자체를 coordinate-level 제어 명령으로** 사용하는 역방향 접근. 사전 정의된 API 없이 자연어 추론만으로 좌표 수준 명령을 출력.

#### 방법론
- 작업/씬 객체의 텍스트 설명을 입력 받아 자연어 추론으로 좌표 수준 제어 명령 출력
- 중간 표현(코드, API)의 필요성을 줄이는 것이 목표

#### 주요 결과
- Prompt engineering 실험에서 자연어 추론이 성공률을 유의미하게 향상
- 새로운 상황으로의 전이 가능성 시사

#### 한계점
- 정밀 제어에서 코드 기반 접근 대비 한계
- 복잡한 다단계 작업에서 확장성 미검증

#### Agentic Coding 대비
코드 vs 자연어의 trade-off를 보여주는 흥미로운 반례(counter-example). Agentic Coding에서도 때로는 자연어 지시가 코드 작성보다 효율적인 경우가 있지만, 정밀한 작업에서는 코드가 필수적이다.

---

## 2. 카테고리 종합 분석

### 2.1 진화 경로: "API 접착제" → "추론 도구" → "에이전틱 시스템"

```
CaP (2022.09)           Code-as-Sym-Planner (2025.03)    CaP-X (2026.03)
    │                              │                          │
    │ 코드 = API 호출            │ 코드 = solver/           │ 에이전틱 스캐폴딩
    │ + 제어 흐름                │ planner/checker           │ + 벤치마크
    │                              │                          │
    ▼                              ▼                          ▼
  Few-shot code gen       Symbolic computing          Multi-turn interaction
  via LLM                  via code generation         + execution feedback
```

### 2.2 코드 vs 자연어 vs 직접 행동: 세 갈래의 비교

| 차원 | Code as Policy | Natural Language | VLA (직접 행동) |
|------|---------------|-----------------|----------------|
| 정밀도 | 높음 (수치 지정) | 중간 | 높음 (연속 행동) |
| 일반화 | 높음 (새 API 조합) | 높음 (언어 유연성) | 낮음 (학습 데이터 의존) |
| 해석 가능성 | 매우 높음 | 높음 | 낮음 |
| 실시간 반응 | 낮음 (생성+실행) | 낮음 | 높음 |
| 새 환경 적응 | API만 있으면 가능 | 설명만 있으면 가능 | 재학습 필요 |

### 2.3 CaP-X의 핵심 발견과 함의

CaP-X가 밝힌 **"human-crafted abstraction ↔ 성능" 의존성**은 이 분야의 가장 중요한 통찰 중 하나:

1. **문제**: 12개 모델 모두 human-crafted abstraction이 제거되면 성능 급락
2. **해결**: 에이전틱 test-time computation (multi-turn, feedback, visual diff, skill synthesis)으로 격차 해소 가능
3. **함의**: 장기적으로 "사전 설계된 추상화" 대신 "에이전틱 스캐폴딩"이 대안이 될 수 있음
4. **Agentic Coding과의 대응**: 이는 정확히 Agentic Coding에서 "잘 설계된 프레임워크 없이도 에이전트가 반복적 시도로 문제를 해결한다"는 것과 동일한 패턴

---

## 3. 인용 네트워크

```
Code as Policies (2022.09)
    ├──→ Code-as-Symbolic-Planner (2025.03, IROS)
    ├──→ CaP-X (2026.03)
    ├──→ RL-GPT (2024.02, NeurIPS)
    ├──→ Natural Language as Policies (2024.03)
    └──→ Voyager (2023, Minecraft code agent)

AutoTAMP (2023.06) ──→ Code-as-Symbolic-Planner (2025.03)
    └──── "LLM as translator + checker" 아이디어 합류

SayCan (2022.04) ──→ CaP (2022.09)
    └──── affordance에서 code generation으로 패러다임 전환
```

---

## 4. 연구 그룹 매핑

| 그룹 | 핵심 기여 | 방향성 |
|------|---------|-------|
| Google Research (Jacky Liang, Wenlong Huang et al.) | CaP | 코드 생성 패러다임 확립 |
| MIT (Yongchao Chen, Chuchu Fan) | Code-as-Symbolic-Planner | 코드를 추론 도구로 확장 |
| Stanford + Microsoft Research (Max Fu et al.) | CaP-X | 에이전틱 벤치마크 및 스캐폴딩 |
| NeurIPS 2024 | RL-GPT | 코드 + RL 하이브리드 |

---

## 5. Agentic Coding ↔ Code as Policy: 핵심 대비 요약

| 차원 | Agentic Coding | Code as Policy (Robotics) |
|------|---------------|--------------------------|
| 실행 환경 | 결정론적 (컴퓨터) | 확률적 (물리 세계) |
| 에러 피드백 | 명확 (스택 트레이스) | 모호 (센서 노이즈, 부분 관찰) |
| 실행 비용 | 거의 무료, 즉시 | 높음, 시간 소요, 안전 위험 |
| 되돌리기 | `git revert`, undo 가능 | 불가역 (물건 파손, 충돌) |
| API 설계 | 풍부한 에코시스템 | 수동 설계 필요 (CaP-X 발견) |
| 테스트 | 단위/통합 테스트 즉시 | sim2real gap 존재 |

**핵심 통찰**: Code as Policy는 Agentic Coding의 로봇 버전이지만, 물리 세계의 비결정성·비가역성·관찰 비용이 근본적 난점을 추가한다. CaP-X는 이 격차를 에이전틱 스캐폴딩으로 줄일 수 있음을 보였다.

---

*작성일: 2026-04-08*
*서베이 범위: 2022.09 ~ 2026.03*
