# Anthropic Engineering Articles 翻译请求

## 任务说明

请将以下 Anthropic Engineering Blog 文章翻译成简体中文，并按照指定的双语对照格式输出。

## 翻译规范

### 1. 双语对照格式

文章应采用**段落级双语对照**格式，具体规则：

```markdown
# English Title
# 英文标题的中文翻译

English paragraph content here. This is the original text from the article.
这里是英文段落内容的中文翻译。这是文章原文的翻译。

## English Subheading
## 英文子标题的翻译

Another paragraph in English. Technical terms like **RAG**, **API**, and **SDK** should be kept in original form.
另一个英文段落。像 **RAG**、**API** 和 **SDK** 这样的技术术语应保持原文形式。

### Code Example

```python
# Code comments can be translated
def example_function():
    return "code remains in English"
```
```

**重要格式规则**：
- 每个英文段落后紧跟中文翻译（无空行）
- 段落之间保持一个空行
- 标题采用双语对照（英文标题 + 中文翻译，同一行或相邻行）
- 代码块保持原样，不翻译代码
- 链接保留URL，翻译链接文本

### 2. 术语一致性

#### 2.1 Claude Code 术语（继承 CHANGELOG 术语表）

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
| MCP | MCP |
| SDK | SDK |
| API | API |
| CLI | CLI |
| IDE | IDE |
| environment variable | 环境变量 |
| fuzzy matching | 模糊匹配 |
| autocomplete | 自动完成 |

#### 2.2 Engineering Blog 专用术语

| 英文 | 中文 |
|------|------|
| Retrieval-Augmented Generation | 检索增强生成 (RAG) |
| contextual retrieval | 上下文检索 |
| embedding | 嵌入 / 向量嵌入 |
| vector embedding | 向量嵌入 |
| vector database | 向量数据库 |
| semantic similarity | 语义相似度 |
| BM25 | BM25（保持原文） |
| TF-IDF | TF-IDF（保持原文） |
| knowledge base | 知识库 |
| chunk | 文本块 / 块 |
| corpus | 语料库 |
| reranking | 重排序 |
| prompt caching | 提示缓存 |
| context window | 上下文窗口 |
| multi-agent | 多代理 |
| agent system | 代理系统 |
| tool use | 工具使用 |
| function calling | 函数调用 |
| Model Context Protocol | Model Context Protocol (MCP) |
| long-running agent | 长运行代理 |
| harness | 控制 / 管理（根据上下文） |
| research system | 研究系统 |
| cookbook | 食谱 / 示例代码 |
| postmortem | 复盘 / 事后分析 |
| contextual embeddings | 上下文嵌入 |
| lexical matching | 词法匹配 |
| rank fusion | 排名融合 |
| saturation function | 饱和函数 |
| exact match | 精确匹配 |
| downstream task | 下游任务 |

### 3. 动词翻译

| 英文 | 中文 | 示例 |
|------|------|------|
| enhance | 增强 / 增强...的能力 | enhance model's knowledge → 增强模型的知识 |
| retrieve | 检索 | retrieve information → 检索信息 |
| encode | 编码 | encode meaning → 编码含义 |
| append | 附加 / 追加 | append to prompt → 附加到提示词 |
| leverage | 利用 / 借助 | leverage both techniques → 利用两种技术 |
| scale | 扩展 / 规模化 | scale to larger bases → 扩展到更大的知识库 |
| refine | 改进 / 优化 | refine this concept → 改进这一概念 |
| deploy | 部署 | deploy solution → 部署解决方案 |
| orchestrate | 编排 | orchestrate agents → 编排代理 |
| equip | 装备 | equip agents with tools → 为代理装备工具 |
| integrate | 集成 | integrate with system → 与系统集成 |

### 4. 特殊格式处理

#### 4.1 代码块
```markdown
**规则：保持代码原样，不翻译代码内容**
代码中的注释可以翻译，但变量名、函数名、字符串内容保持英文
```

#### 4.2 链接
```markdown
[Original link text](https://example.com)
[原文链接文本的翻译](https://example.com)

**规则：翻译链接文本，保留 URL**
```

#### 4.3 加粗强调
```markdown
**Important term** → **重要术语**
**规则：翻译强调内容，保留加粗格式**
```

#### 4.4 列表
```markdown
- First item in English
第一项英文的中文翻译

- Second item in English
第二项英文的中文翻译

**规则：每个列表项进行双语对照**
```

### 5. 翻译质量要求

- **准确性**：准确传达技术概念，不曲解原文含义
- **通顺性**：符合中文表达习惯，语句流畅自然
- **一致性**：严格遵循术语表，保持全文术语统一
- **完整性**：不漏译任何段落、标题或说明
- **格式性**：保持 Markdown 格式规范，代码块和链接格式正确

### 6. 文章元数据处理

每篇文章开头的元数据保持英文：

```markdown
# English Title
# 英文标题

**Published:** Sep 19, 2024
**发布日期：** 2024年9月19日

**Author:** Daniel Ford
**作者：** Daniel Ford

---

**规则：元数据字段名保持英文，字段值可翻译或保留**
```

---

## 待翻译内容

{{ARTICLE_CONTENT}}

---

## 输出要求

请按照上述双语对照格式输出翻译结果：

1. 标题采用双语（英文 + 中文）
2. 元数据保持格式规范
3. 段落采用双语对照（英文段落后紧跟中文翻译）
4. 代码块保持原样
5. 严格遵循术语表
6. 保持 Markdown 格式完整

输出应该是完整的文章翻译，可以直接保存为 `.md` 文件。
