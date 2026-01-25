# Equipping agents for the real world with Agent Skills | 使用 Agent Skills 为现实世界配备 AI 智能体

_Update: We've published_ _Agent Skills_ _as an open standard for cross-platform portability. (December 18, 2025)_

_更新：我们已将 Agent Skills 作为开放标准发布，以实现跨平台可移植性。（2025年12月18日）_

As model capabilities improve, we can now build general-purpose agents that interact with full-fledged computing environments. Claude Code, for example, can accomplish complex tasks across domains using local code execution and filesystems. But as these agents become more powerful, we need more composable, scalable, and portable ways to equip them with domain-specific expertise.

随着模型能力的提升，我们现在可以构建与完整计算环境交互的通用智能体。例如，Claude Code 可以使用本地代码执行和文件系统完成跨领域的复杂任务。但随着这些智能体变得更强大，我们需要更加可组合、可扩展和可移植的方式来为它们配备特定领域的专业知识。

This led us to create __Agent Skills__: organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks. Skills extend Claude's capabilities by packaging your expertise into composable resources for Claude, transforming general-purpose agents into specialized agents that fit your needs.

这促使我们创造了 **Agent Skills**：有组织的指令、脚本和资源文件夹，智能体可以发现并动态加载这些内容以在特定任务中表现得更好。技能通过将你的专业知识打包成 Claude 可组合使用的资源来扩展 Claude 的能力，将通用智能体转变为符合你需求的专业智能体。

Building a skill for an agent is like putting together an onboarding guide for a new hire. Instead of building fragmented, custom-designed agents for each use case, anyone can now specialize their agents with composable capabilities by capturing and sharing their procedural knowledge. In this article, we explain what Skills are, show how they work, and share best practices for building your own.

为智能体构建技能就像为新员工编写入职指南。无需为每个用例构建分散的、定制设计的智能体，现在任何人都可以通过捕获和共享他们的程序性知识来为智能体配备可组合的能力，使其专业化。在本文中，我们将解释什么是技能，展示它们如何工作，并分享构建自己技能的最佳实践。

