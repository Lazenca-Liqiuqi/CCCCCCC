# The "think" tool: Enabling Claude to stop and think
# "Think"工具：让 Claude 能够停下来思考

**Published:** Jan 9, 2025
**发布日期：** 2025年1月9日

**Author:** Multiple
**作者：** 多位作者

---

As we continue to enhance Claude's complex problem-solving abilities, we've discovered a particularly effective approach: a "think" tool that creates dedicated space for structured thinking during complex tasks.
随着我们继续增强 Claude 解决复杂问题的能力，我们发现了一种特别有效的方法："think"工具，它在复杂任务期间为结构化思考创造专门的空间。

This simple yet powerful technique—which, as we'll explain below, is different from Claude's new "extended thinking" capability—has resulted in remarkable improvements in Claude's agentic tool use ability. This includes following policies, making consistent decisions, and handling multi-step problems, all with minimal implementation overhead.
这种简单而强大的技术——正如我们将在下面解释的，与 Claude 的新"扩展思考"能力不同——在 Claude 的代理工具使用能力方面带来了显著的改进。这包括遵循策略、做出一致的决策以及处理多步骤问题，所有这些都具有最小的实现开销。

In this post, we'll explore how to implement the "think" tool on different applications, sharing practical guidance for developers based on verified benchmark results.
在本文中，我们将探讨如何在不同应用程序上实现"think"工具，根据经过验证的基准测试结果与开发者分享实用指导。

### What is the "think" tool?
### 什么是"think"工具？

With the "think" tool, we're giving Claude the ability to include an additional thinking step—complete with its own designated space—as part of getting to its final answer.
通过"think"工具，我们让 Claude 能够包含一个额外的思考步骤——包括其自己的指定空间——作为获得最终答案的一部分。

While it sounds similar to extended thinking, it's a different concept. Extended thinking is all about what Claude does before it starts generating a response. With extended thinking, Claude deeply considers and iterates on its plan before taking action. The "think" tool is for Claude, once it starts generating a response, to add a step to stop and think about whether it has all the information it needs to move forward. This is particularly helpful when performing long chains of tool calls or in long multi-step conversations with the user.
虽然听起来与扩展思考相似，但它是一个不同的概念。扩展思考是关于 Claude 在开始生成响应之前做什么。通过扩展思考，Claude 在采取行动之前深入考虑并迭代其计划。"think"工具是针对 Claude 在开始生成响应后，添加一个步骤来停下来思考它是否有继续前进所需的所有信息。这在执行长链工具调用或与用户进行长多步骤对话时特别有帮助。

This makes the "think" tool more suitable for cases where Claude does not have all the information needed to formulate its response from the user query alone, and where it needs to process external information (e.g. information in tool call results). The reasoning Claude performs with the "think" tool is less comprehensive than what can be obtained with extended thinking, and is more focused on _new_ information that the model discovers.
这使得"think"工具更适合 Claude 单独从用户查询中没有足够信息来制定响应的情况，以及需要处理外部信息（例如，工具调用结果中的信息）的情况。Claude 使用"think"工具进行的推理不如扩展思考获得的推理全面，而更多地关注模型发现的_新_信息。

We recommend using extended thinking for simpler tool use scenarios like non-sequential tool calls or straightforward instruction following. Extended thinking is also useful for use cases, like coding, math, and physics, when you don't need Claude to call tools. The "think" tool is better suited for when Claude needs to call complex tools, analyze tool outputs carefully in long chains of tool calls, navigate policy-heavy environments with detailed guidelines, or make sequential decisions where each step builds on previous ones and mistakes are costly.
我们建议在更简单的工具使用场景中使用扩展思考，例如非顺序工具调用或直接遵循指令。当你不需要 Claude 调用工具时，扩展思考也适用于编码、数学和物理等用例。"think"工具更适合 Claude 需要调用复杂工具、在长链工具调用中仔细分析工具输出、在具有详细指导原则的策略繁重环境中导航，或做出顺序决策（其中每一步都建立在前一步之上且错误成本高昂）的情况。

