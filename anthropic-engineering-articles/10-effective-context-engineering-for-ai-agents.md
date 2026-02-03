# Effective context engineering for AI agents | AI 智能体的有效上下文工程

After a few years of prompt engineering being the focus of attention in applied AI, a new term has come to prominence: **context engineering**. Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of "what configuration of context is most likely to generate our model's desired behavior?"

在应用人工智能领域，经过几年以提示工程为关注焦点的时期后，一个新术语开始崭露头角：**上下文工程**。使用语言模型进行构建，越来越不是关于为你的提示找到正确的词语和短语，而是更多地关于回答一个更广泛的问题："什么配置的上下文最有可能生成我们模型的期望行为？"

**Context** refers to the set of tokens included when sampling from a large-language model (LLM). The **engineering** problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs in order to consistently achieve a desired outcome. Effectively wrangling LLMs often requires _thinking in context_ — in other words: considering the holistic state available to the LLM at any given time and what potential behaviors that state might yield.

**上下文**是指从大型语言模型（LLM）采样时包含的标记集合。手头的**工程**问题是在 LLM 的固有约束下优化这些标记的效用，以持续实现期望的结果。有效地处理 LLM 通常需要**在上下文中思考**——换句话说：考虑 LLM 在任何给定时间可用的整体状态，以及该状态可能产生的潜在行为。

In this post, we'll explore the emerging art of context engineering and offer a refined mental model for building steerable, effective agents.

在本文中，我们将探索上下文工程这一新兴艺术，并为构建可控制、有效的智能体提供一个完善的心智模型。

At Anthropic, we view context engineering as the natural progression of prompt engineering. Prompt engineering refers to methods for writing and organizing LLM instructions for optimal outcomes (see our docs for an overview and useful prompt engineering strategies). **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts.

在 Anthropic，我们将上下文工程视为提示工程的自然演进。提示工程指的是为获得最佳结果而编写和组织 LLM 指令的方法（请参阅我们的文档以获取概述和有用的提示工程策略）。**上下文工程**指的是在 LLM 推理期间策划和维护最优标记（信息）集合的策略集合，包括可能在提示之外到达那里的所有其他信息。

In the early days of engineering with LLMs, prompting was the biggest component of AI engineering work, as the majority of use cases outside of everyday chat interactions required prompts optimized for one-shot classification or text generation tasks. As the term implies, the primary focus of prompt engineering is how to write effective prompts, particularly system prompts. However, as we move towards engineering more capable agents that operate over multiple turns of inference and longer time horizons, we need strategies for managing the entire context state (system instructions, tools, Model Context Protocol (MCP), external data, message history, etc).

在 LLM 工程的早期，提示是 AI 工程工作的最大组成部分，因为日常聊天交互之外的大多数用例都需要针对单次分类或文本生成任务优化的提示。顾名思义，提示工程的主要焦点是如何编写有效的提示，特别是系统提示。然而，随着我们转向工程化更强大的智能体，这些智能体在多次推理轮次和更长时间范围内操作，我们需要策略来管理整个上下文状态（系统指令、工具、模型上下文协议（MCP）、外部数据、消息历史等）。

An agent running in a loop generates more and more data that _could_ be relevant for the next turn of inference, and this information must be cyclically refined. Context engineering is the art and science of curating what will go into the limited context window from that constantly evolving universe of possible information.

在循环中运行的智能体会产生越来越多的数据，这些数据**可能**与下一轮推理相关，并且这些信息必须进行循环精炼。上下文工程是从那个不断演变的可能信息宇宙中，策划将进入有限上下文窗口的内容的艺术和科学。

