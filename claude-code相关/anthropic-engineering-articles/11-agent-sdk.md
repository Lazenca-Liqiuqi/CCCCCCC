# Building agents with the Claude Agent SDK | 使用 Claude Agent SDK 构建 AI 智能体

Last year, we shared lessons in building effective agents alongside our customers. Since then, we've released Claude Code, an agentic coding solution that we originally built to support developer productivity at Anthropic.

去年，我们与客户分享了构建有效智能体的经验教训。自那时以来，我们发布了 Claude Code，这是一个我们最初为支持 Anthropic 的开发者生产力而构建的智能体编码解决方案。

Over the past several months, Claude Code has become far more than a coding tool. At Anthropic, we've been using it for deep research, video creation, and note-taking, among countless other non-coding applications. In fact, it has begun to power almost all of our major agent loops.

在过去的几个月里，Claude Code 已经远不止是一个编码工具。在 Anthropic，我们一直在使用它进行深度研究、视频制作和笔记记录，以及无数其他非编码应用。事实上，它已经开始为我们几乎所有的主流智能体循环提供支持。

In other words, the agent harness that powers Claude Code (the Claude Code SDK) can power many other types of agents, too. To reflect this broader vision, we're renaming the Claude Code SDK to the Claude Agent SDK.

换句话说，驱动 Claude Code 的智能体框架（Claude Code SDK）也可以为许多其他类型的智能体提供支持。为了反映这一更广阔的愿景，我们将 Claude Code SDK 重命名为 Claude Agent SDK。

In this post, we'll highlight why we built the Claude Agent SDK, how to build your own agents with it, and share the best practices that have emerged from our team's own deployments.

在本文中，我们将重点介绍为什么要构建 Claude Agent SDK、如何使用它构建你自己的智能体，并分享我们团队在部署中涌现出的最佳实践。

## Giving Claude a computer | 为 Claude 配备计算机

The key design principle behind Claude Code is that Claude needs the same tools that programmers use every day. It needs to be able to find appropriate files in a codebase, write and edit files, lint the code, run it, debug, edit, and sometimes take these actions iteratively until the code succeeds.

Claude Code 背后的关键设计原则是，Claude 需要程序员每天使用的相同工具。它需要能够在代码库中找到合适的文件，编写和编辑文件，对代码进行语法检查，运行代码，调试，编辑，有时需要迭代地执行这些操作直到代码成功运行。

We found that by giving Claude access to the user's computer (via the terminal), it had what it needed to write code like programmers do.

我们发现，通过让 Claude 访问用户的计算机（通过终端），它拥有了像程序员一样编写代码所需的一切。

But this has also made Claude in Claude Code effective at _non_-coding tasks. By giving it tools to run bash commands, edit files, create files and search files, Claude can read CSV files, search the web, build visualizations, interpret metrics, and do all sorts of other digital work – in short, create general-purpose agents with a computer. The key design principle behind the Claude Agent SDK is to give your agents a computer, allowing them to work like humans do.

但这也让 Claude Code 中的 Claude 在非编码任务中表现出色。通过赋予它运行 bash 命令、编辑文件、创建文件和搜索文件的工具，Claude 可以读取 CSV 文件，搜索网络，构建可视化，解释指标，并执行各种其他数字工作——简而言之，创建配备计算机的通用智能体。Claude Agent SDK 背后的关键设计原则是为你的智能体配备一台计算机，让它们像人类一样工作。

## Creating new types of agents | 创建新型智能体

We believe giving Claude a computer unlocks the ability to build agents that are more effective than before. For example, with our SDK, developers can build:

我们相信，为 Claude 配备计算机解锁了构建比以往更有效的智能体的能力。例如，使用我们的 SDK，开发者可以构建：

- **Finance agents**: Build agents that can understand your portfolio and goals, as well as help you evaluate investments by accessing external APIs, storing data and running code to make calculations.