![Image 1: To activate skills, all you need to do is write a SKILL.md file with custom guidance for your agent.](https://www-cdn.anthropic.com/images/4zrzovbb/website/ddd7e6e572ad0b6a943cacefe957248455f6d522-1650x929.jpg)
图片1说明：要激活技能，只需编写一个 SKILL.md 文件，为你的智能体提供自定义指导。

A skill is a directory containing a SKILL.md file that contains organized folders of instructions, scripts, and resources that give agents additional capabilities.

技能是一个包含 SKILL.md 文件的目录，其中包含有组织的指令、脚本和资源文件夹，为智能体提供额外的能力。

## The anatomy of a skill | 技能的解剖结构

To see Skills in action, let's walk through a real example: one of the skills that powers Claude's recently launched document editing abilities. Claude already knows a lot about understanding PDFs, but is limited in its ability to manipulate them directly (e.g. to fill out a form). This PDF skill lets us give Claude these new abilities.

为了了解技能的实际应用，让我们通过一个真实示例来讲解：驱动 Claude 最近推出的文档编辑功能的技能之一。Claude 已经对理解 PDF 有很多了解，但在直接操作 PDF（例如填写表单）方面能力有限。这个 PDF 技能让我们能够赋予 Claude 这些新能力。

At its simplest, a skill is a directory that contains a `SKILL.md file`. This file must start with YAML frontmatter that contains some required metadata: `name` and `description`. At startup, the agent pre-loads the `name` and `description` of every installed skill into its system prompt.

最简单的说，技能是一个包含 `SKILL.md 文件的目录`。该文件必须以 YAML frontmatter 开头，其中包含一些必需的元数据：`name` 和 `description`。在启动时，智能体会将每个已安装技能的 `name` 和 `description` 预加载到其系统提示中。

This metadata is the __first level__ of _progressive disclosure_: it provides just enough information for Claude to know when each skill should be used without loading all of it into context. The actual body of this file is the __second level__ of detail. If Claude thinks the skill is relevant to the current task, it will load the skill by reading its full `SKILL.md` into context.

这些元数据是 **渐进式披露** 的 **第一级**：它提供刚好足够的信息，让 Claude 知道何时应该使用每个技能，而无需将所有内容加载到上下文中。该文件的实际正文是 **第二级** 详细信息。如果 Claude 认为该技能与当前任务相关，它将通过读取完整的 `SKILL.md` 到上下文中来加载该技能。

![Image 2: Anatomy of a SKILL.md file including the relevant metadata: name, description, and context related to the specific actions the skill should take.](https://www-cdn.anthropic.com/images/4zrzovbb/website/6f22d8913dbc6228e7f11a41e0b3c124d817b6d2-1650x929.jpg)
图片2说明：SKILL.md 文件的解剖结构，包括相关元数据：名称、描述以及与技能应采取的特定操作相关的上下文。

A SKILL.md file must begin with YAML Frontmatter that contains a file name and description, which is loaded into its system prompt at startup.

SKILL.md 文件必须以 YAML Frontmatter 开头，其中包含文件名和描述，这些内容在启动时会被加载到系统提示中。

As skills grow in complexity, they may contain too much context to fit into a single `SKILL.md`, or context that's relevant only in specific scenarios. In these cases, skills can bundle additional files within the skill directory and reference them by name from `SKILL.md`. These additional linked files are the __third level__ (and beyond) of detail, which Claude can choose to navigate and discover only as needed.

随着技能变得越来越复杂，它们可能包含太多上下文，无法放入单个 `SKILL.md` 中，或者包含仅在特定场景中相关的上下文。在这些情况下，技能可以在技能目录中捆绑其他文件，并从 `SKILL.md` 中按名称引用它们。这些附加的链接文件是 **第三级**（及更高级）的详细信息，Claude 可以选择仅在需要时导航和发现这些内容。

In the PDF skill shown below, the `SKILL.md` refers to two additional files (`reference.md` and `forms.md`) that the skill author chooses to bundle alongside the core `SKILL.md`. By moving the form-filling instructions to a separate file (`forms.md`), the skill author is able to keep the core of the skill lean, trusting that Claude will read `forms.md` only when filling out a form.

在下面显示的 PDF 技能中，`SKILL.md` 引用了两个附加文件（`reference.md` 和 `forms.md`），技能作者选择将这些文件与核心 `SKILL.md` 一起捆绑。通过将表单填写说明移到单独的文件（`forms.md`）中，技能作者能够保持技能核心的精简，相信 Claude 只会在填写表单时才阅读 `forms.md`。

![Image 3: How to bundle additional content into a SKILL.md file.](https://www-cdn.anthropic.com/images/4zrzovbb/website/191bf5dd4b6f8cfe6f1ebafe6243dd1641ed231c-1650x1069.jpg)
图片3说明：如何将其他内容捆绑到 SKILL.md 文件中。

You can incorporate more context (via additional files) into your skill that can then be triggered by Claude based on the system prompt.

你可以在技能中整合更多上下文（通过附加文件），然后 Claude 可以根据系统提示触发这些内容。

Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable. Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed:

渐进式披露是使 Agent Skills 灵活和可扩展的核心设计原则。就像一本组织良好的手册，从目录开始，然后是特定章节，最后是详细的附录，技能让 Claude 仅在需要时加载信息：

![Image 4: This image depicts how progressive disclosure of context in Skills.](https://www-cdn.anthropic.com/images/4zrzovbb/website/a3bca2763d7892982a59c28aa4df7993aaae55ae-2292x673.jpg)
图片4说明：此图描绘了技能中上下文的渐进式披露。

Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded.

具有文件系统和代码执行工具的智能体在处理特定任务时不需要将整个技能读入其上下文窗口。这意味着可以捆绑到技能中的上下文量实际上是无限的。

### Skills and the context window | 技能与上下文窗口

The following diagram shows how the context window changes when a skill is triggered by a user's message.

下图显示了当技能被用户消息触发时，上下文窗口如何变化。

![Image 5: This image depicts how skills are triggered in your context window.](https://www-cdn.anthropic.com/images/4zrzovbb/website/441b9f6cc0d2337913c1f41b05357f16f51f702e-1650x929.jpg)
图片5说明：此图描绘了技能如何在上下文窗口中触发。

Skills are triggered in the context window via your system prompt.

技能通过系统提示在上下文窗口中触发。

The sequence of operations shown:

操作序列如下：

1. To start, the context window has the core system prompt and the metadata for each of the installed skills, along with the user's initial message;

首先，上下文窗口包含核心系统提示、每个已安装技能的元数据以及用户的初始消息；

2. Claude triggers the PDF skill by invoking a Bash tool to read the contents of `pdf/SKILL.md`;

Claude 通过调用 Bash 工具读取 `pdf/SKILL.md` 的内容来触发 PDF 技能；

3. Claude chooses to read the `forms.md` file bundled with the skill;

Claude 选择读取与技能捆绑的 `forms.md` 文件；

4. Finally, Claude proceeds with the user's task now that it has loaded relevant instructions from the PDF skill.

最后，Claude 继续处理用户的任务，因为它已经从 PDF 技能中加载了相关指令。

### Skills and code execution | 技能与代码执行

Skills can also include code for Claude to execute as tools at its discretion.

技能还可以包含 Claude 可以自行决定作为工具执行的代码。

Large language models excel at many tasks, but certain operations are better suited for traditional code execution. For example, sorting a list via token generation is far more expensive than simply running a sorting algorithm. Beyond efficiency concerns, many applications require the deterministic reliability that only code can provide.

大型语言模型在许多任务上表现出色，但某些操作更适合传统代码执行。例如，通过令牌生成排序列表比简单地运行排序算法要昂贵得多。除了效率问题外，许多应用程序需要只有代码才能提供的确定性可靠性。

In our example, the PDF skill includes a pre-written Python script that reads a PDF and extracts all form fields. Claude can run this script without loading either the script or the PDF into context. And because code is deterministic, this workflow is consistent and repeatable.

在我们的示例中，PDF 技能包含一个预先编写的 Python 脚本，该脚本读取 PDF 并提取所有表单字段。Claude 可以运行此脚本，而无需将脚本或 PDF 加载到上下文中。而且由于代码是确定性的，此工作流程是一致且可重复的。

![Image 6: This image depicts how code is executed via Skills.](https://www-cdn.anthropic.com/images/4zrzovbb/website/c24b4a2ff77277c430f2c9ef1541101766ae5714-1650x929.jpg)
图片6说明：此图描绘了如何通过技能执行代码。

Skills can also include code for Claude to execute as tools at its discretion based on the nature of the task.

技能还可以包含 Claude 根据任务性质自行决定作为工具执行的代码。

## Developing and evaluating skills | 开发和评估技能

Here are some helpful guidelines for getting started with authoring and testing skills:

以下是一些有助于开始编写和测试技能的指南：

- __Start with evaluation:__ Identify specific gaps in your agents' capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.

- **从评估开始**：通过在代表性任务上运行智能体并观察它们在哪些方面遇到困难或需要额外上下文，来识别智能体能力的具体差距。然后逐步构建技能来解决这些不足。

- __Structure for scale:__ When the `SKILL.md` file becomes unwieldy, split its content into separate files and reference them. If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage. Finally, code can serve as both executable tools and as documentation. It should be clear whether Claude should run scripts directly or read them into context as reference.

- **为扩展而构建**：当 `SKILL.md` 文件变得难以处理时，将其内容拆分为单独文件并引用它们。如果某些上下文互斥或很少一起使用，保持路径分离将减少令牌使用。最后，代码既可以作为可执行工具，也可以作为文档。应该清楚 Claude 是应该直接运行脚本还是将它们作为参考读入上下文。

- __Think from Claude's perspective:__ Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts. Pay special attention to the `name` and `description` of your skill. Claude will use these when deciding whether to trigger the skill in response to its current task.

- **从 Claude 的角度思考**：观察 Claude 在实际场景中如何使用你的技能，并根据观察结果进行迭代：注意意外的轨迹或对某些上下文的过度依赖。特别注意技能的 `name` 和 `description`。Claude 在决定是否响应当前任务而触发技能时会使用这些信息。

- __Iterate with Claude:__ As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong. This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront.

- **与 Claude 一起迭代**：当你与 Claude 一起完成任务时，让 Claude 将其成功的方法和常见错误捕获到技能中的可重用上下文和代码中。如果在使用技能完成任务时偏离了轨道，让它自我反思出了什么问题。这个过程将帮助你发现 Claude 实际需要什么上下文，而不是试图提前预测。

### Security considerations when using Skills | 使用技能时的安全考虑

Skills provide Claude with new capabilities through instructions and code. While this makes them powerful, it also means that malicious skills may introduce vulnerabilities in the environment where they're used or direct Claude to exfiltrate data and take unintended actions.

技能通过指令和代码为 Claude 提供新能力。虽然这使它们变得强大，但也意味着恶意技能可能会在它们所使用的环境中引入漏洞，或者指示 Claude 渗漏数据并采取意外操作。

We recommend installing skills only from trusted sources. When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

我们建议仅从受信任的来源安装技能。当来自不太受信任的来源安装技能时，请在使用前彻底审计它。首先阅读技能中捆绑的文件内容以了解其功能，特别注意代码依赖项和捆绑的资源（如图像或脚本）。同样，请注意技能中指示 Claude 连接到潜在不受信任的外部网络源的指令或代码。

## The future of Skills | 技能的未来

Agent Skills are supported today across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform.

Agent Skills 目前在 Claude.ai、Claude Code、Claude Agent SDK 和 Claude Developer Platform 上得到支持。

In the coming weeks, we'll continue to add features that support the full lifecycle of creating, editing, discovering, sharing, and using Skills. We're especially excited about the opportunity for Skills to help organizations and individuals share their context and workflows with Claude. We'll also explore how Skills can complement Model Context Protocol (MCP) servers by teaching agents more complex workflows that involve external tools and software.

在接下来的几周里，我们将继续添加支持创建、编辑、发现、共享和使用技能的完整生命周期的功能。我们对技能帮助组织和个人与 Claude 共享其上下文和工作流程的机会特别兴奋。我们还将探索技能如何通过向智能体教授涉及外部工具和软件的更复杂工作流程来补充模型上下文协议（MCP）服务器。

Looking further ahead, we hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities.

展望更远的未来，我们希望启用智能体自行创建、编辑和评估技能，让它们将自己的行为模式编码为可重用的能力。

Skills are a simple concept with a correspondingly simple format. This simplicity makes it easier for organizations, developers, and end users to build customized agents and give them new capabilities.

技能是一个简单的概念，具有相应的简单格式。这种简单性使组织、开发者和最终用户更容易构建定制化的智能体并赋予它们新能力。

We're excited to see what people build with Skills. Get started today by checking out our [Skills documentation](https://docs.anthropic.com/en/docs/build-with-claude/agent-skills) and [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/agent-skills/cookbook).

我们很兴奋地看到人们用技能构建什么。今天就查看我们的 [技能文档](https://docs.anthropic.com/en/docs/build-with-claude/agent-skills)和 [cookbook](https://docs.anthropic.com/en/docs/build-with-claude/agent-skills/cookbook)开始吧。

## Acknowledgements | 致谢

Written by Barry Zhang, Keith Lazuka, and Mahesh Murag, who all really like folders. Special thanks to the many others across Anthropic who championed, supported, and built Skills.

本文由 Barry Zhang、Keith Lazuka 和 Mahesh Murag 撰写，他们都非常喜欢文件夹。特别感谢 Anthropic 的许多其他人，他们倡导、支持和构建了技能。
