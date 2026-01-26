# Introducing Contextual Retrieval | 介绍上下文检索

For an AI model to be useful in specific contexts, it often needs access to background knowledge. For example, customer support chatbots need knowledge about the specific business they're being used for, and legal analyst bots need to know about a vast array of past cases.

AI 模型要在特定场景中有用，通常需要访问背景知识。例如，客户支持聊天机器人需要了解它们所服务的特定业务的知识，而法律分析机器人需要知道大量过往案例。

Developers typically enhance an AI model's knowledge using Retrieval-Augmented Generation (RAG). RAG is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt, significantly enhancing the model's response. The problem is that traditional RAG solutions remove context when encoding information, which often results in the system failing to retrieve the relevant information from the knowledge base.

开发人员通常使用检索增强生成（RAG）来增强 AI 模型的知识。RAG 是一种从知识库中检索相关信息并将其附加到用户提示的方法，显著增强模型的响应。问题是传统 RAG 解决方案在编码信息时会移除上下文，这通常导致系统无法从知识库中检索到相关信息。

In this post, we outline a method that dramatically improves the retrieval step in RAG. The method is called "Contextual Retrieval" and uses two sub-techniques: Contextual Embeddings and Contextual BM25. This method can reduce the number of failed retrievals by 49% and, when combined with reranking, by 67%. These represent significant improvements in retrieval accuracy, which directly translates to better performance in downstream tasks.

在本文中，我们概述了一种显著改进 RAG 检索步骤的方法。该方法称为"上下文检索"，使用两种子技术：上下文嵌入和上下文 BM25。该方法可以将检索失败率降低 49%，当结合重排序时，可以降低 67%。这些代表了检索准确性的显著改进，直接转化为下游任务更好的性能。

You can easily deploy your own Contextual Retrieval solution with Claude with our [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval).

您可以使用我们的 [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval) 轻松部署自己的上下文检索解决方案。

---

### A note on simply using a longer prompt | 关于简单使用更长提示的说明

Sometimes the simplest solution is the best. If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods.

有时最简单的解决方案就是最好的。如果您的知识库小于 200,000 个 token（约 500 页材料），您只需将整个知识库包含在提供给模型的提示中，无需 RAG 或类似方法。

A few weeks ago, we released [prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) for Claude, which makes this approach significantly faster and more cost-effective. Developers can now cache frequently used prompts between API calls, reducing latency by > 2x and costs by up to 90% (you can see how it works by reading our [prompt caching cookbook](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)).

几周前，我们为 Claude 发布了[提示缓存](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)，这使这种方法显著更快且更具成本效益。开发人员现在可以在 API 调用之间缓存经常使用的提示，将延迟降低 > 2 倍，成本降低高达 90%（您可以通过阅读我们的[提示缓存 cookbook](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)来了解它的工作原理）。

However, as your knowledge base grows, you'll need a more scalable solution. That's where Contextual Retrieval comes in.

然而，随着知识库的增长，您将需要更具可扩展性的解决方案。这就是上下文检索的用武之地。

---

## A primer on RAG: scaling to larger knowledge bases | RAG 基础：扩展到更大的知识库

For larger knowledge bases that don't fit within the context window, RAG is the typical solution. RAG works by preprocessing a knowledge base using the following steps:

对于不适合上下文窗口的更大知识库，RAG 是典型的解决方案。RAG 通过以下步骤预处理知识库来工作：

1. Break down the knowledge base (the "corpus" of documents) into smaller chunks of text, usually no more than a few hundred tokens;
将知识库（文档的"语料库"）分解为较小的文本块，通常不超过几百个 token；

2. Use an embedding model to convert these chunks into vector embeddings that encode meaning;
使用嵌入模型将这些块转换为编码意义的向量嵌入；

3. Store these embeddings in a vector database that allows for searching by semantic similarity.
将这些嵌入存储在允许通过语义相似性搜索的向量数据库中。

At runtime, when a user inputs a query to the model, the vector database is used to find the most relevant chunks based on semantic similarity to the query. Then, the most relevant chunks are added to the prompt sent to the generative model.

