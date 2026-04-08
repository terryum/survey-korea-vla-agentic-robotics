---
title: "Table of Contents"
subtitle: "목차"
date: "2026-04-08"
last_updated: "2026-04-08"
---

# From LLM Planners to Agentic Robotics — The Future of Physical AI

## Table of Contents

---

### Part I: Foundations — When LLMs Meet Robots

**Chapter 1. Introduction — From Agentic Coding to Agentic Robotics**
- 1.1 What Is Agentic AI?
- 1.2 The Success of Agentic Coding: code → tool → execution → error → LLM Loop
- 1.3 Extending to the Physical World: Why the Same Loop Fails
- 1.4 The Seven-Dimension Gap — Core Framework of This Book
- 1.5 Structure and Reading Guide

**Chapter 2. LLM as Planner — Zero-Shot Planning and Grounding**
- 2.1 Leveraging LLM World Knowledge for Robot Planning
- 2.2 Language Models as Zero-Shot Planners [Huang et al., 2022]
- 2.3 SayCan: Grounding Language in Robotic Affordances [Ahn et al., 2022]
- 2.4 SayPlan: Scaling Planning with 3D Scene Graphs [Rana et al., 2023]
- 2.5 Evolution: "Generate" → "Ground" → "Structure"
- 2.6 Agentic Coding Contrast: Presence vs Absence of the Observation-Action Gap

**Chapter 3. Code as Policies — Controlling Robots with Code**
- 3.1 Why Code Is a Superior Robot Control Interface
- 3.2 Code as Policies [Liang et al., 2022]
- 3.3 Code-as-Symbolic-Planner [Chen et al., 2025]
- 3.4 CaP-X: Benchmarking Coding Agents for Robot Manipulation [Fu et al., 2026]
- 3.5 RL-GPT: Code Agent + RL Agent [2024]
- 3.6 Evolution: "API Glue" → "Reasoning Tool" → "Agentic System"
- 3.7 Direct Correspondence with Agentic Coding

---

### Part II: The VLA Revolution

**Chapter 4. The Rise of Vision-Language-Action Models**
- 4.1 What Is VLA: See (V), Understand (L), Act (A)
- 4.2 PaLM-E: The First Large-Scale Embodied Multimodal LM [Driess et al., 2023]
- 4.3 RT-2: Transferring Web Knowledge to Robot Actions [Brohan et al., 2023]
- 4.4 Open X-Embodiment: The Power of Cross-Embodiment Data [2023]
- 4.5 Octo: Open-Source Generalist Policy [Ghosh et al., 2024]
- 4.6 OpenVLA: 7B Open-Source VLA [Kim et al., 2024]
- 4.7 pi0 / pi0.5: Flow Matching and Open-World Generalization [2024-2025]
- 4.8 GR00T N1: Dual-System Architecture [NVIDIA, 2025]
- 4.9 Evolution of Action Tokenization: RT-2 → FAST → Flow Matching
- 4.10 Five Design Axes and Trade-offs in VLA
- 4.11 Agentic Coding Contrast: Discrete Text vs Continuous Motor Commands

**Chapter 5. Hierarchical Planning — From High-Level to Low-Level**
- 5.1 Why Hierarchical Separation Is Necessary
- 5.2 AutoTAMP: LLM as Translator + Checker [Chen et al., 2023]
- 5.3 RT-H: Language Motion as Intermediate Representation [Belkhale et al., 2024]
- 5.4 Hi Robot: Real-Time Human Feedback Integration [Shi et al., 2025]
- 5.5 HAMSTER: The Power of Off-Domain Data [Li et al., 2025]
- 5.6 Four Forms of Hierarchical Separation
- 5.7 Agentic Coding Contrast: Pseudocode and Language Motion

**Chapter 6. Low-Level Control — Diffusion Policy and 3D Representations**
- 6.1 Where High-Level Plans Get Executed
- 6.2 Diffusion Policy [Chi et al., 2023]
- 6.3 3D Diffuser Actor [Ke et al., 2024]
- 6.4 DROID: Large-Scale Real-World Dataset [Khazatsky et al., 2024]
- 6.5 TinyVLA: Lightweight VLA [2024]
- 6.6 FAST: Action Tokenization Innovation [2025]
- 6.7 Agentic Coding Contrast: Deterministic vs Stochastic Execution Engines

