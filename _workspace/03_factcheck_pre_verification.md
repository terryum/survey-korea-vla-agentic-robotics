# Fact Check Pre-Verification: 핵심 수치 사전 검증

> 생성일: 2026-04-08
> 검증자: fact-checker agent
> 목적: writer 집필 전 핵심 논문의 주요 수치를 WebSearch로 사전 확인

---

## 1. pi0 / pi0.5 성능 수치

### pi0 (arXiv:2410.24164, Physical Intelligence, 2024)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 학습 데이터 | 7개 로봇 플랫폼, 68개 고유 태스크 | pi0 논문 + PI 블로그 |
| 아키텍처 | PaLM-E 기반 VLM + flow matching (diffusion variant) | 논문 Section 3 |
| Pre-training 평가 (Figure 7) | Shirt folding ~95-100%, Bussing easy ~90-95%, Bussing hard ~70-75%, Grocery bagging ~85-90%, Toast ~80-85% | 논문 Figure 7 (근사치, 그래프 기반) |
| Fine-tuning 향상 | Pre-trained 모델이 non-pre-trained 대비 최대 2x 성능 | 논문 본문 |
| 외부 평가 (UPenn) | zero-shot 평균 task progress 약 42.3% | Penn PAL Lab 독립 평가 |
| 시연 태스크 | 빨래 접기, 테이블 정리, 박스 조립 | 논문 + 블로그 |

**주의사항**:
- pi0 논문의 수치는 대부분 Figure(그래프)에서 읽는 근사치임. 정확한 숫자 테이블이 아님
- "95% success rate" 같은 단일 수치 인용 시, 어떤 태스크인지 반드시 명시 필요
- UPenn 독립 평가(42.3%)와 PI 자체 평가 수치는 크게 다름 — 맥락 구분 필수

### pi0.5 (arXiv:2504.16054, Physical Intelligence, 2025)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 핵심 기여 | co-training framework (heterogeneous semantic supervision) | 논문 abstract |
| 일반화 | 새로운 집에서 end-to-end 주방/침실 청소 최초 시연 | 논문 Section 5 |
| 정량적 수치 | **논문에서 구체적 성공률 테이블 미공개** — 주로 정성적 시연 | 확인됨 |

**주의사항**:
- pi0.5의 핵심 기여는 co-training framework이지 특정 수치가 아님
- "최초(first time)" 주장은 end-to-end learning 기반 long-horizon dexterous manipulation에 한정

---

## 2. OpenVLA vs RT-2 비교 수치

### OpenVLA (arXiv:2406.09246, Stanford 등, 2024)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 모델 크기 | 7B 파라미터 | 논문 abstract |
| 학습 데이터 | 970k real-world robot demonstrations (Open X-Embodiment) | 논문 Section 3 |
| vs RT-2-X (55B) | **+16.5% absolute** task success rate, 7x fewer parameters | 논문 abstract |
| vs Diffusion Policy | **+20.4%** (from-scratch imitation learning 대비) | 논문 Table 비교 |
| 평가 규모 | 29 tasks, multiple robot embodiments | 논문 Section 4 |
| BridgeData V2 평균 | **71.3%** success rate | 논문 Table |
| Fine-tuning (Franka) | Full FT 69.7%, LoRA r=32 68.2%, LoRA r=64 68.2% | 논문 Table 1 |
| 양자화 | bfloat16: 71.3%, int4: 71.9%, int8: 58.1% | 논문 Table 2 |

**주의사항**:
- "16.5% 향상"은 **absolute percentage point** (not relative %)
- RT-2-X 추정 평균: ~54.8% (71.3 - 16.5)
- "모든 카테고리에서 RT-2-X 능가" 단, **semantic generalization 제외**
- 신뢰도 한계: "typically achieving less than 90% success rate"

### RT-2 / RT-2-X (arXiv:2307.15818 / 2310.08864, Google DeepMind, 2023)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| RT-2 모델 크기 | PaLI-X 55B 또는 PaLM-E 12B 기반 | 논문 |
| RT-2 평가 규모 | 6,000회 시행 (trials) | researcher 워크스페이스 |
| RT-2-X | 55B, cross-embodiment | Open X-Embodiment 논문 |
| Open X-Embodiment 데이터 | 22개 로봇, 527개 스킬, 100만+ 궤적, 21개 기관 | 논문 abstract |

---

## 3. SayCan 성능 수치

