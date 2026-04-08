중요도 기준: **[S]** 는 survey book의 핵심 축을 이루는 필수 인용 논문, **[A]** 는 본문에서 비교·정리해야 할 대표 논문, **[B]** 는 세부 챕터나 사례 분석에서 선택적으로 확장하면 좋은 보조 논문입니다. **Survey book 집필 시에는 이 중요도를 참고해 본문 비중, 도표 배치, related work 우선순위를 정하시면 됩니다.**

# 2023–2025 LLM/VLM → Code → Agentic Robotics 논문 큐레이션

이 문서는 **최근 3년(대체로 2023–2025)** 안에 arXiv에 올라온 논문 중에서, 다음 흐름을 중심으로 읽기 좋은 논문들을 정리한 목록입니다.

- **LLM/VLM → code / symbolic / planning → agentic robotics**
- 이를 보조하는 **long-term / short-term memory**
- **high-level / low-level planning**
- **scene graph / world representation**
- **sim2real / evaluation / transfer**
- 가능하면 **review / survey paper**를 먼저 두고, 그 안에서 반복적으로 언급되거나 실제로 많이 회자되는 대표 논문을 골랐습니다.

## 표시 기준

- **[S]**: survey book의 메인 챕터와 핵심 그림/표에 반드시 들어갈 가능성이 높은 논문
- **[A]**: 해당 세부 주제를 대표하며, 비교 분석이나 related work에서 비중 있게 다룰 가치가 큰 논문
- **[B]**: 세부 흐름을 보강하거나 사례를 풍부하게 만드는 데 유용한 보조 논문

---

## 0. 가장 먼저 읽을 survey / review paper

### A. 전체 지형을 잡는 survey
- **[S] Large Language Models for Robotics: A Survey** (2023)  
  https://arxiv.org/abs/2311.07226  
  - LLM을 robotics stack의 perception / planning / control / interaction에 어떻게 끼워 넣는지 넓게 정리합니다.

- **[A] A Survey on Integration of Large Language Models with Intelligent Robots** (2024)  
  https://arxiv.org/abs/2404.09228  
  - communication, perception, planning, control 관점으로 정리되어 있어 입문용으로 좋습니다.

- **[S] A Survey on Robotics with Foundation Models: toward Embodied AI** (2024)  
  https://arxiv.org/abs/2402.02385  
  - 특히 **autonomous manipulation**, **high-level planning**, **low-level control** 구분이 명확합니다.

- **[S] Toward General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis** (2023)  
  https://arxiv.org/abs/2312.08782  
  - generalist robot / foundation model / embodiment generalization 축을 이해하기 좋습니다.

### B. VLA 중심 survey
- **[S] A Survey on Vision-Language-Action Models for Embodied AI** (2024)  
  https://arxiv.org/abs/2405.14093  
  - VLA를 **component / low-level policy / high-level task planner**로 나누어 보는 데 가장 직접적입니다.

- **[A] Vision-Language-Action Models: Concepts, Progress, Applications and Challenges** (2025)  
  https://arxiv.org/abs/2505.04769  
  - 2024–2025 VLA 계열을 한 번에 훑어보기 좋습니다.

### C. planning / embodied AI / sim2real 보조 survey
- **[S] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI** (2024)  
  https://arxiv.org/abs/2407.06886  
  - embodied perception / interaction / agents / sim-to-real 을 한 프레임에서 봅니다.

- **[A] A Survey on Large Language Models for Automated Planning** (2025)  
  https://arxiv.org/abs/2502.12435  
  - robotics에 한정되진 않지만, **LLM을 planner로 어디까지 믿을 수 있는가**를 판단하는 데 유용합니다.

- **[B] A Survey of Sim-to-Real Methods in RL** (2025)  
  https://arxiv.org/abs/2502.13187  
  - foundation model/VLA 자체가 아니라도, sim2real 관점을 체계적으로 정리할 때 좋습니다.

---

## 1. 핵심 메인라인: embodied foundation model / VLA / generalist policy

이 섹션은 “**LLM/VLM을 로봇 policy로 직접 연결**”하는 큰 줄기입니다.

- **[S] PaLM-E: An Embodied Multimodal Language Model** (2023)  
  https://arxiv.org/abs/2303.03378  
  - language model 안에 robot state / image / text를 함께 넣는 초기 대표작.
  - RT-2 이전의 embodied multimodal LM 흐름을 이해할 때 중요합니다.

