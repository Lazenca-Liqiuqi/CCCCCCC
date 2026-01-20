# Claude Code CHANGELOG 翻译术语表

本文档用于确保 CHANGELOG 双语对照翻译的一致性和准确性。

## 核心术语对照

| 英文术语 | 中文翻译 | 说明 |
|---------|---------|------|
| skill | 技能 | - |
| slash command | 斜杠命令 | - |
| hook | hook | 保持英文，技术术语 |
| agent | 代理 | - |
| subagent | 子代理 | - |
| sub-agent | 子代理 | - |
| permission | 权限 | - |
| token | 令牌 | 用于认证/计数 |
| context window | 上下文窗口 | - |
| plugin | 插件 | - |
| marketplace | 市场/市场place | 根据上下文 |
| MCP | MCP | 保持原文 |
| OAuth | OAuth | 保持原文 |
| SDK | SDK | 保持原文 |
| API | API | 保持原文 |
| CLI | CLI | 保持原文 |
| IDE | IDE | 保持原文 |
| LSP | LSP | 保持原文 |
| frontmatter | frontmatter | 保持原文，技术术语 |
| hot-reload | 热重载 | - |
| background task | 后台任务 | - |
| environment variable | 环境变量 | - |
| flag | 标志 | CLI 参数 |
| bash command | bash 命令 | - |
| wildcard pattern | 通配符模式 | - |
| forked | 分支 | Git/进程相关 |
| auto-backgrounding | 自动后台化 | - |
| injection vulnerability | 注入漏洞 | 安全相关 |
| command injection | 命令注入 | 安全相关 |
| memory leak | 内存泄漏 | - |
| tree-sitter | tree-sitter | 保持原文 |
| inode | inode | 保持原文 |
| Vim motions | Vim 动作 | - |
| text object | 文本对象 | Vim 术语 |
| yank | 复制 | Vim 术语 |
| paste | 粘贴 | - |
| indent/dedent | 缩进/取消缩进 | - |
| autocomplete | 自动完成 | - |
| status line | 状态栏 | - |
| spinner | 加载指示器/旋转器 | 根据上下文 |
| compaction | 压缩 | 对话压缩 |
| fuzzy matching | 模糊匹配 | - |
| typeahead | 输入提示/自动补全提示 | - |

## 产品名称

| 英文名称 | 中文翻译 |
|---------|---------|
| Claude Code | Claude Code | 保持原文 |
| Claude Code Desktop | Claude Code 桌面版 | - |
| Claude in Chrome | Chrome 中的 Claude | - |
| VS Code | VS Code | 保持原文 |
| iTerm2 | iTerm2 | 保持原文 |
| WezTerm | WezTerm | 保持原文 |
| Ghostty | Ghostty | 保持原文 |
| Kitty | Kitty | 保持原文 |
| Alacritty | Alacritty | 保持原文 |
| Zed | Zed | 保持原文 |
| Warp | Warp | 保持原文 |
| Bedrock | Bedrock | 保持原文 |
| Vertex AI | Vertex AI | 保持原文 |

## 动词翻译规范

| 英文动词 | 中文翻译 | 示例 |
|---------|---------|------|
| Added | 添加了 | Added support for... → 添加了...的支持 |
| Fixed | 修复了 | Fixed a bug where... → 修复了...的问题 |
| Improved | 改进了/改善了 | Improved performance → 改进了性能 |
| Changed | 更改了/改变了 | Changed behavior → 改变了行为 |
| Removed | 移除了 | Removed feature → 移除了功能 |
| Deprecated | 弃用了 | Deprecated option → 弃用了选项 |
| Updated | 更新了 | Updated model → 更新了模型 |
| Reduced | 减少了 | Reduced latency → 减少了延迟 |
| Increased | 增加了 | Increased performance → 增加了性能 |
| Enhanced | 增强了 | Enhanced UI → 增强了 UI |
| Optimized | 优化了 | Optimized performance → 优化了性能 |
| Refactored | 重构了 | Refactored code → 重构了代码 |
| Merged | 合并了 | Merged commands → 合并了命令 |
| Split | 拆分了 | Split feature → 拆分了功能 |
| Renamed | 重命名了 | Renamed command → 重命名了命令 |
| Introduced | 引入了 | Introduced feature → 引入了功能 |
| Released | 发布了 | Released feature → 发布了功能 |
| Enabled | 启用了 | Enabled feature → 启用了功能 |
| Disabled | 禁用了 | Disabled feature → 禁用了功能 |

## 特殊格式处理规则

### 1. 代码和命令示例
```markdown
- Use `Bash(npm *)` wildcard pattern
翻译：使用 `Bash(npm *)` 通配符模式
```
**规则：保留代码块中的英文，不翻译代码**

### 2. 键盘快捷键
```markdown
- Press Ctrl+V to paste
翻译：按 Ctrl+V 粘贴
```
**规则：保持快捷键格式，仅翻译动作词**

### 3. 功能开关和配置项
```markdown
- Added `IS_DEMO` environment variable
翻译：添加了 `IS_DEMO` 环境变量
```
**规则：保留配置项名称原文，翻译描述部分**

### 4. 引用和链接
```markdown
- See [documentation](https://...)
翻译：参见[文档](https://...)
```
**规则：翻译链接文本，保留 URL**

### 5. 专有名词
```markdown
- Claude Code Desktop
翻译：Claude Code 桌面版
```
**规则：保留产品名，添加中文说明**

## 翻译质量检查清单

- [ ] 术语一致性（对照术语表）
- [ ] 语句通顺性（符合中文表达习惯）
- [ ] 技术准确性（不改变技术含义）
- [ ] 格式完整性（代码、链接等保持原样）
- [ ] 无漏译（每个英文条目都有对应翻译）

## 更新日志

- **2025-01-18**: 创建术语表，用于 2.1.2-2.1.6 版本翻译
