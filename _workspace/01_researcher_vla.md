# VLA Foundation Models — 심층 서베이

> 카테고리 핵심 질문: **VLM을 어떻게 로봇 action으로 직접 연결하는가?**

이 카테고리는 Vision-Language Model(VLM)을 로봇 행동(action)에 직접 연결하는 "end-to-end" 패러다임을 다룬다. LLM Planner가 "계획을 세우는" 수준에 머물렀다면, VLA는 "직접 행동한다". 2023년 PaLM-E/RT-2에서 시작하여 2025-2026년 pi0.5/GR00T N1까지 급속히 발전한 이 분야의 가장 활발한 연구 흐름이다.

---

## 1. 핵심 논문 분석

### 1.1 PaLM-E: An Embodied Multimodal Language Model (2023)

- **arXiv**: https://arxiv.org/abs/2303.03378
- **저자**: Danny Driess, Fei Xia et al. (Google, TU Berlin)
- **학회**: ICML 2023

#### 핵심 Contribution
언어 모델에 이미지, 로봇 상태, 텍스트를 **멀티모달 토큰**으로 함께 입력하여 embodied reasoning을 수행하는 최초의 대규모 모델. VLA 이전의 "embodied multimodal LM" 패러다임의 상징.

#### 방법론
- PaLM (540B) 기반, 시각/상태/텍스트 입력을 공유 임베딩 공간에 통합
- End-to-end 학습: 로봇 조작 계획, VQA, captioning을 단일 모델로
- 다양한 센서 모달리티 (RGB, 3D 포인트, 로봇 상태) 지원

#### 주요 결과
| 모델 | 크기 | 특징 |
|------|-----|------|
| PaLM-E-12B | 12B | 로봇 태스크 기준점 |
| PaLM-E-562B | **562B** | OK-VQA SOTA + 로봇 조작 + 언어 일반화 |

- **Positive Transfer**: 다양한 도메인(인터넷 이미지, 로봇 데이터) 공동 학습이 각 도메인 성능 향상
- 스케일이 커질수록 언어 능력 유지 + embodied 능력 향상

#### 한계점
- 562B 파라미터 → 실시간 로봇 제어에 비현실적 크기
- 행동을 직접 출력하지 않고 텍스트 형식의 계획 생성
- 단일 모델이지만 실제 로봇에서의 end-to-end 배포는 제한적

#### Agentic Coding 대비
PaLM-E는 "하나의 거대 모델이 모든 것을 안다"는 접근이다. Agentic Coding에서도 하나의 LLM이 코드, 문서, 디버깅을 모두 처리하지만, 실행은 외부 도구에 위임한다. PaLM-E의 한계(크기, 속도)는 후속 연구에서 전문화/경량화로 해결된다.

---

### 1.2 RT-2: Vision-Language-Action Models (2023)

- **arXiv**: https://arxiv.org/abs/2307.15818
- **저자**: Anthony Brohan, Noah Brown et al. (Google DeepMind)
- **학회**: CoRL 2023

#### 핵심 Contribution
VLM의 **웹 지식을 로봇 행동으로 직접 전이**하는 VLA 패러다임의 상징적 논문. 행동(action)을 텍스트 토큰으로 표현하여 VLM의 출력 형식에 통합.

#### 방법론
- VLM (PaLI-X 55B 또는 PaLM-E 12B)을 로봇 궤적 데이터와 인터넷 VL 데이터로 **공동 파인튜닝**
- **Action Tokenization**: 로봇 행동을 텍스트 토큰으로 인코딩 (예: "1 128 91 241 5 101 127")
- 자연어 응답과 로봇 행동을 동일한 토큰 공간에서 학습

#### 주요 결과 (6,000회 평가 시행)
- **Novel Object Generalization**: 학습 데이터에 없는 물체에 대한 유의미한 일반화
- **Emergent Semantic Reasoning**: "즉흥 망치로 쓸 수 있는 물체를 집어" → 돌을 선택
- **Chain-of-Thought 통합**: 다단계 의미 추론 가능 ("피곤한 사람에게 적합한 음료 선택")
- 학습 데이터에 없는 명령도 해석 가능 (특정 숫자/아이콘 위에 물체 놓기)

#### 한계점
- **55B 모델 크기**: 실시간 제어에 지연 발생
- **Action Tokenization의 한계**: 단순 이산화(binning)로는 고주파/정밀 조작에 부적합 (→ FAST가 해결)
- **데이터 다양성 제한**: Google 로봇 데이터셋에 한정