### SayCan (arXiv:2204.01691, Google, 2022)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| PaLM-SayCan planning success | **84%** | 블로그 + 논문 |
| PaLM-SayCan execution success | **74%** | 블로그 + 논문 |
| FLAN-SayCan planning success | **70%** | 논문 (CoRL 버전) |
| FLAN-SayCan execution success | **61%** | 논문 (CoRL 버전) |
| 평가 규모 | **101 tasks**, 2개 환경 (사무실 주방 + 모의 주방) | 논문 Section 5 |
| 오류 감소 | PaLM이 FLAN 대비 오류 **50% 감소** | 블로그 |
| Affordance grounding 효과 | 비그라운딩 대비 **~15% 향상** | 블로그 |
| 다국어 성능 | 영→중/불/스페인어 전환 시 planning success rate 거의 변화 없음 | 블로그 |
| Long-horizon | 최대 16 step 태스크 성공 시연 | 블로그 |

**주의사항**:
- 84%/74% 수치는 **PaLM-SayCan** (업데이트 버전). 원래 CoRL 논문 수치는 70%/61% (FLAN 기반)
- "planning success"와 "execution success"는 다른 메트릭 — planning은 올바른 스킬 시퀀스 선택, execution은 실제 물리적 수행 포함
- 버전 혼동 주의: 블로그(PaLM)와 원 논문(FLAN) 수치 구분 필수

---

## 4. DROID 데이터셋 규모

### DROID (arXiv:2403.12945, 2024)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 시연 수 | **76,000 demonstration trajectories** | 논문 abstract |
| 시간 | **350 hours** of interaction data | 논문 abstract |
| 환경 수 | **564 scenes**, 52 buildings | 논문 Section 3 |
| 태스크 수 | **84 tasks** | 논문 |
| 수집자 | **50 data collectors**, 13 institutions | 논문 |
| 로봇 수 | **18 robots** | 논문 |
| 수집 기간 | **12 months** | 논문 |
| 지역 | North America, Asia, Europe | 논문 |
| 카메라 | 3 camera views + depth + calibration + language annotations | 논문 |
| 기존 대비 | 기존 최대 데이터셋 대비 **10x 이상** scenes | 논문 abstract |

**주의사항**:
- "76k demonstrations"와 "350 hours"를 함께 인용해야 규모 파악 가능
- "564 scenes"와 "52 buildings"을 구분 — scene ≠ building
- "in-the-wild" 강조 시 52 buildings 수치가 핵심 근거

---

## 5. Diffusion Policy baseline 대비 향상률

### Diffusion Policy (arXiv:2303.04137, Chi et al., 2023)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 평균 향상률 | **46.9%** average success-rate improvement | 논문 abstract |
| 평가 규모 | **12 tasks**, 4 robot manipulation benchmarks | 논문 Section 4 |
| 벤치마크 | Robomimic (Lift, Can, Square, Tool Hang, Transport), Push-T, Block Pushing, Franka Kitchen | 논문 |
| 비교 baselines | LSTM-GMM, IBC, BET | 논문 |
| 발표 | RSS 2023, IJRR 2024 (journal version) | 확인됨 |

**주의사항**:
- **"46.9% improvement"는 absolute success rate improvement (percentage points)인지 relative improvement인지 논문 원문 확인 필요** — "average improvement of 46.9%" 표현은 모호할 수 있음
- 12개 태스크의 **평균**이므로 개별 태스크별 편차 클 수 있음
- 실제 로봇 실험도 있으나 상세 수치는 시뮬레이션 중심

---

## 6. CaP-X 핵심 실험 결과

### CaP-X (arXiv:2603.22435, Microsoft Research 등, 2026)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 평가 모델 수 | **12 models** (7 closed + 5 open-source) | 논문 Table |
| CaP-Agent0 vs 인간 | 7개 core task 중 **4개에서** 인간 수준 이상 달성 (low-level primitives) | 논문 Section 5 |
| BEHAVIOR 결과 | Pick up Radio: CaP-Agent0 56% vs Human 36% (task success) | 논문 Table 3 |
| | Pick up Soda Can: CaP-Agent0 72% vs Human 72% (task success) | 논문 Table 3 |
| CaP-RL Sim (100 trials) | Cube Lift 80%, Cube Stack 44%, Spill Wipe 93% | 논문 Table 4 |
| CaP-RL Real (25 trials) | Cube Lift 84%, Cube Stack 76% | 논문 Table 4 |
| Human baseline (sim) | Cube Lift 93%, Cube Stack 73%, Spill Wipe 100% | 논문 Table 4 |
| Base model (sim) | Cube Lift 25%, Cube Stack 4%, Spill Wipe 30% | 논문 Table 4 |
| 핵심 발견 | abstractions 제거 시 성능 하락; Visual Differencing (M3)이 naive image (M2) 능가 | 논문 Section 5 |

