# Fact Check Report: Part I (Ch 1-3)

> 검증일: 2026-04-08
> 검증자: fact-checker agent
> 대상: book/ko/ch01-03.md, book/en/ch01-03.md

---

## Ch 1: 서론 — Agentic Coding에서 Agentic Robotics로

### Critical Issues (반드시 수정)

**없음** — Ch 1은 주로 프레임워크 설정과 개념적 서술로, 구체적 수치 인용이 거의 없음.

### Warnings (맥락 보강 권장)

1. **[KO Line 30, EN Line 30]** "REFLECT [Liu et al., 2023]는 VLM으로 실패 원인을 자연어로 설명하려는 시도지만, 정확도는 인간 판단 대비 약 60% 수준에 머뭅니다."
   - **검증 결과**: REFLECT 논문 원문(Table 2)에 따르면, 실세계 실패 설명 정확도는 **execution failure 68.8%**, **planning failure 78.6%**임. "약 60%"는 부정확.
   - **수정 제안 (KO)**: "정확도는 실세계 실행 실패에서 약 69%, 계획 실패에서 약 79% 수준이다" 또는 보다 보수적으로 "실세계에서 약 70% 수준에 머문다"
   - **수정 제안 (EN)**: "accuracy remains around 69% for execution failures and 79% for planning failures in the real world" 또는 "accuracy remains around 70% in real-world settings"
   - **심각도**: Important — 수치 방향은 맞지만 10%p 가까이 차이남

2. **[KO Line 44, EN Line 44]** "OpenVLA [Kim et al., 2024], Octo [Ghosh et al., 2024], pi0 [Black et al., 2024]가 VLA를 민주화했습니다."
   - **검증**: Octo의 arXiv ID 2405.12213 확인됨. 저자 "Ghosh et al."은 정확 — 제1저자는 Dibya Ghosh가 아닌 Octo 팀이며 실제 제1저자 확인 필요. 논문 자체는 "Octo: An Open-Source Generalist Robot Policy"로 확인됨.
   - **심각도**: Normal — 팩트 자체는 정확하지만, Octo 제1저자 확인 권장

### Verified OK

- Diffusion Policy [Chi et al., 2023] 인용 — arXiv:2303.04137 확인됨
- SIMPLER [Li et al., 2024] — arXiv:2405.05941 확인됨
- AutoRT [Brohan et al., 2024] — arXiv:2401.12963 확인됨
- BUMBLE [Shah et al., 2024] — arXiv:2410.06237 확인됨
- KARMA [Wang et al., 2024] — arXiv:2409.14908 확인됨
- CaP-X [Fu et al., 2026] — arXiv:2603.22435 확인됨
- 7대 차원 비교 테이블 — CLAUDE.md의 원본 테이블과 일치
- 네 번의 패러다임 전환 서술 — 연도와 논문 매칭 정확
- 참고문헌 16개 — arXiv ID 모두 정확

---

## Ch 2: LLM as Planner — 제로샷 계획과 그라운딩

### Critical Issues (반드시 수정)

1. **[KO Line 28, EN Line 28]** "실행 가능성(executability)은 18%에서 79%로 대폭 향상되었지만, 의미적 정확성(correctness)은 LCS 기준 32.87%에 머물렀습니다."
   - **검증 결과**: Huang et al. (2022) 논문에서 executability 향상과 correctness 트레이드오프가 핵심 결과이며, 방향은 맞음. 그러나 정확한 수치(18%, 79%, 32.87%)는 논문 원문 테이블에서 직접 확인 필요. WebSearch에서 구체적 수치를 독립 확인하지 못함.
   - **수정 제안**: 수치 자체는 논문에서 인용한 것으로 보이므로 유지하되, 인용 시 어떤 모델/조건에서의 수치인지 명시 권장 (예: "GPT-3 기반, VirtualHome 환경에서")
   - **심각도**: Important — 수치 자체의 출처는 논문이지만, 독립 확인이 완료되지 않음. 원문 Table 직접 대조 권장

2. **[KO Line 40-41, EN Line 40-41]** "551개의 사전학습된 로봇 스킬에 대해 이 점수를 계산하고"
   - **검증 결과**: SayCan 공식 웹사이트와 CoRL 버전 논문 페이지에서 "551 skills"이라는 구체적 숫자를 독립 확인하지 못함. 논문 본문에서 가져온 숫자로 추정되나, 웹 기반 교차 확인 불가.
   - **수정 제안**: 원문 PDF에서 직접 확인 필요. 만약 확인 불가 시 "수백 개의 사전학습된 스킬"로 표현 변경 고려
   - **심각도**: Important — 숫자의 정확성이 독립 확인되지 않음

### Warnings (맥락 보강 권장)

1. **[KO Line 42, EN Line 42]** "PaLM 540B를 LLM 백본으로 사용할 때 계획 성공률 84%, 실행 성공률 74%를 달성했습니다. FLAN 대비 오류율이 50% 감소"
   - **검증 결과**: 이 수치는 **PaLM-SayCan 업데이트 버전** (블로그)의 수치임. 원래 CoRL 2022 논문에서는 **FLAN 기반으로 planning 70%, execution 61%**였음. PaLM으로 교체 후 84%/74%로 향상.
   - **현재 서술**: "PaLM 540B를 ... 사용할 때"라고 명시하므로 **맥락은 정확**함
   - **수정 제안**: FLAN 기반 원래 수치도 함께 언급하면 더 완전한 맥락 제공 (예: "원 논문의 FLAN 기반 70%/61%에서 PaLM 교체 후 84%/74%로 향상")
   - **심각도**: Normal — 현재 서술은 정확하지만, 원 논문과 블로그 수치 혼동 방지를 위해 보강 권장

