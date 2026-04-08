---
title: "목차"
subtitle: "Table of Contents"
date: "2026-04-08"
last_updated: "2026-04-08"
---

# LLM 플래너에서 에이전틱 로보틱스까지 — Physical AI의 미래

## 목차

---

### Part I: 기초 — LLM이 로봇을 만나다

**Chapter 1. 서론 — Agentic Coding에서 Agentic Robotics로**
- 1.1 Agentic AI란 무엇인가
- 1.2 Agentic Coding의 성공: code → tool → execution → error → LLM 루프
- 1.3 물리 세계로의 확장: 왜 같은 루프가 작동하지 않는가
- 1.4 7대 차원 간극 — 본서의 핵심 프레임워크
- 1.5 본서의 구성과 읽는 법

**Chapter 2. LLM as Planner — 제로샷 계획과 그라운딩**
- 2.1 LLM의 세계 지식을 로봇 계획에 활용하기
- 2.2 Language Models as Zero-Shot Planners [Huang et al., 2022]
  - 방법론: Semantic Translation + Autoregressive Correction
  - 결과: Executability 18% → 79%, Correctness 32.87%
  - 한계: 접지 부재, 폐루프 부재
- 2.3 SayCan: 언어를 로봇 어포던스에 접지하기 [Ahn et al., 2022]
  - 핵심: P(action) = P_LLM(useful) × P_affordance(feasible)
  - 결과: PaLM-SayCan 84% 계획 성공률, 74% 실행 성공률 (101 tasks)
  - 한계: 폐쇄형 스킬 세트(551개), 정적 어포던스
- 2.4 SayPlan: 3D 씬 그래프로 대규모 환경 계획 [Rana et al., 2023]
  - 핵심: 3D Scene Graph의 계층적 축소/확장
  - 결과: 3층 36개 방 140+ 객체 환경에서 장기 작업 계획
  - 한계: 정적 그래프, 환각 잔존 6.67%
- 2.5 진화 경로: "생성" → "접지" → "구조화"
- 2.6 Agentic Coding 대비: 관찰-행동 간극의 부재 vs 존재

**Chapter 3. Code as Policies — 코드로 로봇을 제어하다**
- 3.1 코드가 자연어보다 나은 로봇 제어 인터페이스인 이유
- 3.2 Code as Policies [Liang et al., 2022]
  - 방법론: Few-shot prompting → 로봇 정책 코드 생성
  - 결과: Seen instructions >90% 성공, 공간-기하학적 추론 입증
  - 한계: 추상 수준 불일치, Error recovery 부재
- 3.3 Code-as-Symbolic-Planner [Chen et al., 2025]
  - 핵심: 코드 = solver / planner / checker
  - 결과: 최고 baseline 대비 +24.1% 성공률
- 3.4 CaP-X: 에이전틱 코딩 에이전트의 로봇 벤치마크 [Fu et al., 2026]
  - CaP-Gym (187개 작업), CaP-Bench (3축 평가), CaP-Agent0, CaP-RL
  - 핵심 발견: human-crafted abstraction 제거 시 성능 급락 → 에이전틱 스캐폴딩으로 회복
- 3.5 RL-GPT: 코드 에이전트 + RL 에이전트 [2024]
- 3.6 진화 경로: "API 접착제" → "추론 도구" → "에이전틱 시스템"
- 3.7 Agentic Coding과의 직접 대응: 코드 생성-실행-디버그 루프

---

### Part II: VLA 혁명

**Chapter 4. Vision-Language-Action 모델의 부상**
- 4.1 VLA란 무엇인가: 보고(V), 이해하고(L), 행동한다(A)
- 4.2 PaLM-E: 최초의 대규모 Embodied Multimodal LM [Driess et al., 2023]
  - 562B 파라미터, positive transfer 입증
- 4.3 RT-2: 웹 지식을 로봇 행동으로 전이 [Brohan et al., 2023]
  - Action tokenization, emergent semantic reasoning
  - 결과: 학습 외 물체에 62% 성공, 6000회 평가
- 4.4 Open X-Embodiment: 크로스-Embodiment 데이터의 힘 [2023]
  - 22개 로봇, 527개 스킬, 100만+ 궤적
- 4.5 Octo: 오픈소스 제너럴리스트 정책 [Ghosh et al., 2024]
- 4.6 OpenVLA: 7B 오픈소스 VLA [Kim et al., 2024]
  - RT-2-X(55B) 대비 +16.5%, 모델 크기 1/8
