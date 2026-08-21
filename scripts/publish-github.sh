#!/usr/bin/env bash
# 一键发布 task-clarify-heuristic 到 GitHub
# 用法：GITHUB_TOKEN=ghp_xxx ./scripts/publish-github.sh
set -euo pipefail

TOKEN="${GITHUB_TOKEN:-}"
REPO="luoxianqiang158/task-clarify-heuristic"

if [[ -z "$TOKEN" ]]; then
  echo "❌ 请设置 GITHUB_TOKEN 环境变量（需要 repo 权限）"
  echo "获取方式：GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → 勾选 repo"
  exit 1
fi

echo "🛠  在 GitHub 创建仓库 ${REPO} ..."
curl -sS -H "Authorization: token ${TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  -d '{"name":"task-clarify-heuristic","private":false,"auto_init":false}' \
  "https://api.github.com/user/repos" | grep -E '"html_url"|"name"|"message"' | head -5

echo "🔗 设置 remote 并推送 main 分支 ..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://${TOKEN}@github.com/${REPO}.git"
git push -u origin main

echo "🏷️  设置 GitHub Topics ..."
curl -sS -X PUT -H "Authorization: token ${TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  -d '{"names":["agent-skill","prompt-engineering","llm","dify","opencode","task-clarification","agent-workflow","workbuddy","prompt-template","ai-agent"]}' \
  "https://api.github.com/repos/${REPO}/topics" | grep -E '"names"|"message"' | head -3

# 推送完成后把 remote 改回不携带 token 的地址，避免 token 留在 .git/config
git remote set-url origin "https://github.com/${REPO}.git"

echo "✅ 发布完成：https://github.com/${REPO}"
