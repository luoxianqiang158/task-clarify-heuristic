# 🎯 Task Clarify Heuristic

> **A task-clarification skill that stops Agents from going off-track** — uses heuristic, multi-turn questioning to turn vague requests into structured, executable agent task specs.

[![License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-Dify%20%7C%20WorkBuddy%20%7C%20OpenCode-8b5cf6)](./platforms)
[![Lang](https://img.shields.io/badge/lang-EN%20%2F%20%E4%B8%AD%E6%96%87-orange)](./README.md)
[![Type](https://img.shields.io/badge/type-agent--skill-green)](./SKILL.md)
[![GitHub](https://img.shields.io/badge/GitHub-task--clarify--heuristic-blue?logo=github)](https://github.com/luoxianqiang158/task-clarify-heuristic)
[![ModelScope](https://img.shields.io/badge/ModelScope-task--clarify--heuristic-green)](https://www.modelscope.cn/luoxianqiang/task-clarify-heuristic)

<p align="center">
  <img src="./assets/demo.gif" alt="Task Clarify Heuristic Demo" width="560"/>
</p>

> One line: **Most prompts teach you how to instruct an Agent. This skill helps you turn a vague request into a clear instruction first.**

---

## 📌 The Problem

You tell an Agent "write me a competitor analysis", "add an export feature", or "analyze this market" — and often:

- The Agent jumps straight in and produces something generic and off-target
- You go through 3 rounds of revisions, both frustrated
- Eventually you realize "that's not even what I wanted"

**Root cause: 90% of drift is not the Agent being dumb — it's the task definition missing goals, boundaries, and acceptance criteria.**

## ✨ Core Features (rare in the wild)

| # | Feature | Why it matters |
|---|---------|----------------|
| 1 | **Distinguish means from business goals** | User says "make a PPT" → real goal may be "persuade the client to buy". Wrong goal = wasted effort. |
| 2 | **Auto-fill assumptions** | When info is missing, propose an assumption for confirmation instead of throwing all questions back — less burden on the user. |
| 3 | **Platform-agnostic** | Output is a plain-text task spec, copy-pasteable to Dify / OpenCode / any Agent. Not locked to one platform. |
| 4 | **≤ 2 questions per round** | No big surveys → no lazy answers. |
| 5 | **Complexity pre-check** | Trivial tasks skip ahead; complex ones dig deep. No wasted turns. |

## 🖼️ Workflow

![Task Clarify Heuristic workflow](./assets/demo-flow.svg)

## 🚀 Quick Start

**WorkBuddy users** (easiest): drop `SKILL.md` into your skills directory and it auto-triggers on vague tasks:

```bash
cp SKILL.md ~/.workbuddy/skills/task-clarify-heuristic/SKILL.md
```

**Dify / OpenCode / others**: see [`platforms/`](./platforms/) for three adapted versions — copy and use.

## 📦 Install

### WorkBuddy
1. Copy [`SKILL.md`](./SKILL.md) to `~/.workbuddy/skills/task-clarify-heuristic/`
2. The skill auto-triggers when your request is vague

### Other platforms (Dify / OpenCode / pure prompt)
| Platform | File | Usage |
|----------|------|-------|
| Pure prompt | [`platforms/pure-prompt.md`](./platforms/pure-prompt.md) | Paste whole file as System Prompt |
| Dify | [`platforms/dify-prompt.md`](./platforms/dify-prompt.md) | Use as a "clarification node"; output `task_spec` variable |
| OpenCode | [`platforms/opencode-system.md`](./platforms/opencode-system.md) | Append to system_prompt; clarify before coding |

## 📂 Structure

```
task-clarify-heuristic/
├── SKILL.md                 # WorkBuddy version (core + platform hooks)
├── README.md                # Chinese docs
├── README_EN.md             # This file
├── LICENSE                  # MIT
├── assets/
│   └── demo-flow.svg        # Workflow diagram
├── platforms/               # Cross-platform adapters
│   ├── pure-prompt.md       # Zero-dependency plain prompt
│   ├── dify-prompt.md       # Dify adapter
│   └── opencode-system.md   # OpenCode adapter
└── examples/                # Full conversation examples
    ├── code-task.md         # coding task
    ├── content-task.md      # content-creation task
    └── research-task.md     # research task
```

## 💡 Example

**Before (no clarification)**
> User: "Write me a competitor analysis."
> Agent writes a generic "three big players" piece — no business angle, useless to you.

**After (via this skill)**
```text
# Agent Task Spec [confirmed]
## Business Goal: decide build-vs-buy OCR, support Q4选型 decision
## Audience: tech VP + procurement director
## Acceptance: clear recommendation + cost/capability comparison table
## Out of Scope: no POC, no RFP
## Input: existing vendor list (web search allowed)
## Output: Markdown report with TCO estimate
## Tools: allowed
```

More cross-type conversations in [`examples/`](./examples/):
- [`code-task.md`](./examples/code-task.md) — "add an export feature"
- [`content-task.md`](./examples/content-task.md) — "write a WeChat post"
- [`research-task.md`](./examples/research-task.md) — "analyze this market"

## ❓ FAQ

**Q: How is this different from a "ask before answering" prompt?**
A: Ordinary prompts just "ask more". This skill has staged phases (intent → constraints → spec), complexity pre-check, means/goal separation, assumption auto-fill, and produces a **structured, reusable spec** — not scattered Q&A.

**Q: Really only 2 questions per round?**
A: At most 2, to avoid survey fatigue. Related questions may merge, but never exceed 2. It's a UX design, not an arbitrary limit.

**Q: Does it execute after clarifying?**
A: No. A HARD GATE requires the user to **explicitly confirm** the spec before any execution.

## 🤝 Contributing

Issues / PRs welcome: more task-type question banks, more platform adapters, more examples. Be friendly and on-topic.

## 📄 License

[MIT](./LICENSE) © 2026 老罗 (Luo)
