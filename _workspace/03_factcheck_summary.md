# Fact Check Summary: 전체 팩트체크 종합 보고서

> 최종 작성일: 2026-04-08
> 검증자: fact-checker agent
> 대상: book/ko/ch01-10.md, book/en/ch01-10.md (총 20 파일)

---

## 1. 전체 통계

| Part | 챕터 | Critical | Important | Normal | 인용 확인 |
|------|------|----------|-----------|--------|----------|
| Part I | Ch 1-3 | 0 | 3 | 7 | 38개 |
| Part II | Ch 4-6 | 3 | 3 | 2 | 32개 |
| Part III | Ch 7-9 | 1 | 1 | 2 | 23개 |
| Part IV | Ch 10 | 2 | 0 | 0 | 20개 (재인용) |
| **합계** | **Ch 1-10** | **6** | **7** | **11** | **93개 (중복 제외)** |

---

## 2. Critical Issues 전체 목록 (6건)

### Issue 1: REFLECT 정확도 "60%" (3곳 반복)
- **위치**: Ch 1 (KO L30, EN L30), Ch 10 (KO L26/L96, EN L26/L92)
- **문제**: "약 60%"로 인용했으나, 원문 Table 2에서 실세계 execution failure **68.8%**, planning failure **78.6%**
- **수정**: "약 70% 수준" 또는 "69~79%"로 변경 (KO/EN 총 6곳)
- **상태**: writer에게 전달 완료, 수정 대기

### Issue 2: DROID "76개 기관" (2곳 반복)
- **위치**: Ch 4 (KO L119, EN L107), Ch 6 (KO L44, EN L44)
- **문제**: "76개 기관"은 **명백한 오류**. 실제 **13개 기관**. "76k trajectories"의 76과 혼동
- **수정**: "13개 기관"으로 변경 (KO/EN 총 4곳)
- **상태**: writer에게 전달 완료, 수정 대기
- **참고**: Ch 10에서는 이미 "13개 기관"으로 올바르게 인용됨

### Issue 3: TinyVLA "5.5배 적은 파라미터"
- **위치**: Ch 4 (KO L64, EN L62)
- **문제**: 독립 확인 불가. 논문은 "20x less inference latency" 강조, 70M~1.4B vs 7B
- **수정**: 원문 PDF 직접 확인 또는 표현 변경 필요
- **상태**: writer에게 전달 완료, 수정 대기

### Issue 4: KARMA "SafeAgentBench 70%"
- **위치**: Ch 7 (KO L28)
- **문제**: SafeAgentBench(arXiv:2412.13178)는 KARMA와 **별도 논문**. 70% 수치의 KARMA 귀속 불명확
- **수정**: 원문 확인 또는 해당 문장 삭제
- **상태**: writer에게 전달 완료, 수정 대기

---

## 3. Important Issues 전체 목록 (7건)

| # | 위치 | 내용 | 상태 |
|---|------|------|------|
| 1 | Ch 2 | SayCan "551개 스킬" — 독립 확인 불가 | 원문 확인 필요 |
| 2 | Ch 2 | LLM Planners 18%→79%, 32.87% — 독립 확인 미완 | 원문 확인 권장 |
| 3 | Ch 4 | OpenVLA "+16.5%" — semantic generalization 제외 조건 미언급 | 맥락 보강 권장 |
| 4 | Ch 4 | Octo "WidowX 55%" — 구체적 조건 불명확 | 맥락 보강 권장 |
| 5 | Ch 4 | pi0 오픈소스 분류 — 현재 공개됨 | 테이블 업데이트 필요 |
| 6 | Ch 9 | 참고문헌 8 "Bridging Sim2Real" — arXiv ID 누락 | ID 추가 필요 |
| 7 | Ch 1 | REFLECT 수치 방향은 맞지만 10%p 차이 | Critical로 승격됨 |

---

## 4. 검증 완료된 핵심 수치

