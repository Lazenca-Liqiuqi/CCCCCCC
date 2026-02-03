# How we built our multi-agent research system | 我们如何构建多智能体研究系统

Claude now has Research capabilities that allow it to search across the web, Google Workspace, and any integrations to accomplish complex tasks.

Claude 现已具备 Research（研究）能力，使其能够通过网络、Google Workspace 和任何集成进行搜索，以完成复杂任务。

The journey of this multi-agent system from prototype to production taught us critical lessons about system architecture, tool design, and prompt engineering. A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together. Our Research feature involves an agent that plans a research process based on user queries, and then uses tools to create parallel agents that search for information simultaneously. Systems with multiple agents introduce new challenges in agent coordination, evaluation, and reliability.

这个多智能体系统从原型到生产的历程，教会了我们关于系统架构、工具设计和提示工程的关键经验教训。多智能体系统由多个协同工作的智能体（在循环中自主使用工具的 LLM）组成。我们的 Research 功能涉及一个基于用户查询规划研究过程的智能体，然后使用工具创建并行搜索信息的子智能体。包含多个智能体的系统在智能体协调、评估和可靠性方面带来了新的挑战。

This post breaks down the principles that worked for us—we hope you'll find them useful to apply when building your own multi-agent systems.

这篇文章分解了对我们有效的原则——我们希望你在构建自己的多智能体系统时能发现这些原则的实用价值。

---

## Benefits of a multi-agent system | 多智能体系统的优势

Research work involves open-ended problems where it's very difficult to predict the required steps in advance. You can't hardcode a fixed path for exploring complex topics, as the process is inherently dynamic and path-dependent. When people conduct research, they tend to continuously update their approach based on discoveries, following leads that emerge during investigation.

研究工作涉及开放式问题，很难提前预测所需的步骤。你无法为探索复杂主题硬编码固定路径，因为该过程本质上是动态的和路径依赖的。当人们进行研究时，他们倾向于根据发现不断更新方法，遵循在调查过程中出现的线索。

This unpredictability makes AI agents particularly well-suited for research tasks. Research demands the flexibility to pivot or explore tangential connections as the investigation unfolds. The model must operate autonomously for many turns, making decisions about which directions to pursue based on intermediate findings. A linear, one-shot pipeline cannot handle these tasks.

这种不可预测性使 AI 智能体特别适合研究任务。研究需要灵活性，能够在调查展开时转向或探索切向联系。模型必须自主运行许多轮次，根据中间发现决定追求哪些方向。线性的一次性管道无法处理这些任务。

The essence of search is compression: distilling insights from a vast corpus. Subagents facilitate compression by operating in parallel with their own context windows, exploring different aspects of the question simultaneously before condensing the most important tokens for the lead research agent. Each subagent also provides separation of concerns—distinct tools, prompts, and exploration trajectories—which reduces path dependency and enables thorough, independent investigations.

搜索的本质是压缩：从海量语料库中提取洞察。子智能体通过并行运行并使用各自的上下文窗口来促进压缩，同时探索问题的不同方面，然后将最重要的 token 浓缩给主导研究智能体。每个子智能体还提供关注点分离——不同的工具、提示和探索轨迹——这减少了路径依赖并实现彻底、独立的调查。

Once intelligence reaches a threshold, multi-agent systems become a vital way to scale performance. For instance, although individual humans have become more intelligent in the last 100,000 years, human societies have become _exponentially_ more capable in the information age because of our _collective_ intelligence and ability to coordinate. Even generally-intelligent agents face limits when operating as individuals; groups of agents can accomplish far more.

一旦智能达到阈值，多智能体系统就成为扩展性能的重要方式。例如，尽管在过去 10 万年中个体人类变得更聪明，但由于我们的_集体_智能和协调能力，人类社会在信息时代变得_指数级_更有能力。即使是具有一般智能的智能体在单独运行时也面临限制；智能体群体可以完成多得多的工作。

Our internal evaluations show that multi-agent research systems excel especially for breadth-first queries that involve pursuing multiple independent directions simultaneously. We found that a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval. For example, when asked to identify all the board members of the companies in the Information Technology S&P 500, the multi-agent system found the correct answers by decomposing this into tasks for subagents, while the single agent system failed to find the answer with slow, sequential searches.

我们的内部评估显示，多智能体研究系统特别擅长涉及同时追求多个独立方向的广度优先查询。我们发现，以 Claude Opus 4 为主导智能体、Claude Sonnet 4 为子智能体的多智能体系统在我们的内部研究评估中比单智能体 Claude Opus 4 表现高出 90.2%。例如，当被要求识别信息技术标普 500 公司的所有董事会成员时，多智能体系统通过将其分解为子智能体的任务找到了正确答案，而单智能体系统通过缓慢的顺序搜索未能找到答案。

Multi-agent systems work mainly because they help spend enough tokens to solve the problem. In our analysis, three factors explained 95% of the performance variance in the BrowseComp evaluation (which tests the ability of browsing agents to locate hard-to-find information). We found that token usage by itself explains 80% of the variance, with the number of tool calls and the model choice as the two other explanatory factors. This finding validates our architecture that distributes work across agents with separate context windows to add more capacity for parallel reasoning. The latest Claude models act as large efficiency multipliers on token use, as upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7. Multi-agent architectures effectively scale token usage for tasks that exceed the limits of single agents.