在运行时，当用户向模型输入查询时，向量数据库用于根据与查询的语义相似性找到最相关的块。然后，最相关的块被添加到发送给生成模型的提示中。

While embedding models excel at capturing semantic relationships, they can miss crucial exact matches. Fortunately, there's an older technique that can assist in these situations. BM25 (Best Matching 25) is a ranking function that uses lexical matching to find precise word or phrase matches. It's particularly effective for queries that include unique identifiers or technical terms.

虽然嵌入模型擅长捕捉语义关系，但它们可能会错过关键的精确匹配。幸运的是，有一种较旧的技术可以在这些情况下提供帮助。BM25（最佳匹配 25）是一种使用词法匹配来查找精确单词或短语匹配的排序函数。它对于包含唯一标识符或技术术语的查询特别有效。

BM25 works by building upon the TF-IDF (Term Frequency-Inverse Document Frequency) concept. TF-IDF measures how important a word is to a document in a collection. BM25 refines this by considering document length and applying a saturation function to term frequency, which helps prevent common words from dominating the results.

BM25 通过建立在 TF-IDF（词频-逆文档频率）概念上来工作。TF-IDF 衡量单词对集合中文档的重要性。BM25 通过考虑文档长度并对词频应用饱和函数来改进这一点，这有助于防止常见词主导结果。

Here's how BM25 can succeed where semantic embeddings fail: Suppose a user queries "Error code TS-999" in a technical support database. An embedding model might find content about error codes in general, but could miss the exact "TS-999" match. BM25 looks for this specific text string to identify the relevant documentation.

BM25 如何在语义嵌入失败的地方成功：假设用户在技术支持数据库中查询"错误代码 TS-999"。嵌入模型可能会找到关于错误代码的一般内容，但可能会错过精确的"TS-999"匹配。BM25 查找这个特定的文本字符串以识别相关文档。

RAG solutions can more accurately retrieve the most applicable chunks by combining the embeddings and BM25 techniques using the following steps:

RAG 解决方案可以通过使用以下步骤结合嵌入和 BM25 技术来更准确地检索最适用的块：

1. Break down the knowledge base (the "corpus" of documents) into smaller chunks of text, usually no more than a few hundred tokens;
将知识库（文档的"语料库"）分解为较小的文本块，通常不超过几百个 token；

2. Create TF-IDF encodings and semantic embeddings for these chunks;
为这些块创建 TF-IDF 编码和语义嵌入；

3. Use BM25 to find top chunks based on exact matches;
使用 BM25 基于精确匹配找到顶级块；

4. Use embeddings to find top chunks based on semantic similarity;
使用嵌入基于语义相似性找到顶级块；

5. Combine and deduplicate results from (3) and (4) using rank fusion techniques;
使用排序融合技术结合和去重（3）和（4）的结果；

6. Add the top-K chunks to the prompt to generate the response.
将前 K 个块添加到提示中以生成响应。

By leveraging both BM25 and embedding models, traditional RAG systems can provide more comprehensive and accurate results, balancing precise term matching with broader semantic understanding.

通过利用 BM25 和嵌入模型，传统 RAG 系统可以提供更全面和准确的结果，平衡精确术语匹配与更广泛的语义理解。

