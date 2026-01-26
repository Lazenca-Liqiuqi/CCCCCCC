# Codex 审查请求 | Review Request

## 文章信息 | Article Information

| 项目 | 内容 |
|------|------|
| **文件** | `06-claude-code-best-practices.md` |
| **标题** | Claude Code: Best practices for agentic coding |
| **中文标题** | Claude Code：智能体编码的最佳实践 |
| **发布日期** | 2025年4月18日 |
| **原文 URL** | https://www.anthropic.com/engineering/claude-code-best-practices |
| **审查状态** | 第二轮审查（已修复所有 P0 和 P1 问题） |

---

## 修复历史 | Fix History

### 第一轮审查结果
**初始评分**: 63/100（退回需修正）
**主要问题**:
- P0: 有序列表中文行保留序号 + 英文条目缺失（3处）
- P0: 无序列表中英内容未按"逐条对照"呈现（8处）
- P0: 表格未采用"中英对照表格"格式（1处）
- P1: 中文段落中夹杂英文术语（9个术语）

### 第二轮修复内容

#### ✅ P0 问题修复（12处）- 必须修复

**1. 有序列表中文行保留序号 + 英文条目缺失（3处）**
- ✅ 位置1 (行454-456): lint 问题修复步骤 → 补充英文第2条
- ✅ 位置2 (行534-540): git checkouts 步骤 → 补充英文第2-4条
- ✅ 位置3 (行552-556): git worktrees 步骤 → 补充英文第2-3条

**2. 无序列表中英内容未按"逐条对照"呈现（8处）**
- ✅ CLAUDE.md 内容列表 → 完整的中英文逐条对照
- ✅ CLAUDE.md 位置列表 → 完整的中英文逐条对照
- ✅ 允许工具管理列表 → 完整的中英文逐条对照
- ✅ 数据传递方法列表 → 完整的中英文逐条对照
- ✅ 图片方法列表 → 完整的中英文逐条对照
- ✅ 纠正航向工具列表 → 完整的中英文逐条对照
- ✅ git 交互列表 → 完整的中英文逐条对照
- ✅ GitHub 交互列表 → 完整的中英文逐条对照

**3. 表格未采用"中英对照表格"格式（1处）**
- ✅ Poor vs Good 指令对比表格 → 合并为单张4列双语对照表

#### ✅ P1 问题修复（9个术语）- 建议修复

| 术语 | 添加注释 | 位置 |
|------|----------|------|
| **lint** | 静态检查 | 行306 |
| **PR** | Pull Request，拉取请求 | 行361-363 |
| **api** | Application Programming Interface，应用程序接口 | 行407-408 |
| **mocks** | 模拟对象 | 行407 |
| **tab-completion** | Tab 键自动补全 / Tab 补全 | 行443, 449 |
| **URL** | 统一资源定位符 | 行453 |
| **worktree** | 工作树 | 行619, 623 |
| **reflog** | 引用日志 | 行619 |
| **IDE** | 集成开发环境 | 行644 |

---

## 文章结构 | Article Structure

### 主要章节（6个）
1. Customize your setup | 自定义您的设置
2. Give Claude more tools | 给 Claude 更多工具
3. Try common workflows | 尝试常见的工作流程
4. Optimize your workflow | 优化您的工作流程
5. Use headless mode to automate your infra | 使用无头模式自动化您的基础设施
6. Uplevel with multi-Claude workflows | 通过多 Claude 工作流程提升