Here's a sample implementation using the standard tool specification format that comes from τ-Bench:
以下是使用来自 τ-Bench 的标准工具规范格式的示例实现：

```
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

### Performance on τ-Bench
### τ-Bench 上的性能

We evaluated the "think" tool using τ-bench (tau-bench), a comprehensive benchmark designed to test a model's ability to use tools in realistic customer service scenarios, where the "think" tool is part of the evaluation's standard environment.
我们使用 τ-bench 评估了"think"工具，这是一个综合基准，旨在测试模型在现实客户服务场景中使用工具的能力，其中"think"工具是评估标准环境的一部分。

τ-bench evaluates Claude's ability to:
τ-bench 评估 Claude 的能力：

- Navigate realistic conversations with simulated users
- 与模拟用户进行现实对话
- Follow complex customer service agent policy guidelines consistently
- 一致地遵循复杂的客户服务代理策略指南
- Use a variety of tools to access and manipulate the environment database
- 使用各种工具访问和操作环境数据库

The primary evaluation metric used in τ-bench is pass^_k_, which measures the probability that all _k_ independent task trials are successful for a given task, averaged across all tasks. Unlike the pass@_k_ metric that is common for other LLM evaluations (which measures if at least one of _k_ trials succeeds), pass^_k_ evaluates consistency and reliability—critical qualities for customer service applications where consistent adherence to policies is essential.
τ-bench 中使用的主要评估指标是 pass^_k_，它衡量给定任务的所有 _k_ 次独立任务试验成功的概率，对所有任务取平均值。与其他 LLM 评估中常见的 pass@_k_ 指标（衡量 _k_ 次试验中至少一次成功）不同，pass^_k_ 评估一致性和可靠性——对于一致遵循策略至关重要的客户服务应用程序来说，这些是关键品质。

#### Performance Analysis
#### 性能分析

Our evaluation compared several different configurations:
我们的评估比较了几种不同的配置：

1. Baseline (no "think" tool, no extended thinking mode)
1. 基线（无"think"工具，无扩展思考模式）
2. Extended thinking mode alone
2. 仅扩展思考模式
3. "Think" tool alone
3. 仅"Think"工具
4. "Think" tool with optimized prompt (for airline domain)
4. "Think"工具和优化提示词（针对航空领域）

The results showed dramatic improvements when Claude 3.7 effectively used the "think" tool in both the "airline" and "retail" customer service domains of the benchmark:
结果表明，当 Claude 3.7 在基准的"航空"和"零售"客户服务领域有效使用"think"工具时，带来了显著的改进：

- __Airline domain__: The "think" tool with an optimized prompt achieved 0.570 on the pass^1 metric, compared to just 0.370 for the baseline—a 54% relative improvement;
- __航空领域__："think"工具和优化提示词在 pass^1 指标上达到了 0.570，而基线仅为 0.370——相对改进了 54%；
- __Retail domain__: The "think" tool alone achieves 0.812, compared to 0.783 for the baseline.
- __零售领域__：仅"think"工具就达到了 0.812，而基线为 0.783。

Claude 3.7 Sonnet's performance on the "Airline" domain of the Tau-Bench eval
Claude 3.7 Sonnet 在 Tau-Bench 评估的"航空"领域的性能

| Configuration | _k_=1 | _k_=2 | _k_=3 | _k_=4 | _k_=5 |
| --- | --- | --- | --- | --- | --- |
| "Think" + Prompt | 0.584 | 0.444 | 0.384 | 0.356 | 0.340 |
| "Think" | 0.404 | 0.254 | 0.186 | 0.140 | 0.100 |
| Extended thinking | 0.412 | 0.290 | 0.232 | 0.192 | 0.160 |
| Baseline | 0.332 | 0.206 | 0.148 | 0.116 | 0.100 |

| 配置 | _k_=1 | _k_=2 | _k_=3 | _k_=4 | _k_=5 |
| --- | --- | --- | --- | --- | --- |
| "Think" + 提示词 | 0.584 | 0.444 | 0.384 | 0.356 | 0.340 |
| "Think" | 0.404 | 0.254 | 0.186 | 0.140 | 0.100 |
| 扩展思考 | 0.412 | 0.290 | 0.232 | 0.192 | 0.160 |
| 基线 | 0.332 | 0.206 | 0.148 | 0.116 | 0.100 |

Evaluation results across four different configurations. Scores are proportions.
四种不同配置的评估结果。分数为比例。

The best performance in the airline domain was achieved by pairing the "think" tool with an optimized prompt that gives examples of the type of reasoning approaches to use when analyzing customer requests. Below is an example of the optimized prompt:
航空领域的最佳性能是通过将"think"工具与优化提示词配对实现的，该提示词给出了在分析客户请求时要使用的推理方法类型的示例。以下是优化提示词的示例：

```
## Using the think tool
## 使用 think 工具

Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to:
在采取任何行动或在收到工具结果后响应用户之前，使用 think 工具作为草稿纸来：
- List the specific rules that apply to the current request
- 列出适用于当前请求的具体规则
- Check if all required information is collected
- 检查是否收集了所有必需的信息
- Verify that the planned action complies with all policies
- 验证计划的操作是否符合所有策略
- Iterate over tool results for correctness
- 迭代检查工具结果的正确性