#### 영향
- **"VLA" 용어의 사실상 확립**
- OpenVLA, pi0, GR00T N1 등 모든 후속 VLA의 직접적 전신
- "웹 지식 → 로봇 행동" 전이가 가능하다는 근본적 증거

#### Agentic Coding 대비
RT-2가 웹 지식을 로봇 행동으로 전이하는 것은, LLM이 코드 학습 데이터의 지식을 새로운 프로그래밍 문제 해결에 전이하는 것과 유사하다. 핵심 차이: 코드는 자연어와 같은 토큰 공간에 자연스럽게 있지만, 로봇 행동은 인위적인 토큰화(action tokenization)가 필요하다.

---

### 1.3 Open X-Embodiment & RT-X Models (2023)

- **arXiv**: https://arxiv.org/abs/2310.08864
- **저자**: Open X-Embodiment Collaboration (21개 기관, 150+ 연구자)

#### 핵심 Contribution
**22개 로봇 실체(embodiment)**, **527개 스킬**, **100만+ 궤적**을 포함하는 역대 최대 크로스-embodiment 데이터셋과 이를 활용한 RT-X 모델을 공개.

#### 주요 결과
| 모델 | 크기 | 특징 |
|------|-----|------|
| RT-1-X | 35M | RT-1 기반, 9개 로봇으로 학습 |
| RT-2-X | 55B | RT-2 기반, cross-embodiment |

- **Positive Transfer**: 다른 로봇의 데이터로 학습하면 각 로봇의 성능 향상
- Cross-embodiment 일반화의 가능성 최초 대규모 실증

#### 한계점
- 데이터 품질/분포 불균형 (특정 로봇에 편중)
- 표준화된 평가 프로토콜 부재
- 실제 산업 현장의 다양한 조작 시나리오는 아직 미포함

#### Agentic Coding 대비
Open X-Embodiment는 "다양한 코드베이스에서 학습한 LLM이 새로운 언어/프레임워크에도 적용 가능"한 것과 유사하다. 차이점: 코드 간 전이는 문법적 유사성에 기반하지만, 로봇 간 전이는 물리적 실체(형태, 자유도, 센서)의 차이를 극복해야 한다.

---

### 1.4 Octo: Open-Source Generalist Robot Policy (2024)

- **arXiv**: https://arxiv.org/abs/2405.12213
- **저자**: UC Berkeley, Stanford, CMU, Google DeepMind
- **학회**: RSS 2024

#### 핵심 Contribution
Open X-Embodiment 데이터셋의 **80만 궤적**으로 학습한 오픈소스 generalist policy. **Transformer 기반 diffusion policy** 아키텍처.

#### 방법론
- **Readout Tokens + Action Chunking**: 행동 시퀀스 예측 효율화
- **유연한 입출력**: 언어 명령 또는 목표 이미지로 지시 가능
- 새로운 센서 입력과 행동 공간에 빠르게 파인튜닝 가능

#### 주요 결과
- 오픈소스 generalist policy의 **기준점(baseline)** 확립
- 적은 in-domain 데이터로 파인튜닝하여 다양한 시나리오에 일반화
- 언어/이미지 두 가지 지시 모달리티 지원

#### 한계점
- 단독 성능은 task-specific policy에 미치지 못함
- 파인튜닝 없이는 새 환경에서 제한적 성능

#### Agentic Coding 대비
Octo의 "파인튜닝으로 새 환경 적응"은 프로그래밍에서 "context window에 관련 코드를 로드하여 적응"하는 것의 물리적 버전이다. 차이점: 코드 적응은 즉시적(in-context learning)이지만, 로봇 적응은 수시간~수일의 추가 학습이 필요하다.

---

### 1.5 OpenVLA: Open-Source Vision-Language-Action Model (2024)

- **arXiv**: https://arxiv.org/abs/2406.09246
- **저자**: Moo Jin Kim, Karl Pertsch et al. (Stanford, UC Berkeley)

#### 핵심 Contribution
**7B 파라미터**의 오픈소스 VLA로, 실제로 "만져볼 수 있는" VLA의 대표적 기준점. Llama 2 + DINOv2 + SigLIP 결합.

#### 방법론
- Llama 2 7B 언어 모델 + DINOv2/SigLIP 시각 인코더
- 97만 실제 로봇 데모로 학습
- LoRA 파인튜닝 지원 → 소비자 GPU에서 파인튜닝 가능
- 양자화 → 성능 저하 없이 효율적 서빙