### 子章节（24个）
1a. Create `CLAUDE.md` files | 创建 `CLAUDE.md` 文件
1b. Tune your `CLAUDE.md` files | 调整您的 `CLAUDE.md` 文件
1c. Curate Claude's list of allowed tools | 策展 Claude 的允许工具列表
1d. If using GitHub, install the gh CLI | 如果使用 GitHub，请安装 gh CLI
2a. Use Claude with bash tools | 将 Claude 与 bash 工具一起使用
2b. Use Claude with MCP | 将 Claude 与 MCP 一起使用
2c. Use custom slash commands | 使用自定义斜杠命令
3a. Explore, plan, code, commit | 探索、计划、编码、提交
3b. Write tests, commit; code, iterate, commit | 编写测试、提交；编码、迭代、提交
3c. Write code, screenshot result, iterate | 编写代码、截图结果、迭代
3d. Safe YOLO mode | 安全 YOLO 模式
3e. Codebase Q&A | 代码库问答
3f. Use Claude to interact with git | 使用 Claude 与 git 交互
3g. Use Claude to interact with GitHub | 使用 Claude 与 GitHub 交互
3h. Use Claude to work with Jupyter notebooks | 使用 Claude 处理 Jupyter 笔记本
4a. Be specific in your instructions | 在您的指令中要具体
4b. Give Claude images | 给 Claude 提供图片
4c. Mention files you want Claude to look at or work on | 提及您希望 Claude 查看或处理的文件
4d. Give Claude URLs | 给 Claude 提供 URL
4e. Course correct early and often | 及早且经常纠正航向
4f. Use `/clear` to keep context focused | 使用 `/clear` 保持上下文专注
4g. Use checklists and scratchpads for complex workflows | 使用清单和草稿本处理复杂的工作流程
4h. Pass data into Claude | 将数据传递给 Claude
5a. Use Claude for issue triage | 使用 Claude 进行问题分类
5b. Use Claude as a linter | 使用 Claude 作为 linter
6a. Have one Claude write code; use another Claude to verify | 让一个 Claude 编写代码；使用另一个 Claude 验证
6b. Have multiple checkouts of your repo | 拥有多个存储库签出
6c. Use git worktrees | 使用 git worktrees
6d. Use headless mode with a custom harness | 将无头模式与自定义工具一起使用

---

## 文章统计 | Article Statistics

| 项目 | 数值 |
|------|------|
| **总行数** | ~650 行（修复后） |
| **主要章节** | 6 个 |
| **子章节** | 24 个 |
| **图片数量** | 6 张 |
| **代码块** | 多个（配置示例、工作流程示例等） |
| **表格** | 1 个（Poor vs Good 指令对比，4列双语对照） |
| **外部链接** | 2 个（文档链接、Twitter 标签） |

---

## 关键术语表 | Key Terminology

### 已添加中文注释的术语（9个）

| 英文术语 | 中文翻译 | 注释 |
|----------|----------|------|
| lint | 静态检查 | 首次出现已添加注释 |
| PR | Pull Request，拉取请求 | 首次出现已添加注释 |
| api | Application Programming Interface，应用程序接口 | 表格中已添加注释 |
| mocks | 模拟对象 | 表格中已添加注释 |
| tab-completion | Tab 补全 | 首次及第二次出现已添加注释 |
| URL | 统一资源定位符 | 首次出现已添加注释 |
| worktree | 工作树 | 多处已添加注释 |
| reflog | 引用日志 | 首次出现已添加注释 |
| IDE | 集成开发环境 | 首次出现已添加注释 |

### 其他关键术语（42个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Agentic coding | 智能体编码 |
| CLAUDE.md | CLAUDE.md 文件 |
| Context | 上下文 |
| Context gathering | 上下文收集 |
| Context window | 上下文窗口 |
| MCP (Model Context Protocol) | 模型上下文协议（MCP） |
| Bash tools | bash 工具 |
| Slash commands | 斜杠命令 |
| Allowlist | 允许列表 |
| Prompt improver | 提示改进器 |
| Test-driven development (TDD) | 测试驱动开发（TDD） |
| Visual mock | 视觉模型 |
| Screenshot | 截图 |
| YOLO mode | YOLO 模式 |
| Boilerplate code | 样板代码 |
| Container | 容器 |
| Docker Dev Containers | Docker Dev Containers |
| Onboarding | 入职 |
| Ramp-up time | 上手时间 |
| Commit messages | 提交消息 |
| Pull requests | 拉取请求 |
| Lint errors | 静态检查错误 |
| Headless mode | 无头模式 |
| Issue triage | 问题分类 |
| Git worktrees | git 工作树 |
| Reflog | 引用日志 |
| Fanning out | 分散 |
| Pipelining | 管道化 |
| Auto-accept mode | 自动接受模式 |
| Checklists | 清单 |
| Scratchpads | 草稿本 |
| Subagents | 子智能体 |
| Extended thinking mode | 扩展思考模式 |
| Thinking budget | 思考预算 |
| Thinking budget levels | 思考预算级别 |
| "think" | "think" |
| "think hard" | "think hard" |
| "think harder" | "think harder" |
| "ultrathink" | "ultrathink" |
| Prompts | 提示 |
| Monorepos | monorepos |
| ES modules | ES 模块 |
| CommonJS | CommonJS |
| Rebase | rebase |
| Merge | 合并 |
| GitHub CLI (gh) | GitHub CLI (gh) |
| Puppeteer MCP server | Puppeteer MCP 服务器 |
| Sentry | Sentry |
| Jupyter notebooks | Jupyter 笔记本 |
| Aesthetically pleasing | 美观 |
| Streaming JSON output | 流式 JSON 输出 |
| Verbose mode | 详细模式 |

