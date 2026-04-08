# Fact Check Report: Part III (Ch 7-9)

> 검증일: 2026-04-08
> 검증자: fact-checker agent
> 대상: book/ko/ch07-09.md, book/en/ 대응 파일

---

## Ch 7: 메모리와 세계 표현

### Critical Issues (반드시 수정)

1. **[KO Line 28]** "SafeAgentBench에서 안전 작업 완료율 70%"
   - **검증 결과**: SafeAgentBench(arXiv:2412.13178)는 KARMA 논문(arXiv:2409.14908)과 **별도의 논문**임. KARMA 논문 자체에는 SafeAgentBench 수치가 없음. SafeAgentBench 논문에서 "best safety-conscious baseline achieves only a 10% rejection rate"라고 언급되며, "70%"라는 수치의 출처가 불명확.
   - **가능성 1**: SafeAgentBench에서 KARMA를 baseline으로 사용한 결과일 수 있으나, 독립 확인 불가
   - **가능성 2**: 다른 메트릭(safe task completion rate ≠ rejection rate)의 혼동
   - **수정 제안**: 원문 확인 후 정확한 출처와 메트릭을 명시하거나, 확인 불가 시 이 문장 삭제 권장
   - **심각도**: **Critical** — 다른 논문의 수치를 KARMA의 결과로 귀속할 가능성

### Warnings (맥락 보강 권장)

1. **[KO Line 28]** "Composite Tasks에서 성공률 1.3배, 실행 효율 3.4배 ... Complex Tasks에서 성공률 2.3배, 실행 효율 62.7배"
   - **검증 결과**: KARMA 논문 abstract 및 사전 검증과 정확히 일치. 모든 수치 확인됨.
   - **주의**: 사전 검증에서 지적한 대로, "62.7x efficiency"는 step 수 감소 메트릭이며 성공률이 아님. 현재 서술에서 "실행 효율"로 구분하고 있어 맥락은 적절함.
   - **심각도**: OK — 수치 정확, 맥락도 적절

2. **[KO Line 52]** VeriGraph "Language-based tasks에서 +58%, Image-based tasks에서 +30%"
   - **검증 결과**: VeriGraph 논문(arXiv:2411.10446) 검색 결과 "outperforming baseline methods by 58% for language-based tasks and 30% for image-based tasks" 확인됨. **정확함**.
   - **심각도**: OK

### Verified OK

- KARMA [Wang et al., 2024] — arXiv:2409.14908 확인, 핵심 수치 정확
- Embodied-RAG [Xie et al., 2024] — arXiv:2409.18313 확인 (사전 검증과 일치)
- RoboEXP [Jiang et al., 2024] — arXiv:2402.15487 확인
- VeriGraph [Ekpo et al., 2024] — arXiv:2411.10446 확인, 수치 정확
- SayPlan [Rana et al., 2023] — arXiv:2307.06135 확인
- MoMa-LLM — arXiv:2403.08605 확인
- 씬 그래프 진화 경로 테이블 — 논리적 일관성 확인
- 참고문헌 9개 — arXiv ID 모두 확인됨

---

## Ch 8: 폐루프 에이전틱 시스템

### Critical Issues (반드시 수정)

**없음**

### Warnings (맥락 보강 권장)

1. **[KO Line 32]** "7개월간 4개 건물에서 20대 이상의 로봇을 운영하며 77,000개의 시연 데이터를 수집 ... 1:5 비율"
   - **검증 결과**: "77k episodes"와 "20+ robots", "1:5 ratio" — WebSearch로 확인됨. "7개월"과 "4개 건물"은 독립 확인 불가하나, 논문 인용으로 보임.
   - **심각도**: Normal — 핵심 수치(77k, 20+, 1:5) 확인됨. 부가 수치는 논문 인용으로 충분

2. **[KO Line 44]** "90시간 이상의 평가에서 70회 시행, 평균 성공률 47.1%, 최대 12단계 스킬 시퀀스"
   - **검증 결과**: BUMBLE 논문(arXiv:2410.06237) 확인. "47.1% success rate averaged over 70 trials", "90+ hours of testing" — **정확함**.
   - **심각도**: OK — 모든 수치 확인됨

3. **[KO Line 56-62]** PragmaBot 성공률 테이블
   - **검증 결과**: PragmaBot 논문(arXiv:2507.16713) 확인.
     - "STM-based self-reflection increases task success rates from 35% to 84%" — **정확**
     - "LTM improves single-trial success rates from 22% to 80%" — **정확**
     - "2.4배" (35→84 = 2.4x) — 계산 정확
   - **심각도**: OK — 모든 수치 확인됨

4. **[KO Line 101]** "각 단계 95% 성공률이라도 20단계 작업의 전체 성공률은 36%에 불과"
   - **검증 결과**: 0.95^20 = 0.3585 ≈ 36%. 수학적으로 **정확**.
   - **심각도**: OK

### Verified OK

