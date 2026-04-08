# 패러다임 전환 타임라인: LLM Planner에서 Agentic Robotics까지

> Critical Analyst 산출물 | 2026-04-08
> 2022-2026 주요 패러다임 전환 분석

---

## 개요

2022년부터 2026년까지 LLM과 로봇의 교차점에서 네 번의 주요 패러다임 전환이 발생했다. 각 전환은 이전 패러다임의 한계를 인식하고 이를 극복하려는 시도에서 비롯되었다.

```
2022          2023              2024                2025-2026
 │              │                 │                    │
 ▼              ▼                 ▼                    ▼
LLM as        Multimodal        Open VLA            Agentic
External      Integration       Ecosystem           Closed-Loop
Planner       (end-to-end)      (democratization)   Systems
```

---

## 전환 1: LLM as External Planner (2022)

### 이전 패러다임
- 로봇 계획은 PDDL, behavior tree 등 수작업 설계에 의존
- 새 작업마다 전문가가 계획 로직을 재설계해야 함
- 자연어 이해와 로봇 제어는 별개의 파이프라인

### 전환 계기
- **LLM as Zero-Shot Planners [Huang et al., 2022]**: GPT-3가 자연어 지시를 행동 시퀀스로 분해 가능함을 최초로 보임. "Make breakfast" → ["open fridge", "take out eggs", "close fridge", ...]
- **SayCan [Ahn et al., 2022]**: LLM의 계획 능력 + 로봇 affordance model의 결합. LLM이 "할 수 있는 것"과 "해야 하는 것"을 조합하여 실행 가능한 계획 생성
- **Code as Policies (CaP) [Liang et al., 2022]**: LLM이 자연어 지시를 Python 코드로 변환. 코드가 로봇 API를 호출하여 제어. "서랍에서 빨간 컵을 꺼내줘" → Python 프로그램

### 새 패러다임
- LLM이 자연어 → 행동 계획의 "번역기" 역할
- 로봇은 LLM의 출력을 실행하는 "실행기(executor)"
- 코드가 로봇 제어의 새로운 인터페이스로 부상

### Agentic Coding 대응
이 시기는 Copilot(2021), ChatGPT(2022)의 등장과 일치. Agentic Coding에서도 LLM이 코드 생성의 "외부 플래너"로 사용되기 시작:
- 자연어 → 코드 생성 (GitHub Copilot)
- 인간이 검토 → 수정 → 실행하는 반자동 루프

### 남은 Gap
1. **Grounding 문제**: LLM은 물리 세계를 "모른다". SayCan의 affordance model은 수작업으로 학습
2. **Open-loop 실행**: 계획을 세우면 끝. 실행 중 실패 대응 불가
3. **Perception-Planning 분리**: LLM은 텍스트만 처리. 이미지, 센서 데이터를 직접 보지 못함
4. **CaP의 한계**: 코드 생성이 가능하나, 코드가 "물리적으로 실행 가능한지" 검증 불가

### 핵심 수치
- SayCan: 84% planning success (kitchen tasks, 101 tasks)
- LLM as Planners: VirtualHome 환경에서 executability 향상이지만, 순수 LLM은 환경 grounding 없이 ~40% 수준
- CaP: 39개 로봇 작업에서 사전 학습 없이 즉시 사용 가능

---

## 전환 2: Multimodal Integration — End-to-End VLA (2023)

### 이전 패러다임 (전환 1)
- LLM은 텍스트만 처리 → 별도 perception 모듈 필요
- Planning과 Control이 분리된 파이프라인 → 모듈 간 정보 손실
- Affordance model, scene descriptor 등 중간 모듈이 병목