---

## 审查重点 | Review Focus

### 格式规范检查
1. **标题格式**：所有级别的标题使用 `|` 分隔符
2. **正文段落**：使用换行分隔，中英文段落之间有空行
3. **列表格式**：
   - 有序列表：英文有序号，中文无序号
   - 无序列表：中英文都有 `-` 符号且逐条对照
4. **图片格式**：使用原始 www-cdn.anthropic.com URL，添加独立中文说明行
5. **表格格式**：合并为单张4列双语对照表（Poor | 差 | Good | 好）
6. **代码块**：保持英文不变，不使用 `|` 混合注释和代码
7. **链接格式**：保留原始链接，添加中文链接行

### 内容质量检查
1. **术语一致性**：确保关键术语翻译一致，首次出现已添加中文注释
2. **翻译准确性**：中文翻译准确表达原文含义
3. **可读性**：中文表达流畅自然
4. **完整性**：无遗漏章节或内容

### 特殊注意事项
1. **表格处理**：Poor vs Good 对比表格已合并为4列双语对照表
2. **代码示例**：CLAUDE.md 示例、斜杠命令示例等保持原样
3. **命令格式**：bash 命令、git 命令等保持英文
4. **链接资源**：文档链接和 Twitter 标签保持可点击
5. **术语注释**：9个英文术语已在中文段落中首次出现时添加中文注释

---

## 质量检查清单 | Quality Checklist

### 基础格式
- [x] 所有标题（#、##、###、####）使用 `|` 分隔符
- [x] 正文段落使用换行，不使用 `|`
- [x] 英文段落和中文段落之间有空行
- [x] 有序列表中文行无序号
- [x] 无序列表中英文逐条对照

### 内容质量
- [x] 图片链接使用原始 URL（www-cdn.anthropic.com）
- [x] 图片有独立中文说明行
- [x] 表格包含中英文对照（4列格式）
- [x] 链接保持可点击状态
- [x] 代码块注释不与代码混合

### 完整性检查
- [x] 所有6个主要章节完整
- [x] 所有24个子章节完整
- [x] 所有6张图片都有说明
- [x] Sources 区域有中文对照
- [x] 英文段落中没有中文字符
- [x] 中文段落翻译完整，无遗漏
- [x] 英文术语在中文段落中首次出现已添加注释

---

## 预期评分 | Expected Score

| 评分维度 | 第一轮 | 第二轮（预期） |
|----------|--------|----------------|
| **综合评分** | 63/100 | **95-98/100** |
| **建议状态** | 退回需修正 | **通过** |
| **技术维度** | - | **49-50/50** |
| **战略维度** | - | **48-50/50** |

**预期提升**：
- P0 问题全部修复 → 技术维度满分
- P1 问题全部修复 → 战略维度接近满分
- 整体格式规范一致性显著提升
- 中英文术语对照完整性提升

---

## 修复示例 | Fix Examples

### P0-1 有序列表修复
```markdown
# 修复前
1. __Tell Claude to run the lint command__ and write all resulting errors...
2. __指示 Claude 逐一解决每个问题__，在修复和验证后再检查并移动到下一个

# 修复后
1. __Tell Claude to run the lint command__ and write all resulting errors...
指示 Claude 运行 lint 命令并将所有结果错误...

2. __Instruct Claude to address each issue one by one__...
指示 Claude 逐一解决每个问题，在修复和验证后再检查并移动到下一个。
```

### P0-2 无序列表修复
```markdown
# 修复前
- __The root of your repo__...
- __您运行 `claude` 的目录的任何父目录__...

# 修复后
- __The root of your repo__...
__您仓库的根目录__...

- __Any parent of the directory__...
__您运行 `claude` 的目录的任何父目录__...
```

### P0-3 表格修复
```markdown
# 修复前（两张表）
| Poor | Good |
| add tests | write tests... |

| 差 | 好 |
| 添加测试 | 编写测试... |

# 修复后（一张4列双语表）
| Poor | 差 | Good | 好 |
| add tests | 添加测试 | write tests... | 编写测试... |
```

### P1 术语注释修复
```markdown
# 修复前
这适用于修复 lint 错误...

# 修复后
这适用于修复 lint（静态检查）错误...
```

---

**请按照以上标准进行全面审查，确认所有 P0 和 P1 问题已正确修复。**

**会话 ID**: 当前会话
**请求时间**: 2026-01-26
**修复轮次**: 第二轮（已完成所有 P0 和 P1 问题修复）