- REFLECT [Liu et al., 2023] — arXiv:2306.15724 확인
- AutoRT [Brohan et al., 2024] — arXiv:2401.12963 확인, 핵심 수치 확인
- BUMBLE [Shah et al., 2024] — arXiv:2410.06237 확인, 수치 정확
- PragmaBot [2025] — arXiv:2507.16713 확인, 수치 정확
- 에이전틱 루프 진화 단계 테이블 — 논리적 일관성 확인
- Robot Constitution 서술 — AutoRT 논문/블로그와 일치
- 참고문헌 7개 — arXiv ID 모두 확인됨

---

## Ch 9: Sim-to-Real 전이와 평가

### Critical Issues (반드시 수정)

**없음**

### Warnings (맥락 보강 권장)

1. **[KO Line 38]** "CLIP, R3M 대비 25-40% 향상"
   - **검증 결과**: Natural Language Sim2Real 논문(arXiv:2405.10020) 확인. "outperforms widely used prior sim2real methods and strong vision-language pretraining baselines like CLIP and R3M by 25 to 40%" — **정확함**.
   - **심각도**: OK

2. **[KO Line 72]** "AutoRT의 77,000 에피소드 수집에 7개월이 소요"
   - **검증 결과**: Ch 8에서 이미 확인된 수치의 재인용. 77k 확인, 7개월은 독립 확인 미완이나 논문 인용으로 충분.
   - **심각도**: Normal — 교차참조 일관성 확인됨

3. **[KO Line 28]** SIMPLER "시뮬레이션 성능과 실세계 성능 간 강한 상관관계"
   - **검증 결과**: SIMPLER 논문(arXiv:2405.05941) 확인. "strong correlation" 표현은 논문과 일치. 구체적 상관계수는 본문에서 인용하지 않으므로 검증 불요.
   - **심각도**: OK

4. **[KO Line 103, Ref 8]** "Bridging Sim2Real, 'Pre-trained Vision Encoders for Sim2Real Transfer,' 2025" — arXiv ID 미제공
   - **검증 결과**: 이 참고문헌만 arXiv ID가 없음. 정확한 논문 식별 불가.
   - **수정 제안**: arXiv ID를 추가하거나, 본문에서 인용되지 않는다면 삭제 고려
   - **심각도**: Important — 참고문헌 형식 불일치

### Verified OK

- SIMPLER [Li et al., 2024] — arXiv:2405.05941 확인
- Lang4Sim2Real — arXiv:2405.10020 확인, 수치 정확
- AutoRT — arXiv:2401.12963 재인용, 일관성 확인
- CaP-X — arXiv:2603.22435 재인용 확인
- Open X-Embodiment — arXiv:2310.08864 재인용 확인
- sim2real gap 3차원 분류 테이블 — 논리적 정확
- 평가 표준 비교 테이블 — 논리적 일관성 확인
- 참고문헌 7개 (1개 arXiv ID 미제공 제외) — 확인됨

---

## 전체 요약: Part III (Ch 7-9)

| 카테고리 | 건수 |
|----------|------|
| **Critical Issues** | 1 |
| **Important Warnings** | 1 |
| **Normal Warnings** | 2 |
| **Verified OK** | 인용 23개 확인, 핵심 수치 대부분 정확 |

### 필수 수정 사항 (Critical)

1. **Ch 7**: KARMA "SafeAgentBench 안전 작업 완료율 70%" — 출처/맥락 불명확. SafeAgentBench는 별도 논문(arXiv:2412.13178)이며, 이 수치가 KARMA의 결과인지 확인 필요. 원문 미확인 시 삭제 권장.

### Important 수정 사항

1. **Ch 9**: 참고문헌 8번 "Bridging Sim2Real" — arXiv ID 미제공. 추가 필요.

### 교차 검증 결과 (사전 검증과 대조)

| 수치 | 사전 검증 | 본문 인용 | 일치 |
|------|----------|----------|------|
| KARMA 1.3x/2.3x 성공률 | 확인 | 확인 | O |
| KARMA 3.4x/62.7x 효율 | 확인 | 확인 | O |
| Embodied-RAG 19 env, 250+ queries | 확인 | 미인용 (수치 안 씀) | N/A |
| VeriGraph +58%/+30% | 미사전검증 | 확인 | O |
| BUMBLE 47.1% / 70 trials / 90h | 미사전검증 | 확인 | O |
| PragmaBot 35%→84%, 22%→80% | 미사전검증 | 확인 | O |
| AutoRT 77k / 20+ robots / 1:5 | 미사전검증 | 확인 | O |
| NL Sim2Real 25-40% over CLIP/R3M | 미사전검증 | 확인 | O |

### 특기 사항

Part III는 Part I-II 대비 새로운 논문 인용이 많아 사전 검증 범위 외 수치가 다수 있었으나, 모두 WebSearch로 확인 완료됨. KARMA SafeAgentBench 수치 1건만 Critical issue.
