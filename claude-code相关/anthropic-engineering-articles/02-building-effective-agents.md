# Building effective agents | 构建有效的智能体

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

在过去一年中，我们与数十个团队合作，在各行业构建大语言模型（LLM）智能体。始终如一的是，最成功的实现并没有使用复杂的框架或专门的库。相反，它们使用简单、可组合的模式进行构建。

In this post, we share what we've learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents.

在这篇文章中，我们分享了与客户合作和自行构建智能体时所获得的经验，并为开发者提供构建有效智能体的实用建议。

## What are agents? | 什么是智能体？

"Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as *agentic systems*, but draw an important architectural distinction between *workflows* and *agents*:

"智能体"可以有几种定义方式。一些客户将智能体定义为在较长时间段内独立运行、使用各种工具完成复杂任务的完全自主系统。另一些客户则用这个术语来描述遵循预定义工作流的更具规定性的实现。在 Anthropic，我们将所有这些变体归类为**智能体系统**，但在**工作流**和**智能体**之间划定了重要的架构区别：

- *Workflows* are systems where LLMs and tools are orchestrated through predefined code paths.
- **工作流**是通过预定义代码路径编排 LLM 和工具的系统。
- *Agents*, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.
- **智能体**则是 LLM 动态指导自身流程和工具使用、保持对如何完成任务进行控制的系统。

Below, we will explore both types of agentic systems in detail. In Appendix 1 ("Agents in Practice"), we describe two domains where customers have found particular value in using these kinds of systems.

下面，我们将详细探讨这两种类型的智能体系统。在附录1（"实践中的智能体"）中，我们描述了客户在使用这些系统时发现特别有价值的两个领域。

## When (and when not) to use agents | 何时（以及何时不）使用智能体

When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

在使用 LLM 构建应用程序时，我们建议找到尽可能简单的解决方案，仅在需要时增加复杂性。这可能意味着根本不构建智能体系统。智能体系统通常以延迟和成本换取更好的任务性能，你应该考虑这种权衡何时是有意义的。

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

当需要更多复杂性时，工作流为明确定义的任务提供可预测性和一致性，而在大规模需要灵活性和模型驱动决策时，智能体是更好的选择。然而，对于许多应用程序，通过检索和上下文示例来优化单个 LLM 调用通常就足够了。

## When and how to use frameworks | 何时以及如何使用框架

There are many frameworks that make agentic systems easier to implement, including:

有许多框架可以使智能体系统更容易实现，包括：

- LangGraph from LangChain;
- LangChain 的 LangGraph；

- Amazon Bedrock's AI Agent framework;
- Amazon Bedrock 的 AI Agent 框架；

- Rivet, a drag and drop GUI LLM workflow builder; and
- Rivet，一个拖放式 GUI LLM 工作流构建器；以及

- Vellum, another GUI tool for building and testing complex workflows.
- Vellum，另一个用于构建和测试复杂工作流的 GUI 工具。

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

这些框架通过简化调用 LLM、定义和解析工具、以及将调用链接在一起等标准低级任务，使入门变得容易。然而，它们经常创建额外的抽象层，可能会掩盖底层的提示和响应，使调试变得更加困难。它们也可能使人在更简单的设置就足够的情况下倾向于增加复杂性。

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

我们建议开发者直接使用 LLM API 开始：许多模式可以在几行代码中实现。如果你确实使用框架，请确保你理解底层代码。对底层代码的错误假设是客户错误的常见来源。

See our cookbook for some sample implementations.

请参阅我们的 cookbook 查看一些示例实现。

## Building blocks, workflows, and agents | 构建模块、工作流和智能体

In this section, we'll explore the common patterns for agentic systems we've seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

在本节中，我们将探讨在生产环境中看到的智能体系统的常见模式。我们将从基础构建模块——增强型 LLM——开始，逐步增加复杂性，从简单的组合工作流到自主智能体。

### Building block: The augmented LLM | 构建模块：增强型 LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

智能体系统的基本构建模块是增强了检索、工具和记忆等功能 augmentations 的 LLM。我们当前的模型可以主动使用这些能力——生成自己的搜索查询、选择适当的工具，以及确定要保留哪些信息。

The augmented LLM

增强型 LLM

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://modelcontextprotocol.io/), which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation.

