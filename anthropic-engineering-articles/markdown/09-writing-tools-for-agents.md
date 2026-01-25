# Writing effective tools for AI agents—using AI agents | 为AI智能体编写有效工具——使用AI智能体

The Model Context Protocol (MCP) can empower LLM agents with potentially hundreds of tools to solve real-world tasks. But how do we make those tools maximally effective?

模型上下文协议（MCP）可以为 LLM 智能体配备数百种工具来解决现实世界任务。但我们要如何让这些工具发挥最大效用呢？

In this post, we describe our most effective techniques for improving performance in a variety of agentic AI systems.

在本文中，我们描述了在各种智能体 AI 系统中提高性能的最有效技术。

We begin by covering how you can:

我们首先涵盖你可以如何：

- Build and test prototypes of your tools

- 构建和测试你的工具原型

- Create and run comprehensive evaluations of your tools with agents

- 使用智能体创建并运行对你工具的综合评估

- Collaborate with agents like Claude Code to automatically increase the performance of your tools

- 与像 Claude Code 这样的智能体协作，自动提升你工具的性能

We conclude with key principles for writing high-quality tools we've identified along the way:

我们最后总结了我们在过程中总结的编写高质量工具的关键原则：

- Choosing the right tools to implement (and not to implement)

- 选择正确的工具来实现（以及不实现）

- Namespacing tools to define clear boundaries in functionality

- 为工具添加命名空间以定义清晰的功能边界

- Returning meaningful context from tools back to agents

- 从工具向智能体返回有意义的上下文

- Optimizing tool responses for token efficiency

- 优化工具响应以提高标记效率

- Prompt-engineering tool descriptions and specs

- 对工具描述和规范进行提示工程