- 4.7 π0 / π0.5: Flow Matching과 Open-World 일반화 [Physical Intelligence, 2024-2025]
  - 세탁물 접기, 새로운 집에서의 주방 청소
- 4.8 GR00T N1: 듀얼 시스템 아키텍처 [NVIDIA, 2025]
  - System 2 (VLM) + System 1 (Diffusion Transformer)
- 4.9 Action Tokenization의 진화: RT-2 → FAST → Flow Matching
- 4.10 VLA의 5대 설계 축과 트레이드오프
- 4.11 Agentic Coding 대비: 이산 텍스트 vs 연속 모터 명령

**Chapter 5. 계층적 계획 — 고수준에서 저수준으로**
- 5.1 왜 계층적 분리가 필요한가: 추상화 간극, 데이터 효율, Off-domain 활용
- 5.2 AutoTAMP: LLM을 번역기+검증기로 [Chen et al., 2023]
  - STL 형식 명세, 다중 에이전트 100% 성공
- 5.3 RT-H: 언어 모션을 중간 표현으로 [Belkhale et al., 2024]
  - "move arm forward" — 작업 간 저수준 모션 공유
- 5.4 Hi Robot: 인간 피드백 실시간 통합 [Shi et al., 2025]
  - VLM + Low-level policy 분리, 원자적 명령 경유
- 5.5 HAMSTER: Off-Domain 데이터의 힘 [Li et al., 2025]
  - OpenVLA 대비 +20%, 비디오/스케치/시뮬레이션 활용
- 5.6 계층적 분리의 네 가지 형태: 형식 명세 / 언어 모션 / 2D 경로 / 원자적 명령
- 5.7 Agentic Coding 대비: 의사코드와 언어 모션의 구조적 유사성

**Chapter 6. 저수준 제어 — Diffusion Policy와 3D 표현**
- 6.1 고수준 계획이 실행되는 곳: 저수준 정책의 역할
- 6.2 Diffusion Policy [Chi et al., 2023]
  - 행동을 조건부 denoising diffusion으로 생성, 기존 SOTA 대비 +46.9%
- 6.3 3D Diffuser Actor [Ke et al., 2024]
  - 3D scene representation + diffusion policy 결합
- 6.4 DROID: 대규모 실환경 데이터셋 [Khazatsky et al., 2024]
  - 13개 기관, 564개 장면 — 역대 최대 규모
- 6.5 TinyVLA: 경량 VLA의 가능성 [2024]
  - <1B 파라미터, OpenVLA 대비 +25.7%
- 6.6 FAST: Action Tokenization 혁신 [2025]
  - DCT 기반, 학습 시간 5배 단축
- 6.7 Agentic Coding 대비: "실행 엔진"의 결정론성 vs 확률성

---

### Part III: 에이전틱 로보틱스를 향하여

**Chapter 7. 메모리와 세계 표현**
- 7.1 로봇이 장기 작업을 수행하려면 무엇을 기억해야 하는가
- 7.2 KARMA: 장기/단기 기억 시스템 [Wang et al., 2024]
  - 3D 씬 그래프 장기 기억 + 동적 단기 기억
  - Complex Tasks에서 2.3배 성공률, 62.7배 효율 향상
- 7.3 Embodied-RAG: 공간-의미 계층 검색 [Xie et al., 2024]
  - 토폴로지 맵 + Semantic Forest
- 7.4 RoboEXP: 행동 조건 씬 그래프 [Jiang et al., 2024]
  - 능동적 탐색, "어떻게 조작할 수 있는가" 포함
- 7.5 VeriGraph: 실행 검증을 위한 씬 그래프 [Ekpo et al., 2024]
  - Language-based +58%, Image-based +30%
- 7.6 MoMa-LLM, 3D-Mem, RoboMemory: 진화하는 메모리 아키텍처
- 7.7 씬 그래프의 네 가지 용도: 계획 / 행동조건 / 검색 / 검증
- 7.8 Agentic Coding 대비: 파일 시스템 vs 3D 씬 그래프, grep vs 공간 검색

**Chapter 8. 폐루프 에이전틱 시스템**
- 8.1 Open-loop에서 Closed-loop으로: 왜 피드백이 필수인가
- 8.2 REFLECT: 실패에서 배우기 [Liu et al., 2023]
  - VLM 기반 실패 요약 및 원인 진단
- 8.3 AutoRT: 대규모 로봇 Fleet 자율 운영 [Brohan et al., 2024]
  - 20+ 로봇 동시 운영, 77,000+ 에피소드, Robot Constitution