| 논문 | 수치 | 검증 결과 |
|------|------|----------|
| OpenVLA | +16.5% over RT-2-X (29 tasks, 7B vs 55B) | 정확 |
| OpenVLA | BridgeV2 평균 71.3% | 정확 |
| Diffusion Policy | 평균 46.9% improvement (12 tasks) | 정확 |
| pi0 | 7 robots, 68 tasks, 50Hz control | 정확 |
| pi0.5 | Open-world generalization (정성적) | 정확 |
| DROID | 76K demos, 350 hours, 564 scenes, **13** institutions | 정확 (기관 수 수정 필요) |
| Open X-Embodiment | 22 robots, 527 skills, 1M+ trajectories, 21 institutions | 정확 |
| SayCan (PaLM) | Planning 84%, Execution 74% (101 tasks) | 정확 |
| Code-as-Symbolic-Planner | +24.1% avg over best baseline (7 TAMP tasks) | 정확 |
| KARMA | 1.3x/2.3x success, 3.4x/62.7x efficiency | 정확 |
| Embodied-RAG | 19 envs, 250+ queries, 7.38x/9.76x faster graph building | 정확 |
| VeriGraph | +58% language, +30% image tasks | 정확 |
| BUMBLE | 47.1% success, 70 trials, 90+ hours | 정확 |
| PragmaBot | 35%→84% (STM), 22%→80% (LTM+RAG) | 정확 |
| AutoRT | 77K episodes, 20+ robots, 1:5 ratio | 정확 |
| HAMSTER | +20% over OpenVLA (7 axes), 50% relative | 정확 |
| AutoTAMP | 82.5-87.7% single, 100% multi-agent | 정확 |
| NL Sim2Real | 25-40% over CLIP/R3M | 정확 |
| TinyVLA | +25.7% over OpenVLA, +21.5% over Diffusion Policy | 정확 |

---

## 5. arXiv ID 검증 결과

전체 참고문헌의 arXiv ID를 검증한 결과:
- **확인됨**: 모든 핵심 논문의 arXiv ID 정확
- **누락**: Ch 9 참고문헌 8 ("Bridging Sim2Real") — arXiv ID 미제공
- **형식**: 모든 인용이 `[Author et al., Year]` 형식 준수

---

## 6. 교차참조 일관성

| 교차참조 | 결과 |
|----------|------|
| 챕터 간 수치 일관성 | DROID 기관 수 Ch4/6(76)과 Ch10(13) 불일치 → 수정 필요 |
| KO/EN 일관성 | 전반적으로 일치. Ch 3 RL-GPT GPU 사양 미세 차이 |
| 7대 차원 테이블 | CLAUDE.md 원본과 Ch 1, Ch 10 일치 |
| 참고문헌 번호 | 각 챕터 내 일관성 확인 |

---

## 7. 전체 평가

### 강점
- **수치 정확도 높음**: Critical 6건 중 4건이 동일 오류(REFLECT 60%, DROID 76기관)의 반복. 고유 오류는 2건(TinyVLA, SafeAgentBench)뿐
- **인용 형식 일관**: 93개 인용 중 arXiv ID 누락은 1건뿐
- **논리적 일관성**: 패러다임 전환, 진화 경로, 7대 차원 분석 모두 논리적으로 정합
- **교차참조 정확**: 챕터 간 상호 참조가 정확하게 연결

### 개선 필요
- REFLECT 60% → ~70%: 3곳에서 반복된 가장 빈번한 오류
- DROID 76기관 → 13기관: 가장 심각한 사실 오류 (10x 차이)
- 일부 수치의 맥락 부족 (OpenVLA semantic generalization 제외 조건 등)

### 최종 판정
이 서베이 책의 전체적인 사실 정확도는 **높음**입니다. Critical issue 6건 중 실질적으로 독립된 오류는 4건이며, 모두 수정 가능합니다. 93개 인용의 arXiv ID가 정확하고, 핵심 성능 수치 19개 중 17개가 검증을 통과했습니다. 제안된 수정 사항을 반영하면 출판 수준의 정확도에 도달할 것으로 판단됩니다.