#### 주요 결과
| 비교 대상 | OpenVLA 우위 |
|----------|-------------|
| RT-2-X (55B) | **+16.5%** 성공률 (29개 작업, 다중 로봇), 7배 적은 파라미터 |
| Diffusion Policy | **+20.4%** 성공률 (multi-task, 다중 객체) |

- 강력한 언어 grounding 능력
- MIT 라이선스 공개 → 커뮤니티 채택 확산
- 소비자 GPU에서 LoRA 파인튜닝 가능

#### 한계점
- 고주파 정밀 조작에서 action tokenization 한계 (→ FAST로 해결)
- 7B라도 50Hz 실시간 제어에는 추가 최적화 필요
- 단일 이미지 입력 → 시간적 맥락 제한

#### Agentic Coding 대비
OpenVLA는 "오픈소스 LLM으로 코딩 에이전트를 만드는 것"에 대응된다. RT-2-X(55B, 비공개)가 GPT-4와 같다면, OpenVLA(7B, 오픈소스)는 Llama에 해당한다. 오픈소스화가 연구 및 실무 채택을 가속화하는 패턴은 동일하다.

---

### 1.6 π0: Vision-Language-Action Flow Model (2024)

- **arXiv**: https://arxiv.org/abs/2410.24164
- **저자**: Kevin Black, Noah Brown et al. (Physical Intelligence)

#### 핵심 Contribution
**Flow matching** 아키텍처를 VLM 위에 구축하여 연속적·정밀한 행동을 생성하는 generalist policy. 세탁물 접기 같은 **정교한 다단계 dexterous 작업**에서 최초 성공.

#### 방법론
- 사전학습 VLM + flow matching 기반 행동 생성
- 7개 로봇 구성, 68개 작업으로 사전학습
- Zero-shot 일반화 또는 downstream 파인튜닝
- 최대 **50Hz** 실시간 제어

#### 주요 결과
- OpenVLA, Octo 대비 **일관적으로 우수** (셔츠 접기, 테이블 정리, 식료품 포장, 토스터에서 토스트 꺼내기)
- 100초~수분 길이의 다단계 작업 수행
- 세탁물: 건조기에서 꺼내기 → 바구니에 넣기 → 접기 테이블로 이동 → 각 의류 접기

#### 한계점
- Physical Intelligence의 비공개 데이터에 의존
- 재현성 제한 (코드/데이터 비공개)
- 범용성 주장에 비해 평가 환경 다양성 제한

#### Agentic Coding 대비
pi0의 "flow matching"은 이산적 토큰 대신 연속적 행동을 생성한다. Agentic Coding에서 모든 출력이 이산적 텍스트인 것과 달리, 로봇은 연속적 모터 명령이 필요하다. 이 근본적 차이가 action tokenization vs flow matching 논쟁을 낳았다.

---

### 1.7 π0.5: Open-World Generalization (2025)

- **arXiv**: https://arxiv.org/abs/2504.16054
- **저자**: Physical Intelligence

#### 핵심 Contribution
π0을 **open-world**로 확장. 학습 데이터에 없는 **완전히 새로운 집**에서 주방/침실 청소 같은 long-horizon 작업을 수행하는 최초의 end-to-end 학습 기반 로봇 시스템.

#### 방법론
- **Heterogeneous Co-training**: 다양한 로봇 데이터, 고수준 의미 예측, 웹 데이터, 객체 감지 등을 혼합
- **Subtask Prediction**: 고수준 서브태스크를 예측하고 저수준 행동을 생성하는 하이브리드 구조
- 다중 모달리티 입력 (이미지, 언어, 객체 감지, 서브태스크, 저수준 행동)

#### 주요 결과
- 학습 데이터에 **없는 새로운 집**에서 주방 청소 수행: 캐비닛 닫기 → 물건 서랍에 넣기 → 엎질러진 것 닦기 → 식기를 싱크대에
- Long-horizon dexterous manipulation의 open-world 일반화 **최초 달성**

#### 한계점
- "open-world"의 범위가 아직 제한적 (주거 환경 중심)
- 비공개 데이터/모델
- 정량적 비교 기준이 아직 표준화되지 않음

#### Agentic Coding 대비
pi0.5의 "open-world generalization"은 LLM이 학습 데이터에 없는 새로운 API/프레임워크에서도 작동하는 것과 유사하다. 다만 물리 세계에서의 "새로운 환경"은 시각적·물리적 다양성이 디지털 세계보다 훨씬 크다.