- **[S] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** (2023)  
  https://arxiv.org/abs/2307.15818  
  - “VLM의 웹 지식을 robot action으로 직접 옮긴다”는 VLA 메인스트림의 상징적인 논문.

- **[S] Open X-Embodiment: Robotic Learning Datasets and RT-X Models** (2023)  
  https://arxiv.org/abs/2310.08864  
  - cross-embodiment / large-scale robot dataset / generalist policy의 기반 데이터 축.

- **[S] Octo: An Open-Source Generalist Robot Policy** (2024)  
  https://arxiv.org/abs/2405.12213  
  - Open X-Embodiment 기반 generalist policy의 오픈소스 기준점.

- **[S] OpenVLA: An Open-Source Vision-Language-Action Model** (2024)  
  https://arxiv.org/abs/2406.09246  
  - 최근 open VLA 생태계의 대표 기준점.
  - “실제로 만져볼 수 있는 VLA”라는 점에서 실무적 가치가 큽니다.

- **[B] TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation** (2024)  
  https://arxiv.org/abs/2409.12514  
  - 경량화 / 데이터 효율 관점에서 VLA를 보고 싶을 때 좋습니다.

- **[A] Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models** (2024)  
  https://arxiv.org/abs/2412.14058  
  - backbone, action formulation, cross-embodiment data 등 **VLA 설계 변수**를 체계적으로 봅니다.

- **[A] FAST: Efficient Action Tokenization for Vision-Language-Action Models** (2025)  
  https://arxiv.org/abs/2501.09747  
  - VLA에서 action tokenization이 실제로 얼마나 중요한지 보여주는 대표 논문.

- **[S] π0: A Vision-Language-Action Flow Model for General Robot Control** (2024)  
  https://arxiv.org/abs/2410.24164  
  - flow-matching 계열 generalist robot policy의 강력한 대표작.

- **[A] π0.5: a Vision-Language-Action Model with Open-World Generalization** (2025)  
  https://arxiv.org/abs/2504.16054  
  - open-world generalization / long-horizon dexterous manipulation 쪽으로 확장된 후속작.

- **[A] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** (2025)  
  https://arxiv.org/abs/2503.14734  
  - humanoid 쪽으로 VLA를 확장한 대표 사례.
  - dual-system(System 2 reasoning + System 1 action) 구조를 명시적으로 드러냅니다.

---

## 2. LLM/VLM 기반 high-level planning, TAMP, hierarchy, code generation

이 섹션은 “**LLM/VLM을 planner / program synthesizer / symbolic interface**로 쓰는 방향”입니다.

- **[S] Task and Motion Planning with Large Language Models for Object Rearrangement** (2023)  
  https://arxiv.org/abs/2303.06247  
  - LLM을 TAMP에 직접 연결하는 초기 대표작 중 하나.

- **[S] AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers** (2023)  
  https://arxiv.org/abs/2306.06531  
  - LLM을 자연어→형식 명세 translator, 그리고 checker로 쓰는 구성이 핵심입니다.
  - “LLM을 planner 그 자체보다 **planner의 전처리기 + 검증기**로 쓰는 편이 낫다”는 감각을 줍니다.

- **[S] SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning** (2023)  
  https://arxiv.org/abs/2307.06135  
  - 3D scene graph를 써서 long-horizon planning을 grounding하는 대표 논문.
  - scene graph가 planning의 확장성 문제를 어떻게 줄이는지 보기 좋습니다.

- **[A] RT-H: Action Hierarchies Using Language** (2024)  
  https://arxiv.org/abs/2403.01823  
  - language motion을 intermediate representation으로 쓰는 **hierarchical action** 접근.

- **[A] Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models** (2025)  
  https://arxiv.org/abs/2502.19417  
  - complex prompt, user correction, multi-stage instruction을 처리하는 **high-level/low-level 분리형 VLA**.
  - 인간 피드백이 실시간으로 끼어드는 agentic robotics에 특히 중요합니다.

- **[A] HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation** (2025)  
  https://arxiv.org/abs/2502.05485  
  - high-level VLM은 coarse path / low-level policy는 precise control.
  - **off-domain data, sketches, videos, simulation**을 hierarchical VLA가 더 잘 활용한다는 메시지가 강합니다.

- **[S] Code-as-Symbolic-Planner: Foundation Model-Based Robot Planning via Symbolic Code Generation** (2025)  
  https://arxiv.org/abs/2503.01700  
  - 사용자의 관심축인 “**LLM/VLM → code → planning**”에 가장 직접적으로 닿는 최근 논문 중 하나.
  - code를 단순 API glue가 아니라 **solver / planner / checker**로 쓰는 점이 핵심입니다.