- **金融智能体**：构建能够理解你的投资组合和目标的智能体，以及通过访问外部 API、存储数据和运行代码进行计算来帮助你评估投资。

- **Personal assistant agents**. Build agents that can help you book travel and manage your calendar, as well as schedule appointments, put together briefs, and more by connecting to your internal data sources and tracking context across applications.

- **个人助理智能体**：构建可以帮助你预订旅行和管理日历，以及通过连接到你的内部数据源和跨应用程序跟踪上下文来安排约会、整理简报等的智能体。

- **Customer support agents:** Build agents that can handle high ambiguity user requests, like customer service tickets, by collecting and reviewing user data, connecting to external APIs, messaging users back and escalating to humans when needed.

- **客户支持智能体**：构建可以处理高模糊性用户请求（如客户服务工单）的智能体，通过收集和审查用户数据，连接到外部 API，回复用户消息，并在需要时升级给人工处理。

- **Deep research agents**: Build agents that can conduct comprehensive research across large document collections by searching through file systems, analyzing and synthesizing information from multiple sources, cross-referencing data across files, and generating detailed reports.

- **深度研究智能体**：构建可以通过搜索文件系统、分析和综合来自多个来源的信息、交叉引用文件之间的数据以及生成详细报告，从而对大型文档集合进行综合研究的智能体。

And much more. At its core, the SDK gives you the primitives to build agents for whatever workflow you're trying to automate.

以及更多。从根本上说，SDK 为你提供了原语，可用于为你试图自动化的任何工作流构建智能体。

## Building your agent loop | 构建你的智能体循环

In Claude Code, Claude often operates in a specific feedback loop: gather context -> take action -> verify work -> repeat.

在 Claude Code 中，Claude 通常在一个特定的反馈循环中操作：收集上下文 → 采取行动 → 验证工作 → 重复。

