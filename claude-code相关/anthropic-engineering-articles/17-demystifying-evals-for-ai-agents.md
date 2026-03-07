# Demystifying Evals for AI Agents | 揭开 AI 智能体评估的神秘面纱

---

## Introduction | 介绍

Good evaluations help teams ship AI agents more confidently. Without them, it's easy to get stuck in reactive loops—catching issues only in production, where fixing one failure creates others. Evals make problems and behavioral changes visible before they affect users, and their value compounds over the lifecycle of an agent.
良好的评估帮助团队更自信地发布 AI 智能体。没有评估，团队很容易陷入被动循环——只在生产环境中发现问题，修复一个失败又会导致其他问题。评估在问题影响用户之前就使其可见，并在智能体的整个生命周期中产生复合价值。

As we described in Building effective agents, agents operate over many turns: calling tools, modifying state, and adapting based on intermediate results. These same capabilities that make AI agents useful—autonomy, intelligence, and flexibility—also make them harder to evaluate.
正如我们在《构建有效智能体》中所述，智能体在多个轮次中运作：调用工具、修改状态并根据中间结果进行调整。这些使 AI 智能体变得有用的能力——自主性、智能和灵活性——也使它们更难评估。

Through our internal work and with customers at the frontier of agent development, we've learned how to design more rigorous and useful evals for agents. Here's what's worked across a range of agent architectures and use cases in real-world deployment.
通过我们的内部工作以及与处于智能体开发前沿的客户合作，我们学会了如何为智能体设计更严格、更有用的评估。以下是在各种智能体架构和用例的实际部署中行之有效的方法。

## The Structure of an Evaluation | 评估的结构

An *evaluation* ("eval") is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success. In this post, we focus on *automated evals* that can be run during development without real users.
*评估*（"eval"）是对 AI 系统的测试：给 AI 一个输入，然后对其输出应用评分逻辑以衡量成功。在本文中，我们专注于 *自动化评估*，它可以在开发过程中运行，无需真实用户。

*Single-turn evaluations* are straightforward: a prompt, a response, and grading logic. For earlier LLMs, single-turn, non-agentic evals were the main evaluation method. As AI capabilities have advanced, *multi-turn evaluations* have become increasingly common.
*单轮评估* 很简单：一个提示、一个响应和评分逻辑。对于早期的 LLM，单轮非智能体评估是主要的评估方法。随着 AI 能力的进步，*多轮评估* 变得越来越普遍。

