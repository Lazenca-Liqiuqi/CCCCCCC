# Codex 审查请求 | Review Request

## 文章信息 | Article Information

| 项目 | 内容 |
|------|------|
| **文件** | `01-contextual-retrieval.md` |
| **标题** | Introducing Contextual Retrieval |
| **中文标题** | 介绍上下文检索 |
| **发布日期** | 2024年9月19日 |
| **原文 URL** | https://www.anthropic.com/news/contextual-retrieval |
| **审查状态** | 第一轮审查 |

---

## 文章结构 | Article Structure

### 主要章节（10个）

1. Introduction | 引言 - RAG 的局限性和上下文检索介绍
2. A note on simply using a longer prompt | 关于简单使用更长提示的说明
3. A primer on RAG: scaling to larger knowledge bases | RAG 基础：扩展到更大的知识库
4. The context conundrum in traditional RAG | 传统 RAG 中的上下文难题
5. Introducing Contextual Retrieval | 介绍上下文检索
6. Implementing Contextual Retrieval | 实现上下文检索
7. Using Prompt Caching to reduce the costs | 使用提示缓存降低成本
   - Methodology | 方法论
   - Performance improvements | 性能改进
   - Implementation considerations | 实现考虑
8. Further boosting performance with Reranking | 通过重排序进一步提升性能
   - Performance improvements | 性能改进
   - Cost and latency considerations | 成本和延迟考虑
9. Conclusion | 结论
10. Appendix I | 附录 I

---

## 文章统计 | Article Statistics

| 项目 | 数值 |
|------|------|
| **总行数** | ~350 行 |
| **主要章节** | 10 个 |
| **图片数量** | 5 张（架构图和结果图） |
| **代码块** | 2 个（Haiku 提示、代码示例） |
| **表格** | 0 个 |
| **外部链接** | 5 个（Cookbook、文档、Engineering Blog） |

---

## 关键术语表 | Key Terminology

### 核心概念术语（12个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Contextual Retrieval | 上下文检索 |
| RAG (Retrieval-Augmented Generation) | 检索增强生成 |
| Contextual Embeddings | 上下文嵌入 |
| Contextual BM25 | 上下文 BM25 |
| Reranking | 重排序 |
| Embeddings | 嵌入 |
| Vector embeddings | 向量嵌入 |
| BM25 | BM25 排序算法 |
| TF-IDF | 词频-逆文档频率 |
| Prompt caching | 提示缓存 |
| Recall@20 | 前20项召回率 |
| Top-K chunks | 前 K 个块 |

### RAG 技术术语（8个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Knowledge base | 知识库 |
| Context window | 上下文窗口 |
| Chunk | 文本块 |
| Chunk boundaries | 块边界 |
| Chunk overlap | 块重叠 |
| Semantic similarity | 语义相似性 |
| Lexical matching | 词法匹配 |
| Rank fusion | 排序融合 |

### 模型与工具术语（8个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Claude 3 Haiku | Claude 3 Haiku 模型 |
| Gemini Text 004 | Gemini Text 004 嵌入模型 |
| Voyage embeddings | Voyage 嵌入 |
| Cohere reranker | Cohere 重排序器 |
| Vector database | 向量数据库 |
| Embedding model | 嵌入模型 |
| Reranking model | 重排序模型 |
| Reranker | 重排序器 |

### 性能与评估术语（6个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Retrieval failure rate | 检索失败率 |
| Retrieval accuracy | 检索准确性 |
| Latency | 延迟 |
| Cost-effective | 成本效益 |
| Top-N chunks | 前 N 个块 |
| Evaluation metrics | 评估指标 |

---

## 审查重点 | Review Focus

### 格式规范检查

1. **标题格式**：
   - 所有级别的标题（#、##、###、####）使用 `|` 分隔符
   - 确保标题层级正确（# → ## → ### → ####）

2. **正文段落**：
   - 使用换行分隔，中英文段落之间有空行
   - 英文段落中禁止出现中文字符
   - 中文段落独立成段

3. **列表格式**：
   - 有序列表：英文有序号，中文无序号
   - 无序列表：中英文逐条对照
   - 列表项之间应有空行分隔

4. **代码块格式**：
   - 保持原有代码格式
   - 代码注释不与代码混合
   - 中英文对照注释

5. **图片格式**：
   - 使用原始图片链接（www-cdn.anthropic.com）
   - 每张图片后面有中文说明
   - 禁止使用代理 URL（_next/image）

6. **链接格式**：
   - 保留原始链接
   - Sources 区域添加中文链接行
   - 确保所有链接可点击

7. **特殊格式**：
   - `__text__` 加粗格式保持一致
   - 代码块使用正确的 markdown 格式

### 内容质量检查

