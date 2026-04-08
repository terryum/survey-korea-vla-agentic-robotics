# Fact Check Report: Part II (Ch 4-6)

> 검증일: 2026-04-08
> 검증자: fact-checker agent
> 대상: book/ko/ch04-06.md, book/en/ch04-06.md

---

## Ch 4: Vision-Language-Action 모델의 부상

### Critical Issues (반드시 수정)

1. **[KO Line 119, EN Line 107]** "DROID [Khazatsky et al., 2024]가 **76개 기관**, 564개 장면에서 76,000 궤적을 수집한 것"
   - **검증 결과**: DROID 공식 웹사이트와 논문에서 확인한 바, DROID는 **13개 기관(institutions)**, 50명 data collectors, 564 scenes에서 수집됨. "76개 기관"은 **명백한 오류** — "76k trajectories"의 "76"과 혼동된 것으로 보임.
   - **수정 제안 (KO)**: "13개 기관, 564개 장면에서 76,000 궤적을 수집"
   - **수정 제안 (EN)**: "76,000 trajectories from 13 institutions across 564 scenes"
   - **심각도**: **Critical** — 핵심 데이터셋 규모의 사실 오류

2. **[KO Line 64, EN Line 62]** "TinyVLA ... OpenVLA 대비 +25.7% 성공률, **5.5배** 적은 파라미터를 달성"
   - **검증 결과**: TinyVLA 논문(arXiv:2409.12514)에서 +25.7% 성공률은 확인됨 (94.0% vs OpenVLA). 그러나 "5.5배 적은 파라미터"는 논문 검색에서 독립 확인 불가. 논문은 "20x less inference latency"를 강조하며, 파라미터 범위는 70M~1.4B vs OpenVLA 7B로 5~100x 차이. "5.5x"라는 구체적 배수의 출처 불명.
   - **수정 제안**: 원문 PDF에서 "5.5x" 직접 확인 필요. 만약 확인 불가 시 "수 배 적은 파라미터"로 변경하거나, 논문에서 강조하는 "20배 빠른 추론"으로 대체
   - **심각도**: **Critical** — 구체적 수치의 출처 미확인

### Warnings (맥락 보강 권장)

1. **[KO Line 54, EN Line 54]** "파인튜닝 후 WidowX에서 55% 성공률을 달성"
   - **검증 결과**: Octo 논문에서 WidowX 55% 성공률의 정확한 조건을 독립 확인하지 못함. 논문은 fine-tuning 후 "25% higher success rate on average with goal image conditioning" 및 "52% outperforms next best baseline"을 언급하지만, "55%"라는 절대 수치는 특정 태스크/조건에서의 결과로 보임.
   - **수정 제안**: 어떤 태스크에서의 55%인지 맥락 추가 권장
   - **심각도**: Important — 수치의 맥락이 불명확

2. **[KO Line 58, EN Line 58]** "RT-2-X(55B) 대비 +16.5% 성공률을 달성하면서 파라미터는 1/8"
   - **검증 결과**: OpenVLA 논문 확인됨. +16.5% absolute는 정확, 7B vs 55B = 약 1/8은 근사적으로 정확 (정확히는 7/55 ≈ 1/7.86). 단, "+16.5%"는 29개 tasks 평균이며 semantic generalization 제외 조건 존재.
   - **현재 서술**: "semantic generalization 제외" 미언급
   - **수정 제안**: "대부분의 평가 카테고리에서" 또는 "semantic generalization을 제외한" 조건 부기 고려
   - **심각도**: Important — 방향은 맞지만 조건 누락

3. **[KO Line 64, EN Line 62]** "MetaWorld 50개 작업에서 Diffusion Policy 대비 +21.5%"
   - **검증 결과**: TinyVLA 논문에서 확인됨. 방향과 수치 모두 정확.
   - **심각도**: OK

