# Effective Harnesses for Long-Running Agents
长时间运行智能体的有效工具

As AI agents become more capable, developers are increasingly asking them to take on complex tasks requiring work that spans hours, or even days. However, getting agents to make consistent progress across multiple context windows remains an open problem.
随着 AI 智能体变得更强大，开发人员越来越要求它们承担需要数小时甚至数天才能完成的复杂任务。然而，让智能体在多个上下文窗口中取得一致进展仍然是一个未解决的问题。

The core challenge of long-running agents is that they must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift. Because context windows are limited, and because most complex projects cannot be completed within a single window, agents need a way to bridge the gap between coding sessions.
长时间运行智能体的核心挑战是它们必须在离散的会话中工作，每个新会话开始时都没有之前发生的事情的记忆。想象一个由轮班工程师组成的软件项目，每个新工程师到来时都没有记忆之前轮班发生了什么。由于上下文窗口有限，而且大多数复杂项目无法在单个窗口内完成，智能体需要一种方法来弥合编码会话之间的差距。

We developed a two-fold solution to enable the Claude Agent SDK to work effectively across many context windows: an __initializer agent__ that sets up the environment on the first run, and a __coding agent__ that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session. You can find code examples in the accompanying quickstart.
我们开发了一个双重解决方案，使 Claude Agent SDK 能够在许多上下文窗口中有效工作：一个在第一次运行时设置环境的 __初始化智能体__，和一个在每个会话中负责取得增量进展同时为下一个会话留下清晰工件的 __编码智能体__。你可以在附带的快速入门中找到代码示例。

## The Long-Running Agent Problem
长时间运行智能体的问题

The Claude Agent SDK is a powerful, general-purpose agent harness adept at coding, as well as other tasks that require the model to use tools to gather上下文、plan, and execute. It has context management capabilities such as compaction, which enables an agent to work on a task without exhausting the context window. Theoretically, given this setup, it should be possible for an agent to continue to do useful work for an arbitrarily long time.
Claude Agent SDK 是一个强大的、通用的智能体工具，擅长编码以及其他需要模型使用工具来收集上下文、计划和执行的任务。它具有上下文管理功能（如压缩），使智能体能够处理任务而不会耗尽上下文窗口。理论上，鉴于这种设置，智能体应该可以继续进行有用的工作任意长的时间。

However, compaction isn't sufficient. Out of the box, even a frontier coding model like Opus 4.5 running on the Claude Agent SDK in a loop across multiple context windows will fall short of building a production-quality web app if it's only given a high-level prompt, such as "build a clone of claude.ai."
然而，压缩是不够的。开箱即用，即使是一个前沿的编码模型（如 Opus 4.5）在 Claude Agent SDK 上跨多个上下文窗口循环运行，如果只给它一个高级提示（如"构建 claude.ai 的克隆"），也无法构建生产质量的 Web 应用程序。

Claude's failures manifested in two patterns. First, the agent tended to try to do too much at once—essentially to attempt to one-shot the app. Often, this led to the model running out of context in the middle of its implementation, leaving the next session to start with a feature half-implemented and undocumented. The agent would then have to guess at what had happened, and spend substantial time trying to get the basic app working again. This happens even with compaction, which doesn't always pass perfectly clear instructions to the next agent.
Claude 的失败表现为两种模式。首先，智能体倾向于一次做太多事情——本质上是一次性尝试完成应用程序。通常，这会导致模型在实现过程中用尽上下文，留下下一个会话从一个功能一半实现且无文档记录的状态开始。然后智能体必须猜测发生了什么，并花费大量时间试图使基本应用程序再次工作。即使使用压缩也会发生这种情况，压缩并不总是向下一个智能体传递完美清晰的指令。

A second failure mode would often occur later in a project. After some features had already been built, a later agent instance would look around, see that progress had been made, and declare the job done.
第二种失败模式通常会在项目的后期发生。在已经构建了一些功能后，后来的智能体实例会环顾四周，看到已经取得了进展，并宣布工作完成。

This decomposes the problem into two parts. First, we need to set up an initial environment that lays the foundation for _all_ the features that a given prompt requires, which sets up the agent to work step-by-step and feature-by-feature. Second, we should prompt each agent to make incremental progress towards its goal while also leaving the environment in a clean state at the end of a session. By "clean state" we mean the kind of code that would be appropriate for merging to a main branch: there are no major bugs, the code is orderly and well-documented, and in general, a developer could easily begin work on a new feature without first having to clean up an unrelated mess.
这将问题分解为两个部分。首先，我们需要设置一个初始环境，为给定提示所需的所有功能奠定基础，这将智能体设置为逐步、逐功能地工作。其次，我们应该提示每个智能体在朝着其目标取得增量进展的同时，在会话结束时将环境保持在干净状态。通过"干净状态"，我们指的是适合合并到主分支的代码：没有重大错误，代码有序且有良好的文档，总体而言，开发人员可以轻松开始新功能的工作，而无需先清理无关的混乱。