### 전환 계기
- **PaLM-E [Driess et al., 2023]**: 562B 파라미터. 이미지, 로봇 상태, 텍스트를 하나의 언어 모델에 통합. "보고, 읽고, 행동하는" 통합 모델의 가능성 제시
- **RT-2 [Brohan et al., 2023]**: VLM(PaLI-X, 55B)을 로봇 action token으로 fine-tune. 웹에서 학습한 시각-언어 지식이 로봇 제어로 직접 전이(transfer). "Emergent capabilities": 학습하지 않은 물체/지시에도 일반화
- **Open X-Embodiment [O'Brien et al., 2023]**: 22개 로봇 embodiment, 527개 스킬, 100만+ 에피소드의 통합 데이터셋. Cross-embodiment 일반화의 데이터 기반 구축

### 새 패러다임
- **VLA (Vision-Language-Action)**: 하나의 모델이 이미지를 보고(V), 지시를 이해하고(L), 행동을 출력(A)
- End-to-end 학습: 모듈 분리 없이 입력→출력을 직접 매핑
- 웹 스케일 사전 학습의 로봇 전이: 인터넷 이미지/텍스트 지식 → 로봇 제어 능력

### Agentic Coding 대응
2023년은 GPT-4(멀티모달), Claude(100K context)의 해:
- 코드 에이전트도 스크린샷 이해, 에러 메시지 해석, 멀티모달 입력 처리 가능
- "보고 이해하고 행동"하는 통합 에이전트의 출현 (예: GPT-4V 기반 UI 자동화)
- 그러나 코드 에이전트는 이미 텍스트 기반으로 충분히 작동 — 멀티모달의 필요성이 로봇보다 낮음

### 남은 Gap
1. **모델 크기와 실시간성**: PaLM-E 562B, RT-2 55B → 로봇의 실시간 제어(100Hz+)에 부적합
2. **데이터 부족**: 웹 데이터는 풍부하나, 로봇 action 데이터는 여전히 희소
3. **Fine-grained control**: VLA는 high-level 의도는 이해하나, 정밀한 모터 제어는 미흡
4. **Closed-source**: RT-2, PaLM-E 모두 Google 내부. 재현/확장 불가

### 핵심 수치
- RT-2: emergent evaluation에서 기존 RT-1 대비 2배 성능. 학습하지 않은 물체에 대해 62% 성공
- PaLM-E: OK-VQA에서 state-of-the-art, robot planning에서도 sequence-level 성공률 향상
- Open X-Embodiment: RT-1-X는 in-domain 대비 out-of-domain에서도 50%+ 전이 성공

---

## 전환 3: Open VLA Ecosystem — 민주화 (2024)

### 이전 패러다임 (전환 2)
- VLA는 Google, DeepMind 등 대기업 독점
- 재현 불가능한 연구 → 커뮤니티 발전 저해
- 데이터셋도 비공개 → 독립 연구 불가

### 전환 계기
- **Octo [Ghosh et al., 2024]**: Open X-Embodiment 기반 오픈소스 generalist policy. 다양한 로봇에 fine-tuning 가능. 93M 파라미터로 경량
- **OpenVLA [Kim et al., 2024]**: 7B VLA 모델을 완전 오픈소스로 공개. Llama 2 backbone + ViT. 연구자가 자체 데이터로 fine-tune 가능
- **pi0 [Black et al., 2024]**: Physical Intelligence의 flow-matching 기반 generalist policy. 다양한 dexterous manipulation 성공. 산업 수준의 성능
- **pi0.5 [2025]**: open-world generalization + long-horizon dexterous manipulation으로 확장
- **Diffusion Policy [Chi et al., 2023]**: 확률적 행동 생성의 표준 프레임워크로 자리잡음
- **DROID [Khazatsky et al., 2024]**: 대규모 in-the-wild 데이터셋 공개

### 새 패러다임
- **오픈소스 VLA 생태계**: 누구나 VLA 모델을 학습, 수정, 배포 가능
- **Fine-tuning 패러다임**: 사전 학습된 generalist를 특정 로봇/작업에 적응
- **Flow/Diffusion 기반 정책**: deterministic 대신 확률적, 다봉(multimodal) action 분포 학습
- **GR00T N1 [NVIDIA, 2025]**: humanoid 로봇용 dual-system VLA. System 2(reasoning) + System 1(fast action). VLA를 넘어 인지 아키텍처까지 확장

### Agentic Coding 대응
2024년은 Agentic Coding의 폭발적 성장기:
- **Claude Code, Cursor, Devin, Windsurf**: 코드 에이전트가 상용화
- **오픈소스 에이전트**: SWE-Agent, OpenHands 등 오픈소스 코드 에이전트 등장
- **에이전트 벤치마크**: SWE-bench가 표준 평가로 자리잡음
- **공통점**: 오픈소스 민주화가 양쪽에서 동시에 진행. Robotics는 ~2년 지연

### 남은 Gap
1. **Generalist의 한계**: OpenVLA, Octo는 특정 작업에서 task-specific policy에 밀림
2. **Fine-tuning 비용**: 여전히 상당한 컴퓨팅/데이터 필요
3. **Embodiment 다양성**: 각 로봇 하드웨어의 차이가 큼 → 진정한 cross-embodiment 일반화 미달성
4. **Long-horizon 한계**: 단일 manipulation은 가능하나, 연쇄 작업은 여전히 취약

### 핵심 수치
- OpenVLA (7B): RT-2-X (55B) 대비 유사 성능, 모델 크기 1/8
- Octo: 9개 로봇 플랫폼에서 out-of-the-box 작동. Fine-tuning 후 55% 성공률 (WidowX)
- pi0: 5개 dexterous manipulation task에서 인간 시연 대비 80%+ 성공률
- DROID: 564개 장면, 76개 기관 참여 — 로봇 데이터셋 역사상 최대 규모

---

## 전환 4: Agentic Closed-Loop Systems (2025-2026)

### 이전 패러다임 (전환 3)
- VLA는 "한 번에 하나의 작업"을 수행하는 정책
- Open-loop 또는 단순한 재시도 수준의 피드백
- 장기(long-horizon) 작업에서 누적 에러로 실패
- 자율적 판단/재계획/학습이 부재

### 전환 계기
- **BUMBLE [Garrett et al., 2024]**: VLM이 building 규모에서 mobile manipulation을 계획, 실행, 실패 감지, 재계획하는 폐루프 시스템. navigation + manipulation + reasoning 통합
- **REFLECT [Liu et al., 2023]**: 실패 경험을 요약하고 원인을 진단하여 다음 시도에 반영. "로봇이 실패에서 배우는" 최초의 체계적 시도
- **AutoRT [Brohan et al., 2024]**: 20+ 로봇을 LLM이 자율 지시. 안전 규칙(robot constitution)을 자동 생성. 대규모 fleet 운영의 첫 사례
- **PragmaBot [2025]**: 실세계에서 직접 경험하며 작업 계획을 학습하는 "실용주의 로봇". 시뮬레이션 의존도를 줄이고 실환경 데이터로 적응
- **CaP-X [2026]**: Code-as-Policy의 "agentic 버전". 코드 에이전트가 로봇 조작을 벤치마킹. Agentic Coding의 code→execute→debug 루프를 Robotics에 이식
- **Code-as-Symbolic-Planner [2025]**: LLM 생성 코드가 symbolic planner/solver/checker 역할. 단순 API glue가 아닌 "추론하는 코드"

### 새 패러다임
- **폐루프(Closed-loop)**: 계획 → 실행 → 관찰 → 재계획의 지속적 루프
- **자기 반성(Self-reflection)**: 실패를 진단하고 학습에 반영
- **Safety-aware autonomy**: 자율성과 안전성의 균형
- **Code as reasoning interface**: 코드가 단순 제어가 아닌 추론의 매개체
- **경험 기반 적응**: 사전 학습이 아닌 실시간 경험으로 행동 수정

### Agentic Coding 대응
2025-2026년 Agentic Coding은 이미 성숙기:
- **Claude Code**: code → execute → observe error → fix → re-execute 루프가 완전 자동
- **자기 반성**: 에러 패턴을 인식하고 접근 방식 자체를 변경
- **도구 사용**: 파일 시스템, 터미널, 브라우저를 자유롭게 활용
- **장기 작업**: 수백 줄의 리팩토링, 전체 기능 구현을 자율적으로 수행
- **핵심 차이**: Agentic Coding은 이미 "production-ready". Agentic Robotics는 "research prototype" 단계

### 남은 Gap
1. **루프 속도**: 코드 에이전트의 루프는 수초. 로봇 에이전트의 루프는 수분~수십분
2. **실패 비용**: 코드 에이전트의 실패 = 되돌리기. 로봇 에이전트의 실패 = 물리적 결과
3. **일반화**: 코드 에이전트는 모든 프로그래밍 언어/프레임워크에 작동. 로봇 에이전트는 특정 하드웨어/환경에 제한
4. **자율성 수준**: 코드 에이전트는 인간 개입 없이 작업 완료. 로봇 에이전트는 여전히 인간 감독 필수

### 핵심 수치
- BUMBLE: building-scale mobile manipulation, 다층 건물에서 작동
- AutoRT: 20+ 로봇 fleet 동시 운영, 77,000+ 에피소드 수집
- REFLECT: failure correction으로 재시도 성공률 향상 (baseline 대비 +20%p)
- CaP-X: Agentic Coding 메트릭을 로봇 조작에 최초 적용

---

## 전환 간 연결 구조

```
전환 1 (2022)              전환 2 (2023)
LLM External Planner  ──→  Multimodal VLA
    │                          │
    │ "텍스트만으론 부족"      │ "모델이 너무 크고 비공개"
    │                          │
    ▼                          ▼
전환 3 (2024)              전환 4 (2025-26)
Open VLA Ecosystem    ──→  Agentic Closed-Loop
    │                          │
    │ "한 번에 하나의 작업"    │ "자율적 반복 학습"
    └──────────────────────────┘
```

### 전환 동인 패턴
1. **전환 1→2**: 모달리티 통합 필요성 (텍스트 → 이미지+텍스트+행동)
2. **전환 2→3**: 접근성 문제 (closed → open)
3. **전환 3→4**: 자율성 문제 (one-shot → closed-loop)

각 전환은 정확히 하나의 핵심 한계를 해소하면서 새로운 한계를 노출하는 패턴을 보인다.

---

## Agentic Coding과의 시간축 비교

| 연도 | Agentic Coding | Agentic Robotics | 지연 |
|------|---------------|-----------------|------|
| 2021 | Copilot (코드 자동완성) | — | — |
| 2022 | ChatGPT (대화형 코드 생성) | SayCan, CaP (LLM 플래너) | 동시 |
| 2023 | GPT-4 멀티모달, 100K context | PaLM-E, RT-2 (VLA 등장) | 동시 |
| 2024 | Claude Code, Cursor, Devin (Agentic) | OpenVLA, pi0 (오픈 VLA) | ~1년 지연 |
| 2025 | Production-ready agentic coding | BUMBLE, PragmaBot (폐루프 프로토타입) | ~2년 지연 |
| 2026 | 산업 표준 | CaP-X (벤치마킹 시작) | ~2년 지연 |

### 핵심 관찰
Agentic Robotics는 Agentic Coding 대비 약 **1-2년의 패러다임 지연**을 보인다. 그러나 이 지연은 단순한 "기술 성숙 시간"이 아니라, 물리 세계의 근본적 제약(7대 차원 간극)에서 비롯된다. 따라서 Agentic Coding의 발전 궤적을 그대로 따라가지 않고, 독자적인 해결 경로(hierarchical abstraction, safety-first design, sim-augmented verification)를 개척하고 있다.

---

## 다음 전환 예측: 2026-2027

### 유력한 전환 5: Embodied World Models
- **근거**: VLA가 "반응적(reactive)" 정책에 머물러 있음. "미래를 예측하고 계획하는" 내부 세계 모델(world model) 통합이 다음 단계
- **징후**: GR00T N1의 dual-system, Code-as-Symbolic-Planner의 symbolic reasoning, 그리고 video prediction model의 발전
- **Agentic Coding 대응**: 코드 에이전트는 이미 "실행 전 결과 예측"이 가능 (type checking, static analysis). 로봇도 "행동 전 결과 시뮬레이션"이 가능해야 함

### 필요 조건
1. 실시간 물리 예측 모델 (현재 수초 → 수밀리초 필요)
2. 예측의 불확실성을 정량화하고 의사결정에 반영
3. 예측 실패 시 graceful fallback 메커니즘
