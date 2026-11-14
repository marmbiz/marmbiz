# Hi, I'm Martin 👋

**Senior Digital Platform Manager** - CMS, UX, content governance & AI workflows.

I come from managing digital platforms, not from a pure software-engineering track: content systems, editorial workflows, SEO and governance for regulated industries such as German statutory health insurance (*Krankenkassen / GKV*), banking and biotech. With coding agents, I turn those operating problems into open tools and empirical studies with documented methods.

My two main public projects are:

- **[humanizer-de](https://github.com/marmbiz/humanizer-de)**: one of the most-starred German-focused AI humanizer skills on GitHub, with **200+ stars**.[^humanizer-stars] Built for **Claude Code & OpenAI Codex** to edit German AI text while preserving facts and author voice.
- **[AußenBlick GKV – Studie zu öffentlichen Krankenkasseninformationen](https://martin-moeller.biz/lab/aussenblick-gkv)**: a study of **56,198 public pages across 84 websites and sub-sites** in the German statutory health insurance sector. It examines how LLM-assisted triage can prioritise specialist review of health and benefit information. [Preprint: arXiv:2608.03500](https://arxiv.org/abs/2608.03500).

🌐 [martin-moeller.biz](https://martin-moeller.biz) · 💼 [LinkedIn](https://www.linkedin.com/in/martinmoellerbiz) · 🤗 [Hugging Face](https://huggingface.co/marmbiz) · [ORCID](https://orcid.org/0009-0009-4352-8765)

---

## 🧹 humanizer-de — German AI Text Humanizer

**KI-Texte menschlicher machen: KI-Floskeln redigieren, Schreibstimme erhalten.**

[**humanizer-de**](https://github.com/marmbiz/humanizer-de) is an open-source **Claude Code & OpenAI Codex skill** with **200+ GitHub stars**. It combines a **72-pattern catalog** of German AI clichés (*KI-Floskeln*), **register & rhythm analysis**, selected **deterministic linting** and a **5-pass editorial review**. Its evidence-safe (*belegtreu / quellentreu*) post-editing is designed to preserve facts, sources and the author's voice (*Schreibstimme*).

Built for German editorial teams, content governance, SEO and regulated publishing. [Read the German guide](https://martin-moeller.biz/lab/ki/humanizer-deutsch-ki-texte-erkennen-entfernen) or [install the skill](https://github.com/marmbiz/humanizer-de#installation). [Licenses: MIT + CC BY-SA 4.0](https://github.com/marmbiz/humanizer-de/blob/main/NOTICE).

**Try it without installing a skill:** [Humanizer mini prompt in Grok](https://x.ai/bot/0CnSle5jrlIDlJIRVy4VM). Open the template and paste your German text. This short editing prompt works on AI stock phrases with instructions to preserve facts and voice; the full skill adds the pattern catalog and local checks.

---

## 🔬 Research & platform audits

### 🔍 AußenBlick GKV — German statutory health insurance (*Krankenkassen*) audit

[AußenBlick GKV – Studie zu öffentlichen Krankenkasseninformationen](https://martin-moeller.biz/lab/aussenblick-gkv) covers **56,198 public pages across 84 websites and sub-sites** of German statutory health insurers (*gesetzliche Krankenversicherung / Krankenkassen*), using a May 2026 snapshot.

The study examines medical and benefit information, legal framing, transparency and contradictions to build a prioritised workload for editorial and specialist review. Model-assisted triage identifies review candidates; medical or legal conclusions require human adjudication. The study reports a review workload, not an error rate or insurer ranking.

📄 **Preprint:** [AußenBlick GKV: LLM-Assisted Review Prioritization for German Statutory Health Insurance Websites: A Multi-Stage Corpus Audit](https://arxiv.org/abs/2608.03500) — arXiv:2608.03500 (cs.CY). [Open-access preprint on Zenodo](https://doi.org/10.5281/zenodo.20591063). A German short form is under submission at *Monitor Versorgungsforschung*. The paper documents the method and its reproducibility limits.

🎤 **Talk (DE):** [AußenBlick GKV — „Wer verantwortet die Information, der Sie vertrauen?“](https://www.youtube.com/watch?v=YHvQs7Dq4tI) — a spoken walkthrough of the Krankenkassen study.

### Additional empirical studies & platform audits

🎙️ [**Transcription models compared: Deepgram vs. Whisper**](https://martin-moeller.biz/en/lab/ai/transcription-models-compared-podcast-ungeskriptet) *(new)* - The AußenBlick review system applied to 898 hours of the German podcast {ungeskriptet} (331 episodes). Deepgram nova-3 for words and speaker separation, Whisper large-v3-turbo as a second pass, names checked by a language model. Audio clips show where each model mishears. One podcast, not a general benchmark.

📊 [**What are Claude skills about?**](research/claude-skill-landscape.md) *(new)* - A metadata census of 8,277 non-fork Claude skill repositories on GitHub, classified by theme. Design leads at 28.5%, the median repo has 2 stars, and the field peaked in May 2026. No `SKILL.md` was read - metadata only, so there is no prompt-injection surface. Method, chart and raw data included.

🎲 [**Kolibri-1 safety field test**](https://huggingface.co/datasets/marmbiz/kolibri-1-eni-safety-consistency) *(new)* - An exploratory case study with 20 recorded responses under an ENI-derived persona jailbreak and client control of the system message. AI-assisted classification found 12 instructional responses and 8 refusals. Redacted data, methods and limitations are included; no neutral control or independent human review.

✍️ [**The Lab**](https://martin-moeller.biz/en/lab) - Notes on SEO, GEO and AI-content governance from running real platforms.

---

## 🛠️ Other open source tools

Small, opinionated tools I build and use myself.

🧩 [**fusion-lite**](https://github.com/marmbiz/fusion-lite) - Local multi-model panels for running Claude, Codex, Gemini, Grok and other CLI/API tools from one terminal workflow.

🧭 [**future-self**](https://github.com/marmbiz/future-self) *(new)* - A decision-coherence skill for Claude Code and Codex. One question – "Will my future self thank me for this?" – and a five-stage exercise for when the answer dodges. Ends in kill criteria, not advice.

🎀 [**tomoko**](https://github.com/marmbiz/tomoko) *(new)* - A compact persona-based LLM jailbreak (2.5k chars, ~91% smaller than its ENI LIME reference), built on Anthropic's published prompting research and tested against nine models (LongCat, Nemotron, Ling, MiMo, Space Bunny, DeepSeek 4.1) with a documented probe matrix. Ships as an opencode agent; includes a hands-on red-team variant.

[^humanizer-stars]: GitHub [repositories tagged `humanizer` and `german`, sorted by stars](https://github.com/search?q=topic%3Ahumanizer+topic%3Agerman&type=repositories&s=stars&o=desc), checked November 14, 2026: humanizer-de had 207 stars and ranked first among the 12 results. This comparison covers those topic-tagged repositories.
