# 发布与运营规划 · Publishing & Promotion Plan

> 目标：把 `task-clarify-heuristic` 打造成跨平台爆款 Agent Skill 仓库。
> 节奏：**先发 ModelScope（用户 luoxianqiang）→ 找回 GitHub 密码后补发 GitHub**，双平台同步 README（中/英）。

---

## 1. GitHub Topics（找回密码后设置）

在仓库页面 `Settings → Topics` 添加，或用 `gh`：

```bash
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic agent-skill
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic prompt-engineering
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic llm
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic ai-agent
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic dify
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic opencode
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic task-clarification
gh repo edit luoxianqiang/task-clarify-heuristic --add-topic requirements-engineering
```

**选取理由**：前两个是社区高频检索词（决定曝光），中间是技术栈标签（Dify/OpenCode 用户能搜到），后两个是语义长尾词（精准流量）。

---

## 2. ModelScope 标签（Tags）

ModelScope 以「模型 / 数据集 / 空间」为主，本仓库是**提示词工程 Skill**，建议以 **「数据集」形态** 发布（承载 SKILL.md + 示例 + 平台适配文件），并在描述里强调「Agent 提示词 / Prompt Skill」。推荐标签：

```
agent-skill, prompt-engineering, llm, ai-agent, task-clarification, dify, opencode, 提示词工程
```

> 注：ModelScope 的仓库标签在创建/编辑页面填写，无 CLI 批量命令，需网页操作一次。

---

## 3. GIF 演示方案（README 顶部抓眼球）

### 为什么需要
纯文本 skill 仓库很难爆。一张「**对话前（模糊任务）↔ 对话后（结构化规约）**」的动图，能在 3 秒内讲清价值，显著提升点击与 star。

### 录制工具（任选）
| 工具 | 平台 | 特点 |
|------|------|------|
| **ScreenToGif** | Windows | 免费、轻量、可直接裁剪/降帧/转 WebP，推荐 |
| LICEcap | Win/Mac | 极简，直接出 GIF |
| OBS Studio | 全平台 | 功能强，可录成 MP4/WebM（体积更小） |

### 分镜脚本（≤ 30s，1280×720）
1. **0–4s** 用户丢模糊任务：*"帮我做个智能客服"*
2. **4–12s** Skill 反问 2 个问题（业务目标？受众？）+ 主动给出假设让用户确认
3. **12–20s** 用户简短回答
4. **20–27s** 自动生成结构化任务规约（高亮 `## 业务目标 / ## 验收标准 / ## 不在范围`）
5. **27–30s** HARD GATE：*"确认无误我就开始执行"*

### 规格与放置
- 格式优先 **WebP / MP4**（GIF 体积大，README 里用 `<img>` 或视频标签）；若只能用 GIF，控制在 **< 5MB**，用 ScreenToGif 降帧到 10fps。
- 文件放 `assets/demo.gif`（或 `assets/demo.webp`），README 顶部引用：
  ```markdown
  ![demo](assets/demo.gif)
  ```

---

## 4. 双平台发布步骤

### A. ModelScope（先发）
前置：你的 **ModelScope Access Token**（获取路径：modelscope.cn → 用户中心 → 访问令牌）。

方式一（推荐，网页建仓 + 我推）：
1. 你在 ModelScope 网页新建仓库（命名 `task-clarify-heuristic`，类型选「数据集」，可见性 public）。
2. 把 Token 发我，我用一次性命令推送（token 不落盘）：
   ```bash
   cd task-clarify-heuristic
   git remote add modelscope https://luoxianqiang:<YOUR_TOKEN>@www.modelscope.cn/luoxianqiang/task-clarify-heuristic.git
   git push -u modelscope main
   ```

方式二（全自动化，需 token 调 API 建仓）：把 Token 给我，我帮你建仓 + 推送一条龙。

### B. GitHub（找回密码后）
前置：GitHub **Personal Access Token**（勾选 `repo` 权限）。

```bash
# 方式一：gh 一键建仓并推送（找回密码后先 `gh auth login`）
gh repo create luoxianqiang/task-clarify-heuristic --public --source=. --remote=origin --push

# 方式二：网页建仓 + HTTPS 推送
git remote add origin https://luoxianqiang:<YOUR_TOKEN>@github.com/luoxianqiang/task-clarify-heuristic.git
git push -u origin main
```

建仓后执行第 1 节的 Topics 命令，并上传 GIF（第 3 节）。

---

## 5. 冲爆款 Checklist
- [ ] README 三个差异化卖点置顶（手段vs目标 / 自动猜测 / 跨平台）
- [ ] Demo GIF 在 README 顶部
- [ ] GitHub Topics 设置完整
- [ ] 英文 README 就位（已含 README_EN.md）
- [ ] 在中文社区（掘金 / 知乎 / V2EX）与海外（Reddit r/LocalLLaMA、Hacker News）发安利帖
- [ ] 回复 issue / PR 及时，前两周关键期
- [ ] 加一张「跨平台适配」说明图，降低 Dify/OpenCode 用户上手成本