---

### 1.8 GR00T N1: Generalist Humanoid Robots (2025)

- **arXiv**: https://arxiv.org/abs/2503.14734
- **저자**: NVIDIA

#### 핵심 Contribution
**Dual-System Architecture**를 명시적으로 구현한 humanoid 로봇용 VLA. System 2 (VLM, 느린 추론)가 환경을 해석하고, System 1 (diffusion transformer, 빠른 행동)이 실시간 모터 행동을 생성.

#### 방법론
- **System 2**: Vision-Language 모듈 → 환경 인식, 언어 지시 해석
- **System 1**: Diffusion Transformer 모듈 → 유연한 실시간 모터 행동 생성
- 두 모듈을 **end-to-end 공동 학습**
- 학습 데이터: 실제 로봇 궤적 + 인간 비디오 + 합성 데이터

#### 주요 결과
- 표준 시뮬레이션 벤치마크에서 **SOTA imitation learning 대비 우수**
- Fourier GR-1 humanoid에서 **양손 조작 작업** 성공
- 높은 데이터 효율 (적은 시연으로 학습)
- Cross-embodiment: tabletop 로봇팔 ~ 휴머노이드까지 지원
- **GR00T-N1-2B**: 모델 체크포인트, 학습 데이터, 벤치마크 공개

#### 한계점
- Humanoid 환경에서의 평가가 주 (이동+조작 통합은 아직 제한)
- 합성 데이터 의존도가 높을 수 있음
- Dual-system 간 상호작용 최적화가 추가 연구 필요

#### Agentic Coding 대비
GR00T N1의 Dual-System은 Agentic Coding의 "계획 (System 2) + 실행 (System 1)"과 구조적으로 동일하다. Claude가 먼저 계획을 세우고(System 2) 코드를 실행하는(System 1) 것처럼, GR00T N1은 환경을 해석하고(System 2) 모터 명령을 생성한다(System 1). 차이점: 코딩에서는 System 1/2가 동일한 LLM이 담당하지만, 로봇에서는 분리된 모듈이 필요하다 (레이턴시 제약).

---

### 1.9 보조 논문 요약

#### FAST: Efficient Action Tokenization (2025)
- **arXiv**: https://arxiv.org/abs/2501.09747
- DCT(이산 코사인 변환) 기반 action tokenization으로 고주파 정밀 제어 가능
- pi0와 결합 시 **10,000시간 로봇 데이터** 스케일 학습, diffusion VLA에 필적하면서 학습 시간 **최대 5배 단축**
- FAST+: 100만 실제 로봇 궤적으로 학습한 범용 action tokenizer

#### TinyVLA: Data-Efficient Small VLA (2024)
- **arXiv**: https://arxiv.org/abs/2409.12514
- 1B 미만 소형 VLM + diffusion head → OpenVLA 대비 **+25.7% 성공률**, **5.5배 적은 파라미터**
- MetaWorld 50개 작업에서 Diffusion Policy 대비 **+21.5%**
- 다양한 일반화 차원(언어, 객체, 위치, 외관, 배경, 환경)에서 강건

#### Diffusion Policy (2023)
- **arXiv**: https://arxiv.org/abs/2303.04137
- 행동을 조건부 denoising diffusion으로 생성 → 12개 작업에서 기존 SOTA 대비 **평균 46.9% 향상**
- VLA가 아니지만, pi0/Octo/GR00T N1의 **low-level policy 기반** 형성
- 다중 모드 행동 분포 처리, 고차원 행동 공간 지원

#### "What Matters in Building VLA Models" (2024)
- **arXiv**: https://arxiv.org/abs/2412.14058
- 8개 VLM backbone, 4개 policy 아키텍처, 600+ 실험으로 체계적 분석
- **핵심 발견**: 연속 행동 공간 + policy-head 구조가 가장 효과적
- **VLM backbone**: KosMos, Paligemma가 우수 (광범위한 VL 사전학습 덕분)
- **Cross-embodiment data**: 사전학습보다 파인튜닝/사후학습에서 효과적

---

## 2. 카테고리 종합 분석

### 2.1 VLA 진화 타임라인