When experimenting internally, we addressed these problems using a two-part solution:
在内部实验时，我们使用两部分解决方案解决了这些问题：

1. Initializer agent: The very first agent session uses a specialized prompt that asks the model to set up the initial environment: an `init.sh` script, a claude-progress.txt file that keeps a log of what agents have done, and an initial git commit that shows what files were added.
1. 初始化智能体：第一个智能体会话使用一个专门的提示，要求模型设置初始环境：一个 `init.sh` 脚本、一个记录智能体所做事情的 claude-progress.txt 文件，以及一个显示添加了哪些文件的初始 git 提交。

2. Coding agent: Every subsequent session asks the model to make incremental progress, then leave structured updates.
2. 编码智能体：每个后续会话要求模型取得增量进展，然后留下结构化更新。

The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window, which is accomplished with the claude-progress.txt file alongside the git history. Inspiration for these practices came from knowing what effective software engineers do every day.
这里的关键洞察是找到一种方法，让智能体在从新的上下文窗口开始时快速理解工作状态，这是通过 claude-progress.txt 文件与 git 历史一起完成的。这些实践的灵感来自于了解有效的软件工程师每天所做的事情。

## Environment Management
环境管理

In the updated Claude 4 prompting guide, we shared some best practices for multi-context window workflows, including a harness structure that uses "a different prompt for the very first context window." This "different prompt" requests that the initializer agent set up the environment with all the necessary context that future coding agents will need to work effectively. Here, we provide a deeper dive on some of the key components of such an environment.
在更新的 Claude 4 提示指南中，我们分享了一些多上下文窗口工作流程的最佳实践，包括使用"第一个上下文窗口使用不同的提示"的工具结构。这个"不同的提示"要求初始化智能体设置环境，其中包含未来的编码智能体有效工作所需的所有必要上下文。在这里，我们将深入探讨这种环境的一些关键组件。

### Feature List
功能列表

To address the problem of the agent one-shotting an app or prematurely considering the project complete, we prompted the initializer agent to write a comprehensive file of feature requirements expanding on the user's initial prompt. In the claude.ai clone example, this meant over 200 features, such as "a user can open a new chat, type in a query, press enter, and see an AI response." These features were all initially marked as "failing" so that later coding agents would have a clear outline of what full functionality looked like.
为了解决智能体一次性完成应用程序或过早认为项目完成的问题，我们提示初始化智能体编写一个全面的功能需求文件，扩展用户的初始提示。在 claude.ai 克隆示例中，这意味着超过 200 个功能，例如"用户可以打开新聊天、输入查询、按回车键并查看 AI 响应"。这些功能最初都被标记为"失败"，以便后来的编码智能体能够清楚地了解完整功能的样子。

```
{
    "category": "functional",
    "description": "New chat button creates a fresh conversation",
    "steps": [
      "Navigate to main interface",
      "Click the 'New Chat' button",
      "Verify a new conversation is created",
      "Check that chat area shows welcome state",
      "Verify conversation appears in sidebar"
    ],
    "passes": false
  }
```

We prompt coding agents to edit this file only by changing the status of a passes field, and we use strongly-worded instructions like "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality." After some experimentation, we landed on using JSON for this, as the model is less likely to inappropriately change or overwrite JSON files compared to Markdown files.
我们提示编码智能体只能通过更改 passes 字段的状态来编辑此文件，并且我们使用措辞强硬的指令，如"删除或编辑测试是不可接受的，因为这可能导致功能缺失或错误。"经过一些实验，我们决定使用 JSON，因为与 Markdown 文件相比，模型不太可能不当更改或覆盖 JSON 文件。

### Incremental Progress
增量进展

Given this initial environment scaffolding, the next iteration of the coding agent was then asked to work on only one feature at a time. This incremental approach turned out to be critical to addressing the agent's tendency to do too much at once.
鉴于这种初始环境脚手架，下一轮编码智能体被要求一次只处理一个功能。这种增量方法被证明是解决智能体一次做太多事情倾向的关键。

Once working incrementally, it's still essential that the model leaves the environment in a clean state after making a code change. In our experiments, we found that the best way to elicit this behavior was to ask the model to commit its progress to git with descriptive commit messages and to write summaries of its progress in a progress file. This allowed the model to use git to revert bad code changes and recover working states of the code base.
一旦增量工作，模型在进行代码更改后仍必须将环境保持在干净状态。在我们的实验中，我们发现引发这种行为的最佳方法是要求模型将其进展提交到 git，并带有描述性的提交消息，并在进度文件中编写其进展摘要。这允许模型使用 git 恢复错误的代码更改并恢复代码库的工作状态。