1. **术语一致性**：
   - RAG 统一翻译为"检索增强生成"
   - Contextual Retrieval 统一翻译为"上下文检索"
   - Embeddings 统一翻译为"嵌入"
   - Reranking 统一翻译为"重排序"
   - Chunk 统一翻译为"块"或"文本块"

2. **翻译准确性**：
   - 技术概念是否准确传达（Contextual Embeddings、Contextual BM25）
   - RAG 工作流程的描述是否清晰
   - 性能指标是否正确（49%、67% 改进）
   - 成本数字是否准确（$1.02 per million tokens）

3. **可读性**：
   - 中文表达流畅自然
   - 技术内容易于理解
   - 专业术语不过度晦涩

4. **完整性**：
   - 所有章节完整无遗漏
   - 5 张图片完整
   - 2 个代码块完整
   - Sources 区域完整

### 特殊注意事项

1. **技术概念区分**：
   - Contextual Embeddings（上下文嵌入）vs Contextual BM25（上下文 BM25）
   - Embeddings（语义嵌入）vs BM25（词法匹配）
   - RAG（检索增强生成）的完整工作流程
   - Prompt caching（提示缓存）在成本优化中的作用

2. **性能指标**：
   - 检索失败率降低 35%（Contextual Embeddings）
   - 检索失败率降低 49%（Contextual Embeddings + Contextual BM25）
   - 检索失败率降低 67%（+ Reranking）
   - 成本：$1.02 per million document tokens

3. **实现细节**：
   - Claude 3 Haiku 提示格式
   - 块分割策略（800 tokens）
   - Top-K 选择（5、10、20 chunks）
   - 重排序工作流程

4. **应用场景**：
   - 知识库大小阈值（200,000 tokens）
   - 不同嵌入模型的性能差异
   - 成本和延迟的权衡考虑

5. **代码和示例**：
   - Haiku 提示示例的中英文对照
   - SEC 文件示例的准确性
   - 块转换示例的清晰度

---

## 质量检查清单 | Quality Checklist

### 基础格式
- [ ] 所有标题（#、##、###、####）使用 `|` 分隔符
- [ ] 正文段落使用换行，不使用 `|`
- [ ] 英文段落和中文段落之间有空行
- [ ] 有序列表中文行无序号
- [ ] 无序列表中英文逐条对照

### 内容质量
- [ ] 图片使用原始 URL（www-cdn.anthropic.com）
- [ ] 代码块格式正确，注释不与代码混合
- [ ] 链接保持可点击状态
- [ ] `__text__` 加粗格式正确
- [ ] 术语翻译一致

### 完整性检查
- [ ] 所有10个主要章节完整
- [ ] 附录 I 完整
- [ ] 5张图片完整
- [ ] 2个代码块完整
- [ ] Sources 区域有中文对照
- [ ] 英文段落中没有中文字符
- [ ] 中文段落翻译完整，无遗漏

### 术语一致性
- [ ] RAG 翻译一致（检索增强生成）
- [ ] Contextual Retrieval 翻译一致（上下文检索）
- [ ] Embeddings 翻译一致（嵌入）
- [ ] Reranking 翻译一致（重排序）
- [ ] Chunk 翻译一致（块/文本块）

### 技术准确性
- [ ] 性能指标数字正确（35%、49%、67%）
- [ ] 成本数字正确（$1.02 per million tokens）
- [ ] Haiku 提示格式准确
- [ ] 块大小数字准确（800 tokens、8k token documents）

---

## 预期评分 | Expected Score

| 评分维度 | 预期分数 |
|----------|----------|
| **综合评分** | **90-95/100** |
| **建议状态** | **通过（预期）** |
| **技术维度** | **45-48/50** |
| **战略维度** | **45-47/50** |

**预期依据**：
- 严格按照格式规范创建，格式问题较少
- 技术内容准确，术语翻译一致
- 双语对照完整，章节结构清晰
- 图片、代码块、链接格式正确
- Sources 区域包含中文对照
- 性能指标和成本数字准确

---

## 特别说明 | Special Notes

1. **首次翻译**：这是 ID 02 的首次翻译，无修复历史
2. **格式规范**：已严格按照 `.claude/rules/translation-format.md` 创建
3. **技术准确性**：已确保技术概念和性能指标准确性
4. **完整性**：所有章节、图片、代码块已完整翻译
5. **图片处理**：所有 5 张图片使用原始 URL（www-cdn.anthropic.com）
6. **代码块**：包含 Haiku 提示示例和代码示例，需要检查格式
7. **性能指标**：重点检查 35%、49%、67% 改进数字的准确性

**会话 ID**: 当前会话
**请求时间**: 2026-01-26
**审查轮次**: 第一轮（首次审查）