多智能体系统之所以有效，主要是因为它们有助于花费足够的 token 来解决问题。在我们的分析中，三个因素解释了 BrowseComp 评估中 95% 的性能方差（该评估测试浏览智能体定位难以找到信息的能力）。我们发现，token 使用本身解释了 80% 的方差，工具调用次数和模型选择是另外两个解释因素。这一发现验证了我们的架构，该架构将工作分布在具有独立上下文窗口的智能体之间，为并行推理增加更多容量。最新的 Claude 模型在 token 使用上充当大型效率倍增器，因为升级到 Claude Sonnet 4 比在 Claude Sonnet 3.7 上增加一倍 token 预算带来更大的性能提升。多智能体架构有效地扩展了超过单智能体限制的任务的 token 使用。

There is a downside: in practice, these architectures burn through tokens fast. In our data, agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats. For economic viability, multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance. Further, some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today. For instance, most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time. We've found that multi-agent systems excel at valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools.

有一个缺点：在实践中，这些架构很快消耗大量 token。在我们的数据中，智能体通常使用的 token 比聊天交互多约 4 倍，而多智能体系统使用的 token 比聊天多约 15 倍。为了经济可行性，多智能体系统需要任务价值足够高以支付增加的性能。此外，一些需要所有智能体共享相同上下文或涉及智能体之间许多依赖的领域目前不太适合多智能体系统。例如，大多数编码任务涉及的可真正并行化的任务比研究少，而 LLM 智能体目前还不擅长实时协调和委派给其他智能体。我们发现，多智能体系统擅长涉及大量并行化、超过单个上下文窗口的信息以及与众多复杂工具交互的有价值任务。

---

## Architecture overview for Research | Research 架构概览

Our Research system uses a multi-agent architecture with an orchestrator-worker pattern, where a lead agent coordinates the process while delegating to specialized subagents that operate in parallel.

我们的 Research 系统使用编排者-工作者模式的多智能体架构，其中主导智能体协调过程，同时委派给并行运行的专门子智能体。

