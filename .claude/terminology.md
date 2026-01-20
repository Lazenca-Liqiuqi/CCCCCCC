# Claude Code 翻译术语表

本文档用于确保项目翻译的一致性和准确性，包含 Claude Code CHANGELOG 和 Anthropic Engineering Blog 两部分术语。

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

---

# Anthropic Engineering Blog 专用术语

本部分术语专门用于 Anthropic Engineering Blog 文章翻译。

## AI 与代理系统术语

| 英文术语 | 中文翻译 | 说明 |
|---------|---------|------|
| Retrieval-Augmented Generation | 检索增强生成 (RAG) | 也可简称为 RAG |
| contextual retrieval | 上下文检索 | - |
| embedding | 嵌入 / 向量嵌入 | 根据上下文选择 |
| vector embedding | 向量嵌入 | - |
| vector database | 向量数据库 | - |
| semantic similarity | 语义相似度 | - |
| BM25 | BM25 | 保持原文 |
| TF-IDF | TF-IDF | 保持原文 |
| knowledge base | 知识库 | - |
| chunk | 文本块 / 块 | 文档分割的单位 |
| corpus | 语料库 | - |
| reranking | 重排序 | - |
| prompt caching | 提示缓存 | - |
| multi-agent | 多代理 | - |
| agent system | 代理系统 | - |
| tool use | 工具使用 | - |
| function calling | 函数调用 | - |
| long-running agent | 长运行代理 | - |
| harness | 控制 / 管理 | 根据上下文 |
| research system | 研究系统 | - |
| cookbook | 食谱 / 示例代码 | 示例代码集合 |
| postmortem | 复盘 / 事后分析 | - |
| contextual embeddings | 上下文嵌入 | - |
| lexical matching | 词法匹配 | - |
| rank fusion | 排名融合 | - |
| saturation function | 饱和函数 | - |
| exact match | 精确匹配 | - |
| downstream task | 下游任务 | - |
| orchestrate | 编排 | 协调多个代理 |
| equip | 装备 | 为代理提供工具 |
| integrate | 集成 | 系统集成 |

## 动词翻译（Engineering Blog）

| 英文动词 | 中文翻译 | 示例 |
|---------|---------|------|
| enhance | 增强 / 增强...的能力 | enhance model's knowledge → 增强模型的知识 |
| retrieve | 检索 | retrieve information → 检索信息 |
| encode | 编码 | encode meaning → 编码含义 |
| append | 附加 / 追加 | append to prompt → 附加到提示词 |
| leverage | 利用 / 借助 | leverage both techniques → 利用两种技术 |
| scale | 扩展 / 规模化 | scale to larger bases → 扩展到更大的知识库 |
| refine | 改进 / 优化 | refine this concept → 改进这一概念 |
| deploy | 部署 | deploy solution → 部署解决方案 |

## 文章标题对照

| 英文标题 | 中文标题 |
|---------|---------|
| Introducing Contextual Retrieval | 上下文检索技术介绍 |
| Building effective agents | 构建有效代理 |
| Claude Code Best Practices | Claude Code 最佳实践 |
| How We Built Our Multi-Agent Research System | 我们如何构建多代理研究系统 |
| A Postmortem of Three Recent Issues | 三个近期问题的复盘 |
| Effective Context Engineering for AI Agents | AI 代理的有效上下文工程 |
| Building Agents with the Claude Agent SDK | 使用 Claude Agent SDK 构建代理 |
| Equipping Agents for the Real World with Agent Skills | 为现实世界装备代理技能 |
| Code Execution with MCP | 使用 MCP 执行代码 |
| Effective Harnesses for Long-Running Agents | 长运行代理的有效管理 |
| Introducing SWE Bench Verified | SWE Bench Verified 介绍 |
| Think tool: Helping Claude navigate complex situations | Think 工具：帮助 Claude 处理复杂情况 |
| Desktop extensions: MCP server installation | 桌面扩展：MCP 服务器安装 |
| Writing Effective Tools for Agents | 为代理编写有效的工具 |
| Beyond Permission Prompts | 超越权限提示词 |
| Advanced Tool Use on the Claude Developer Platform | Claude 开发者平台上的高级工具使用 |

## 更新日志

- **2025-01-20**: 添加 Engineering Blog 专用术语，扩展为通用术语表
- **2025-01-18**: 创建术语表，用于 2.1.2-2.1.6 版本翻译
