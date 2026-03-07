# Claude Code 更新日志 - 双语对照

## 2.1.63

- Added `/simplify` and `/batch` bundled slash commands
添加了 `/simplify` 和 `/batch` 打包斜杠命令

- Fixed local slash command output like /cost appearing as user-sent messages instead of system messages in the UI
修复了本地斜杠命令输出（如 /cost）在 UI 中显示为用户发送的消息而非系统消息的问题

- Project configs & auto memory now shared across git worktrees of the same repository
项目配置和自动内存现在在同一仓库的 git 工作树之间共享

- Added `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var to opt out from making claude.ai MCP servers available
添加了 `ENABLE_CLAUDEAI_MCP_SERVERS=false` 环境变量以选择退出 claude.ai MCP 服务器的可用性

- Improved `/model` command to show the currently active model in the slash command menu
改进了 `/model` 命令，在斜杠命令菜单中显示当前活动的模型

- Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running a shell command
添加了 HTTP 钩子，可以 POST JSON 到 URL 并接收 JSON，而不是运行 shell 命令

- Fixed listener leak in bridge polling loop
修复了桥接轮询循环中的监听器泄漏

- Fixed listener leak in MCP OAuth flow cleanup
修复了 MCP OAuth 流程清理中的监听器泄漏

- Added manual URL paste fallback during MCP OAuth authentication. If the automatic localhost redirect doesn't work, you can paste the callback URL to complete authentication.
在 MCP OAuth 认证期间添加了手动 URL 粘贴回退。如果自动 localhost 重定向不起作用，您可以粘贴回调 URL 来完成认证。

- Fixed memory leak when navigating hooks configuration menu
修复了导航钩子配置菜单时的内存泄漏

- Fixed listener leak in interactive permission handler during auto-approvals
修复了自动批准期间交互式权限处理程序中的监听器泄漏

- Fixed file count cache ignoring glob ignore patterns
修复了文件计数缓存忽略 glob ignore 模式的问题

- Fixed memory leak in bash command prefix cache
修复了 bash 命令前缀缓存中的内存泄漏

- Fixed MCP tool/resource cache leak on server reconnect
修复了服务器重新连接时 MCP 工具/资源缓存泄漏

- Fixed IDE host IP detection cache incorrectly sharing results across ports
修复了 IDE 主机 IP 检测缓存错误地在端口间共享结果的问题

- Fixed WebSocket listener leak on transport reconnect
修复了传输重新连接时 WebSocket 监听器泄漏

- Fixed memory leak in git root detection cache that could cause unbounded growth in long-running sessions
修复了 git 根目录检测缓存中的内存泄漏，可能导致长时间运行的会话中内存无限增长

- Fixed memory leak in JSON parsing cache that grew unbounded over long sessions
修复了 JSON 解析缓存中的内存泄漏，该缓存在长时间会话中无限增长

- VSCode: Fixed remote sessions not appearing in conversation history
VSCode：修复了远程会话未出现在对话历史中的问题

- Fixed a race condition in the REPL bridge where new messages could arrive at the server interleaved with historical messages during the initial connection flush, causing message ordering issues.
修复了 REPL 桥接中的竞态条件，即新消息可能在初始连接刷新期间与历史消息交错到达服务器，导致消息排序问题。

- Fixed memory leak where long-running teammates retained all messages in AppState even after conversation compaction
修复了长时间运行的队友在 AppState 中保留所有消息的内存泄漏，即使在对对话压缩后也是如此

- Fixed a memory leak where MCP server fetch caches were not cleared on disconnect, causing growing memory usage with servers that reconnect frequently
修复了 MCP 服务器获取缓存在断开连接时未清除的内存泄漏，导致频繁重新连接的服务器内存使用量增长

- Improved memory usage in long sessions with subagents by stripping heavy progress message payloads during context compaction
通过在上下文压缩期间剥离重型进度消息负载，改进了具有子代理的长时间会话的内存使用

- Added "Always copy full response" option to the `/copy` picker. When selected, future `/copy` commands will skip the code block picker and copy the full response directly.
在 `/copy` 选择器中添加了"始终复制完整响应"选项。选中后，未来的 `/copy` 命令将跳过代码块选择器并直接复制完整响应。

- VSCode: Added session rename and remove actions to the sessions list
VSCode：在会话列表中添加了会话重命名和删除操作

- Fixed `/clear` not resetting cached skills, which could cause stale skill content to persist in the new conversation
修复了 `/clear` 不重置缓存技能的问题，这可能导致过时的技能内容在新对话中持续存在

## 2.1.62

- Fixed prompt suggestion cache regression that reduced cache hit rates
修复了导致缓存命中率下降的提示建议缓存回归问题

## 2.1.61

- Fixed concurrent writes corrupting config file on Windows
修复了 Windows 上并发写入损坏配置文件的问题

## 2.1.59

- Claude automatically saves useful context to auto-memory. Manage with /memory
Claude 自动将有用的上下文保存到自动内存。使用 /memory 管理

- Added `/copy` command to show an interactive picker when code blocks are present, allowing selection of individual code blocks or the full response.
添加了 `/copy` 命令，当代码块存在时显示交互式选择器，允许选择单个代码块或完整响应。

- Improved "always allow" prefix suggestions for compound bash commands (e.g. `cd /tmp && git fetch && git push`) to compute smarter per-subcommand prefixes instead of treating the whole command as one
改进了复合 bash 命令（例如 `cd /tmp && git fetch && git push`）的"始终允许"前缀建议，计算更智能的每子命令前缀，而不是将整个命令视为一个

- Improved ordering of short task lists
改进了短任务列表的排序

- Improved memory usage in multi-agent sessions by releasing completed subagent task state
通过释放已完成的子代理任务状态，改进了多代理会话的内存使用

- Fixed MCP OAuth token refresh race condition when running multiple Claude Code instances simultaneously
修复了同时运行多个 Claude Code 实例时 MCP OAuth 令牌刷新竞态条件

- Fixed shell commands not showing a clear error message when the working directory has been deleted
修复了当工作目录被删除时 shell 命令不显示清晰错误消息的问题

- Fixed config file corruption that could wipe authentication when multiple Claude Code instances ran simultaneously
修复了多个 Claude Code 实例同时运行时可能清除认证的配置文件损坏问题

## 2.1.58

- Expand Remote Control to more users
将远程控制扩展到更多用户

## 2.1.56

- VS Code: Fixed another cause of "command 'claude-vscode.editor.openLast' not found" crashes
VS Code：修复了"command 'claude-vscode.editor.openLast' not found"崩溃的另一个原因

## 2.1.55

- Fixed BashTool failing on Windows with EINVAL error
修复了 BashTool 在 Windows 上因 EINVAL 错误失败的问题

## 2.1.53

- Fixed a UI flicker where user input would briefly disappear after submission before the message rendered
修复了 UI 闪烁问题，用户输入在提交后消息渲染前会短暂消失

- Fixed bulk agent kill (ctrl+f) to send a single aggregate notification instead of one per agent, and to properly clear the command queue
修复了批量代理终止（ctrl+f），发送单个聚合通知而不是每个代理一个，并正确清除命令队列

- Fixed graceful shutdown sometimes leaving stale sessions when using Remote Control by parallelizing teardown network calls
通过并行化拆除网络调用，修复了使用远程控制时优雅关闭有时会留下过期会话的问题

- Fixed `--worktree` sometimes being ignored on first launch
修复了 `--worktree` 有时在首次启动时被忽略的问题

- Fixed a panic ("switch on corrupted value") on Windows
修复了 Windows 上的崩溃（"switch on corrupted value"）

- Fixed a crash that could occur when spawning many processes on Windows
修复了在 Windows 上生成许多进程时可能发生的崩溃

- Fixed a crash in the WebAssembly interpreter on Linux x64 & Windows x64
修复了 Linux x64 和 Windows x64 上 WebAssembly 解释器中的崩溃

- Fixed a crash that sometimes occurred after 2 minutes on Windows ARM64
修复了 Windows ARM64 上有时在 2 分钟后发生的崩溃

## 2.1.52

- VS Code: Fixed extension crash on Windows ("command 'claude-vscode.editor.openLast' not found")
VS Code：修复了 Windows 上的扩展崩溃（"command 'claude-vscode.editor.openLast' not found"）

## 2.1.51

- Added `claude remote-control` subcommand for external builds, enabling local environment serving for all users.
为外部构建添加了 `claude remote-control` 子命令，为所有用户启用本地环境服务。

- Updated plugin marketplace default git timeout from 30s to 120s and added `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` to configure.
将插件市场默认 git 超时从 30 秒更新为 120 秒，并添加了 `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` 进行配置。

- Added support for custom npm registries and specific version pinning when installing plugins from npm sources
添加了对自定义 npm 注册表和从 npm 源安装插件时特定版本固定的支持

- BashTool now skips login shell (`-l` flag) by default when a shell snapshot is available, improving command execution performance. Previously this required setting `CLAUDE_BASH_NO_LOGIN=true`.
BashTool 现在在 shell 快照可用时默认跳过登录 shell（`-l` 标志），提高命令执行性能。以前这需要设置 `CLAUDE_BASH_NO_LOGIN=true`。

- Fixed a security issue where `statusLine` and `fileSuggestion` hook commands could execute without workspace trust acceptance in interactive mode.
修复了一个安全问题，即 `statusLine` 和 `fileSuggestion` 钩子命令可以在交互模式下未经工作区信任接受而执行。

- Tool results larger than 50K characters are now persisted to disk (previously 100K). This reduces context window usage and improves conversation longevity.
大于 50K 字符的工具结果现在持久化到磁盘（以前是 100K）。这减少了上下文窗口使用并提高了对话持久性。

- Fixed a bug where duplicate `control_response` messages (e.g. from WebSocket reconnects) could cause API 400 errors by pushing duplicate assistant messages into the conversation.
修复了一个错误，即重复的 `control_response` 消息（例如来自 WebSocket 重新连接）可能通过将重复的助手消息推入对话而导致 API 400 错误。

- Added `CLAUDE_CODE_ACCOUNT_UUID`, `CLAUDE_CODE_USER_EMAIL`, and `CLAUDE_CODE_ORGANIZATION_UUID` environment variables for SDK callers to provide account info synchronously, eliminating a race condition where early telemetry events lacked account metadata.
添加了 `CLAUDE_CODE_ACCOUNT_UUID`、`CLAUDE_CODE_USER_EMAIL` 和 `CLAUDE_CODE_ORGANIZATION_UUID` 环境变量，供 SDK 调用者同步提供账户信息，消除了早期遥测事件缺少账户元数据的竞态条件。

- Fixed slash command autocomplete crashing when a plugin's SKILL.md description is a YAML array or other non-string type
修复了当插件的 SKILL.md 描述是 YAML 数组或其他非字符串类型时斜杠命令自动完成崩溃的问题

- The `/model` picker now shows human-readable labels (e.g., "Sonnet 4.5") instead of raw model IDs for pinned model versions, with an upgrade hint when a newer version is available.
`/model` 选择器现在为固定的模型版本显示人类可读的标签（例如"Sonnet 4.5"）而不是原始模型 ID，并在有更新版本可用时显示升级提示。

- Managed settings can now be set via macOS plist or Windows Registry. Learn more at https://code.claude.com/docs/en/settings#settings-files
托管设置现在可以通过 macOS plist 或 Windows 注册表设置。了解更多信息请访问 https://code.claude.com/docs/en/settings#settings-files

## 2.1.50

- Added support for `startupTimeout` configuration for LSP servers
添加了对 LSP 服务器 `startupTimeout` 配置的支持

- Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees.
添加了 `WorktreeCreate` 和 `WorktreeRemove` 钩子事件，当代理工作树隔离创建或删除工作树时，支持自定义 VCS 设置和清理

- Fixed a bug where resumed sessions could be invisible when the working directory involved symlinks, because the session storage path was resolved at different times during startup. Also fixed session data loss on SSH disconnect by flushing session data before hooks and analytics in the graceful shutdown sequence.
修复了当工作目录涉及符号链接时恢复的会话可能不可见的错误，因为会话存储路径在启动期间的不同时间被解析。同时通过在优雅关闭序列中的钩子和分析之前刷新会话数据，修复了 SSH 断开时的会话数据丢失问题

- Linux: Fixed native modules not loading on systems with glibc older than 2.30 (e.g., RHEL 8)
Linux：修复了原生模块在 glibc 版本低于 2.30 的系统上无法加载的问题（例如 RHEL 8）

- Fixed memory leak in agent teams where completed teammate tasks were never garbage collected from session state
修复了 Agent Teams 中的内存泄漏问题，已完成的队友任务从未从会话状态中被垃圾回收

- Fixed `CLAUDE_CODE_SIMPLE` to fully strip down skills, session memory, custom agents, and CLAUDE.md token counting
修复了 `CLAUDE_CODE_SIMPLE` 以完全精简技能、会话内存、自定义代理和 CLAUDE.md 令牌计数

- Fixed `/mcp reconnect` freezing the CLI when given a server name that doesn't exist
修复了当给定的服务器名称不存在时 `/mcp reconnect` 冻结 CLI 的问题

- Fixed memory leak where completed task state objects were never removed from AppState
修复了已完成的任务状态对象从未从 AppState 中移除的内存泄漏问题

- Added support for `isolation: worktree` in agent definitions, allowing agents to declaratively run in isolated git worktrees.
添加了代理定义中对 `isolation: worktree` 的支持，允许代理声明式地在隔离的 git 工作树中运行

- `CLAUDE_CODE_SIMPLE` mode now also disables MCP tools, attachments, hooks, and CLAUDE.md file loading for a fully minimal experience.
`CLAUDE_CODE_SIMPLE` 模式现在还会禁用 MCP 工具、附件、钩子和 CLAUDE.md 文件加载，以提供完全最小化的体验

- Fixed bug where MCP tools were not discovered when tool search is enabled and a prompt is passed in as a launch argument
修复了当启用工具搜索并将提示作为启动参数传递时 MCP 工具未被发现的问题

- Improved memory usage during long sessions by clearing internal caches after compaction
通过在压缩后清理内部缓存，改进了长时间会话的内存使用

- Added `claude agents` CLI command to list all configured agents
添加了 `claude agents` CLI 命令来列出所有配置的代理

- Improved memory usage during long sessions by clearing large tool results after they have been processed
通过在处理完成后清理大型工具结果，改进了长时间会话的内存使用

- Fixed a memory leak where LSP diagnostic data was never cleaned up after delivery, causing unbounded memory growth in long sessions
修复了 LSP 诊断数据在传递后从未被清理的内存泄漏问题，导致长时间会话中内存无限增长

- Fixed a memory leak where completed task output was not freed from memory, reducing memory usage in long sessions with many tasks
修复了已完成的任务输出未从内存中释放的内存泄漏问题，减少了具有许多任务的长时间会话的内存使用

- Improved startup performance for headless mode (`-p` flag) by deferring Yoga WASM and UI component imports
通过延迟 Yoga WASM 和 UI 组件导入，改进了无头模式（`-p` 标志）的启动性能

- Fixed prompt suggestion cache regression that reduced cache hit rates
修复了导致缓存命中率下降的提示建议缓存回归问题

- Fixed unbounded memory growth in long sessions by capping file history snapshots
通过限制文件历史快照，修复了长时间会话中的内存无限增长问题

- Added `CLAUDE_CODE_DISABLE_1M_CONTEXT` environment variable to disable 1M context window support
添加了 `CLAUDE_CODE_DISABLE_1M_CONTEXT` 环境变量以禁用 1M 上下文窗口支持

- Opus 4.6 (fast mode) now includes the full 1M context window
Opus 4.6（快速模式）现在包含完整的 1M 上下文窗口

- VSCode: Added `/extra-usage` command support in VS Code sessions
VSCode：在 VS Code 会话中添加了 `/extra-usage` 命令支持

- Fixed memory leak where TaskOutput retained recent lines after cleanup
修复了 TaskOutput 在清理后仍保留最近行的内存泄漏问题

- Fixed memory leak in CircularBuffer where cleared items were retained in the backing array
修复了 CircularBuffer 中已清理项目仍保留在后备数组中的内存泄漏问题

- Fixed memory leak in shell command execution where ChildProcess and AbortController references were retained after cleanup
修复了 shell 命令执行中 ChildProcess 和 AbortController 引用在清理后仍被保留的内存泄漏问题

## 2.1.49

- Improved MCP OAuth authentication with step-up auth support and discovery caching, reducing redundant network requests during server connections
改进了 MCP OAuth 认证，支持阶梯式认证和发现缓存，减少了服务器连接期间的冗余网络请求

- Added `--worktree` (`-w`) flag to start Claude in an isolated git worktree
添加了 `--worktree` (`-w`) 标志，用于在隔离的 git 工作树中启动 Claude

- Subagents support `isolation: "worktree"` for working in a temporary git worktree
子代理支持 `isolation: "worktree"`，可在临时 git 工作树中工作

- Added Ctrl+F keybinding to kill background agents (two-press confirmation)
添加了 Ctrl+F 快捷键来终止后台代理（需按两次确认）

- Agent definitions support `background: true` to always run as a background task
代理定义支持 `background: true`，可始终作为后台任务运行

- Plugins can ship `settings.json` for default configuration
插件可以附带 `settings.json` 提供默认配置

- Fixed file-not-found errors to suggest corrected paths when the model drops the repo folder
修复了文件未找到错误，当模型遗漏仓库文件夹时会建议修正后的路径

- Fixed Ctrl+C and ESC being silently ignored when background agents are running and the main thread is idle. Pressing twice within 3 seconds now kills all background agents.
修复了 Ctrl+C 和 ESC 在后台代理运行且主线程空闲时被静默忽略的问题。现在在 3 秒内按两次可终止所有后台代理

- Fixed prompt suggestion cache regression that reduced cache hit rates.
修复了导致缓存命中率下降的提示建议缓存回归问题

- Fixed `plugin enable` and `plugin disable` to auto-detect the correct scope when `--scope` is not specified, instead of always defaulting to user scope
修复了 `plugin enable` 和 `plugin disable` 在未指定 `--scope` 时自动检测正确作用域的问题，不再始终默认为用户作用域

- Simple mode (`CLAUDE_CODE_SIMPLE`) now includes the file edit tool in addition to the Bash tool, allowing direct file editing in simple mode.
简单模式（`CLAUDE_CODE_SIMPLE`）现在除了 Bash 工具外还包含文件编辑工具，允许在简单模式下直接编辑文件

- Permission suggestions are now populated when safety checks trigger an ask response, enabling SDK consumers to display permission options
当安全检查触发询问响应时，现在会填充权限建议，使 SDK 使用者能够显示权限选项

- Sonnet 4.5 with 1M context is being removed from the Max plan in favor of our frontier Sonnet 4.6 model, which now has 1M context. Please switch in /model.
具有 1M 上下文的 Sonnet 4.5 正从 Max 计划中移除，取而代之的是我们的前沿 Sonnet 4.6 模型，该模型现在也具有 1M 上下文。请在 /model 中切换

- Fixed verbose mode not updating thinking block display when toggled via `/config` — memo comparators now correctly detect verbose changes
修复了通过 `/config` 切换时详细模式不更新思考块显示的问题 —— 记忆比较器现在正确检测详细模式变更

- Fixed unbounded WASM memory growth during long sessions by periodically resetting the tree-sitter parser
通过定期重置 tree-sitter 解析器，修复了长时间会话期间 WASM 内存无限增长的问题

- Fixed potential rendering issues caused by stale yoga layout references
修复了由过时的 yoga 布局引用导致的潜在渲染问题

- Improved performance in non-interactive mode (`-p`) by skipping unnecessary API calls during startup
通过在启动期间跳过不必要的 API 调用，改进了非交互模式（`-p`）的性能

- Improved performance by caching authentication failures for HTTP and SSE MCP servers, avoiding repeated connection attempts to servers requiring auth
通过缓存 HTTP 和 SSE MCP 服务器的认证失败，改进了性能，避免重复尝试连接需要认证的服务器

- Fixed unbounded memory growth during long-running sessions caused by Yoga WASM linear memory never shrinking
修复了长时间运行会话中由于 Yoga WASM 线性内存从不收缩导致的内存无限增长问题

- SDK model info now includes `supportsEffort`, `supportedEffortLevels`, and `supportsAdaptiveThinking` fields so consumers can discover model capabilities.
SDK 模型信息现在包含 `supportsEffort`、`supportedEffortLevels` 和 `supportsAdaptiveThinking` 字段，使使用者能够发现模型能力

- Added `ConfigChange` hook event that fires when configuration files change during a session, enabling enterprise security auditing and optional blocking of settings changes.
添加了 `ConfigChange` 钩子事件，当配置文件在会话期间更改时触发，支持企业安全审计和可选的设置更改阻止

- Improved startup performance by caching MCP auth failures to avoid redundant connection attempts
通过缓存 MCP 认证失败以避免冗余连接尝试，改进了启动性能

- Improved startup performance by reducing HTTP calls for analytics token counting
通过减少用于分析令牌计数的 HTTP 调用，改进了启动性能

- Improved startup performance by batching MCP tool token counting into a single API call
通过将 MCP 工具令牌计数批量处理为单个 API 调用，改进了启动性能

- Fixed `disableAllHooks` setting to respect managed settings hierarchy — non-managed settings can no longer disable managed hooks set by policy (#26637)
修复了 `disableAllHooks` 设置以遵守托管设置层级 —— 非托管设置不再能禁用由策略设置的托管钩子 (#26637)

- Fixed `--resume` session picker showing raw XML tags for sessions that start with commands like `/clear`. Now correctly falls through to the session ID fallback.
修复了 `--resume` 会话选择器为以 `/clear` 等命令开头的会话显示原始 XML 标签的问题。现在正确回退到会话 ID 备选方案

- Improved permission prompts for path safety and working directory blocks to show the reason for the restriction instead of a bare prompt with no context
改进了路径安全和工作目录阻止的权限提示，显示限制的原因而非无上下文的裸提示

## 2.1.47

- Fixed FileWriteTool line counting to preserve intentional trailing blank lines instead of stripping them with `trimEnd()`.
修复了 FileWriteTool 行计数问题，现在保留有意添加的尾部空行，而不是用 `trimEnd()` 去除它们

- Fixed Windows terminal rendering bugs caused by `os.EOL` (`\r\n`) in display code — line counts now show correct values instead of always showing 1 on Windows.
修复了由显示代码中的 `os.EOL` (`\r\n`) 导致的 Windows 终端渲染错误 —— 行计数现在显示正确值，而不是在 Windows 上始终显示 1

- Improved VS Code plan preview: auto-updates as Claude iterates, enables commenting only when the plan is ready for review, and keeps the preview open when rejecting so Claude can revise.
改进了 VS Code 计划预览：随着 Claude 迭代自动更新，仅在计划准备好审查时启用评论，并在拒绝时保持预览打开以便 Claude 修订

- Fixed a bug where bold and colored text in markdown output could shift to the wrong characters on Windows due to `\r\n` line endings.
修复了 markdown 输出中的粗体和彩色文本在 Windows 上由于 `\r\n` 行尾而可能偏移到错误字符的错误

- Fixed compaction failing when conversation contains many PDF documents by stripping document blocks alongside images before sending to the compaction API (anthropics/claude-code#26188)
修复了当对话包含许多 PDF 文档时压缩失败的问题，通过在发送到压缩 API 之前去除文档块和图片 (anthropics/claude-code#26188)

- Improved memory usage in long-running sessions by releasing API stream buffers, agent context, and skill state after use
通过在使用后释放 API 流缓冲区、代理上下文和技能状态，改进了长时间运行会话的内存使用

- Improved startup performance by deferring SessionStart hook execution, reducing time-to-interactive by ~500ms.
通过延迟 SessionStart 钩子执行改进了启动性能，将交互时间减少了约 500ms

- Fixed an issue where bash tool output was silently discarded on Windows when using MSYS2 or Cygwin shells.
修复了在 Windows 上使用 MSYS2 或 Cygwin shell 时 bash 工具输出被静默丢弃的问题

- Improved performance of `@` file mentions - file suggestions now appear faster by pre-warming the index on startup and using session-based caching with background refresh.
改进了 `@` 文件提及的性能 —— 文件建议现在出现得更快，通过在启动时预热索引并使用带后台刷新的基于会话的缓存

- Improved memory usage by trimming agent task message history after tasks complete
通过在任务完成后修剪代理任务消息历史，改进了内存使用

- Improved memory usage during long agent sessions by eliminating O(n²) message accumulation in progress updates
通过消除进度更新中的 O(n²) 消息累积，改进了长时间代理会话的内存使用

- Fixed the bash permission classifier to validate that returned match descriptions correspond to actual input rules, preventing hallucinated descriptions from incorrectly granting permissions
修复了 bash 权限分类器以验证返回的匹配描述对应于实际输入规则，防止幻觉描述错误地授予权限

- Fixed user-defined agents only loading one file on NFS/FUSE filesystems that report zero inodes (anthropics/claude-code#26044)
修复了用户定义的代理在报告零 inode 的 NFS/FUSE 文件系统上只加载一个文件的问题 (anthropics/claude-code#26044)

- Fixed plugin agent skills silently failing to load when referenced by bare name instead of fully-qualified plugin name (anthropics/claude-code#25834)
修复了当通过裸名称而非完全限定的插件名称引用时，插件代理技能静默加载失败的问题 (anthropics/claude-code#25834)

- Search patterns in collapsed tool results are now displayed in quotes for clarity
折叠工具结果中的搜索模式现在以引号显示以提高清晰度

- Windows: Fixed CWD tracking temp files never being cleaned up, causing them to accumulate indefinitely (anthropics/claude-code#17600)
Windows：修复了 CWD 跟踪临时文件从未被清理，导致它们无限期累积的问题 (anthropics/claude-code#17600)

- Use `ctrl+f` to kill all background agents instead of double-pressing ESC. Background agents now continue running when you press ESC to cancel the main thread, giving you more control over agent lifecycle.
使用 `ctrl+f` 终止所有后台代理，而不是双击 ESC。当你按 ESC 取消主线程时，后台代理现在继续运行，让你对代理生命周期有更多控制

- Fixed API 400 errors ("thinking blocks cannot be modified") that occurred in sessions with concurrent agents, caused by interleaved streaming content blocks preventing proper message merging.
修复了在具有并发代理的会话中出现的 API 400 错误（"思考块无法修改"），由交错的流式内容块阻止正确的消息合并引起

- Simplified teammate navigation to use only Shift+Down (with wrapping) instead of both Shift+Up and Shift+Down.
简化了队友导航，仅使用 Shift+Down（带循环）而不是同时使用 Shift+Up 和 Shift+Down

- Fixed an issue where a single file write/edit error would abort all other parallel file write/edit operations. Independent file mutations now complete even when a sibling fails.
修复了单个文件写入/编辑错误会中止所有其他并行文件写入/编辑操作的问题。独立的文件变更现在即使同级失败也能完成

- Added `last_assistant_message` field to Stop and SubagentStop hook inputs, providing the final assistant response text so hooks can access it without parsing transcript files.
向 Stop 和 SubagentStop 钩子输入添加了 `last_assistant_message` 字段，提供最终的助手响应文本，以便钩子可以访问它而无需解析转录文件

- Fixed custom session titles set via `/rename` being lost after resuming a conversation (anthropics/claude-code#23610)
修复了通过 `/rename` 设置的自定义会话标题在恢复对话后丢失的问题 (anthropics/claude-code#23610)

- Fixed collapsed read/search hint text overflowing on narrow terminals by truncating from the start.
修复了折叠的读取/搜索提示文本在窄终端上溢出的问题，通过从头开始截断

- Fixed an issue where bash commands with backslash-newline continuation lines (e.g., long commands split across multiple lines with `\`) would produce spurious empty arguments, potentially breaking command execution.
修复了带有反斜杠换行续行的 bash 命令（例如，用 `\` 分割成多行的长命令）会产生虚假空参数，可能破坏命令执行的问题

- Fixed built-in slash commands (`/help`, `/model`, `/compact`, etc.) being hidden from the autocomplete dropdown when many user skills are installed (anthropics/claude-code#22020)
修复了当安装了许多用户技能时，内置斜杠命令（`/help`、`/model`、`/compact` 等）被隐藏在自动完成下拉列表中的问题 (anthropics/claude-code#22020)

- Fixed MCP servers not appearing in the MCP Management Dialog after deferred loading
修复了 MCP 服务器在延迟加载后不出现在 MCP 管理对话框中的问题

- Fixed session name persisting in status bar after `/clear` command (anthropics/claude-code#26082)
修复了 `/clear` 命令后会话名称在状态栏中持久存在的问题 (anthropics/claude-code#26082)

- Fixed crash when a skill's `name` or `description` in SKILL.md frontmatter is a bare number (e.g., `name: 3000`) — the value is now properly coerced to a string (anthropics/claude-code#25837)
修复了当 SKILL.md frontmatter 中技能的 `name` 或 `description` 是裸数字（例如 `name: 3000`）时的崩溃问题 —— 该值现在正确地被强制转换为字符串 (anthropics/claude-code#25837)

- Fixed /resume silently dropping sessions when the first message exceeds 16KB or uses array-format content (anthropics/claude-code#25721)
修复了当第一条消息超过 16KB 或使用数组格式内容时 /resume 静默丢弃会话的问题 (anthropics/claude-code#25721)

- Added `chat:newline` keybinding action for configurable multi-line input (anthropics/claude-code#26075)
添加了 `chat:newline` 快捷键动作用于可配置的多行输入 (anthropics/claude-code#26075)

- Added `added_dirs` to the statusline JSON `workspace` section, exposing directories added via `/add-dir` to external scripts (anthropics/claude-code#26096)
向状态栏 JSON `workspace` 部分添加了 `added_dirs`，将通过 `/add-dir` 添加的目录暴露给外部脚本 (anthropics/claude-code#26096)

- Fixed `claude doctor` misclassifying mise and asdf-managed installations as native installs (anthropics/claude-code#26033)
修复了 `claude doctor` 将 mise 和 asdf 管理的安装错误分类为原生安装的问题 (anthropics/claude-code#26033)

- Fixed zsh heredoc failing with "read-only file system" error in sandboxed commands (anthropics/claude-code#25990)
修复了 zsh heredoc 在沙盒命令中以"只读文件系统"错误失败的问题 (anthropics/claude-code#25990)

- Fixed agent progress indicator showing inflated tool use count (anthropics/claude-code#26023)
修复了代理进度指示器显示虚高的工具使用计数的问题 (anthropics/claude-code#26023)

- Fixed image pasting not working on WSL2 systems where Windows copies images as BMP format (anthropics/claude-code#25935)
修复了在 Windows 以 BMP 格式复制图片的 WSL2 系统上图片粘贴不起作用的问题 (anthropics/claude-code#25935)

- Fixed background agent results returning raw transcript data instead of the agent's final answer (anthropics/claude-code#26012)
修复了后台代理结果返回原始转录数据而不是代理最终答案的问题 (anthropics/claude-code#26012)

- Fixed Warp terminal incorrectly prompting for Shift+Enter setup when it supports it natively (anthropics/claude-code#25957)
修复了 Warp 终端在原生支持 Shift+Enter 时错误地提示设置的问题 (anthropics/claude-code#25957)

- Fixed CJK wide characters causing misaligned timestamps and layout elements in the TUI (anthropics/claude-code#26084)
修复了 CJK 宽字符导致 TUI 中时间戳和布局元素错位的问题 (anthropics/claude-code#26084)

- Fixed custom agent `model` field in `.claude/agents/*.md` being ignored when spawning team teammates (anthropics/claude-code#26064)
修复了在生成团队队友时 `.claude/agents/*.md` 中自定义代理 `model` 字段被忽略的问题 (anthropics/claude-code#26064)

- Fixed plan mode being lost after context compaction, causing the model to switch from planning to implementation mode (anthropics/claude-code#26061)
修复了上下文压缩后计划模式丢失，导致模型从计划模式切换到实现模式的问题 (anthropics/claude-code#26061)

- Fixed `alwaysThinkingEnabled: true` in settings.json not enabling thinking mode on Bedrock and Vertex providers (anthropics/claude-code#26074)
修复了 settings.json 中的 `alwaysThinkingEnabled: true` 在 Bedrock 和 Vertex 提供商上不启用思考模式的问题 (anthropics/claude-code#26074)

- Fixed `tool_decision` OTel telemetry event not being emitted in headless/SDK mode (anthropics/claude-code#26059)
修复了 `tool_decision` OTel 遥测事件在无头/SDK 模式下不被发送的问题 (anthropics/claude-code#26059)

- Fixed session name being lost after context compaction — renamed sessions now preserve their custom title through compaction (anthropics/claude-code#26121)
修复了上下文压缩后会话名称丢失的问题 —— 重命名的会话现在通过压缩保留其自定义标题 (anthropics/claude-code#26121)

- Increased initial session count in resume picker from 10 to 50 for faster session discovery (anthropics/claude-code#26123)
将恢复选择器中的初始会话计数从 10 增加到 50，以加快会话发现 (anthropics/claude-code#26123)

- Windows: fixed worktree session matching when drive letter casing differs (anthropics/claude-code#26123)
Windows：修复了驱动器号大小写不同时的工作树会话匹配问题 (anthropics/claude-code#26123)

- Fixed `/resume <session-id>` failing to find sessions whose first message exceeds 16KB (anthropics/claude-code#25920)
修复了 `/resume <session-id>` 无法找到第一条消息超过 16KB 的会话的问题 (anthropics/claude-code#25920)

- Fixed "Always allow" on multiline bash commands creating invalid permission patterns that corrupt settings (anthropics/claude-code#25909)
修复了在多行 bash 命令上"始终允许"创建损坏设置的无效权限模式的问题 (anthropics/claude-code#25909)

- Fixed React crash (error #31) when a skill's `argument-hint` in SKILL.md frontmatter uses YAML sequence syntax (e.g., `[topic: foo | bar]`) — the value is now properly coerced to a string (anthropics/claude-code#25826)
修复了当 SKILL.md frontmatter 中技能的 `argument-hint` 使用 YAML 序列语法（例如 `[topic: foo | bar]`）时的 React 崩溃（错误 #31）—— 该值现在正确地被强制转换为字符串 (anthropics/claude-code#25826)

- Fixed crash when using `/fork` on sessions that used web search — null entries in search results from transcript deserialization are now handled gracefully (anthropics/claude-code#25811)
修复了在使用了 Web 搜索的会话上使用 `/fork` 时的崩溃问题 —— 转录反序列化中搜索结果的空条目现在被优雅地处理 (anthropics/claude-code#25811)

- Fixed read-only git commands triggering FSEvents file watcher loops on macOS by adding --no-optional-locks flag (anthropics/claude-code#25750)
通过添加 --no-optional-locks 标志修复了只读 git 命令在 macOS 上触发 FSEvents 文件监视器循环的问题 (anthropics/claude-code#25750)

- Fixed custom agents and skills not being discovered when running from a git worktree — project-level `.claude/agents/` and `.claude/skills/` from the main repository are now included (anthropics/claude-code#25816)
修复了从 git 工作树运行时自定义代理和技能不被发现的问题 —— 主仓库中项目级的 `.claude/agents/` 和 `.claude/skills/` 现在被包括 (anthropics/claude-code#25816)

- Fixed non-interactive subcommands like `claude doctor` and `claude plugin validate` being blocked inside nested Claude sessions (anthropics/claude-code#25803)
修复了 `claude doctor` 和 `claude plugin validate` 等非交互子命令在嵌套 Claude 会话中被阻止的问题 (anthropics/claude-code#25803)

- Windows: Fixed the same CLAUDE.md file being loaded twice when drive letter casing differs between paths (anthropics/claude-code#25756)
Windows：修复了当路径间驱动器号大小写不同时同一个 CLAUDE.md 文件被加载两次的问题 (anthropics/claude-code#25756)

- Fixed inline code spans in markdown being incorrectly parsed as bash commands (anthropics/claude-code#25792)
修复了 markdown 中的内联代码 span 被错误地解析为 bash 命令的问题 (anthropics/claude-code#25792)

- Fixed teammate spinners not respecting custom spinnerVerbs from settings (anthropics/claude-code#25748)
修复了队友加载动画不遵守设置中的自定义 spinnerVerbs 的问题 (anthropics/claude-code#25748)

- Fixed shell commands permanently failing after a command deletes its own working directory (anthropics/claude-code#26136)
修复了命令删除自己的工作目录后 shell 命令永久失败的问题 (anthropics/claude-code#26136)

- Fixed hooks (PreToolUse, PostToolUse) silently failing to execute on Windows by using Git Bash instead of cmd.exe (anthropics/claude-code#25981)
通过使用 Git Bash 而不是 cmd.exe 修复了钩子（PreToolUse、PostToolUse）在 Windows 上静默执行失败的问题 (anthropics/claude-code#25981)

- Fixed LSP `findReferences` and other location-based operations returning results from gitignored files (e.g., `node_modules/`, `venv/`) (anthropics/claude-code#26051)
修复了 LSP `findReferences` 和其他基于位置的操作返回来自 gitignored 文件（例如 `node_modules/`、`venv/`）的结果的问题 (anthropics/claude-code#26051)

- Moved config backup files from home directory root to `~/.claude/backups/` to reduce home directory clutter (anthropics/claude-code#26130)
将配置备份文件从主目录根目录移动到 `~/.claude/backups/` 以减少主目录混乱 (anthropics/claude-code#26130)

- Fixed sessions with large first prompts (>16KB) disappearing from the /resume list (anthropics/claude-code#26140)
修复了具有大首次提示（>16KB）的会话从 /resume 列表中消失的问题 (anthropics/claude-code#26140)

- Fixed shell functions with double-underscore prefixes (e.g., `__git_ps1`) not being preserved across shell sessions (anthropics/claude-code#25824)
修复了带有双下划线前缀（例如 `__git_ps1`）的 shell 函数在 shell 会话之间不被保留的问题 (anthropics/claude-code#25824)

- Fixed spinner showing "0 tokens" counter before any tokens have been received (anthropics/claude-code#26105)
修复了在接收到任何令牌之前加载动画显示"0 令牌"计数器的问题 (anthropics/claude-code#26105)

- VSCode: Fixed conversation messages appearing dimmed while the AskUserQuestion dialog is open (anthropics/claude-code#26078)
VSCode：修复了当 AskUserQuestion 对话框打开时对话消息显示为暗淡的问题 (anthropics/claude-code#26078)

- Fixed background tasks failing in git worktrees due to remote URL resolution reading from worktree-specific gitdir instead of the main repository config (anthropics/claude-code#26065)
修复了由于远程 URL 解析从工作树特定的 gitdir 而不是主仓库配置读取导致 git 工作树中后台任务失败的问题 (anthropics/claude-code#26065)

- Fixed Right Alt key leaving visible `[25~` escape sequence residue in the input field on Windows/Git Bash terminals (anthropics/claude-code#25943)
修复了右 Alt 键在 Windows/Git Bash 终端的输入字段中留下可见的 `[25~` 转义序列残留的问题 (anthropics/claude-code#25943)

- The `/rename` command now updates the terminal tab title by default (anthropics/claude-code#25789)
`/rename` 命令现在默认更新终端标签标题 (anthropics/claude-code#25789)

- Fixed Edit tool silently corrupting Unicode curly quotes (\u201c\u201d \u2018\u2019) by replacing them with straight quotes when making edits (anthropics/claude-code#26141)
修复了编辑工具在进行编辑时通过将 Unicode 弯引号（\u201c\u201d \u2018\u2019）替换为直引号而静默损坏它们的问题 (anthropics/claude-code#26141)

- Fixed OSC 8 hyperlinks only being clickable on the first line when link text wraps across multiple terminal lines.
修复了 OSC 8 超链接仅在链接文本跨多个终端行换行时的第一行可点击的问题

## 2.1.46

- Fixed orphaned CC processes after terminal disconnect on macOS
修复了 macOS 上终端断开后孤立的 CC 进程问题

- Added support for using claude.ai MCP connectors in Claude Code
添加了在 Claude Code 中使用 claude.ai MCP 连接器的支持

## 2.1.45

- Added support for Claude Sonnet 4.6
添加了对 Claude Sonnet 4.6 的支持

- Added support for reading `enabledPlugins` and `extraKnownMarketplaces` from `--add-dir` directories
添加了从 `--add-dir` 目录读取 `enabledPlugins` 和 `extraKnownMarketplaces` 的支持

- Added `spinnerTipsOverride` setting to customize spinner tips — configure `tips` with an array of custom tip strings, and optionally set `excludeDefault: true` to show only your custom tips instead of the built-in ones
添加了 `spinnerTipsOverride` 设置以自定义加载提示 —— 使用字符串数组配置 `tips`，并可选设置 `excludeDefault: true` 以仅显示自定义提示而非内置提示

- Added `SDKRateLimitInfo` and `SDKRateLimitEvent` types to the SDK, enabling consumers to receive rate limit status updates including utilization, reset times, and overage information
向 SDK 添加了 `SDKRateLimitInfo` 和 `SDKRateLimitEvent` 类型，使使用者能够接收速率限制状态更新，包括使用率、重置时间和超额信息

- Fixed Agent Teams teammates failing on Bedrock, Vertex, and Foundry by propagating API provider environment variables to tmux-spawned processes (anthropics/claude-code#23561)
修复了 Agent Teams 队友在 Bedrock、Vertex 和 Foundry 上失败的问题，通过将 API 提供商环境变量传递给 tmux 生成的进程 (anthropics/claude-code#23561)

- Fixed sandbox "operation not permitted" errors when writing temporary files on macOS by using the correct per-user temp directory (anthropics/claude-code#21654)
修复了 macOS 上写入临时文件时的沙盒"操作不允许"错误，通过使用正确的每用户临时目录 (anthropics/claude-code#21654)

- Fixed Task tool (backgrounded agents) crashing with a `ReferenceError` on completion (anthropics/claude-code#22087)
修复了 Task 工具（后台代理）在完成时因 `ReferenceError` 崩溃的问题 (anthropics/claude-code#22087)

- Fixed autocomplete suggestions not being accepted on Enter when images are pasted in the input
修复了当输入框粘贴图片时按 Enter 键无法接受自动完成建议的问题

- Fixed skills invoked by subagents incorrectly appearing in main session context after compaction
修复了子代理调用的技能在压缩后错误地出现在主会话上下文中的问题

- Fixed excessive `.claude.json.backup` files accumulating on every startup
修复了每次启动时累积过多 `.claude.json.backup` 文件的问题

- Fixed plugin-provided commands, agents, and hooks not being available immediately after installation without requiring a restart
修复了插件提供的命令、代理和钩子在安装后无法立即可用而需要重启的问题

- Improved startup performance by removing eager loading of session history for stats caching
通过移除用于统计缓存的会话历史预加载，改进了启动性能

- Improved memory usage for shell commands that produce large output — RSS no longer grows unboundedly with command output size
改进了产生大量输出的 shell 命令的内存使用 —— RSS 不再随命令输出大小无限增长

- Improved collapsed read/search groups to show the current file or search pattern being processed beneath the summary line while active
改进了折叠的读取/搜索组，在活动时于摘要行下方显示正在处理的当前文件或搜索模式

- [VSCode] Improved permission destination choice (project/user/session) to persist across sessions
[VSCode] 改进了权限目标选择（项目/用户/会话），使其在会话间持久保存

## 2.1.44

- Fixed ENAMETOOLONG errors for deeply-nested directory paths
修复了深层嵌套目录路径的 ENAMETOOLONG 错误

- Fixed auth refresh errors
修复了身份验证刷新错误

## 2.1.43

- Fixed AWS auth refresh hanging indefinitely by adding a 3-minute timeout
通过添加 3 分钟超时修复了 AWS 身份验证刷新无限期挂起的问题

- Fixed spurious warnings for non-agent markdown files in `.claude/agents/` directory
修复了 `.claude/agents/` 目录中非代理 markdown 文件的虚假警告问题

- Fixed structured-outputs beta header being sent unconditionally on Vertex/Bedrock
修复了在 Vertex/Bedrock 上无条件发送 structured-outputs beta 标头的问题

## 2.1.42

- Improved startup performance by deferring Zod schema construction
通过延迟 Zod schema 构建改进了启动性能

- Improved prompt cache hit rates by moving date out of system prompt
通过将日期移出系统提示改进了提示缓存命中率

- Added one-time Opus 4.6 effort callout for eligible users
为符合条件的用户添加了一次性 Opus 4.6 调用提示

- Fixed /resume showing interrupt messages as session titles
修复了 /resume 将中断消息显示为会话标题的问题

- Fixed image dimension limit errors to suggest /compact
修复了图片尺寸限制错误，现在会建议使用 /compact

## 2.1.41

- Added guard against launching Claude Code inside another Claude Code session
添加了防止在另一个 Claude Code 会话中启动 Claude Code 的保护机制

- Fixed Agent Teams using wrong model identifier for Bedrock, Vertex, and Foundry customers
修复了 Agent Teams 为 Bedrock、Vertex 和 Foundry 客户使用错误模型标识符的问题

- Fixed a crash when MCP tools return image content during streaming
修复了 MCP 工具在流式传输期间返回图片内容时的崩溃问题

- Fixed /resume session previews showing raw XML tags instead of readable command names
修复了 /resume 会话预览显示原始 XML 标签而非可读命令名称的问题

- Improved model error messages for Bedrock/Vertex/Foundry users with fallback suggestions
改进了 Bedrock/Vertex/Foundry 用户的模型错误消息，增加了回退建议

- Fixed plugin browse showing misleading "Space to Toggle" hint for already-installed plugins
修复了插件浏览对已安装插件显示误导性的"Space to Toggle"提示的问题

- Fixed hook blocking errors (exit code 2) not showing stderr to the user
修复了 hook 阻塞错误（退出码 2）不向用户显示 stderr 的问题

- Added `speed` attribute to OTel events and trace spans for fast mode visibility
为 OTel 事件和跟踪 span 添加了 `speed` 属性，用于快速模式可见性

- Added `claude auth login`, `claude auth status`, and `claude auth logout` CLI subcommands
添加了 `claude auth login`、`claude auth status` 和 `claude auth logout` CLI 子命令

- Added Windows ARM64 (win32-arm64) native binary support
添加了 Windows ARM64 (win32-arm64) 原生二进制支持

- Improved `/rename` to auto-generate session name from conversation context when called without arguments
改进了 `/rename`，在无参数调用时自动从对话上下文生成会话名称

- Improved narrow terminal layout for prompt footer
改进了提示页脚的窄终端布局

- Fixed file resolution failing for @-mentions with anchor fragments (e.g., `@README.md#installation`)
修复了带锚点片段的 @-提及（如 `@README.md#installation`）文件解析失败的问题

- Fixed FileReadTool blocking the process on FIFOs, `/dev/stdin`, and large files
修复了 FileReadTool 在 FIFO、`/dev/stdin` 和大文件上阻塞进程的问题

- Fixed background task notifications not being delivered in streaming Agent SDK mode
修复了流式 Agent SDK 模式下后台任务通知未送达的问题

- Fixed cursor jumping to end on each keystroke in classifier rule input
修复了分类器规则输入中每次按键光标跳到末尾的问题

- Fixed markdown link display text being dropped for raw URL
修复了原始 URL 的 markdown 链接显示文本被丢弃的问题

- Fixed auto-compact failure error notifications being shown to users
修复了向用户显示自动压缩失败错误通知的问题

- Fixed permission wait time being included in subagent elapsed time display
修复了权限等待时间被包含在子代理耗时显示中的问题

- Fixed proactive ticks firing while in plan mode
修复了计划模式下主动触发器触发的问题

- Fixed clear stale permission rules when settings change on disk
修复了磁盘上设置更改时清除过时权限规则的问题

- Fixed hook blocking errors showing stderr content in UI
修复了 hook 阻塞错误在 UI 中显示 stderr 内容的问题

## 2.1.39

- Improved terminal rendering performance
改进了终端渲染性能

- Fixed fatal errors being swallowed instead of displayed
修复了致命错误被静默吞没而不显示的问题

- Fixed process hanging after session close
修复了会话关闭后进程挂起的问题

- Fixed character loss at terminal screen boundary
修复了终端屏幕边界处字符丢失的问题

- Fixed blank lines in verbose transcript view
修复了详细转录视图中的空白行问题

## 2.1.38

- Fixed VS Code terminal scroll-to-top regression introduced in 2.1.37
修复了 2.1.37 引入的 VS Code 终端滚动到顶部回归问题

- Fixed Tab key queueing slash commands instead of autocompleting
修复了 Tab 键排队斜杠命令而不是自动补全的问题

- Fixed bash permission matching for commands using environment variable wrappers
修复了使用环境变量包装器的命令的 bash 权限匹配问题

- Fixed text between tool uses disappearing when not using streaming
修复了不使用流式传输时工具使用之间的文本消失的问题

- Fixed duplicate sessions when resuming in VS Code extension
修复了在 VS Code 扩展中恢复会话时出现重复会话的问题

- Improved heredoc delimiter parsing to prevent command smuggling
改进了 heredoc 分隔符解析以防止命令注入

- Blocked writes to `.claude/skills` directory in sandbox mode
在沙盒模式下阻止对 `.claude/skills` 目录的写入

## 2.1.37

- Fixed an issue where /fast was not immediately available after enabling /extra-usage
修复了启用 /extra-usage 后 /fast 无法立即可用的问题

## 2.1.36

- Fast mode is now available for Opus 4.6. Learn more at https://code.claude.com/docs/en/fast-mode
快速模式现在可用于 Opus 4.6。了解更多：https://code.claude.com/docs/en/fast-mode

## 2.1.34

- Fixed a crash when agent teams setting changed between renders
修复了智能体团队设置在渲染之间更改时的崩溃问题

- Fixed a bug where commands excluded from sandboxing could bypass the Bash ask permission rule
修复了从沙盒中排除的命令可以绕过 Bash 询问权限规则的错误

## 2.1.33

- Fixed agent teammate sessions in tmux to send and receive messages
修复了 tmux 中的智能体队友会话发送和接收消息的问题

- Fixed warnings about agent teams not being available on your current plan
修复了关于智能体团队在当前计划上不可用的警告

- Added `TeammateIdle` and `TaskCompleted` hook events for multi-agent workflows
为多智能体工作流添加了 `TeammateIdle` 和 `TaskCompleted` 钩子事件

- Added support for restricting which sub-agents can be spawned via `Task(agent_type)` syntax in agent "tools" frontmatter
添加了通过 agent "tools" frontmatter 中的 `Task(agent_type)` 语法限制可生成子智能体的支持

- Added `memory` frontmatter field support for agents, enabling persistent memory with `user`, `project`, or `local` scope
为智能体添加了 `memory` frontmatter 字段支持，启用 `user`、`project` 或 `local` 作用域的持久记忆

- Added plugin name to skill descriptions and `/skills` menu for better discoverability
在技能描述和 `/skills` 菜单中添加了插件名称，提高可发现性

- Fixed an issue where submitting a new message while the model was in extended thinking would interrupt the thinking phase
修复了在模型处于扩展思考时提交新消息会中断思考阶段的问题

- Fixed an API error that could occur when aborting mid-stream, where whitespace text combined with a thinking block would bypass normalization and produce an invalid request
修复了中止流式传输时可能发生的 API 错误，空白文本与思考块结合会绕过规范化并产生无效请求

- Fixed API proxy compatibility issue where 404 errors on streaming endpoints no longer triggered non-streaming fallback
修复了 API 代理兼容性问题，流式端点的 404 错误不再触发非流式回退

- Fixed an issue where proxy settings configured via `settings.json` environment variables were not applied to WebFetch and other HTTP requests on the Node.js build
修复了通过 `settings.json` 环境变量配置的代理设置未应用于 Node.js 构建上的 WebFetch 和其他 HTTP 请求的问题

- Fixed `/resume` session picker showing raw XML markup instead of clean titles for sessions started with slash commands
修复了 `/resume` 会话选择器对以斜杠命令开始的会话显示原始 XML 标记而非清晰标题的问题

- Improved error messages for API connection failures — now shows specific cause (e.g., ECONNREFUSED, SSL errors) instead of generic "Connection error"
改进了 API 连接失败的错误消息 — 现在显示具体原因（如 ECONNREFUSED、SSL 错误）而非通用"Connection error"

- Errors from invalid managed settings are now surfaced
来自无效托管设置的错误现在会被显示

- VSCode: Added support for remote sessions, allowing OAuth users to browse and resume sessions from claude.ai
VSCode：添加了对远程会话的支持，允许 OAuth 用户从 claude.ai 浏览和恢复会话

- VSCode: Added git branch and message count to the session picker, with support for searching by branch name
VSCode：在会话选择器中添加了 git 分支和消息计数，支持按分支名搜索

- VSCode: Fixed scroll-to-bottom under-scrolling on initial session load and session switch
VSCode：修复了初始会话加载和会话切换时滚动到底部不足的问题

## 2.1.32

- Claude Opus 4.6 is now available!
Claude Opus 4.6 现已可用！

- Added research preview agent teams feature for multi-agent collaboration (token-intensive feature, requires setting CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1)
添加了用于多智能体协作的研究预览版智能体团队功能（token 消耗密集型功能，需设置 CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1）

- Claude now automatically records and recalls memories as it works
Claude 现在会在工作时自动记录和回忆记忆

- Added "Summarize from here" to the message selector, allowing partial conversation summarization
在消息选择器中添加了"从此处摘要"功能，允许部分对话摘要

- Skills defined in `.claude/skills/` within additional directories (`--add-dir`) are now loaded automatically
在附加目录（`--add-dir`）中的 `.claude/skills/` 里定义的技能现在会自动加载

- Fixed `@` file completion showing incorrect relative paths when running from a subdirectory
修复了从子目录运行时 `@` 文件补全显示错误相对路径的问题

- Updated --resume to re-use --agent value specified in previous conversation by default
更新了 --resume 默认重用上一次对话中指定的 --agent 值

- Fixed: Bash tool no longer throws "Bad substitution" errors when heredocs contain JavaScript template literals like `${index + 1}`, which previously interrupted tool execution
修复了：Bash 工具不再在 heredocs 包含 JavaScript 模板字面量（如 `${index + 1}`）时抛出"Bad substitution"错误，该错误之前会中断工具执行

- Skill character budget now scales with context window (2% of context), so users with larger context windows can see more skill descriptions without truncation
技能字符预算现在根据上下文窗口扩展（上下文的 2%），因此具有更大上下文窗口的用户可以看到更多技能描述而不被截断

- Fixed Thai/Lao spacing vowels (สระ า, ำ) not rendering correctly in the input field
修复了泰语/老挝语元音（สระ า, ำ）在输入字段中无法正确渲染的问题

- VSCode: Fixed slash commands incorrectly being executed when pressing Enter with preceding text in the input field
VSCode：修复了在输入字段中有前置文本时按 Enter 错误执行斜杠命令的问题

- VSCode: Added spinner when loading past conversations list
VSCode：添加了加载历史对话列表时的加载动画

## 2.1.31

- Added session resume hint on exit, showing how to continue your conversation later
添加了退出时的会话恢复提示，展示稍后如何继续对话

- Added support for full-width (zenkaku) space input from Japanese IME in checkbox selection
添加了在复选框选择中支持日语输入法全角空格输入

- Fixed PDF too large errors permanently locking up sessions, requiring users to start a new conversation
修复了 PDF 过大错误永久锁定会话的问题，该问题曾要求用户开始新对话

- Fixed bash commands incorrectly reporting failure with "Read-only file system" errors when sandbox mode was enabled
修复了启用沙盒模式时 bash 命令错误报告"只读文件系统"失败的问题

- Fixed a crash that made sessions unusable after entering plan mode when project config in `~/.claude.json` was missing default fields
修复了当 `~/.claude.json` 中的项目配置缺少默认字段时，进入计划模式后导致会话无法使用的崩溃问题

- Fixed `temperatureOverride` being silently ignored in the streaming API path, causing all streaming requests to use the default temperature (1) regardless of the configured override
修复了 `temperatureOverride` 在流式 API 路径中被静默忽略的问题，该问题曾导致所有流式请求都使用默认温度（1），而不管配置的覆盖值

- Fixed LSP shutdown/exit compatibility with strict language servers that reject null params
修复了与拒绝 null 参数的严格语言服务器的 LSP 关闭/退出兼容性问题

- Improved system prompts to more clearly guide the model toward using dedicated tools (Read, Edit, Glob, Grep) instead of bash equivalents (`cat`, `sed`, `grep`, `find`), reducing unnecessary bash command usage
改进了系统提示，更清晰地引导模型使用专用工具（Read、Edit、Glob、Grep）而不是 bash 等效命令（`cat`、`sed`、`grep`、`find`），减少了不必要的 bash 命令使用

- Improved PDF and request size error messages to show actual limits (100 pages, 20MB)
改进了 PDF 和请求大小错误消息，显示实际限制（100 页，20MB）

- Reduced layout jitter in the terminal when the spinner appears and disappears during streaming
减少了流式传输期间加载动画出现和消失时终端中的布局抖动

- Removed misleading Anthropic API pricing from model selector for third-party provider (Bedrock, Vertex, Foundry) users
为第三方提供商（Bedrock、Vertex、Foundry）用户从模型选择器中移除了误导性的 Anthropic API 定价

## 2.1.30

- Added `pages` parameter to the Read tool for PDFs, allowing specific page ranges to be read (e.g., `pages: "1-5"`). Large PDFs (>10 pages) now return a lightweight reference when `@` mentioned instead of being inlined into context.
为 Read 工具添加了 `pages` 参数用于 PDF，允许读取特定页面范围（例如 `pages: "1-5"`）。大型 PDF（>10 页）在 `@` 提到时现在返回轻量级引用，而不是内联到上下文中。

- Added pre-configured OAuth client credentials for MCP servers that don't support Dynamic Client Registration (e.g., Slack). Use `--client-id` and `--client-secret` with `claude mcp add`.
为不支持动态客户端注册的 MCP 服务器（例如 Slack）添加了预配置的 OAuth 客户端凭据。使用 `--client-id` 和 `--client-secret` 与 `claude mcp add` 一起使用。

- Added `/debug` for Claude to help troubleshoot the current session
为 Claude 添加了 `/debug` 命令以帮助排查当前会话问题

- Added support for additional `git log` and `git show` flags in read-only mode (e.g., `--topo-order`, `--cherry-pick`, `--format`, `--raw`)
在只读模式下添加了对额外 `git log` 和 `git show` 标志的支持（例如 `--topo-order`、`--cherry-pick`、`--format`、`--raw`）

- Added token count, tool uses, and duration metrics to Task tool results
为 Task 工具结果添加了令牌计数、工具使用和持续时间指标

- Added reduced motion mode to the config
为配置添加了减少动画模式

- Fixed phantom "(no content)" text blocks appearing in API conversation history, reducing token waste and potential model confusion
修复了 API 对话历史中出现的虚幻"(no content)"文本块，减少了令牌浪费和潜在的模型混淆

- Fixed prompt cache not correctly invalidating when tool descriptions or input schemas changed, only when tool names changed
修复了工具描述或输入架构更改时提示缓存未正确失效的问题，之前仅在工具名称更改时才失效

- Fixed 400 errors that could occur after running `/login` when the conversation contained thinking blocks
修复了当对话包含思考块时运行 `/login` 后可能发生的 400 错误

- Fixed a hang when resuming sessions with corrupted transcript files containing `parentUuid` cycles
修复了恢复包含 `parentUuid` 循环的损坏转录文件会话时的挂起问题

- Fixed rate limit message showing incorrect "/upgrade" suggestion for Max 20x users when extra-usage is unavailable
修复了当额外使用不可用时，Max 20x 用户的速率限制消息显示不正确的"/upgrade"建议

- Fixed permission dialogs stealing focus while actively typing
修复了在主动输入时权限对话框窃取焦点的问题

- Fixed subagents not being able to access SDK-provided MCP tools because they were not synced to the shared application state
修复了子智能体无法访问 SDK 提供的 MCP 工具的问题，因为它们未同步到共享应用程序状态

- Fixed a regression where Windows users with a `.bashrc` file could not run bash commands
修复了 Windows 用户拥有 `.bashrc` 文件时无法运行 bash 命令的回归问题

- Improved memory usage for `--resume` (68% reduction for users with many sessions) by replacing the session index with lightweight stat-based loading and progressive enrichment
通过用轻量级基于统计的加载和渐进式丰富替换会话索引，改进了 `--resume` 的内存使用（拥有许多会话的用户减少 68%）

- Improved `TaskStop` tool to display the stopped command/task description in the result line instead of a generic "Task stopped" message
改进了 `TaskStop` 工具，在结果行中显示已停止的命令/任务描述，而不是通用的"Task stopped"消息

- Changed `/model` to execute immediately instead of being queued
将 `/model` 更改为立即执行而不是排队

- [VSCode] Added multiline input support to the "Other" text input in question dialogs (use Shift+Enter for new lines)
[VSCode] 为问题对话框中的"Other"文本输入添加了多行输入支持（使用 Shift+Enter 换行）

- [VSCode] Fixed duplicate sessions appearing in the session list when starting a new conversation
[VSCode] 修复了开始新对话时会话列表中出现重复会话的问题

## 2.1.29

- Fixed startup performance issues when resuming sessions that have `saved_hook_context`
修复了恢复具有 `saved_hook_context` 的会话时的启动性能问题

## 2.1.27

- Added tool call failures and denials to debug logs
添加了工具调用失败和拒绝到调试日志

- Fixed context management validation error for gateway users, ensuring `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` avoids the error
修复了网关用户的上下文管理验证错误，确保 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` 可以避免该错误

- Added `--from-pr` flag to resume sessions linked to a specific GitHub PR number or URL
添加了 `--from-pr` 标志以恢复链接到特定 GitHub PR 编号或 URL 的会话

- Sessions are now automatically linked to PRs when created via `gh pr create`
现在通过 `gh pr create` 创建会话时会自动链接到 PR

- Fixed /context command not displaying colored output
修复了 /context 命令不显示彩色输出的问题

- Fixed status bar duplicating background task indicator when PR status was shown
修复了显示 PR 状态时状态栏重复显示后台任务指示器的问题

- Windows: Fixed bash command execution failing for users with `.bashrc` files
Windows：修复了拥有 `.bashrc` 文件的用户 bash 命令执行失败的问题

- Windows: Fixed console windows flashing when spawning child processes
Windows：修复了生成子进程时控制台窗口闪烁的问题

- VSCode: Fixed OAuth token expiration causing 401 errors after extended sessions
VSCode：修复了 OAuth 令牌过期在长时间会话后导致 401 错误的问题

## 2.1.25

- Fixed beta header validation error for gateway users on Bedrock and Vertex, ensuring `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` avoids the error
修复了 Bedrock 和 Vertex 上网关用户的 beta 标头验证错误，确保 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` 可以避免该错误

## 2.1.23

- Added customizable spinner verbs setting (`spinnerVerbs`)
添加了可自定义的加载动画动词设置（`spinnerVerbs`）

- Fixed mTLS and proxy connectivity for users behind corporate proxies or using client certificates
修复了企业代理后用户或使用客户端证书用户的 mTLS 和代理连接问题

- Fixed per-user temp directory isolation to prevent permission conflicts on shared systems
修复了每用户临时目录隔离，防止共享系统上的权限冲突

- Fixed a race condition that could cause 400 errors when prompt caching scope was enabled
修复了启用提示缓存范围时可能导致 400 错误的竞态条件

- Fixed pending async hooks not being cancelled when headless streaming sessions ended
修复了无头流会话结束时待处理的异步钩子未被取消的问题

- Fixed tab completion not updating the input field when accepting a suggestion
修复了接受建议时 tab 补全未更新输入字段的问题

- Fixed ripgrep search timeouts silently returning empty results instead of reporting errors
修复了 ripgrep 搜索超时时静默返回空结果而非报告错误的问题

- Improved terminal rendering performance with optimized screen data layout
通过优化屏幕数据布局改进了终端渲染性能

- Changed Bash commands to show timeout duration alongside elapsed time
将 Bash 命令更改为同时显示超时时长和已用时长

- Changed merged pull requests to show a purple status indicator in the prompt footer
将已合并的 PR 更改为在提示页脚显示紫色状态指示器

- [IDE] Fixed model options displaying incorrect region strings for Bedrock users in headless mode
[IDE] 修复了无头模式下 Bedrock 用户的模型选项显示错误区域字符串的问题

## 2.1.22

- Fixed structured outputs for non-interactive (-p) mode
修复了非交互式（-p）模式下的结构化输出问题

## 2.1.21

- Added support for full-width (zenkaku) number input from Japanese IME in option selection prompts
添加了对日语输入法全角（zenkaku）数字输入在选项选择提示中的支持

- Fixed shell completion cache files being truncated on exit
修复了 shell 补全缓存文件在退出时被截断的问题

- Fixed API errors when resuming sessions that were interrupted during tool execution
修复了恢复在工具执行期间被中断的会话时的 API 错误

- Fixed auto-compact triggering too early on models with large output token limits
修复了在大输出 token 限制的模型上自动压缩过早触发的问题

- Fixed task IDs potentially being reused after deletion
修复了任务 ID 在删除后可能被重用的问题

- Fixed file search not working in VS Code extension on Windows
修复了 VS Code 扩展在 Windows 上文件搜索不工作的问题

- Improved read/search progress indicators to show "Reading…" while in progress and "Read" when complete
改进了读取/搜索进度指示器，进行中显示"Reading…"，完成后显示"Read"

- Improved Claude to prefer file operation tools (Read, Edit, Write) over bash equivalents (cat, sed, awk)
改进了 Claude 的行为，使其优先使用文件操作工具（Read、Edit、Write）而非等效的 bash 命令（cat、sed、awk）

- [VSCode] Added automatic Python virtual environment activation, ensuring `python` and `pip` commands use the correct interpreter (configurable via `claudeCode.usePythonEnvironment` setting)
[VSCode] 添加了自动 Python 虚拟环境激活功能，确保 `python` 和 `pip` 命令使用正确的解释器（可通过 `claudeCode.usePythonEnvironment` 设置配置）

- [VSCode] Fixed message action buttons having incorrect background colors
[VSCode] 修复了消息操作按钮背景颜色不正确的问题

## 2.1.20

- Added arrow key history navigation in vim normal mode when cursor cannot move further
添加了 vim 普通模式下光标无法继续移动时的方向键历史导航功能

- Added external editor shortcut (Ctrl+G) to the help menu for better discoverability
在帮助菜单中添加了外部编辑器快捷键（Ctrl+G），提高可发现性

- Added PR review status indicator to the prompt footer, showing the current branch's PR state (approved, changes requested, pending, or draft) as a colored dot with a clickable link
在提示页脚添加了 PR 审查状态指示器，以彩色圆点和可点击链接显示当前分支的 PR 状态（已批准、请求更改、待处理或草稿）

- Added support for loading `CLAUDE.md` files from additional directories specified via `--add-dir` flag (requires setting `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`)
添加了从通过 `--add-dir` 标志指定的其他目录加载 `CLAUDE.md` 文件的支持（需要设置 `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1`）

- Added ability to delete tasks via the `TaskUpdate` tool
添加了通过 `TaskUpdate` 工具删除任务的功能

- Fixed session compaction issues that could cause resume to load full history instead of the compact summary
修复了会话压缩问题，该问题可能导致恢复时加载完整历史而非压缩摘要

- Fixed agents sometimes ignoring user messages sent while actively working on a task
修复了代理在积极处理任务时有时忽略用户消息的问题

- Fixed wide character (emoji, CJK) rendering artifacts where trailing columns were not cleared when replaced by narrower characters
修复了宽字符（表情符号、CJK）渲染瑕疵，该问题会导致尾部列在替换为较窄字符时未被清除

- Fixed JSON parsing errors when MCP tool responses contain special Unicode characters
修复了 MCP 工具响应包含特殊 Unicode 字符时的 JSON 解析错误

- Fixed up/down arrow keys in multi-line and wrapped text input to prioritize cursor movement over history navigation
修复了多行和换行文本输入中上下方向键优先执行光标移动而非历史导航的问题

- Fixed draft prompt being lost when pressing UP arrow to navigate command history
修复了按 UP 方向键导航命令历史时草稿提示丢失的问题

- Fixed ghost text flickering when typing slash commands mid-input
修复了输入中途输入斜杠命令时幽灵文本闪烁的问题

- Fixed marketplace source removal not properly deleting settings
修复了插件市场来源移除未正确删除设置的问题

- Fixed duplicate output in some commands like `/context`
修复了某些命令（如 `/context`）中的重复输出问题

- Fixed task list sometimes showing outside the main conversation view
修复了任务列表有时显示在主对话视图之外的问题

- Fixed syntax highlighting for diffs occurring within multiline constructs like Python docstrings
修复了 Python 文档字符串等多行构造中的差异语法高亮问题

- Fixed crashes when cancelling tool use
修复了取消工具使用时的崩溃问题

- Improved `/sandbox` command UI to show dependency status with installation instructions when dependencies are missing
改进了 `/sandbox` 命令 UI，在缺少依赖时显示依赖状态和安装说明

- Improved thinking status text with a subtle shimmer animation
为思考状态文本添加了微妙的微光动画效果

- Improved task list to dynamically adjust visible items based on terminal height
改进了任务列表，使其根据终端高度动态调整可见项目

- Improved fork conversation hint to show how to resume the original session
改进了分支对话提示，显示如何恢复原始会话

- Changed collapsed read/search groups to show present tense ("Reading", "Searching for") while in progress, and past tense ("Read", "Searched for") when complete
将折叠的读取/搜索组更改为进行中显示现在时（"Reading"、"Searching for"），完成后显示过去时（"Read"、"Searched for"）

- Changed teammate messages to render with rich Markdown formatting (bold, code blocks, lists, etc.) instead of plain text
将团队成员消息更改为使用富 Markdown 格式（粗体、代码块、列表等）渲染，而非纯文本

- Changed `ToolSearch` results to appear as a brief notification instead of inline in the conversation
将 `ToolSearch` 结果更改为以简短通知形式显示，而非对话中的内联显示

- Changed the `/commit-push-pr` skill to automatically post PR URLs to Slack channels when configured via MCP tools
将 `/commit-push-pr` 技能更改为在通过 MCP 工具配置时自动将 PR URL 发布到 Slack 频道

- Changed the `/copy` command to be available to all users
将 `/copy` 命令更改为对所有用户可用

- Changed background agents to prompt for tool permissions before launching
将后台代理更改为在启动前提示工具权限

- Changed permission rules like `Bash(*)` to be accepted and treated as equivalent to `Bash`
将 `Bash(*)` 等权限规则更改为被接受并视为与 `Bash` 等效

- Changed config backups to be timestamped and rotated (keeping 5 most recent) to prevent data loss
将配置备份更改为带时间戳并轮换（保留最近 5 个），以防止数据丢失

## 2.1.19

- Added env var `CLAUDE_CODE_ENABLE_TASKS`, set to `false` to keep the old system temporarily
添加了环境变量 `CLAUDE_CODE_ENABLE_TASKS`，设置为 `false` 可暂时保留旧系统

- Added shorthand `$0`, `$1`, etc. for accessing individual arguments in custom commands
添加了简写 `$0`、`$1` 等，用于在自定义命令中访问单个参数

- Fixed crashes on processors without AVX instruction support
修复了不支持 AVX 指令集的处理器上的崩溃问题

- Fixed dangling Claude Code processes when terminal is closed by catching EIO errors from `process.exit()` and using SIGKILL as fallback
修复了终端关闭时残留的 Claude Code 进程问题，通过捕获 `process.exit()` 的 EIO 错误并使用 SIGKILL 作为备用方案

- Fixed `/rename` and `/tag` not updating the correct session when resuming from a different directory (e.g., git worktrees)
修复了从不同目录（如 git worktrees）恢复会话时 `/rename` 和 `/tag` 未更新正确会话的问题

- Fixed resuming sessions by custom title not working when run from a different directory
修复了从不同目录运行时无法按自定义标题恢复会话的问题

- Fixed pasted text content being lost when using prompt stash (Ctrl+S) and restore
修复了使用提示暂存（Ctrl+S）和恢复时粘贴文本内容丢失的问题

- Fixed agent list displaying "Sonnet (default)" instead of "Inherit (default)" for agents without an explicit model setting
修复了代理列表为未明确设置模型的代理显示"Sonnet (default)"而非"Inherit (default)"的问题

- Fixed backgrounded hook commands not returning early, potentially causing the session to wait on a process that was intentionally backgrounded
修复了后台 hook 命令未提前返回的问题，该问题可能导致会话等待本应后台运行的进程

- Fixed file write preview omitting empty lines
修复了文件写入预览省略空行的问题

- Changed skills without additional permissions or hooks to be allowed without requiring approval
更改了无额外权限或 hooks 的技能的许可方式，现在无需审批即可使用

- Changed indexed argument syntax from `$ARGUMENTS.0` to `$ARGUMENTS[0]` (bracket syntax)
将索引参数语法从 `$ARGUMENTS.0` 更改为 `$ARGUMENTS[0]`（括号语法）

- [SDK] Added replay of `queued_command` attachment messages as `SDKUserMessageReplay` events when `replayUserMessages` is enabled
[SDK] 添加了在启用 `replayUserMessages` 时将 `queued_command` 附件消息作为 `SDKUserMessageReplay` 事件重放的功能

- [VSCode] Enabled session forking and rewind functionality for all users
[VSCode] 为所有用户启用了会话分支和回退功能

## 2.1.18

- Added customizable keyboard shortcuts. Configure keybindings per context, create chord sequences, and personalize your workflow. Run `/keybindings` to get started. Learn more at https://code.claude.com/docs/en/keybindings
添加了可自定义的键盘快捷键功能。可以按上下文配置键绑定、创建和弦序列并个性化工作流程。运行 `/keybindings` 开始使用。了解更多信息：https://code.claude.com/docs/en/keybindings

## 2.1.17

- Fixed crashes on processors without AVX instruction support
修复了不支持 AVX 指令集的处理器上的崩溃问题

## 2.1.16

- Added new task management system, including new capabilities like dependency tracking
添加了新的任务管理系统，包括依赖跟踪等新功能

- [VSCode] Added native plugin management support
[VSCode] 添加了原生插件管理支持

- [VSCode] Added ability for OAuth users to browse and resume remote Claude sessions from the Sessions dialog
[VSCode] 为 OAuth 用户添加了从会话对话框浏览和恢复远程 Claude 会话的功能

- Fixed out-of-memory crashes when resuming sessions with heavy subagent usage
修复了恢复使用大量子代理的会话时的内存不足崩溃问题

- Fixed an issue where the "context remaining" warning was not hidden after running `/compact`
修复了运行 `/compact` 命令后"上下文剩余"警告未隐藏的问题

- Fixed session titles on the resume screen not respecting the user's language setting
修复了恢复屏幕上的会话标题未遵守用户语言设置的问题

- [IDE] Fixed a race condition on Windows where the Claude Code sidebar view container would not appear on start
[IDE] 修复了 Windows 上 Claude Code 侧边栏视图容器在启动时不显示的竞态条件问题

## 2.1.15

- Added deprecation notification for npm installations - run `claude install` or see https://docs.anthropic.com/en/docs/claude-code/getting-started for more options
添加了 npm 安装方式的弃用通知 - 运行 `claude install` 或访问 https://docs.anthropic.com/en/docs/claude-code/getting-started 查看更多选项

- Improved UI rendering performance with React Compiler
通过 React Compiler 改进了 UI 渲染性能

- Fixed the "Context left until auto-compact" warning not disappearing after running `/compact`
修复了运行 `/compact` 命令后"上下文自动压缩剩余量"警告未消失的问题

- Fixed MCP stdio server timeout not killing child process, which could cause UI freezes
修复了 MCP stdio 服务器超时未终止子进程的问题，该问题可能导致 UI 冻结

## 2.1.14

- Added history-based autocomplete in bash mode (`!`) - type a partial command and press Tab to complete from your bash command history
添加了基于历史记录的 bash 模式（`!`）自动补全 - 输入部分命令并按 Tab 键从 bash 命令历史中完成补全

- Added search to installed plugins list - type to filter by name or description
为已安装插件列表添加了搜索功能 - 输入以按名称或描述进行筛选

- Added support for pinning plugins to specific git commit SHAs, allowing marketplace entries to install exact versions
添加了将插件固定到特定 git commit SHA 的支持，允许从市场条目安装精确版本

- Fixed a regression where the context window blocking limit was calculated too aggressively, blocking users at ~65% context usage instead of the intended ~98%
修复了上下文窗口阻塞限制计算过于激进的回归问题，之前在约 65% 上下文使用时就阻止用户，而非预期的约 98%

- Fixed memory issues that could cause crashes when running parallel subagents
修复了运行并行子代理时可能导致崩溃的内存问题

- Fixed memory leak in long-running sessions where stream resources were not cleaned up after shell commands completed
修复了长时间运行会话中的内存泄漏问题，此前 shell 命令完成后未清理流资源

- Fixed `@` symbol incorrectly triggering file autocomplete suggestions in bash mode
修复了 bash 模式下 `@` 符号错误触发文件自动补全建议的问题

- Fixed `@`-mention menu folder click behavior to navigate into directories instead of selecting them
修复了 `@` 提及菜单文件夹点击行为，现在会进入目录而不是选择它们

- Fixed `/feedback` command generating invalid GitHub issue URLs when description is very long
修复了 `/feedback` 命令在描述很长时生成无效 GitHub issue URL 的问题

- Fixed `/context` command to show the same token count and percentage as the status line in verbose mode
修复了 `/context` 命令，使其在详细模式下显示与状态行相同的 token 数量和百分比

- Fixed an issue where `/config`, `/context`, `/model`, and `/todos` command overlays could close unexpectedly
修复了 `/config`、`/context`、`/model` 和 `/todos` 命令覆盖层可能意外关闭的问题

- Fixed slash command autocomplete selecting wrong command when typing similar commands (e.g., `/context` vs `/compact`)
修复了输入相似命令时（如 `/context` 与 `/compact`）斜杠命令自动补全选择错误命令的问题

- Fixed inconsistent back navigation in plugin marketplace when only one marketplace is configured
修复了仅配置一个市场时插件市场返回导航不一致的问题

- Fixed iTerm2 progress bar not clearing properly on exit, preventing lingering indicators and bell sounds
修复了 iTerm2 进度栏在退出时未正确清除的问题，避免了残留指示器和提示音

- Improved backspace to delete pasted text as a single token instead of one character at a time
改进了退格键功能，现在可以将粘贴的文本作为单个标记删除，而不是逐字符删除

- [VSCode] Added `/usage` command to display current plan usage
[VSCode] 添加了 `/usage` 命令以显示当前计划使用情况

## 2.1.13

（该版本在官方 CHANGELOG 中未列出具体更新内容）

## 2.1.12

- Fixed message rendering bug
修复了消息渲染的 bug

## 2.1.11

- Fixed excessive MCP connection requests for HTTP/SSE transports
修复了 HTTP/SSE 传输方式的过度 MCP 连接请求问题

## 2.1.10

- Added new `Setup` hook event that can be triggered via `--init`, `--init-only`, or `--maintenance` CLI flags for repository setup and maintenance operations
添加了新的 `Setup` hook 事件，可通过 `--init`、`--init-only` 或 `--maintenance` CLI 标志触发，用于仓库设置和维护操作

- Added keyboard shortcut 'c' to copy OAuth URL when browser doesn't open automatically during login
添加了键盘快捷键 'c'，用于在登录时浏览器未自动打开时复制 OAuth URL

- Fixed a crash when running bash commands containing heredocs with JavaScript template literals like `${index + 1}`
修复了运行包含 JavaScript 模板字面量（如 `${index + 1}`）的 heredocs bash 命令时的崩溃问题

- Improved startup to capture keystrokes typed before the REPL is fully ready
改进了启动过程，以捕获在 REPL 完全准备好之前输入的按键

- Improved file suggestions to show as removable attachments instead of inserting text when accepted
改进了文件建议，使其在接受时显示为可移除的附件，而不是插入文本

- [VSCode] Added install count display to plugin listings
[VSCode] 在插件列表中添加了安装数量显示

- [VSCode] Added trust warning when installing plugins
[VSCode] 安装插件时添加了信任警告

## 2.1.9

- Added `auto:N` syntax for configuring the MCP tool search auto-enable threshold, where N is the context window percentage (0-100)
添加了 `auto:N` 语法，用于配置 MCP 工具搜索自动启用阈值，其中 N 是上下文窗口百分比（0-100）

- Added `plansDirectory` setting to customize where plan files are stored
添加了 `plansDirectory` 设置，用于自定义计划文件的存储位置

- Added external editor support (Ctrl+G) in AskUserQuestion "Other" input field
在 AskUserQuestion "Other" 输入字段中添加了外部编辑器支持（Ctrl+G）

- Added session URL attribution to commits and PRs created from web sessions
为从 web 会话创建的提交和 PR 添加了会话 URL 归属信息

- Added support for `PreToolUse` hooks to return `additionalContext` to the model
添加了 `PreToolUse` hooks 向模型返回 `additionalContext` 的支持

- Added `${CLAUDE_SESSION_ID}` string substitution for skills to access the current session ID
添加了 `${CLAUDE_SESSION_ID}` 字符串替换，供技能访问当前会话 ID

- Fixed long sessions with parallel tool calls failing with an API error about orphan tool_result blocks
修复了长时间会话中使用并行工具调用时因孤立 tool_result 块而导致的 API 错误

- Fixed MCP server reconnection hanging when cached connection promise never resolves
修复了缓存的连接 promise 永远不解析时 MCP 服务器重新连接挂起的问题

- Fixed Ctrl+Z suspend not working in terminals using Kitty keyboard protocol (Ghostty, iTerm2, kitty, WezTerm)
修复了使用 Kitty 键盘协议的终端（Ghostty、iTerm2、kitty、WezTerm）中 Ctrl+Z 挂起不起作用的问题

## 2.1.7

- Added `showTurnDuration` setting to hide turn duration messages (e.g., "Cooked for 1m 6s")
添加了 `showTurnDuration` 设置，用于隐藏回合持续时间消息（例如"Cooked for 1m 6s"）

- Added ability to provide feedback when accepting permission prompts
添加了在接受权限提示时提供反馈的功能

- Added inline display of agent's final response in task notifications, making it easier to see results without reading the full transcript file
在任务通知中添加了代理最终响应的内联显示，便于在不阅读完整记录文件的情况下查看结果

- Fixed security vulnerability where wildcard permission rules could match compound commands containing shell operators
修复了通配符权限规则可能匹配包含 shell 操作符的复合命令的安全漏洞

- Fixed false "file modified" errors on Windows when cloud sync tools, antivirus scanners, or Git touch file timestamps without changing content
修复了 Windows 上云同步工具、防病毒扫描程序或 Git 在未更改内容的情况下触碰文件时间戳时产生的虚假"文件已修改"错误

- Fixed orphaned tool_result errors when sibling tools fail during streaming execution
修复了流式执行期间同级工具失败时产生的孤立 tool_result 错误

- Fixed context window blocking limit being calculated using the full context window instead of the effective context window (which reserves space for max output tokens)
修复了使用完整上下文窗口而非有效上下文窗口（为最大输出令牌预留空间）计算上下文窗口阻塞限制的问题

- Fixed spinner briefly flashing when running local slash commands like `/model` or `/theme`
修复了运行本地斜杠命令（如 `/model` 或 `/theme`）时加载器短暂闪烁的问题

- Fixed terminal title animation jitter by using fixed-width braille characters
通过使用固定宽度的盲文字符修复了终端标题动画抖动

- Fixed plugins with git submodules not being fully initialized when installed
修复了带有 git 子模块的插件在安装时未完全初始化的问题

- Fixed bash commands failing on Windows when temp directory paths contained characters like `t` or `n` that were misinterpreted as escape sequences
修复了 Windows 上临时目录路径包含 `t` 或 `n` 等被误解为转义序列的字符时 bash 命令失败的问题

- Improved typing responsiveness by reducing memory allocation overhead in terminal rendering
通过减少终端渲染中的内存分配开销，改进了输入响应性

- Enabled MCP tool search auto mode by default for all users. When MCP tool descriptions exceed 10% of the context window, they are automatically deferred and discovered via the MCPSearch tool instead of being loaded upfront. This reduces context usage for users with many MCP tools configured. Users can disable this by adding `MCPSearch` to `disallowedTools` in their settings.
为所有用户默认启用了 MCP 工具搜索自动模式。当 MCP 工具描述超过上下文窗口的 10% 时，它们将被自动延迟并通过 MCPSearch 工具发现，而不是预先加载。这减少了配置了许多 MCP 工具的用户的上下文使用量。用户可以通过在设置中将 `MCPSearch` 添加到 `disallowedTools` 来禁用此功能。

- Changed OAuth and API Console URLs from console.anthropic.com to platform.claude.com
将 OAuth 和 API Console URL 从 console.anthropic.com 更改为 platform.claude.com

- [VSCode] Fixed `claudeProcessWrapper` setting passing the wrapper path instead of the Claude binary path
[VSCode] 修复了 `claudeProcessWrapper` 设置传递包装器路径而非 Claude 二进制路径的问题

## 2.1.6

- Added search functionality to `/config` command for quickly filtering settings
为 `/config` 命令添加了搜索功能，用于快速过滤设置

- Added Updates section to `/doctor` showing auto-update channel and available npm versions (stable/latest)
为 `/doctor` 添加了 Updates 部分，显示自动更新通道和可用的 npm 版本（stable/latest）

- Added date range filtering to `/stats` command - press `r` to cycle between Last 7 days, Last 30 days, and All time
为 `/stats` 命令添加了日期范围过滤 - 按 `r` 在"最近 7 天"、"最近 30 天"和"全部时间"之间循环

- Added automatic discovery of skills from nested `.claude/skills` directories when working with files in subdirectories
添加了在子目录中处理文件时从嵌套的 `.claude/skills` 目录自动发现技能的功能

- Added `context_window.used_percentage` and `context_window.remaining_percentage` fields to status line input for easier context window display
为状态行输入添加了 `context_window.used_percentage` 和 `context_window.remaining_percentage` 字段，以便更轻松地显示上下文窗口

- Added an error display when the editor fails during Ctrl+G
在 Ctrl+G 期间编辑器失败时添加了错误显示

- Fixed permission bypass via shell line continuation that could allow blocked commands to execute
修复了通过 shell 行继续绕过权限的问题，该问题可能允许被阻止的命令执行

- Fixed false "File has been unexpectedly modified" errors when file watchers touch files without changing content
修复了文件监视器在不更改内容的情况下触碰文件时产生的虚假"文件已被意外修改"错误

- Fixed text styling (bold, colors) getting progressively misaligned in multi-line responses
修复了多行响应中文本样式（粗体、颜色）逐渐错位的问题

- Fixed the feedback panel closing unexpectedly when typing 'n' in the description field
修复了在描述字段中输入 'n' 时反馈面板意外关闭的问题

- Fixed rate limit warning appearing at low usage after weekly reset (now requires 70% usage)
修复了每周重置后在低使用量时出现速率限制警告的问题（现在需要 70% 的使用量）

- Fixed rate limit options menu incorrectly auto-opening when resuming a previous session
修复了恢复先前会话时速率限制选项菜单错误自动打开的问题

- Fixed numpad keys outputting escape sequences instead of characters in Kitty keyboard protocol terminals
修复了 Kitty 键盘协议终端中小键盘键输出转义序列而非字符的问题

- Fixed Option+Return not inserting newlines in Kitty keyboard protocol terminals
修复了 Kitty 键盘协议终端中 Option+Return 不插入换行符的问题

- Fixed corrupted config backup files accumulating in the home directory (now only one backup is created per config file)
修复了主目录中损坏的配置备份文件累积的问题（现在每个配置文件只创建一个备份）

- Fixed `mcp list` and `mcp get` commands leaving orphaned MCP server processes
修复了 `mcp list` 和 `mcp get` 命令留下孤立的 MCP 服务器进程的问题

- Fixed visual artifacts in ink2 mode when nodes become hidden via `display:none`
修复了当节点通过 `display:none` 隐藏时 ink2 模式中的视觉伪影

- Improved the external CLAUDE.md imports approval dialog to show which files are being imported and from where
改进了外部 CLAUDE.md 导入批准对话框，以显示正在导入哪些文件以及从哪里导入

- Improved the `/tasks` dialog to go directly to task details when there's only one background task running
改进了 `/tasks` 对话框，使其在只有一个后台任务运行时直接进入任务详细信息

- Improved @ autocomplete with icons for different suggestion types and single-line formatting
改进了 @ 自动完成，为不同的建议类型添加了图标并使用单行格式

- Updated "Help improve Claude" setting fetch to refresh OAuth and retry when it fails due to a stale OAuth token
更新了"帮助改进 Claude"设置获取，以在由于过时的 OAuth 令牌而失败时刷新 OAuth 并重试

- Changed task notification display to cap at 3 lines with overflow summary when multiple background tasks complete simultaneously
更改了任务通知显示，当多个后台任务同时完成时，最多显示 3 行并带有溢出摘要

- Changed terminal title to "Claude Code" on startup for better window identification
将启动时的终端标题更改为"Claude Code"，以便更好地识别窗口

- Removed ability to @-mention MCP servers to enable/disable - use `/mcp enable ` instead
移除了通过 @ 提及 MCP 服务器来启用/禁用的功能 - 请改用 `/mcp enable`

- [VSCode] Fixed usage indicator not updating after manual compact
[VSCode] 修复了手动压缩后使用指示器不更新的问题

## 2.1.5

- Added `CLAUDE_CODE_TMPDIR` environment variable to override the temp directory used for internal temp files, useful for environments with custom temp directory requirements
添加了 `CLAUDE_CODE_TMPDIR` 环境变量，用于覆盖内部临时文件使用的临时目录，适用于具有自定义临时目录要求的环境

## 2.1.4

- Added `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` environment variable to disable all background task functionality including auto-backgrounding and the Ctrl+B shortcut
添加了 `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` 环境变量，用于禁用所有后台任务功能，包括自动后台化和 Ctrl+B 快捷键

- Fixed "Help improve Claude" setting fetch to refresh OAuth and retry when it fails due to a stale OAuth token
修复了"帮助改进 Claude"设置获取，以在由于过时的 OAuth 令牌而失败时刷新 OAuth 并重试

## 2.1.3

- Merged slash commands and skills, simplifying the mental model with no change in behavior
合并了斜杠命令和技能，简化了思维模型，但行为没有变化

- Added release channel (`stable` or `latest`) toggle to `/config`
为 `/config` 添加了发布通道（`stable` 或 `latest`）切换

- Added detection and warnings for unreachable permission rules, with warnings in `/doctor` and after saving rules that include the source of each rule and actionable fix guidance
添加了无法访问的权限规则的检测和警告，在 `/doctor` 中以及保存规则后显示警告，其中包括每个规则的来源和可操作的修复指导

- Fixed plan files persisting across `/clear` commands, now ensuring a fresh plan file is used after clearing a conversation
修复了计划文件在 `/clear` 命令之间持久化的问题，现在确保清除对话后使用新的计划文件

- Fixed false skill duplicate detection on filesystems with large inodes (e.g., ExFAT) by using 64-bit precision for inode values
通过使用 64 位精度的 inode 值，修复了具有大 inode 的文件系统（例如 ExFAT）上的虚假技能重复检测

- Fixed mismatch between background task count in status bar and items shown in tasks dialog
修复了状态栏中的后台任务计数与任务对话框中显示的项目之间的不匹配

- Fixed sub-agents using the wrong model during conversation compaction
修复了子代理在对话压缩期间使用错误模型的问题

- Fixed web search in sub-agents using incorrect model
修复了子代理中的网络搜索使用错误模型的问题

- Fixed trust dialog acceptance when running from the home directory not enabling trust-requiring features like hooks during the session
修复了从主目录运行时信任对话框接受未在会话期间启用需要信任的功能（如 hooks）的问题

- Improved terminal rendering stability by preventing uncontrolled writes from corrupting cursor state
通过防止不受控制的写入破坏光标状态，改进了终端渲染稳定性

- Improved slash command suggestion readability by truncating long descriptions to 2 lines
通过将长描述截断为 2 行，改进了斜杠命令建议的可读性

- Changed tool hook execution timeout from 60 seconds to 10 minutes
将工具 hook 执行超时从 60 秒更改为 10 分钟

- [VSCode] Added clickable destination selector for permission requests, allowing you to choose where settings are saved (this project, all projects, shared with team, or session only)
[VSCode] 为权限请求添加了可点击的目标选择器，允许您选择设置保存的位置（此项目、所有项目、与团队共享或仅会话）

## 2.1.2

- Added source path metadata to images dragged onto the terminal, helping Claude understand where images originated
为拖动到终端的图像添加了源路径元数据，帮助 Claude 了解图像的来源

- Added clickable hyperlinks for file paths in tool output in terminals that support OSC 8 (like iTerm)
在支持 OSC 8 的终端（如 iTerm）中为工具输出中的文件路径添加了可点击的超链接

- Added support for Windows Package Manager (winget) installations with automatic detection and update instructions
添加了对 Windows Package Manager (winget) 安装的支持，包括自动检测和更新说明

- Added Shift+Tab keyboard shortcut in plan mode to quickly select "auto-accept edits" option
在计划模式中添加了 Shift+Tab 键盘快捷键，用于快速选择"自动接受编辑"选项

- Added `FORCE_AUTOUPDATE_PLUGINS` environment variable to allow plugin autoupdate even when the main auto-updater is disabled
添加了 `FORCE_AUTOUPDATE_PLUGINS` 环境变量，用于在主自动更新程序被禁用时允许插件自动更新

- Added `agent_type` to SessionStart hook input, populated if `--agent` is specified
为 SessionStart hook 输入添加了 `agent_type`，如果指定了 `--agent` 则会填充

- Fixed a command injection vulnerability in bash command processing where malformed input could execute arbitrary commands
修复了 bash 命令处理中的命令注入漏洞，该漏洞可能导致格式错误的输入执行任意命令

- Fixed a memory leak where tree-sitter parse trees were not being freed, causing WASM memory to grow unbounded over long sessions
修复了 tree-sitter 解析树未释放的内存泄漏问题，导致 WASM 内存在长时间会话中无限制增长

- Fixed binary files (images, PDFs, etc.) being accidentally included in memory when using `@include` directives in CLAUDE.md files
修复了在 CLAUDE.md 文件中使用 `@include` 指令时二进制文件（图像、PDF 等）意外包含在内存中的问题

- Fixed updates incorrectly claiming another installation is in progress
修复了更新错误地声称另一个安装正在进行的问题

- Fixed crash when socket files exist in watched directories (defense-in-depth for EOPNOTSUPP errors)
修复了监视目录中存在套接字文件时的崩溃问题（EOPNOTSUPP 错误的深度防御）

- Fixed remote session URL and teleport being broken when using `/tasks` command
修复了使用 `/tasks` 命令时远程会话 URL 和传送失效的问题

- Fixed MCP tool names being exposed in analytics events by sanitizing user-specific server configurations
通过清理用户特定的服务器配置，修复了分析事件中暴露 MCP 工具名称的问题

- Improved Option-as-Meta hint on macOS to show terminal-specific instructions for native CSIu terminals like iTerm2, Kitty, and WezTerm
改进了 macOS 上的 Option-as-Meta 提示，为原生 CSIu 终端（如 iTerm2、Kitty 和 WezTerm）显示特定于终端的说明

- Improved error message when pasting images over SSH to suggest using `scp` instead of the unhelpful clipboard shortcut hint
改进了通过 SSH 粘贴图像时的错误消息，建议使用 `scp` 而不是无用的剪贴板快捷键提示

- Improved permission explainer to not flag routine dev workflows (git fetch/rebase, npm install, tests, PRs) as medium risk
改进了权限说明器，不将常规开发工作流程（git fetch/rebase、npm install、测试、PR）标记为中等风险

- Changed large bash command outputs to be saved to disk instead of truncated, allowing Claude to read the full content
将大型 bash 命令输出更改为保存到磁盘而不是截断，允许 Claude 读取完整内容

- Changed large tool outputs to be persisted to disk instead of truncated, providing full output access via file references
将大型工具输出更改为持久化到磁盘而不是截断，通过文件引用提供完整的输出访问

- Changed `/plugins` installed tab to unify plugins and MCPs with scope-based grouping
更改了 `/plugins` 已安装选项卡，以统一插件和 MCP，并按范围分组

- Deprecated Windows managed settings path `C:\ProgramData\ClaudeCode\managed-settings.json` - administrators should migrate to `C:\Program Files\ClaudeCode\managed-settings.json`
弃用了 Windows 托管设置路径 `C:\ProgramData\ClaudeCode\managed-settings.json` - 管理员应迁移到 `C:\Program Files\ClaudeCode\managed-settings.json`

- [SDK] Changed minimum zod peer dependency to ^4.0.0
[SDK] 将最低 zod 对等依赖更改为 ^4.0.0

- [VSCode] Fixed usage display not updating after manual compact
[VSCode] 修复了手动压缩后使用显示不更新的问题

## 2.1.0

- Added automatic skill hot-reload - skills created or modified in `~/.claude/skills` or `.claude/skills` are now immediately available without restarting the session
添加了技能自动热重载功能 - 在 `~/.claude/skills` 或 `.claude/skills` 中创建或修改的技能现在立即可用，无需重新启动会话

- Added support for running skills and slash commands in a forked sub-agent context using `context: fork` in skill frontmatter
添加了在分支子代理上下文中运行技能和斜杠命令的支持，通过在技能 frontmatter 中使用 `context: fork`

- Added support for `agent` field in skills to specify agent type for execution
添加了技能中的 `agent` 字段支持，用于指定执行的代理类型

- Added `language` setting to configure Claude's response language (e.g., language: "japanese")
添加了 `language` 设置以配置 Claude 的响应语言（例如，language: "japanese"）

- Changed Shift+Enter to work out of the box in iTerm2, WezTerm, Ghostty, and Kitty without modifying terminal configs
更改了 Shift+Enter，使其在 iTerm2、WezTerm、Ghostty 和 Kitty 中开箱即用，无需修改终端配置

- Added `respectGitignore` support in `settings.json` for per-project control over @-mention file picker behavior
在 `settings.json` 中添加了 `respectGitignore` 支持，用于每个项目对 @ 提及文件选择器行为的控制

- Added `IS_DEMO` environment variable to hide email and organization from the UI, useful for streaming or recording sessions
添加了 `IS_DEMO` 环境变量以在 UI 中隐藏电子邮件和组织，用于流式传输或录制会话

- Fixed security issue where sensitive data (OAuth tokens, API keys, passwords) could be exposed in debug logs
修复了敏感数据（OAuth 令牌、API 密钥、密码）可能在调试日志中暴露的安全问题

- Fixed files and skills not being properly discovered when resuming sessions with `-c` or `--resume`
修复了使用 `-c` 或 `--resume` 恢复会话时文件和技能未正确发现的问题

- Fixed pasted content being lost when replaying prompts from history using up arrow or Ctrl+R search
修复了使用向上箭头或 Ctrl+R 搜索从历史记录重放提示时粘贴内容丢失的问题

- Fixed Esc key with queued prompts to only move them to input without canceling the running task
修复了 Esc 键在排队提示时仅将它们移动到输入而不取消正在运行的任务的问题

- Reduced permission prompts for complex bash commands
减少了复杂 bash 命令的权限提示

- Fixed command search to prioritize exact and prefix matches on command names over fuzzy matches in descriptions
修复了命令搜索以优先考虑命令名称的精确匹配和前缀匹配，而不是描述中的模糊匹配

- Fixed PreToolUse hooks to allow `updatedInput` when returning `ask` permission decision, enabling hooks to act as middleware while still requesting user consent
修复了 PreToolUse hooks 在返回 `ask` 权限决策时允许 `updatedInput`，使 hooks 可以充当中间件同时仍然请求用户同意

- Fixed plugin path resolution for file-based marketplace sources
修复了基于文件的市场place源的插件路径解析

- Fixed LSP tool being incorrectly enabled when no LSP servers were configured
修复了未配置 LSP 服务器时错误启用 LSP 工具的问题

- Fixed background tasks failing with "git repository not found" error for repositories with dots in their names
修复了名称中包含点的存储库的后台任务因"git repository not found"错误而失败的问题

- Fixed Claude in Chrome support for WSL environments
修复了 WSL 环境的 Claude in Chrome 支持

- Fixed Windows native installer silently failing when executable creation fails
修复了 Windows 本机安装程序在可执行文件创建时静默失败的问题

- Improved CLI help output to display options and subcommands in alphabetical order for easier navigation
改进了 CLI 帮助输出，按字母顺序显示选项和子命令以便于导航

- Added wildcard pattern matching for Bash tool permissions using `*` at any position in rules (e.g., `Bash(npm *)`, `Bash(* install)`, `Bash(git * main)`)
为 Bash 工具权限添加了通配符模式匹配，在规则的任何位置使用 `*`（例如，`Bash(npm *)`、`Bash(* install)`、`Bash(git * main)`）

- Added unified Ctrl+B backgrounding for both bash commands and agents - pressing Ctrl+B now backgrounds all running foreground tasks simultaneously
为 bash 命令和代理添加了统一的 Ctrl+B 后台化 - 按 Ctrl+B 现在同时将所有正在运行的前台任务后台化

- Added support for MCP `list_changed` notifications, allowing MCP servers to dynamically update their available tools, prompts, and resources without requiring reconnection
添加了对 MCP `list_changed` 通知的支持，允许 MCP 服务器动态更新其可用工具、提示和资源，而无需重新连接

- Added `/teleport` and `/remote-env` slash commands for claude.ai subscribers, allowing them to resume and configure remote sessions
为 claude.ai 订阅者添加了 `/teleport` 和 `/remote-env` 斜杠命令，允许他们恢复和配置远程会话

- Added support for disabling specific agents using `Task(AgentName)` syntax in settings.json permissions or the `--disallowedTools` CLI flag
添加了使用 settings.json 权限中的 `Task(AgentName)` 语法或 `--disallowedTools` CLI 标志禁用特定代理的支持

- Added hooks support to agent frontmatter, allowing agents to define PreToolUse, PostToolUse, and Stop hooks scoped to the agent's lifecycle
向 agent frontmatter 添加了 hooks 支持，允许代理定义限定于代理生命周期的 PreToolUse、PostToolUse 和 Stop hooks

- Added hooks support for skill and slash command frontmatter
添加了对 skill 和斜杠命令 frontmatter 的 hooks 支持

- Added new Vim motions: `;` and `,` to repeat f/F/t/T motions, `y` operator for yank with `yy`/`Y`, `p`/`P` for paste, text objects (`iw`, `aw`, `iW`, `aW`, `i"`, `a"`, `i'`, `a'`, `i(`, `a(`, `i[`, `a[`, `i{`, `a{`), `>>` and `<<` for indent/dedent, and `J` to join lines
添加了新的 Vim 动作：`;` 和 `,` 重复 f/F/t/T 动作，`y` 操作符用于复制（yy/Y），`p`/`P` 用于粘贴，文本对象（`iw`、`aw`、`iW`、`aW`、`i"`、`a"`、`i'`、`a'`、`i(`、`a(`、`i[`、`a[`、`i{`、`a{`），`>>` 和 `<<` 用于缩进/取消缩进，以及 `J` 连接行

- Added `/plan` command shortcut to enable plan mode directly from the prompt
添加了 `/plan` 命令快捷键，可直接从提示启用计划模式

- Added slash command autocomplete support when `/` appears anywhere in input, not just at the beginning
添加了斜杠命令自动完成支持，当 `/` 出现在输入的任何位置时，而不仅仅是在开头

- Added `--tools` flag support in interactive mode to restrict which built-in tools Claude can use during interactive sessions
在交互模式中添加了 `--tools` 标志支持，以限制 Claude 在交互会话期间可以使用的内置工具

- Added `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` environment variable to override the default file read token limit
添加了 `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` 环境变量以覆盖默认文件读取令牌限制

- Added support for `once: true` config for hooks
添加了对 hooks 的 `once: true` 配置支持

- Added support for YAML-style lists in frontmatter `allowed-tools` field for cleaner skill declarations
在 frontmatter `allowed-tools` 字段中添加了对 YAML 样式列表的支持，以实现更清晰的技能声明

- Added support for prompt and agent hook types from plugins (previously only command hooks were supported)
添加了对来自插件的 prompt 和 agent hook 类型的支持（以前仅支持 command hooks）

- Added Cmd+V support for image paste in iTerm2 (maps to Ctrl+V)
在 iTerm2 中添加了 Cmd+V 图像粘贴支持（映射到 Ctrl+V）

- Added left/right arrow key navigation for cycling through tabs in dialogs
添加了左右箭头键导航，用于在对话框中循环浏览选项卡

- Added real-time thinking block display in Ctrl+O transcript mode
在 Ctrl+O 记录模式中添加了实时思考块显示

- Added filepath to full output in background bash task details dialog
在后台 bash 任务详细信息对话框的完整输出中添加了文件路径

- Added Skills as a separate category in the context visualization
在上下文可视化中添加了技能作为单独类别

- Fixed OAuth token refresh not triggering when server reports token expired but local expiration check disagrees
修复了服务器报告令牌已过期但本地过期检查不一致时 OAuth 令牌刷新未触发的问题

- Fixed session persistence getting stuck after transient server errors by recovering from 409 conflicts when the entry was actually stored
通过在条目实际存储时从 409 冲突中恢复，修复了短暂服务器错误后会话持久化卡住的问题

- Fixed session resume failures caused by orphaned tool results during concurrent tool execution
修复了并发工具执行期间孤立工具结果导致的会话恢复失败

- Fixed a race condition where stale OAuth tokens could be read from the keychain cache during concurrent token refresh attempts
修复了并发令牌刷新期间可能从钥匙串缓存读取过期 OAuth 令牌的竞争条件

- Fixed AWS Bedrock subagents not inheriting EU/APAC cross-region inference model configuration, causing 403 errors when IAM permissions are scoped to specific regions
修复了 AWS Bedrock 子代理未继承 EU/APAC 跨区域推理模型配置，导致 IAM 权限限定于特定区域时出现 403 错误的问题

- Fixed API context overflow when background tasks produce large output by truncating to 30K chars with file path reference
通过截断到 30K 字符并包含文件路径引用，修复了后台任务产生大输出时的 API 上下文溢出

- Fixed a hang when reading FIFO files by skipping symlink resolution for special file types
通过跳过特殊文件类型的符号链接解析，修复了读取 FIFO 文件时的挂起

- Fixed terminal keyboard mode not being reset on exit in Ghostty, iTerm2, Kitty, and WezTerm
修复了 Ghostty、iTerm2、Kitty 和 WezTerm 中退出时未重置终端键盘模式的问题

- Fixed Alt+B and Alt+F (word navigation) not working in iTerm2, Ghostty, Kitty, and WezTerm
修复了 iTerm2、Ghostty、Kitty 和 WezTerm 中 Alt+B 和 Alt+F（单词导航）不起作用的问题

- Fixed `${CLAUDE_PLUGIN_ROOT}` not being substituted in plugin `allowed-tools` frontmatter, which caused tools to incorrectly require approval
修复了插件 `allowed-tools` frontmatter 中未替换 `${CLAUDE_PLUGIN_ROOT}` 的问题，该问题导致工具错误地需要批准

- Fixed files created by the Write tool using hardcoded 0o600 permissions instead of respecting the system umask
修复了 Write 工具创建的文件使用硬编码的 0o600 权限而不是尊重系统 umask 的问题

- Fixed commands with `$()` command substitution failing with parse errors
修复了带有 `$()` 命令替换的命令因解析错误而失败的问题

- Fixed multi-line bash commands with backslash continuations being incorrectly split and flagged for permissions
修复了带反斜杠续行的多行 bash 命令被错误拆分和标记权限的问题

- Fixed bash command prefix extraction to correctly identify subcommands after global options (e.g., `git -C /path log` now correctly matches `Bash(git log:*)` rules)
修复了 bash 命令前缀提取以在全局选项之后正确识别子命令（例如，`git -C /path log` 现在正确匹配 `Bash(git log:*)` 规则）

- Fixed slash commands passed as CLI arguments (e.g., `claude /context`) not being executed properly
修复了作为 CLI 参数传递的斜杠命令（例如，`claude /context`）未正确执行的问题

- Fixed pressing Enter after Tab-completing a slash command selecting a different command instead of submitting the completed one
修复了 Tab 完成斜杠命令后按 Enter 选择不同命令而不是提交已完成命令的问题

- Fixed slash command argument hint flickering and inconsistent display when typing commands with arguments
修复了输入带参数的命令时斜杠命令参数提示闪烁和显示不一致的问题

- Fixed Claude sometimes redundantly invoking the Skill tool when running slash commands directly
修复了 Claude 在直接运行斜杠命令时有时冗余调用 Skill 工具的问题

- Fixed skill token estimates in `/context` to accurately reflect frontmatter-only loading
修复了 `/context` 中的技能令牌估计以准确反映仅 frontmatter 加载

- Fixed subagents sometimes not inheriting the parent's model by default
修复了子代理有时默认不继承父代理模型的问题

- Fixed model picker showing incorrect selection for Bedrock/Vertex users using `--model haiku`
修复了使用 `--model haiku` 的 Bedrock/Vertex 用户的模型选择器显示错误选择的问题

- Fixed duplicate Bash commands appearing in permission request option labels
修复了权限请求选项标签中出现重复 Bash 命令的问题

- Fixed noisy output when background tasks complete - now shows clean completion message instead of raw output
修复了后台任务完成时的嘈杂输出 - 现在显示干净的完成消息而不是原始输出

- Fixed background task completion notifications to appear proactively with bullet point
修复了后台任务完成通知主动显示并带有项目符号

- Fixed forked slash commands showing "AbortError" instead of "Interrupted" message when cancelled
修复了分支斜杠命令在取消时显示"AbortError"而不是"Interrupted"消息的问题

- Fixed cursor disappearing after dismissing permission dialogs
修复了关闭权限对话框后光标消失的问题

- Fixed `/hooks` menu selecting wrong hook type when scrolling to a different option
修复了滚动到不同选项时 `/hooks` 菜单选择错误 hook 类型的问题

- Fixed images in queued prompts showing as "[object Object]" when pressing Esc to cancel
修复了按 Esc 取消时排队提示中的图像显示为"[object Object]"的问题

- Fixed images being silently dropped when queueing messages while backgrounding a task
修复了后台任务时排队消息时图像被静默丢弃的问题

- Fixed large pasted images failing with "Image was too large" error
修复了大粘贴图像因"图像太大"错误而失败的问题

- Fixed extra blank lines in multiline prompts containing CJK characters (Japanese, Chinese, Korean)
修复了包含中日韩（CJK）字符（日语、中文、韩语）的多行提示中的额外空行

- Fixed ultrathink keyword highlighting being applied to wrong characters when user prompt text wraps to multiple lines
修复了用户提示文本换行到多行时 ultrathink 关键字高亮应用于错误字符的问题

- Fixed collapsed "Reading X files…" indicator incorrectly switching to past tense when thinking blocks appear mid-stream
修复了当思考块出现在流中间时折叠的"Reading X files…"指示器错误地切换到过去时的问题

- Fixed Bash read commands (like `ls` and `cat`) not being counted in collapsed read/search groups, causing groups to incorrectly show "Read 0 files"
修复了 Bash 读取命令（如 `ls` 和 `cat`）未在折叠读取/搜索组中计数，导致组错误显示"Read 0 files"的问题

- Fixed spinner token counter to properly accumulate tokens from subagents during execution
修复了旋转器令牌计数器以在执行期间正确累积来自子代理的令牌

- Fixed memory leak in git diff parsing where sliced strings retained large parent strings
修复了 git diff 解析中的内存泄漏，其中切片字符串保留了大的父字符串

- Fixed race condition where LSP tool could return "no server available" during startup
修复了启动期间 LSP 工具可能返回"no server available"的竞争条件

- Fixed feedback submission hanging indefinitely when network requests timeout
修复了网络请求超时时反馈提交无限期挂起的问题

- Fixed search mode in plugin discovery and log selector views exiting when pressing up arrow
修复了插件发现和日志选择器视图中的搜索模式在按向上箭头时退出的问题

- Fixed hook success message showing trailing colon when hook has no output
修复了 hook 没有输出时成功消息显示尾随冒号的问题

- Multiple optimizations to improve startup performance
多项优化以提高启动性能

- Improved terminal rendering performance when using native installer or Bun, especially for text with emoji, ANSI codes, and Unicode characters
使用本机安装程序或 Bun 时改进终端渲染性能，特别是对于带有表情符号、ANSI 代码和 Unicode 字符的文本

- Improved performance when reading Jupyter notebooks with many cells
改进了读取具有许多单元格的 Jupyter 笔记本时的性能

- Improved reliability for piped input like `cat refactor.md | claude`
改进了管道输入（如 `cat refactor.md | claude`）的可靠性

- Improved reliability for AskQuestion tool
改进了 AskQuestion 工具的可靠性

- Improved sed in-place edit commands to render as file edits with diff preview
改进了 sed 就地编辑命令以呈现为带有差异预览的文件编辑

- Improved Claude to automatically continue when response is cut off due to output token limit, instead of showing an error message
改进了 Claude 在因输出令牌限制导致响应被切断时自动继续，而不是显示错误消息

- Improved compaction reliability
改进了压缩可靠性

- Improved subagents (Task tool) to continue working after permission denial, allowing them to try alternative approaches
改进了子代理（Task 工具）以在权限拒绝后继续工作，允许它们尝试替代方法

- Improved skills to show progress while executing, displaying tool uses as they happen
改进了技能以在执行时显示进度，显示正在发生的工具使用

- Improved skills from `/skills/` directories to be visible in the slash command menu by default (opt-out with `user-invocable: false` in frontmatter)
改进了来自 `/skills/` 目录的技能默认情况下在斜杠命令菜单中可见（在 frontmatter 中使用 `user-invocable: false` 选择退出）

- Improved skill suggestions to prioritize recently and frequently used skills
改进了技能建议以优先考虑最近和经常使用的技能

- Improved spinner feedback when waiting for the first response token
改进了等待第一个响应令牌时的旋转器反馈

- Improved token count display in spinner to include tokens from background agents
改进了旋转器中的令牌计数显示以包括来自后台代理的令牌

- Improved incremental output for async agents to give the main thread more control and visibility
改进了异步代理的增量输出，以为主线程提供更多控制和可见性

- Improved permission prompt UX with Tab hint moved to footer, cleaner Yes/No input labels with contextual placeholders
改进了权限提示 UX，Tab 提示移至页脚，更清晰的 Yes/No 输入标签带有上下文占位符

- Improved the Claude in Chrome notification with shortened help text and persistent display until dismissed
改进了 Claude in Chrome 通知，具有缩短的帮助文本并持续显示直到被关闭

- Improved macOS screenshot paste reliability with TIFF format support
通过支持 TIFF 格式改进了 macOS 截图粘贴可靠性

- Improved `/stats` output
改进了 `/stats` 输出

- Updated Atlassian MCP integration to use a more reliable default configuration (streamable HTTP)
更新了 Atlassian MCP 集成以使用更可靠的默认配置（可流式 HTTP）

- Changed "Interrupted" message color from red to grey for a less alarming appearance
将"Interrupted"消息颜色从红色更改为灰色，以减少 alarming 的外观

- Removed permission prompt when entering plan mode - users can now enter plan mode without approval
删除了进入计划模式时的权限提示 - 用户现在可以未经批准进入计划模式

- Removed underline styling from image reference links
从图像引用链接中删除了下划线样式

- [SDK] Changed minimum zod peer dependency to ^4.0.0
[SDK] 将最小 zod 对等依赖更改为 ^4.0.0

- [VSCode] Added currently selected model name to the context menu
[VSCode] 在上下文菜单中添加了当前选择的模型名称

- [VSCode] Added descriptive labels on auto-accept permission button (e.g., "Yes, allow npm for this project" instead of "Yes, and don't ask again")
[VSCode] 在自动接受权限按钮上添加了描述性标签（例如，"Yes, allow npm for this project"而不是"Yes, and don't ask again"）

- [VSCode] Fixed paragraph breaks not rendering in markdown content
[VSCode] 修复了 markdown 内容中段落换行未渲染的问题

- [VSCode] Fixed scrolling in the extension inadvertently scrolling the parent iframe
[VSCode] 修复了扩展中的滚动意外滚动父 iframe 的问题

- [Windows] Fixed issue with improper rendering
[Windows] 修复了渲染不正确的问题

## 2.0.76

- Fixed issue with macOS code-sign warning when using Claude in Chrome integration
修复了在使用 Claude in Chrome 集成时 macOS 代码签名警告的问题

## 2.0.75

- Minor bugfixes
小错误修复

## 2.0.74

- Added LSP (Language Server Protocol) tool for code intelligence features like go-to-definition, find references, and hover documentation
添加了 LSP（语言服务器协议）工具，用于代码智能功能，如转到定义、查找引用和悬停文档

- Added `/terminal-setup` support for Kitty, Alacritty, Zed, and Warp terminals
添加了 `/terminal-setup` 对 Kitty、Alacritty、Zed 和 Warp 终端的支持

- Added ctrl+t shortcut in `/theme` to toggle syntax highlighting on/off
在 `/theme` 中添加了 ctrl+t 快捷键以切换语法高亮开/关

- Added syntax highlighting info to theme picker
向主题选择器添加了语法高亮信息

- Added guidance for macOS users when Alt shortcuts fail due to terminal configuration
为 macOS 用户添加了当 Alt 快捷键因终端配置而失败时的指导

- Fixed skill `allowed-tools` not being applied to tools invoked by the skill
修复了技能的 `allowed-tools` 未应用于技能调用的工具的问题

- Fixed Opus 4.5 tip incorrectly showing when user was already using Opus
修复了当用户已在使用 Opus 时错误显示 Opus 4.5 提示的问题

- Fixed a potential crash when syntax highlighting isn't initialized correctly
修复了语法高亮未正确初始化时可能的崩溃问题

- Fixed visual bug in `/plugins discover` where list selection indicator showed while search box was focused
修复了 `/plugins discover` 中搜索框获焦时列表选择指示器仍显示的视觉错误

- Fixed macOS keyboard shortcuts to display 'opt' instead of 'alt'
修复了 macOS 键盘快捷键显示 'opt' 而不是 'alt'

- Improved `/context` command visualization with grouped skills and agents by source, slash commands, and sorted token count
改进了 `/context` 命令的视觉显示，按来源、技能和代理分组，斜杠命令，并按令牌计数排序

- [Windows] Fixed issue with improper rendering
[Windows] 修复了渲染不正确的问题

- [VSCode] Added gift tag pictogram for year-end promotion message
[VSCode] 为年终促销消息添加了礼物标签图形

## 2.0.73

- Added clickable `[Image #N]` links that open attached images in the default viewer
添加了可点击的 `[Image #N]` 链接，可在默认查看器中打开附加图像

- Added alt-y yank-pop to cycle through kill ring history after ctrl-y yank
添加了 alt-y yank-pop，用于在 ctrl-y yank 后循环浏览 kill ring 历史记录

- Added search filtering to the plugin discover screen (type to filter by name, description, or marketplace)
在插件发现屏幕添加了搜索过滤功能（按名称、描述或市场进行过滤）

- Added support for custom session IDs when forking sessions with `--session-id` combined with `--resume` or `--continue` and `--fork-session`
添加了在使用 `--session-id` 结合 `--resume` 或 `--continue` 和 `--fork-session` 分支会话时支持自定义会话 ID

- Fixed slow input history cycling and race condition that could overwrite text after message submission
修复了输入历史循环缓慢以及可能导致消息提交后文本覆盖的竞争条件

- Improved `/theme` command to open theme picker directly
改进了 `/theme` 命令以直接打开主题选择器

- Improved theme picker UI
改进了主题选择器 UI

- Improved search UX across resume session, permissions, and plugins screens with a unified SearchBox component
通过统一的 SearchBox 组件改进了恢复会话、权限和插件屏幕的搜索体验

- [VSCode] Added tab icon badges showing pending permissions (blue) and unread completions (orange)
[VSCode] 添加了显示待处理权限（蓝色）和未读完成（橙色）的选项卡图标徽章

## 2.0.72

- Added Claude in Chrome (Beta) feature that works with the Chrome extension (https://claude.ai/chrome) to let you control your browser directly from Claude Code
添加了 Claude in Chrome（Beta）功能，可与 Chrome 扩展程序（https://claude.ai/chrome）配合使用，让您直接从 Claude Code 控制浏览器

- Reduced terminal flickering
减少了终端闪烁

- Added scannable QR code to mobile app tip for quick app downloads
在移动应用提示中添加了可扫描的二维码以便快速下载应用

- Added loading indicator when resuming conversations for better feedback
在恢复对话时添加了加载指示器以提供更好的反馈

- Fixed `/context` command not respecting custom system prompts in non-interactive mode
修复了 `/context` 命令在非交互模式下不尊重自定义系统提示的问题

- Fixed order of consecutive Ctrl+K lines when pasting with Ctrl+Y
修复了使用 Ctrl+Y 粘贴时连续 Ctrl+K 行的顺序问题

- Improved @ mention file suggestion speed (~3x faster in git repositories)
改进了 @ 提及文件建议速度（在 git 仓库中快约 3 倍）

- Improved file suggestion performance in repos with `.ignore` or `.rgignore` files
改进了具有 `.ignore` 或 `.rgignore` 文件的仓库中的文件建议性能

- Improved settings validation errors to be more prominent
改进了设置验证错误，使其更加突出

- Changed thinking toggle from Tab to Alt+T to avoid accidental triggers
将思考切换从 Tab 改为 Alt+T 以避免意外触发

## 2.0.71

- Added /config toggle to enable/disable prompt suggestions
添加了 /config 切换以启用/禁用提示建议

- Added `/settings` as an alias for the `/config` command
添加了 `/settings` 作为 `/config` 命令的别名

- Fixed @ file reference suggestions incorrectly triggering when cursor is in the middle of a path
修复了当光标在路径中间时 @ 文件引用建议错误触发的问题

- Fixed MCP servers from `.mcp.json` not loading when using `--dangerously-skip-permissions`
修复了使用 `--dangerously-skip-permissions` 时 `.mcp.json` 中的 MCP 服务器不加载的问题

- Fixed permission rules incorrectly rejecting valid bash commands containing shell glob patterns (e.g., `ls *.txt`, `for f in *.png`)
修复了权限规则错误拒绝包含 shell glob 模式的有效 bash 命令的问题（例如 `ls *.txt`、`for f in *.png`）

- Bedrock: Environment variable `ANTHROPIC_BEDROCK_BASE_URL` is now respected for token counting and inference profile listing
Bedrock：环境变量 `ANTHROPIC_BEDROCK_BASE_URL` 现在在令牌计数和推理配置文件列表中被尊重

- New syntax highlighting engine for native build
本机构建的新语法高亮引擎

## 2.0.70

- Added Enter key to accept and submit prompt suggestions immediately (tab still accepts for editing)
添加了 Enter 键以立即接受并提交提示建议（Tab 键仍然接受用于编辑）

- Added wildcard syntax `mcp__server__*` for MCP tool permissions to allow or deny all tools from a server
为 MCP 工具权限添加了通配符语法 `mcp__server__*`，以允许或拒绝来自服务器的所有工具

- Added auto-update toggle for plugin marketplaces, allowing per-marketplace control over automatic updates
为插件市场places添加了自动更新切换，允许每个市场单独控制自动更新

- Added `plan_mode_required` spawn parameter for teammates to require plan approval before implementing changes
为队友添加了 plan_mode_required 生成参数，要求在实施更改前获得计划批准

- Added `current_usage` field to status line input, enabling accurate context window percentage calculations
在状态行输入中添加了 current_usage 字段，能够准确计算上下文窗口百分比

- Fixed input being cleared when processing queued commands while the user was typing
修复了在处理排队命令时用户正在输入导致输入被清除的问题

- Fixed prompt suggestions replacing typed input when pressing Tab
修复了按 Tab 键时提示建议替换已输入内容的问题

- Fixed diff view not updating when terminal is resized
修复了终端调整大小时差异视图不更新的问题

- Improved memory usage by 3x for large conversations
将大型对话的内存使用量减少了 3 倍

- Improved resolution of stats screenshots copied to clipboard (Ctrl+S) for crisper images
改进了复制到剪贴板的统计截图（Ctrl+S）的分辨率，使图像更清晰

- Removed # shortcut for quick memory entry (tell Claude to edit your CLAUDE.md instead)
移除了 # 快速记忆条目快捷键（改为告诉 Claude 编辑您的 CLAUDE.md）

- Fix thinking mode toggle in /config not persisting correctly
修复 /config 中思考模式切换无法正确保持的问题

- Improve UI for file creation permission dialog
改进了文件创建权限对话框的 UI

## 2.0.69

- Minor bugfixes
小错误修复

## 2.0.68

- Fixed IME (Input Method Editor) support for languages like Chinese, Japanese, and Korean by correctly positioning the composition window at the cursor
修复了中文、日文、韩文等语言的输入法（IME）支持，通过将组合窗口正确定位在光标处

- Fixed a bug where disallowed MCP tools were visible to the model
修复了被禁止的 MCP 工具对模型可见的错误

- Fixed an issue where steering messages could be lost while a subagent is working
修复了子代理工作期间可能导致引导消息丢失的问题

- Fixed Option+Arrow word navigation treating entire CJK (Chinese, Japanese, Korean) text sequences as a single word instead of navigating by word boundaries
修复了 Option+箭头单词导航将整个中日韩（CJK）文本序列视为单个单词而不是按单词边界导航的问题

- Improved plan mode exit UX: show simplified yes/no dialog when exiting with empty or missing plan instead of throwing an error
改进了计划模式退出体验：当计划为空或缺失时退出时，显示简化的"是/否"对话框而不是抛出错误

- Add support for enterprise managed settings. Contact your Anthropic account team to enable this feature.
添加对企业托管设置的支持。请联系您的 Anthropic 账户团队以启用此功能。

## 2.0.67

- Thinking mode is now enabled by default for Opus 4.5
Opus 4.5 现在默认启用思考模式

- Thinking mode configuration has moved to /config
思考模式配置已移至 /config

- Added search functionality to `/permissions` command with `/` keyboard shortcut for filtering rules by tool name
为 `/permissions` 命令添加搜索功能，使用 `/` 键盘快捷键按工具名称过滤规则

- Show reason why autoupdater is disabled in `/doctor`
在 `/doctor` 中显示自动更新程序被禁用的原因

- Fixed false "Another process is currently updating Claude" error when running `claude update` while another instance is already on the latest version
修复了在另一个实例已是最新版本时运行 `claude update` 出现虚假的"另一个进程正在更新 Claude"错误

- Fixed MCP servers from `.mcp.json` being stuck in pending state when running in non-interactive mode (`-p` flag or piped input)
修复了在非交互模式（`-p` 标志或管道输入）下运行时，`.mcp.json` 中的 MCP 服务器卡在待处理状态的问题

- Fixed scroll position resetting after deleting a permission rule in `/permissions`
修复了在 `/permissions` 中删除权限规则后滚动位置重置的问题

- Fixed word deletion (opt+delete) and word navigation (opt+arrow) not working correctly with non-Latin text such as Cyrillic, Greek, Arabic, Hebrew, Thai, and Chinese
修复了单词删除（opt+delete）和单词导航（opt+arrow）在西里尔文、希腊文、阿拉伯文、希伯来文、泰文和中文等非拉丁文本中无法正常工作的问题

- Fixed `claude install --force` not bypassing stale lock files
修复了 `claude install --force` 无法绕过过时锁文件的问题

- Fixed consecutive @~/ file references in CLAUDE.md being incorrectly parsed due to markdown strikethrough interference
修复了由于 markdown 删除线干扰，CLAUDE.md 中连续的 @~/ 文件引用被错误解析的问题

- Windows: Fixed plugin MCP servers failing due to colons in log directory paths
Windows：修复了由于日志目录路径中的冒号导致插件 MCP 服务器失败的问题

## 2.0.65

- Added ability to switch models while writing a prompt using alt+p (linux, windows), option+p (macos).
添加了在编写提示时使用 alt+p（Linux、Windows）或 option+p（macOS）切换模型的功能。

- Added context window information to status line input
向状态行输入添加上下文窗口信息

- Added `fileSuggestion` setting for custom `@` file search commands
添加了 `fileSuggestion` 设置用于自定义 `@` 文件搜索命令

- Added `CLAUDE_CODE_SHELL` environment variable to override automatic shell detection (useful when login shell differs from actual working shell)
添加了 `CLAUDE_CODE_SHELL` 环境变量以覆盖自动 shell 检测（当登录 shell 与实际工作 shell 不同时很有用）

- Fixed prompt not being saved to history when aborting a query with Escape
修复了使用 Escape 中止查询时提示未保存到历史记录的问题

- Fixed Read tool image handling to identify format from bytes instead of file extension
修复了 Read 工具图像处理，改为从字节而不是文件扩展名识别格式

## 2.0.64

- Made auto-compacting instant
使自动压缩即时生效

- Agents and bash commands can run asynchronously and send messages to wake up the main agent
代理和 bash 命令可以异步运行并发送消息来唤醒主代理

- /stats now provides users with interesting CC stats, such as favorite model, usage graph, usage streak
/stats 现在为用户提供有趣的 CC 统计信息，如最喜欢的模型、使用图表、使用连续记录

- Added named session support: use `/rename` to name sessions, `/resume <name>` in REPL or `claude --resume <name>` from the terminal to resume them
添加了命名会话支持：使用 `/rename` 为会话命名，在 REPL 中使用 `/resume <name>` 或从终端使用 `claude --resume <name>` 恢复它们

- Added support for .claude/rules/. See https://code.claude.com/docs/en/memory for details.
添加了对 .claude/rules/ 的支持。详细信息请参见 https://code.claude.com/docs/en/memory

- Added image dimension metadata when images are resized, enabling accurate coordinate mappings for large images
添加了图像调整大小时的尺寸元数据，为大图像启用精确的坐标映射

- Fixed auto-loading .env when using native installer
修复了使用本机安装程序时自动加载 .env 的问题

- Fixed `--system-prompt` being ignored when using `--continue` or `--resume` flags
修复了使用 `--continue` 或 `--resume` 标志时忽略 `--system-prompt` 的问题

- Improved `/resume` screen with grouped forked sessions and keyboard shortcuts for preview (P) and rename (R)
改进了 `/resume` 屏幕，包含分组的分支会话以及预览（P）和重命名（R）的键盘快捷键

- VSCode: Added copy-to-clipboard button on code blocks and bash tool inputs
VSCode：在代码块和 bash 工具输入上添加了复制到剪贴板按钮

- VSCode: Fixed extension not working on Windows ARM64 by falling back to x64 binary via emulation
VSCode：通过回退到 x64 二进制文件的模拟，修复了扩展在 Windows ARM64 上无法工作的问题

- Bedrock: Improve efficiency of token counting
Bedrock：提高令牌计数效率

- Bedrock: Add support for `aws login` AWS Management Console credentials
Bedrock：添加对 `aws login` AWS 管理控制台凭证的支持

- Unshipped AgentOutputTool and BashOutputTool, in favor of a new unified TaskOutputTool
未发布的 AgentOutputTool 和 BashOutputTool，改为支持新的统一 TaskOutputTool

## 2.0.62

- Added "(Recommended)" indicator for multiple-choice questions, with the recommended option moved to the top of the list
为多项选择题添加"(推荐)"指示器，并将推荐选项移至列表顶部

- Added `attribution` setting to customize commit and PR bylines (deprecates `includeCoAuthoredBy`)
添加了 `attribution` 设置以自定义提交和 PR 署名（废弃了 `includeCoAuthoredBy`）

- Fixed duplicate slash commands appearing when ~/.claude is symlinked to a project directory
修复了 ~/.claude 被符号链接到项目目录时出现重复斜杠命令的问题

- Fixed slash command selection not working when multiple commands share the same name
修复了多个命令共享相同名称时斜杠命令选择不起作用的问题

- Fixed an issue where skill files inside symlinked skill directories could become circular symlinks
修复了符号链接的技能目录内的技能文件可能成为循环符号链接的问题

- Fixed running versions getting removed because lock file incorrectly going stale
修复了由于锁文件错误过期导致正在运行的版本被删除的问题

- Fixed IDE diff tab not closing when rejecting file changes
修复了拒绝文件更改时 IDE 差异选项卡未关闭的问题

## 2.0.61

- Reverted VSCode support for multiple terminal clients due to responsiveness issues.
由于响应性问题，回滚了 VSCode 对多个终端客户端的支持。

## 2.0.60

- Added background agent support. Agents run in the background while you work
添加了后台代理支持。代理在您工作时在后台运行

- Added --disable-slash-commands CLI flag to disable all slash commands
添加了 --disable-slash-commands CLI 标志以禁用所有斜杠命令

- Added model name to "Co-Authored-By" commit messages
将模型名称添加到"Co-Authored-By"提交消息

- Enabled "/mcp enable [server-name]" or "/mcp disable [server-name]" to quickly toggle all servers
启用"/mcp enable [server-name]"或"/mcp disable [server-name]"以快速切换所有服务器

- Updated Fetch to skip summarization for pre-approved websites
更新了 Fetch，对预先批准的网站跳过摘要

- VSCode: Added support for multiple terminal clients connecting to the IDE server simultaneously
VSCode：添加了对多个终端客户端同时连接到 IDE 服务器的支持

## 2.0.59

- Added --agent CLI flag to override the agent setting for the current session
添加了 --agent CLI 标志以覆盖当前会话的代理设置

- Added `agent` setting to configure main thread with a specific agent's system prompt, tool restrictions, and model
添加了 `agent` 设置，以使用特定代理的系统提示、工具限制和模型配置主线程

- VS Code: Fixed .claude.json config file being read from incorrect location
VS Code：修复了从错误位置读取 .claude.json 配置文件的问题

## 2.0.58

- Pro users now have access to Opus 4.5 as part of their subscription!
Pro 用户现在可以通过订阅使用 Opus 4.5！

- Fixed timer duration showing "11m 60s" instead of "12m 0s"
修复了计时器持续时间显示"11m 60s"而不是"12m 0s"的问题

- Windows: Managed settings now prefer `C:\Program Files\ClaudeCode` if it exists. Support for `C:\ProgramData\ClaudeCode` will be removed in a future version.
Windows：托管设置现在优先使用 `C:\Program Files\ClaudeCode`（如果存在）。未来版本将取消对 `C:\ProgramData\ClaudeCode` 的支持。

## 2.0.57

- Added feedback input when rejecting plans, allowing users to tell Claude what to change
添加了拒绝计划时的反馈输入，允许用户告诉 Claude 需要更改什么

- VSCode: Added streaming message support for real-time response display
VSCode：添加了流式消息支持以实时显示响应

## 2.0.56

- Added setting to enable/disable terminal progress bar (OSC 9;4)
添加了启用/禁用终端进度条（OSC 9;4）的设置

- VSCode Extension: Added support for VS Code's secondary sidebar (VS Code 1.97+), allowing Claude Code to be displayed in the right sidebar while keeping the file explorer on the left. Requires setting sidebar as Preferred Location in the config.
VSCode 扩展：添加了对 VS Code 辅助侧边栏（VS Code 1.97+）的支持，允许 Claude Code 显示在右侧边栏，同时将文件资源管理器保留在左侧。需要在配置中将侧边栏设置为首选位置。

## 2.0.55

- Fixed proxy DNS resolution being forced on by default. Now opt-in via `CLAUDE_CODE_PROXY_RESOLVES_HOSTS=true` environment variable
修复了默认强制启用代理 DNS 解析的问题。现在通过 `CLAUDE_CODE_PROXY_RESOLVES_HOSTS=true` 环境变量选择启用

- Fixed keyboard navigation becoming unresponsive when holding down arrow keys in memory location selector
修复了在内存位置选择器中按住箭头键时键盘导航无响应的问题

- Improved AskUserQuestion tool to auto-submit single-select questions on the last question, eliminating the extra review screen for simple question flows
改进了 AskUserQuestion 工具，在最后一个问题时自动提交单选问题，消除了简单问题流程的额外审查屏幕

- Improved fuzzy matching for `@` file suggestions with faster, more accurate results
改进了 `@` 文件建议的模糊匹配，提供更快、更准确的结果

## 2.0.54

- Hooks: Enable PermissionRequest hooks to process 'always allow' suggestions and apply permission updates
Hooks：启用 PermissionRequest hooks 以处理"始终允许"建议并应用权限更新

- Fix issue with excessive iTerm notifications
修复 iTerm 通知过多的问题

## 2.0.52

- Fixed duplicate message display when starting Claude with a command line argument
修复了使用命令行参数启动 Claude 时出现重复消息显示的问题

- Fixed `/usage` command progress bars to fill up as usage increases (instead of showing remaining percentage)
修复了 `/usage` 命令进度条随使用增加而填充（而不是显示剩余百分比）的问题

- Fixed image pasting not working on Linux systems running Wayland (now falls back to wl-paste when xclip is unavailable)
修复了在运行 Wayland 的 Linux 系统上图像粘贴不起作用的问题（现在在 xclip 不可用时回退到 wl-paste）

- Permit some uses of `$!` in bash commands
允许在 bash 命令中使用某些 `$!`

## 2.0.51

- Added Opus 4.5! https://www.anthropic.com/news/claude-opus-4-5
添加了 Opus 4.5！https://www.anthropic.com/news/claude-opus-4-5

- Introducing Claude Code for Desktop: https://claude.com/download
推出 Claude Code 桌面版：https://claude.com/download

- To give you room to try out our new model, we've updated usage limits for Claude Code users. See the Claude Opus 4.5 blog for full details
为了给您空间试用我们的新模型，我们更新了 Claude Code 用户的使用限制。详细信息请参见 Claude Opus 4.5 博客

- Pro users can now purchase extra usage for access to Opus 4.5 in Claude Code
Pro 用户现在可以购买额外使用量以在 Claude Code 中使用 Opus 4.5

- Plan Mode now builds more precise plans and executes more thoroughly
计划模式现在构建更精确的计划并执行得更彻底

- Usage limit notifications now easier to understand
使用限制通知现在更容易理解

- Switched `/usage` back to "% used"
将 `/usage` 切换回"% 已使用"

- Fixed handling of thinking errors
修复了思考错误的处理

- Fixed performance regression
修复了性能回归

## 2.0.50

- Fixed bug preventing calling MCP tools that have nested references in their input schemas
修复了阻止调用输入架构中具有嵌套引用的 MCP 工具的错误

- Silenced a noisy but harmless error during upgrades
消除了升级期间嘈杂但无害的错误

- Improved ultrathink text display
改进了 ultrathink 文本显示

- Improved clarity of 5-hour session limit warning message
改进了 5 小时会话限制警告消息的清晰度

## 2.0.49

- Added readline-style ctrl-y for pasting deleted text
添加了 readline 风格的 ctrl-y 用于粘贴已删除的文本

- Improved clarity of usage limit warning message
改进了使用限制警告消息的清晰度

- Fixed handling of subagent permissions
修复了子代理权限的处理

## 2.0.47

- Improved error messages and validation for `claude --teleport`
改进了 `claude --teleport` 的错误消息和验证

- Improved error handling in `/usage`
改进了 `/usage` 中的错误处理

- Fixed race condition with history entry not getting logged at exit
修复了退出时历史记录条目未记录的竞争条件

- Fixed Vertex AI configuration not being applied from `settings.json`
修复了未从 `settings.json` 应用 Vertex AI 配置的问题

## 2.0.46

- Fixed image files being reported with incorrect media type when format cannot be detected from metadata
修复了当无法从元数据检测格式时图像文件被报告为不正确媒体类型的问题

## 2.0.45

- Added support for Microsoft Foundry! See https://code.claude.com/docs/en/azure-ai-foundry
添加了对 Microsoft Foundry 的支持！请参见 https://code.claude.com/docs/en/azure-ai-foundry

- Added `PermissionRequest` hook to automatically approve or deny tool permission requests with custom logic
添加了 `PermissionRequest` hook 以使用自定义逻辑自动批准或拒绝工具权限请求

- Send background tasks to Claude Code on the web by starting a message with `&`
通过以 `&` 开头的消息向网络上的 Claude Code 发送后台任务

## 2.0.43

- Added `permissionMode` field for custom agents
为自定义代理添加了 `permissionMode` 字段

- Added `tool_use_id` field to `PreToolUseHookInput` and `PostToolUseHookInput` types
为 `PreToolUseHookInput` 和 `PostToolUseHookInput` 类型添加了 `tool_use_id` 字段

- Added skills frontmatter field to declare skills to auto-load for subagents
添加了技能 frontmatter 字段，以声明为子代理自动加载的技能

- Added the `SubagentStart` hook event
添加了 `SubagentStart` hook 事件

- Fixed nested `CLAUDE.md` files not loading when @-mentioning files
修复了在 @ 提及文件时不加载嵌套 `CLAUDE.md` 文件的问题

- Fixed duplicate rendering of some messages in the UI
修复了某些消息在 UI 中重复渲染的问题

- Fixed some visual flickers
修复了一些视觉闪烁

- Fixed NotebookEdit tool inserting cells at incorrect positions when cell IDs matched the pattern `cell-N`
修复了当单元格 ID 匹配模式 `cell-N` 时 NotebookEdit 工具在错误位置插入单元格的问题

## 2.0.42

- Added `agent_id` and `agent_transcript_path` fields to `SubagentStop` hooks.
为 `SubagentStop` hooks 添加了 `agent_id` 和 `agent_transcript_path` 字段。

## 2.0.41

- Added `model` parameter to prompt-based stop hooks, allowing users to specify a custom model for hook evaluation
为基于提示的停止 hooks 添加了 `model` 参数，允许用户指定用于 hook 评估的自定义模型

- Fixed slash commands from user settings being loaded twice, which could cause rendering issues
修复了来自用户设置的斜杠命令被加载两次的问题，这可能导致渲染问题

- Fixed incorrect labeling of user settings vs project settings in command descriptions
修复了命令描述中用户设置与项目设置标签不正确的问题

- Fixed crash when plugin command hooks timeout during execution
修复了插件命令 hooks 在执行期间超时导致的崩溃

- Fixed: Bedrock users no longer see duplicate Opus entries in the /model picker when using `--model haiku`
修复：Bedrock 用户在使用 `--model haiku` 时在 /model 选择器中不再看到重复的 Opus 条目

- Fixed broken security documentation links in trust dialogs and onboarding
修复了信任对话框和入门指南中损坏的安全文档链接

- Fixed issue where pressing ESC to close the diff modal would also interrupt the model
修复了按 ESC 关闭差异模态框也会中断模型的问题

- ctrl-r history search landing on a slash command no longer cancels the search
ctrl-r 历史搜索落在斜杠命令上不再取消搜索

- SDK: Support custom timeouts for hooks
SDK：支持 hooks 的自定义超时

- Allow more safe git commands to run without approval
允许更多安全的 git 命令在无需批准的情况下运行

- Plugins: Added support for sharing and installing output styles
Plugins：添加了共享和安装输出样式支持

- Teleporting a session from web will automatically set the upstream branch
从网络传送会话将自动设置上游分支

## 2.0.37

- Fixed how idleness is computed for notifications
修复了通知的空闲时间计算方式

- Hooks: Added matcher values for Notification hook events
Hooks：为 Notification hook 事件添加了匹配器值

- Output Styles: Added `keep-coding-instructions` option to frontmatter
输出样式：在 frontmatter 中添加了 `keep-coding-instructions` 选项

## 2.0.36

- Fixed: DISABLE_AUTOUPDATER environment variable now properly disables package manager update notifications
修复：DISABLE_AUTOUPDATER 环境变量现在正确禁用包管理器更新通知

- Fixed queued messages being incorrectly executed as bash commands
修复了排队的消息被错误执行为 bash 命令的问题

- Fixed input being lost when typing while a queued message is processed
修复了在处理排队的消息时输入丢失的问题

## 2.0.35

- Improve fuzzy search results when searching commands
改进搜索命令时的模糊搜索结果

- Improved VS Code extension to respect `chat.fontSize` and `chat.fontFamily` settings throughout the entire UI, and apply font changes immediately without requiring reload
改进 VS Code 扩展以在整个 UI 中遵守 `chat.fontSize` 和 `chat.fontFamily` 设置，并立即应用字体更改而无需重新加载

- Added `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY` environment variable to automatically exit SDK mode after a specified idle duration, useful for automated workflows and scripts
添加了 `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY` 环境变量，以在指定的空闲持续时间后自动退出 SDK 模式，对自动化工作流和脚本很有用

- Migrated `ignorePatterns` from project config to deny permissions in the localSettings.
将 `ignorePatterns` 从项目配置迁移到 localSettings 中的拒绝权限。

- Fixed menu navigation getting stuck on items with empty string or other falsy values (e.g., in the `/hooks` menu)
修复了菜单导航在空字符串或其他虚假值的项目上卡住的问题（例如，在 `/hooks` 菜单中）

## 2.0.34

- VSCode Extension: Added setting to configure the initial permission mode for new conversations
VSCode 扩展：添加了设置以配置新对话的初始权限模式

- Improved file path suggestion performance with native Rust-based fuzzy finder
使用基于 Rust 的原生模糊查找器改进了文件路径建议性能

- Fixed infinite token refresh loop that caused MCP servers with OAuth (e.g., Slack) to hang during connection
修复了导致带 OAuth 的 MCP 服务器（例如，Slack）在连接期间挂起的无限令牌刷新循环

- Fixed memory crash when reading or writing large files (especially base64-encoded images)
修复了读取或写入大文件（特别是 base64 编码的图像）时的内存崩溃

## 2.0.33

- Native binary installs now launch quicker.
本机二进制安装现在启动更快。

- Fixed `claude doctor` incorrectly detecting Homebrew vs npm-global installations by properly resolving symlinks
通过正确解析符号链接，修复了 `claude doctor` 错误检测 Homebrew 与 npm 全局安装的问题

- Fixed `claude mcp serve` exposing tools with incompatible outputSchemas
修复了 `claude mcp serve` 暴露具有不兼容 outputSchemas 的工具的问题

## 2.0.32

- Un-deprecate output styles based on community feedback
根据社区反馈，取消对输出样式的弃用

- Added `companyAnnouncements` setting for displaying announcements on startup
添加了 `companyAnnouncements` 设置以在启动时显示公告

- Fixed hook progress messages not updating correctly during PostToolUse hook execution
修复了 PostToolUse hook 执行期间 hook 进度消息未正确更新的问题

## 2.0.31

- Windows: native installation uses shift+tab as shortcut for mode switching, instead of alt+m
Windows：本机安装使用 shift+tab 作为模式切换快捷键，而不是 alt+m

- Vertex: add support for Web Search on supported models
Vertex：为支持的模型添加 Web Search 支持

- VSCode: Adding the respectGitIgnore configuration to include .gitignored files in file searches (defaults to true)
VSCode：添加 respectGitIgnore 配置以在文件搜索中包含 .gitignored 文件（默认为 true）

- Fixed a bug with subagents and MCP servers related to "Tool names must be unique" error
修复了与"工具名称必须唯一"错误相关的子代理和 MCP 服务器错误

- Fixed issue causing `/compact` to fail with `prompt_too_long` by making it respect existing compact boundaries
通过使其尊重现有的压缩边界，修复了导致 `/compact` 因 `prompt_too_long` 而失败的问题

- Fixed plugin uninstall not removing plugins
修复了插件卸载未移除插件的问题

## 2.0.30

- Added helpful hint to run `security unlock-keychain` when encountering API key errors on macOS with locked keychain
在 macOS 上遇到 API 密钥错误且钥匙串已锁定时，添加了运行 `security unlock-keychain` 的有用提示

- Added `allowUnsandboxedCommands` sandbox setting to disable the dangerouslyDisableSandbox escape hatch at policy level
添加了 `allowUnsandboxedCommands` 沙箱设置，以在策略级别禁用 dangerouslyDisableSandbox 逃生舱口

- Added `disallowedTools` field to custom agent definitions for explicit tool blocking
为自定义代理定义添加了 `disallowedTools` 字段，用于明确的工具阻止

- Added prompt-based stop hooks
添加了基于提示的停止 hooks

- VSCode: Added respectGitIgnore configuration to include .gitignored files in file searches (defaults to true)
VSCode：添加 respectGitIgnore 配置以在文件搜索中包含 .gitignored 文件（默认为 true）

- Enabled SSE MCP servers on native build
在本机构建上启用 SSE MCP 服务器

- Deprecated output styles. Review options in `/output-style` and use --system-prompt-file, --system-prompt, --append-system-prompt, CLAUDE.md, or plugins instead
弃用输出样式。查看 `/output-style` 中的选项，并改用 --system-prompt-file、--system-prompt、--append-system-prompt、CLAUDE.md 或 plugins

- Removed support for custom ripgrep configuration, resolving an issue where Search returns no results and config discovery fails
移除了对自定义 ripgrep 配置的支持，解决了 Search 不返回结果且配置发现失败的问题

- Fixed Explore agent creating unwanted .md investigation files during codebase exploration
修复了 Explore 代理在代码库探索期间创建不需要的 .md 调查文件的问题

- Fixed a bug where `/context` would sometimes fail with "max_tokens must be greater than thinking.budget_tokens" error message
修复了 `/context` 有时会因"max_tokens must be greater than thinking.budget_tokens"错误消息而失败的问题

- Fixed `--mcp-config` flag to correctly override file-based MCP configurations
修复了 `--mcp-config` 标志以正确覆盖基于文件的 MCP 配置

- Fixed bug that saved session permissions to local settings
修复了将会话权限保存到本地设置的错误

- Fixed MCP tools not being available to sub-agents
修复了 MCP 工具对子代理不可用的问题

- Fixed hooks and plugins not executing when using --dangerously-skip-permissions flag
修复了使用 --dangerously-skip-permissions 标志时 hooks 和插件不执行的问题

- Fixed delay when navigating through typeahead suggestions with arrow keys
修复了使用箭头键导航类型建议时的延迟

- VSCode: Restored selection indicator in input footer showing current file or code selection status
VSCode：恢复了输入页脚中的选择指示器，显示当前文件或代码选择状态

## 2.0.28

- Plan mode: introduced new Plan subagent
计划模式：引入新的 Plan 子代理

- Subagents: claude can now choose to resume subagents
子代理：claude 现在可以选择恢复子代理

- Subagents: claude can dynamically choose the model used by its subagents
子代理：claude 可以动态选择其子代理使用的模型

- SDK: added --max-budget-usd flag
SDK：添加了 --max-budget-usd 标志

- Discovery of custom slash commands, subagents, and output styles no longer respects .gitignore
自定义斜杠命令、子代理和输出样式的发现不再尊重 .gitignore

- Stop `/terminal-setup` from adding backslash to `Shift + Enter` in VS Code
阻止 `/terminal-setup` 在 VS Code 中为 `Shift + Enter` 添加反斜杠

- Add branch and tag support for git-based plugins and marketplaces using fragment syntax (e.g., `owner/repo#branch`)
使用片段语法（例如，`owner/repo#branch`）添加对基于 git 的插件和市场places 的分支和标签支持

- Fixed a bug where macOS permission prompts would show up upon initial launch when launching from home directory
修复了从主目录启动时初始启动时出现 macOS 权限提示的问题

- Various other bug fixes
其他各种错误修复

## 2.0.27

- New UI for permission prompts
权限提示的新 UI

- Added current branch filtering and search to session resume screen for easier navigation
为会话恢复屏幕添加了当前分支过滤和搜索，以便于导航

- Fixed directory @-mention causing "No assistant message found" error
修复了目录 @ 提及导致"未找到助手消息"错误的问题

- VSCode Extension: Add config setting to include .gitignored files in file searches
VSCode 扩展：添加配置设置以在文件搜索中包含 .gitignored 文件

- VSCode Extension: Bug fixes for unrelated 'Warmup' conversations, and configuration/settings occasionally being reset to defaults
VSCode 扩展：修复了无关的"Warmup"对话以及配置/设置偶尔被重置为默认值的错误

## 2.0.25

- Removed legacy SDK entrypoint. Please migrate to @anthropic-ai/claude-agent-sdk for future SDK updates: https://platform.claude.com/docs/en/agent-sdk/migration-guide
移除了旧版 SDK 入口点。请迁移到 @anthropic-ai/claude-agent-sdk 以进行未来的 SDK 更新：https://platform.claude.com/docs/en/agent-sdk/migration-guide

## 2.0.24

- Fixed a bug where project-level skills were not loading when --setting-sources 'project' was specified
修复了指定 --setting-sources 'project' 时项目级技能未加载的问题

- Claude Code Web: Support for Web -> CLI teleport
Claude Code Web：支持 Web -> CLI 传送

- Sandbox: Releasing a sandbox mode for the BashTool on Linux & Mac
沙箱：在 Linux 和 Mac 上发布 BashTool 的沙箱模式

- Bedrock: Display awsAuthRefresh output when auth is required
Bedrock：当需要身份验证时显示 awsAuthRefresh 输出

## 2.0.22

- Fixed content layout shift when scrolling through slash commands
修复了滚动浏览斜杠命令时的内容布局偏移

- IDE: Add toggle to enable/disable thinking.
IDE：添加启用/禁用思考的切换。

- Fix bug causing duplicate permission prompts with parallel tool calls
修复并行工具调用导致重复权限提示的错误

- Add support for enterprise managed MCP allowlist and denylist
添加对企业托管 MCP 允许列表和拒绝列表的支持

## 2.0.21

- Support MCP `structuredContent` field in tool responses
支持工具响应中的 MCP `structuredContent` 字段

- Added an interactive question tool
添加了交互式问题工具

- Claude will now ask you questions more often in plan mode
Claude 现在会在计划模式中更频繁地向您提问

- Added Haiku 4.5 as a model option for Pro users
为 Pro 用户添加了 Haiku 4.5 作为模型选项

- Fixed an issue where queued commands don't have access to previous messages' output
修复了排队命令无法访问先前消息输出的问题

## 2.0.20

- Added support for Claude Skills
添加了对 Claude Skills 的支持

## 2.0.19

- Auto-background long-running bash commands instead of killing them. Customize with BASH_DEFAULT_TIMEOUT_MS
自动后台化长时间运行的 bash 命令而不是终止它们。使用 BASH_DEFAULT_TIMEOUT_MS 自定义

- Fixed a bug where Haiku was unnecessarily called in print mode
修复了 Haiku 在打印模式下被不必要调用的错误

## 2.0.17

- Added Haiku 4.5 to model selector!
在模型选择器中添加了 Haiku 4.5！

- Haiku 4.5 automatically uses Sonnet in plan mode, and Haiku for execution (i.e. SonnetPlan by default)
Haiku 4.5 在计划模式中自动使用 Sonnet，执行时使用 Haiku（即默认为 SonnetPlan）

- 3P (Bedrock and Vertex) are not automatically upgraded yet. Manual upgrading can be done through setting `ANTHROPIC_DEFAULT_HAIKU_MODEL`
3P（Bedrock 和 Vertex）尚未自动升级。可以通过设置 `ANTHROPIC_DEFAULT_HAIKU_MODEL` 进行手动升级

- Introducing the Explore subagent. Powered by Haiku it'll search through your codebase efficiently to save context!
推出 Explore 子代理。由 Haiku 驱动，它将高效搜索您的代码库以节省上下文！

- OTEL: support HTTP_PROXY and HTTPS_PROXY
OTEL：支持 HTTP_PROXY 和 HTTPS_PROXY

- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` now disables release notes fetching
`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` 现在禁用发行说明获取

## 2.0.15

- Fixed bug with resuming where previously created files needed to be read again before writing
修复了恢复时之前创建的文件需要在写入前再次读取的错误

- Fixed bug with `-p` mode where @-mentioned files needed to be read again before writing
修复了 `-p` 模式下 @ 提及的文件需要在写入前再次读取的错误

## 2.0.14

- Fix @-mentioning MCP servers to toggle them on/off
修复 @ 提及 MCP 服务器以开启/关闭它们

- Improve permission checks for bash with inline env vars
改进带有内联环境变量的 bash 的权限检查

- Fix ultrathink + thinking toggle
修复 ultrathink + 思考切换

- Reduce unnecessary logins
减少不必要的登录

- Document --system-prompt
记录 --system-prompt

- Several improvements to rendering
渲染的多项改进

- Plugins UI polish
Plugins UI 优化

## 2.0.13

- Fixed `/plugin` not working on native build
修复了 `/plugin` 在本机构建上不工作的问题

## 2.0.12

- **Plugin System Released**: Extend Claude Code with custom commands, agents, hooks, and MCP servers from marketplaces
**插件系统发布**：通过自定义命令、代理、hooks 和来自市场places 的 MCP 服务器扩展 Claude Code

- `/plugin install`, `/plugin enable/disable`, `/plugin marketplace` commands for plugin management
`/plugin install`、`/plugin enable/disable`、`/plugin marketplace` 命令用于插件管理

- Repository-level plugin configuration via `extraKnownMarketplaces` for team collaboration
通过 `extraKnownMarketplaces` 进行存储库级插件配置，用于团队协作

- `/plugin validate` command for validating plugin structure and configuration
`/plugin validate` 命令用于验证插件结构和配置

- Plugin announcement blog post at https://www.anthropic.com/news/claude-code-plugins
插件公告博客文章：https://www.anthropic.com/news/claude-code-plugins

- Plugin documentation available at https://code.claude.com/docs/en/plugins
插件文档：https://code.claude.com/docs/en/plugins

- Comprehensive error messages and diagnostics via `/doctor` command
通过 `/doctor` 命令提供全面的错误消息和诊断

- Avoid flickering in `/model` selector
避免在 `/model` 选择器中闪烁

- Improvements to `/help`
`/help` 的改进

- Avoid mentioning hooks in `/resume` summaries
避免在 `/resume` 摘要中提及 hooks

- Changes to the "verbose" setting in `/config` now persist across sessions
`/config` 中"verbose"设置的更改现在在会话间保持

## 2.0.11

- Reduced system prompt size by 1.4k tokens
将系统提示大小减少了 1.4k 令牌

- IDE: Fixed keyboard shortcuts and focus issues for smoother interaction
IDE：修复了键盘快捷键和焦点问题，以实现更流畅的交互

- Fixed Opus fallback rate limit errors appearing incorrectly
修复了 Opus 回退速率限制错误显示不正确的问题

- Fixed /add-dir command selecting wrong default tab
修复了 /add-dir 命令选择错误默认选项卡的问题

## 2.0.10

- Rewrote terminal renderer for buttery smooth UI
重写终端渲染器，实现流畅的 UI

- Enable/disable MCP servers by @mentioning, or in /mcp
通过 @ 提及或在 /mcp 中启用/禁用 MCP 服务器

- Added tab completion for shell commands in bash mode
在 bash 模式下为 shell 命令添加了 tab 补全

- PreToolUse hooks can now modify tool inputs
PreToolUse hooks 现在可以修改工具输入

- Press Ctrl-G to edit your prompt in your system's configured text editor
按 Ctrl-G 在系统配置的文本编辑器中编辑您的提示

- Fixes for bash permission checks with environment variables in the command
修复命令中带有环境变量的 bash 权限检查

## 2.0.9

- Fix regression where bash backgrounding stopped working
修复 bash 后台化停止工作的回归

## 2.0.8

- Update Bedrock default Sonnet model to `global.anthropic.claude-sonnet-4-5-20250929-v1:0`
将 Bedrock 默认 Sonnet 模型更新为 `global.anthropic.claude-sonnet-4-5-20250929-v1:0`

- IDE: Add drag-and-drop support for files and folders in chat
IDE：为聊天中的文件和文件夹添加拖放支持

- /context: Fix counting for thinking blocks
/context：修复思考块的计数

- Improve message rendering for users with light themes on dark terminals
为在暗色终端上使用浅色主题的用户改进消息渲染

- Remove deprecated .claude.json allowedTools, ignorePatterns, env, and todoFeatureEnabled config options (instead, configure these in your settings.json)
移除已弃用的 .claude.json allowedTools、ignorePatterns、env 和 todoFeatureEnabled 配置选项（改为在 settings.json 中配置这些）

## 2.0.5

- IDE: Fix IME unintended message submission with Enter and Tab
IDE：修复 IME 使用 Enter 和 Tab 意外提交消息的问题

- IDE: Add "Open in Terminal" link in login screen
IDE：在登录屏幕中添加"在终端中打开"链接

- Fix unhandled OAuth expiration 401 API errors
修复未处理的 OAuth 过期 401 API 错误

- SDK: Added SDKUserMessageReplay.isReplay to prevent duplicate messages
SDK：添加了 SDKUserMessageReplay.isReplay 以防止重复消息

## 2.0.1

- Skip Sonnet 4.5 default model setting change for Bedrock and Vertex
跳过 Bedrock 和 Vertex 的 Sonnet 4.5 默认模型设置更改

- Various bug fixes and presentation improvements
各种错误修复和演示改进

## 2.0.0

- New native VS Code extension
新的本机 VS Code 扩展

- Fresh coat of paint throughout the whole app
整个应用程序的新外观

- /rewind a conversation to undo code changes
/rewind 对话以撤消代码更改

- /usage command to see plan limits
/usage 命令查看计划限制

- Tab to toggle thinking (sticky across sessions)
Tab 切换思考（在会话间保持）

- Ctrl-R to search history
Ctrl-R 搜索历史

- Unshipped claude config command
未发布的 claude config 命令

- Hooks: Reduced PostToolUse 'tool_use' ids were found without 'tool_result' blocks errors
Hooks：减少了 PostToolUse 'tool_use' ids 在没有 'tool_result' 块时发现的错误

- SDK: The Claude Code SDK is now the Claude Agent SDK
SDK：Claude Code SDK 现在是 Claude Agent SDK

- Add subagents dynamically with `--agents` flag
使用 `--agents` 标志动态添加子代理

## 1.0.126

- Enable /context command for Bedrock and Vertex
为 Bedrock 和 Vertex 启用 /context 命令

- Add mTLS support for HTTP-based OpenTelemetry exporters
为基于 HTTP 的 OpenTelemetry 导出器添加 mTLS 支持

## 1.0.124

- Set `CLAUDE_BASH_NO_LOGIN` environment variable to 1 or true to to skip login shell for BashTool
将 `CLAUDE_BASH_NO_LOGIN` 环境变量设置为 1 或 true 以跳过 BashTool 的登录 shell

- Fix Bedrock and Vertex environment variables evaluating all strings as truthy
修复 Bedrock 和 Vertex 环境变量将所有字符串评估为真值的问题

- No longer inform Claude of the list of allowed tools when permission is denied
权限被拒绝时不再告知 Claude 允许的工具列表

- Fixed security vulnerability in Bash tool permission checks
修复 Bash 工具权限检查中的安全漏洞

- Improved VSCode extension performance for large files
改进了大文件的 VSCode 扩展性能

## 1.0.123

- Bash permission rules now support output redirections when matching (e.g., `Bash(python:*)` matches `python script.py > output.txt`)
Bash 权限规则现在在匹配时支持输出重定向（例如，`Bash(python:*)` 匹配 `python script.py > output.txt`）

- Fixed thinking mode triggering on negation phrases like "don't think"
修复了思考模式在"不要思考"等否定短语上触发的问题

- Fixed rendering performance degradation during token streaming
修复了令牌流式传输期间的渲染性能下降

- Added SlashCommand tool, which enables Claude to invoke your slash commands. https://code.claude.com/docs/en/slash-commands#SlashCommand-tool
添加了 SlashCommand 工具，使 Claude 能够调用您的斜杠命令。https://code.claude.com/docs/en/slash-commands#SlashCommand-tool

- Enhanced BashTool environment snapshot logging
增强了 BashTool 环境快照日志记录

- Fixed a bug where resuming a conversation in headless mode would sometimes enable thinking unnecessarily
修复了在无头模式下恢复对话时有时不必要启用思考的错误

- Migrated --debug logging to a file, to enable easy tailing & filtering
将 --debug 日志迁移到文件，以便轻松查看和过滤

## 1.0.120

- Fix input lag during typing, especially noticeable with large prompts
修复输入延迟，特别是在使用大提示时很明显

- Improved VSCode extension command registry and sessions dialog user experience
改进了 VSCode 扩展命令注册和会话对话框用户体验

- Enhanced sessions dialog responsiveness and visual feedback
增强了会话对话框响应性和视觉反馈

- Fixed IDE compatibility issue by removing worktree support check
通过移除工作树支持检查修复了 IDE 兼容性问题

- Fixed security vulnerability where Bash tool permission checks could be bypassed using prefix matching
修复了使用前缀匹配可以绕过 Bash 工具权限检查的安全漏洞

## 1.0.119

- Fix Windows issue where process visually freezes on entering interactive mode
修复 Windows 上进程在进入交互模式时视觉冻结的问题

- Support dynamic headers for MCP servers via headersHelper configuration
通过 headersHelper 配置支持 MCP 服务器的动态标头

- Fix thinking mode not working in headless sessions
修复思考模式在无头会话中不工作的问题

- Fixed slash commands now properly update allowed tools instead of replacing them
修复斜杠命令现在正确更新允许的工具而不是替换它们

## 1.0.117

- Add Ctrl-R history search to recall previous commands like bash/zsh
添加 Ctrl-R 历史搜索以像 bash/zsh 一样调用先前的命令

- Fix input lag while typing, especially on Windows
修复输入延迟，特别是在 Windows 上

- Add sed command to auto-allowed commands in acceptEdits mode
在 acceptEdits 模式下将 sed 命令添加到自动允许的命令

- Fix Windows PATH comparison to be case-insensitive for drive letters
修复 Windows PATH 比较对驱动器字母不区分大小写的问题

- Add permissions management hint to /add-dir output
向 /add-dir 输出添加权限管理提示

## 1.0.115

- Improve thinking mode display with enhanced visual effects
通过增强的视觉效果改进思考模式显示

- Type /t to temporarily disable thinking mode in your prompt
输入 /t 在提示中临时禁用思考模式

- Improve path validation for glob and grep tools
改进 glob 和 grep 工具的路径验证

- Show condensed output for post-tool hooks to reduce visual clutter
为 post-tool hooks 显示压缩输出以减少视觉混乱

- Fix visual feedback when loading state completes
修复加载状态完成时的视觉反馈

- Improve UI consistency for permission request dialogs
改进权限请求对话框的 UI 一致性

## 1.0.113

- Deprecated piped input in interactive mode
弃用交互模式下的管道输入

- Move Ctrl+R keybinding for toggling transcript to Ctrl+O
将切换记录的 Ctrl+R 键绑定移动到 Ctrl+O

## 1.0.112

- Transcript mode (Ctrl+R): Added the model used to generate each assistant message
记录模式（Ctrl+R）：添加了用于生成每个助手消息的模型

- Addressed issue where some Claude Max users were incorrectly recognized as Claude Pro users
解决了一些 Claude Max 用户被错误识别为 Claude Pro 用户的问题

- Hooks: Added systemMessage support for SessionEnd hooks
Hooks：为 SessionEnd hooks 添加了 systemMessage 支持

- Added `spinnerTipsEnabled` setting to disable spinner tips
添加了 `spinnerTipsEnabled` 设置以禁用旋转器提示

- IDE: Various improvements and bug fixes
IDE：各种改进和错误修复

## 1.0.111

- /model now validates provided model names
/model 现在验证提供的模型名称

- Fixed Bash tool crashes caused by malformed shell syntax parsing
修复了由格式错误的 shell 语法解析导致的 Bash 工具崩溃

## 1.0.110

- /terminal-setup command now supports WezTerm
/terminal-setup 命令现在支持 WezTerm

- MCP: OAuth tokens now proactively refresh before expiration
MCP：OAuth 令牌现在在过期前主动刷新

- Fixed reliability issues with background Bash processes
修复了后台 Bash 进程的可靠性问题

## 1.0.109

- SDK: Added partial message streaming support via `--include-partial-messages` CLI flag
SDK：通过 `--include-partial-messages` CLI 标志添加了部分消息流式传输支持

## 1.0.106

- Windows: Fixed path permission matching to consistently use POSIX format (e.g., `Read(//c/Users/...)`)
Windows：修复路径权限匹配以一致使用 POSIX 格式（例如，`Read(//c/Users/...)`）

## 1.0.97

- Settings: /doctor now validates permission rule syntax and suggests corrections
设置：/doctor 现在验证权限规则语法并建议更正

## 1.0.94

- Vertex: add support for global endpoints for supported models
Vertex：为支持的模型添加全局端点支持

- /memory command now allows direct editing of all imported memory files
/memory 命令现在允许直接编辑所有导入的内存文件

- SDK: Add custom tools as callbacks
SDK：添加自定义工具作为回调

- Added /todos command to list current todo items
添加了 /todos 命令以列出当前待办事项

## 1.0.93

- Windows: Add alt + v shortcut for pasting images from clipboard
Windows：添加 alt + v 快捷键用于从剪贴板粘贴图像

- Support NO_PROXY environment variable to bypass proxy for specified hostnames and IPs
支持 NO_PROXY 环境变量以绕过指定主机名和 IP 的代理

## 1.0.90

- Settings file changes take effect immediately - no restart required
设置文件更改立即生效 - 无需重启

## 1.0.88

- Fixed issue causing "OAuth authentication is currently not supported"
修复了导致"目前不支持 OAuth 身份验证"的问题

- Status line input now includes `exceeds_200k_tokens`
状态行输入现在包括 `exceeds_200k_tokens`

- Fixed incorrect usage tracking in /cost.
修复了 /cost 中不正确的使用跟踪。

- Introduced `ANTHROPIC_DEFAULT_SONNET_MODEL` and `ANTHROPIC_DEFAULT_OPUS_MODEL` for controlling model aliases opusplan, opus, and sonnet.
引入了 `ANTHROPIC_DEFAULT_SONNET_MODEL` 和 `ANTHROPIC_DEFAULT_OPUS_MODEL` 用于控制模型别名 opusplan、opus 和 sonnet。

- Bedrock: Updated default Sonnet model to Sonnet 4
Bedrock：将默认 Sonnet 模型更新为 Sonnet 4

## 1.0.86

- Added /context to help users self-serve debug context issues
添加 /context 以帮助用户自助调试上下文问题

- SDK: Added UUID support for all SDK messages
SDK：为所有 SDK 消息添加了 UUID 支持

- SDK: Added `--replay-user-messages` to replay user messages back to stdout
SDK：添加了 `--replay-user-messages` 以将用户消息重播回 stdout

## 1.0.85

- Status line input now includes session cost info
状态行输入现在包括会话成本信息

- Hooks: Introduced SessionEnd hook
Hooks：引入 SessionEnd hook

## 1.0.84

- Fix tool_use/tool_result id mismatch error when network is unstable
修复网络不稳定时 tool_use/tool_result ID 不匹配错误

- Fix Claude sometimes ignoring real-time steering when wrapping up a task
修复 Claude 在完成任务时有时忽略实时引导的问题

- @-mention: Add ~/.claude/\* files to suggestions for easier agent, output style, and slash command editing
@ 提及：将 ~/.claude/\* 文件添加到建议中，以便更轻松地编辑代理、输出样式和斜杠命令

- Use built-in ripgrep by default; to opt out of this behavior, set USE_BUILTIN_RIPGREP=0
默认使用内置 ripgrep；要选择退出此行为，请设置 USE_BUILTIN_RIPGREP=0

## 1.0.83

- @-mention: Support files with spaces in path
@ 提及：支持路径中包含空格的文件

- New shimmering spinner
新的闪烁旋转器

## 1.0.82

- SDK: Add request cancellation support
SDK：添加请求取消支持

- SDK: New additionalDirectories option to search custom paths, improved slash command processing
SDK：新的 additionalDirectories 选项以搜索自定义路径，改进的斜杠命令处理

- Settings: Validation prevents invalid fields in .claude/settings.json files
设置：验证防止 .claude/settings.json 文件中的无效字段

- MCP: Improve tool name consistency
MCP：改进工具名称一致性

- Bash: Fix crash when Claude tries to automatically read large files
Bash：修复 Claude 尝试自动读取大文件时的崩溃

## 1.0.81

- Released output styles, including new built-in educational output styles "Explanatory" and "Learning". Docs: https://code.claude.com/docs/en/output-styles
发布输出样式，包括新的内置教育输出样式"解释性"和"学习性"。文档：https://code.claude.com/docs/en/output-styles

- Agents: Fix custom agent loading when agent files are unparsable
代理：修复代理文件无法解析时的自定义代理加载

## 1.0.80

- UI improvements: Fix text contrast for custom subagent colors and spinner rendering issues
UI 改进：修复自定义子代理颜色的文本对比度和旋转器渲染问题

## 1.0.77

- Bash tool: Fix heredoc and multiline string escaping, improve stderr redirection handling
Bash 工具：修复 heredoc 和多行字符串转义，改进 stderr 重定向处理

- SDK: Add session support and permission denial tracking
SDK：添加会话支持和权限拒绝跟踪

- Fix token limit errors in conversation summarization
修复对话摘要中的令牌限制错误

- Opus Plan Mode: New setting in `/model` to run Opus only in plan mode, Sonnet otherwise
Opus 计划模式：`/model` 中的新设置，仅在计划模式下运行 Opus，否则运行 Sonnet

## 1.0.73

- MCP: Support multiple config files with `--mcp-config file1.json file2.json`
MCP：支持多个配置文件，使用 `--mcp-config file1.json file2.json`

- MCP: Press Esc to cancel OAuth authentication flows
MCP：按 Esc 取消 OAuth 身份验证流程

- Bash: Improved command validation and reduced false security warnings
Bash：改进的命令验证和减少虚假安全警告

- UI: Enhanced spinner animations and status line visual hierarchy
UI：增强的旋转器动画和状态行视觉层次

- Linux: Added support for Alpine and musl-based distributions (requires separate ripgrep installation)
Linux：添加对 Alpine 和基于 musl 的发行版的支持（需要单独安装 ripgrep）

## 1.0.72

- Ask permissions: have Claude Code always ask for confirmation to use specific tools with /permissions
请求权限：让 Claude Code 始终请求确认以使用 /permissions 的特定工具

## 1.0.71

- Background commands: (Ctrl-b) to run any Bash command in the background so Claude can keep working (great for dev servers, tailing logs, etc.)
后台命令：（Ctrl-b）在后台运行任何 Bash 命令，以便 Claude 可以继续工作（非常适合开发服务器、跟踪日志等）

- Customizable status line: add your terminal prompt to Claude Code with /statusline
可自定义状态行：使用 /statusline 将您的终端提示添加到 Claude Code

## 1.0.70

- Performance: Optimized message rendering for better performance with large contexts
性能：优化消息渲染以在大型上下文中提供更好的性能

- Windows: Fixed native file search, ripgrep, and subagent functionality
Windows：修复本机文件搜索、ripgrep 和子代理功能

- Added support for @-mentions in slash command arguments
添加对斜杠命令参数中 @ 提及的支持

## 1.0.69

- Upgraded Opus to version 4.1
将 Opus 升级到版本 4.1

## 1.0.68

- Fix incorrect model names being used for certain commands like `/pr-comments`
修复为某些命令（如 `/pr-comments`）使用不正确模型名称的问题

- Windows: improve permissions checks for allow / deny tools and project trust. This may create a new project entry in `.claude.json` - manually merge the history field if desired.
Windows：改进允许/拒绝工具和项目信任的权限检查。这可能在 `.claude.json` 中创建新的项目条目 - 如果需要，请手动合并历史字段。

- Windows: improve sub-process spawning to eliminate "No such file or directory" when running commands like pnpm
Windows：改进子进程生成，以消除运行 pnpm 等命令时的"No such file or directory"错误

- Enhanced /doctor command with CLAUDE.md and MCP tool context for self-serve debugging
增强 /doctor 命令，提供 CLAUDE.md 和 MCP 工具上下文用于自助调试

- SDK: Added canUseTool callback support for tool confirmation
SDK：添加了 canUseTool 回调支持用于工具确认

- Added `disableAllHooks` setting
添加了 `disableAllHooks` 设置

- Improved file suggestions performance in large repos
改进了大型存储库中的文件建议性能

## 1.0.65

- IDE: Fixed connection stability issues and error handling for diagnostics
IDE：修复连接稳定性问题和诊断的错误处理

- Windows: Fixed shell environment setup for users without .bashrc files
Windows：修复没有 .bashrc 文件的用户的 shell 环境设置

## 1.0.64

- Agents: Added model customization support - you can now specify which model an agent should use
代理：添加了模型自定义支持 - 您现在可以指定代理应使用哪个模型

- Agents: Fixed unintended access to the recursive agent tool
代理：修复了对递归代理工具的意外访问

- Hooks: Added systemMessage field to hook JSON output for displaying warnings and context
Hooks：在 hook JSON 输出中添加了 systemMessage 字段用于显示警告和上下文

- SDK: Fixed user input tracking across multi-turn conversations
SDK：修复了多轮对话中的用户输入跟踪

- Added hidden files to file search and @-mention suggestions
将隐藏文件添加到文件搜索和 @ 提及建议

## 1.0.63

- Windows: Fixed file search, @agent mentions, and custom slash commands functionality
Windows：修复了文件搜索、@ 代理提及和自定义斜杠命令功能

## 1.0.62

- Added @-mention support with typeahead for custom agents. @<your-custom-agent> to invoke it
为自定义代理添加了带有类型预读的 @ 提及支持。@<your-custom-agent> 来调用它

- Hooks: Added SessionStart hook for new session initialization
Hooks：为新会话初始化添加了 SessionStart hook

- /add-dir command now supports typeahead for directory paths
/add-dir 命令现在支持目录路径的类型预读

- Improved network connectivity check reliability
改进了网络连接检查可靠性

## 1.0.61

- Transcript mode (Ctrl+R): Changed Esc to exit transcript mode rather than interrupt
记录模式（Ctrl+R）：将 Esc 更改为退出记录模式而不是中断

- Settings: Added `--settings` flag to load settings from a JSON file
设置：添加了 `--settings` 标志以从 JSON 文件加载设置

- Settings: Fixed resolution of settings files paths that are symlinks
设置：修复符号链接的设置文件路径解析

- OTEL: Fixed reporting of wrong organization after authentication changes
OTEL：修复身份验证更改后报告错误组织的问题

- Slash commands: Fixed permissions checking for allowed-tools with Bash
斜杠命令：修复允许工具与 Bash 的权限检查

- IDE: Added support for pasting images in VSCode MacOS using ⌘+V
IDE：添加在 VSCode MacOS 中使用 ⌘+V 粘贴图像的支持

- IDE: Added `CLAUDE_CODE_AUTO_CONNECT_IDE=false` for disabling IDE auto-connection
IDE：添加了 `CLAUDE_CODE_AUTO_CONNECT_IDE=false` 用于禁用 IDE 自动连接

- Added `CLAUDE_CODE_SHELL_PREFIX` for wrapping Claude and user-provided shell commands run by Claude Code
添加了 `CLAUDE_CODE_SHELL_PREFIX` 用于包装由 Claude Code 运行的 Claude 和用户提供的 shell 命令

## 1.0.60

- You can now create custom subagents for specialized tasks! Run /agents to get started
您现在可以为专门任务创建自定义子代理！运行 /agents 开始使用

## 1.0.59

- SDK: Added tool confirmation support with canUseTool callback
SDK：添加了带有 canUseTool 回调的工具确认支持

- SDK: Allow specifying env for spawned process
SDK：允许为生成的进程指定 env

- Hooks: Exposed PermissionDecision to hooks (including "ask")
Hooks：向 hooks 公开 PermissionDecision（包括"询问"）

- Hooks: UserPromptSubmit now supports additionalContext in advanced JSON output
Hooks：UserPromptSubmit 现在在高级 JSON 输出中支持 additionalContext

- Fixed issue where some Max users that specified Opus would still see fallback to Sonnet
修复了某些指定 Opus 的 Max 用户仍然看到回退到 Sonnet 的问题

## 1.0.58

- Added support for reading PDFs
添加了读取 PDF 的支持

- MCP: Improved server health status display in 'claude mcp list'
MCP：改进了 'claude mcp list' 中的服务器健康状态显示

- Hooks: Added CLAUDE_PROJECT_DIR env var for hook commands
Hooks：为 hook 命令添加了 CLAUDE_PROJECT_DIR 环境变量

## 1.0.57

- Added support for specifying a model in slash commands
添加了在斜杠命令中指定模型的支持

- Improved permission messages to help Claude understand allowed tools
改进了权限消息以帮助 Claude 理解允许的工具

- Fix: Remove trailing newlines from bash output in terminal wrapping
修复：在终端包装中从 bash 输出中删除尾随换行符

## 1.0.56

- Windows: Enabled shift+tab for mode switching on versions of Node.js that support terminal VT mode
Windows：在支持终端 VT 模式的 Node.js 版本上启用 shift+tab 进行模式切换

- Fixes for WSL IDE detection
WSL IDE 检测的修复

- Fix an issue causing awsRefreshHelper changes to .aws directory not to be picked up
修复导致 awsRefreshHelper 对 .aws 目录的更改未被拾取的问题

## 1.0.55

- Clarified knowledge cutoff for Opus 4 and Sonnet 4 models
澄清了 Opus 4 和 Sonnet 4 模型的知识截止日期

- Windows: fixed Ctrl+Z crash
Windows：修复 Ctrl+Z 崩溃

- SDK: Added ability to capture error logging
SDK：添加了捕获错误日志的能力

- Add --system-prompt-file option to override system prompt in print mode
添加 --system-prompt-file 选项以在打印模式下覆盖系统提示

## 1.0.54

- Hooks: Added UserPromptSubmit hook and the current working directory to hook inputs
Hooks：添加了 UserPromptSubmit hook 和当前工作目录到 hook 输入

- Custom slash commands: Added argument-hint to frontmatter
自定义斜杠命令：在 frontmatter 中添加了 argument-hint

- Windows: OAuth uses port 45454 and properly constructs browser URL
Windows：OAuth 使用端口 45454 并正确构造浏览器 URL

- Windows: mode switching now uses alt + m, and plan mode renders properly
Windows：模式切换现在使用 alt + m，并且计划模式正确渲染

- Shell: Switch to in-memory shell snapshot to fix file-related errors
Shell：切换到内存中 shell 快照以修复文件相关错误

## 1.0.53

- Updated @-mention file truncation from 100 lines to 2000 lines
将 @ 提及文件截断从 100 行更新为 2000 行

- Add helper script settings for AWS token refresh: awsAuthRefresh (for foreground operations like aws sso login) and awsCredentialExport (for background operation with STS-like response).
添加用于 AWS 令牌刷新的助手脚本设置：awsAuthRefresh（用于 aws sso login 等前台操作）和 awsCredentialExport（用于具有 STS 类似响应的后台操作）。

## 1.0.52

- Added support for MCP server instructions
添加了对 MCP 服务器指令的支持

## 1.0.51

- Added support for native Windows (requires Git for Windows)
添加了对本机 Windows 的支持（需要 Git for Windows）

- Added support for Bedrock API keys through environment variable AWS_BEARER_TOKEN_BEDROCK
添加了通过环境变量 AWS_BEARER_TOKEN_BEDROCK 对 Bedrock API 密钥的支持

- Settings: /doctor can now help you identify and fix invalid setting files
设置：/doctor 现在可以帮助您识别和修复无效的设置文件

- `--append-system-prompt` can now be used in interactive mode, not just --print/-p.
`--append-system-prompt` 现在可以在交互模式下使用，而不仅仅是 --print/-p。

- Increased auto-compact warning threshold from 60% to 80%
将自动压缩警告阈值从 60% 提高到 80%

- Fixed an issue with handling user directories with spaces for shell snapshots
修复了处理带空格的用户目录进行 shell 快照的问题

- OTEL resource now includes os.type, os.version, host.arch, and wsl.version (if running on Windows Subsystem for Linux)
OTEL 资源现在包括 os.type、os.version、host.arch 和 wsl.version（如果在 Windows 子系统 for Linux 上运行）

- Custom slash commands: Fixed user-level commands in subdirectories
自定义斜杠命令：修复子目录中的用户级命令

- Plan mode: Fixed issue where rejected plan from sub-task would get discarded
计划模式：修复来自子任务的被拒绝计划被丢弃的问题

## 1.0.48

- Fixed a bug in v1.0.45 where the app would sometimes freeze on launch
修复了 v1.0.45 中应用程序有时在启动时冻结的错误

- Added progress messages to Bash tool based on the last 5 lines of command output
根据命令输出的最后 5 行向 Bash 工具添加了进度消息

- Added expanding variables support for MCP server configuration
为 MCP 服务器配置添加了展开变量支持

- Moved shell snapshots from /tmp to ~/.claude for more reliable Bash tool calls
将 shell 快照从 /tmp 移动到 ~/.claude 以实现更可靠的 Bash 工具调用

- Improved IDE extension path handling when Claude Code runs in WSL
改进了当 Claude Code 在 WSL 中运行时的 IDE 扩展路径处理

- Hooks: Added a PreCompact hook
Hooks：添加了 PreCompact hook

- Vim mode: Added c, f/F, t/T
Vim 模式：添加了 c、f/F、t/T

## 1.0.45

- Redesigned Search (Grep) tool with new tool input parameters and features
重新设计搜索（Grep）工具，具有新的工具输入参数和功能

- Disabled IDE diffs for notebook files, fixing "Timeout waiting after 1000ms" error
为笔记本文件禁用 IDE 差异，修复"Timeout waiting after 1000ms"错误

- Fixed config file corruption issue by enforcing atomic writes
通过强制原子写入修复配置文件损坏问题

- Updated prompt input undo to Ctrl+\_ to avoid breaking existing Ctrl+U behavior, matching zsh's undo shortcut
将提示输入撤消更新为 Ctrl+\_ 以避免破坏现有 Ctrl+U 行为，匹配 zsh 的撤消快捷键

- Stop Hooks: Fixed transcript path after /clear and fixed triggering when loop ends with tool call
停止 Hooks：修复了 /clear 后的记录路径并修复了当循环以工具调用结束时的触发

- Custom slash commands: Restored namespacing in command names based on subdirectories. For example, .claude/commands/frontend/component.md is now /frontend:component, not /component.
自定义斜杠命令：基于子目录恢复命令名称中的命名空间。例如，.claude/commands/frontend/component.md 现在是 /frontend:component，而不是 /component。

## 1.0.44

- New /export command lets you quickly export a conversation for sharing
新的 /export 命令允许您快速导出对话以进行共享

- MCP: resource_link tool results are now supported
MCP：现在支持 resource_link 工具结果

- MCP: tool annotations and tool titles now display in /mcp view
MCP：工具注释和工具标题现在在 /mcp 视图中显示

- Changed Ctrl+Z to suspend Claude Code. Resume by running `fg`. Prompt input undo is now Ctrl+U.
将 Ctrl+Z 更改为挂起 Claude Code。通过运行 `fg` 恢复。提示输入撤消现在是 Ctrl+U。

## 1.0.43

- Fixed a bug where the theme selector was saving excessively
修复了主题选择器过度保存的错误

- Hooks: Added EPIPE system error handling
Hooks：添加了 EPIPE 系统错误处理

## 1.0.42

- Added tilde (`~`) expansion support to `/add-dir` command
向 `/add-dir` 命令添加了波浪号（`~`）展开支持

## 1.0.41

- Hooks: Split Stop hook triggering into Stop and SubagentStop
Hooks：将 Stop hook 触发拆分为 Stop 和 SubagentStop

- Hooks: Enabled optional timeout configuration for each command
Hooks：为每个命令启用了可选超时配置

- Hooks: Added "hook_event_name" to hook input
Hooks：向 hook 输入添加了"hook_event_name"

- Fixed a bug where MCP tools would display twice in tool list
修复了 MCP 工具在工具列表中显示两次的错误

- New tool parameters JSON for Bash tool in `tool_decision` event
Bash 工具的新工具参数 JSON 在 `tool_decision` 事件中

## 1.0.40

- Fixed a bug causing API connection errors with UNABLE_TO_GET_ISSUER_CERT_LOCALLY if `NODE_EXTRA_CA_CERTS` was set
修复了如果设置了 `NODE_EXTRA_CA_CERTS` 导致 API 连接错误 UNABLE_TO_GET_ISSUER_CERT_LOCALLY 的错误

## 1.0.39

- New Active Time metric in OpenTelemetry logging
OpenTelemetry 日志记录中的新活动时间指标

## 1.0.38

- Released hooks. Special thanks to community input in https://github.com/anthropics/claude-code/issues/712. Docs: https://code.claude.com/docs/en/hooks
发布 hooks。特别感谢社区在 https://github.com/anthropics/claude-code/issues/712 中的输入。文档：https://code.claude.com/docs/en/hooks

## 1.0.37

- Remove ability to set `Proxy-Authorization` header via ANTHROPIC_AUTH_TOKEN or apiKeyHelper
移除通过 ANTHROPIC_AUTH_TOKEN 或 apiKeyHelper 设置 `Proxy-Authorization` 标头的能力

## 1.0.36

- Web search now takes today's date into context
Web 搜索现在将今天的日期考虑在内

- Fixed a bug where stdio MCP servers were not terminating properly on exit
修复了 stdio MCP 服务器在退出时未正确终止的错误

## 1.0.35

- Added support for MCP OAuth Authorization Server discovery
添加了对 MCP OAuth 授权服务器发现的支持

## 1.0.34

- Fixed a memory leak causing a MaxListenersExceededWarning message to appear
修复了导致出现 MaxListenersExceededWarning 消息的内存泄漏

## 1.0.33

- Improved logging functionality with session ID support
通过会话 ID 改进日志记录功能

- Added prompt input undo functionality (Ctrl+Z and vim 'u' command)
添加了提示输入撤消功能（Ctrl+Z 和 vim 'u' 命令）

- Improvements to plan mode
计划模式的改进

## 1.0.32

- Updated loopback config for litellm
更新了 litellm 的环回配置

- Added forceLoginMethod setting to bypass login selection screen
添加了 forceLoginMethod 设置以绕过登录选择屏幕

## 1.0.31

- Fixed a bug where ~/.claude.json would get reset when file contained invalid JSON
修复了当文件包含无效 JSON 时 ~/.claude.json 被重置的错误

## 1.0.30

- Custom slash commands: Run bash output, @-mention files, enable thinking with thinking keywords
自定义斜杠命令：运行 bash 输出、@ 提及文件、使用思考关键词启用思考

- Improved file path autocomplete with filename matching
通过文件名匹配改进文件路径自动完成

- Added timestamps in Ctrl-r mode and fixed Ctrl-c handling
在 Ctrl-r 模式添加时间戳并修复 Ctrl-c 处理

- Enhanced jq regex support for complex filters with pipes and select
为带有管道和选择器的复杂过滤器增强 jq 正则表达式支持

## 1.0.29

- Improved CJK character support in cursor navigation and rendering
改进光标导航和渲染中的中日韩字符支持

## 1.0.28

- Slash commands: Fix selector display during history navigation
斜杠命令：修复历史导航期间的选择器显示

- Resizes images before upload to prevent API size limit errors
在上传前调整图像大小以防止 API 大小限制错误

- Added XDG_CONFIG_HOME support to configuration directory
添加 XDG_CONFIG_HOME 对配置目录的支持

- Performance optimizations for memory usage
内存使用性能优化

- New attributes (terminal.type, language) in OpenTelemetry logging
OpenTelemetry 日志记录中的新属性（terminal.type、language）

## 1.0.27

- Streamable HTTP MCP servers are now supported
现在支持可流式 HTTP MCP 服务器

- Remote MCP servers (SSE and HTTP) now support OAuth
远程 MCP 服务器（SSE 和 HTTP）现在支持 OAuth

- MCP resources can now be @-mentioned
现在可以 @ 提及 MCP 资源

- /resume slash command to switch conversations within Claude Code
/resume 斜杠命令以在 Claude Code 内切换对话

## 1.0.25

- Slash commands: moved "project" and "user" prefixes to descriptions
斜杠命令：将"项目"和"用户"前缀移动到描述

- Slash commands: improved reliability for command discovery
斜杠命令：改进了命令发现的可靠性

- Improved support for Ghostty
改进了对 Ghostty 的支持

- Improved web search reliability
改进了 Web 搜索可靠性

## 1.0.24

- Improved /mcp output
改进了 /mcp 输出

- Fixed a bug where settings arrays got overwritten instead of merged
修复了设置数组被覆盖而不是合并的错误

## 1.0.23

- Released TypeScript SDK: import @anthropic-ai/claude-code to get started
发布 TypeScript SDK：导入 @anthropic-ai/claude-code 开始使用

- Released Python SDK: pip install claude-code-sdk to get started
发布 Python SDK：pip install claude-code-sdk 开始使用

## 1.0.22

- SDK: Renamed `total_cost` to `total_cost_usd`
SDK：将 `total_cost` 重命名为 `total_cost_usd`

## 1.0.21

- Improved editing of files with tab-based indentation
改进了基于缩进的文件的编辑

- Fix for tool_use without matching tool_result errors
修复了 tool_use 没有匹配 tool_result 的错误

- Fixed a bug where stdio MCP server processes would linger after quitting Claude Code
修复了 stdio MCP 服务器进程在退出 Claude Code 后仍会滞留的错误

## 1.0.18

- Added --add-dir CLI argument for specifying additional working directories
添加了 --add-dir CLI 参数以指定额外的工作目录

- Added streaming input support without require -p flag
添加了无需 -p 标志的流式输入支持

- Improved startup performance and session storage performance
改进了启动性能和会话存储性能

- Added CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR environment variable to freeze working directory for bash commands
添加了 CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR 环境变量以冻结 bash 命令的工作目录

- Added detailed MCP server tools display (/mcp)
添加了详细的 MCP 服务器工具显示（/mcp）

- MCP authentication and permission improvements
MCP 身份验证和权限改进

- Added auto-reconnection for MCP SSE connections on disconnect
为断开连接时的 MCP SSE 连接添加了自动重新连接

- Fixed issue where pasted content was lost when dialogs appeared
修复了对话框出现时粘贴内容丢失的问题

## 1.0.17

- We now emit messages from sub-tasks in -p mode (look for the parent_tool_use_id property)
我们现在在 -p 模式下发出子任务的消息（查找 parent_tool_use_id 属性）

- Fixed crashes when the VS Code diff tool is invoked multiple times quickly
修复了快速多次调用 VS Code 差异工具时的崩溃

- MCP server list UI improvements
MCP 服务器列表 UI 改进

- Update Claude Code process title to display "claude" instead of "node"
更新 Claude Code 进程标题以显示"claude"而不是"node"

## 1.0.11

- Claude Code can now also be used with a Claude Pro subscription
Claude Code 现在也可以通过 Claude Pro 订阅使用

- Added /upgrade for smoother switching to Claude Max plans
添加 /upgrade 以更平滑地切换到 Claude Max 计划

- Improved UI for authentication from API keys and Bedrock/Vertex/external auth tokens
改进了从 API 密钥和 Bedrock/Vertex/外部身份验证令牌进行身份验证的 UI

- Improved shell configuration error handling
改进了 shell 配置错误处理

- Improved todo list handling during compaction
改进了压缩期间待办事项列表的处理

## 1.0.10

- Added markdown table support
添加了 markdown 表格支持

- Improved streaming performance
改进了流式传输性能

## 1.0.8

- Fixed Vertex AI region fallback when using CLOUD_ML_REGION
修复了使用 CLOUD_ML_REGION 时的 Vertex AI 区域回退

- Increased default otel interval from 1s -> 5s
将默认 otel 间隔从 1s 增加到 5s

- Fixed edge cases where MCP_TIMEOUT and MCP_TOOL_TIMEOUT weren't being respected
修复了 MCP_TIMEOUT 和 MCP_TOOL_TIMEOUT 未被尊重的边缘情况

- Fixed a regression where search tools unnecessarily asked for permissions
修复了搜索工具不必要请求权限的回归

- Added support for triggering thinking non-English languages
添加了触发非语言思考的支持

- Improved compacting UI
改进了压缩 UI

## 1.0.7

- Renamed /allowed-tools -> /permissions
重命名 /allowed-tools -> /permissions

- Migrated allowedTools and ignorePatterns from .claude.json -> settings.json
将 allowedTools 和 ignorePatterns 从 .claude.json 迁移到 settings.json

- Deprecated claude config commands in favor of editing settings.json
弃用 claude config 命令，改为编辑 settings.json

- Fixed a bug where --dangerously-skip-permissions sometimes didn't work in --print mode
修复了 --dangerously-skip-permissions 有时在 --print 模式下不起作用的错误

- Improved error handling for /install-github-app
改进了 /install-github-app 的错误处理

- Bugfixes, UI polish, and tool reliability improvements
错误修复、UI 优化和工具可靠性改进

## 1.0.6

- Improved edit reliability for tab-indented files
提高了缩进文件的编辑可靠性

- Respect CLAUDE_CONFIG_DIR everywhere
在各处尊重 CLAUDE_CONFIG_DIR

- Reduced unnecessary tool permission prompts
减少了不必要的工具权限提示

- Added support for symlinks in @file typeahead
在 @file 类型预读中添加了对符号链接的支持

- Bugfixes, UI polish, and tool reliability improvements
错误修复、UI 优化和工具可靠性改进

## 1.0.4

- Fixed a bug where MCP tool errors weren't being parsed correctly
修复了 MCP 工具错误未被正确解析的错误

## 1.0.1

- Added `DISABLE_INTERLEAVED_THINKING` to give users the option to opt out of interleaved thinking.
添加了 `DISABLE_INTERLEAVED_THINKING` 以让用户选择退出交错思考。

- Improved model references to show provider-specific names (Sonnet 3.7 for Bedrock, Sonnet 4 for Console)
改进了模型引用以显示提供商特定名称（Bedrock 的 Sonnet 3.7，Console 的 Sonnet 4）

- Updated documentation links and OAuth process descriptions
更新了文档链接和 OAuth 流程描述

## 1.0.0

- Claude Code is now generally available
Claude Code 现已正式发布

- Introducing Sonnet 4 and Opus 4 models
推出 Sonnet 4 和 Opus 4 模型

## 0.2.125

- Breaking change: Bedrock ARN passed to `ANTHROPIC_MODEL` or `ANTHROPIC_SMALL_FAST_MODEL` should no longer contain an escaped slash (specify `/` instead of `%2F`)
破坏性更改：传递给 `ANTHROPIC_MODEL` 或 `ANTHROPIC_SMALL_FAST_MODEL` 的 Bedrock ARN 不应再包含转义的斜杠（指定 `/` 而不是 `%2F`）

- Removed `DEBUG=true` in favor of `ANTHROPIC_LOG=debug`, to log all requests
移除了 `DEBUG=true`，改为使用 `ANTHROPIC_LOG=debug` 来记录所有请求

## 0.2.117

- Breaking change: --print JSON output now returns nested message objects, for forwards-compatibility as we introduce new metadata fields
破坏性更改：--print JSON 输出现在返回嵌套的消息对象，以在引入新元数据字段时保持前向兼容性

- Introduced settings.cleanupPeriodDays
引入了 settings.cleanupPeriodDays

- Introduced CLAUDE_CODE_API_KEY_HELPER_TTL_MS env var
引入了 CLAUDE_CODE_API_KEY_HELPER_TTL_MS 环境变量

- Introduced --debug mode
引入了 --debug 模式

## 0.2.108

- You can now send messages to Claude while it works to steer Claude in real-time
您现在可以在 Claude 工作时向其发送消息以实时引导 Claude

- Introduced BASH_DEFAULT_TIMEOUT_MS and BASH_MAX_TIMEOUT_MS env vars
引入了 BASH_DEFAULT_TIMEOUT_MS 和 BASH_MAX_TIMEOUT_MS 环境变量

- Fixed a bug where thinking was not working in -p mode
修复了思考在 -p 模式下不工作的错误

- Fixed a regression in /cost reporting
修复了 /cost 报告中的回归

- Deprecated MCP wizard interface in favor of other MCP commands
弃用 MCP 向导界面，改为使用其他 MCP 命令

- Lots of other bugfixes and improvements
大量其他错误修复和改进

## 0.2.107

- CLAUDE.md files can now import other files. Add @path/to/file.md to ./CLAUDE.md to load additional files on launch
CLAUDE.md 文件现在可以导入其他文件。向 ./CLAUDE.md 添加 @path/to/file.md 以在启动时加载其他文件

## 0.2.106

- MCP SSE server configs can now specify custom headers
MCP SSE 服务器配置现在可以指定自定义标头

- Fixed a bug where MCP permission prompt didn't always show correctly
修复了 MCP 权限提示未始终正确显示的错误

## 0.2.105

- Claude can now search the web
Claude 现在可以搜索网络

- Moved system & account status to /status
将系统和账户状态移动到 /status

- Added word movement keybindings for Vim
为 Vim 添加了单词移动键绑定

- Improved latency for startup, todo tool, and file edits
改进了启动、todo 工具和文件编辑的延迟

## 0.2.102

- Improved thinking triggering reliability
改进了思考触发可靠性

- Improved @mention reliability for images and folders
改进了图像和文件夹的 @ 提及可靠性

- You can now paste multiple large chunks into one prompt
您现在可以将多个大块粘贴到一个提示中

## 0.2.100

- Fixed a crash caused by a stack overflow error
修复了由堆栈溢出错误导致的崩溃

- Made db storage optional; missing db support disables --continue and --resume
使数据库存储可选；缺少数据库支持会禁用 --continue 和 --resume

## 0.2.98

- Fixed an issue where auto-compact was running twice
修复了自动压缩运行两次的问题

## 0.2.96

- Claude Code can now also be used with a Claude Max subscription (https://claude.ai/upgrade)
Claude Code 现在也可以通过 Claude Max 订阅使用（https://claude.ai/upgrade）

## 0.2.93

- Resume conversations from where you left off from with "claude --continue" and "claude --resume"
使用"claude --continue"和"claude --resume"从您离开的地方恢复对话

- Claude now has access to a Todo list that helps it stay on track and be more organized
Claude 现在可以访问待办事项列表，帮助它保持正轨并更有条理

## 0.2.82

- Added support for --disallowedTools
添加了对 --disallowedTools 的支持

- Renamed tools for consistency: LSTool -> LS, View -> Read, etc.
为一致性重命名工具：LSTool -> LS、View -> Read 等

## 0.2.75

- Hit Enter to queue up additional messages while Claude is working
在 Claude 工作时按 Enter 排队更多消息

- Drag in or copy/paste image files directly into the prompt
将图像文件直接拖放或复制/粘贴到提示中

- @-mention files to directly add them to context
@ 提及文件以直接将它们添加到上下文中

- Run one-off MCP servers with `claude --mcp-config <path-to-file>`
使用 `claude --mcp-config <path-to-file>` 运行一次性 MCP 服务器

- Improved performance for filename auto-complete
改进了文件名自动完成的性能

## 0.2.74

- Added support for refreshing dynamically generated API keys (via apiKeyHelper), with a 5 minute TTL
添加了刷新动态生成的 API 密钥（通过 apiKeyHelper）的支持，具有 5 分钟 TTL

- Task tool can now perform writes and run bash commands
Task 工具现在可以执行写入和运行 bash 命令

## 0.2.72

- Updated spinner to indicate tokens loaded and tool usage
更新了旋转器以指示加载的令牌和工具使用

## 0.2.70

- Network commands like curl are now available for Claude to use
curl 等网络命令现在可供 Claude 使用

- Claude can now run multiple web queries in parallel
Claude 现在可以并行运行多个 Web 查询

- Pressing ESC once immediately interrupts Claude in Auto-accept mode
在自动接受模式下按 ESC 一次立即中断 Claude

## 0.2.69

- Fixed UI glitches with improved Select component behavior
通过改进 Select 组件行为修复 UI 小故障

- Enhanced terminal output display with better text truncation logic
通过更好的文本截断逻辑增强终端输出显示

## 0.2.67

- Shared project permission rules can be saved in .claude/settings.json
共享项目权限规则可以保存在 .claude/settings.json 中

## 0.2.66

- Print mode (-p) now supports streaming output via --output-format=stream-json
打印模式（-p）现在通过 --output-format=stream-json 支持流式输出

- Fixed issue where pasting could trigger memory or bash mode unexpectedly
修复了粘贴可能意外触发内存或 bash 模式的问题

## 0.2.63

- Fixed an issue where MCP tools were loaded twice, which caused tool call errors
修复了 MCP 工具被加载两次导致工具调用错误的问题

## 0.2.61

- Navigate menus with vim-style keys (j/k) or bash/emacs shortcuts (Ctrl+n/p) for faster interaction
使用 vim 风格键（j/k）或 bash/emacs 快捷键（Ctrl+n/p）导航菜单以实现更快的交互

- Enhanced image detection for more reliable clipboard paste functionality
增强图像检测以实现更可靠的剪贴板粘贴功能

- Fixed an issue where ESC key could crash the conversation history selector
修复了 ESC 键可能导致对话历史记录选择器崩溃的问题

## 0.2.59

- Copy+paste images directly into your prompt
直接将图像复制+粘贴到您的提示中

- Improved progress indicators for bash and fetch tools
改进了 bash 和 fetch 工具的进度指示器

- Bugfixes for non-interactive mode (-p)
非交互模式（-p）的错误修复

## 0.2.54

- Quickly add to Memory by starting your message with '#'
通过以'#'开头消息快速添加到内存

- Press ctrl+r to see full output for long tool results
按 ctrl+r 查看长工具结果的完整输出

- Added support for MCP SSE transport
添加了对 MCP SSE 传输的支持

## 0.2.53

- New web fetch tool lets Claude view URLs that you paste in
新的 Web 获取工具让 Claude 查看您粘贴的 URL

- Fixed a bug with JPEG detection
修复了 JPEG 检测错误

## 0.2.50

- New MCP "project" scope now allows you to add MCP servers to .mcp.json files and commit them to your repository
新的 MCP"项目"范围现在允许您将 MCP 服务器添加到 .mcp.json 文件并将它们提交到您的存储库

## 0.2.49

- Previous MCP server scopes have been renamed: previous "project" scope is now "local" and "global" scope is now "user"
以前的 MCP 服务器范围已重命名：以前的"项目"范围现在是"本地"，"全局"范围现在是"用户"

## 0.2.47

- Press Tab to auto-complete file and folder names
按 Tab 自动完成文件和文件夹名称

- Press Shift + Tab to toggle auto-accept for file edits
按 Shift + Tab 切换文件编辑的自动接受

- Automatic conversation compaction for infinite conversation length (toggle with /config)
自动对话压缩以实现无限对话长度（使用 /config 切换）

## 0.2.44

- Ask Claude to make a plan with thinking mode: just say 'think' or 'think harder' or even 'ultrathink'
要求 Claude 使用思考模式制定计划：只需说'think'或'think harder'甚至'ultrathink'

## 0.2.41

- MCP server startup timeout can now be configured via MCP_TIMEOUT environment variable
MCP 服务器启动超时现在可以通过 MCP_TIMEOUT 环境变量配置

- MCP server startup no longer blocks the app from starting up
MCP 服务器启动不再阻止应用程序启动

## 0.2.37

- New /release-notes command lets you view release notes at any time
新的 /release-notes 命令允许您随时查看发行说明

- `claude config add/remove` commands now accept multiple values separated by commas or spaces
`claude config add/remove` 命令现在接受以逗号或空格分隔的多个值

## 0.2.36

- Import MCP servers from Claude Desktop with `claude mcp add-from-claude-desktop`
使用 `claude mcp add-from-claude-desktop` 从 Claude Desktop 导入 MCP 服务器

- Add MCP servers as JSON strings with `claude mcp add-json <n> <json>`
使用 `claude mcp add-json <n> <json>` 将 MCP 服务器添加为 JSON 字符串

## 0.2.34

- Vim bindings for text input - enable with /vim or /config
文本输入的 Vim 绑定 - 使用 /vim 或 /config 启用

## 0.2.32

- Interactive MCP setup wizard: Run "claude mcp add" to add MCP servers with a step-by-step interface
交互式 MCP 设置向导：运行"claude mcp add"以通过分步界面添加 MCP 服务器

- Fix for some PersistentShell issues
一些 PersistentShell 问题的修复

## 0.2.31

- Custom slash commands: Markdown files in .claude/commands/ directories now appear as custom slash commands to insert prompts into your conversation
自定义斜杠命令：.claude/commands/ 目录中的 Markdown 文件现在显示为自定义斜杠命令，以将提示插入到您的对话中

- MCP debug mode: Run with --mcp-debug flag to get more information about MCP server errors
MCP 调试模式：使用 --mcp-debug 标志运行以获取有关 MCP 服务器错误的更多信息

## 0.2.30

- Added ANSI color theme for better terminal compatibility
添加了 ANSI 颜色主题以实现更好的终端兼容性

- Fixed issue where slash command arguments weren't being sent properly
修复了斜杠命令参数未正确发送的问题

- (Mac-only) API keys are now stored in macOS Keychain
-（仅限 Mac）API 密钥现在存储在 macOS 钥匙串中

## 0.2.26

- New /approved-tools command for managing tool permissions
新的 /approved-tools 命令用于管理工具权限

- Word-level diff display for improved code readability
单词级差异显示以提高代码可读性

- Fuzzy matching for slash commands
斜杠命令的模糊匹配

## 0.2.21

- Fuzzy matching for /commands
/commands 的模糊匹配