![A Standard Retrieval-Augmented Generation (RAG) system that uses both embeddings and Best Match 25 (BM25) to retrieve information. TF-IDF (term frequency-inverse document frequency) measures word importance and forms the basis for BM25.](https://www-cdn.anthropic.com/images/4zrzovbb/website/45603646e979c62349ce27744a940abf30200d57-3840x2160.png)

标准的检索增强生成（RAG）系统，使用嵌入和最佳匹配 25（BM25）来检索信息。TF-IDF（词频-逆文档频率）衡量单词重要性，并构成 BM25 的基础。

This approach allows you to cost-effectively scale to enormous knowledge bases, far beyond what could fit in a single prompt. But these traditional RAG systems have a significant limitation: they often destroy context.

这种方法使您能够经济有效地扩展到巨大的知识库，远远超出单个提示所能容纳的内容。但这些传统 RAG 系统有一个显著的限制：它们经常破坏上下文。

---

### The context conundrum in traditional RAG | 传统 RAG 中的上下文难题

In traditional RAG, documents are typically split into smaller chunks for efficient retrieval. While this approach works well for many applications, it can lead to problems when individual chunks lack sufficient context.

在传统 RAG 中，文档通常被分割成较小的块以便高效检索。虽然这种方法对许多应用程序效果良好，但当单个块缺乏足够的上下文时，可能会导致问题。

For example, imagine you had a collection of financial information (say, U.S. SEC filings) embedded in your knowledge base, and you received the following question: "What was the revenue growth for ACME Corp in Q2 2023?"

例如，假设您在知识库中嵌入了一组财务信息（比如美国 SEC 文件），并收到以下问题："ACME 公司在 2023 年第二季度的收入增长是多少？"

A relevant chunk might contain the text: "The company's revenue grew by 3% over the previous quarter." However, this chunk on its own doesn't specify which company it's referring to or the relevant time period, making it difficult to retrieve the right information or use the information effectively.

相关的块可能包含文本："公司收入比上季度增长 3%。"然而，这个块本身并没有指定它指的是哪家公司或相关时间段，这使得检索正确的信息或有效使用信息变得困难。

---

## Introducing Contextual Retrieval | 介绍上下文检索

Contextual Retrieval solves this problem by prepending chunk-specific explanatory context to each chunk before embedding ("Contextual Embeddings") and creating the BM25 index ("Contextual BM25").

上下文检索通过在嵌入（"上下文嵌入"）和创建 BM25 索引（"上下文 BM25"）之前，为每个块附加块特定的解释性上下文来解决这个问题。

Let's return to our SEC filings collection example. Here's an example of how a chunk might be transformed:

让我们回到我们的 SEC 文件集合示例。以下是一个块可能如何转换的示例：

```
original_chunk = "The company's revenue grew by 3% over the previous quarter."
原始块 = "公司收入比上季度增长 3%。"

contextualized_chunk = "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."
上下文化块 = "此块来自 ACME 公司 2023 年第二季度业绩的 SEC 文件；上一季度收入为 3.14 亿美元。公司收入比上季度增长 3%。"
```

It is worth noting that other approaches to using context to improve retrieval have been proposed in the past. Other proposals include: adding generic document summaries to chunks (we experimented and saw very limited gains), hypothetical document embedding, and summary-based indexing (we evaluated and saw low performance). These methods differ from what is proposed in this post.

值得注意的是，过去已经提出了其他使用上下文来改进检索的方法。其他建议包括：向块添加通用文档摘要（我们进行了实验，收益非常有限）、假设文档嵌入和基于摘要的索引（我们进行了评估，性能较低）。这些方法与本文提出的方法不同。

---

### Implementing Contextual Retrieval | 实现上下文检索

Of course, it would be far too much work to manually annotate the thousands or even millions of chunks in a knowledge base. To implement Contextual Retrieval, we turn to Claude. We've written a prompt that instructs the model to provide concise, chunk-specific context that explains the chunk using the context of the overall document. We used the following Claude 3 Haiku prompt to generate context for each chunk:

当然，手动注释知识库中的数千甚至数百万个块工作量太大了。为了实现上下文检索，我们转向 Claude。我们编写了一个提示，指示模型提供简洁的、块特定的上下文，使用整个文档的上下文来解释该块。我们使用以下 Claude 3 Haiku 提示为每个块生成上下文：

```
<document>
{{WHOLE_DOCUMENT}}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{{CHUNK_CONTENT}}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else.

<document>
{{WHOLE_DOCUMENT}}
</document>
这是我们要在整个文档中定位的块
<chunk>
{{CHUNK_CONTENT}}
</chunk>
请给出一个简短简洁的上下文，将此块定位在整个文档中，以改进块的搜索检索。仅回答简洁的上下文，不回答其他内容。
```

The resulting contextual text, usually 50-100 tokens, is prepended to the chunk before embedding it and before creating the BM25 index.

生成的上下文文本，通常 50-100 个 token，在嵌入块和创建 BM25 索引之前被添加到块的前面。

Here's what the preprocessing flow looks like in practice:

以下是预处理流程的实际情况：

![Contextual Retrieval is a preprocessing technique that improves retrieval accuracy.](https://www-cdn.anthropic.com/images/4zrzovbb/website/2496e7c6fedd7ffaa043895c23a4089638b0c21b-3840x2160.png)

上下文检索是一种改进检索准确性的预处理技术。

If you're interested in using Contextual Retrieval, you can get started with our [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval).

如果您对使用上下文检索感兴趣，可以从我们的 [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval) 开始。

---

### Using Prompt Caching to reduce the costs of Contextual Retrieval | 使用提示缓存降低上下文检索的成本

Contextual Retrieval is uniquely possible at low cost with Claude, thanks to the special prompt caching feature we mentioned above. With prompt caching, you don't need to pass in the reference document for every chunk. You simply load the document into the cache once and then reference the previously cached content. Assuming 800 token chunks, 8k token documents, 50 token context instructions, and 100 tokens of context per chunk, **the one-time cost to generate contextualized chunks is $1.02 per million document tokens**.

由于我们上面提到的特殊提示缓存功能，上下文检索可以以低成本独特地使用 Claude。通过提示缓存，您不需要为每个块传入参考文档。您只需将文档加载到缓存中一次，然后引用以前缓存的内容。假设 800 token 块、8k token 文档、50 token 上下文指令和每个块 100 token 的上下文，**生成上下文化块的一次性成本为每百万文档 token $1.02**。

#### Methodology | 方法论

We experimented across various knowledge domains (codebases, fiction, ArXiv papers, Science Papers), embedding models, retrieval strategies, and evaluation metrics. We've included a few examples of the questions and answers we used for each domain in Appendix II.

我们在各种知识领域（代码库、小说、ArXiv 论文、科学论文）、嵌入模型、检索策略和评估指标上进行了实验。我们在附录 II 中包含了我们在每个领域使用的问题和答案的一些示例。

The graphs below show the average performance across all knowledge domains with the top-performing embedding configuration (Gemini Text 004) and retrieving the top-20-chunks. We use 1 minus recall@20 as our evaluation metric, which measures the percentage of relevant documents that fail to be retrieved within the top 20 chunks. You can see the full results in the appendix - contextualizing improves performance in every embedding-source combination we evaluated.

下面的图表显示了所有知识领域的平均性能，使用表现最佳的嵌入配置（Gemini Text 004）和检索前 20 个块。我们使用 1 减去 recall@20 作为我们的评估指标，它衡量在前 20 个块中未能检索到的相关文档的百分比。您可以在附录中看到完整结果 - 在我们评估的每个嵌入源组合中，上下文化都提高了性能。

#### Performance improvements | 性能改进

Our experiments showed that:

我们的实验表明：

- **Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35%** (5.7% → 3.7%).
- **上下文嵌入将前 20 个块的检索失败率降低了 35%**（5.7% → 3.7%）。

- **Combining Contextual Embeddings and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 49%** (5.7% → 2.9%).
- **结合上下文嵌入和上下文 BM25 将前 20 个块的检索失败率降低了 49%**（5.7% → 2.9%）。

![Combining Contextual Embedding and Contextual BM25 reduce the top-20-chunk retrieval failure rate by 49%.](https://www-cdn.anthropic.com/images/4zrzovbb/website/7f8d739e491fe6b3ba0e6a9c74e4083d760b88c9-3840x2160.png)

结合上下文嵌入和上下文 BM25 将前 20 个块的检索失败率降低了 49%。

#### Implementation considerations | 实现考虑

When implementing Contextual Retrieval, there are a few considerations to keep in mind:

在实现上下文检索时，需要记住一些考虑事项：

1. **Chunk boundaries:** Consider how you split your documents into chunks. The choice of chunk size, chunk boundary, and chunk overlap can affect retrieval performance<sup>1</sup>.
**块边界：**考虑如何将文档分割成块。块大小、块边界和块重叠的选择可能会影响检索性能<sup>1</sup>。

2. **Embedding model:** Whereas Contextual Retrieval improves performance across all embedding models we tested, some models may benefit more than others. We found Gemini and Voyage embeddings to be particularly effective.
**嵌入模型：**虽然上下文检索改进了我们测试的所有嵌入模型的性能，但某些模型可能比其他模型受益更多。我们发现 Gemini 和 Voyage 嵌入特别有效。

3. **Custom contextualizer prompts:** While the generic prompt we provided works well, you may be able to achieve even better results with prompts tailored to your specific domain or use case (for example, including a glossary of key terms that might only be defined in other documents in the knowledge base).
**自定义上下文提示器：**虽然我们提供的通用提示效果很好，但您可能能够通过针对特定领域或用例量身定制的提示获得更好的结果（例如，包含可能仅在知识库中的其他文档中定义的关键术语词汇表）。

4. **Number of chunks:** Adding more chunks into the context window increases the chances that you include the relevant information. However, more information can be distracting for models so there's a limit to this. We tried delivering 5, 10, and 20 chunks, and found using 20 to be the most performant of these options (see appendix for comparisons) but it's worth experimenting on your use case.
**块数量：**将更多块添加到上下文窗口会增加包含相关信息的机会。然而，更多的信息可能会分散模型的注意力，因此这有一个限制。我们尝试提供 5、10 和 20 个块，发现使用 20 个是这些选项中性能最好的（参见附录进行比较），但这值得在您的用例上进行实验。

**Always run evals:** Response generation may be improved by passing it the contextualized chunk and distinguishing between what is context and what is the chunk.

**始终运行评估：**响应生成可能会通过传递上下文化块并区分什么是上下文、什么是块来改进。

---

## Further boosting performance with Reranking | 通过重排序进一步提升性能

In a final step, we can combine Contextual Retrieval with another technique to give even more performance improvements. In traditional RAG, the AI system searches its knowledge base to find the potentially relevant information chunks. With large knowledge bases, this initial retrieval often returns a lot of chunks—sometimes hundreds—of varying relevance and importance.

在最后一步，我们可以将上下文检索与另一种技术结合起来，以获得更多的性能改进。在传统 RAG 中，AI 系统搜索其知识库以查找潜在相关信息块。对于大型知识库，这种初始检索通常返回大量块——有时数百个——具有不同的相关性和重要性。

Reranking is a commonly used filtering technique to ensure that only the most relevant chunks are passed to the model. Reranking provides better responses and reduces cost and latency because the model is processing less information. The key steps are:

重排序是一种常用的过滤技术，确保只有最相关的块被传递给模型。重排序提供更好的响应并降低成本和延迟，因为模型处理的信息更少。关键步骤是：

1. Perform initial retrieval to get the top potentially relevant chunks (we used the top 150);
执行初始检索以获取前 N 个潜在相关块（我们使用了前 150 个）；

2. Pass the top-N chunks, along with the user's query, through the reranking model;
将前 N 个块与用户的查询一起传递给重排序模型；

3. Using a reranking model, give each chunk a score based on its relevance and importance to the prompt, then select the top-K chunks (we used the top 20);
使用重排序模型，根据每个块与提示的相关性和重要性为其打分，然后选择前 K 个块（我们使用了前 20 个）；

4. Pass the top-K chunks into the model as context to generate the final result.
将前 K 个块作为上下文传递给模型以生成最终结果。

![Combine Contextual Retrieval and Reranking to maximize retrieval accuracy.](https://www-cdn.anthropic.com/images/4zrzovbb/website/8f82c6175a64442ceff4334b54fac2ab3436a1d1-3840x2160.png)

结合上下文检索和重排序以最大化检索准确性。

### Performance improvements | 性能改进

There are several reranking models on the market. We ran our tests with the Cohere reranker. Voyage also offers a reranker, though we did not have time to test it. Our experiments showed that, across various domains, adding a reranking step further optimizes retrieval.

市场上有几种重排序模型。我们使用 Cohere 重排序器运行了测试。Voyage 也提供重排序器，尽管我们没有时间测试它。我们的实验表明，在各种领域，添加重排序步骤进一步优化了检索。

Specifically, we found that Reranked Contextual Embedding and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 67% (5.7% → 1.9%).

具体来说，我们发现重排序的上下文嵌入和上下文 BM25 将前 20 个块的检索失败率降低了 67%（5.7% → 1.9%）。

![Reranked Contextual Embedding and Contextual BM25 reduces the top-20-chunk retrieval failure rate by 67%.](https://www-cdn.anthropic.com/images/4zrzovbb/website/93a70cfbb7cca35bb8d86ea0a23bdeeb699e8e58-3840x2160.png)

重排序的上下文嵌入和上下文 BM25 将前 20 个块的检索失败率降低了 67%。

#### Cost and latency considerations | 成本和延迟考虑

One important consideration with reranking is the impact on latency and cost, especially when reranking a large number of chunks. Because reranking adds an extra step at runtime, it inevitably adds a small amount of latency, even though the reranker scores all the chunks in parallel. There is an inherent trade-off between reranking more chunks for better performance vs. reranking fewer for lower latency and cost. We recommend experimenting with different settings on your specific use case to find the right balance.

重排序的一个重要考虑因素是对延迟和成本的影响，尤其是在重排序大量块时。由于重排序在运行时添加了一个额外步骤，它不可避免地会增加少量延迟，即使重排序器并行对所有块进行评分。在重排序更多块以获得更好性能与重排序较少块以降低延迟和成本之间存在固有的权衡。我们建议在您的特定用例上试验不同设置以找到正确的平衡。

---

## Conclusion | 结论

We ran a large number of tests, comparing different combinations of all the techniques described above (embedding model, use of BM25, use of contextual retrieval, use of a reranker, and total # of top-K results retrieved), all across a variety of different dataset types. Here's a summary of what we found:

我们进行了大量测试，比较了上述所有技术的不同组合（嵌入模型、BM25 的使用、上下文检索的使用、重排序器的使用以及检索的前 K 个结果的总数），跨越各种不同的数据集类型。以下是我们发现的总结：

1. Embeddings+BM25 is better than embeddings on their own;
嵌入 + BM25 比单独的嵌入更好；

2. Voyage and Gemini have the best embeddings of the ones we tested;
Voyage 和 Gemini 在我们测试的嵌入中是最好的；

3. Passing the top-20 chunks to the model is more effective than just the top-10 or top-5;
将前 20 个块传递给模型比仅传递前 10 个或前 5 个更有效；

4. Adding context to chunks improves retrieval accuracy a lot;
向块添加上下文大大提高了检索准确性；

5. Reranking is better than no reranking;
重排序比不重排序更好；

6. **All these benefits stack**: to maximize performance improvements, we can combine contextual embeddings (from Voyage or Gemini) with contextual BM25, plus a reranking step, and adding the 20 chunks to the prompt.
**所有这些好处都可以叠加**：为了最大化性能改进，我们可以结合上下文嵌入（来自 Voyage 或 Gemini）与上下文 BM25，加上重排序步骤，并将 20 个块添加到提示中。

We encourage all developers working with knowledge bases to use our [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval) to experiment with these approaches to unlock new levels of performance.

我们鼓励所有使用知识库的开发人员使用我们的 [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval) 试验这些方法，以解锁新的性能水平。

---

## Appendix I | 附录 I

Below is a breakdown of results across datasets, embedding providers, use of BM25 in addition to embeddings, use of contextual retrieval, and use of reranking for Retrievals @ 20.

以下是跨数据集、嵌入提供商、除嵌入外还使用 BM25、使用上下文检索以及使用重排序的检索 @ 20 的结果细分。

See Appendix II for the breakdowns for Retrievals @ 10 and @ 5 as well as example questions and answers for each dataset.

参见附录 II 了解检索 @ 10 和 @ 5 的细分以及每个数据集的示例问题和答案。

![1 minus recall @ 20 results across data sets and embedding providers.](https://www-cdn.anthropic.com/images/4zrzovbb/website/646a894ec4e6120cade9951a362f685cd2ec89b2-2458x2983.png)

跨数据集和嵌入提供商的 1 减去 recall @ 20 结果。

---

## Sources | 来源

- [Anthropic Engineering Blog](https://www.anthropic.com/engineering)
- [Anthropic 工程博客](https://www.anthropic.com/engineering)
- [Contextual Retrieval Cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval)
- [上下文检索 Cookbook](https://docs.anthropic.com/en/docs/build-with-claude/contextual-retrieval)
- [Prompt Caching Documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [提示缓存文档](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
