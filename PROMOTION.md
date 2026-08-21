# 引流安利文案 / Promotion Copy

> 适用场景：把 `task-clarify-heuristic` 推到社区冲爆款。
> 双仓库地址（帖子里直接用）：
> - GitHub：https://github.com/luoxianqiang158/task-clarify-heuristic
> - ModelScope：https://www.modelscope.cn/luoxianqiang/task-clarify-heuristic
> 配图建议：帖子首图用 `assets/cover-github.png`（横版）或 `assets/demo.gif`（动图演示更吸睛）。

---

## 一、中文版

### 1. 掘金 / 知乎（深度长文风）

**标题**：你给 Agent 的任务越写越长，它却越跑越偏？试试"反向澄清"这个 Skill

**正文**：

Agent 平台现在很强——WorkBuddy、Dify、OpenCode 随便挑。但一个真实的痛点没人提：**我们很容易把"模糊想法"直接当成"任务指令"扔给 Agent**，结果它吭哧吭哧干半天，方向全错。

比如你随口说一句"帮我分析销售数据"，Agent 怎么知道：
- 这份报告是给老板看还是给团队看？
- 要找异常，还是要给出可落地建议？
- 输出 Markdown 还是 PPT？能不能联网查资料？

我做了个 Skill：**task-clarify-heuristic（任务目标澄清助手）**。它不替你干活，而是先**反向审你的需求**——通过启发式多轮提问，把模糊任务收敛成一份结构化 Agent 任务规约，再交给下游 Agent 执行。

核心三个设计：
1. **区分"手段"和"目标"** —— 你说"写个 PPT"，它追问"真实目的是说服客户采购吗？"
2. **自动猜测补全** —— 信息不足时主动给假设让你确认/修正，而不是干巴巴地等你填表。
3. **跨平台通用** —— 同一份澄清逻辑，WorkBuddy / Dify / OpenCode 都能用，产出是纯文本规约可直接喂下游。

纯提示词、零依赖、MIT 开源。仓库里带了：
- 5 类任务的分类提问题库（代码/内容/研究/设计/数据分析）
- 3 个完整对话示例（代码、内容创作、研究分析）
- 一张 Demo 动图，一眼看懂流程

GitHub：https://github.com/luoxianqiang158/task-clarify-heuristic
ModelScope：https://www.modelscope.cn/luoxianqiang/task-clarify-heuristic

欢迎 star / 提 issue，一起把它打磨成 Agent 时代的"需求防跑偏护栏"。

---

### 2. V2EX / 即刻（短平快风）

**标题**：做了一个给 Agent 用的"需求澄清" Skill，专治任务描述不清导致跑偏

一句话：你给 Agent 的任务越模糊，它越容易乱干。这个 Skill 在真正执行前，先用 2-3 轮启发式提问把"业务目标 / 受众 / 验收标准 / 约束 / 边界"补全，输出一份结构化任务规约。

亮点：区分"手段 vs 目标"、自动猜测补全、跨 Dify/WorkBuddy/OpenCode 通用、纯提示词零依赖。

Demo 动图直接看效果 👉 https://github.com/luoxianqiang158/task-clarify-heuristic
ModelScope 同步：https://www.modelscope.cn/luoxianqiang/task-clarify-heuristic

---

### 3. 小红书 / 视频号封面文案（卡片式）

**主标题**：别再让 Agent 乱跑了 🛑
**副标题**：一个 Skill，把模糊需求变成清晰指令
**三点**：手段≠目标 · 自动猜你想要 · 跨平台通用
**CTA**：GitHub 搜 task-clarify-heuristic

---

## 二、英文版

### 1. Reddit r/LocalLLaMA（技术社区风）

**Title**: I built a prompt-only "task clarification" skill that stops Agents from going off-track

**Body**:

Agent platforms are powerful (Dify, WorkBuddy, OpenCode, etc.), but there's a silent productivity killer: **we hand Agents vague requests and expect them to read our minds.**

"I want to analyze our sales data" — does that mean a dashboard? An anomaly report? A strategy doc for the exec team? Most Agents will just pick one and run with it.

So I built `task-clarify-heuristic`. It doesn't execute anything — it **interrogates your request first**. Through heuristic multi-round Q&A, it converges a vague task into a structured Agent task spec, then hands it to the downstream Agent.

Three ideas that make it different:
1. **Goal vs. Means** — you say "build a PPT", it asks "is the real goal to persuade the client to buy?"
2. **Auto-guess & confirm** — when info is missing, it proposes assumptions for you to confirm/correct, instead of a blank form.
3. **Platform-agnostic** — same logic works in WorkBuddy / Dify / OpenCode. Output is a plain-text spec you can paste anywhere.

Prompt-only, zero dependencies, MIT. The repo ships:
- A typed question bank (code / content / research / design / data-analysis)
- 3 full dialogue examples
- A demo GIF showing the whole flow

GitHub: https://github.com/luoxianqiang158/task-clarify-heuristic
ModelScope: https://www.modelscope.cn/luoxianqiang/task-clarify-heuristic

Open to feedback — what would make this more useful for your Agent workflow?

---

### 2. X / Twitter（线程风）

**Post 1**:
Your Agent doesn't fail because it's dumb. It fails because your task description is vague.
I made a skill that fixes the *input*, not the model. 🧵

**Post 2**:
`task-clarify-heuristic` runs heuristic multi-round Q&A BEFORE execution:
- distinguishes Goal vs Means
- auto-guesses missing context (you just confirm)
- outputs a structured spec any Agent can consume
Works on Dify / WorkBuddy / OpenCode. Prompt-only, MIT.

**Post 3**:
Repo + demo GIF 👉 https://github.com/luoxianqiang158/task-clarify-heuristic
ModelScope mirror 👉 https://www.modelscope.cn/luoxianqiang/task-clarify-heuristic
Star if this would save you from one more wasted Agent run. ⭐

---

### 3. Product Hunt 一句话（如后续上架）

**Tagline**: A clarification layer that turns vague Agent requests into structured specs — before they go off-track.

---

## 三、发布节奏建议（冲爆款）

| 阶段 | 动作 | 时机 |
|------|------|------|
| Day 1 | GitHub 发布 + 同步 ModelScope + 站内发 README | 已做 |
| Day 1-2 | 掘金 + 知乎 + V2EX 中文帖（带 demo.gif） | 建议现在发 |
| Day 3 | Reddit r/LocalLLaMA + X 英文帖 | 错峰，覆盖海外时区 |
| Week 1 | 根据 issue/评论迭代 SKILL.md，发 v1.1.0 | 持续 |
| Week 2 | 做对比视频（有/无澄清的 Agent 输出对照） | 强化卖点 |

**钩子话术公式**：痛点（Agent 乱跑）→ 反直觉（问题在输入不在模型）→ 方案（反向澄清）→ 证据（demo.gif）→ CTA（star + 双链接）。