![Image 1: Prompt engineering vs. context engineering](https://www-cdn.anthropic.com/images/4zrzovbb/website/faa261102e46c7f090a2402a49000ffae18c5dd6-2292x1290.png)

图片1说明：提示工程与上下文工程的对比。

_In contrast to the discrete task of writing a prompt, context engineering is iterative and the curation phase happens each time we decide what to pass to the model._

_与编写提示的离散任务不同，上下文工程是迭代的，策划阶段每次我们决定向模型传递什么内容时都会发生。_

## Why context engineering is important to building capable agents | 为什么上下文工程对构建强大的智能体很重要

Despite their speed and ability to manage larger and larger volumes of data, we've observed that LLMs, like humans, lose focus or experience confusion at a certain point. Studies on needle-in-a-haystackstyle benchmarking have uncovered the concept of context rot: as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases.

尽管 LLM 具有速度和管理越来越大数据量的能力，但我们观察到，像人类一样，LLM 在某个点会失去焦点或经历困惑。关于"大海捞针式"基准测试的研究揭示了上下文衰退（context rot）的概念：随着上下文窗口中标记数量的增加，模型从该上下文中准确回忆信息的能力下降。

While some models exhibit more gentle degradation than others, this characteristic emerges across all models. Context, therefore, must be treated as a finite resource with diminishing marginal returns. Like humans, who have limited working memory capacity, LLMs have an "attention budget" that they draw on when parsing large volumes of context. Every new token introduced depletes this budget by some amount, increasing the need to carefully curate the tokens available to the LLM.

虽然某些模型比其他模型表现出更温和的退化，但这个特征出现在所有模型中。因此，上下文必须被视为一种具有递减边际收益的有限资源。就像工作记忆容量有限的人类一样，LLM 在解析大量上下文时会利用"注意力预算"。引入的每个新标记都会消耗一定量的预算，增加了仔细策划 LLM 可用标记的需求。

This attention scarcity stems from architectural constraints of LLMs. LLMs are based on the transformer architecture, which enables every token to attend to every other token across the entire context. This results in n² pairwise relationships for n tokens.

这种注意力稀缺源于 LLM 的架构约束。LLM 基于 transformer 架构，该架构使每个标记能够关注整个上下文中的每个其他标记。这导致 n 个标记产生 n² 成对关系。

As its context length increases, a model's ability to capture these pairwise relationships gets stretched thin, creating a natural tension between context size and attention focus. Additionally, models develop their attention patterns from training data distributions where shorter sequences are typically more common than longer ones. This means models have less experience with, and fewer specialized parameters for, context-wide dependencies.

随着上下文长度的增加，模型捕获这些成对关系的能力变得稀薄，在上下文大小和注意力焦点之间产生了自然的紧张关系。此外，模型从训练数据分布中发展其注意力模式，其中较短的序列通常比较长的序列更常见。这意味着模型对上下文范围的依赖关系的经验较少，专门化参数也较少。

Techniques like position encoding interpolation allow models to handle longer sequences by adapting them to the originally trained smaller context, though with some degradation in token position understanding. These factors create a performance gradient rather than a hard cliff: models remain highly capable at longer contexts but may show reduced precision for information retrieval and long-range reasoning compared to their performance on shorter contexts.

位置编码插值等技术允许模型通过适应原始训练的较小上下文来处理更长的序列，尽管在标记位置理解方面有一些退化。这些因素产生性能梯度而不是硬性悬崖：模型在较长上下文中仍然高度强大，但与在较短上下文中的表现相比，可能在信息检索和远程推理方面显示精度降低。

These realities mean that thoughtful context engineering is essential for building capable agents.

这些现实意味着深思熟虑的上下文工程对于构建强大的智能体至关重要。

## The anatomy of effective context | 有效上下文的解剖结构

Given that LLMs are constrained by a finite attention budget, _good_ context engineering means finding the _smallest_ _possible_ set of high-signal tokens that maximize the likelihood of some desired outcome. Implementing this practice is much easier said than done, but in the following section, we outline what this guiding principle means in practice across the different components of context.

鉴于 LLM 受到有限注意力预算的约束，**好的**上下文工程意味着找到**尽可能最小的**高信号标记集合，以最大化某些期望结果的可能性。实施这种实践说起来容易做起来难，但在以下部分，我们概述了这个指导原则在上下文的不同组件中的实际意义。

**System prompts** should be extremely clear and use simple, direct language that presents ideas at the _right altitude_ for the agent. The right altitude is the Goldilocks zone between two common failure modes. At one extreme, we see engineers hardcoding complex, brittle logic in their prompts to elicit exact agentic behavior. This approach creates fragility and increases maintenance complexity over time. At the other extreme, engineers sometimes provide vague, high-level guidance that fails to give the LLM concrete signals for desired outputs or falsely assumes shared context. The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics to guide behavior.

**系统提示**应该极其清晰，使用简单、直接的语言，为智能体在**正确的高度**呈现想法。正确的高度是两种常见失败模式之间的金发姑娘区域。在一个极端，我们看到工程师在提示中硬编码复杂、脆弱的逻辑，以引发精确的智能体行为。这种方法随着时间的推移产生脆弱性并增加维护复杂性。在另一个极端，工程师有时提供模糊的、高层级的指导，未能为 LLM 提供期望输出的具体信号或错误地假设共享上下文。最优高度在两者之间取得平衡：足够具体以有效指导行为，又足够灵活以提供模型强启发式方法来指导行为。

![Image 2: Calibrating the system prompt in the process of context engineering.](https://www-cdn.anthropic.com/images/4zrzovbb/website/0442fe138158e84ffce92bed1624dd09f37ac46f-2292x1288.png)

图片2说明：在上下文工程过程中校准系统提示。

_At one end of the spectrum, we see brittle if-else hardcoded prompts, and at the other end we see prompts that are overly general or falsely assume shared context._

_在光谱的一端，我们看到脆弱的 if-else 硬编码提示，在另一端我们看到过于通用或错误地假设共享上下文的提示。_

We recommend organizing prompts into distinct sections (like `<background_information>`, `<instructions>`, `## Tool guidance`, `## Output description`, etc) and using techniques like XML tagging or Markdown headers to delineate these sections, although the exact formatting of prompts is likely becoming less important as models become more capable.

我们建议将提示组织成不同的部分（如 `<background_information>`、`<instructions>`、`## Tool guidance`、`## Output description` 等），并使用 XML 标记或 Markdown 标题等技术来划定这些部分，尽管随着模型变得更强大，提示的确切格式可能变得不那么重要。

Regardless of how you decide to structure your system prompt, you should be striving for the minimal set of information that fully outlines your expected behavior. (Note that minimal does not necessarily mean short; you still need to give the agent sufficient information up front to ensure it adheres to the desired behavior.) It's best to start by testing a minimal prompt with the best model available to see how it performs on your task, and then add clear instructions and examples to improve performance based on failure modes found during initial testing.

无论你决定如何构建系统提示，你都应该努力争取完全概述你期望行为的最小信息集合。（请注意，最小不一定意味着短；你仍然需要提前给智能体足够的信息以确保它遵守期望的行为。）最好从使用可用的最佳模型测试最小提示开始，看看它在你的任务上如何表现，然后根据初始测试期间发现的失败模式添加清晰的指令和示例以提高性能。

**Tools** allow agents to operate with their environment and pull in new, additional context as they work. Because tools define the contract between agents and their information/action space, it's extremely important that tools promote efficiency, both by returning information that is token efficient and by encouraging efficient agent behaviors.

**工具**允许智能体在其环境中操作并在工作时引入新的、额外的上下文。因为工具定义了智能体与其信息/操作空间之间的契约，工具促进效率极其重要，既通过返回标记效率的信息，又通过鼓励高效的智能体行为。

In [Writing tools for AI agents – with AI agents](https://www.anthropic.com/engineering/writing-effective-tools), we discussed building tools that are well understood by LLMs and have minimal overlap in functionality. Similar to the functions of a well-designed codebase, tools should be self-contained, robust to error, and extremely clear with respect to their intended use. Input parameters should similarly be descriptive, unambiguous, and play to the inherent strengths of the model.

在[为 AI 智能体编写工具——使用 AI 智能体](https://www.anthropic.com/engineering/writing-effective-tools)中，我们讨论了构建 LLM 理解良好且功能重叠最小的工具。与设计良好的代码库的函数类似，工具应该是自包含的、对错误鲁棒的，并且对于其预期用途极其清晰。输入参数同样应该是描述性的、无歧义的，并发挥模型的固有优势。

One of the most common failure modes we see is bloated tool sets that cover too much functionality or lead to ambiguous decision points about which tool to use. If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better. As we'll discuss later, curating a minimal viable set of tools for the agent can also lead to more reliable maintenance and pruning of context over long interactions.

我们看到的最常见的失败模式之一是臃肿的工具集，它们涵盖太多功能或导致关于使用哪个工具的模糊决策点。如果人类工程师不能明确地说在给定情况下应该使用哪个工具，就不能期望 AI 智能体做得更好。正如我们稍后将讨论的，为智能体策划最小可行工具集也可以在长时间交互中导致更可靠的维护和上下文修剪。

Providing examples, otherwise known as few-shot prompting, is a well known best practice that we continue to strongly advise. However, teams will often stuff a laundry list of edge cases into a prompt in an attempt to articulate every possible rule the LLM should follow for a particular task. We do not recommend this. Instead, we recommend working to curate a set of diverse, canonical examples that effectively portray the expected behavior of the agent. For an LLM, examples are the "pictures" worth a thousand words.

提供示例，也称为少样本提示（few-shot prompting），是一个众所周知的最佳实践，我们继续强烈建议。然而，团队经常将大量边缘情况列表塞入提示中，试图详述 LLM 应该为特定任务遵循的每条可能规则。我们不建议这样做。相反，我们建议策划一组多样化的、规范的示例，有效地描绘智能体的期望行为。对于 LLM 来说，示例是"一张图片值一千字"。

Our overall guidance across the different components of context (system prompts, tools, examples, message history, etc) is to be thoughtful and keep your context informative, yet tight. Now let's dive into dynamically retrieving context at runtime.

我们对上下文不同组件（系统提示、工具、示例、消息历史等）的整体指导是要深思熟虑，保持上下文信息丰富但紧凑。现在让我们深入探讨在运行时动态检索上下文。

## Context retrieval and agentic search | 上下文检索与智能体搜索

In [Building effective AI agents](https://www.anthropic.com/engineering/building-effective-agents), we highlighted the differences between LLM-based workflows and agents. Since we wrote that post, we've gravitated towards a simple definition for agents: LLMs autonomously using tools in a loop.

在[构建有效的 AI 智能体](https://www.anthropic.com/engineering/building-effective-agents)中，我们强调了基于 LLM 的工作流与智能体之间的区别。自从我们撰写那篇文章以来，我们倾向于一个简单的智能体定义：在循环中自主使用工具的 LLM。

Working alongside our customers, we've seen the field converging on this simple paradigm. As the underlying models become more capable, the level of autonomy of agents can scale: smarter models allow agents to independently navigate nuanced problem spaces and recover from errors.

与我们的客户一起工作，我们看到该领域正在向这个简单的范式趋同。随着底层模型变得更强大，智能体的自主性水平可以扩展：更智能的模型允许智能体独立导航微妙的问题空间并从错误中恢复。

We're now seeing a shift in how engineers think about designing context for agents. Today, many AI-native applications employ some form of embedding-based pre-inference time retrieval to surface important context for the agent to reason over. As the field transitions to more agentic approaches, we increasingly see teams augmenting these retrieval systems with "just in time" context strategies.

我们现在看到工程师在为智能体设计上下文的思考方式发生了转变。今天，许多 AI 原生应用程序采用某种形式的基于嵌入的预推理时间检索来呈现重要上下文供智能体推理。随着该领域转向更智能体的方法，我们越来越多地看到团队使用"即时"上下文策略来增强这些检索系统。

Rather than pre-processing all relevant data up front, agents built with the "just in time" approach maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools. Anthropic's agentic coding solution Claude Code uses this approach to perform complex data analysis over large databases. The model can write targeted queries, store results, and leverage Bash commands like head and tail to analyze large volumes of data without ever loading the full data objects into context. This approach mirrors human cognition: we generally don't memorize entire corpuses of information, but rather introduce external organization and indexing systems like file systems, inboxes, and bookmarks to retrieve relevant information on demand.

使用"即时"方法构建的智能体不是预先处理所有相关数据，而是维护轻量级标识符（文件路径、存储的查询、Web 链接等）并使用这些引用在运行时使用工具动态地将数据加载到上下文中。Anthropic 的智能体编码解决方案 Claude Code 使用这种方法对大型数据库执行复杂的数据分析。模型可以编写有针对性的查询、存储结果，并利用 head 和 tail 等 Bash 命令来分析大量数据，而无需将完整的数据对象加载到上下文中。这种方法反映了人类认知：我们通常不会记忆整个信息语料库，而是引入外部组织和索引系统，如文件系统、收件箱和书签，按需检索相关信息。

Beyond storage efficiency, the metadata of these references provides a mechanism to efficiently refine behavior, whether explicitly provided or intuitive. To an agent operating in a file system, the presence of a file named `test_utils.py` in a `tests` folder implies a different purpose than a file with the same name located in `src/core_logic/` Folder hierarchies, naming conventions, and timestamps all provide important signals that help both humans and agents understand how and when to utilize information.

除了存储效率之外，这些引用的元数据提供了一种有效精炼行为的机制，无论是明确提供还是直观的。对于在文件系统中操作的智能体，位于 `tests` 文件夹中的名为 `test_utils.py` 的文件的存在暗示了与位于 `src/core_logic/` 中的同名文件不同的目的。文件夹层次结构、命名约定和时间戳都提供重要信号，帮助人类和智能体理解如何以及何时使用信息。

Letting agents navigate and retrieve data autonomously also enables progressive disclosure—in other words, allows agents to incrementally discover relevant context through exploration. Each interaction yields context that informs the next decision: file sizes suggest complexity; naming conventions hint at purpose; timestamps can be a proxy for relevance. Agents can assemble understanding layer by layer, maintaining only what's necessary in working memory and leveraging note-taking strategies for additional persistence. This self-managed context window keeps the agent focused on relevant subsets rather than drowning in exhaustive but potentially irrelevant information.

让智能体自主导航和检索数据还实现了渐进式披露——换句话说，允许智能体通过探索增量地发现相关上下文。每次交互都会产生通知下一个决策的上下文：文件大小建议复杂性；命名约定暗示目的；时间戳可以作为相关性的代理。智能体可以逐层组装理解，仅在工作记忆中保持必要的内容，并利用笔记策略进行额外的持久化。这种自我管理的上下文窗口使智能体专注于相关子集，而不是淹没在详尽但可能不相关的信息中。

Of course, there's a trade-off: runtime exploration is slower than retrieving pre-computed data. Not only that, but opinionated and thoughtful engineering is required to ensure that an LLM has the right tools and heuristics for effectively navigating its information landscape. Without proper guidance, an agent can waste context by misusing tools, chasing dead-ends, or failing to identify key information.

当然，存在权衡：运行时探索比检索预计算的数据慢。不仅如此，还需要有观点和深思熟虑的工程来确保 LLM 拥有有效导航其信息景观的正确工具和启发式方法。如果没有适当的指导，智能体可能会通过滥用工具、追逐死胡同或未能识别关键信息而浪费上下文。

In certain settings, the most effective agents might employ a hybrid strategy, retrieving some data up front for speed, and pursuing further autonomous exploration at its discretion. The decision boundary for the 'right' level of autonomy depends on the task. Claude Code is an agent that employs this hybrid model: CLAUDE.md files are naively dropped into context up front, while primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time, effectively bypassing the issues of stale indexing and complex syntax trees.

在某些设置中，最有效的智能体可能采用混合策略，预先检索一些数据以提高速度，并自行决定进一步进行自主探索。"正确"自主水平的决策边界取决于任务。Claude Code 是一个采用这种混合模型的智能体：CLAUDE.md 文件被天真地预先放入上下文中，而 glob 和 grep 等原语允许它导航其环境并即时检索文件，有效地绕过过时索引和复杂语法树的问题。

The hybrid strategy might be better suited for contexts with less dynamic content, such as legal or finance work. As model capabilities improve, agentic design will trend towards letting intelligent models act intelligently, with progressively less human curation. Given the rapid pace of progress in the field, "do the simplest thing that works" will likely remain our best advice for teams building agents on top of Claude.

对于动态内容较少的上下文，如法律或金融工作，混合策略可能更适合。随着模型能力的提高，智能体设计将趋向于让智能模型智能地行动，人类的策划逐渐减少。鉴于该领域快速发展的步伐，对于在 Claude 之上构建智能体的团队，"做最简单的有效方法"可能仍然是我们最好的建议。

### Context engineering for long-horizon tasks | 长时间跨度任务的上下文工程

Long-horizon tasks require agents to maintain coherence, context, and goal-directed behavior over sequences of actions where the token count exceeds the LLM's context window. For tasks that span tens of minutes to multiple hours of continuous work, like large codebase migrations or comprehensive research projects, agents require specialized techniques to work around the context window size limitation.

长时间跨度任务要求智能体在标记数量超过 LLM 上下文窗口的操作序列中保持连贯性、上下文和目标导向行为。对于跨越数十分钟到数小时连续工作的任务，如大型代码库迁移或综合研究项目，智能体需要专门的技术来解决上下文窗口大小限制。

Waiting for larger context windows might seem like an obvious tactic. But it's likely that for the foreseeable future, context windows of all sizes will be subject to context pollution and information relevance concerns—at least for situations where the strongest agent performance is desired. To enable agents to work effectively across extended time horizons, we've developed a few techniques that address these context pollution constraints directly: compaction, structured note-taking, and multi-agent architectures.

等待更大的上下文窗口似乎是一个明显的策略。但很可能在可预见的未来，所有大小的上下文窗口都将受到上下文污染和信息相关性问题的困扰——至少在期望最强智能体性能的情况下。为了使智能体能够在扩展的时间跨度内有效地工作，我们开发了几种直接解决这些上下文污染约束的技术：压缩、结构化笔记和多智能体架构。

**Compaction**

**压缩**

Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary. Compaction typically serves as the first lever in context engineering to drive better long-term coherence. At its core, compaction distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation.

压缩是采用接近上下文窗口限制的对话、总结其内容并用总结重新启动新上下文窗口的做法。压缩通常作为上下文工程中的第一个杠杆，以驱动更好的长期连贯性。其核心是，压缩以高保真方式精炼上下文窗口的内容，使智能体能够以最小的性能退化继续工作。

In Claude Code, for example, we implement this by passing the message history to the model to summarize and compress the most critical details. The model preserves architectural decisions, unresolved bugs, and implementation details while discarding redundant tool outputs or messages. The agent can then continue with this compressed context plus the five most recently accessed files. Users get continuity without worrying about context window limitations.

例如，在 Claude Code 中，我们通过将消息历史传递给模型来总结和压缩最关键的细节来实现这一点。模型保留架构决策、未解决的错误和实现细节，同时丢弃冗余的工具输出或消息。然后智能体可以继续使用这个压缩的上下文加上最近访问的五个文件。用户获得连续性而无需担心上下文窗口限制。

The art of compaction lies in the selection of what to keep versus what to discard, as overly aggressive compaction can result in the loss of subtle but critical context whose importance only becomes apparent later. For engineers implementing compaction systems, we recommend carefully tuning your prompt on complex agent traces. Start by maximizing recall to ensure your compaction prompt captures every relevant piece of information from the trace, then iterate to improve precision by eliminating superfluous content.

压缩的艺术在于选择保留什么与丢弃什么，因为过于激进的压缩可能导致微妙但关键的上下文丢失，其重要性只有在后来才变得明显。对于实施压缩系统的工程师，我们建议在复杂的智能体轨迹上仔细调整你的提示。首先最大化召回率以确保你的压缩提示捕获轨迹中的每一条相关信息，然后迭代以通过消除多余内容来提高精度。

An example of low-hanging superfluous content is clearing tool calls and results – once a tool has been called deep in the message history, why would the agent need to see the raw result again? One of the safest lightest touch forms of compaction is tool result clearing, most recently launched as a feature on the [Claude Developer Platform](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering).

多余内容的一个简单例子是清除工具调用和结果——一旦工具在消息历史深处被调用，智能体为什么需要再次看到原始结果？最安全的、最轻微的压缩形式之一是工具结果清除，最近在 [Claude 开发者平台](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) 上作为功能推出。

**Structured note-taking**

**结构化笔记**

Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times.

结构化笔记，或智能体记忆，是一种智能体定期将笔记持久化到上下文窗口之外的内存中的技术。这些笔记在稍后的时间被拉回上下文窗口。

This strategy provides persistent memory with minimal overhead. Like Claude Code creating a to-do list, or your custom agent maintaining a NOTES.md file, this simple pattern allows the agent to track progress across complex tasks, maintaining critical context and dependencies that would otherwise be lost across dozens of tool calls.

这种策略以最小的开销提供持久记忆。像 Claude Code 创建待办事项列表，或你的自定义智能体维护 NOTES.md 文件，这种简单模式允许智能体跨复杂任务跟踪进度，维护关键的上下文和依赖关系，否则这些会在数十次工具调用中丢失。

Claude playing Pokémon demonstrates how memory transforms agent capabilities in non-coding domains. The agent maintains precise tallies across thousands of game steps—tracking objectives like "for the last 1,234 steps I've been training my Pokémon in Route 1, Pikachu has gained 8 levels toward the target of 10." Without any prompting about memory structure, it develops maps of explored regions, remembers which key achievements it has unlocked, and maintains strategic notes of combat strategies that help it learn which attacks work best against different opponents.

Claude 玩宝可梦展示了记忆如何改变非编码领域的智能体能力。智能体在数千个游戏步骤中保持精确计数——跟踪目标，如"在过去的 1,234 个步骤中，我一直在 Route 1 训练我的宝可梦，皮卡丘已经向目标 10 级提升了 8 级。"没有任何关于记忆结构的提示，它开发了探索区域的地图，记得它解锁了哪些关键成就，并维护战斗策略的战略笔记，帮助它学习哪些攻击对不同对手最有效。

After context resets, the agent reads its own notes and continues multi-hour training sequences or dungeon explorations. This coherence across summarization steps enables long-horizon strategies that would be impossible when keeping all the information in the LLM's context window alone.

在上下文重置后，智能体读取自己的笔记并继续多小时的训练序列或地牢探索。这种跨总结步骤的连贯性使得长期策略成为可能，而仅将所有信息保持在 LLM 的上下文窗口中是不可能的。

As part of our Sonnet 4.5 launch, we released a memory tool in public beta on the Claude Developer Platform that makes it easier to store and consult information outside the context window through a file-based system. This allows agents to build up knowledge bases over time, maintain project state across sessions, and reference previous work without keeping everything in context.

作为我们 Sonnet 4.5 发布的一部分，我们在 Claude 开发者平台上发布了公共测试版的记忆工具，使通过文件系统更容易在上下文窗口之外存储和查询信息。这允许智能体随时间建立知识库，跨会话维护项目状态，并引用以前的工作而无需将所有内容保持在上下文中。

**Sub-agent architectures**

**子智能体架构**

Sub-agent architectures provide another way around context limitations. Rather than one agent attempting to maintain state across an entire project, specialized sub-agents can handle focused tasks with clean context windows. The main agent coordinates with a high-level plan while subagents perform deep technical work or use tools to find relevant information. Each subagent might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens).

子智能体架构提供了绕过上下文限制的另一种方法。不是一个智能体尝试在整个项目中维护状态，专门的子智能体可以使用干净的上下文窗口处理专注的任务。主智能体使用高级计划进行协调，而子智能体执行深度的技术工作或使用工具查找相关信息。每个子智能体可能广泛探索，使用数万个或更多标记，但只返回其工作的浓缩、精炼摘要（通常为 1,000-2,000 个标记）。

This approach achieves a clear separation of concerns—the detailed search context remains isolated within sub-agents, while the lead agent focuses on synthesizing and analyzing the results. This pattern, discussed in [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research), showed a substantial improvement over single-agent systems on complex research tasks.

这种方法实现了明确的关注点分离——详细的搜索上下文保持在子智能体内隔离，而主导智能体专注于综合和分析结果。在[我们如何构建多智能体研究系统](https://www.anthropic.com/engineering/multi-agent-research)中讨论的这种模式，在复杂研究任务上比单智能体系统显示了实质性改进。

The choice between these approaches depends on task characteristics. For example:

这些方法之间的选择取决于任务特征。例如：

- Compaction maintains conversational flow for tasks requiring extensive back-and-forth;

- 压缩为需要大量来回的任务维护对话流；

- Note-taking excels for iterative development with clear milestones;

- 笔记在具有明确里程碑的迭代开发中表现出色；

- Multi-agent architectures handle complex research and analysis where parallel exploration pays dividends.

- 多智能体架构处理复杂研究和分析，其中并行探索会产生回报。

Even as models continue to improve, the challenge of maintaining coherence across extended interactions will remain central to building more effective agents.

即使模型继续改进，在扩展交互中保持连贯性的挑战仍然是构建更有效智能体的核心。

## Conclusion | 结论

Context engineering represents a fundamental shift in how we build with LLMs. As models become more capable, the challenge isn't just crafting the perfect prompt—it's thoughtfully curating what information enters the model's limited attention budget at each step. Whether you're implementing compaction for long-horizon tasks, designing token-efficient tools, or enabling agents to explore their environment just-in-time, the guiding principle remains the same: find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome.

上下文工程代表了使用 LLM 构建方式的根本转变。随着模型变得更强大，挑战不仅仅是制作完美的提示——而是在每一步深思熟虑地策划什么信息进入模型的有限注意力预算。无论你是在为长时间跨度任务实施压缩、设计标记效率的工具，还是使智能体能够即时探索其环境，指导原则保持不变：找到最大化期望结果可能性的最小高信号标记集合。

The techniques we've outlined will continue evolving as models improve. We're already seeing that smarter models require less prescriptive engineering, allowing agents to operate with more autonomy. But even as capabilities scale, treating context as a precious, finite resource will remain central to building reliable, effective agents.

我们概述的技术将随着模型的改进而继续演进。我们已经看到，更智能的模型需要更少的规定性工程，允许智能体以更大的自主性操作。但即使能力扩展，将上下文视为宝贵的有限资源仍然是构建可靠、有效的智能体的核心。

Get started with context engineering in the [Claude Developer Platform](https://docs.anthropic.com/en/docs/build-with-claude/agent-sdk) today, and access helpful tips and best practices via our [memory and context management cookbook](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/memory-management).

今天在 [Claude 开发者平台](https://docs.anthropic.com/en/docs/build-with-claude/agent-sdk) 上开始使用上下文工程，并通过我们的[记忆和上下文管理手册](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/memory-management)访问有用的提示和最佳实践。

## Acknowledgements | 致谢

Written by Anthropic's Applied AI team: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, and Jeremy Hadfield, with contributions from team members Rafi Ayub, Hannah Moran, Cal Rueb, and Connor Jennings. Special thanks to Molly Vorwerck, Stuart Ritchie, and Maggie Vo for their support.

本文由 Anthropic 的应用 AI 团队撰写：Prithvi Rajasekaran、Ethan Dixon、Carly Ryan 和 Jeremy Hadfield，团队成员 Rafi Ayub、Hannah Moran、Cal Rueb 和 Connor Jennings 做出了贡献。特别感谢 Molly Vorwerck、Stuart Ritchie 和 Maggie Vo 的支持。