![The multi-agent architecture in action: user queries flow through a lead agent that creates specialized subagents to search for different aspects in parallel. | 多智能体架构的实际运行：用户查询通过主导智能体流动，该智能体创建专门的子智能体并行搜索不同方面。](https://www-cdn.anthropic.com/images/4zrzovbb/website/1198befc0b33726c45692ac40f764022f4de1bf2-4584x2579.png)

多智能体架构的实际运行：用户查询通过主导智能体流动，该智能体创建专门的子智能体并行搜索不同方面。

When a user submits a query, the lead agent analyzes it, develops a strategy, and spawns subagents to explore different aspects simultaneously. As shown in the diagram above, the subagents act as intelligent filters by iteratively using search tools to gather information, in this case on AI agent companies in 2025, and then returning a list of companies to the lead agent so it can compile a final answer.

当用户提交查询时，主导智能体分析它，制定策略，并生成子智能体以同时探索不同方面。如上图所示，子智能体通过迭代使用搜索工具来收集信息而充当智能过滤器（在这种情况下是 2025 年的 AI 智能体公司），然后将公司列表返回给主导智能体，以便它能够汇编最终答案。

Traditional approaches using Retrieval Augmented Generation (RAG) use static retrieval. That is, they fetch some set of chunks that are most similar to an input query and use these chunks to generate a response. In contrast, our architecture uses a multi-step search that dynamically finds relevant information, adapts to new findings, and analyzes results to formulate high-quality answers.

使用检索增强生成（RAG）的传统方法使用静态检索。也就是说，它们获取与输入查询最相似的一组块，并使用这些块生成响应。相反，我们的架构使用多步搜索，动态地查找相关信息，适应新发现，并分析结果以制定高质量答案。

![Process diagram showing the complete workflow of our multi-agent Research system. When a user submits a query, the system creates a LeadResearcher agent that enters an iterative research process. The LeadResearcher begins by thinking through the approach and saving its plan to Memory to persist the context, since if the context window exceeds 200,000 tokens it will be truncated and it is important to retain the plan. It then creates specialized Subagents (two are shown here, but it can be any number) with specific research tasks. Each Subagent independently performs web searches, evaluates tool results using interleaved thinking, and returns findings to the LeadResearcher. The LeadResearcher synthesizes these results and decides whether more research is needed—if so, it can create additional subagents or refine its strategy. Once sufficient information is gathered, the system exits the research loop and passes all findings to a CitationAgent, which processes the documents and research report to identify specific locations for citations. This ensures all claims are properly attributed to their sources. The final research results, complete with citations, are then returned to the user. | 流程图显示了我们多智能体 Research 系统的完整工作流程。当用户提交查询时，系统创建一个 LeadResearcher 智能体，进入迭代研究过程。LeadResearcher 首先通过思考方法并将其计划保存到 Memory 以持久化上下文，因为如果上下文窗口超过 200,000 个 token，它将被截断，保留计划很重要。然后它创建具有特定研究任务的专门子智能体（这里显示了两个，但可以是任何数量）。每个子智能体独立执行网络搜索，使用交错思考评估工具结果，并将发现返回给 LeadResearcher。LeadResearcher 综合这些结果并决定是否需要更多研究——如果是，它可以创建额外的子智能体或完善其策略。一旦收集了足够的信息，系统退出研究循环并将所有发现传递给 CitationAgent，后者处理文档和研究报告以识别引用的具体位置。这确保所有声明都正确归因于其来源。最终的研究结果（包括引用）然后返回给用户。](https://www-cdn.anthropic.com/images/4zrzovbb/website/3bde53c9578d74f6e05c3e515e20b910c5a8c20a-4584x4584.png)

流程图显示了我们多智能体 Research 系统的完整工作流程。当用户提交查询时，系统创建一个 LeadResearcher 智能体，进入迭代研究过程。LeadResearcher 首先通过思考方法并将其计划保存到 Memory 以持久化上下文，因为如果上下文窗口超过 200,000 个 token，它将被截断，保留计划很重要。然后它创建具有特定研究任务的专门子智能体（这里显示了两个，但可以是任何数量）。每个子智能体独立执行网络搜索，使用交错思考评估工具结果，并将发现返回给 LeadResearcher。LeadResearcher 综合这些结果并决定是否需要更多研究——如果是，它可以创建额外的子智能体或完善其策略。一旦收集了足够的信息，系统退出研究循环并将所有发现传递给 CitationAgent，后者处理文档和研究报告以识别引用的具体位置。这确保所有声明都正确归因于其来源。最终的研究结果（包括引用）然后返回给用户。

---

## Prompt engineering and evaluations for research agents | 研究智能体的提示工程与评估

Multi-agent systems have key differences from single-agent systems, including a rapid growth in coordination complexity. Early agents made errors like spawning 50 subagents for simple queries, scouring the web endlessly for nonexistent sources, and distracting each other with excessive updates. Since each agent is steered by a prompt, prompt engineering was our primary lever for improving these behaviors. Below are some principles we learned for prompting agents:

多智能体系统与单智能体系统有关键区别，包括协调复杂性的快速增长。早期智能犯的错误包括为简单查询生成 50 个子智能体、无休止地搜索网络以寻找不存在的来源，以及通过过多更新相互干扰。由于每个智能体都由提示驱动，提示工程是我们改进这些行为的主要手段。以下是我们为提示智能体学到的一些原则：

1. *Think like your agents.* To iterate on prompts, you must understand their effects. To help us do this, we built simulations using our Console with the exact prompts and tools from our system, then watched agents work step-by-step. This immediately revealed failure modes: agents continuing when they already had sufficient results, using overly verbose search queries, or selecting incorrect tools. Effective prompting relies on developing an accurate mental model of the agent, which can make the most impactful changes obvious.

*像你的智能体一样思考。* 要迭代提示，你必须理解它们的效果。为了帮助我们做到这一点，我们使用我们系统的确切提示和工具在 Console 中构建模拟，然后逐步观察智能体工作。这立即揭示了失败模式：智能体在已经有足够结果时继续，使用过于冗长的搜索查询，或选择错误的工具。有效的提示依赖于开发智能体的准确心理模型，这可以使最具影响力的变化变得明显。

2. *Teach the orchestrator how to delegate.* In our system, the lead agent decomposes queries into subtasks and describes them to subagents. Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries. Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information. We started by allowing the lead agent to give simple, short instructions like 'research the semiconductor shortage,' but found these instructions often were vague enough that subagents misinterpreted the task or performed the exact same searches as other agents. For instance, one subagent explored the 2021 automotive chip crisis while 2 others duplicated work investigating current 2025 supply chains, without an effective division of labor.

*教导编排者如何委派。* 在我们的系统中，主导智能体将查询分解为子任务并将其描述给子智能体。每个子智能体需要目标、输出格式、关于要使用的工具和来源的指导以及明确的任务边界。没有详细的任务描述，智能体会重复工作、留下空白或未能找到必要信息。我们开始时允许主导智能体给出简单、简短的指令，如"研究半导体短缺"，但发现这些指令通常足够模糊，以至于子智能体误解了任务或执行与其他智能体完全相同的搜索。例如，一个子智能体探索 2021 年汽车芯片危机，而另外两个重复工作调查当前的 2025 年供应链，没有有效的分工。

3. *Scale effort to query complexity.* Agents struggle to judge appropriate effort for different tasks, so we embedded scaling rules in the prompts. Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents with clearly divided responsibilities. These explicit guidelines help the lead agent allocate resources efficiently and prevent overinvestment in simple queries, which was a common failure mode in our early versions.

*根据查询复杂性调整工作量。* 智能体难以判断不同任务的适当工作量，因此我们在提示中嵌入了扩展规则。简单的事实查找只需要 1 个智能体进行 3-10 次工具调用，直接比较可能需要 2-4 个子智能体各自进行 10-15 次调用，而复杂研究可能使用超过 10 个具有明确划分职责的子智能体。这些明确的指导原则帮助主导智能体高效分配资源，并防止在简单查询中过度投资，这是我们早期版本中常见的失败模式。

4. *Tool design and selection are critical.* Agent-tool interfaces are as critical as human-computer interfaces. Using the right tool is efficient—often, it's strictly necessary. For instance, an agent searching the web for context that only exists in Slack is doomed from the start. With MCP servers that give the model access to external tools, this problem compounds, as agents encounter unseen tools with descriptions of wildly varying quality. We gave our agents explicit heuristics: for example, examine all available tools first, match tool usage to user intent, search the web for broad external exploration, or prefer specialized tools over generic ones. Bad tool descriptions can send agents down completely wrong paths, so each tool needs a distinct purpose and a clear description.

*工具设计和选择至关重要。* 智能体-工具接口与人机接口一样重要。使用正确的工具是高效的——通常，它是绝对必要的。例如，在网络上搜索仅存在于 Slack 中的上下文的智能体从一开始就注定失败。通过 MCP 服务器赋予模型访问外部工具的能力，这个问题变得更加复杂，因为智能体遇到具有质量差异极大的描述的未见过的工具。我们给我们的智能体明确的启发式规则：例如，首先检查所有可用工具，将工具使用与用户意图匹配，在网络搜索以进行广泛的外部探索，或者优先使用专用工具而不是通用工具。糟糕的工具描述可能会使智能体走向完全错误的路径，因此每个工具都需要独特的目的和清晰的描述。

5. *Let agents improve themselves.* We found that the Claude 4 models can be excellent prompt engineers. When given a prompt and a failure mode, they are able to diagnose why the agent is failing and suggest improvements. We even created a tool-testing agent—when given a flawed MCP tool, it attempts to use the tool and then rewrites the tool description to avoid failures. By testing the tool dozens of times, this agent found key nuances and bugs. This process for improving tool ergonomics resulted in a 40% decrease in task completion time for future agents using the new description, because they were able to avoid most mistakes.

*让智能体自我改进。* 我们发现 Claude 4 模型可以是出色的提示工程师。当给定提示和失败模式时，它们能够诊断智能体为何失败并建议改进。我们甚至创建了一个工具测试智能体——当给定有缺陷的 MCP 工具时，它尝试使用该工具，然后重写工具描述以避免失败。通过测试工具数十次，该智能体发现了关键细微差别和错误。这个改进工具人体工程学的过程使使用新描述的未来智能体的任务完成时间减少了 40%，因为它们能够避免大多数错误。

6. *Start wide, then narrow down.* Search strategy should mirror expert human research: explore the landscape before drilling into specifics. Agents often default to overly long, specific queries that return few results. We counteracted this tendency by prompting agents to start with short, broad queries, evaluate what's available, then progressively narrow focus.

*先宽泛，后深入。* 搜索策略应反映专家人类研究：在深入细节之前探索领域。智能体通常默认使用过长、具体的查询，返回很少的结果。我们通过提示智能体以简短、宽泛的查询开始，评估可用的内容，然后逐渐缩小焦点来对抗这种倾向。

7. *Guide the thinking process.* Extended thinking mode, which leads Claude to output additional tokens in a visible thinking process, can serve as a controllable scratchpad. The lead agent uses thinking to plan its approach, assessing which tools fit the task, determining query complexity and subagent count, and defining each subagent's role. Our testing showed that extended thinking improved instruction-following, reasoning, and efficiency. Subagents also plan, then use interleaved thinking after tool results to evaluate quality, identify gaps, and refine their next query. This makes subagents more effective in adapting to any task.

*指导思考过程。* 扩展思考模式使 Claude 在可见的思考过程中输出额外的 token，可以充当可控的草稿板。主导智能体使用思考来规划其方法，评估哪些工具适合任务，确定查询复杂性和子智能体数量，并定义每个子智能体的角色。我们的测试表明，扩展思考改进了指令遵循、推理和效率。子智能体也规划，然后在工具结果之后使用交错思考来评估质量、识别空白并完善其下一个查询。这使得子智能体更有效地适应任何任务。

8. *Parallel tool calling transforms speed and performance.* Complex research tasks naturally involve exploring many sources. Our early agents executed sequential searches, which was painfully slow. For speed, we introduced two kinds of parallelization: (1) the lead agent spins up 3-5 subagents in parallel rather than serially; (2) the subagents use 3+ tools in parallel. These changes cut research time by up to 90% for complex queries, allowing Research to do more work in minutes instead of hours while covering more information than other systems.

*并行工具调用转变速度和性能。*复杂的研究任务自然涉及探索许多来源。我们的早期智能体执行顺序搜索，这非常慢。为了提高速度，我们引入了两种并行化：（1）主导智能体并行而不是串行启动 3-5 个子智能体；（2）子智能体并行使用 3+ 个工具。这些变化将复杂查询的研究时间减少了高达 90%，使 Research 能够在几分钟而不是几小时内完成更多工作，同时覆盖比其他系统更多的信息。

Our prompting strategy focuses on instilling good heuristics rather than rigid rules. We studied how skilled humans approach research tasks and encoded these strategies in our prompts—strategies like decomposing difficult questions into smaller tasks, carefully evaluating the quality of sources, adjusting search approaches based on new information, and recognizing when to focus on depth (investigating one topic in detail) vs. breadth (exploring many topics in parallel). We also proactively mitigated unintended side effects by setting explicit guardrails to prevent the agents from spiraling out of control. Finally, we focused on a fast iteration loop with observability and test cases.

我们的提示策略专注于灌输良好的启发式规则而不是僵化规则。我们研究了熟练的人类如何处理研究任务，并在我们的提示中编码了这些策略——策略包括将困难问题分解为较小的任务、仔细评估来源质量、根据新信息调整搜索方法，以及识别何时专注于深度（详细调查一个主题）与广度（并行探索许多主题）。我们还通过设置明确的护栏来主动减轻意外的副作用，以防止智能体失控。最后，我们专注于具有可观察性和测试用例的快速迭代循环。

---

## Effective evaluation of agents | 智能体的有效评估

Good evaluations are essential for building reliable AI applications, and agents are no different. However, evaluating multi-agent systems presents unique challenges. Traditional evaluations often assume that the AI follows the same steps each time: given input X, the system should follow path Y to produce output Z. But multi-agent systems don't work this way. Even with identical starting points, agents might take completely different valid paths to reach their goal. One agent might search three sources while another searches ten, or they might use different tools to find the same answer. Because we don't always know what the right steps are, we usually can't just check if agents followed the "correct" steps we prescribed in advance. Instead, we need flexible evaluation methods that judge whether agents achieved the right outcomes while also following a reasonable process.

良好的评估对于构建可靠的 AI 应用程序至关重要，智能体也不例外。然而，评估多智能体系统带来了独特的挑战。传统的评估通常假设 AI 每次都遵循相同的步骤：给定输入 X，系统应该遵循路径 Y 产生输出 Z。但多智能体系统不是这样工作的。即使具有相同的起点，智能体也可能采取完全不同的有效路径来达到目标。一个智能体可能搜索三个来源，而另一个搜索十个，或者它们可能使用不同的工具来找到相同的答案。因为我们并不总是知道正确的步骤是什么，所以我们通常不能只检查智能体是否遵循了我们预先规定的"正确"步骤。相反，我们需要灵活的评估方法来判断智能体是否实现了正确的成果，同时遵循了合理的过程。

*Start evaluating immediately with small samples*. In early agent development, changes tend to have dramatic impacts because there is abundant low-hanging fruit. A prompt tweak might boost success rates from 30% to 80%. With effect sizes this large, you can spot changes with just a few test cases. We started with a set of about 20 queries representing real usage patterns. Testing these queries often allowed us to clearly see the impact of changes. We often hear that AI developer teams delay creating evals because they believe that only large evals with hundreds of test cases are useful. However, it's best to start with small-scale testing right away with a few examples, rather than delaying until you can build more thorough evals.

*立即开始小样本评估。* 在早期智能体开发中，变化往往具有巨大影响，因为存在大量容易实现的目标。提示调整可能会将成功率从 30% 提高到 80%。具有如此大的效果大小，你可以只用几个测试用例就能发现变化。我们开始时使用了一组约 20 个代表真实使用模式的查询。测试这些查询通常使我们能够清楚地看到变化的影响。我们经常听到 AI 开发团队延迟创建评估，因为他们认为只有具有数百个测试用例的大规模评估才有用。然而，最好立即用几个示例开始小规模测试，而不是延迟直到你可以构建更彻底的评估。

*LLM-as-judge evaluation scales when done well.* Research outputs are difficult to evaluate programmatically, since they are free-form text and rarely have a single correct answer. LLMs are a natural fit for grading outputs. We used an LLM judge that evaluated each output against criteria in a rubric: factual accuracy (do claims match sources?), citation accuracy (do the cited sources match the claims?), completeness (are all requested aspects covered?), source quality (did it use primary sources over lower-quality secondary sources?), and tool efficiency (did it use the right tools a reasonable number of times?). We experimented with multiple judges to evaluate each component, but found that a single LLM call with a single prompt outputting scores from 0.0-1.0 and a pass-fail grade was the most consistent and aligned with human judgements. This method was especially effective when the eval test cases _did_ have a clear answer, and we could use the LLM judge to simply check if the answer was correct (i.e. did it accurately list the pharma companies with the top 3 largest R&D budgets?). Using an LLM as a judge allowed us to scalably evaluate hundreds of outputs.

*LLM 作为评估者在做得好时可以扩展。* 研究输出很难通过编程评估，因为它们是自由形式文本，很少有一个正确答案。LLM 自然适合对输出进行评分。我们使用了一个 LLM 评估者，根据标准表中的标准评估每个输出：事实准确性（声明是否与来源匹配？）、引用准确性（引用的来源是否与声明匹配？）、完整性（是否涵盖了所有请求的方面？）、来源质量（它是否使用主要来源而不是较低质量的次要来源？）和工具效率（它是否以合理的次数使用正确的工具？）。我们尝试了多个评估者来评估每个组件，但发现单个 LLM 调用与单个提示输出 0.0-1.0 的分数和通过-失败等级是最一致的，并与人类判断一致。当评估测试用例_确实_有明确答案时，这种方法特别有效，我们可以使用 LLM 评估者简单地检查答案是否正确（即，它是否准确地列出了研发预算前 3 大的制药公司？）。使用 LLM 作为评估者使我们可以扩展评估数百个输出。

*Human evaluation catches what automation misses.* People testing agents find edge cases that evals miss. These include hallucinated answers on unusual queries, system failures, or subtle source selection biases. In our case, human testers noticed that our early agents consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources like academic PDFs or personal blogs. Adding source quality heuristics to our prompts helped resolve this issue. Even in a world of automated evaluations, manual testing remains essential.

*人类评估捕获自动化遗漏的内容。* 测试智能体的人发现评估遗漏的边缘情况。这些包括异常查询上的幻觉答案、系统故障或微妙的来源选择偏差。在我们的案例中，人类测试员注意到我们的早期智能体始终选择 SEO 优化的内容农场，而不是权威但排名较低的来源，如学术 PDF 或个人博客。在我们的提示中添加来源质量启发式规则有助于解决这个问题。即使在自动化评估的世界中，手动测试仍然至关重要。

Multi-agent systems have emergent behaviors, which arise without specific programming. For instance, small changes to the lead agent can unpredictably change how subagents behave. Success requires understanding interaction patterns, not just individual agent behavior. Therefore, the best prompts for these agents are not just strict instructions, but frameworks for collaboration that define the division of labor, problem-solving approaches, and effort budgets. Getting this right relies on careful prompting and tool design, solid heuristics, observability, and tight feedback loops. See the open-source prompts in our Cookbook for example prompts from our system.

多智能体系统具有在没有特定编程的情况下出现的涌现行为。例如，对主导智能体的小变化可能会不可预测地改变子智能体的行为。成功需要理解交互模式，而不仅仅是个体智能体行为。因此，这些智能体的最佳提示不仅仅是严格的指令，而是协作框架，定义分工、解决问题的方法和工作量预算。正确实现这一点依赖于仔细的提示和工具设计、可靠的启发式规则、可观察性和紧密的反馈循环。请参阅我们 Cookbook 中的开源提示，了解我们系统的示例提示。

---

## Production reliability and engineering challenges | 生产可靠性与工程挑战

In traditional software, a bug might break a feature, degrade performance, or cause outages. In agentic systems, minor changes cascade into large behavioral changes, which makes it remarkably difficult to write code for complex agents that must maintain state in a long-running process.

在传统软件中，bug 可能会破坏功能、降低性能或导致中断。在智能体系统中，小变化会级联成大的行为变化，这使得为必须在长时间运行过程中保持状态的复杂智能体编写代码变得异常困难。

*Agents are stateful and errors compound.* Agents can run for long periods of time, maintaining state across many tool calls. This means we need to durably execute code and handle errors along the way. Without effective mitigations, minor system failures can be catastrophic for agents. When errors occur, we can't just restart from the beginning: restarts are expensive and frustrating for users. Instead, we built systems that can resume from where the agent was when the errors occurred. We also use the model's intelligence to handle issues gracefully: for instance, letting the agent know when a tool is failing and letting it adapt works surprisingly well. We combine the adaptability of AI agents built on Claude with deterministic safeguards like retry logic and periodic checkpoints.

*智能体是有状态的，错误会复合。* 智能体可以运行很长时间，在许多工具调用之间保持状态。这意味着我们需要耐久地执行代码并沿途处理错误。没有有效的缓解措施，轻微的系统故障对智能体来说可能是灾难性的。当错误发生时，我们不能只是从头重新启动：重新启动对用户来说既昂贵又令人沮丧。相反，我们构建了可以从智能体发生错误时所在的位置恢复的系统。我们还使用模型的智能优雅地处理问题：例如，让智能体知道工具何时失败并让它适应效果出奇地好。我们将基于 Claude 构建的 AI 智能体的适应性与确定性保障（如重试逻辑和定期检查点）结合起来。

*Debugging benefits from new approaches.* Agents make dynamic decisions and are non-deterministic between runs, even with identical prompts. This makes debugging harder. For instance, users would report agents "not finding obvious information," but we couldn't see why. Were the agents using bad search queries? Choosing poor sources? Hitting tool failures? Adding full production tracing let us diagnose why agents failed and fix issues systematically. Beyond standard observability, we monitor agent decision patterns and interaction structures—all without monitoring the contents of individual conversations, to maintain user privacy. This high-level observability helped us diagnose root causes, discover unexpected behaviors, and fix common failures.

*调试受益于新方法。* 智能体做出动态决策，并且在运行之间是不确定性的，即使具有相同的提示。这使得调试更加困难。例如，用户会报告智能体"没有找到明显信息"，但我们看不到原因。智能体是否使用了糟糕的搜索查询？选择了糟糕的来源？遇到了工具故障？添加完整的生产跟踪使我们能够诊断智能体为何失败并系统地修复问题。除了标准的可观察性外，我们还监控智能体决策模式和交互结构——所有这些都不监控单个对话的内容，以维护用户隐私。这种高级别的可观察性帮助我们诊断根本原因、发现意外行为并修复常见故障。

*Deployment needs careful coordination.* Agent systems are highly stateful webs of prompts, tools, and execution logic that run almost continuously. This means that whenever we deploy updates, agents might be anywhere in their process. We therefore need to prevent our well-meaning code changes from breaking existing agents. We can't update every agent to the new version at the same time. Instead, we use rainbow deployments to avoid disrupting running agents, by gradually shifting traffic from old to new versions while keeping both running simultaneously.

*部署需要仔细协调。*智能体系统是高度有状态的提示、工具和执行逻辑网络，几乎连续运行。这意味着每当我们部署更新时，智能体可能处于其过程的任何位置。因此，我们需要防止我们善意的代码更改破坏现有智能体。我们不能同时将每个智能体更新到新版本。相反，我们使用彩虹部署来避免中断正在运行的智能体，通过逐渐将流量从旧版本转移到新版本，同时保持两者同时运行。

*Synchronous execution creates bottlenecks.* Currently, our lead agents execute subagents synchronously, waiting for each set of subagents to complete before proceeding. This simplifies coordination, but creates bottlenecks in the information flow between agents. For instance, the lead agent can't steer subagents, subagents can't coordinate, and the entire system can be blocked while waiting for a single subagent to finish searching. Asynchronous execution would enable additional parallelism: agents working concurrently and creating new subagents when needed. But this asynchronicity adds challenges in result coordination, state consistency, and error propagation across the subagents. As models can handle longer and more complex research tasks, we expect the performance gains will justify the complexity.

*同步执行造成瓶颈。*目前，我们的主导智能体同步执行子智能体，等待每组子智能体完成后再继续。这简化了协调，但在智能体之间的信息流中造成瓶颈。例如，主导智能体无法引导子智能体，子智能体无法协调，整个系统可能在等待单个子智能体完成搜索时被阻塞。异步执行将实现额外的并行性：智能体并发工作并在需要时创建新的子智能体。但这种异步性在结果协调、状态一致性和子智能体之间的错误传播方面增加了挑战。随着模型可以处理更长和更复杂的研究任务，我们预计性能提升将证明复杂性是合理的。

---

## Conclusion | 结论

When building AI agents, the last mile often becomes most of the journey. Codebases that work on developer machines require significant engineering to become reliable production systems. The compound nature of errors in agentic systems means that minor issues for traditional software can derail agents entirely. One step failing can cause agents to explore entirely different trajectories, leading to unpredictable outcomes. For all the reasons described in this post, the gap between prototype and production is often wider than anticipated.

在构建 AI 智能体时，最后一英里通常成为旅程的大部分。在开发人员机器上工作的代码库需要大量工程才能成为可靠的生产系统。智能体系统中错误的复合性质意味着传统软件的小问题可能会完全破坏智能体。一步失败可能导致智能体探索完全不同的轨迹，导致不可预测的结果。由于本文中描述的所有原因，原型和生产之间的差距通常比预期的要大。

Despite these challenges, multi-agent systems have proven valuable for open-ended research tasks. Users have said that Claude helped them find business opportunities they hadn't considered, navigate complex healthcare options, resolve thorny technical bugs, and save up to days of work by uncovering research connections they wouldn't have found alone. Multi-agent research systems can operate reliably at scale with careful engineering, comprehensive testing, detail-oriented prompt and tool design, robust operational practices, and tight collaboration between research, product, and engineering teams who have a strong understanding of current agent capabilities. We're already seeing these systems transform how people solve complex problems.

尽管面临这些挑战，多智能体系统已被证明对开放式研究任务很有价值。用户表示，Claude 帮助他们发现了他们未曾考虑过的商业机会，导航复杂的医疗保健选项，解决棘手的技术错误，并通过揭示他们不会独自发现的研究联系而节省高达数天的工作。多智能体研究系统可以通过仔细的工程、全面的测试、注重细节的提示和工具设计、强大的运营实践以及研究、产品和工程团队之间的紧密协作来可靠地大规模运行，这些团队对当前智能体能力有深刻的理解。我们已经看到这些系统正在改变人们解决复杂问题的方式。

![A Clio embedding plot showing the most common ways people are using the Research feature today. The top use case categories are developing software systems across specialized domains (10%), develop and optimize professional and technical content (8%), develop business growth and revenue generation strategies (8%), assist with academic research and educational material development (7%), and research and verify information about people, places, or organizations (5%). | Clio 嵌入图显示人们今天使用 Research 功能的最常见方式。顶级用例类别包括跨专业领域开发软件系统（10%），开发和优化专业和技术内容（8%），制定业务增长和收入生成策略（8%），协助学术研究和教育材料开发（7%），以及研究和验证有关人员、地点或组织的信息（5%）。](https://www-cdn.anthropic.com/images/4zrzovbb/website/09a90e0aca54859553e93c18683e7fd33ff16d4c-2654x2148.png)

Clio 嵌入图显示人们今天使用 Research 功能的最常见方式。顶级用例类别包括跨专业领域开发软件系统（10%），开发和优化专业和技术内容（8%），制定业务增长和收入生成策略（8%），协助学术研究和教育材料开发（7%），以及研究和验证有关人员、地点或组织的信息（5%）。

---

## Acknowledgements | 致谢

Written by Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, and Daniel Ford. This work reflects the collective efforts of several teams across Anthropic who made the Research feature possible. Special thanks go to the Anthropic apps engineering team, whose dedication brought this complex multi-agent system to production. We're also grateful to our early users for their excellent feedback.

本文由 Jeremy Hadfield、Barry Zhang、Kenneth Lien、Florian Scholz、Jeremy Fox 和 Daniel Ford 撰写。这项工作反映了 Anthropic 多个团队的集体努力，他们使 Research 功能成为可能。特别感谢 Anthropic 应用工程团队，他们的奉献使这个复杂的多智能体系统投入生产。我们还感谢我们早期用户的出色反馈。

---

## Appendix | 附录

Below are some additional miscellaneous tips for multi-agent systems.

以下是一些关于多智能体系统的额外杂项提示。

*End-state evaluation of agents that mutate state over many turns.* Evaluating agents that modify persistent state across multi-turn conversations presents unique challenges. Unlike read-only research tasks, each action can change the environment for subsequent steps, creating dependencies that traditional evaluation methods struggle to handle. We found success focusing on end-state evaluation rather than turn-by-turn analysis. Instead of judging whether the agent followed a specific process, evaluate whether it achieved the correct final state. This approach acknowledges that agents may find alternative paths to the same goal while still ensuring they deliver the intended outcome. For complex workflows, break evaluation into discrete checkpoints where specific state changes should have occurred, rather than attempting to validate every intermediate step.

*评估在多轮对话中改变状态的智能体的最终状态。*评估在多轮对话中修改持久状态的智能体提出了独特的挑战。与只读研究任务不同，每个操作都可以改变后续步骤的环境，创建传统评估方法难以处理的依赖关系。我们成功地专注于最终状态评估而不是逐轮分析。不是判断智能体是否遵循了特定过程，而是评估它是否达到了正确的最终状态。这种方法承认智能体可能找到通往同一目标的替代路径，同时仍然确保它们交付预期的结果。对于复杂的工作流程，将评估分解为离散的检查点，其中应该发生特定的状态变化，而不是尝试验证每个中间步骤。

*Long-horizon conversation management.* Production agents often engage in conversations spanning hundreds of turns, requiring careful context management strategies. As conversations extend, standard context windows become insufficient, necessitating intelligent compression and memory mechanisms. We implemented patterns where agents summarize completed work phases and store essential information in external memory before proceeding to new tasks. When context limits approach, agents can spawn fresh subagents with clean contexts while maintaining continuity through careful handoffs. Further, they can retrieve stored context like the research plan from their memory rather than losing previous work when reaching the context limit. This distributed approach prevents context overflow while preserving conversation coherence across extended interactions.

*长期对话管理。*生产智能体经常进行跨越数百轮的对话，需要仔细的上下文管理策略。随着对话的延长，标准上下文窗口变得不足，需要智能压缩和内存机制。我们实现了智能体总结已完成工作阶段并在继续新任务之前将重要信息存储在外部内存中的模式。当接近上下文限制时，智能体可以生成具有干净上下文的新子智能体，同时通过仔细的交接保持连续性。此外，它们可以从其内存中检索存储的上下文（如研究计划），而不是在达到上下文限制时丢失以前的工作。这种分布式方法防止上下文溢出，同时在扩展交互中保持对话连贯性。

*Subagent output to a filesystem to minimize the 'game of telephone.'* Direct subagent outputs can bypass the main coordinator for certain types of results, improving both fidelity and performance. Rather than requiring subagents to communicate everything through the lead agent, implement artifact systems where specialized agents can create outputs that persist independently. Subagents call tools to store their work in external systems, then pass lightweight references back to the coordinator. This prevents information loss during multi-stage processing and reduces token overhead from copying large outputs through conversation history. The pattern works particularly well for structured outputs like code, reports, or data visualizations where the subagent's specialized prompt produces better results than filtering through a general coordinator.

*子智能体输出到文件系统以最小化"传话游戏"。* 直接的子智能体输出可以绕过主要协调器以获取某些类型的结果，提高保真度和性能。不是要求子智能体通过主导智能体传达所有内容，而是实现工件系统，其中专用智能体可以创建独立持久化的输出。子智能体调用工具将其工作存储在外部系统中，然后将轻量级引用传递回协调器。这防止了多阶段处理期间的信息丢失，并减少了通过对话历史复制大输出的 token 开销。该模式特别适用于结构化输出，如代码、报告或数据可视化，其中子智能体的专用提示产生比通过通用协调器过滤更好的结果。

---

## Sources | 来源

- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

- [我们如何构建多智能体研究系统](https://www.anthropic.com/engineering/multi-agent-research-system)
