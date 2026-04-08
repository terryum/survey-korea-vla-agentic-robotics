# Fact Check Report: Part IV (Ch 10)

> 검증일: 2026-04-08
> 검증자: fact-checker agent
> 대상: book/ko/ch10.md, book/en/ch10.md

---

## Ch 10: Agentic Coding vs Agentic Robotics — 간극과 미래

### Critical Issues (반드시 수정)

1. **[KO Line 26, EN Line 26]** "REFLECT ... 인간 판단 대비 약 60% 수준"
   - **검증 결과**: Part I 팩트체크에서 이미 지적된 동일 오류. REFLECT 원문 Table 2: 실세계 execution failure **68.8%**, planning failure **78.6%**. "약 60%"는 부정확.
   - **수정 제안**: "약 70% 수준" 또는 "69~79%"
   - **심각도**: **Critical** — Part I에서 지적한 오류가 Ch 10에서 반복됨

2. **[KO Line 96, EN Line 92]** 이식 테이블 "~60% 정확도"
   - **검증 결과**: 위와 동일 오류. 테이블 내 "초기 (~60% 정확도)" 표현도 수정 필요.
   - **수정 제안**: "초기 (~70% 정확도)"
   - **심각도**: **Critical** — 같은 오류의 3번째 발생 (Ch 1, Ch 10 본문, Ch 10 테이블)

### Warnings (맥락 보강 권장)

**없음** — 다른 모든 교차 인용 수치가 정확함.

### 교차 인용 검증 (이전 챕터 수치와 대조)

| 인용 수치 | Ch 10 인용 | 원 챕터 검증 결과 | 일치 |
|----------|-----------|-----------------|------|
| PragmaBot 84% | KO L18, EN L18 | Ch 8: 확인됨 | O |
| BUMBLE 47.1% | KO L18, EN L18 | Ch 8: 확인됨 | O |
| REFLECT ~60% | KO L26, EN L26 | Ch 1: **68.8~78.6%** | **X** |
| DROID 13기관, 564장면 | KO L34, EN L34 | Ch 4: **13이 맞음** (76 오류 수정됨) | O |
| KARMA 62.7x 효율 | KO L50, EN L48 | Ch 7: 확인됨 | O |
| 0.95^20 = 36% | KO L125, EN L114 | Ch 8: 수학적 확인 | O |
| REFLECT ~60% (테이블) | KO L96, EN L92 | Ch 1: **68.8~78.6%** | **X** |

### Verified OK

- 7대 차원 분류 (해소불가/구조적/실용적) — 논리적 일관성 확인
- 세 등급 분류 — CLAUDE.md 원본 테이블과 일치
- 8대 미해결 문제 분류 — 이전 챕터와 정합성 확인
- 5번째 패러다임 전환 (Embodied World Models) — 서술적 전망이므로 팩트체크 대상 아님
- 참고문헌 20개 — arXiv ID 모두 이전 챕터에서 검증 완료
- KO/EN 내용 일관성 — 확인됨

---

## 요약: Part IV (Ch 10)

| 카테고리 | 건수 |
|----------|------|
| **Critical Issues** | 2 (동일 오류의 반복) |
| **Important Warnings** | 0 |
| **Normal Warnings** | 0 |
| **Verified OK** | 교차 인용 7건 중 5건 정확, 참고문헌 20개 확인 |

### 필수 수정

REFLECT "60%" → "~70%" 수정 (KO/EN 각 2곳, 총 4곳):
1. KO Line 26 본문
2. KO Line 96 테이블
3. EN Line 26 본문
4. EN Line 92 테이블

이 오류는 Ch 1에서 최초 발생하여 Ch 10에서 2회 반복된 것임. Ch 1 수정 시 Ch 10도 함께 수정 필요.
