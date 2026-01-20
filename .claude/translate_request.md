# Claude Code CHANGELOG 翻译请求

## 任务说明

请将以下 Claude Code CHANGELOG 版本内容翻译成简体中文，并按照指定的双语对照格式输出。

## 翻译规范

### 1. 双语对照格式
每个变更条目必须遵循以下格式：
```markdown
- English original text
简体中文翻译文本
```
注意：英文和中文之间**没有空行**，中文翻译紧接在英文下一行。

### 2. 术语一致性
请严格遵循以下术语对照表：

| 英文 | 中文 |
|------|------|
| skill | 技能 |
| slash command | 斜杠命令 |
| hook | hook |
| agent | 代理 |
| subagent / sub-agent | 子代理 |
| permission | 权限 |
| token | 令牌 |
| context window | 上下文窗口 |
| plugin | 插件 |
| marketplace | 市场/市场place |
| MCP | MCP |
| OAuth | OAuth |
| SDK | SDK |
| API | API |
| CLI | CLI |
| IDE | IDE |
| LSP | LSP |
| frontmatter | frontmatter |
| hot-reload | 热重载 |
| background task | 后台任务 |
| environment variable | 环境变量 |
| flag | 标志 |
| wildcard pattern | 通配符模式 |
| injection vulnerability | 注入漏洞 |
| command injection | 命令注入 |
| memory leak | 内存泄漏 |
| tree-sitter | tree-sitter |
| inode | inode |
| fuzzy matching | 模糊匹配 |
| autocomplete | 自动完成 |
| status line | 状态栏 |
| spinner | 加载指示器 |
| compaction | 压缩 |

### 3. 动词翻译
- Added → 添加了
- Fixed → 修复了
- Improved → 改进了/改善了
- Changed → 更改了
- Removed → 移除了
- Deprecated → 弃用了
- Updated → 更新了
- Reduced → 减少了
- Increased → 增加了
- Enhanced → 增强了
- Optimized → 优化了
- Merged → 合并了
- Introduced → 引入了
- Enabled → 启用了
- Disabled → 禁用了

### 4. 特殊格式处理规则

**代码和命令示例：**
- 保留代码块中的英文，不翻译代码
- 例如：`Bash(npm *)` 保持原样

**键盘快捷键：**
- 保持快捷键格式，仅翻译动作词
- 例如：Press Ctrl+V to paste → 按 Ctrl+V 粘贴

**配置项名称：**
- 保留配置项名称原文，翻译描述部分
- 例如：Added `IS_DEMO` environment variable → 添加了 `IS_DEMO` 环境变量

**专有名词：**
- 保留产品名原文
- Claude Code、Claude Code Desktop、iTerm2、WezTerm、Ghostty、Kitty、Bedrock、Vertex AI 等保持原文

### 5. 翻译质量要求
- 语句通顺，符合中文表达习惯
- 技术准确性，不改变技术含义
- 保持格式完整（代码、链接等保持原样）
- 确保每个英文条目都有对应的中文翻译

---

## 待翻译内容

### 版本 2.1.6

- Added search functionality to `/config` command for quickly filtering settings
- Added Updates section to `/doctor` showing auto-update channel and available npm versions (stable/latest)
- Added date range filtering to `/stats` command - press `r` to cycle between Last 7 days, Last 30 days, and All time
- Added automatic discovery of skills from nested `.claude/skills` directories when working with files in subdirectories
- Added `context_window.used_percentage` and `context_window.remaining_percentage` fields to status line input for easier context window display
- Added an error display when the editor fails during Ctrl+G
- Fixed permission bypass via shell line continuation that could allow blocked commands to execute
- Fixed false "File has been unexpectedly modified" errors when file watchers touch files without changing content
- Fixed text styling (bold, colors) getting progressively misaligned in multi-line responses
- Fixed the feedback panel closing unexpectedly when typing 'n' in the description field
- Fixed rate limit warning appearing at low usage after weekly reset (now requires 70% usage)
- Fixed rate limit options menu incorrectly auto-opening when resuming a previous session
- Fixed numpad keys outputting escape sequences instead of characters in Kitty keyboard protocol terminals
- Fixed Option+Return not inserting newlines in Kitty keyboard protocol terminals
- Fixed corrupted config backup files accumulating in the home directory (now only one backup is created per config file)
- Fixed `mcp list` and `mcp get` commands leaving orphaned MCP server processes
- Fixed visual artifacts in ink2 mode when nodes become hidden via `display:none`
- Improved the external CLAUDE.md imports approval dialog to show which files are being imported and from where
- Improved the `/tasks` dialog to go directly to task details when there's only one background task running
- Improved @ autocomplete with icons for different suggestion types and single-line formatting
- Updated "Help improve Claude" setting fetch to refresh OAuth and retry when it fails due to a stale OAuth token
- Changed task notification display to cap at 3 lines with overflow summary when multiple background tasks complete simultaneously
- Changed terminal title to "Claude Code" on startup for better window identification
- Removed ability to @-mention MCP servers to enable/disable - use `/mcp enable <name>` instead
- [VSCode] Fixed usage indicator not updating after manual compact