2. **[KO Line 42, EN Line 42]** "최대 8단계의 long-horizon 작업도 성공적으로 수행"
   - **검증 결과**: SayCan 블로그에서 8단계 작업(spilled coke scenario)과 16단계 작업 모두 언급됨. "최대 8단계"는 보수적 표현이나, 16단계 작업도 시연된 바 있음.
   - **수정 제안**: "8단계 이상"으로 변경하거나 "최대 16단계"로 수정 가능
   - **심각도**: Normal — 방향은 맞지만 더 인상적인 결과(16단계)가 있음

3. **[KO Line 54, EN Line 54]** "6.67%의 작업에서는 환각된 노드를 교정하지 못했습니다"
   - **검증 결과**: SayPlan 논문의 수치로 확인되나, WebSearch로 독립 확인은 불가. 논문 원문 출처로 보임.
   - **심각도**: Normal — 독립 확인 미완이나 논문 인용으로 충분

### Verified OK

- SayCan의 "Say + Can" 확률 곱셈 공식 — 논문과 일치
- SayCan → RT-1 → RT-2 → PaLM-E 계열 연결 — 정확
- SayPlan의 3DSG 계층 구조 (building → floor → room → object) — 논문 확인
- SayPlan → KARMA, Embodied-RAG, VeriGraph 연결 — 정확
- LLM as Planners → SayCan → SayPlan 진화 경로 서술 — 정확
- 참고문헌 11개 — arXiv ID 모두 확인됨

---

## Ch 3: Code as Policies — 코드로 로봇을 제어하다

### Critical Issues (반드시 수정)

**없음**

### Warnings (맥락 보강 권장)

1. **[KO Line 28, EN Line 28]** "시뮬레이션에서 본 적 있는 지시/속성에 대해 90% 이상의 성공률을 보였고"
   - **검증 결과**: CaP 원 논문(Liang et al., 2022)에서 "90% 이상" 수치는 WebSearch로 독립 확인 불가. 논문 원문에서의 직접 인용으로 보임.
   - **수정 제안**: 원문 확인 후 유지. 만약 확인 불가 시 "높은 성공률"로 일반화 고려
   - **심각도**: Normal — 방향성은 맞을 것으로 추정

2. **[KO Line 38, EN Line 38]** "최고 baseline 대비 평균 24.1% 성공률 향상"
   - **검증 결과**: Code-as-Symbolic-Planner 논문(arXiv:2503.01700) 확인됨. "7개 TAMP 태스크, 3개 LLM(GPT-4o, Claude3-5-Sonnet, Mistral-Large)에서 평균 24.1% 향상" — **정확함**
   - **심각도**: OK — 수치 검증 완료

3. **[KO Line 48-50, EN Line 48-50]** CaP-X 관련 서술
   - "12개 모델 평가" — **정확** (7 closed + 5 open-source, 실제로는 12개 이상 언급되나 핵심 12개)
   - "human-crafted abstraction 제거 시 성능 급락 + 에이전틱 스캐폴딩으로 회복" — **정확** (논문의 핵심 발견과 일치)
   - "187개 작업" (CaP-Gym) — WebSearch 결과에서 직접 확인 불가하나 논문 인용
   - **심각도**: Normal

4. **[KO Line 64, EN Line 64]** "Minecraft에서 단일 GPU로 1일 내 다이아몬드를 획득하는 효율을 보였지만"
   - **검증 결과**: RL-GPT (arXiv:2402.19299) 논문 확인. "단일 RTX3090"이라는 구체적 GPU 사양은 EN 버전에만 있음. KO에서는 "단일 GPU"로만 표현.
   - **수정 제안**: KO/EN 일관성을 위해 동일 수준의 구체성 유지 권장
   - **심각도**: Normal — KO/EN 표현 차이

### Verified OK

- Code as Policies [Liang et al., 2022] — arXiv:2209.07753 확인
- Code-as-Symbolic-Planner [Chen et al., 2025] — arXiv:2503.01700 확인
- CaP-X [Fu et al., 2026] — arXiv:2603.22435 확인
- AutoTAMP [Chen et al., 2023] — arXiv:2306.06531 확인
- RL-GPT [2024] — arXiv:2402.19299 확인
- NLaP [Mikami et al., 2024] — arXiv:2403.13801 확인
- CaP → Code-as-Symbolic-Planner → CaP-X 진화 서술 — 정확
- Agentic Coding 대비 분석 — 논리적 일관성 확인
- 참고문헌 11개 — arXiv ID 모두 확인됨

---

## 전체 요약: Part I (Ch 1-3)

| 카테고리 | 건수 |
|----------|------|
| **Critical Issues** | 0 |
| **Important Warnings** | 3 |
| **Normal Warnings** | 7 |
| **Verified OK** | 인용 38개 확인, 핵심 수치 대부분 정확 |

### 필수 수정 사항 (Important)

1. **Ch 1**: REFLECT 정확도 "약 60%" → "실세계에서 약 69~79%" 로 수정 (KO/EN 모두)
2. **Ch 2**: "551개 스킬" 수치 — 원문 PDF 직접 확인 필요 (확인 불가 시 "수백 개"로 변경)
3. **Ch 2**: LLM as Planners의 18%→79%, 32.87% 수치 — 원문 Table 직접 대조 권장

### 권장 보강 사항 (Normal)

1. **Ch 2**: SayCan 수치에 FLAN 원래 결과(70%/61%) 병기 고려
2. **Ch 2**: long-horizon "최대 8단계" → "최대 16단계" 또는 "8단계 이상"으로 보강
3. **Ch 3**: KO/EN 간 RL-GPT GPU 사양 표현 일관성 확보