**주의사항**:
- BEHAVIOR 결과에서 CaP-Agent0가 **navigation**에서는 인간과 비슷하지만 **task success**에서 일부 능가 — 맥락 구분 필요
- "M2 (naive image interleaving)이 성능 저하 유발" — 직관적 기대와 반대되는 결과이므로 정확한 인용 중요
- CaP-RL real world는 25 trials로 통계적 유의성 한계 있음

---

## 7. KARMA / Embodied-RAG 성능 수치

### KARMA (arXiv:2409.14908, 2024)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| Composite Tasks 성공률 향상 | **1.3x** (기존 memory-augmented agent 대비) | 논문 abstract |
| Complex Tasks 성공률 향상 | **2.3x** | 논문 abstract |
| Composite Tasks 효율성 향상 | **3.4x** | 논문 abstract |
| Complex Tasks 효율성 향상 | **62.7x** | 논문 abstract |
| 평가 환경 | AI2-THOR simulator | 논문 |
| 메모리 구조 | Long-term (3D scene graph) + Short-term (object position/state) | 논문 Section 3 |

**주의사항**:
- "1.3x" = 30% 향상, "2.3x" = 130% 향상 — 배수와 퍼센트 혼동 주의
- "62.7x efficiency" 수치는 매우 극단적 — 효율성(step 수 감소) 메트릭이며 성공률과 다름
- "state-of-the-art embodied agents enhanced with memory" 대비 — 어떤 baseline인지 명시 필요
- AI2-THOR 시뮬레이터 결과이며 실제 로봇 결과와 구분

### Embodied-RAG (arXiv:2409.18313, 2024)

| 항목 | 검증된 수치 | 출처 |
|------|-----------|------|
| 평가 환경 | **19 environments** (14 simulated + 5 real) | 논문 Section 4 |
| 쿼리 수 | **250+** explanation & navigation queries | 논문 |
| Explicit query P(Q\|A) | Embodied-RAG **0.55** vs Naive-RAG 0.08, GraphRAG 0.06, LightRAG 0.08 | 논문 Table II |
| Implicit query P(Q\|A) | Embodied-RAG **0.62** vs Naive-RAG 0.10, GraphRAG 0.12, LightRAG 0.13 | 논문 Table II |
| Global semantic sim | Embodied-RAG **0.67** vs GraphRAG 0.68, LightRAG 0.65, Naive-RAG 0.31 | 논문 Table II |
| 그래프 구축 속도 | GraphRAG 대비 **7.38x**, LightRAG 대비 **9.76x** 빠름 | 논문 Section 5 |
| 구축 시간 | 3,353 nodes에 약 4분 35초 | 논문 |
| 대규모 그래프 | 3,525 nodes (1km 반경 street-view) | 논문 |

**주의사항**:
- P(Q|A) 메트릭은 "질문이 답변으로부터 재생성될 확률" — 일반적인 accuracy/success rate가 아님
- Global query에서는 **GraphRAG(0.68)이 Embodied-RAG(0.67)보다 미세하게 높음** — "모든 면에서 우수" 인용 시 주의
- "7.38x faster"는 **구축 속도**이지 추론 속도가 아님

---

## 요약: 인용 시 특별 주의 사항

1. **pi0**: 그래프 기반 근사치 다수 — 정확한 수치 인용 시 "approximately" 표현 권장
2. **OpenVLA vs RT-2-X**: "+16.5%"는 absolute pp, semantic generalization 제외 조건 명시
3. **SayCan**: PaLM 버전(84%/74%)과 FLAN 버전(70%/61%) 구분 필수
4. **DROID**: 76k demos, 350 hours, 564 scenes — 세 수치 세트로 규모 표현
5. **Diffusion Policy**: "46.9% improvement"의 계산 방식(absolute vs relative) 확인 필요
6. **CaP-X**: real world 실험은 25 trials — 통계적 한계 존재
7. **KARMA**: 배수(x) 표현과 퍼센트(%) 표현 혼동 주의; 62.7x는 효율성 메트릭
8. **Embodied-RAG**: Global query에서 GraphRAG가 미세 우위 — 전면 우위 인용 금지