These approaches also increased efficiency, as they eliminated the need for an agent to have to guess at what had happened and spend its time trying to get the basic app working again.
这些方法还提高了效率，因为它们消除了智能体猜测发生了什么并花费时间试图使基本应用程序再次工作的需要。

### Testing
测试

One final major failure mode that we observed was Claude's tendency to mark a feature as complete without proper testing. Absent explicit prompting, Claude tended to make code changes, and even do testing with unit tests or `curl` commands against a development server, but would fail recognize that the feature didn't work end-to-end.
我们观察到的最后一个主要失败模式是 Claude 倾向于在没有适当测试的情况下将功能标记为完成。如果没有明确的提示，Claude 倾向于进行代码更改，甚至对开发服务器进行单元测试或 `curl` 命令测试，但无法认识到功能端到端不起作用。

In the case of building a web app, Claude mostly did well at verifying features end-to-end once explicitly prompted to use browser automation tools and do all testing as a human user would.
在构建 Web 应用程序的情况下，一旦明确提示使用浏览器自动化工具并像人类用户一样进行所有测试，Claude 在端到端验证功能方面大多做得很好。

![Image 1: Screenshots taken by Claude through the Puppeteer MCP server as it tested the claude.ai clone.](https://example.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff94c2257964fb2d623f1e81f874977ebfc0986bc-1920x1080.gif&w=3840&q=75)

Screenshots taken by Claude through the Puppeteer MCP server as it tested the claude.ai clone.
Claude 通过 Puppeteer MCP 服务器在测试 claude.ai 克隆时拍摄的屏幕截图。

Providing Claude with these kinds of testing tools dramatically improved performance, as the agent was able to identify and fix bugs that weren't obvious from the code alone.
为 Claude 提供这些类型的测试工具显着提高了性能，因为智能体能够识别并修复仅从代码中看不出来的错误。

Some issues remain, like limitations to Claude's vision and to browser automation tools making it difficult to identify every kind of bug. For example, Claude can't see browser-native alert modals through the Puppeteer MCP, and features relying on these modals tended to be buggier as a result.
一些问题仍然存在，例如 Claude 的视觉和浏览器自动化工具的局限性，使得难以识别每种类型的错误。例如，Claude 无法通过 Puppeteer MCP 看到浏览器原生警报模态框，因此依赖这些模态框的功能往往更有问题。

## Getting Up to Speed
快速了解状态

With all of the above in place, every coding agent is prompted to run through a series of steps to get its bearings, some quite basic but still helpful:
有了上述所有内容，每个编码智能体都被提示运行一系列步骤来了解其方位，其中一些非常基本但仍然有帮助：

1. _Run `pwd` to see the directory you're working in. You'll only be able to edit files in this directory._
1. _运行 `pwd` 查看你正在工作的目录。你只能编辑此目录中的文件。_

2. _Read the git logs and progress files to get up to speed on what was recently worked on._
2. _阅读 git 日志和进度文件以快速了解最近的工作内容。_

3. _Read the features list file and choose the highest-priority feature that's not yet done to work on._
3. _阅读功能列表文件，选择尚未完成的最高优先级功能进行处理。_

This approach saves Claude some tokens in every session since it doesn't have to figure out how to test the code. It also helps to ask the initializer agent to write an init.sh script that can run the development server, and then run through a basic end-to-end test before implementing a new feature.
这种方法在每个会话中为 Claude 节省了一些令牌，因为它不必弄清楚如何测试代码。它还有助于要求初始化智能体编写一个可以运行开发服务器的 init.sh 脚本，然后在实现新功能之前运行基本的端到端测试。

In the case of the claude.ai clone, this meant that the agent always started the local development server and used the Puppeteer MCP to start a new chat, send a message, and receive a response. This ensured that Claude could quickly identify if the app had been left in a broken state, and immediately fix any existing bugs. If the agent had instead started implementing a new feature, it would likely make the problem worse.
在 claude.ai 克隆的情况下，这意味着智能体总是启动本地开发服务器并使用 Puppeteer MCP 开始新聊天、发送消息和接收响应。这确保了 Claude 可以快速识别应用程序是否处于损坏状态，并立即修复任何现有的错误。如果智能体开始实现新功能，很可能会使问题变得更糟。

Given all this, a typical session starts off with the following assistant messages:
鉴于所有这些，典型的会话以以下助手消息开始：

```
[Assistant] I'll start by getting my bearings and understanding the current state of the project.
[工具使用] <bash - pwd>
[工具使用] <read - claude-progress.txt>
[工具使用] <read - feature_list.json>
[Assistant] Let me check the git log to see recent work.
[工具使用] <bash - git log --oneline -20>
[Assistant] Now let me check if there's an init.sh script to restart the servers.
<启动开发服务器>
[Assistant] Excellent! Now let me navigate to the application and verify that some fundamental features are still working.
<测试基本功能>
[Assistant] Based on my verification testing, I can see that the fundamental functionality is working well. The core chat features, theme switching, conversation loading, and error handling are all functioning correctly. Now let me review the tests.json file more comprehensively to understand what needs to be implemented next.
<开始处理新功能>
```

Agent Failure Modes and Solutions
智能体失败模式和解决方案

| __问题__ | __初始化智能体行为__ | __编码智能体行为__ |
| --- | --- | --- |
| Claude 过早宣布整个项目完成。 | 设置功能列表文件：根据输入规范，设置一个结构化的 JSON 文件，其中包含端到端功能描述列表。 | 在会话开始时阅读功能列表文件。选择一个功能开始工作。 |
| Claude 将环境置于有错误或未记录进展的状态。 | 编写初始 git 存储库和进度笔记文件。 | 通过阅读进度笔记文件和 git 提交日志开始会话，并在开发服务器上运行基本测试以捕获任何未记录的错误。通过编写 git 提交和进度更新来结束会话。 |
| Claude 过早地将功能标记为完成。 | 设置功能列表文件。 | 自我验证所有功能。只有在仔细测试后才将功能标记为"通过"。 |
| Claude 必须花时间弄清楚如何运行应用程序。 | 编写一个可以运行开发服务器的 `init.sh` 脚本。 | 通过阅读 `init.sh` 开始会话。 |

Summarizing four common failure modes and solutions in long-running AI agents.
总结长时间运行 AI 智能体的四种常见失败模式和解决方案。

## Future Work
未来工作

This research demonstrates one possible set of solutions in a long-running agent harness to enable the model to make incremental progress across many context windows. However, there remain open questions.
这项研究展示了长时间运行智能体工具中一组可能的解决方案，使模型能够在许多上下文窗口中取得增量进展。然而，仍然存在未解决的问题。

Most notably, it's still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture. It seems reasonable that specialized agents like a testing agent, a quality assurance agent, or a code cleanup agent, could do an even better job at sub-tasks across the software development lifecycle.
最值得注意的是，目前尚不清楚是单个通用编码智能体在各种情况下表现最佳，还是通过多智能体架构可以实现更好的性能。专门的智能体（如测试智能体、质量保证智能体或代码清理智能体）在软件开发生命周期的子任务上可能会做得更好，这似乎是合理的。

Additionally, this demo is optimized for full-stack web app development. A future direction is to generalize these findings to other fields. It's likely that some or all of these lessons can be applied to the types of long-running agentic tasks required in, for example, scientific research or financial modeling.
此外，此演示针对全栈 Web 应用程序开发进行了优化。未来的方向是将这些发现概括到其他领域。其中一些或所有这些教训可能适用于例如科学研究或金融建模所需的长时间运行的智能体任务类型。

### Acknowledgements
致谢

Written by Justin Young. Special thanks to David Hershey, Prithvi Rajasakeran, Jeremy Hadfield, Naia Bouscal, Michael Tingley, Jesse Mu, Jake Eaton, Marius Buleandara, Maggie Vo, Pedram Navid, Nadine Yasser, and Alex Notov for their contributions.
本文由 Justin Young 撰写。特别感谢 David Hershey、Prithvi Rajasakeran、Jeremy Hadfield、Naia Bouscal、Michael Tingley、Jesse Mu、Jake Eaton、Marius Buleandara、Maggie Vo、Pedram Navid、Nadine Yasser 和 Alex Notov 的贡献。

This work reflects the collective efforts of several teams across Anthropic who made it possible for Claude to safely do long-horizon autonomous software engineering, especially the code RL & Claude Code teams. Interested candidates who would like to contribute are welcome to apply at anthropic.com/careers.
这项工作反映了 Anthropic 的几个团队的集体努力，他们使 Claude 能够安全地进行长时间自主软件工程，尤其是代码 RL 和 Claude Code 团队。欢迎有兴趣做出贡献的候选人申请 anthropic.com/careers。

### Footnotes
脚注

1. We refer to these as separate agents in this context only because they have different initial user prompts. The system prompt, set of tools, and overall agent harness was otherwise identical.
1. 我们在这种情况下将它们称为独立的智能体，只是因为它们具有不同的初始用户提示。系统提示、工具集和整体智能体工具在其他方面是相同的。