- 8.4 BUMBLE: 빌딩 규모 모바일 매니퓰레이션 [Garrett et al., 2024]
  - Navigation + Manipulation + Reasoning 통합, 실패 감지 → 재계획
- 8.5 PragmaBot: 실세계 경험으로 학습하는 실용주의 로봇 [2025]
  - 보수적 행동 전략, 시뮬레이션 의존도 감소
- 8.6 폐루프의 핵심 요소: 감지 → 진단 → 재계획 → 실행
- 8.7 Agentic Coding 대비: code→execute→error→fix 루프의 물리 세계 버전

**Chapter 9. Sim-to-Real 전이와 평가**
- 9.1 시뮬레이션의 약속과 한계: Sim2Real Gap
- 9.2 SIMPLER: 시뮬레이션에서 실환경 정책 평가 [Li et al., 2024]
  - VLA/generalist policy 비교 벤치마크
- 9.3 Natural Language Sim2Real [2024]
  - 의미 수준에서 sim-real 매칭 (픽셀 대신 언어)
- 9.4 Vision Encoder Pre-Training for Sim2Real Transfer [2025]
- 9.5 CaP-X의 Sim2Real: CaP-RL의 최소 격차 달성 [2026]
- 9.6 Agentic Coding 대비: Simulation ≈ Production vs Sim2Real Gap

---

### Part IV: 근본적 차이 — 디지털 에이전트 vs 물리 에이전트

**Chapter 10. Agentic Coding vs Agentic Robotics — 간극과 미래**
- 10.1 7대 차원 간극 종합 분석
  - Error Feedback (★★★★★): 스택 트레이스 vs 센서 노이즈
  - Execution Determinism (★★★★☆): 재현성 vs 확률성
  - State Representation (★★★★☆): AST/파일 vs 씬 그래프
  - Memory Architecture (★★★☆☆): Long context vs 공간 메모리
  - Action Space (★★★★☆): API 호출 vs 연속 모터 명령
  - Verification (★★★★★): 단위 테스트 vs 물리 실험
  - Recoverability (★★★★★): git revert vs 물리적 비가역성
- 10.2 패러다임 전환 타임라인 (2022-2026)
  - 전환 1: LLM as External Planner (2022)
  - 전환 2: Multimodal VLA (2023)
  - 전환 3: Open VLA Ecosystem (2024)
  - 전환 4: Agentic Closed-Loop (2025-2026)
- 10.3 8대 미해결 문제
  - 물리적 피드백 의미 변환 [근본적]
  - 실시간 세계 모델 [구조적]
  - Cross-Embodiment 일반화 [구조적]
  - Long-Horizon 누적 에러 [구조적]
  - Safety-Autonomy 균형 [근본적]
  - 데이터 효율성 [실용적]
  - 실시간 추론 [실용적]
  - 평가 표준 부재 [실용적]
- 10.4 다음 전환 예측: Embodied World Models (2026-2027)
- 10.5 Agentic Coding의 성공 요인을 Robotics에 이식하기
  - 빠르고 정확한 피드백 → VLM 기반 피드백
  - 저비용 실험 → Sim 환경 고도화
  - 쉬운 복구 → Safety-first 설계
  - 구조화된 상태 → Scene graph 채택
- 10.6 결론: 물리 세계의 에이전틱 AI를 향하여

---

## 참고문헌

→ `references.bib` (통합 BibTeX)

---

## 부록

**Chapter 11. 참고 — Agentic Coding 시스템의 구조**
- 11.1 도입: 왜 코딩 에이전트의 내부를 들여다보는가
- 11.2 Claude Code의 아키텍처
  - 3층 메모리 시스템 (CLAUDE.md / 세션 컨텍스트 / 도구 기반 검색)
  - 도구 오케스트레이션 (Read, Edit, Bash, Grep, Agent)
  - 서브에이전트와 병렬 실행
  - 피드백 루프: 에러에서 수정까지
  - 권한 모델과 안전 장치
- 11.3 OpenAI Codex의 아키텍처
  - 컨테이너 기반 샌드박스
  - AGENTS.md — CLAUDE.md에 대응
  - codex-1에서 GPT-5.3-Codex로
  - 통합 서버 아키텍처
- 11.4 공통 성공 패턴 분석 (6대 패턴)
- 11.5 Agentic Robotics로의 이식
- 11.6 미래 전망: 물리 세계의 Claude Code
- 11.7 결론

---

- A. 논문 간 영향 관계 맵 (4대 연구 흐름)
- B. 연구 그룹별 기여 정리
- C. 핵심 약어 및 용어 정리