![An engineer might use Claude Code to evaluate the efficacy of agentic tools.](https://www-cdn.anthropic.com/images/4zrzovbb/website/cdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png)

工程师可能会使用 Claude Code 来评估智能体工具的功效。

Building an evaluation allows you to systematically measure the performance of your tools. You can use Claude Code to automatically optimize your tools against this evaluation.

构建评估让你能够系统性地测量工具的性能。你可以使用 Claude Code 针对此评估自动优化你的工具。

## What is a tool? | 什么是工具？

In computing, deterministic systems produce the same output every time given identical inputs, while _non-deterministic_ systems—like agents—can generate varied responses even with the same starting conditions.

在计算中，确定性系统在给定相同输入时每次都产生相同的输出，而_非确定性_系统——如智能体——即使在相同的起始条件下也可能生成不同的响应。

When we traditionally write software, we're establishing a contract between deterministic systems. For instance, a function call like `getWeather("NYC")` will always fetch the weather in New York City in the exact same manner every time it is called.

当我们传统地编写软件时，我们正在建立确定性系统之间的契约。例如，像 `getWeather("NYC")` 这样的函数调用将始终以完全相同的方式获取纽约市的天气。

Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents. When a user asks "Should I bring an umbrella today?," an agent might call the weather tool, answer from general knowledge, or even ask a clarifying question about location first. Occasionally, an agent might hallucinate or even fail to grasp how to use a tool.

工具是一种新型软件，它反映了确定性系统与非确定性智能体之间的契约。当用户问"我今天应该带伞吗？"时，智能体可能会调用天气工具，从常识中回答，甚至首先询问关于位置的澄清问题。偶尔，智能体可能会产生幻觉，甚至无法理解如何使用工具。

This means fundamentally rethinking our approach when writing software for agents: instead of writing tools and MCP servers the way we'd write functions and APIs for other developers or systems, we need to design them for agents.

这意味着在为智能体编写软件时需要从根本上重新思考我们的方法：我们需要为智能体设计工具和 MCP 服务器，而不是像为其他开发者或系统编写函数和 API 那样。

Our goal is to increase the surface area over which agents can be effective in solving a wide range of tasks by using tools to pursue a variety of successful strategies. Fortunately, in our experience, the tools that are most "ergonomic" for agents also end up being surprisingly intuitive to grasp as humans.

我们的目标是通过使用工具来追求各种成功的策略，扩大智能体在解决各种任务方面的有效范围。幸运的是，根据我们的经验，对智能体来说最"符合人体工程学"的工具最终对人类来说也出奇地直观。

## How to write tools | 如何编写工具

In this section, we describe how you can collaborate with agents both to write and to improve the tools you give them. Start by standing up a quick prototype of your tools and testing them locally. Next, run a comprehensive evaluation to measure subsequent changes. Working alongside agents, you can repeat the process of evaluating and improving your tools until your agents achieve strong performance on real-world tasks.

在本节中，我们描述如何与智能体协作来编写和改进你给它们的工具。首先快速构建你的工具原型并在本地测试。接下来，运行综合评估来测量后续的更改。与智能体一起工作，你可以重复评估和改进工具的过程，直到你的智能体在现实世界任务上实现强大的性能。

### Building a prototype | 构建原型

It can be difficult to anticipate which tools agents will find ergonomic and which tools they won't without getting hands-on yourself. Start by standing up a quick prototype of your tools. If you're using Claude Code to write your tools (potentially in one-shot), it helps to give Claude documentation for any software libraries, APIs, or SDKs (including potentially the MCP SDK) your tools will rely on. LLM-friendly documentation can commonly be found in flat `llms.txt` files on official documentation sites (here's our API's).

如果不亲自动手，很难预测智能体会觉得哪些工具符合人体工程学，哪些不会。首先快速构建你的工具原型。如果你使用 Claude Code 编写工具（可能是一次性编写），为你的工具所依赖的任何软件库、API 或 SDK（包括可能的 MCP SDK）提供 Claude 文档会很有帮助。对 LLM 友好的文档通常可以在官方文档站点上的平面 `llms.txt` 文件中找到（这是我们 API 的文档）。

Wrapping your tools in a local MCP server or Desktop extension (DXT) will allow you to connect and test your tools in Claude Code or the Claude Desktop app.

将你的工具包装在本地 MCP 服务器或桌面扩展（DXT）中，将允许你在 Claude Code 或 Claude 桌面应用中连接和测试你的工具。

To connect your local MCP server to Claude Code, run `claude mcp add <name> <command> [args...]`.

要将本地 MCP 服务器连接到 Claude Code，运行 `claude mcp add <name> <command> [args...]`。

To connect your local MCP server or DXT to the Claude Desktop app, navigate to `Settings > Developer` or `Settings > Extensions`, respectively.

要将本地 MCP 服务器或 DXT 连接到 Claude 桌面应用，分别导航到 `Settings > Developer` 或 `Settings > Extensions`。

Tools can also be passed directly into Anthropic API calls for programmatic testing.

工具也可以直接传递到 Anthropic API 调用中以进行程序化测试。

Test the tools yourself to identify any rough edges. Collect feedback from your users to build an intuition around the use-cases and prompts you expect your tools to enable.

自己测试工具以识别任何粗糙的边缘。收集用户的反馈，以建立对你期望工具启用的用例和提示的直觉。

### Running an evaluation | 运行评估

Next, you need to measure how well Claude uses your tools by running an evaluation. Start by generating lots of evaluation tasks, grounded in real world uses. We recommend collaborating with an agent to help analyze your results and determine how to improve your tools. See this process end-to-end in our [tool evaluation cookbook](https://docs.anthropic.com/en/docs/build-with-claude/tool-evaluation).

接下来，你需要通过运行评估来测量 Claude 使用你的工具的效果。首先生成许多评估任务，基于现实世界的使用。我们建议与智能体合作帮助分析你的结果并确定如何改进你的工具。在我们的[工具评估手册](https://docs.anthropic.com/en/docs/build-with-claude/tool-evaluation)中端到端地查看此过程。

![This graph measures the test set accuracy of human-written vs. Claude-optimized Slack MCP servers.](https://www-cdn.anthropic.com/images/4zrzovbb/website/6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png)

此图表测量了人工编写的与 Claude 优化的 Slack MCP 服务器的测试集准确性。

Held-out test set performance of our internal Slack tools

我们内部 Slack 工具的保留测试集性能

__Generating evaluation tasks__

__生成评估任务__

With your early prototype, Claude Code can quickly explore your tools and create dozens of prompt and response pairs. Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices). We recommend you avoid overly simplistic or superficial "sandbox" environments that don't stress-test your tools with sufficient complexity. Strong evaluation tasks might require multiple tool calls—potentially dozens.

使用你的早期原型，Claude Code 可以快速探索你的工具并创建数十个提示和响应对。提示应该受到现实世界使用的启发，并基于现实的数据源和服务（例如，内部知识库和微服务）。我们建议你避免过于简单或表面的"沙箱"环境，这些环境不会以足够的复杂性对你的工具进行压力测试。强大的评估任务可能需要多次工具调用——可能多达数十次。

Here are some examples of strong tasks:

以下是一些强大任务的示例：

- Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach the notes from our last project planning meeting and reserve a conference room.

- 安排下周与 Jane 的会议，讨论我们最新的 Acme Corp 项目。附上我们上次项目规划会议的笔记并预订会议室。

- Customer ID 9182 reported that they were charged three times for a single purchase attempt. Find all relevant log entries and determine if any other customers were affected by the same issue.

- 客户 ID 9182 报告他们在一次购买尝试中被收取了三次费用。查找所有相关的日志条目，并确定是否有任何其他客户受到同一问题的影响。

- Customer Sarah Chen just submitted a cancellation request. Prepare a retention offer. Determine: (1) why they're leaving, (2) what retention offer would be most compelling, and (3) any risk factors we should be aware of before making an offer.

- 客户 Sarah Chen 刚刚提交了取消请求。准备一个挽留优惠。确定：(1) 他们为什么要离开，(2) 什么挽留优惠最有吸引力，以及 (3) 在提出优惠之前我们应该注意的任何风险因素。

And here are some weaker tasks:

以下是一些较弱的任务：

- Schedule a meeting with jane@acme.corp next week.

- 安排下周与 jane@acme.corp 的会议。

- Search the payment logs for `purchase_complete` and `customer_id=9182`.

- 在支付日志中搜索 `purchase_complete` 和 `customer_id=9182`。

- Find the cancellation request by Customer ID 45892.

- 查找客户 ID 45892 的取消请求。

Each evaluation prompt should be paired with a verifiable response or outcome. Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response. Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings.

每个评估提示应该与可验证的响应或结果配对。你的验证器可以简单到基本事实和采样响应之间的精确字符串比较，也可以高级到让 Claude 来判断响应。避免过于严格的验证器，它们会因格式、标点符号或有效的替代措辞等虚假差异而拒绝正确的响应。

For each prompt-response pair, you can optionally also specify the tools you expect an agent to call in solving the task, to measure whether or not agents are successful in grasping each tool's purpose during evaluation. However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies.

对于每个提示-响应对，你还可以选择指定你期望智能体在解决任务时调用的工具，以测量智能体是否在评估期间成功掌握每个工具的用途。然而，由于可能有多种正确的有效路径来解决任务，尽量避免过度指定或过度拟合策略。

__Running the evaluation__

__运行评估__

We recommend running your evaluation programmatically with direct LLM API calls. Use simple agentic loops (`while`-loops wrapping alternating LLM API and tool calls): one loop for each evaluation task. Each evaluation agent should be given a single task prompt and your tools.

我们建议通过直接 LLM API 调用以编程方式运行评估。使用简单的智能体循环（包装交替的 LLM API 和工具调用的 `while` 循环）：每个评估任务一个循环。每个评估智能体应该被赋予一个单一任务提示和你的工具。

In your evaluation agents' system prompts, we recommend instructing agents to output not just structured response blocks (for verification), but also reasoning and feedback blocks. Instructing agents to output these _before_ tool call and response blocks may increase LLMs' effective intelligence by triggering chain-of-thought (CoT) behaviors.

在评估智能体的系统提示中，我们建议指示智能体不仅输出结构化响应块（用于验证），还输出推理和反馈块。指示智能体在工具调用和响应块之前输出这些可能会通过触发思维链（CoT）行为来提高 LLM 的有效智能。

If you're running your evaluation with Claude, you can turn on interleaved thinking for similar functionality "off-the-shelf". This will help you probe why agents do or don't call certain tools and highlight specific areas of improvement in tool descriptions and specs.

如果你使用 Claude 运行评估，你可以开启交错思考以获得"开箱即用"的类似功能。这将帮助你探测智能体为什么调用或不调用某些工具，并突出工具描述和规范中需要改进的具体领域。

As well as top-level accuracy, we recommend collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors. Tracking tool calls can help reveal common workflows that agents pursue and offer some opportunities for tools to consolidate.

除了顶层准确性之外，我们还建议收集其他指标，如单个工具调用和任务的总运行时间、工具调用总数、总标记消耗和工具错误。跟踪工具调用可以帮助揭示智能体追求的常见工作流程，并为工具整合提供一些机会。

![This graph measures the test set accuracy of human-written vs. Claude-optimized Asana MCP servers.](https://www-cdn.anthropic.com/images/4zrzovbb/website/3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png)

此图表测量了人工编写的与 Claude 优化的 Asana MCP 服务器的测试集准确性。

Held-out test set performance of our internal Asana tools

我们内部 Asana 工具的保留测试集性能

__Analyzing results__

__分析结果__

Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas. However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include. LLMs don't always say what they mean.

智能体是你发现问题的有用伙伴，并提供从矛盾的工具描述到低效的工具实现和混乱的工具架构的所有内容的反馈。然而，请记住，智能体在其反馈和响应中省略的内容往往比它们包含的内容更重要。LLM 并不总是说它们的本意。

Observe where your agents get stumped or confused. Read through your evaluation agents' reasoning and feedback (or CoT) to identify rough edges. Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent's CoT. Read between the lines; remember that your evaluation agents don't necessarily know the correct answers and strategies.

观察你的智能体在哪里被难住或困惑。通读评估智能体的推理和反馈（或 CoT）以识别粗糙的边缘。审查原始记录（包括工具调用和工具响应）以捕获智能体的 CoT 中未明确描述的任何行为。读懂言外之意；记住你的评估智能体不一定知道正确的答案和策略。

Analyze your tool calling metrics. Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples. When we launched Claude's web search tool, we identified that Claude was needlessly appending `2025` to the tool's `query` parameter, biasing search results and degrading performance (we steered Claude in the right direction by improving the tool description).

分析你的工具调用指标。大量冗余的工具调用可能表明需要对分页或标记限制参数进行适当调整；大量无效参数的工具错误可能表明工具可以使用更清晰的描述或更好的示例。当我们推出 Claude 的网络搜索工具时，我们发现 Claude 不必要地在工具的 `query` 参数上附加 `2025`，从而使搜索结果产生偏差并降低性能（我们通过改进工具描述将 Claude 引向正确的方向）。

### Collaborating with agents | 与智能体协作

You can even let agents analyze your results and improve your tools for you. Simply concatenate the transcripts from your evaluation agents and paste them into Claude Code. Claude is an expert at analyzing transcripts and refactoring lots of tools all at once—for example, to ensure tool implementations and descriptions remain self-consistent when new changes are made.

你甚至可以让智能体分析你的结果并为你改进工具。只需连接评估智能体的记录并将它们粘贴到 Claude Code 中。Claude 是分析记录和一次性重构大量工具的专家——例如，以确保工具实现和描述在进行新更改时保持自洽。

In fact, most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code. Our evaluations were created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages.

事实上，本文中的大多数建议来自使用 Claude Code 反复优化我们的内部工具实现。我们的评估是在我们的内部工作区之上创建的，反映了我们内部工作流程的复杂性，包括真实的项目、文档和消息。

We relied on held-out test sets to ensure we did not overfit to our "training" evaluations. These test sets revealed that we could extract additional performance improvements even beyond what we achieved with "expert" tool implementations—whether those tools were manually written by our researchers or generated by Claude itself.

我们依赖保留测试集来确保我们不会过度拟合我们的"训练"评估。这些测试集表明，我们可以提取超越我们在"专家"工具实现中所实现的额外性能改进——无论这些工具是由我们的研究人员手动编写还是由 Claude 本身生成。

In the next section, we'll share some of what we learned from this process.

在下一节中，我们将分享我们从这一过程中学到的一些内容。

## Principles for writing effective tools | 编写有效工具的原则

In this section, we distill our learnings into a few guiding principles for writing effective tools.

在本节中，我们将我们的学习提炼为编写有效工具的几个指导原则。

### Choosing the right tools for agents | 为智能体选择正确的工具

More tools don't always lead to better outcomes. A common error we've observed is tools that merely wrap existing software functionality or API endpoints—whether or not the tools are appropriate for agents. This is because agents have distinct "affordances" to traditional software—that is, they have different ways of perceiving the potential actions they can take with those tools

更多的工具并不总是导致更好的结果。我们观察到的一个常见错误是工具仅仅包装现有的软件功能或 API 端点——无论这些工具是否适合智能体。这是因为智能体具有与传统软件截然不同的"可供性"——也就是说，它们以不同的方式感知可以使用这些工具采取的潜在行动

LLM agents have limited "context" (that is, there are limits to how much information they can process at once), whereas computer memory is cheap and abundant. Consider the task of searching for a contact in an address book. Traditional software programs can efficiently store and process a list of contacts one at a time, checking each one before moving on.

LLM 智能体具有有限的"上下文"（也就是说，它们一次可以处理的信息量有限制），而计算机内存便宜且丰富。考虑在地址簿中搜索联系人的任务。传统软件程序可以高效地存储和处理联系人列表，一次处理一个，在继续之前检查每个联系人。

However, if an LLM agent uses a tool that returns ALL contacts and then has to read through each one token-by-token, it's wasting its limited context space on irrelevant information (imagine searching for a contact in your address book by reading each page from top-to-bottom—that is, via brute-force search). The better and more natural approach (for agents and humans alike) is to skip to the relevant page first (perhaps finding it alphabetically).

然而，如果 LLM 智能体使用返回所有联系人的工具，然后必须逐个标记地阅读每个联系人，它会将有限的上下文空间浪费在无关信息上（想象一下通过从上到下阅读每一页来在地址簿中搜索联系人——也就是说，通过暴力搜索）。更好且更自然的方法（对智能体和人类都一样）是首先跳到相关的页面（也许按字母顺序找到它）。

We recommend building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there. In the address book case, you might choose to implement a `search_contacts` or `message_contact` tool instead of a `list_contacts` tool.

我们建议构建一些针对特定高影响力工作流程的深思熟虑的工具，这些工具与你的评估任务相匹配，并从那里扩展。在地址簿的情况下，你可能会选择实现 `search_contacts` 或 `message_contact` 工具，而不是 `list_contacts` 工具。

Tools can consolidate functionality, handling potentially _multiple_ discrete operations (or API calls) under the hood. For example, tools can enrich tool responses with related metadata or handle frequently chained, multi-step tasks in a single tool call.

工具可以整合功能，在底层处理潜在的_多个_离散操作（或 API 调用）。例如，工具可以用相关元数据丰富工具响应，或者在单个工具调用中处理频繁链接的多步骤任务。

Here are some examples:

以下是一些示例：

- Instead of implementing a `list_users`, `list_events`, and `create_event` tools, consider implementing a `schedule_event` tool which finds availability and schedules an event.

- 与其实现 `list_users`、`list_events` 和 `create_event` 工具，不如考虑实现 `schedule_event` 工具，它可以查找可用性并安排事件。

- Instead of implementing a `read_logs` tool, consider implementing a `search_logs` tool which only returns relevant log lines and some surrounding context.

- 与其实现 `read_logs` 工具，不如考虑实现 `search_logs` 工具，它只返回相关的日志行和一些周围的上下文。

- Instead of implementing `get_customer_by_id`, `list_transactions`, and `list_notes` tools, implement a `get_customer_context` tool which compiles all of a customer's recent & relevant information all at once.

- 与其实现 `get_customer_by_id`、`list_transactions` 和 `list_notes` 工具，不如实现 `get_customer_context` 工具，它一次性编译客户的所有最近和相关信息。

Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs.

确保你构建的每个工具都有清晰、独特的用途。工具应该使智能体能够像人类一样细分和解决任务（假设可以访问相同的底层资源），同时减少否则会被中间输出消耗的上下文。

Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don't build) can really pay off.

太多的工具或重叠的工具也会分散智能体追求高效策略的注意力。仔细、有选择地规划你构建（或不构建）的工具真的会有回报。

### Namespacing your tools | 为工具添加命名空间

Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different tools–including those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use.

你的 AI 智能体可能会访问数十个 MCP 服务器和数百种不同的工具——包括其他开发者的工具。当工具在功能上重叠或目的模糊时，智能体可能会对使用哪些工具感到困惑。

Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools; MCP clients sometimes do this by default. For example, namespacing tools by service (e.g., `asana_search`, `jira_search`) and by resource (e.g., `asana_projects_search`, `asana_users_search`), can help agents select the right tools at the right time.

命名空间（将相关工具分组在公共前缀下）可以帮助在许多工具之间划定边界；MCP 客户端有时默认执行此操作。例如，按服务（例如 `asana_search`、`jira_search`）和按资源（例如 `asana_projects_search`、`asana_users_search`）对工具进行命名空间，可以帮助智能体在正确的时间选择正确的工具。

We have found selecting between prefix- and suffix-based namespacing to have non-trivial effects on our tool-use evaluations. Effects vary by LLM and we encourage you to choose a naming scheme according to your own evaluations.

我们发现选择基于前缀和基于后缀的命名空间对我们的工具使用评估有非平凡的影响。效果因 LLM 而异，我们鼓励你根据自己的评估选择命名方案。

Agents might call the wrong tools, call the right tools with the wrong parameters, call too few tools, or process tool responses incorrectly. By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent's context and offload agentic computation from the agent's context back into the tool calls themselves. This reduces an agent's overall risk of making mistakes.

智能体可能会调用错误的工具，用错误的参数调用正确的工具，调用太少的工具，或错误地处理工具响应。通过选择性地实现名称反映任务自然细分的工具，你同时减少了加载到智能体上下文中的工具和工具描述的数量，并将智能体计算从智能体的上下文卸载回工具调用本身。这降低了智能体犯错的总体风险。

### Returning meaningful context from your tools | 从工具返回有意义的上下文

In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents' downstream actions and responses.

同样，工具实现应该注意只向智能体返回高信号信息。它们应该优先考虑上下文相关性而不是灵活性，并避免低级技术标识符（例如：`uuid`、`256px_image_url`、`mime_type`）。像 `name`、`image_url` 和 `file_type` 这样的字段更有可能直接通知智能体的下游行动和响应。

Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers. We've found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude's precision in retrieval tasks by reducing hallucinations.

智能体也倾向于比处理神秘标识符更成功地处理自然语言名称、术语或标识符。我们发现，仅将任意字母数字 UUID 解析为更有语义意义和可解释的语言（甚至是从 0 开始索引的 ID 方案）就可以通过减少幻觉显著提高 Claude 在检索任务中的精度。

In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls (for example, `search_user(name='jane')` → `send_message(id=12345)`). You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `"concise"` or `"detailed"` responses (images below).

在某些情况下，智能体可能需要与自然语言和技术标识符输出交互的灵活性，即使只是为了触发下游工具调用（例如，`search_user(name='jane')` → `send_message(id=12345)`）。你可以通过在工具中暴露一个简单的 `response_format` 枚举参数来实现两者，允许你的智能体控制工具是返回 `"concise"` 还是 `"detailed"` 响应（下图）。

You can add more formats for even greater flexibility, similar to GraphQL where you can choose exactly which pieces of information you want to receive. Here is an example ResponseFormat enum to control tool response verbosity:

你可以添加更多格式以获得更大的灵活性，类似于 GraphQL，你可以选择接收哪些信息片段。以下是控制工具响应详细程度的 ResponseFormat 枚举示例：

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

Here's an example of a detailed tool response (206 tokens):

以下是详细工具响应的示例（206 个标记）：

![This code snippet depicts an example of a detailed tool response.](https://www-cdn.anthropic.com/images/4zrzovbb/website/5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png)

此代码片段描述了详细工具响应的示例。

Here's an example of a concise tool response (72 tokens):

以下是简洁工具响应的示例（72 个标记）：

![This code snippet depicts a concise tool response.](https://www-cdn.anthropic.com/images/4zrzovbb/website/d4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png)

此代码片段描述了简洁工具响应的示例。

Slack threads and thread replies are identified by unique `thread_ts` which are required to fetch thread replies. `thread_ts` and other IDs (`channel_id`, `user_id`) can be retrieved from a `"detailed"` tool response to enable further tool calls that require these. `"concise"` tool responses return only thread content and exclude IDs. In this example, we use ~⅓ of the tokens with `"concise"` tool responses.

Slack 线程和线程回复由唯一的 `thread_ts` 标识，这是获取线程回复所需的。`thread_ts` 和其他 ID（`channel_id`、`user_id`）可以从 `"detailed"` 工具响应中检索，以启用需要这些 ID 的进一步工具调用。`"concise"` 工具响应仅返回线程内容并排除 ID。在此示例中，我们使用 `"concise"` 工具响应时使用了约 ⅓ 的标记。

Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on evaluation performance: there is no one-size-fits-all solution. This is because LLMs are trained on next-token prediction and tend to perform better with formats that match their training data. The optimal response structure will vary widely by task and agent. We encourage you to select the best response structure based on your own evaluation.

即使是你的工具响应结构——例如 XML、JSON 或 Markdown——也会影响评估性能：没有一刀切的解决方案。这是因为 LLM 是在下一个标记预测上训练的，并且在与训练数据匹配的格式上表现更好。最佳响应结构将因任务和智能体而异。我们鼓励你根据自己的评估选择最佳响应结构。

### Optimizing tool responses for token efficiency | 优化工具响应以提高标记效率

Optimizing the quality of context is important. But so is optimizing the _quantity_ of context returned back to agents in tool responses.

优化上下文的质量很重要。但优化工具响应中返回给智能体的上下文_数量_也很重要。

We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.

我们建议为可能使用大量上下文的任何工具响应实现分页、范围选择、过滤和/或截断的某种组合，并具有合理的默认参数值。对于 Claude Code，我们默认将工具响应限制为 25,000 个标记。我们期望智能体的有效上下文长度会随着时间增长，但对上下文高效工具的需求将保持不变。

If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task. Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

如果你选择截断响应，请确保通过有用的指令引导智能体。你可以直接鼓励智能体追求更节省标记的策略，例如进行许多小的和有针对性的搜索，而不是对知识检索任务进行单一的广泛搜索。同样，如果工具调用引发错误（例如，在输入验证期间），你可以对错误响应进行提示工程，以清楚地传达具体和可操作的改进，而不是不透明的错误代码或回溯。

Here's an example of a truncated tool response:

以下是截断工具响应的示例：

![This image depicts an example of a truncated tool response.](https://www-cdn.anthropic.com/images/4zrzovbb/website/e440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png)

此图像描述了截断工具响应的示例。

Here's an example of an unhelpful error response:

以下是无帮助的错误响应的示例：

![This image depicts an example of an unhelpful tool response.](https://www-cdn.anthropic.com/images/4zrzovbb/website/2445187904704fec8c50af0b950e310ba743fac2-1920x733.png)

此图像描述了无帮助的工具响应的示例。

Here's an example of a helpful error response:

以下是有帮助的错误响应的示例：

![This image depicts an example of a helpful error response.](https://www-cdn.anthropic.com/images/4zrzovbb/website/810661bd44a35fb273806ae95160040155978c3e-1920x850.png)

此图像描述了有帮助的工具响应的示例。

Tool truncation and error responses can steer agents towards more token-efficient tool-use behaviors (using filters or pagination) or give examples of correctly formatted tool inputs.

工具截断和错误响应可以引导智能体朝向更节省标记的工具使用行为（使用过滤器或分页），或给出正确格式化的工具输入的示例。

### Prompt-engineering your tool descriptions | 对工具描述进行提示工程

We now come to one of the most effective methods for improving tools: prompt-engineering your tool descriptions and specs. Because these are loaded into your agents' context, they can collectively steer agents toward effective tool-calling behaviors.

我们现在来讨论改进工具的最有效方法之一：对工具描述和规范进行提示工程。因为这些被加载到智能体的上下文中，它们可以共同引导智能体采用有效的工具调用行为。

When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.

在编写工具描述和规范时，想想你会如何向团队的新员工描述你的工具。考虑你可能隐式带来的上下文——专门的查询格式、小众术语的定义、底层资源之间的关系——并使其明确化。通过清楚地描述（并通过严格的数据模型强制执行）预期的输入和输出来避免歧义。特别是，输入参数应该明确无误地命名：尝试使用名为 `user_id` 的参数，而不是名为 `user` 的参数。

With your evaluation you can measure the impact of your prompt engineering with greater confidence. Even small refinements to tool descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved state-of-the-art performance on the [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench) evaluation after we made precise refinements to tool descriptions, dramatically reducing error rates and improving task completion.

通过你的评估，你可以更自信地测量提示工程的影响。即使对工具描述的小幅改进也能产生巨大的改进。在对工具描述进行精确改进后，Claude Sonnet 3.5 在 [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench) 评估中实现了最先进的性能，大幅降低了错误率并提高了任务完成度。

You can find other best practices for tool definitions in our [Developer Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use). If you're building tools for Claude, we also recommend reading about how tools are dynamically loaded into Claude's system prompt. Lastly, if you're writing tools for an MCP server, tool annotations help disclose which tools require open-world access or make destructive changes.

你可以在我们的[开发者指南](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)中找到工具定义的其他最佳实践。如果你正在为 Claude 构建工具，我们还建议阅读关于工具如何动态加载到 Claude 的系统提示中。最后，如果你正在为 MCP 服务器编写工具，工具注释有助于披露哪些工具需要开放世界访问或进行破坏性更改。

## Looking ahead | 展望未来

To build effective tools for agents, we need to re-orient our software development practices from predictable, deterministic patterns to non-deterministic ones.

要为智能体构建有效的工具，我们需要将软件开发实践从可预测的确定性模式重新定向到非确定性模式。

Through the iterative, evaluation-driven process we've described in this post, we've identified consistent patterns in what makes tools successful: Effective tools are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks.

通过本文中描述的迭代、评估驱动的过程，我们已经确定了使工具成功的持续模式：有效的工具是有意且清晰定义的，明智地使用智能体上下文，可以在各种工作流程中组合在一起，并使智能体能够直观地解决现实世界的任务。

In the future, we expect the specific mechanisms through which agents interact with the world to evolve—from updates to the MCP protocol to upgrades to the underlying LLMs themselves. With a systematic, evaluation-driven approach to improving tools for agents, we can ensure that as agents become more capable, the tools they use will evolve alongside them.

在未来，我们期望智能体与世界交互的具体机制会演进——从 MCP 协议的更新到底层 LLM 本身的升级。通过系统性的、评估驱动的方法来改进智能体的工具，我们可以确保随着智能体变得更有能力，它们使用的工具也会随之演进。

## Acknowledgements | 致谢

Written by Ken Aizawa with valuable contributions from colleagues across Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly Vorwerck), Design (Drew Roper), and Applied AI (Christian Ryan, Alexander Bricken).

由 Ken Aizawa 撰写，研究部门（Barry Zhang、Zachary Witten、Daniel Jiang、Sami Al-Sheikh、Matt Bell、Maggie Vo）、MCP（Theodora Chu、John Welsh、David Soria Parra、Adam Jones）、产品工程（Santiago Seira）、市场营销（Molly Vorwerck）、设计（Drew Roper）和应用 AI（Christian Ryan、Alexander Bricken）的同事提供了宝贵的贡献。

## Footnotes | 脚注

[1] Beyond training the underlying LLMs themselves.

[1] 除了训练底层 LLM 本身之外。