### 版本 2.1.5

- Added `CLAUDE_CODE_TMPDIR` environment variable to override the temp directory used for internal temp files, useful for environments with custom temp directory requirements

### 版本 2.1.4

- Added `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to disable all background task functionality including auto-backgrounding and the Ctrl+B shortcut
- Fixed "Help improve Claude" setting fetch to refresh OAuth and retry when it fails due to a stale OAuth token

### 版本 2.1.3

- Merged slash commands and skills, simplifying the mental model with no change in behavior
- Added release channel (`stable` or `latest`) toggle to `/config`
- Added detection and warnings for unreachable permission rules, with warnings in `/doctor` and after saving rules that include the source of each rule and actionable fix guidance
- Fixed plan files persisting across `/clear` commands, now ensuring a fresh plan file is used after clearing a conversation
- Fixed false skill duplicate detection on filesystems with large inodes (e.g., ExFAT) by using 64-bit precision for inode values
- Fixed mismatch between background task count in status bar and items shown in tasks dialog
- Fixed sub-agents using the wrong model during conversation compaction
- Fixed web search in sub-agents using incorrect model
- Fixed trust dialog acceptance when running from the home directory not enabling trust-requiring features like hooks during the session
- Improved terminal rendering stability by preventing uncontrolled writes from corrupting cursor state
- Improved slash command suggestion readability by truncating long descriptions to 2 lines
- Changed tool hook execution timeout from 60 seconds to 10 minutes
- [VSCode] Added clickable destination selector for permission requests, allowing you to choose where settings are saved (this project, all projects, shared with team, or session only)

### 版本 2.1.2

- Added source path metadata to images dragged onto the terminal, helping Claude understand where images originated
- Added clickable hyperlinks for file paths in tool output in terminals that support OSC 8 (like iTerm)
- Added support for Windows Package Manager (winget) installations with automatic detection and update instructions
- Added Shift+Tab keyboard shortcut in plan mode to quickly select "auto-accept edits" option
- Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate even when the main auto-updater is disabled
- Added `agent_type` to SessionStart hook input, populated if `--agent` is specified
- Fixed a command injection vulnerability in bash command processing where malformed input could execute arbitrary commands
- Fixed a memory leak where tree-sitter parse trees were not being freed, causing WASM memory to grow unbounded over long sessions
- Fixed binary files (images, PDFs, etc.) being accidentally included in memory when using `@include` directives in CLAUDE.md files
- Fixed updates incorrectly claiming another installation is in progress
- Fixed crash when socket files exist in watched directories (defense-in-depth for EOPNOTSUPP errors)
- Fixed remote session URL and teleport being broken when using `/tasks` command
- Fixed MCP tool names being exposed in analytics events by sanitizing user-specific server configurations
- Improved Option-as-Meta hint on macOS to show terminal-specific instructions for native CSIu terminals like iTerm2, Kitty, and WezTerm
- Improved error message when pasting images over SSH to suggest using `scp` instead of the unhelpful clipboard shortcut hint
- Improved permission explainer to not flag routine dev workflows (git fetch/rebase, npm install, tests, PRs) as medium risk
- Changed large bash command outputs to be saved to disk instead of truncated, allowing Claude to read the full content
- Changed large tool outputs to be persisted to disk instead of truncated, providing full output access via file references
- Changed `/plugins` installed tab to unify plugins and MCPs with scope-based grouping
- Deprecated Windows managed settings path `C:\ProgramData\ClaudeCode\managed-settings.json` - administrators should migrate to `C:\Program Files\ClaudeCode\managed-settings.json`
- [SDK] Changed minimum zod peer dependency to ^4.0.0
- [VSCode] Fixed usage display not updating after manual compact

---

## 输出要求

请按照上述双语对照格式输出翻译结果，确保：
1. 每个版本标题格式为 `## X.Y.Z`
2. 版本标题后空一行
3. 每个条目格式为 `- 英文\n中文`（无空行）
4. 条目之间空一行
5. 严格按照术语表进行翻译
6. 保持代码、命令、配置项的原始格式

输出应该可以直接插入到双语对照文件的顶部。