---

### Part III: Toward Agentic Robotics

**Chapter 7. Memory and World Representation**
- 7.1 What Must Robots Remember for Long-Horizon Tasks?
- 7.2 KARMA: Long-Term and Short-Term Memory Systems [Wang et al., 2024]
- 7.3 Embodied-RAG: Spatial-Semantic Hierarchical Retrieval [Xie et al., 2024]
- 7.4 RoboEXP: Action-Conditioned Scene Graphs [Jiang et al., 2024]
- 7.5 VeriGraph: Scene Graphs for Execution Verification [Ekpo et al., 2024]
- 7.6 MoMa-LLM, 3D-Mem, RoboMemory: Evolving Memory Architectures
- 7.7 Four Uses of Scene Graphs: Planning / Action-Conditioned / Retrieval / Verification
- 7.8 Agentic Coding Contrast: File Systems vs 3D Scene Graphs

**Chapter 8. Closed-Loop Agentic Systems**
- 8.1 From Open-Loop to Closed-Loop: Why Feedback Is Essential
- 8.2 REFLECT: Learning from Failure [Liu et al., 2023]
- 8.3 AutoRT: Autonomous Large-Scale Robot Fleet Operation [Brohan et al., 2024]
- 8.4 BUMBLE: Building-Wide Mobile Manipulation [Garrett et al., 2024]
- 8.5 PragmaBot: A Pragmatist Robot Learning from Real-World Experience [2025]
- 8.6 Core Elements of Closed-Loop: Detect → Diagnose → Replan → Execute
- 8.7 Agentic Coding Contrast: The Physical-World Version of code → execute → error → fix

**Chapter 9. Sim-to-Real Transfer and Evaluation**
- 9.1 The Promise and Limits of Simulation
- 9.2 SIMPLER: Evaluating Real-World Policies in Simulation [Li et al., 2024]
- 9.3 Natural Language Sim2Real [2024]
- 9.4 Vision Encoder Pre-Training for Sim2Real Transfer [2025]
- 9.5 CaP-X Sim2Real: Minimal Gap with CaP-RL [2026]
- 9.6 Agentic Coding Contrast: Simulation ≈ Production vs Sim2Real Gap

---

### Part IV: The Fundamental Divide — Digital Agents vs Physical Agents

**Chapter 10. Agentic Coding vs Agentic Robotics — The Gap and the Future**
- 10.1 Comprehensive Seven-Dimension Gap Analysis
- 10.2 Paradigm Shift Timeline (2022-2026)
- 10.3 Eight Open Problems
- 10.4 Predicting the Next Shift: Embodied World Models (2026-2027)
- 10.5 Transplanting Success Factors from Agentic Coding to Robotics
- 10.6 Conclusion: Toward Agentic AI in the Physical World

---

## References

→ `references.bib` (Unified BibTeX)

---

## Appendices

**Chapter 11. Appendix — Architecture of Agentic Coding Systems**
- 11.1 Introduction: Why Examine the Internals of Coding Agents
- 11.2 Claude Code's Architecture
  - Three-Layer Memory System (CLAUDE.md / Session Context / Tool-Based Retrieval)
  - Tool Orchestration (Read, Edit, Bash, Grep, Agent)
  - Subagents and Parallel Execution
  - The Feedback Loop: From Error to Fix
  - Permission Model and Safety Guardrails
- 11.3 OpenAI Codex's Architecture
  - Container-Based Sandbox
  - AGENTS.md — Codex's Counterpart to CLAUDE.md
  - From codex-1 to GPT-5.3-Codex
  - Unified Server Architecture
- 11.4 Common Success Patterns (Six Patterns)
- 11.5 Transplanting to Agentic Robotics
- 11.6 Future Vision: Claude Code for the Physical World
- 11.7 Conclusion

---

- A. Paper Influence Map (Four Research Flows)
- B. Research Group Contributions
- C. Key Abbreviations and Glossary