Here are some examples of what to iterate over inside the think tool:
以下是在 think 工具中要迭代检查的一些示例：

User wants to cancel flight ABC123
用户想要取消航班 ABC123
- Need to verify: user ID, reservation ID, reason
- 需要验证：用户 ID、预订 ID、原因
- Check cancellation rules:
- 检查取消规则：
  * Is it within 24h of booking?
  * 是否在预订后 24 小时内？
  * If not, check ticket class and insurance
  * 如果不是，检查机票等级和保险
- Verify no segments flown or are in the past
- 验证没有航班段已飞行或已过去
- Plan: collect missing info, verify rules, get confirmation
- 计划：收集缺失信息，验证规则，获得确认

User wants to book 3 tickets to NYC with 2 checked bags each
用户想要预订 3 张到纽约的机票，每张 2 件托运行李
- Need user ID to check:
- 需要用户 ID 来检查：
  * Membership tier for baggage allowance
  * 用于行李额度的会员等级
  * Which payments methods exist in profile
  * 个人资料中存在哪些支付方式
- Baggage calculation:
- 行李计算：
  * Economy class × 3 passengers
  * 经济舱 × 3 位乘客
  * If regular member: 1 free bag each → 3 extra bags = $150
  * 如果是普通会员：每人 1 件免费行李 → 3 件额外行李 = $150
  * If silver member: 2 free bags each → 0 extra bags = $0
  * 如果是银卡会员：每人 2 件免费行李 → 0 件额外行李 = $0
  * If gold member: 3 free bags each → 0 extra bags = $0
  * 如果是金卡会员：每人 3 件免费行李 → 0 件额外行李 = $0
- Payment rules to verify:
- 要验证的支付规则：
  * Max 1 travel certificate, 1 credit card, 3 gift cards
  * 最多 1 张旅行券、1 张信用卡、3 张礼品卡
  * All payment methods must be in profile
  * 所有支付方式必须在个人资料中
  * Travel certificate remainder goes to waste
  * 旅行券的余额将浪费