![Image 1: Agent feedback loop](https://www-cdn.anthropic.com/images/4zrzovbb/website/952fb04cb836d6de9662c8450c6a47dfe58bbd9f-2292x1290.png)
图片1说明：智能体反馈循环。

Agents often operate in a specific feedback loop: gather context -> take action -> verify work -> repeat.

智能体通常在一个特定的反馈循环中操作：收集上下文 → 采取行动 → 验证工作 → 重复。

This offers a useful way to think about other agents, and the capabilities they should be given. To illustrate this, we'll walk through the example of how we might build an email agent in the Claude Agent SDK.

这为思考其他智能体以及它们应该被赋予的能力提供了一种有用的方式。为了说明这一点，我们将演练如何在 Claude Agent SDK 中构建电子邮件智能体的示例。

## Gather context | 收集上下文

When developing an agent, you want to give it more than just a prompt: it needs to be able to fetch and update its own context. Here's how features in the SDK can help.

在开发智能体时，你想给它的不仅仅是一个提示：它需要能够获取和更新自己的上下文。以下是 SDK 中的功能如何提供帮助。

### **Agentic search and the file system** | **智能体搜索和文件系统**

The file system represents information that _could_ be pulled into the model's context.

文件系统代表了可以被拉入模型上下文的信息。

When Claude encounters large files, like logs or user-uploaded files, it will decide which way to load these into its context by using bash scripts like `grep` and `tail`. In essence, the folder and file structure of an agent becomes a form of context engineering.

当 Claude 遇到大文件（如日志或用户上传的文件）时，它将通过使用 `grep` 和 `tail` 等 bash 脚本来决定将这些文件加载到其上下文中的方式。本质上，智能体的文件夹和文件结构成为了一种上下文工程的形式。

Our email agent might store previous conversations in a folder called 'Conversations'. This would allow it to search these for context when asked about them.

我们的电子邮件智能体可能会将以前的对话存储在一个名为 "Conversations" 的文件夹中。这将允许它在被询问时搜索这些对话以获取其上下文。

![Image 2: File system as context for an email agent](https://www-cdn.anthropic.com/images/4zrzovbb/website/d5e3b46900277431b86467fdc308b64e61edd740-2292x623.png)
图片2说明：电子邮件智能体的文件系统作为上下文。

### **Semantic search** | **语义搜索**

Semantic search is usually faster than agentic search, but less accurate, more difficult to maintain, and less transparent. It involves 'chunking' the relevant context, embedding these chunks as vectors, and then searching for concepts by querying those vectors. Given its limitations, we suggest starting with agentic search, and only adding semantic search if you need faster results or more variations.

语义搜索通常比智能体搜索更快，但准确性较低，更难维护，透明度也较低。它涉及将相关上下文"分块"，将这些块嵌入为向量，然后通过查询这些向量来搜索概念。鉴于其局限性，我们建议从智能体搜索开始，仅在需要更快的结果或更多变化时才添加语义搜索。

### **Subagents** | **子智能体**

Claude Agent SDK supports subagents by default. Subagents are useful for two main reasons. First, they enable parallelization: you can spin up multiple subagents to work on different tasks simultaneously. Second, they help manage context: subagents use their own isolated context windows, and only send relevant information back to the orchestrator, rather than their full context. This makes them ideal for tasks that require sifting through large amounts of information where most of it won't be useful.

Claude Agent SDK 默认支持子智能体。子智能体主要有两个有用的原因。首先，它们实现并行化：你可以启动多个子智能体同时处理不同的任务。其次，它们帮助管理上下文：子智能体使用自己独立的上下文窗口，只将相关信息发送给编排器，而不是它们的完整上下文。这使它们成为需要筛选大量信息（其中大部分不会有用）的任务的理想选择。

When designing our email agent, we might give it a 'search subagent' capability. The email agent could then spin off multiple search subagents in parallel—each running different queries against your email history—and have them return only the relevant excerpts rather than full email threads.

在设计我们的电子邮件智能体时，我们可能会给它一个"搜索子智能体"功能。然后，电子邮件智能体可以并行启动多个搜索子智能体——每个对电子邮件历史运行不同的查询——并让它们只返回相关摘录而不是完整的电子邮件线程。

### **Compaction** | **压缩**

When agents are running for long periods of time, context maintenance becomes critical. The Claude Agent SDK's compact feature automatically summarizes previous messages when the context limit approaches, so your agent won't run out of context. This is built on Claude Code's compact slash command.

当智能体运行长时间时，上下文维护变得至关重要。Claude Agent SDK 的压缩功能会在上下文限制接近时自动汇总先前的消息，因此你的智能体不会用完上下文。这是基于 Claude Code 的 compact 斜杠命令构建的。

## Take action | 采取行动

Once you've gathered context, you'll want to give your agent flexible ways of taking action.

一旦你收集了上下文，你会想给你的智能体灵活的采取行动的方式。

### **Tools** | **工具**

Tools are the primary building blocks of execution for your agent. Tools are prominent in Claude's context window, making them the primary actions Claude will consider when deciding how to complete a task. This means you should be conscious about how you design your tools to maximize context efficiency. You can see more best practices in our blog post, [Writing effective tools for agents – with agents](https://www.anthropic.com/engineering/writing-effective-tools).

工具是智能体执行的主要构建块。工具在 Claude 的上下文中很突出，使它们成为 Claude 在决定如何完成任务时考虑的主要行动。这意味着你应该有意识地设计工具以最大化上下文效率。你可以在我们的博客文章中看到更多最佳实践，为智能体编写有效的工具——使用智能体。

As such, your tools should be primary actions you want your agent to take. [Learn how to make custom tools](https://docs.anthropic.com/en/docs/build-with-claude/agent-sdk) in the Claude Agent SDK.

因此，你的工具应该是你希望智能体采取的主要行动。了解如何在 Claude Agent SDK 中制作自定义工具。

For our email agent, we might define tools like "`fetchInbox`" or "`searchEmails`" as the agent's primary, most frequent actions.

对于我们的电子邮件智能体，我们可能会将诸如 "`fetchInbox`" 或 "`searchEmails`" 之类的工具定义为智能体的主要、最频繁的行动。

### **Bash & scripts** | **Bash 和脚本**

Bash is useful as a general-purpose tool to allow the agent to do flexible work using a computer.

Bash 作为一种通用工具很有用，允许智能体使用计算机进行灵活的工作。

In our email agent, the user might have important information stored in their attachments. Claude could write code to download the PDF, convert it to text, and search across it to find useful information by calling, as depicted below:

在我们的电子邮件智能体中，用户可能在其附件中存储了重要信息。Claude 可以编写代码来下载 PDF，将其转换为文本，并搜索其中以查找有用信息，通过调用，如下所示：

![Image 3: Claude using bash to process email attachments](https://www-cdn.anthropic.com/images/4zrzovbb/website/e2a32595e35164f46c054dc003197e622ca95180-2292x623.png)
图片3说明：Claude 使用 bash 处理电子邮件附件。

### **Code generation** | **代码生成**

The Claude Agent SDK excels at code generation—and for good reason. Code is precise, composable, and infinitely reusable, making it an ideal output for agents that need to perform complex operations reliably.

Claude Agent SDK 擅长代码生成——这是有充分理由的。代码是精确的、可组合的、无限可重用的，使其成为需要可靠执行复杂操作的智能体的理想输出。

When building agents, consider: which tasks would benefit from being expressed as code? Often, the answer unlocks significant capabilities.

在构建智能体时，请考虑：哪些任务将受益于被表达为代码？通常，答案会解锁重要的能力。

For example, our recent launch of file creation in Claude.AI relies entirely on code generation. Claude writes Python scripts to create Excel spreadsheets, PowerPoint presentations, and Word documents, ensuring consistent formatting and complex functionality that would be difficult to achieve any other way.

例如，我们最近在 Claude.AI 中推出的文件创建功能完全依赖于代码生成。Claude 编写 Python 脚本来创建 Excel 电子表格、PowerPoint 演示文稿和 Word 文档，确保一致的格式和复杂的功能，这很难通过其他方式实现。

In our email agent, we might want to allow users to create rules for inbound emails. To achieve this, we could write code to run on that event:

在我们的电子邮件智能体中，我们可能希望允许用户为入站电子邮件创建规则。为了实现这一点，我们可以编写在该事件上运行的代码：

![Image 4: Code generation for email rules](https://www-cdn.anthropic.com/images/4zrzovbb/website/180c83cc0f6f0ea26e18cbfbc59040cab6767b55-2292x1290.png)
图片4说明：用于电子邮件规则的代码生成。

### **MCPs** | **MCP 协议**

The Model Context Protocol (MCP) provides standardized integrations to external services, handling authentication and API calls automatically. This means you can connect your agent to tools like Slack, GitHub, Google Drive, or Asana without writing custom integration code or managing OAuth flows yourself.

模型上下文协议（MCP）提供到外部服务的标准化集成，自动处理身份验证和 API 调用。这意味着你可以将智能体连接到 Slack、GitHub、Google Drive 或 Asana 等工具，而无需编写自定义集成代码或自己管理 OAuth 流程。

For our email agent, we might want to `search Slack messages` to understand team context, or `check Asana tasks` to see if someone has already been assigned to handle a customer request. With MCP servers, these integrations work out of the box—your agent can simply call tools like search_slack_messages or get_asana_tasks and the MCP handles the rest.

对于我们的电子邮件智能体，我们可能想要 `搜索 Slack 消息` 以了解团队上下文，或 `检查 Asana 任务` 以查看是否已经有人被指派处理客户请求。使用 MCP 服务器，这些集成开箱即用——你的智能体只需调用 search_slack_messages 或 get_asana_tasks 等工具，MCP 处理其余的工作。

The growing MCP ecosystem means you can quickly add new capabilities to your agents as pre-built integrations become available, letting you focus on agent behavior.

不断增长的 MCP 生态系统意味着你可以随着预构建集成的可用性快速为智能体添加新功能，让你专注于智能体行为。

## Verify your work | 验证你的工作

The Claude Code SDK finishes the agentic loop by evaluating its work. Agents that can check and improve their own output are fundamentally more reliable—they catch mistakes before they compound, self-correct when they drift, and get better as they iterate.

Claude Code SDK 通过评估其工作来完成智能体循环。能够检查和改进自己的输出的智能体从根本上更可靠——它们在错误复合之前捕获错误，在偏离时自我纠正，并在迭代时变得更好。

The key is giving Claude concrete ways to evaluate its work. Here are three approaches we've found effective:

关键是给 Claude 具体的方式来评估其工作。以下是我们发现有效的三种方法：

### **Defining rules** | **定义规则**

The best form of feedback is providing clearly defined rules for an output, then explaining which rules failed and why.

最好的反馈形式是为输出提供明确定义的规则，然后解释哪些规则失败了以及为什么失败。

Code linting is an excellent form of rules-based feedback. The more in-depth the feedback, the better. For instance, it is usually better to generate TypeScript and lint it than it is to generate pure JavaScript because it provides you with multiple additional layers of feedback.

代码语法检查是一种基于规则的反馈的优秀形式。反馈越深入越好。例如，生成 TypeScript 并对其进行语法检查通常比生成纯 JavaScript 更好，因为它为你提供了多层额外的反馈。

When generating an email, you may want Claude to check that the email address is valid (if not, throw an error) and that the user has sent an email to them before (if so, throw a warning).

在生成电子邮件时，你可能希望 Claude 检查电子邮件地址是否有效（如果无效，则抛出错误），以及用户以前是否向他们发送过电子邮件（如果是，则发出警告）。

### **Visual feedback** | **视觉反馈**

When using an agent to complete visual tasks, like UI generation or testing, visual feedback (in the form of screenshots or renders) can be helpful. For example, if sending an email with HTML formatting, you could screenshot the generated email and provide it back to the model for visual verification and iterative refinement. The model would then check whether the visual output matches what was requested.

当使用智能体完成视觉任务（如 UI 生成或测试）时，视觉反馈（以屏幕截图或渲染的形式）可能会有所帮助。例如，如果发送带有 HTML 格式的电子邮件，你可以截取生成的电子邮件的屏幕截图，并将其提供给模型以进行视觉验证和迭代优化。然后，模型将检查视觉输出是否与所要求的内容匹配。

For instance:

例如：

- **Layout** - Are elements positioned correctly? Is spacing appropriate?

- **布局** - 元素是否正确定位？间距是否合适？

- **Styling** - Do colors, fonts, and formatting appear as intended?

- **样式** - 颜色、字体和格式是否按预期显示？

- **Content hierarchy** - Is information presented in the right order with proper emphasis?

- **内容层次结构** - 信息是否按正确的顺序呈现，并具有适当的强调？

- **Responsiveness** - Does it look broken or cramped? (though a single screenshot has limited viewport info)

- **响应性** - 它看起来是否破损或拥挤？（尽管单个屏幕截图的视口信息有限）

Using an MCP server like Playwright, you can automate this visual feedback loop—taking screenshots of rendered HTML, capturing different viewport sizes, and even testing interactive elements—all within your agent's workflow.

使用像 Playwright 这样的 MCP 服务器，你可以自动执行这个视觉反馈循环——截取渲染的 HTML 的屏幕截图，捕获不同的视口大小，甚至测试交互元素——所有这些都在你的智能体的工作流程中。

![Image 5: Visual feedback for email body generation](https://www-cdn.anthropic.com/images/4zrzovbb/website/5ea7f3d8652778dc5e2db0cc33a846db5f1a5fb8-2292x2293.png)
图片5说明：Claude 为智能体生成的电子邮件正文提供视觉反馈。

Visual feedback from a large-language model (LLM) can provide helpful guidance to your agent.

来自大型语言模型（LLM）的视觉反馈可以为你的智能体提供有用的指导。

### **LLM as a judge** | **LLM 作为评判者**

You can also have another language model "judge" the output of your agent based on fuzzy rules. This is generally not a very robust method, and can have heavy latency tradeoffs, but for applications where any boost in performance is worth the cost, it can be helpful.

你也可以让另一个语言模型根据模糊规则"评判"你的智能体的输出。这通常不是很稳健的方法，并且可能有很重的延迟权衡，但对于任何性能提升都值得成本的应用程序，它可能会有所帮助。

Our email agent might have a separate subagent judge the tone of its drafts, to see if they fit well with the user's previous messages.

我们的电子邮件智能体可能有一个单独的子智能体来判断其草稿的语气，以查看它们是否与用户以前的消息很好地匹配。

## Testing and improving your agent | 测试和改进你的智能体

After you've gone through the agent loop a few times, we recommend testing your agent, and ensuring that it's well-equipped for its tasks. The best way to improve an agent is to look carefully at its output, especially the cases where it fails, and to put yourself in its shoes: does it have the right tools for the job?

在你完成了智能体循环几次之后，我们建议你测试你的智能体，并确保它为其任务装备齐全。改进智能体的最佳方法是仔细观察其输出，特别是它失败的情况，并设身处地：它是否有正确的工具来完成工作？

Here are some other questions to ask as you're evaluating whether or not your agent is well-equipped to do its job:

在评估你的智能体是否装备齐全以完成其工作时，还有以下一些问题要问：

- If your agent misunderstands the task, it might be missing key information. Can you alter the structure of your search APIs to make it easier to find what it needs to know?

- 如果你的智能体误解了任务，它可能缺少关键信息。你可以更改搜索 API 的结构以使其更容易找到它需要知道的内容吗？

- If your agent fails at a task repeatedly, can you add a formal rule in your tool calls to identify and fix the failure?

- 如果你的智能体在某个任务上反复失败，你可以在工具调用中添加正式规则来识别和修复失败吗？

- If your agent can't fix its errors, can you give it more useful or creative tools to approach the problem differently?

- 如果你的智能体无法修复其错误，你可以给它更有用或更有创意的工具来以不同的方式处理问题吗？

- If your agent's performance varies as you add features, build a representative test set for programmatic evaluations (or evals) based on customer usage.

- 如果你添加功能时智能体的性能发生变化，请根据客户使用情况构建代表性测试集以进行程序化评估（或 evals）。

## Getting started | 入门指南

The Claude Agent SDK makes it easier to build autonomous agents by giving Claude access to a computer where it can write files, run commands, and iterate on its work.

Claude Agent SDK 通过让 Claude 访问可以写入文件、运行命令和迭代其工作的计算机，使构建自主智能体变得更容易。

With the agent loop in mind (gathering context, taking action, and your verifying work), you can build reliable agents that are easy to deploy and iterate on.

牢记智能体循环（收集上下文、采取行动和验证工作），你可以构建易于部署和迭代的可靠智能体。

You can get started with the Claude Agent SDK today. For developers who are already building on the SDK, we recommend migrating to the latest version by following this [guide](https://docs.anthropic.com/en/docs/build-with-claude/agent-sdk).

你今天就可以开始使用 Claude Agent SDK。对于已经在 SDK 上构建的开发者，我们建议通过遵循此[指南](https://docs.anthropic.com/en/docs/build-with-claude/agent-sdk)迁移到最新版本。

## Acknowledgements | 致谢

Written by Thariq Shihipar with notes and editing from Molly Vorwerck, Suzanne Wang, Alex Isken, Cat Wu, Keir Bradwell, Alexander Bricken & Ashwin Bhat.

本文由 Thariq Shihipar 撰写，Molly Vorwerck、Suzanne Wang、Alex Isken、Cat Wu、Keir Bradwell、Alexander Bricken 和 Ashwin Bhat 提供注释和编辑。