- **[A] Natural Language as Policies: Reasoning for Coordinate-Level Embodied Control with LLMs** (2024)  
  https://arxiv.org/abs/2403.13801  
  - language를 coordinate-level control까지 연결하려는 흥미로운 방향.

- **[B] RL-GPT: Integrating Reinforcement Learning and Code-as-Policies for Language-Driven Robot Control** (2024)  
  https://arxiv.org/abs/2402.19299  
  - code-centric slow agent + RL fast agent 구조로, code와 low-level control의 분리를 보여줍니다.

---

## 3. Memory, long-horizon execution, scene graph, structured world representation

이 섹션은 “**agentic robotics가 길게 일하려면 무엇을 기억해야 하는가**”에 관한 논문들입니다.

- **[S] KARMA: Augmenting Embodied AI Agents with Long-and-short Term Memory Systems** (2024)  
  https://arxiv.org/abs/2409.14908  
  - long-term / short-term memory를 분리하고, long-term memory를 **3D scene graph**로 다루는 매우 직접적인 논문.

- **[S] Embodied-RAG: General Non-parametric Embodied Memory for Retrieval and Generation** (2024)  
  https://arxiv.org/abs/2409.18313  
  - embodied agent용 RAG를 정면으로 다룹니다.
  - memory를 “문서 검색”이 아니라 **spatial / semantic hierarchy**로 재구성하려는 점이 중요합니다.

- **[B] 3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning** (2024)  
  https://arxiv.org/abs/2411.17735  
  - long-term embodied memory를 3D scene memory로 푸는 방향.
  - 조작(manipulation)보다 넓은 embodied reasoning 관점에서 유용합니다.

- **[S] RoboEXP: Action-Conditioned Scene Graph via Interactive Exploration for Robotic Manipulation** (2024)  
  https://arxiv.org/abs/2402.15487  
  - interactive exploration을 통해 **action-conditioned scene graph**를 구축.
  - 단순 perception graph가 아니라 “어떻게 조작할 수 있는가”까지 포함한다는 점에서 중요합니다.

- **[A] Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation** (MoMa-LLM) (2024)  
  https://arxiv.org/abs/2403.08605  
  - language-grounded scene graph + mobile manipulation + object-centric action space.
  - scene graph가 LLM grounding의 실질적 인터페이스가 될 수 있음을 보여줍니다.

- **[A] VeriGraph: Scene Graphs for Execution Verifiable Robot Planning** (2024)  
  https://arxiv.org/abs/2411.10446  
  - scene graph를 intermediate representation으로 써서 **plan verification / refinement**까지 수행.

- **[B] LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics** (2025)  
  https://arxiv.org/abs/2504.21716  
  - local lightweight LLM 기반 agent orchestration + memory-augmented planning.
  - 실제 household robotics stack에 가까운 구현 감각이 있습니다.

- **[B] RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Lifelong Learning in Physical Embodied Systems** (2025)  
  https://arxiv.org/abs/2508.01415  
  - physical embodied systems에서 lifelong learning과 multi-memory architecture를 노린 최근 논문.
  - 아직 아주 최신 축이지만, “agentic memory stack”을 로봇에 심는다는 관점에서 눈여겨볼 만합니다.

---

## 4. Low-level control, 3D policy, diffusion, real-robot data

이 섹션은 **high-level LLM/VLM planner가 결국 어떤 low-level policy 위에 올라타는가**를 이해하는 데 중요합니다.

- **[S] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023)  
  https://arxiv.org/abs/2303.04137  
  - 엄밀히 LLM/VLM 논문은 아니지만, 최근 robot policy의 low-level 기준점을 형성한 핵심 논문.

- **[A] 3D Diffuser Actor: Policy Diffusion with 3D Scene Representations** (2024)  
  https://arxiv.org/abs/2402.10885  
  - 3D scene representation과 diffusion policy를 결합.
  - scene representation이 low-level control robustness에 왜 중요한지 잘 보여줍니다.

- **[S] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset** (2024)  
  https://arxiv.org/abs/2403.12945  
  - recent real-robot foundation policy 계열에서 매우 중요한 데이터셋 논문.
  - diverse real-world manipulation data가 얼마나 중요한지 보여줍니다.

---

