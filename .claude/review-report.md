# 翻译格式审查报告（ID 08）

时间：2026-01-25 23:37

> 说明：当前 `.claude/review-request.md` 仍为 ID 09；本报告按你的指令“审查 08”，审查目标为 `anthropic-engineering-articles/markdown/08-desktop-extensions.md`。

## 综合结论
**综合评分：79/100**

- 技术维度：40/50
- 战略维度：39/50

**建议：有条件通过（建议先修再合并）**

## 技术维度评分（50分）
- 标题格式正确性：10/10
- 正文格式正确性：20/20
- 列表格式正确性：4/10
- 代码块格式正确性：1/5
- 图片链接正确性：5/5

## 战略维度评分（50分）
- 需求匹配度：14/15
- 格式规范一致性：12/20
- 翻译质量：8/10
- 可维护性：5/5

## 关键发现（问题清单）
### A. 无序列表中文行缺少 `-`（破坏列表结构，属于格式硬伤）
规范要求无序列表“保持原有的列表符号”，但多处英文为 `- ...`、中文译文变成普通段落（缺 `-`），导致渲染时中文不再作为列表项。

典型位置（仅列部分）：
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:23` / `anthropic-engineering-articles/markdown/08-desktop-extensions.md:25`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:147` / `anthropic-engineering-articles/markdown/08-desktop-extensions.md:149`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:394` / `anthropic-engineering-articles/markdown/08-desktop-extensions.md:396`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:506` / `anthropic-engineering-articles/markdown/08-desktop-extensions.md:508`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:602` / `anthropic-engineering-articles/markdown/08-desktop-extensions.md:604`

### B. 多处 `json` 代码块出现“重复键”以承载中英对照（会误导读者，且不可复制）
多段 ` ```json ` 示例把同一个字段写两次（英文值一行、中文值一行），例如 `"description"` 连续重复，这会让示例难以作为“可用配置/参考实现”使用。

典型位置（仅列部分）：
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:230`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:231`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:249`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:250`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:251`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:252`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:284`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:285`
- `anthropic-engineering-articles/markdown/08-desktop-extensions.md:528`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:529`

### C. 存在明显占位链接（需替换为真实链接）
- 文末“Submit your extension”使用 `example.com` 占位：`anthropic-engineering-articles/markdown/08-desktop-extensions.md:756`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:758`。

## 优点（做得好的地方）
- 标题层级清晰，且标题均为“英文 | 中文”：`anthropic-engineering-articles/markdown/08-desktop-extensions.md:1`、`:17`、`:47`、`:89`、`:349`、`:468`、`:542`、`:618`、`:664`、`:688`、`:742`。
- 正文段落严格按“英文段落 → 空行 → 中文段落”对照（未发现相邻中英直连）。
- 代码块边界成对闭合（未发现 fence 破坏）：如 `anthropic-engineering-articles/markdown/08-desktop-extensions.md:163`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:196`。
- 图片为原始 `www-cdn.anthropic.com` 链接且有中文说明：`anthropic-engineering-articles/markdown/08-desktop-extensions.md:752`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:754`。
- Sources 区域提供了可点击链接：`anthropic-engineering-articles/markdown/08-desktop-extensions.md:763`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:766`。

## 修改建议（按优先级）
1. 批量修复无序列表中文行：为每个中文译文行补上 `- `（保持与英文一致的列表符号），例如从 `anthropic-engineering-articles/markdown/08-desktop-extensions.md:25` 开始同类问题。
2. 重构 `json` 示例的中英对照方式：避免在 JSON 内重复键；建议做法是“保留英文原样 + 在相邻中文段落解释字段含义/示例值”，或改为 `jsonc` 并用注释写中文说明（但不要重复键）。
3. 将 `Submit your extension` 的占位 URL 替换为原文真实链接：`anthropic-engineering-articles/markdown/08-desktop-extensions.md:756`、`anthropic-engineering-articles/markdown/08-desktop-extensions.md:758`。

[CONVERSATION_ID]: 019bf489-67c1-7362-a343-d5114f763579