4. **[KO Line 72]** "최대 50Hz 실시간 제어를 달성"
   - **검증 결과**: pi0 논문 및 Hugging Face 블로그에서 "50Hz" 제어 주파수 확인됨. 정확.
   - **심각도**: OK

5. **[KO Line 50, EN Line 50]** "21개 기관, 150명 이상의 연구자가 참여하여 22개 로봇 실체, 527개 스킬, 100만 이상의 궤적"
   - **검증 결과**: Open X-Embodiment 논문(arXiv:2310.08864) 및 사전 검증과 일치. 수치 정확.
   - **심각도**: OK

6. **[KO Line 105, EN Line 101]** 5대 설계축 테이블에서 "pi0"이 Closed로 분류
   - **검증 결과**: pi0의 코드와 모델은 초기에 비공개였으나, 이후 HuggingFace를 통해 공개됨. 현재(2026년 4월) 기준 오픈소스임.
   - **수정 제안**: pi0을 "비공개 → 공개"로 업데이트하거나, "초기 비공개, 이후 공개"로 주석 추가
   - **심각도**: Important — 시점에 따라 달라지는 정보

### KO/EN 일관성

- KO와 EN 내용이 전반적으로 일치
- GR00T N1 관련 서술 정확 (arXiv:2503.14734, Dual-System, 오픈소스 확인)
- 참고문헌 14개 — arXiv ID 모두 확인됨

---

## Ch 5: 계층적 계획 — 고수준에서 저수준으로

### Critical Issues (반드시 수정)

**없음**

### Warnings (맥락 보강 권장)

1. **[KO Line 28, EN Line 28]** "GPT-4 + AutoTAMP은 단일 에이전트에서 82.5~87.7%, 다중 에이전트(전체 AutoTAMP)에서 100% 성공률"
   - **검증 결과**: AutoTAMP 논문(arXiv:2306.06531) Tables 1-2에서 확인됨. 단일 에이전트 82.5%, 82%, 87.7% (STL/Syntactic/Semantic 각각), 다중 에이전트에서 100%, 79%, 100%. 서술은 최선+최악의 범위를 보여줌.
   - **주의**: "다중 에이전트에서 100%"는 전체 AutoTAMP(STL+Syntactic+Semantic) 조건에서만이며, 일부 조건에서는 79%. 현재 서술 "(전체 AutoTAMP)에서 100%"는 맥락이 맞음.
   - **심각도**: OK — 검증 완료

2. **[KO Line 54, EN Line 52]** "OpenVLA 대비 평균 +20% 성공률(7개 일반화 축), 50% 상대적 향상"
   - **검증 결과**: HAMSTER 논문(arXiv:2502.05485) 확인. "average of 20% improvement ... seven different axes of generalization over OpenVLA, representing a 50% relative gain" — **정확함**.
   - **심각도**: OK — 검증 완료

3. **[KO Line 36-38, EN Line 36-38]** RT-H의 language motion 서술
   - **검증 결과**: RT-H (arXiv:2403.01823) 존재 확인됨. 구체적 수치 인용 없이 개념 서술만 있어 별도 수치 검증 불요.
   - **심각도**: OK

### Verified OK

- AutoTAMP [Chen et al., 2023] — arXiv:2306.06531 확인
- RT-H [Belkhale et al., 2024] — arXiv:2403.01823 확인
- Hi Robot [Shi et al., 2025] — arXiv:2502.19417 확인
- HAMSTER [Li et al., 2025] — arXiv:2502.05485 확인
- 네 가지 계층적 분리 비교 테이블 — 논리적으로 정확
- Agentic Coding 대비 분석 — 일관성 확인
- 참고문헌 8개 — arXiv ID 모두 확인됨

---

## Ch 6: 저수준 제어 — Diffusion Policy와 3D 표현

### Critical Issues (반드시 수정)

