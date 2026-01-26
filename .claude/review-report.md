# 翻译格式审查报告（ID06 - 修复后复审）

时间：2026-01-26 19:34  
审查目标：`anthropic-engineering-articles/markdown/06-claude-code-best-practices.md`

## 结论

**建议：通过（可以合并）**  
**综合评分：92 / 100**

本轮已补齐此前所有关键结构性问题：有序列表/无序列表的中英对照与符号规则已统一，MCP/工作流/无头模式等“步骤型内容”已补全中文对照，表格已保持单表双语对照，图片链接与中文说明也符合规范。整体已满足 `.claude/rules/translation-format.md` 的核心格式要求。

## 关键修复点（已验证）

1) **无序列表：中文行补齐 `-`，保持列表结构**
- 典型位置：`06-claude-code-best-practices.md:75-95`（CLAUDE.md 放置位置列表）  
- 典型位置：`06-claude-code-best-practices.md:460-486`（Course correct 工具列表）  
- 典型位置：`06-claude-code-best-practices.md:515-535`（Pass data 方法列表）

2) **有序列表：补齐中文翻译行，并移除中文序号（含嵌套步骤）**
- 典型位置：`06-claude-code-best-practices.md:159-167`（bash tools 的 1-3 步）  
- 典型位置：`06-claude-code-best-practices.md:224-308`（常见工作流 3a/3b/3c）  
- 典型位置：`06-claude-code-best-practices.md:573-610`（multi-Claude 6a）  
- 典型位置：`06-claude-code-best-practices.md:693-715`（无头模式 6d 的两种模式与子步骤）

3) **MCP 连接方式列表已补齐逐条中英对照**
- 证据：`06-claude-code-best-practices.md:169-181`

4) **Codebase Q&A 示例问题列表已补齐逐条中英对照**
- 证据：`06-claude-code-best-practices.md:314-360`

5) **worktrees 的 Some tips 列表已改为逐条中英对照**
- 证据：`06-claude-code-best-practices.md:683-700`

6) **图片与 Sources 规范通过**
- 图片：均为 `www-cdn.anthropic.com` 且紧随中文说明（例如 `06-claude-code-best-practices.md:113-115`）  
- Sources：已提供中英双条目（`06-claude-code-best-practices.md:767-771`）

## 可选优化（不影响显示）

1) **中文段落中的英文术语可继续统一“首次括注”策略**
- 现状：正文中仍会出现少量技术缩写/术语（如 `TDD`、`PR`、`README` 等），整体可读性已可接受。  
- 建议：若追求全仓一致性，可在首次出现处统一为“中文（英文/缩写）”。

[CONVERSATION_ID]: 019bf489-67c1-7362-a343-d5114f763579