- Plan:
- 计划：
1. Get user ID
1. 获取用户 ID
2. Verify membership level for bag fees
2. 验证会员等级以获取行李费用
3. Check which payment methods in profile and if their combination is allowed
3. 检查个人资料中的支付方式及其组合是否允许
4. Calculate total: ticket price + any bag fees
4. 计算总计：机票价格 + 任何行李费用
5. Get explicit confirmation for booking
5. 获得预订的明确确认
```

What's particularly interesting is how the different approaches compared. Using the "think" tool with the optimized prompt achieved significantly better results over extended thinking mode (which showed similar performance to the unprompted "think" tool). Using the "think" tool alone (without prompting) improved performance over baseline, but still fell short of the optimized approach.
特别有趣的是不同方法的比较。使用"think"工具和优化提示词取得了比扩展思考模式显著更好的结果（扩展思考模式的性能与无提示的"think"工具相似）。仅使用"think"工具（无提示）的性能比基线有所提高，但仍未达到优化方法的水平。

The combination of the "think" tool with optimized prompting delivered the strongest performance by a significant margin, likely due to the high complexity of the airline policy part of the benchmark, where the model benefitted the most from being given examples of how to "think."
"think"工具和优化提示词的组合以显著优势提供了最强的性能，这可能是由于基准中航空策略部分的高复杂性，模型从给出如何"思考"的示例中受益最大。

In the retail domain, we also tested various configurations to understand the specific impact of each approach
在零售领域，我们还测试了各种配置以了解每种方法的具体影响

Performance of Claude 3.7 Sonnet on the "Retail" domain of the Tau-Bench eval
Claude 3.7 Sonnet 在 Tau-Bench 评估的"零售"领域的性能

| Configuration | _k_=1 | _k_=2 | _k_=3 | _k_=4 | _k_=5 |
| --- | --- | --- | --- | --- | --- |
| "Think" + no prompt | 0.812 | 0.735 | 0.685 | 0.650 | 0.626 |
| Extended thinking | 0.770 | 0.681 | 0.623 | 0.581 | 0.548 |
| Baseline | 0.783 | 0.695 | 0.643 | 0.607 | 0.583 |

| 配置 | _k_=1 | _k_=2 | _k_=3 | _k_=4 | _k_=5 |
| --- | --- | --- | --- | --- | --- |
| "Think" + 无提示 | 0.812 | 0.735 | 0.685 | 0.650 | 0.626 |
| 扩展思考 | 0.770 | 0.681 | 0.623 | 0.581 | 0.548 |
| 基线 | 0.783 | 0.695 | 0.643 | 0.607 | 0.583 |

Evaluation results across three different configurations. Scores are proportions.
三种不同配置的评估结果。分数为比例。

The "think" tool achieved the highest pass^1 score of 0.812 even without additional prompting. The retail policy is noticeably easier to navigate compared to the airline domain, and Claude was able to improve just by having a space to think without further guidance.
"think"工具即使没有额外的提示也达到了最高的 pass^1 分数 0.812。与航空领域相比，零售策略明显更容易导航，Claude 仅通过拥有一个思考空间而无需进一步指导就能改进。

#### Key Insights from τ-Bench Analysis
#### τ-Bench 分析的关键见解

Our detailed analysis revealed several patterns that can help you implement the "think" tool effectively:
我们的详细分析揭示了几个可以帮助你有效实现"think"工具的模式：

1. __Prompting matters significantly on difficult domains__. Simply making the "think" tool available might improve performance somewhat, but pairing it with optimized prompting yielded dramatically better results for difficult domains. However, easier domains may benefit from simply having access to "think."
1. __在困难领域中提示词非常重要__。简单地提供"think"工具可能会在一定程度上提高性能，但将其与优化提示词配对在困难领域中产生了显著更好的结果。然而，较简单的领域可能仅从拥有"think"访问权限中受益。
2. __Improved consistency across trials__. The improvements from using "think" were maintained for pass^k up to k=5, indicating that the tool helped Claude handle edge cases and unusual scenarios more effectively.
2. __跨试验的一致性改进__。使用"think"的改进在 pass^k 上一直保持到 k=5，表明该工具帮助 Claude 更有效地处理边缘情况和异常场景。

### Performance on SWE-Bench
### SWE-Bench 上的性能

A similar "think" tool was added to our SWE-bench setup when evaluating Claude 3.7 Sonnet, contributing to the achieved state-of-the-art score of 0.623. The adapted "think" tool definition is given below:
在评估 Claude 3.7 Sonnet 时，我们的 SWE-bench 设置中添加了类似的"think"工具，为达到的最先进分数 0.623 做出了贡献。调整后的"think"工具定义如下：

```
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or make any changes to the repository, but just log the thought. Use it when complex reasoning or brainstorming is needed. For example, if you explore the repo and discover the source of a bug, call this tool to brainstorm several unique ways of fixing the bug, and assess which change(s) are likely to be simplest and most effective. Alternatively, if you receive some test results, call this tool to brainstorm ways to fix the failing tests.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "Your thoughts."
      }
    },
    "required": ["thought"]
  }
}
```

Our experiments (_n_=30 samples with "think" tool, _n_=144 samples without) showed the isolated effects of including this tool improved performance by 1.6% on average (Welch's _t_-test: _t_(38.89) = 6.71, _p_ < .001, _d_ = 1.47).
我们的实验（_n_=30 个样本带"think"工具，_n_=144 个样本不带）表明，单独包含这个工具的效果是平均提高性能 1.6%（Welch _t_ 检验：_t_(38.89) = 6.71，_p_ < .001，_d_ = 1.47）。

### When to use the "think" tool
### 何时使用"think"工具

Based on these evaluation results, we've identified specific scenarios where Claude benefits most from the "think" tool:
基于这些评估结果，我们确定了 Claude 从"think"工具中受益最多的特定场景：

1. __Tool output analysis.__ When Claude needs to carefully process the output of previous tool calls before acting and might need to backtrack in its approach;
1. __工具输出分析。__当 Claude 需要在采取行动之前仔细处理先前工具调用的输出，并且可能需要回溯其方法时；
2. __Policy-heavy environments__. When Claude needs to follow detailed guidelines and verify compliance; and
2. __策略繁重的环境。__当 Claude 需要遵循详细的指导原则并验证合规性时；以及
3. __Sequential decision making__. When each action builds on previous ones and mistakes are costly (often found in multi-step domains).
3. __顺序决策。__当每个操作都建立在前一个操作之上且错误成本高昂时（常见于多步骤领域）。

## Implementation best practices
## 实现最佳实践

To get the most out of the "think" tool with Claude, we recommend the following implementation practices based on our τ-bench experiments.
为了充分利用 Claude 的"think"工具，我们根据我们的 τ-bench 实验推荐以下实现实践。

#### 1. Strategic prompting with domain-specific examples
#### 1. 使用特定领域示例的策略提示

The most effective approach is to provide clear instructions on when and how to use the "think" tool, such as the one used for the τ-bench airline domain. Providing examples tailored to your specific use case significantly improves how effectively the model uses the "think" tool:
最有效的方法是提供关于何时以及如何使用"think"工具的清晰说明，例如用于 τ-bench 航空领域的说明。提供针对特定用例定制的示例显著提高了模型使用"think"工具的有效性：

- The level of detail expected in the reasoning process;
- 推理过程中期望的详细程度；
- How to break down complex instructions into actionable steps;
- 如何将复杂的指令分解为可操作的步骤；
- Decision trees for handling common scenarios; and
- 处理常见场景的决策树；以及
- How to check if all necessary information has been collected.
- 如何检查是否已收集所有必要信息。

#### 2. Place complex guidance in the system prompt
#### 2. 将复杂的指导放在系统提示词中

We found that, when they were long and/or complex, including instructions about the "think" tool in the system prompt was more effective than placing them in the tool description itself. This approach provides broader context and helps the model better integrate the thinking process into its overall behavior.
我们发现，当关于"think"工具的说明很长和/或很复杂时，将它们放在系统提示词中比放在工具描述本身中更有效。这种方法提供了更广泛的上下文，并帮助模型更好地将思考过程整合到其整体行为中。

### When _not_ to use the "think" tool
### 何时_不_使用"think"工具

Whereas the "think" tool can offer substantial improvements, it is not applicable to all tool use use cases, and does come at the cost of increased prompt length and output tokens. Specifically, we have found the "think" tool does not offer any improvements in the following use cases:
虽然"think"工具可以提供显著的改进，但它并不适用于所有工具使用用例，并且确实会增加提示词长度和输出令牌的成本。具体来说，我们发现"think"工具在以下用例中没有提供任何改进：

1. __Non-sequential tool calls__. If Claude only needs to make a single tool call or multiple parallel calls to complete a task, there is unlikely to be any improvements from adding in "think."
1. __非顺序工具调用。__如果 Claude 只需要进行单个工具调用或多个并行调用来完成任务，添加"think"不太可能带来任何改进。
2. __Simple instruction following__. When there are not many constraints to which Claude needs to adhere, and its default behaviour is good enough, there are unlikely to be gains from additional "think"-ing.
2. __简单的指令遵循。__当 Claude 需要遵守的约束不多，并且其默认行为已经足够好时，额外的"思考"不太可能带来任何收益。

### Getting started
### 开始使用

The "think" tool is a straightforward addition to your Claude implementation that can yield meaningful improvements in just a few steps:
"think"工具是对你的 Claude 实现的直接补充，只需几个步骤就能产生有意义的改进：

1. __Test with agentic tool use scenarios.__ Start with challenging use cases—ones where Claude currently struggles with policy compliance or complex reasoning in long tool call chains.
1. __在代理工具使用场景中测试。__从具有挑战性的用例开始——Claude 当前在长工具调用链中难以遵守策略或进行复杂推理的用例。
2. __Add the tool definition__. Implement a "think" tool customized to your domain. It requires minimal code but enables more structured reasoning. Also consider including instructions on when and how to use the tool, with examples relevant to your domain to the system prompt.
2. __添加工具定义。__实现针对你的领域定制的"think"工具。它只需要最少的代码，但能够实现更结构化的推理。还要考虑在系统提示词中包含关于何时以及如何使用工具的说明，以及与你的领域相关的示例。
3. __Monitor and refine__. Watch how Claude uses the tool in practice, and adjust your prompts to encourage more effective thinking patterns.
3. __监控和改进。__观察 Claude 在实践中如何使用工具，并调整你的提示词以鼓励更有效的思考模式。

The best part is that adding this tool has minimal downside in terms of performance outcomes. It doesn't change external behavior unless Claude decides to use it, and doesn't interfere with your existing tools or workflows.
最好的部分是，添加这个工具在性能结果方面的 downside 最小。除非 Claude 决定使用它，否则它不会改变外部行为，并且不会干扰你现有的工具或工作流程。

### Conclusion
### 结论

Our research has demonstrated that the "think" tool can significantly enhance Claude 3.7 Sonnet's performance1 on complex tasks requiring policy adherence and reasoning in long chains of tool calls. "Think" is not a one-size-fits-all solution, but it offers substantial benefits for the correct use cases, all with minimal implementation complexity.
我们的研究表明，"think"工具可以显著增强 Claude 3.7 Sonnet 在需要策略遵守和长工具调用链推理的复杂任务上的性能1。"Think"不是一刀切的解决方案，但对于正确的用例提供了显著的好处，所有这些都具有最小的实现复杂性。

We look forward to seeing how you'll use the "think" tool to build more capable, reliable, and transparent AI systems with Claude.
我们期待看到你如何使用"think"工具与 Claude 一起构建更有能力、更可靠和更透明的 AI 系统。

1. While our τ-Bench results focused on the improvement of Claude 3.7 Sonnet with the "think" tool, our experiments show Claude 3.5 Sonnet (New) is also able to achieve performance gains with the same configuration as 3.7 Sonnet, indicating that this improvement generalizes to other Claude models as well.
1. 虽然我们的 τ-Bench 结果专注于 Claude 3.7 Sonnet 使用"think"工具的改进，但我们的实验表明 Claude 3.5 Sonnet（新版）也能够使用与 3.7 Sonnet 相同的配置实现性能提升，表明这种改进也适用于其他 Claude 模型。