```
2023.03  PaLM-E (562B, multimodal LM, 행동 미직접출력)
   │
2023.07  RT-2 (55B, VLA 확립, action=text token)
   │
2023.10  Open X-Embodiment (1M+ 궤적, cross-embodiment 데이터)
   │
2024.05  Octo (transformer+diffusion, 오픈소스 기준점)
   │
2024.06  OpenVLA (7B, 오픈소스, RT-2-X +16.5%)
   │
2024.09  TinyVLA (<1B, OpenVLA +25.7%)
   │
2024.10  π0 (flow matching, dexterous 조작)
   │
2025.01  FAST (DCT tokenization, 5x 학습 가속)
   │
2025.03  GR00T N1 (dual-system, humanoid)
   │
2025.04  π0.5 (open-world generalization)
```

### 2.2 핵심 설계 축: 5대 선택지

| 설계 축 | 선택지 | 대표 모델 |
|--------|-------|----------|
| **Action 표현** | Discrete token / Flow matching / Diffusion | RT-2 / pi0 / Octo |
| **모델 크기** | 55B / 7B / <1B | RT-2-X / OpenVLA / TinyVLA |
| **사전학습 데이터** | 웹+로봇 / 로봇만 / 시뮬레이션 | RT-2 / Octo / GR00T N1 |
| **아키텍처** | One-step / Interleaved / Policy-head | 다양 / RT-2 / pi0 |
| **오픈소스** | 비공개 / 공개 | RT-2, pi0 / OpenVLA, Octo, GR00T N1 |

### 2.3 VLA의 근본적 한계 (현재진행형)

1. **Action Tokenization vs Continuous**: 이산 토큰은 학습 효율적이지만 정밀도 한계, 연속 행동은 정밀하지만 학습 어려움 → FAST가 절충안 제시
2. **스케일 vs 속도**: 큰 모델은 일반화 우수하지만 실시간 제어 불가 → TinyVLA, FAST가 대안
3. **데이터 병목**: 실제 로봇 데이터 수집 비용이 극도로 높음 → 시뮬레이션/합성 데이터/인간 비디오 활용
4. **Open-world 일반화**: pi0.5가 최초 시도했으나, 아직 주거 환경에 한정
5. **Safety**: VLA가 직접 행동을 출력하므로 안전 보장 메커니즘 필요 (현재 미비)

---

## 3. 인용 네트워크

```
PaLM (540B)
    └──→ PaLM-E (2023.03) ──→ RT-2 (2023.07) ──→ RT-2-X (2023.10)
                                    │                     │
                               OpenVLA (2024.06)    Open X-Embodiment
                                    │                     │
                               TinyVLA (2024.09)    Octo (2024.05)
                               
Diffusion Models
    └──→ Diffusion Policy (2023.03) ──→ Octo ──→ pi0 (flow matching)
                                              └──→ GR00T N1 (diffusion transformer)

RT-2 + Diffusion Policy
    └──→ pi0 (2024.10) ──→ pi0.5 (2025.04)
                       └──→ FAST (2025.01)
```

---

## 4. 연구 그룹 매핑

| 그룹 | 핵심 모델 | 특징 |
|------|---------|------|
| **Google DeepMind** | PaLM-E, RT-2, RT-X, AutoRT | VLA의 원조, 대규모 데이터+모델 |
| **Physical Intelligence** | pi0, pi0.5, FAST | Flow matching, dexterous manipulation |
| **UC Berkeley (RAIL)** | Octo, OpenVLA, DROID | 오픈소스 생태계 주도 |
| **Stanford** | OpenVLA, CaP-X | 오픈소스 + 벤치마크 |
| **NVIDIA** | GR00T N1 | Humanoid, dual-system, 시뮬레이션 |

---

## 5. Agentic Coding ↔ VLA: 근본적 차이점 요약

| 차원 | Agentic Coding | VLA |
|------|---------------|-----|
| 행동 공간 | 이산적 (텍스트/코드) | 연속적 (모터 토크/속도) |
| 관찰 | 완전 관찰 (파일 시스템) | 부분 관찰 (카메라, 센서) |
| 피드백 지연 | 즉시 (ms) | 지연 (물리 세계 반응 시간) |
| 되돌리기 | 가능 | 불가능 |
| 일반화 기반 | 코드의 구문적 유사성 | 시각·물리적 유사성 |
| 데이터 비용 | 인터넷에 풍부 | 수집 비용 극도로 높음 |
| 안전 위험 | 낮음 (sandbox) | 높음 (물리적 충돌) |

---

*작성일: 2026-04-08*
*서베이 범위: 2023.03 ~ 2025.04*