## 5. Sim2real, evaluation, transfer

화장품 제조업 현장에 적용을 생각하면, 여기의 중요도가 매우 높습니다.

- **[S] Evaluating Real-World Robot Manipulation Policies in Simulation** (SIMPLER) (2024)  
  https://arxiv.org/abs/2405.05941  
  - real-world policy를 simulation에서 얼마나 믿고 평가할 수 있는지 다루는 대표 논문.
  - VLA / generalist policy를 대규모로 비교할 때 유용합니다.

- **[A] Natural Language Can Help Bridge the Sim2Real Gap** (2024)  
  https://arxiv.org/abs/2405.10020  
  - sim과 real을 직접 픽셀 매칭하지 않고, **language description**을 중간 의미 표현으로 쓰는 흥미로운 접근.

- **[A] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer** (2025)  
  https://arxiv.org/abs/2501.16389  
  - pre-trained vision encoder가 sim2real transfer에 주는 효과를 분석합니다.

---

## 6. 빠른 추천 읽기 순서

### 6-1. “전체 지형”을 빨리 잡고 싶다면
1. **A Survey on Vision-Language-Action Models for Embodied AI**  
2. **A Survey on Robotics with Foundation Models: toward Embodied AI**  
3. **Large Language Models for Robotics: A Survey**

### 6-2. “VLA 메인스트림”을 따라가고 싶다면
1. **PaLM-E**  
2. **RT-2**  
3. **Open X-Embodiment**  
4. **Octo**  
5. **OpenVLA**  
6. **π0 / π0.5**  
7. **GR00T N1**

### 6-3. “LLM/VLM → planner/code → embodied agent”를 따라가고 싶다면
1. **Task and Motion Planning with LLMs for Object Rearrangement**  
2. **AutoTAMP**  
3. **SayPlan**  
4. **RT-H**  
5. **Hi Robot**  
6. **HAMSTER**  
7. **Code-as-Symbolic-Planner**

### 6-4. “memory / scene graph / long-horizon”을 따라가고 싶다면
1. **RoboEXP**  
2. **MoMa-LLM**  
3. **KARMA**  
4. **Embodied-RAG**  
5. **3D-Mem**  
6. **VeriGraph**  
7. **RoboMemory**

### 6-5. “실제 적용성 / transfer / evaluation”을 먼저 보고 싶다면
1. **DROID**  
2. **SIMPLER**  
3. **OpenVLA**  
4. **HAMSTER**  
5. **Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer**

---

## 7. 제조업/현장 적용 관점에서 특히 볼 만한 축

### A. 현장형 agentic robotics에 가까운 것
- Hi Robot
- HAMSTER
- Code-as-Symbolic-Planner
- LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics

### B. 메모리 / 상태 추적 / 재계획이 중요한 것
- KARMA
- Embodied-RAG
- VeriGraph
- RoboMemory

### C. scene graph / structured state representation이 중요한 것
- SayPlan
- RoboEXP
- MoMa-LLM
- VeriGraph

### D. real-robot generalization / transfer 관점에서 중요한 것
- Open X-Embodiment
- DROID
- OpenVLA
- π0 / π0.5
- SIMPLER
- HAMSTER

---

## 8. 메모: 이 목록을 어떻게 쓰면 좋은가

이 목록은 크게 세 갈래로 읽으면 좋습니다.

1. **Survey 2~3편으로 taxonomy를 먼저 잡는다.**  
2. 그 다음 **VLA 본류(OpenVLA, π0, GR00T N1)** 와 **planning 본류(AutoTAMP, SayPlan, Hi Robot, Code-as-Symbolic-Planner)** 를 분리해서 읽는다.  
3. 마지막으로 **memory / scene graph / sim2real** 을 붙여서, “실제 오래 일하는 로봇 시스템” 관점으로 다시 묶어 본다.  

---

## 부록. 요청 범위(최근 3년) 밖이지만 꼭 같이 봐야 하는 precursor 2편

아래 둘은 2022년 논문이라 이번 본문 범위에서는 제외했지만, 사용자가 관심 있는 **code-as-policy / LLM grounding** 계열의 원형이라 함께 보는 편이 좋습니다.

- **[S] Do As I Can, Not As I Say: Grounding Language in Robotic Affordances** (SayCan) (2022)  
  https://arxiv.org/abs/2204.01691

- **[S] Code as Policies: Language Model Programs for Embodied Control** (2022)  
  https://arxiv.org/abs/2209.07753