我们建议重点关注实现的两个关键方面：将这些能力定制到你的特定用例，并确保它们为你的 LLM 提供易于使用且有良好文档记录的接口。虽然有许多方法可以实现这些增强功能，但一种方法是通过我们最近发布的模型上下文协议（[Model Context Protocol](https://modelcontextprotocol.io/)），它允许开发者通过简单的客户端实现与不断增长的第三方工具生态系统集成。

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

在本文的其余部分，我们将假设每个 LLM 调用都可以访问这些增强功能。

### Workflow: Prompt chaining | 工作流：提示链

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate" in the diagram below) on any intermediate steps to ensure that the process is still on track.

提示链将任务分解为一系列步骤，每个 LLM 调用处理前一个调用的输出。你可以在任何中间步骤添加程序化检查（参见下图中的"门"），以确保过程仍在正确的轨道上。

The prompt chaining workflow

提示链工作流

*When to use this workflow:* This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**何时使用此工作流：** 此工作流非常适合可以轻松清晰地分解为固定子任务的情况。主要目标是通过使每个 LLM 调用成为更容易的任务，以延迟换取更高的准确性。

*Examples where prompt chaining is useful:*

**提示链有用的示例：**

- Generating Marketing copy, then translating it into a different language.
- 生成营销文案，然后将其翻译成另一种语言。

- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.
- 编写文档大纲，检查大纲是否符合某些标准，然后根据大纲编写文档。

### Workflow: Routing | 工作流：路由

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

路由对输入进行分类并将其引导到专门的后续任务。此工作流允许分离关注点并构建更专门的提示。如果没有此工作流，针对一种输入进行优化可能会损害其他输入的性能。

The routing workflow

路由工作流

*When to use this workflow:* Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**何时使用此工作流：** 路由适用于有不同类别需要单独处理、并且可以准确进行分类的复杂任务，无论是通过 LLM 还是更传统的分类模型/算法。

*Examples where routing is useful:*

**路由有用的示例：**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- 将不同类型的客户服务查询（一般问题、退款请求、技术支持）引导到不同的下游流程、提示和工具。

- Routing easy/common questions to smaller models like Claude 3.5 Haiku and hard/unusual questions to more capable models like Claude 3.5 Sonnet to optimize cost and speed.
- 将简单/常见问题路由到较小的模型（如 Claude 3.5 Haiku），将困难/不寻常的问题路由到能力更强的模型（如 Claude 3.5 Sonnet），以优化成本和速度。

### Workflow: Parallelization | 工作流：并行化

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

LLM 有时可以同时处理一个任务，并以编程方式聚合其输出。此工作流（并行化）表现为两种主要变体：

- *Sectioning*: Breaking a task into independent subtasks run in parallel.
- **分节**：将任务分解为并行运行的独立子任务。

- *Voting:* Running the same task multiple times to get diverse outputs.
- **投票**：多次运行同一任务以获得多样化的输出。

The parallelization workflow

并行化工作流

*When to use this workflow:* Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

**何时使用此工作流：** 当分解的子任务可以并行化以提高速度，或者需要多个视角或尝试以获得更高置信度的结果时，并行化是有效的。对于具有多个考虑因素的复杂任务，当每个考虑因素由单独的 LLM 调用处理时，LLM 通常表现更好，从而允许专注于每个特定方面。

*Examples where parallelization is useful:*

**并行化有用的示例：**

- *Sectioning*:
- **分节**：
  - Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response.
  - 实现防护栏，其中一个模型实例处理用户查询，另一个模型实例筛选不当内容或请求。这往往比让同一个 LLM 调用处理防护栏和核心响应表现更好。

  - Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model's performance on a given prompt.
  - 自动化评估以评估 LLM 性能，其中每个 LLM 调用评估模型在给定提示上的不同方面的性能。

- *Voting*:
- **投票**：
  - Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
  - 审查代码是否存在漏洞，其中几个不同的提示审查代码并在发现问题时标记。

  - Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.
  - 评估给定内容是否不当，使用多个提示评估不同方面或需要不同的投票阈值以平衡误报和漏报。

### Workflow: Orchestrator-workers | 工作流：编排器-工作者

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

在编排器-工作者工作流中，一个中央 LLM 动态分解任务，将其委托给工作者 LLM，并综合它们的结果。

The orchestrator-workers workflow

编排器-工作者工作流

*When to use this workflow:* This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**何时使用此工作流：** 此工作流非常适合无法预测所需子任务的复杂任务（例如，在编码中，需要更改的文件数量和每个文件中更改的性质可能取决于任务）。尽管在拓扑上相似，但与并行化的关键区别在于其灵活性——子任务不是预定义的，而是由编排器根据特定输入确定的。

*Example where orchestrator-workers is useful:*

**编排器-工作者有用的示例：**

- Coding products that make complex changes to multiple files each time.
- 每次对多个文件进行复杂更改的编码产品。

- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.
- 涉及从多个来源收集和分析信息以查找可能相关信息的搜索任务。

### Workflow: Evaluator-optimizer | 工作流：评估器-优化器

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

在评估器-优化器工作流中，一个 LLM 调用生成响应，而另一个 LLM 调用在循环中提供评估和反馈。

The evaluator-optimizer workflow

评估器-优化器工作流

*When to use this workflow:* This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**何时使用此工作流：** 当我们有明确的评估标准，并且迭代改进可提供可衡量的价值时，此工作流特别有效。适合的两个标志是：首先，当人类表达他们的反馈时，LLM 响应可以明显改善；其次，LLM 可以提供此类反馈。这类似于人类作家在生成润色文档时可能经历的迭代写作过程。

*Examples where evaluator-optimizer is useful:*

**评估器-优化器有用的示例：**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- 文学翻译，其中存在翻译器 LLM 最初可能无法捕捉的细微差别，但评估器 LLM 可以提供有用的批评。

- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.
- 需要多轮搜索和分析以收集全面信息的复杂搜索任务，其中评估器决定是否需要进一步搜索。

### Agents | 智能体

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain "ground truth" from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

随着 LLM 在关键能力——理解复杂输入、参与推理和规划、可靠地使用工具以及从错误中恢复——方面的发展，智能体正在生产环境中出现。智能体通过来自人类的命令或与人类的交互讨论开始工作。一旦任务明确，智能体就会独立规划和操作，可能会向人类寻求更多信息或判断。在执行过程中，智能体必须在每一步从环境中获得"真实答案"（例如工具调用结果或代码执行）以评估其进度。智能体可以在检查点或遇到障碍时暂停以获取人类反馈。任务通常在完成时终止，但也包括停止条件（例如最大迭代次数）以保持控制也是常见的。

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

智能体可以处理复杂的任务，但其实现通常很简单。它们通常只是在循环中基于环境反馈使用工具的 LLM。因此，清晰而深思熟虑地设计工具集及其文档至关重要。我们在附录2（"提示工程你的工具"）中扩展了工具开发的最佳实践。

Autonomous agent

自主智能体

*When to use agents:* Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

**何时使用智能体：** 智能体可用于难以或无法预测所需步骤数量、并且无法硬编码固定路径的开放式问题。LLM 可能会运行许多轮，并且你必须对其决策有一定程度的信任。智能体的自主性使其成为在受信任的环境中扩展任务的理想选择。

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

智能体的自主性质意味着更高的成本以及复合错误的潜在可能性。我们建议在沙盒环境中进行广泛的测试，并配合适当的防护措施。

*Examples where agents are useful:*

**智能体有用的示例：**

The following examples are from our own implementations:

以下示例来自我们自己的实现：

- A coding Agent to resolve SWE-bench tasks, which involve edits to many files based on a task description;
- 一个解决 SWE-bench 任务的编码智能体，涉及根据任务描述编辑多个文件；

- Our "computer use" reference implementation, where Claude uses a computer to accomplish tasks.
- 我们的"计算机使用"参考实现，其中 Claude 使用计算机完成任务。

High-level flow of a coding agent

编码智能体的高级流程

## Combining and customizing these patterns | 组合和定制这些模式

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

这些构建模块不是规定性的。它们是开发者可以塑造和组合以适应不同用例的常见模式。与任何 LLM 功能一样，成功的关键是衡量性能并迭代实现。重申一遍：只有在复杂性明显改善结果时，你才应该考虑增加复杂性。

## Summary | 总结

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

在 LLM 领域取得成功并不是要构建最复杂的系统。而是要为你的需求构建_正确的_系统。从简单的提示开始，通过全面的评估对其进行优化，只有在更简单的解决方案不足时才添加多步骤智能体系统。

When implementing agents, we try to follow three core principles:

在实现智能体时，我们尝试遵循三个核心原则：

1. Maintain *simplicity* in your agent's design.
在智能体设计中保持**简单性**。

2. Prioritize *transparency* by explicitly showing the agent's planning steps.
通过明确显示智能体的规划步骤来优先考虑**透明度**。

3. Carefully craft your agent-computer interface (ACI) through thorough tool *documentation and testing*.
通过彻底的工具**文档和测试**精心设计智能体-计算机接口（ACI）。

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

框架可以帮助你快速入门，但在转向生产时不要犹豫减少抽象层并使用基本组件构建。通过遵循这些原则，你可以创建不仅强大而且可靠、可维护且受用户信任的智能体。

### Acknowledgements | 致谢

Written by Erik Schluntz and Barry Zhang. This work draws upon our experiences building agents at Anthropic and the valuable insights shared by our customers, for which we're deeply grateful.

由 Erik Schluntz 和 Barry Zhang 撰写。这项工作基于我们在 Anthropic 构建智能体的经验以及客户分享的有价值的见解，我们对此深表感谢。

## Appendix 1: Agents in practice | 附录 1：实践中的智能体

Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight.

我们与客户的工作揭示了两个特别有前景的 AI 智能体应用，展示了上述讨论的模式的实际价值。这两个应用都说明了智能体如何为既需要对话又需要行动、具有明确的成功标准、支持反馈循环并集成有意义的人类监督的任务增加最大价值。

### A. Customer support | A. 客户支持

Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because:

客户支持通过工具集成将熟悉的聊天机器人界面与增强功能相结合。这对于更开放的智能体来说是一个自然的契合，因为：

- Support interactions naturally follow a conversation flow while requiring access to external information and actions;
- 支持交互自然遵循对话流程，同时需要访问外部信息和操作；

- Tools can be integrated to pull customer data, order history, and knowledge base articles;
- 可以集成工具来提取客户数据、订单历史和知识库文章；

- Actions such as issuing refunds or updating tickets can be handled programmatically; and
- 诸如发放退款或更新工单等操作可以通过编程方式处理；并且

- Success can be clearly measured through user-defined resolutions.
- 成功可以通过用户定义的解决方案来明确衡量。

Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness.

几家公司通过仅对成功解决方案收费的基于使用量的定价模型展示了这种方法的可行性，表明对其智能体效果的信心。

### B. Coding agents | B. 编码智能体

The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because:

软件开发领域展现了 LLM 功能的巨大潜力，能力从代码补全发展到自主问题解决。智能体特别有效，因为：

- Code solutions are verifiable through automated tests;
- 代码解决方案可以通过自动化测试进行验证；

- Agents can iterate on solutions using test results as feedback;
- 智能体可以使用测试结果作为反馈来迭代解决方案；

- The problem space is well-defined and structured; and
- 问题空间定义明确且结构化；并且

- Output quality can be measured objectively.
- 输出质量可以客观衡量。

In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

在我们自己的实现中，智能体现在可以仅根据拉取请求描述解决 SWE-bench Verified 基准测试中的真实 GitHub 问题。然而，虽然自动化测试有助于验证功能，但人工审查对于确保解决方案符合更广泛的系统要求仍然至关重要。

## Appendix 2: Prompt engineering your tools | 附录 2：提示工程你的工具

No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

无论你构建哪种智能体系统，工具都可能是智能体的重要组成部分。工具使 Claude 能够通过在我们的 API 中指定其确切结构和定义来与外部服务和 API 交互。当 Claude 响应时，如果它计划调用工具，它将在 API 响应中包含工具使用块。工具定义和规范应该与你的整体提示一样受到同等的提示工程关注。在这个简短的附录中，我们描述了如何对你的工具进行提示工程。

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

通常有几种方法可以指定相同的操作。例如，你可以通过编写 diff 或重写整个文件来指定文件编辑。对于结构化输出，你可以返回 markdown 或 JSON 中的代码。在软件工程中，这些差异是表面的，可以无损地相互转换。然而，对于 LLM 来说，某些格式比其他格式更难编写。编写 diff 需要在编写新代码之前知道块头中有多少行正在更改。在 JSON 中编写代码（与 markdown 相比）需要对换行符和引号进行额外的转义。

Our suggestions for deciding on tool formats are the following:

我们关于决定工具格式的建议如下：

- Give the model enough tokens to "think" before it writes itself into a corner.
- 给模型足够的 token 来"思考"，以免它将自己写入死角。

- Keep the format close to what the model has seen naturally occurring in text on the internet.
- 保持格式接近模型在互联网上的文本中自然看到的内容。

- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.
- 确保没有格式"开销"，例如必须准确计算数千行代码，或对其编写的任何代码进行字符串转义。

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

一个经验法则是考虑在人机交互界面（HCI）上投入多少精力，并计划投入同样的精力来创建良好的_智能体_-计算机接口（ACI）。以下是一些关于如何这样做的思考：

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- 设身处地为模型着想。根据描述和参数，如何使用这个工具是否明显，或者你需要仔细考虑吗？如果是这样，那么对模型来说可能也是如此。一个好的工具定义通常包括示例用法、边缘情况、输入格式要求以及与其他工具的清晰边界。

- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- 你可以如何更改参数名称或描述使事情更明显？将其视为为团队中的初级开发者编写出色的文档字符串。在使用许多类似工具时，这尤其重要。

- Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate.
- 测试模型如何使用你的工具：在我们的工作台中运行许多示例输入，看看模型犯了什么错误，然后迭代。

- Poka-yoke your tools. Change the arguments so that it is harder to make mistakes.
- 对你的工具进行防错（Poka-yoke）。更改参数，使其更难犯错。

While building our agent for SWE-bench, we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

在为 SWE-bench 构建我们的智能体时，我们实际上花了更多时间优化我们的工具而不是整体提示。例如，我们发现模型在智能体移出根目录后，使用相对文件路径的工具会犯错误。为了解决这个问题，我们将工具更改为始终需要绝对文件路径——我们发现模型完美地使用了这种方法。

---

## Sources | 来源

- [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents)
- [构建有效的 AI 智能体](https://www.anthropic.com/research/building-effective-agents)