![Image 1](https://www-cdn.anthropic.com/images/4zrzovbb/website/bd42e7b2f3e9bb5218142796d3ede4816588dec0-4584x2834.png)

In a simple eval, an agent processes a prompt, and a grader checks if the output matches expectations. For a more complex multi-turn eval, a coding agent receives tools, a task (building an MCP server in this case), and an environment, executes an "agent loop" (tool calls and reasoning), and updates the environment with the implementation. Grading then uses unit tests to verify the working MCP server.
在一个简单的评估中，智能体处理一个提示，评分器检查输出是否符合预期。对于更复杂的多轮评估，编码智能体接收工具、一个任务（在这种情况下是构建 MCP 服务器）和一个环境，执行"智能体循环"（工具调用和推理），并通过实现更新环境。然后评分使用单元测试来验证工作的 MCP 服务器。

*Agent evaluations* are even more complex. Agents use tools across many turns, modifying state in the environment and adapting as they go—which means mistakes can propagate and compound. Frontier models can also find creative solutions that surpass the limits of static evals. For instance, Opus 4.5 solved a 𝜏2-bench problem about booking a flight by discovering a loophole in the policy. It "failed" the evaluation as written, but actually came up with a better solution for the user.
*智能体评估* 更加复杂。智能体在多个轮次中使用工具，修改环境中的状态并随着进行而调整——这意味着错误可能会传播和复合。前沿模型还可以找到超越静态评估限制的创造性解决方案。例如，Opus 4.5 通过发现策略中的漏洞解决了一个关于预订航班的 𝜏2-bench 问题。它"未通过"了书面评估，但实际上为用户提出了更好的解决方案。

When building agent evaluations, we use the following definitions:
在构建智能体评估时，我们使用以下定义：

- A *task* (a.k.a *problem* or *test case*) is a single test with defined inputs and success criteria.
- 一个 *任务*（也叫 *问题* 或 *测试用例*）是具有定义输入和成功标准的单个测试。

- Each attempt at a task is a *trial*. Because model outputs vary between runs, we run multiple trials to produce more consistent results.
- 每次尝试任务都是一个 *试验*。由于模型输出在运行之间有所不同，我们运行多个试验以产生更一致的结果。

- A *grader* is logic that scores some aspect of the agent's performance. A task can have multiple graders, each containing multiple assertions (sometimes called *checks*).
- *评分器* 是对智能体性能的某些方面进行评分的逻辑。一个任务可以有多个评分器，每个评分器包含多个断言（有时称为 *检查*）。

- A *transcript* (also called a *trace* or *trajectory*) is the complete record of a trial, including outputs, tool calls, reasoning, intermediate results, and any other interactions. For the Anthropic API, this is the full messages array at the end of an eval run - containing all the calls to the API and all of the returned responses during the evaluation.
- *记录*（也叫 *跟踪* 或 *轨迹*）是试验的完整记录，包括输出、工具调用、推理、中间结果和任何其他交互。对于 Anthropic API，这是评估运行结束时的完整消息数组——包含在评估期间对 API 的所有调用和所有返回的响应。

- The *outcome* is the final state in the environment at the end of the trial. A flight-booking agent might say "Your flight has been booked" at the end of the transcript, but the outcome is whether a reservation exists in the environment's SQL database.
- *结果*是试验结束时环境中的最终状态。航班预订智能体可能在记录结束时说"您的航班已预订"，但结果是环境 SQL 数据库中是否存在预订。

- An *evaluation harness* is the infrastructure that runs evals end-to-end. It provides instructions and tools, runs tasks concurrently, records all the steps, grades outputs, and aggregates results.
- *评估工具* 是端到端运行评估的基础设施。它提供说明和工具、并发运行任务、记录所有步骤、评分输出并汇总结果。

- An *agent harness* (or *scaffold*) is the system that enables a model to act as an agent: it processes inputs, orchestrates tool calls, and returns results. When we evaluate "an agent," we're evaluating the harness _and_ the model working together. For example, Claude Code is a flexible agent harness, and we used its core primitives through the Agent SDK to build our long-running agent harness.
- *智能体工具*（或 *脚手架*）是使模型能够充当智能体的系统：它处理输入、编排工具调用并返回结果。当我们评估"一个智能体"时，我们是在评估工具和模型一起工作。例如，Claude Code 是一个灵活的智能体工具，我们通过 Agent SDK 使用其核心原语来构建我们的长时间运行的智能体工具。

- An *evaluation suite* is a collection of tasks designed to measure specific capabilities or behaviors. Tasks in a suite typically share a broad goal. For instance, a customer support eval suite might test refunds, cancellations, and escalations.
- *评估套件* 是旨在测量特定能力或行为的任务集合。套件中的任务通常共享一个广泛的目标。例如，客户支持评估套件可能测试退款、取消和升级。

![Image 2](https://www-cdn.anthropic.com/images/4zrzovbb/website/0205b36f9639fc27f2f6566f73cb56b06f59d555-4584x2580.png)

Components of evaluations for agents.
智能体评估的组件。

## Why Build Evaluations? | 为什么要构建评估？

When teams first start building agents, they can get surprisingly far through a combination of manual testing, dogfooding, and intuition. More rigorous evaluation may even seem like overhead that slows down shipping. But after the early prototyping stages, once an agent is in production and has started scaling, building without evals starts to break down.
当团队开始构建智能体时，他们可以通过手动测试、内部使用和直觉的组合取得令人惊讶的进展。更严格的评估甚至可能看起来会减慢发布的开销。但在早期原型阶段之后，一旦智能体投入生产并开始扩展，没有评估的构建就会开始崩溃。

The breaking point often comes when users report the agent feels worse after changes, and the team is 'flying blind' with no way to verify except to guess and check. Absent evals, debugging is reactive: wait for complaints, reproduce manually, fix the bug, and hope nothing else regressed. Teams can't distinguish real regressions from noise, automatically test changes against hundreds of scenarios before shipping, or measure improvements.
崩溃点通常出现在用户报告智能体在更改后感觉更糟糕时，团队"盲目飞行"，除了猜测和检查之外无法验证。没有评估，调试是被动的：等待投诉、手动重现、修复错误，并希望没有其他回归。团队无法区分真正的回归和噪音，无法在发布之前自动针对数百种场景测试更改，也无法衡量改进。

We've seen this progression play out many times. For instance, Claude Code started with fast iteration based on feedback from Anthropic employees and external users. Later, we added evals—first for narrow areas like concision and file edits, and then for more complex behaviors like over-engineering. These evals helped identify issues, guide improvements, and focus research-product collaborations. Combined with production monitoring, A/B tests, user research, and more, evals provide signals to continue improving Claude Code as it scales.
我们已经看到这种进展发生了很多次。例如，Claude Code 最初基于 Anthropic 员工和外部用户的反馈进行快速迭代。后来，我们添加了评估——首先用于简洁性和文件编辑等狭窄领域，然后用于过度工程等更复杂的行为。这些评估有助于识别问题、指导改进并专注于研究-产品合作。与生产监控、A/B 测试、用户研究等相结合，评估提供了随着 Claude Code 扩展而继续改进的信号。

Writing evals is useful at any stage in the agent lifecycle. Early on, evals force product teams to specify what success means for the agent, while later they help uphold a consistent quality bar.
在智能体生命周期的任何阶段编写评估都是有用的。在早期，评估迫使产品团队明确智能体的成功意味着什么，而后期它们有助于保持一致的质量标准。

Descript's agent helps users edit videos, so they built evals around three dimensions of a successful editing workflow: don't break things, do what I asked, and do it well. They evolved from manual grading to LLM graders with criteria defined by the product team and periodic human calibration, and now regularly run two separate suites for quality benchmarking and regression testing. The Bolt AI team started building evals later, after they already had a widely used agent. In 3 months, they built an eval system that runs their agent and grades outputs with static analysis, uses browser agents to test apps, and employs LLM judges for behaviors like instruction following.
Descript 的智能体帮助用户编辑视频，因此他们围绕成功编辑工作流程的三个维度构建了评估：不破坏东西、做我要求的事情、做好它。他们从手动评分演变为 LLM 评分器，标准由产品团队定义并定期人工校准，现在定期运行两个独立的套件进行质量基准测试和回归测试。Bolt AI 团队后来开始构建评估，此时他们已经有了一个广泛使用的智能体。在 3 个月内，他们构建了一个评估系统，运行他们的智能体并通过静态分析对输出进行评分，使用浏览器智能体测试应用程序，并使用 LLM 判断器来评估指令遵循等行为。

Some teams create evals at the start of development; others add them once at scale when evals become a bottleneck for improving the agent. Evals are especially useful at the start of agent development to explicitly encode expected behavior. Two engineers reading the same initial spec could come away with different interpretations on how the AI should handle edge cases. An eval suite resolves this ambiguity. Regardless of when they're created, evals help accelerate development.
一些团队在开发开始时创建评估；其他团队在规模扩大后添加评估，此时评估成为改进智能体的瓶颈。评估在智能体开发开始时特别有用，可以显式编码预期行为。两个工程师阅读相同的初始规范可能会对 AI 应如何处理边缘情况有不同的解释。评估套件解决了这种歧义。无论何时创建，评估都有助于加速开发。

Evals also shape how quickly you can adopt new models. When more powerful models come out, teams without evals face weeks of testing while competitors with evals can quickly determine the model's strengths, tune their prompts, and upgrade in days.
评估还影响你采用新模型的速度。当更强大的模型出现时，没有评估的团队面临数周的测试，而有评估的竞争对手可以快速确定模型的优势、调整提示并在几天内升级。

Once evals exist, you get baselines and regression tests for free: latency, token usage, cost per task, and error rates can be tracked on a static bank of tasks. Evals can also become the highest-bandwidth communication channel between product and research teams, defining metrics researchers can optimize against. Clearly, evals have wide-ranging benefits beyond tracking regressions and improvements. Their compounding value is easy to miss given that costs are visible upfront while benefits accumulate later.
一旦评估存在，你就会免费获得基线和回归测试：延迟、令牌使用、每任务成本和错误率可以在静态任务库上跟踪。评估还可以成为产品团队和研究团队之间最高带宽的沟通渠道，定义研究人员可以优化的指标。显然，评估除了跟踪回归和改进之外还有广泛的好处。它们的复合价值很容易被忽视，因为成本是前期可见的，而效益则是后期累积的。

## How to Evaluate AI Agents | 如何评估 AI 智能体

We see several common types of agents deployed at scale today, including coding agents, research agents, computer use agents, and conversational agents. Each type may be deployed across a wide variety of industries, but they can be evaluated using similar techniques. You don't need to invent an evaluation from scratch. The sections below describe proven techniques for several agent types. Use these methods as a foundation, then extend them to your domain.
我们看到今天大规模部署的几种常见类型的智能体，包括编码智能体、研究智能体、计算机使用智能体和对话智能体。每种类型可能部署在各种行业中，但可以使用类似的技术进行评估。你不需要从头开始发明评估。以下部分描述了几种智能体类型的经过验证的技术。以这些方法为基础，然后将其扩展到你的领域。

### Types of Graders for Agents | 智能体评分器的类型

Agent evaluations typically combine three types of graders: code-based, model-based, and human. Each grader evaluates some portion of either the transcript or the outcome. An essential component of effective evaluation design is to choose the right graders for the job.
智能体评估通常结合三种类型的评分器：基于代码、基于模型和基于人工。每个评分器评估记录或结果的某些部分。有效评估设计的一个基本组成部分是为工作选择合适的评分器。

Code-based graders
基于代码的评分器

| *Methods* | *Strengths* | *Weaknesses* |
| --- | --- | --- |
| • String match checks (exact, regex, fuzzy, etc) • Binary tests (fail-to-pass, pass-to-pass) • Static analysis (lint, type, security) • Outcome verification • Tool calls verification (tools used, parameters) • Transcript analysis (turns taken, token usage) | • Fast • Cheap • Objective • Reproducible • Easy to debug • Verify specific conditions | • Brittle to valid variations that don't match expected patterns exactly • Lacking in nuance • Limited for evaluating some more subjective tasks |

基于代码的评分器

| *方法* | *优势* | *劣势* |
| --- | --- | --- |
| • 字符串匹配检查（精确、正则、模糊等） • 二元测试（失败到通过、通过到通过） • 静态分析（lint、类型、安全） • 结果验证 • 工具调用验证（使用的工具、参数） • 记录分析（轮次、令牌使用） | • 快速 • 便宜 • 客观 • 可重现 • 易于调试 • 验证特定条件 | • 对不符合预期模式的有效变体很脆弱 • 缺乏细微差别 • 对于评估一些更主观的任务有限 |

Model-based graders
基于模型的评分器

| *Methods* | *Strengths* | *Weaknesses* |
| --- | --- | --- |
| - Rubric-based scoring - Natural language assertions - Pairwise comparison - Reference-based evaluation - Multi-judge consensus | - Flexible - Scalable - Captures nuance - Handles open-ended tasks - Handles freeform output | - Non-deterministic - More expensive than code - Requires calibration with human graders for accuracy |

基于模型的评分器

| *方法* | *优势* | *劣势* |
| --- | --- | --- |
| - 基于标准的评分 - 自然语言断言 - 成对比较 - 基于参考的评估 - 多判断者共识 | - 灵活 - 可扩展 - 捕捉细微差别 - 处理开放式任务 - 处理自由形式输出 | - 非确定性 - 比代码更昂贵 - 需要与人工评分器校准以确保准确性 |

Human graders
人工评分器

| *Methods* | *Strengths* | *Weaknesses* |
| --- | --- | --- |
| - SME review - Crowdsourced judgment - Spot-check sampling - A/B testing - Inter-annotator agreement | - Gold standard quality - Matches expert user judgment - Used to calibrate model-based graders | - Expensive - Slow - Often requires access to human experts at scale |

人工评分器

| *方法* | *优势* | *劣势* |
| --- | --- | --- |
| - SME 审核 - 众包判断 - 抽查 - A/B 测试 - 评估者间一致性 | - 黄金标准质量 - 匹配专家用户判断 - 用于校准基于模型的评分器 | - 昂贵 - 慢 - 通常需要大规模访问人工专家 |

For each task, scoring can be weighted (combined grader scores must hit a threshold), binary (all graders must pass), or a hybrid.
对于每个任务，评分可以是加权的（组合评分器分数必须达到阈值）、二元的（所有评分器必须通过）或混合的。

### Capability vs. Regression Evals | 能力评估与回归评估

*Capability or "quality" evals* ask "what can this agent do well?" They should start at a low pass rate, targeting tasks the agent struggles with and giving teams a hill to climb.
*能力或"质量"评估* 问"这个智能体能做好什么？"它们的通过率应该从低开始，针对智能体挣扎的任务，给团队一个攀登的山坡。

*Regression evals* ask "does the agent still handle all the tasks it used to?" and should have a nearly 100% pass rate. They protect against backsliding, as a decline in score signals that something is broken and needs to be improved. As teams hill-climb on capability evals, it's important to also run regression evals to make sure changes don't cause issues elsewhere.
*回归评估* 问"智能体是否仍然处理它以前处理的所有任务？"并且应该具有近 100% 的通过率。它们防止倒退，因为分数下降表明有问题需要改进。当团队在能力评估上攀登时，运行回归测试以确保更改不会在其他地方引起问题也很重要。

After an agent is launched and optimized, capability evals with high pass rates can "graduate" to become a regression suite that is run continuously to catch any drift. Tasks that once measured "can we do this at all?" then measure "can we still do this reliably?"
在智能体发布和优化后，高通过率的能力评估可以"毕业"成为回归套件，持续运行以捕获任何漂移。曾经衡量"我们能否做到这一点的任务？"现在衡量"我们能否仍然可靠地做到这一点？"

### Evaluating Coding Agents | 评估编码智能体

*Coding agents* write, test, and debug code, navigating codebases, and running commands much like a human developer. Effective evals for modern coding agents usually rely on well-specified tasks, stable test environments, and thorough tests for the generated code.
*编码智能体* 编写、测试和调试代码，导航代码库并运行命令，就像人类开发人员一样。现代编码智能体的有效评估通常依赖于明确定义的任务、稳定的测试环境和对生成代码的彻底测试。

Deterministic graders are natural for coding agents because software is generally straightforward to evaluate: Does the code run and do the tests pass? Two widely-used coding agent benchmarks, SWE-bench Verified and Terminal-Bench, follow this approach. SWE-bench Verified gives agents GitHub issues from popular Python repositories and grades solutions by running the test suite; a solution passes only if it fixes the failing tests without breaking existing ones. LLMs have progressed from 40% to >80% on this eval in just one year. Terminal-Bench takes a different track: it tests end-to-end technical tasks, such as building a Linux kernel from source or training an ML model.
确定性评分器对编码智能体来说很自然，因为软件通常很容易评估：代码是否运行，测试是否通过？两个广泛使用的编码智能体基准 SWE-bench Verified 和 Terminal-Bench 遵循这种方法。SWE-bench Verified 给代理来自流行 Python 存储库的 GitHub 问题，并通过运行测试套件来对解决方案进行评分；解决方案只有在修复失败的测试而不破坏现有测试的情况下才通过。LLM 在这个评估上在一年内从 40% 进展到 >80%。Terminal-Bench 采取不同的路径：它测试端到端的技术任务，例如从源代码构建 Linux 内核或训练 ML 模型。

Once you have a set of pass-or-fail tests for validating the key _outcomes_ of a coding task, it's often useful to also grade the transcript_. For instance, heuristics-based code quality rules can evaluate the generated code based on more than passing tests, and model-based graders with clear rubrics can assess behaviors like how the agent calls tools or interacts with the user.
一旦你有一组通过/失败测试来验证编码任务的关键结果，通常也对记录进行评分也很有用。例如，基于启发式的代码质量规则可以不仅仅根据通过测试来评估生成的代码，而具有明确标准的基于模型的评分器可以评估智能体如何调用工具或与用户交互等行为。

*Example: Theoretical evaluation for a coding agent*
*示例：编码智能体的理论评估*

Consider a coding task where the agent must fix an authentication bypass vulnerability. As shown in the illustrative YAML file below, one could evaluate this agent using both graders and metrics.
考虑一个编码任务，其中智能体必须修复身份验证绕过漏洞。如以下说明性 YAML 文件所示，可以使用评分器和指标来评估此智能体。

```
task:
  id: "fix-auth-bypass_1"
  desc: "Fix authentication bypass when password field is empty and ..."
  graders:
    - type: deterministic_tests
      required: [test_empty_pw_rejected.py, test_null_pw_rejected.py]
    - type: llm_rubric
      rubric: prompts/code_quality.md
    - type: static_analysis
      commands: [ruff, mypy, bandit]
    - type: state_check
      expect:
        security_logs: {event_type: "auth_blocked"}
    - type: tool_calls
      required:
        - {tool: read_file, params: {path: "src/auth/*"}}
        - {tool: edit_file}
        - {tool: run_tests}
  tracked_metrics:
    - type: transcript
      metrics:
        - n_turns
        - n_toolcalls
        - n_total_tokens
    - type: latency
      metrics:
        - time_to_first_token
        - output_tokens_per_sec
        - time_to_last_token
```

Note that this example showcases the full range of available graders for illustration. In practice, coding evaluations typically rely on unit tests for correctness verification and an LLM rubric for assessing overall code quality, with additional graders and metrics added only as needed.
请注意，此示例展示了可用评分器的全部范围以进行说明。在实践中，编码评估通常依赖单元测试进行正确性验证，并使用 LLM 标准来评估整体代码质量，仅根据需要添加额外的评分器和指标。

### Evaluating Conversational Agents | 评估对话智能体

*Conversational agents* interact with users in domains like support, sales, or coaching. Unlike traditional chatbots, they maintain state, use tools, and take actions mid-conversation. While coding and research agents can also involve many turns of interaction with the user, conversational agents present a distinct challenge: the quality of the interaction itself is part of what you're evaluating. Effective evals for conversational agents usually rely on verifiable end-state outcomes and rubrics that capture both task completion and interaction quality. Unlike most other evals, they often require a second LLM to simulate the user. We use this approach in our alignment auditing agents to stress-test models through extended, adversarial conversations.
*对话智能体* 在支持、销售或指导等领域与用户互动。与传统聊天机器人不同，它们维护状态、使用工具并在对话中采取行动。虽然编码和研究智能体也可以涉及与用户的多轮互动，但对话智能体提出了一个独特的挑战：互动本身的质量是你正在评估的一部分。对话智能体的有效评估通常依赖于可验证的最终状态结果和捕获任务完成和互动质量的标准。与大多数其他评估不同，它们通常需要第二个 LLM 来模拟用户。我们在我们的对齐审计智能体中使用这种方法，通过延长的对抗性对话对模型进行压力测试。

Success for conversational agents can be multidimensional: is the ticket resolved (state check), did it finish in <10 turns (transcript constraint), and was the tone appropriate (LLM rubric)? Two benchmarks that incorporate multidimensionality are 𝜏-Bench and its successor, τ2-Bench. These simulate multi-turn interactions across domains like retail support and airline booking, where one model plays a user persona while the agent navigates realistic scenarios.
对话智能体的成功可以是多维度的：工单是否已解决（状态检查），是否在 <10 轮内完成（记录约束），语气是否适当（LLM 标准）？两个结合多维度的基准是 𝜏-Bench 及其继任者 τ2-Bench。这些模拟跨零售支持和航班预订等领域的多轮互动，其中一个模型扮演用户角色，而智能体导航现实场景。

*Example: Theoretical evaluation for a conversational agent*
*示例：对话智能体的理论评估*

Consider a support task where the agent must handle a refund for a frustrated customer.
考虑一个支持任务，其中智能体必须为愤怒的客户处理退款。

```
graders:
  - type: llm_rubric
    rubric: prompts/support_quality.md
    assertions:
      - "Agent showed empathy for customer's frustration"
      - "Resolution was clearly explained"
      - "Agent's response grounded in fetch_policy tool results"
  - type: state_check
    expect:
      tickets: {status: resolved}
      refunds: {status: processed}
  - type: tool_calls
    required:
      - {tool: verify_identity}
      - {tool: process_refund, params: {amount: "<=100"}}
      - {tool: send_confirmation}
  - type: transcript
    max_turns: 10
tracked_metrics:
  - type: transcript
    metrics:
      - n_turns
      - n_toolcalls
      - n_total_tokens
  - type: latency
    metrics:
      - time_to_first_token
      - output_tokens_per_sec
      - time_to_last_token
```

As in our coding agent example, this task showcases multiple grader types for illustration. In practice, conversational agent evaluations typically use model-based graders to assess both communication quality and goal completion, because many tasks—like answering a question—may have multiple "correct" solutions.
与我们的编码智能体示例一样，此任务展示了多种评分器类型以进行说明。在实践中，对话智能体评估通常使用基于模型的评分器来评估沟通质量和目标完成，因为许多任务（如回答问题）可能有多个"正确"解决方案。

### Evaluating Research Agents | 评估研究智能体

*Research agents* gather, synthesize, and analyze information, then produce output like an answer or report. Unlike coding agents where unit tests provide binary pass/fail signals, research quality can only be judged relative to the task. What counts as "comprehensive," "well-sourced," or even "correct" depends on context: a market scan, due diligence for an acquisition, and a scientific report each require different standards.
*研究智能体* 收集、综合和分析信息，然后产生答案或报告等输出。与单元测试提供二元通过/失败信号的编码智能体不同，研究质量只能相对于任务来判断。什么算作"全面"、"来源良好"甚至"正确"取决于上下文：市场扫描、收购尽职调查和科学报告各自需要不同的标准。

Research evals face unique challenges: experts may disagree on whether a synthesis is comprehensive, ground truth shifts as reference content changes constantly, and longer, more open-ended outputs create more room for mistakes. A benchmark like BrowseComp, for example, tests whether AI agents can find needles in haystacks across the open web—questions designed to be easy to verify but hard to solve.
研究评估面临独特的挑战：专家可能不同意综合是否全面，随着参考内容不断变化，基本事实发生变化，更长、更开放的输出为错误创造更多空间。例如，像 BrowseComp 这样的基准测试 AI 智能体是否可以在开放网络中找到大海捞针——这些问题设计得易于验证但难以解决。

One strategy to build research agent evals is to combine grader types. Groundedness checks verify that claims are supported by retrieved sources, coverage checks define key facts a good answer must include, and source quality checks confirm the consulted sources are authoritative, rather than simply the first retrieved. For tasks with objectively correct answers ("What was Company X's Q3 revenue?"), exact match works. An LLM can flag unsupported claims and gaps in coverage, but also verify the open-ended synthesis for coherence and completeness.
构建研究智能体评估的一种策略是结合评分器类型。基础性检查验证声明是否得到检索来源的支持，覆盖检查定义良好答案必须包含的关键事实，源质量检查确认咨询的来源是权威的，而不仅仅是第一个检索到的。对于具有客观正确答案的任务（"X 公司第三季度收入是多少？"），精确匹配有效。LLM 可以标记不支持的声明和覆盖缺口，还可以验证开放式综合的连贯性和完整性。

Given the subjective nature of research quality, LLM-based rubrics should be frequently calibrated against expert human judgment to grade these agents effectively.
鉴于研究质量的主观性质，基于 LLM 的标准应该经常根据专家人工判断进行校准，以有效地对这些智能体进行评分。

### Computer Use Agents | 计算机使用智能体

*Computer use agents* interact with software through the same interface as humans—screenshots, mouse clicks, keyboard input, and scrolling—rather than through APIs or code execution. They can use any application with a graphical user interface (GUI), from design tools to legacy enterprise software. Evaluation requires running the agent in a real or sandboxed environment where it can use software applications, and checking whether it achieved the intended outcome. For instance, WebArena tests browser-based tasks, using URL and page state checks to verify the agent navigated correctly, along with backend state verification for tasks that modify data (confirming an order was actually placed, not just that the confirmation page appeared). OSWorld extends this to full operating system control, with evaluation scripts that inspect diverse artifacts after task completion: file system state, application configs, database contents, and UI element properties.
*计算机使用智能体* 通过与人类相同的界面与软件交互——屏幕截图、鼠标点击、键盘输入和滚动——而不是通过 API 或代码执行。它们可以使用任何具有图形用户界面（GUI）的应用程序，从设计工具到遗留企业软件。评估需要在真实或沙盒环境中运行智能体，使其可以使用软件应用程序，并检查它是否达到了预期结果。例如，WebArena 测试基于浏览器的任务，使用 URL 和页面状态检查来验证智能体是否正确导航，以及针对修改数据的任务的后端状态验证（确认订单实际上已放置，而不仅仅是确认页面出现）。OSWorld 将其扩展到完整的操作系统控制，评估脚本在任务完成后检查各种工件：文件系统状态、应用程序配置、数据库内容和 UI 元素属性。

Browser use agents require a balance between token efficiency and latency. DOM-based interactions execute quickly but consume many tokens, while screenshot-based interactions are slower but more token-efficient. For example, when asking Claude to summarize Wikipedia, it is more efficient to extract the text from the DOM. When finding a new laptop case on Amazon, it is more efficient to take screenshots (as extracting the entire DOM is token intensive). In our Claude for Chrome product, we developed evals to check that the agent was selecting the right tool for each context. This enabled us to complete browser based tasks faster and more accurately.
浏览器使用智能体需要在令牌效率和延迟之间取得平衡。基于 DOM 的交互执行迅速但消耗许多令牌，而基于屏幕截图的交互较慢但更令牌高效。例如，当要求 Claude 总结 Wikipedia 时，从 DOM 提取文本更有效。在 Amazon 上寻找新的笔记本电脑包时，截取屏幕截图更有效（因为提取整个 DOM 是令牌密集的）。在我们的 Chrome 版 Claude 产品中，我们开发了评估来检查智能体是否为每个上下文选择了正确的工具。这使我们能够更快、更准确地完成基于浏览器的任务。

### How to Think About Non-determinism in Evaluations for Agents | 如何考虑智能体评估中的非确定性

Regardless of agent type, agent behavior varies between runs, which makes evaluation results harder to interpret than they first appear. Each task has its own success rate—maybe 90% on one task, 50% on another—and a task that passed on one eval run might fail on the next. Sometimes, what we want to measure is how _often_ (what proportion of the trials) an agent succeeds for a task.
无论智能体类型如何，智能体行为在运行之间都有所不同，这使得评估结果比最初看起来更难解释。每个任务都有自己的成功率——也许一个任务 90%，另一个任务 50%——在一个评估运行中通过的任务可能在下一次失败。有时，我们要衡量的是智能体在任务中成功的频率（试验的比例）。

Two metrics help capture this nuance:
两个指标有助于捕捉这种细微差别：

*pass@k* measures the likelihood that an agent gets at least one correct solution in _k_ attempts. As k increases, pass@k score rises - more 'shots on goal' means higher odds of at least 1 success. A score of 50% pass@1 means that a model succeeds at half the tasks in the eval on its first try. In coding, we're often most interested in the agent finding the solution on the first try—pass@1. In other cases, proposing many solutions is valid as long as one works.
*pass@k* 衡量智能体在 _k_ 次尝试中至少获得一个正确解决方案的可能性。随着 k 的增加，pass@k 分数上升——更多的"射门"意味着至少 1 次成功的几率更高。50% pass@1 的分数意味着模型在第一次尝试中成功完成了评估中一半的任务。在编码中，我们通常最感兴趣的是智能体在第一次尝试中找到解决方案——pass@1。在其他情况下，只要一个有效，提出许多解决方案就是有效的。

*pass^k* measures the probability that _all k_ trials succeed. As _k_ increases, pass^k falls since demanding consistency across more trials is a harder bar to clear. If your agent has a 75% per-trial success rate and you run 3 trials, the probability of passing all three is (0.75)³ ≈ 42%. This metric especially matters for customer-facing agents where users expect reliable behavior every time.
*pass^k* 衡量所有 k 次试验都成功的概率。随着 k 的增加，pass^k 下降，因为在更多试验中要求一致性是一个更高的门槛。如果你的智能体有 75% 的试验成功率，你运行 3 次试验，通过所有三次的概率是 (0.75)³ ≈ 42%。此指标对于面向客户的智能体尤其重要，因为用户每次都期望可靠的行为。

![Image 3](https://www-cdn.anthropic.com/images/4zrzovbb/website/3ddac5be07a0773922ec9df06afec55922f8194a-4584x2580.png)

pass@k and pass^k diverge as trials increase. At k=1, they're identical (both equal the per-trial success rate). By k=10, they tell opposite stories: pass@k approaches 100% while pass^k falls to 0%.
pass@k 和 pass^k 随着试验的增加而分歧。在 k=1 时，它们相同（都等于试验成功率）。到 k=10 时，它们讲述相反的故事：pass@k 接近 100%，而 pass^k 降至 0%。

Both metrics are useful, and which to use depends on product requirements: pass@k for tools where one success matters, pass^k for agents where consistency is essential.
两个指标都有用，使用哪个取决于产品要求：pass@k 适用于一次成功很重要的工具，pass^k 适用于一致性至关重要的智能体。

## Going from Zero to One: A Roadmap to Great Evals for Agents | 从零到一：为智能体构建出色评估的路线图

This section lays out our practical, field-tested advice for going from no evals to evals you can trust. Think of this as a roadmap for eval-driven agent development: define success early, measure it clearly, and iterate continuously.
本节概述了我们从没有评估到可以信任的评估的实用、经过现场验证的建议。将此视为评估驱动的智能体开发的路线图：尽早定义成功、清楚地衡量它并持续迭代。

### Collect Tasks for the Initial Eval Dataset | 收集初始评估数据集的任务

*Step 0. Start early*
*步骤 0. 尽早开始*

We see teams delay building evals because they think they need hundreds of tasks. In reality, 20-50 simple tasks drawn from real failures is a great start. After all, in early agent development, each change to the system often has a clear, noticeable impact, and this large effect size means small sample sizes suffice. More mature agents may need larger, more difficult evals to detect smaller effects, but it's best to take the 80/20 approach in the beginning. Evals get harder to build the longer you wait. Early on, product requirements naturally translate into test cases. Wait too long and you're reverse-engineering success criteria from a live system.
我们看到团队推迟构建评估，因为他们认为需要数百个任务。实际上，从真实失败中提取的 20-50 个简单任务就是一个很好的开始。毕竟，在早期智能体开发中，对系统的每次更改通常都有明显的影响，这种大的效应大小意味着小样本量就足够了。更成熟的智能体可能需要更大、更难的评估来检测更小的效果，但最好在开始时采用 80/20 方法。你等待的时间越长，评估就越难构建。在早期，产品需求自然会转化为测试用例。等待太久，你就是在从实时系统中逆向工程成功标准。

*Step 1. Start with what you already test manually*
*步骤 1. 从你已经手动测试的内容开始*

Begin with the manual checks you run during development—the behaviors you verify before each release and common tasks end users try. If you're already in production, look at your bug tracker and support queue. Converting user-reported failures into test cases ensures your suite reflects actual usage; prioritizing by user impact helps you invest effort where it counts.
从你在开发过程中运行的手动检查开始——你在每次发布之前验证的行为和最终用户尝试的常见任务。如果你已经在生产中，请查看你的错误跟踪和支持队列。将用户报告的失败转换为测试用例可确保你的套件反映实际使用；按用户影响确定优先级有助于你在重要的地方投入精力。

*Step 2: Write unambiguous tasks with reference solutions*
*步骤 2：编写明确的任务并提供参考解决方案*

Getting task quality right is harder than it seems. A good task is one where two domain experts would independently reach the same pass/fail verdict. Could they pass the task themselves? If not, the task needs refinement. Ambiguity in task specifications becomes noise in metrics. The same applies to criteria for model-based graders: vague rubrics produce inconsistent judgments.
正确处理任务质量比看起来更难。一个好的任务是两个领域专家会独立得出相同的通过/失败判断的任务。他们自己能通过任务吗？如果不能，任务需要改进。任务规范中的歧义会成为指标中的噪音。这同样适用于基于模型的评分器的标准：模糊的标准会产生不一致的判断。

Each task should be passable by an agent that follows instructions correctly. This can be subtle. For instance, auditing Terminal-Bench revealed that if a task asks the agent to write a script but doesn't specify a filepath, and the tests assume a particular filepath for the script, the agent might fail through no fault of its own. Everything the grader checks should be clear from the task description; agents shouldn't fail due to ambiguous specs. With frontier models, a 0% pass rate across many trials (i.e. 0% pass@100) is most often a signal of a broken task, not an incapable agent, and a sign to double-check your task specification and graders. For each task, it's useful to create a reference solution: a known-working output that passes all graders. This proves that the task is solvable and verifies graders are correctly configured.
每个任务都应该可以被正确遵循指令的智能体通过。这可能是微妙的。例如，审计 Terminal-Bench 显示，如果任务要求智能体编写脚本但没有指定文件路径，而测试假设脚本的特定文件路径，智能体可能会因为不是自己的错误而失败。评分器检查的所有内容都应该从任务描述中清楚；智能体不应因模糊的规范而失败。对于前沿模型，在多次试验中 0% 的通过率（即 0% pass@100）通常是任务损坏的信号，而不是智能体无能，这是仔细检查任务规范和评分器的标志。对于每个任务，创建参考解决方案很有用：一个通过所有评分器的已知工作输出。这证明任务是可解的，并验证评分器配置正确。

*Step 3: Build balanced problem sets*
*步骤 3：构建平衡的问题集*

Test both the cases where a behavior _should_ occur and where it _shouldn't_. One-sided evals create one-sided optimization. For instance, if you only test whether the agent searches when it should, you might end up with an agent that searches for almost everything. Try to avoid class-imbalanced evals. We learned this firsthand when building evals for web search in Claude.ai. The challenge was preventing the model from searching when it shouldn't, while preserving its ability to do extensive research when appropriate. The team built evals covering both directions: queries where the model should search (like finding the weather) and queries where it should answer from existing knowledge (like "who founded Apple?"). Striking the right balance between undertriggering (not searching when it should) or overtriggering (searching when it shouldn't) was difficult, and took many rounds of refinements to both the prompts and the eval. As more example problems come up, we continue to add to evals to improve our coverage.
测试行为应该发生和不应该发生的情况。单方面的评估会创建单方面的优化。例如，如果你只测试智能体是否在应该的时候搜索，你最终可能会得到一个几乎搜索所有内容的智能体。尽量避免类别不平衡的评估。我们在为 Claude.ai 中的网络搜索构建评估时亲自学到了这一点。挑战是防止模型在不应该搜索时搜索，同时保留其在适当时进行广泛研究的能力。团队构建了涵盖两个方向的评估：模型应该搜索的查询（如查找天气）和模型应该从现有知识回答的查询（如"谁创立了 Apple？"）。在触发不足（应该搜索时不搜索）或过度触发（不应该搜索时搜索）之间取得正确的平衡是困难的，并且对提示和评估进行了多轮改进。随着更多示例问题的出现，我们继续添加到评估中以改善我们的覆盖范围。

### Design the Eval Harness and Graders | 设计评估工具和评分器

*Step 4: Build a robust eval harness with a stable environment*
*步骤 4：使用稳定的环境构建强大的评估工具*

It's essential that the agent in the eval functions roughly the same as the agent used in production, and the environment itself doesn't introduce further noise. Each trial should be "isolated" by starting from a clean environment. Unnecessary shared state between runs (leftover files, cached data, resource exhaustion) can cause correlated failures due to infrastructure flakiness rather than agent performance. Shared state can also artificially inflate performance. For example, in some internal evals we observed Claude gaining an unfair advantage on some tasks by examining the git history from previous trials. If multiple distinct trials fail because of the same limitation in the environment (like limited CPU memory), these trials are not independent because they're affected by the same factor, and the eval results become unreliable for measuring agent performance.
评估中的智能体功能与生产中使用的智能体大致相同，并且环境本身不会引入进一步的噪音，这一点至关重要。每个试验都应该通过从干净的环境开始来"隔离"。运行之间不必要的共享状态（剩余文件、缓存数据、资源耗尽）可能导致由于基础设施不稳定而非智能体性能的相关失败。共享状态也可能人为地提高性能。例如，在一些内部评估中，我们观察到 Claude 通过检查以前试验的 git 历史在某些任务上获得了不公平的优势。如果多个不同的试验因为环境中的相同限制（如有限的 CPU 内存）而失败，这些试验不是独立的，因为它们受到相同因素的影响，评估结果对于衡量智能体性能变得不可靠。

*Step 5: Design graders thoughtfully*
*步骤 5：仔细设计评分器*

As discussed above, great eval design involves choosing the best graders for the agent and the tasks. We recommend choosing deterministic graders where possible, LLM graders where necessary or for additional flexibility, and using human graders judiciously for additional validation.
如上所述，出色的评估设计涉及为智能体和任务选择最佳评分器。我们建议尽可能选择确定性评分器，在必要或需要额外灵活性时使用 LLM 评分器，并谨慎使用人工评分器进行额外验证。

There is a common instinct to check that agents followed very specific steps like a sequence of tool calls in the right order. We've found this approach too rigid and results in overly brittle tests, as agents regularly find valid approaches that eval designers didn't anticipate. So as not to unnecessarily punish creativity, it's often better to grade what the agent produced, not the path it took.
有一种常见的本能是检查智能体是否遵循了非常具体的步骤，比如按正确顺序的工具调用序列。我们发现这种方法太僵化，导致过于脆弱的测试，因为智能体经常找到评估设计师未预料到的有效方法。因此，为了不必要地惩罚创造力，通常最好评估智能体产生的结果，而不是它采取的路径。

For tasks with multiple components, build in partial credit. A support agent that correctly identifies the problem and verifies the customer but fails to process a refund is meaningfully better than one that fails immediately. It's important to represent this continuum of success in results.
对于具有多个组件的任务，建立部分功劳。正确识别问题并验证客户但未能处理退款的支持智能体比立即失败的智能体要好得多。重要的是在结果中表示这种成功的连续性。

Model grading often takes careful iteration to validate accuracy. LLM-as-judge graders should be closely calibrated with human experts to gain confidence that there is little divergence between the human grading and model grading. To avoid hallucinations, give the LLM a way out like providing an instruction to return "Unknown" when it doesn't have enough information. It can also help to create clear, structured rubrics to grade each dimension of a task, and then grade each dimension with an isolated LLM-as-judge rather than using one to grade all dimensions. Once the system is robust, it's sufficient to use human review only occasionally.
模型评分通常需要仔细迭代以验证准确性。LLM 作为判断的评分器应与人类专家密切校准，以获得人工评分和模型评分之间几乎没有分歧的信心。为避免幻觉，给 LLM 一条出路，比如提供指令在信息不足时返回"未知"。它还有助于创建清晰、结构化的标准来对任务的每个维度进行评分，然后使用独立的 LLM 作为判断对每个维度进行评分，而不是使用一个对所有维度进行评分。一旦系统强大，偶尔使用人工审查就足够了。

Some evaluations have subtle failure modes that result in low scores even with good agent performance, as the agent fails to solve tasks due to grading bugs, agent harness constraints, or ambiguity. Even sophisticated teams can miss these issues. For example, Opus 4.5 initially scored 42% on CORE-Bench, until an Anthropic researcher found multiple issues: rigid grading that penalized "96.12" when expecting "96.124991…", ambiguous task specs, and stochastic tasks that were impossible to reproduce exactly. After fixing bugs and using a less constrained scaffold, Opus 4.5's score jumped to 95%. Similarly, METR discovered several misconfigured tasks in their time horizon benchmark that asked agents to optimize to a stated score threshold, but the grading required exceeding that threshold. This penalized models like Claude for following the instructions, while models that ignored the stated goal received better scores. Carefully double-checking tasks and graders can help avoid these problems.
一些评估有微妙的失败模式，即使智能体表现良好也会导致低分，因为智能体由于评分错误、智能体工具约束或歧义而无法完成任务。即使是复杂的团队也可能错过这些问题。例如，Opus 4.5 最初在 CORE-Bench 上得分 42%，直到 Anthropic 研究人员发现多个问题：僵化的评分在预期"96.124991…"时惩罚"96.12"，模糊的任务规范，以及无法完全重现的随机任务。修复错误并使用较少约束的脚手架后，Opus 4.5 的分数跃升至 95%。同样，METR 在其时间范围基准测试中发现了几个配置错误的任务，这些任务要求智能体优化到声明的分数阈值，但评分要求超过该阈值。这惩罚了像 Claude 这样遵循指令的模型，而忽略声明目标的模型获得了更好的分数。仔细仔细检查任务和评分器可以帮助避免这些问题。

Make your graders resistant to bypasses or hacks. The agent shouldn't be able to easily "cheat" the eval. Tasks and graders should be designed so that passing genuinely requires solving the problem rather than exploiting unintended loopholes.
使你的评分器能够抵抗绕过或黑客攻击。智能体不应该能够轻易"作弊"评估。任务和评分器应该设计成通过真正需要解决问题，而不是利用意外的漏洞。

### Maintain and Use the Eval Long-term | 长期维护和使用评估

*Step 6: Check the transcripts*
*步骤 6：检查记录*

You won't know if your graders are working well unless you read the transcripts and grades from many trials. At Anthropic, we invested in tooling for viewing eval transcripts and we regularly take the time to read them. When a task fails, the transcript tells you whether the agent made a genuine mistake or whether your graders rejected a valid solution. It also often surfaces key details about agent and eval behavior.
除非你阅读多次试验的记录和分数，否则你不会知道你的评分器是否工作良好。在 Anthropic，我们投资了查看评估记录的工具，我们定期花时间阅读它们。当任务失败时，记录告诉你智能体是否犯了真正的错误，或者你的评分器是否拒绝了有效的解决方案。它还经常显示关于智能体和评估行为的关键细节。

Failures should seem fair: it's clear what the agent got wrong and why. When scores don't climb, we need confidence that it's due to agent performance and not the eval. Reading transcripts is how you verify that your eval is measuring what actually matters, and is a critical skill for agent development.
失败应该是公平的：很清楚智能体做错了什么以及为什么。当分数没有上升时，我们需要确信这是由于智能体性能而不是评估。阅读记录是你验证评估是否衡量真正重要的东西的方法，这是智能体开发的关键技能。

*Step 7: Monitor for capability eval saturation*
*步骤 7：监控能力评估饱和*

An eval at 100% tracks regressions but provides no signal for improvement. *Eval saturation* occurs when an agent passes all of the solvable tasks, leaving no room for improvement. For instance, SWE-Bench Verified scores started at 30% this year, and frontier models are now nearing saturation at >80%. As evals approach saturation, progress will also slow, as only the most difficult tasks remain. This can make results deceptive, as large capability improvements appear as small increases in scores. For example, the code review startup Qodo was initially unimpressed by Opus 4.5 because their one-shot coding evals didn't capture the gains on longer, more complex tasks. In response, they developed a new agentic eval framework, providing a much clearer picture of progress.
100% 的评估跟踪回归但不提供改进的信号。当智能体通过所有可解决的任务时，就会发生 *评估饱和*，没有改进的余地。例如，SWE-Bench Verified 分数今年从 30% 开始，前沿模型现在接近 >80% 的饱和。随着评估接近饱和，进展也会放缓，因为只有最困难的任务仍然存在。这可能会使结果具有欺骗性，因为大的能力改进表现为分数的小幅增加。例如，代码审查初创公司 Qodo 最初对 Opus 4.5 不满意，因为他们的一次性编码评估没有捕捉到在更长、更复杂的任务上的收益。作为回应，他们开发了一个新的智能体评估框架，提供了更清晰的进展情况。

As a rule, we do not take eval scores at face value until someone digs into the details of the eval and reads some transcripts. If grading is unfair, tasks are ambiguous, valid solutions are penalized, or the harness constrains the model, the eval should be revised.
作为规则，我们不会表面上看评估分数，直到有人深入研究评估的细节并阅读一些记录。如果评分不公平、任务模糊、有效解决方案受到惩罚或工具约束模型，则应修改评估。

*Step 8: Keep evaluation suites healthy long-term through open contribution and maintenance*
*步骤 8：通过开放贡献和维护保持评估套件的长期健康*

An eval suite is a living artifact which needs ongoing attention and clear ownership to remain useful.
评估套件是一个持续的生命，需要持续的关注和明确的所有权才能保持有用。

At Anthropic, we experimented with various approaches to eval maintenance. What proved most effective was establishing dedicated evals teams to own the core infrastructure, while domain experts and product teams contribute most eval tasks and run the evaluations themselves.
在 Anthropic，我们尝试了各种评估维护方法。证明最有效的是建立专门的评估团队来拥有核心基础设施，而领域专家和产品团队贡献大多数评估任务并自己运行评估。

For AI product teams, owning and iterating on evaluations should be as routine as maintaining unit tests. Teams can waste weeks on AI features that "work" in early testing but fail to meet unstated expectations that a well-designed eval would have surfaced early. Defining eval tasks is one of the best ways to stress-test whether the product requirements are concrete enough to start building.
对于 AI 产品团队，拥有和迭代评估应该像维护单元测试一样常规。团队可能会在早期测试中"工作"但在早期测试中未满足明确期望的 AI 功能上浪费数周，而精心设计的评估会在早期发现这些期望。定义评估任务是压力测试产品需求是否足够具体以开始构建的最佳方法之一。

We recommend practicing eval-driven development: build evals to define planned capabilities before agents can fulfill them, then iterate until the agent performs well. Internally, we often build features that work "well enough" today but are bets on what models can do in a few months. Capability evals that start at a low pass rate make this visible. When a new model drops, running the suite quickly reveals which bets paid off.
我们建议实践评估驱动开发：在智能体能够满足计划能力之前构建评估来定义计划能力，然后迭代直到智能体表现良好。在内部，我们经常构建今天"足够好"但赌模型几个月内能做的事情的功能。从低通过率开始的能力评估使这一点可见。当新模型出现时，运行套件快速揭示了哪些赌注成功了。

The people closest to product requirements and users are best positioned to define success. With current model capabilities, product managers, customer success managers, or salespeople can use Claude Code to contribute an eval task as a PR - let them! Or even better, actively enable them.
最接近产品需求和和用户的人最有资格定义成功。凭借当前的模型能力，产品经理、客户成功经理或销售人员可以使用 Claude Code 将评估任务作为 PR 贡献——让他们这样做吧！或者甚至更好，积极地让他们这样做。

![Image 4](https://www-cdn.anthropic.com/images/4zrzovbb/website/0db40cc0e14402222a179fc6297b9c8818e97c8a-4584x2580.png)

_The process of creating an effective evaluation._
_创建有效评估的过程。_

## How Evals Fit with Other Methods for a Holistic Understanding of Agents | 评估如何与其他方法相结合以全面了解智能体

Automated evaluations can be run against an agent in thousands of tasks without deploying to production or affecting real users. But this is just one of many ways to understand agent performance. A complete picture includes production monitoring, user feedback, A/B testing, manual transcript review, and systematic human evaluation.
自动化评估可以在数千个任务中针对智能体运行，而无需部署到生产或影响真实用户。但这只是了解智能体性能的众多方法之一。完整的图景包括生产监控、用户反馈、A/B 测试、手动记录审查和系统性的人工评估。

An overview of approaches for understanding AI agent performance
了解 AI 智能体性能的方法概述

| Method | Pros | Cons |
| --- | --- | --- |
| *Automated evals* _Running tests programmatically without real users_ | - Faster iteration - Fully reproducible - No user impact - Can run on every commit - Tests scenarios at scale without requiring a prod deployment | - Requires more upfront investment to build - Requires ongoing maintenance as product and model evolves to avoid drift - Can create false confidence if it doesn't match real usage patterns |

| 方法 | 优点 | 缺点 |
| --- | --- | --- |
| *自动化评估* _在没有真实用户的情况下以编程方式运行测试_ | - 更快的迭代 - 完全可重现 - 无用户影响 - 可以在每次提交时运行 - 在不需要生产部署的情况下大规模测试场景 | - 需要更多前期投资来构建 - 需要持续维护，因为产品和模型演变以避免漂移 - 如果不匹配真实使用模式，可能会产生虚假的信心 |

| *Production monitoring* _Tracking metrics and errors in live systems_ | - Reveals real user behavior at scale - Catches issues that synthetic evals miss - Provides ground truth on how agents actually perform | - Reactive, problems reach users before you know about them - Signals can be noisy - Requires investment in instrumentation - Lacks ground truth for grading |

| *生产监控* _跟踪实时系统中的指标和错误_ | - 大规模显示真实用户行为 - 捕获合成评估遗漏的问题 - 提供智能体实际表现的基本事实 | - 被动，问题在你知道之前就达到了用户 - 信号可能很嘈杂 - 需要投资仪表化 - 缺乏评分的基本事实 |

| *A/B testing* _Comparing variants with real user traffic_ | - Measures actual user outcomes (retention, task completion) - Controls for confounds - Scalable and systematic | - Slow, days or weeks to reach significance and requires sufficient traffic - Only tests changes you deploy - Less signal on the underlying "why" for changes in metrics without being able to thoroughly review the transcripts |

| *A/B 测试* _使用真实用户流量比较变体_ | - 衡量实际用户结果（保留、任务完成） - 控制混淆 - 可扩展和系统化 | - 慢，需要数天或数周才能达到显著性并需要足够的流量 - 只测试你部署的更改 - 在无法彻底审查记录的情况下，对指标变化的潜在"原因"信号较少 |

| *User feedback* _Explicit signals like thumbs-down or bug reports_ | - Surfaces problems you didn't anticipate - Comes with real examples from actual human users - The feedback often correlates with product goals | - Sparse and self-selected - Skews toward severe issues - Users rarely explain _why_ something failed - Not automated - Relying primarily on users to catch issues can have negative user impact |

| *用户反馈* _明确的信号，如竖起大拇指或错误报告_ | - 显示你没有预料到的问题 - 来自实际人类用户的真实示例 - 反馈通常与产品目标相关 | - 稀疏和自选 - 偏向严重问题 - 用户很少解释为什么某事失败 - 不自动化 - 主要依赖用户捕获问题可能会对用户产生负面影响 |

| *Manual transcript review* _Humans reading through agent conversations_ | - Builds intuition for failure modes - Catches subtle quality issues automated checks miss - Helps calibrate what "good" looks like and grasp details | - Time-intensive - Doesn't scale - coverage is inconsistent - Reviewer fatigue or different reviewers can affect the signal quality - Typically only gives qualitative signal rather than clear quantitative grading |

| *手动记录审查* _人类阅读智能体对话_ | - 建立失败模式的直觉 - 捕获自动检查遗漏的细微质量问题 - 帮助校准"好"的样子并掌握细节 | - 耗时 - 不可扩展 - 覆盖范围不一致 - 审查者疲劳或不同的审查者可能会影响信号质量 - 通常只提供定性信号而不是明确的定量评分 |

| *Systematic human studies* _Structured grading of agent outputs by trained raters_ | - Gold-standard quality judgements from multiple human raters - Handles subjective or ambiguous tasks - Provides signal for improving model-based graders | - Relatively expensive and slow turnaround - Hard to run frequently - Inter-rater disagreement requires reconciliation - Complex domains (legal, finance, healthcare) require human experts to conduct studies |

| *系统性人工研究* _训练有素的评估员对智能体输出进行结构化评分_ | - 来自多个人类评估员的黄金标准质量判断 - 处理主观或模糊的任务 - 为改进基于模型的评分器提供信号 | - 相对昂贵和缓慢的周转 - 难以频繁运行 - 评估者之间的分歧需要和解 - 复杂领域（法律、金融、医疗保健）需要人类专家进行研究 |

These methods map to different stages of agent development. Automated evals are especially useful pre-launch and in CI/CD, running on each agent change and model upgrade as the first line of defense against quality problems. Production monitoring kicks in post-launch to detect distribution drift and unanticipated real-world failures. A/B testing validates significant changes once you have sufficient traffic. User feedback and transcript review are ongoing practices to fill the gaps - triage feedback constantly, sample transcripts to read weekly, and dig deeper as needed. Reserve systematic human studies for calibrating LLM graders or evaluating subjective outputs where human consensus serves as the reference standard.
这些方法对应于智能体开发的不同阶段。自动化评估在发布前和 CI/CD 中特别有用，作为针对质量问题的第一道防线，在每个智能体更改和模型升级上运行。生产监控在发布后启动以检测分布漂移和意外的现实世界失败。A/B 测试在拥有足够流量后验证重大更改。用户反馈和记录审查是填补空白的不间断实践——不断分类反馈、每周抽样记录阅读，并根据需要深入挖掘。保留系统性人工研究用于校准 LLM 评分器或评估主观输出，其中人工共识作为参考标准。

![Image 5](https://www-cdn.anthropic.com/images/4zrzovbb/website/b77b8dbb7c2e57f063fbc8a087a853d5809b74b0-4584x2580.png)

Like the Swiss Cheese Model from safety engineering, no single evaluation layer catches every issue. With multiple methods combined, failures that slip through one layer are caught by another.
就像安全工程中的瑞士奶酪模型一样，没有单一的评估层能捕获每个问题。通过结合多种方法，穿过一层的失败会被另一层捕获。

The most effective teams combine these methods - automated evals for fast iteration, production monitoring for ground truth, and periodic human review for calibration.
最有效的团队结合这些方法——用于快速迭代的自动化评估、用于基本事实的生产监控以及用于校准的定期人工审查。

## Conclusion | 结论

Teams without evals get bogged down in reactive loops - fixing one failure, creating another, unable to distinguish real regressions from noise. Teams that invest early find the opposite: development accelerates as failures become test cases, test cases prevent regressions, and metrics replace guesswork. Evals give the whole team a clear hill to climb, turning "the agent feels worse" into something actionable. The value compounds, but only if you treat evals as a core component, not an afterthought.
没有评估的团队陷入被动循环——修复一个失败，创建另一个，无法区分真正的回归和噪音。早期投资的团队发现相反的情况：随着失败变成测试用例，测试用例防止回归，指标取代猜测，开发加速。评估给整个团队一个清晰的山坡要攀登，将"智能体感觉更糟"变成可操作的东西。价值是复合的，但只有当你将评估视为核心组件而不是事后想法时。

The patterns vary by agent type, but the fundamentals described here are constant. Start early and don't wait for the perfect suite. Source realistic tasks from the failures you see. Define unambiguous, robust success criteria. Design graders thoughtfully and combine multiple types. Make sure the problems are hard enough for the model. Iterate on the evaluations to improve their signal-to-noise ratio. Read the transcripts!
模式因智能体类型而异，但这里描述的基本原理是不变的。尽早开始，不要等待完美的套件。从你看到的失败中获取现实任务。定义明确、强大的成功标准。仔细设计评分器并结合多种类型。确保问题对模型来说足够困难。迭代评估以提高其信噪比。阅读记录！

AI agent evaluation is still a nascent, fast-evolving field. As agents take on longer tasks, collaborate in multi-agent systems, and handle increasingly subjective work, we will need to adapt our techniques. We'll keep sharing best practices as we learn more.
AI 智能体评估仍然是一个新兴的、快速发展的领域。随着智能体承担更长的任务、在多智能体系统中协作并处理越来越主观的工作，我们将需要调整我们的技术。我们将随着学习更多继续分享最佳实践。

### *Acknowledgements* | *致谢*

Written by Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe. We're also grateful to David Hershey, Gian Segato, Mike Merrill, Alex Shaw, Nicholas Carlini, Ethan Dixon, Pedram Navid, Jake Eaton, Alyssa Baum, Lina Tawfik, Karen Zhou, Alexander Bricken, Sam Kennedy, Robert Ying, and others for their contributions. Special thanks to the customers and partners we have learned from through collaborating on evals, including iGent, Cognition, Bolt, Sierra, Vals.ai, Macroscope, PromptLayer, Stripe, Shopify, the Terminal Bench team, and more. This work reflects the collective efforts of several teams who helped develop the practice of evaluations at Anthropic.
本文由 Mikaela Grace、Jeremy Hadfield、Rodrigo Olivares 和 Jiri De Jonghe 撰写。我们还感谢 David Hershey、Gian Segato、Mike Merrill、Alex Shaw、Nicholas Carlini、Ethan Dixon、Pedram Navid、Jake Eaton、Alyssa Baum、Lina Tawfik、Karen Zhou、Alexander Bricken、Sam Kennedy、Robert Ying 和其他人的贡献。特别感谢我们通过评估合作学习的客户和合作伙伴，包括 iGent、Cognition、Bolt、Sierra、Vals.ai、Macroscope、PromptLayer、Stripe、Shopify、Terminal Bench 团队等。这项工作反映了几个团队的集体努力，他们帮助在 Anthropic 开发了评估实践。

## Appendix: Eval Frameworks | 附录：评估框架

Several open-source and commercial frameworks can help teams implement agent evaluations without building infrastructure from scratch. The right choice depends on your agent type, existing stack, and whether you need offline evaluation, production observability, or both.
几个开源和商业框架可以帮助团队实现智能体评估，而无需从头开始构建基础设施。正确的选择取决于你的智能体类型、现有堆栈以及你是否需要离线评估、生产可观察性或两者兼而有之。

Harbor is designed for running agents in containerized environments, with infrastructure for running trials at scale across cloud providers and a standardized format for defining tasks and graders. Popular benchmarks like Terminal-Bench 2.0 ship through the Harbor registry, making it easy to run established benchmarks along with custom eval suites.
Harbor 旨在在容器化环境中运行智能体，具有跨云提供商大规模运行试验的基础设施，以及用于定义任务和评分器的标准化格式。流行的基准测试（如 Terminal-Bench 2.0）通过 Harbor 注册表发布，使其易于运行既定基准测试以及自定义评估套件。

Promptfoo is a lightweight, flexible, and open-source framework that focuses on declarative YAML configuration for prompt testing, with assertion types ranging from string matching to LLM-as-judge rubrics. We use a version of Promptfoo for many of our product evals.
Promptfoo 是一个轻量级、灵活和开源的框架，专注于用于提示测试的声明性 YAML 配置，断言类型从字符串匹配到 LLM 作为判断的标准。我们在许多产品评估中使用 Promptfoo 的版本。

Braintrust is a platform that combines offline evaluation with production observability and experiment tracking–useful for teams that need to both iterate during development and monitor quality in production. Its `autoevals` library includes pre-built scorers for factuality, relevance, and other common dimensions.
Braintrust 是一个将离线评估与生产可观察性和实验跟踪相结合的平台——对于需要在开发期间迭代并在生产中监控质量的团队很有用。其 `autoevals` 库包括事实性、相关性和其他常见维度的预构建评分器。

LangSmith offers tracing, offline and online evaluations, and dataset management with tight integration into the LangChain ecosystem. Langfuse provides similar capabilities as a self-hosted open-source alternative for teams with data residency requirements.
LangSmith 提供跟踪、离线和在线评估以及数据集管理，与 LangChain 生态系统紧密集成。Langfuse 作为具有数据驻留要求的团队的自托管开源替代方案，提供类似功能。

Many teams combine multiple tools, roll their own eval framework, or just use simple evaluation scripts as a starting point. We find that while frameworks can be a valuable way to accelerate progress and standardize, they're only as good as the eval tasks you run through them. It's often best to quickly pick a framework that fits your workflow, then invest your energy in the evals themselves by iterating on high-quality test cases and graders.
许多团队结合多个工具，推出自己的评估框架，或者只是使用简单的评估脚本作为起点。我们发现，虽然框架可能是加速进展和标准化的有价值的方式，但它们的好坏取决于你通过它们运行的评估任务。通常最好快速选择适合你工作流程的框架，然后通过迭代高质量的测试用例和评分器将精力投入到评估本身。