1. **[KO Line 44, EN Line 44]** "**76개 기관**, 564개 장면에서 76,000개 궤적을 수집한 역사상 가장 큰 규모"
   - **검증 결과**: Ch 4와 동일한 오류. DROID는 **13개 기관**, 50 data collectors. "76개 기관"은 **명백한 오류**.
   - **수정 제안**: "13개 기관, 564개 장면에서 76,000개 궤적"
   - **심각도**: **Critical** — Ch 4와 동일한 반복 오류

### Warnings (맥락 보강 권장)

1. **[KO Line 32, EN Line 32]** "12개 작업에서 기존 SOTA 대비 평균 46.9% 향상"
   - **검증 결과**: Diffusion Policy 논문 및 사전 검증과 일치. "12 tasks across 4 benchmarks" + "average improvement of 46.9%" — **정확함**.
   - **주의**: "46.9% improvement"가 absolute pp인지 relative인지는 사전 검증에서 지적한 대로 논문 원문 확인 필요하나, 논문 표현 자체가 "average improvement of 46.9%"이므로 인용은 정확.
   - **심각도**: OK — 사전 검증 주의사항 유지

2. **[KO Line 44, EN Line 44]** DROID "84 tasks" vs 웹사이트 "86 tasks"
   - **검증 결과**: arXiv abstract에서 "84 tasks", 웹사이트에서 "86 tasks" — 미세한 차이 존재. 논문 버전에 따라 다를 수 있음.
   - **수정 제안**: 현재 KO/EN 모두 구체적 task 수를 명시하지 않으므로 문제 없음
   - **심각도**: Normal — 참고용

### Verified OK

- Diffusion Policy [Chi et al., 2023] — arXiv:2303.04137 확인, 수치 정확
- 3D Diffuser Actor [Ke et al., 2024] — arXiv:2402.10885 확인
- DROID [Khazatsky et al., 2024] — arXiv:2403.12945 확인 (기관 수 제외)
- 저수준 설계 축 비교 테이블 — 논리적 정확
- Agentic Coding 대비 분석 (결정론 vs 확률, 이산 vs 연속, 접촉 역학) — 논리 일관성 확인
- 참고문헌 10개 — arXiv ID 모두 확인됨

---

## 전체 요약: Part II (Ch 4-6)

| 카테고리 | 건수 |
|----------|------|
| **Critical Issues** | 3 |
| **Important Warnings** | 3 |
| **Normal Warnings** | 2 |
| **Verified OK** | 인용 32개 확인, 핵심 VLA 수치 대부분 정확 |

### 필수 수정 사항 (Critical)

1. **Ch 4 + Ch 6**: DROID "76개 기관" → **"13개 기관"** 으로 수정 (KO/EN 모두, 2곳)
2. **Ch 4**: TinyVLA "5.5배 적은 파라미터" — 원문 확인 불가. 정확한 수치로 교체 필요

### Important 수정 사항

1. **Ch 4**: OpenVLA "+16.5%" — semantic generalization 제외 조건 미언급
2. **Ch 4**: Octo "WidowX 55%" — 맥락(어떤 태스크/조건) 불명확
3. **Ch 4**: pi0 오픈소스 분류 — 5대 설계축 테이블에서 "비공개"로 되어 있으나 현재 공개됨

### 교차 검증 결과 (사전 검증과 대조)

| 수치 | 사전 검증 | 본문 인용 | 일치 |
|------|----------|----------|------|
| OpenVLA +16.5% over RT-2-X | 확인 | 확인 | O |
| OpenVLA 7B, 970K demos | 확인 | 확인 | O |
| Diffusion Policy 46.9% avg improvement | 확인 | 확인 | O |
| DROID 76K demos, 564 scenes | 확인 | 확인 (기관 수 오류) | X (기관 수) |
| pi0: 7 robots, 68 tasks, 50Hz | 확인 | 확인 | O |
| Open X-Embodiment: 22 robots, 527 skills, 1M+ trajectories | 확인 | 확인 | O |
