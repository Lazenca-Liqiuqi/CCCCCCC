# A postmortem of three recent issues | 三个近期问题的事后分析

This is a technical report on three bugs that intermittently degraded responses from Claude. Below we explain what happened, why it took time to fix, and what we're changing.

这是一份技术报告，关于三个间歇性降低 Claude 响应质量的 Bug。下面我们解释发生了什么、为什么修复耗时较长，以及我们正在做出哪些改变。

Between August and early September, three infrastructure bugs intermittently degraded Claude's response quality. We've now resolved these issues and want to explain what happened.

在8月到9月初期间，三个基础设施 Bug 间歇性地降低了 Claude 的响应质量。我们现在已经解决了这些问题，并想解释发生了什么。

In early August, a number of users began reporting degraded responses from Claude. These initial reports were difficult to distinguish from normal variation in user feedback. By late August, the increasing frequency and persistence of these reports prompted us to open an investigation that led us to uncover three separate infrastructure bugs.

8月初，一些用户开始报告 Claude 的响应质量下降。这些初步报告很难与用户反馈的正常变化区分开来。到8月下旬，这些报告的频率和持续性的增加促使我们展开调查，最终发现了三个独立的基础设施 Bug。

To state it plainly: We never reduce model quality due to demand, time of day, or server load. The problems our users reported were due to infrastructure bugs alone.

明确地说：我们绝不会因为需求、时段或服务器负载而降低模型质量。用户报告的问题完全是由基础设施 Bug 造成的。

We recognize users expect consistent quality from Claude, and we maintain an extremely high bar for ensuring infrastructure changes don't affect model outputs. In these recent incidents, we didn't meet that bar. The following postmortem explains what went wrong, why detection and resolution took longer than we would have wanted, and what we're changing to prevent similar future incidents.

我们认识到用户期望 Claude 提供一致的质量，我们对确保基础设施变更不影响模型输出设定了极高的标准。在最近的这些事件中，我们没有达到这个标准。以下的事后分析解释出了什么问题、为什么检测和解决的时间比我们希望的更长，以及我们正在做出什么改变来防止类似的未来事件。

We don't typically share this level of technical detail about our infrastructure, but the scope and complexity of these issues justified a more comprehensive explanation.

我们通常不会分享关于我们基础设施的这种技术细节，但这些问题的范围和复杂性值得一个更全面的解释。

## How we serve Claude at scale | 我们如何大规模提供 Claude 服务

We serve Claude to millions of users via our first-party API, Amazon Bedrock, and Google Cloud's Vertex AI. We deploy Claude across multiple hardware platforms, namely AWS Trainium, NVIDIA GPUs, and Google TPUs. This approach provides the capacity and geographic distribution necessary to serve users worldwide.

我们通过我们的官方 API、Amazon Bedrock 和 Google Cloud 的 Vertex AI 向数百万用户提供 Claude 服务。我们在多个硬件平台上部署 Claude，即 AWS Trainium、NVIDIA GPU 和 Google TPU。这种方法提供了服务全球用户所需的容量和地理分布。

Each hardware platform has different characteristics and requires specific optimizations. Despite these variations, we have strict equivalence standards for model implementations. Our aim is that users should get the same quality responses regardless of which platform serves their request. This complexity means that any infrastructure change requires careful validation across all platforms and configurations.

每个硬件平台都有不同的特征，需要特定的优化。尽管存在这些差异，我们对模型实现有严格的等效性标准。我们的目标是，无论哪个平台服务用户的请求，用户都应该获得相同质量的响应。这种复杂性意味着任何基础设施变更都需要在所有平台和配置上进行仔细验证。

## Timeline of events | 事件时间线

![Image 1: Illustrative timeline of events on the Claude API. Yellow: issue detected, Red: degradation worsened, Green: fix deployed.](https://www-cdn.anthropic.com/images/4zrzovbb/website/d707dfc2effceba608d04007bc776132a3e57838-3840x1800.png)

Claude API 上事件的时间线示意图。黄色：检测到问题，红色：质量下降恶化，绿色：修复部署。

The overlapping nature of these bugs made diagnosis particularly challenging. The first bug was introduced on August 5, affecting approximately 0.8% of requests made to Sonnet 4. Two more bugs arose from deployments on August 25 and 26.

这些 Bug 的重叠性质使得诊断特别具有挑战性。第一个 Bug 于8月5日引入，影响了约 0.8% 对 Sonnet 4 的请求。另外两个 Bug 出现于8月25日和26日的部署。

Although initial impacts were limited, a load balancing change on August 29 started to increase affected traffic. This caused many more users to experience issues while others continued to see normal performance, creating confusing and contradictory reports.

虽然初始影响有限，但8月29日的一次负载平衡变更开始增加受影响的流量。这导致更多用户遇到问题，而其他用户继续看到正常性能，从而产生了令人困惑和矛盾的报告。

## Three overlapping issues | 三个重叠问题

Below we describe the three bugs that caused the degradation, when they occurred, and how we resolved them:

下面我们描述导致质量下降的三个 Bug、它们发生的时间以及我们如何解决它们：

### Context window routing error | 上下文窗口路由错误

On August 5, some Sonnet 4 requests were misrouted to servers configured for the upcoming 1M token context window. This bug initially affected 0.8% of requests. On August 29, a routine load balancing change unintentionally increased the number of short-context requests routed to the 1M context servers. At the worst impacted hour on August 31, 16% of Sonnet 4 requests were affected.

8月5日，一些 Sonnet 4 请求被错误地路由到为即将到来的 1M 标记上下文窗口配置的服务器。这个 Bug 最初影响了 0.8% 的请求。8月29日，一次常规的负载平衡变更无意中增加了路由到 1M 上下文服务器的短上下文请求数量。在8月31日受影响最严重的小时，16% 的 Sonnet 4 请求受到影响。

Approximately 30% of Claude Code users who made requests during this period had at least one message routed to the wrong server type, resulting in degraded responses. On Amazon Bedrock, misrouted traffic peaked at 0.18% of all Sonnet 4 requests from August 12. Incorrect routing affected less than 0.0004% of requests on Google Cloud's Vertex AI between August 27 and September 16.

在此期间请求的 Claude Code 用户中，约 30% 至少有一条消息被路由到错误的服务器类型，导致响应质量下降。在 Amazon Bedrock 上，从8月12日开始，错误路由的流量峰值占所有 Sonnet 4 请求的 0.18%。在 Google Cloud 的 Vertex AI 上，8月27日至9月16日期间，错误路由影响了不到 0.0004% 的请求。

However, some users were affected more severely, as our routing is "sticky". This meant that once a request was served by the incorrect server, subsequent follow-ups were likely to be served by the same incorrect server.

然而，一些用户受到更严重的影响，因为我们的路由是"粘性的"。这意味着一旦请求由错误的服务器提供服务，后续的后续请求很可能由同一错误服务器提供服务。

**Resolution:** We fixed the routing logic to ensure short- and long-context requests were directed to the correct server pools. We deployed the fix on September 4. Rollout to our first-party platform and Google Cloud's Vertex AI was completed by September 16, and to AWS Bedrock by September 18.

**解决方案：** 我们修复了路由逻辑，以确保短上下文和长上下文请求被定向到正确的服务器池。我们在9月4日部署了修复。到我们的官方平台和 Google Cloud 的 Vertex AI 的推出在9月16日完成，到 AWS Bedrock 的推出在9月18日完成。

### Output corruption | 输出损坏

On August 25, we deployed a misconfiguration to the Claude API TPU servers that caused an error during token generation. An issue caused by a runtime performance optimization occasionally assigned a high probability to tokens that should rarely be produced given the context, for example producing Thai or Chinese characters in response to English prompts, or producing obvious syntax errors in code. A small subset of users that asked a question in English might have seen "สวัสดี" in the middle of the response, for example.

8月25日，我们向 Claude API TPU 服务器部署了一个错误配置，导致标记生成期间出现错误。由运行时性能优化引起的问题偶尔会给在给定上下文下很少应该产生的标记分配高概率，例如在响应英语提示时产生泰语或中文字符，或在代码中产生明显的语法错误。例如，一小部分用英语提问的用户可能会在响应中间看到"สวัสดี"。

This corruption affected requests made to Opus 4.1 and Opus 4 on August 25-28, and requests to Sonnet 4 August 25–September 2. Third-party platforms were not affected by this issue.

这种损坏影响了8月25日至28日期间对 Opus 4.1 和 Opus 4 的请求，以及8月25日至9月2日期间对 Sonnet 4 的请求。第三方平台未受此问题影响。

**Resolution:** We identified the issue and rolled back the change on September 2. We've added detection tests for unexpected character outputs to our deployment process.

**解决方案：** 我们在9月2日确认了问题并回滚了变更。我们已向我们的部署流程添加了意外字符输出的检测测试。

### Approximate top-k XLA:TPU miscompilation | 近似 top-k XLA:TPU 错误编译

On August 25, we deployed code to improve how Claude selects tokens during text generation. This change inadvertently triggered a latent bug in the XLA:TPU compiler, which has been confirmed to affect requests to Claude Haiku 3.5.

8月25日，我们部署了代码以改进 Claude 在文本生成期间选择标记的方式。这个变更无意中触发了 XLA:TPU 编译器中的一个潜在 Bug，该 Bug 已被确认影响对 Claude Haiku 3.5 的请求。

We also believe this could have impacted a subset of Sonnet 4 and Opus 3 on the Claude API. Third-party platforms were not affected by this issue.

我们还认为这可能影响了 Claude API 上 Sonnet 4 和 Opus 3 的一个子集。第三方平台未受此问题影响。

**Resolution:** We first observed the bug affecting Haiku 3.5 and rolled it back on September 4. We later noticed user reports of problems with Opus 3 that were compatible with this bug, and rolled it back on September 12. After extensive investigation we were unable to reproduce this bug on Sonnet 4 but decided to also roll it back out of an abundance of caution.

**解决方案：** 我们首先观察到影响 Haiku 3.5 的 Bug 并在9月4日回滚了它。我们后来注意到用户报告的 Opus 3 问题与此 Bug 兼容，并在9月12日回滚了它。经过广泛调查，我们无法在 Sonnet 4 上重现此 Bug，但出于谨慎考虑也决定回滚它。

Simultaneously, we have (a) been working with the XLA:TPU team on a fix for the compiler bug and (b) rolled out a fix to use exact top-k with enhanced precision. For details, see the deep dive below.

同时，我们（a）一直在与 XLA:TPU 团队合作修复编译器 Bug，（b）推出了使用精确 top-k 和增强精度的修复。有关详细信息，请参阅下面的深入分析。

## A closer look at the XLA compiler bug | 深入了解 XLA 编译器 Bug

To illustrate the complexity of these issues, here's how the XLA compiler bug manifested and why it proved particularly challenging to diagnose.

为了说明这些问题的复杂性，以下是 XLA 编译器 Bug 如何表现以及为什么证明特别难以诊断。

When Claude generates text, it calculates probabilities for each possible next word, then randomly chooses a sample from this probability distribution. We use "top-p sampling" to avoid nonsensical outputs—only considering words whose cumulative probability reaches a threshold (typically 0.99 or 0.999). On TPUs, our models run across multiple chips, with probability calculations happening in different locations. To sort these probabilities, we need to coordinate data between chips, which is complex.

当 Claude 生成文本时，它会计算每个可能的下一个单词的概率，然后从此概率分布中随机选择一个样本。我们使用"top-p 采样"来避免荒谬的输出——只考虑累积概率达到阈值的单词（通常为 0.99 或 0.999）。在 TPU 上，我们的模型跨多个芯片运行，概率计算发生在不同的位置。为了对这些概率进行排序，我们需要在芯片之间协调数据，这很复杂。

In December 2024, we discovered our TPU implementation would occasionally drop the most probable token when temperature was zero. We deployed a workaround to fix this case.

2024年12月，我们发现我们的 TPU 实现在温度为零时会偶尔丢弃最可能的标记。我们部署了一个解决方法来修复这种情况。

![Image 2: Code snippet of a December 2024 patch to work around the unexpected dropped token bug when temperature = 0.](https://www-cdn.anthropic.com/images/4zrzovbb/website/efee0d3d25f6b03cbfc57e70e0e364dcd8b82fe0-2000x500.png)

2024年12月的补丁代码片段，用于解决温度 = 0 时意外丢弃标记的 Bug。

The root cause involved mixed precision arithmetic. Our models compute next-token probabilities in bf16 (16-bit floating point). However, the vector processor is fp32-native, so the TPU compiler (XLA) can optimize runtime by converting some operations to fp32 (32-bit). This optimization pass is guarded by the `xla_allow_excess_precision` flag which defaults to true.

根本原因涉及混合精度算术。我们的模型使用 bf16（16位浮点）计算下一个标记的概率。然而，向量处理器是 fp32 原生的，因此 TPU 编译器（XLA）可以通过将某些操作转换为 fp32（32位）来优化运行时。此优化通道由 `xla_allow_excess_precision` 标志保护，该标志默认为 true。

This caused a mismatch: operations that should have agreed on the highest probability token were running at different precision levels. The precision mismatch meant they didn't agree on which token had the highest probability. This caused the highest probability token to sometimes disappear from consideration entirely.

这导致了一个不匹配：应该在最高概率标记上一致的操作在不同的精度级别运行。精度不匹配意味着它们在哪个标记具有最高概率上不一致。这导致最高概率标记有时完全从考虑中消失。

On August 26, we deployed a rewrite of our sampling code to fix the precision issues and improve how we handled probabilities at the limit that reach the top-p threshold. But in fixing these problems, we exposed a trickier one.

8月26日，我们部署了采样代码的重写以修复精度问题并改进我们在达到 top-p 阈值极限时处理概率的方式。但在修复这些问题的过程中，我们暴露了一个更棘手的问题。

![Image 3: Code snippet showing minimized reproducer merged as part of the August 11 change that root-caused the "bug" being worked around in December 2024; in reality, it's expected behavior of the `xla_allow_excess_precision` flag.](https://www-cdn.anthropic.com/images/4zrzovbb/website/6d10e58c0bd5fd7cb03dc0adc716cb1e4f039343-2000x2560.png)

代码片段显示作为8月11日变更一部分合并的最小化重现器，该变更根本分析了2024年12月绕过的"Bug"；实际上，这是 `xla_allow_excess_precision` 标志的预期行为。

Our fix removed the December workaround because we believed we'd solved the root cause. This led to a deeper bug in the approximate top-k operation—a performance optimization that quickly finds the highest probability tokens. This approximation sometimes returned completely wrong results, but only for certain batch sizes and model configurations. The December workaround had been inadvertently masking this problem.

我们的修复删除了12月的解决方法，因为我们相信我们已经解决了根本原因。这导致近似 top-k 操作（一种快速找到最高概率标记的性能优化）中的一个更深层 Bug。这种近似有时会返回完全错误的结果，但仅针对某些批量大小和模型配置。12月的解决方法无意中掩盖了这个问题。

![Image 4: Slack message showing reproducer of the underlying approximate top-k bug shared with the XLA:TPU engineers who developed the algorithm. The code returns correct results when run on CPUs.](https://www-cdn.anthropic.com/images/4zrzovbb/website/7e42db934d0e84ea40fc56b416ddb09b2097a5ff-2400x1404.png)

Slack 消息显示与开发该算法的 XLA:TPU 工程师共享的潜在近似 top-k Bug 的重现器。代码在 CPU 上运行时返回正确结果。

The bug's behavior was frustratingly inconsistent. It changed depending on unrelated factors such as what operations ran before or after it, and whether debugging tools were enabled. The same prompt might work perfectly on one request and fail on the next.

Bug 的行为令人沮丧地不一致。它根据不相关的因素而变化，例如在它之前或之后运行的操作，以及是否启用了调试工具。同一个提示可能在一个请求上完美工作，而在下一个请求上失败。

While investigating, we also discovered that the exact top-k operation no longer had the prohibitive performance penalty it once did. We switched from approximate to exact top-k and standardized some additional operations on fp32 precision. Model quality is non-negotiable, so we accepted the minor efficiency impact.

在调查过程中，我们还发现精确 top-k 操作不再具有曾经那样的过高性能惩罚。我们从近似 top-k 切换到精确 top-k，并将一些额外操作标准化为 fp32 精度。模型质量是不可妥协的，所以我们接受了轻微的效率影响。

## Why detection was difficult | 为什么检测很困难

Our validation process ordinarily relies on benchmarks alongside safety evaluations and performance metrics. Engineering teams perform spot checks and deploy to small "canary" groups first.

我们的验证过程通常依赖于基准测试以及安全评估和性能指标。工程团队首先进行抽查并部署到小型的"金丝雀"组。

These issues exposed critical gaps that we should have identified earlier. The evaluations we ran simply didn't capture the degradation users were reporting, in part because Claude often recovers well from isolated mistakes. Our own privacy practices also created challenges in investigating reports. Our internal privacy and security controls limit how and when engineers can access user interactions with Claude, in particular when those interactions are not reported to us as feedback. This protects user privacy but prevents engineers from examining the problematic interactions needed to identify or reproduce bugs.

这些问题暴露了我们本应更早识别的关键差距。我们运行的评估根本没有捕获用户报告的质量下降，部分原因是 Claude 通常能很好地从孤立的错误中恢复。我们自己的隐私实践也给调查报告带来了挑战。我们的内部隐私和安全控制限制了工程师访问用户与 Claude 交互的方式和时间，特别是当这些交互未作为反馈报告给我们时。这保护了用户隐私，但阻止了工程师检查识别或重现 Bug 所需的有问题的交互。

Each bug produced different symptoms on different platforms at different rates. This created a confusing mix of reports that didn't point to any single cause. It looked like random, inconsistent degradation.

每个 Bug 在不同平台上以不同速率产生不同的症状。这创建了一组令人困惑的报告，没有指向任何单一原因。它看起来像随机的、不一致的质量下降。

More fundamentally, we relied too heavily on noisy evaluations. Although we were aware of an increase in reports online, we lacked a clear way to connect these to each of our recent changes. When negative reports spiked on August 29, we didn't immediately make the connection to an otherwise standard load balancing change.

更根本的是，我们过于依赖嘈杂的评估。尽管我们意识到在线报告的增加，但我们缺乏一种清晰的方法将这些报告与我们最近的每个变更联系起来。当8月29日负面报告激增时，我们没有立即将其联系到否则标准的负载平衡变更。

## What we're changing | 我们正在做出的改变

As we continue to improve our infrastructure, we're also improving the way we evaluate and prevent bugs like those discussed above across all platforms where we serve Claude. Here's what we're changing:

在我们继续改进基础设施的同时，我们也在改进我们在所有提供 Claude 服务的平台上评估和防止上述 Bug 的方式。我们正在做出以下改变：

- **More sensitive evaluations:** To help discover the root cause of any given issue, we've developed evaluations that can more reliably differentiate between working and broken implementations. We'll keep improving these evaluations to keep a closer eye on model quality.

- **更敏感的评估：** 为了帮助发现任何给定问题的根本原因，我们开发了能够更可靠地区分工作和损坏实现的评估。我们将继续改进这些评估，以更密切地关注模型质量。

- **Quality evaluations in more places:** Although we run regular evaluations on our systems, we will run them continuously on true production systems to catch issues such as the context window load balancing error.

- **在更多地方进行质量评估：** 尽管我们在系统上运行定期评估，但我们将在真正的生产系统上持续运行它们，以捕获诸如上下文窗口负载平衡错误之类的问题。

- **Faster debugging tooling:** We'll develop infrastructure and tooling to better debug community-sourced feedback without sacrificing user privacy. Additionally, some bespoke tools developed here will be used to reduce the remediation time in future similar incidents, if those should occur.

- **更快的调试工具：** 我们将开发基础设施和工具来更好地调试社区来源的反馈，而不牺牲用户隐私。此外，这里开发的一些定制工具将用于在未来类似事件（如果发生）中减少修复时间。

Evals and monitoring are important. But these incidents have shown that we also need continuous signal from users when responses from Claude aren't up to the usual standard. Reports of specific changes observed, examples of unexpected behavior encountered, and patterns across different use cases all helped us isolate the issues.

评估和监控很重要。但这些事件表明，当 Claude 的响应未达到通常标准时，我们还需要来自用户的持续信号。观察到的特定变化报告、遇到的意外行为示例以及不同用例的模式都帮助我们隔离了问题。

It remains particularly helpful for users to continue to send us their feedback directly. You can use the `/bug` command in Claude Code or you can use the "thumbs down" button in the Claude apps to do so. Developers and researchers often create new and interesting ways to evaluate model quality that complement our internal testing. If you'd like to share yours, reach out to [feedback@anthropic.com](mailto:feedback@anthropic.com).

用户继续直接向我们发送反馈仍然特别有帮助。您可以在 Claude Code 中使用 `/bug` 命令，或使用 Claude 应用中的"向下拇指"按钮来执行此操作。开发人员和研究人员经常创建新的有趣的方法来评估模型质量，以补充我们的内部测试。如果您想分享您的方法，请联系 [feedback@anthropic.com](mailto:feedback@anthropic.com)。

We remain grateful to our community for these contributions.

我们仍然感谢社区为这些贡献做出的努力。

## Acknowledgments | 致谢

Written by Sam McAllister, with thanks to Stuart Ritchie, Jonathan Gray, Kashyap Murali, Brennan Saeta, Oliver Rausch, Alex Palcuie, and many others.

由 Sam McAllister 撰写，感谢 Stuart Ritchie、Jonathan Gray、Kashyap Murali、Brennan Saeta、Oliver Rausch、Alex Palcuie 以及许多其他人。

---

## Footnotes | 脚注

[1] XLA:TPU is the optimizing compiler that translates XLA High Level Optimizing language—often written using JAX—to TPU machine instructions.

[1] XLA:TPU 是优化编译器，将 XLA 高级优化语言（通常使用 JAX 编写）翻译成 TPU 机器指令。

[2] Our models are too large for single chips and are partitioned across tens of chips or more, making our sorting operation a distributed sort. TPUs (just like GPUs and Trainium) also have different performance characteristics than CPUs, requiring different implementation techniques using vectorized operations instead of serial algorithms.

[2] 我们的模型对于单个芯片来说太大，被分区到数十个或更多芯片上，使我们的排序操作成为分布式排序。TPU（就像 GPU 和 Trainium）也与 CPU 有不同的性能特征，需要使用向量化操作而不是串行算法的不同实现技术。

[3] We had been using this approximate operation because it yielded substantial performance improvements. The approximation works by accepting potential inaccuracies in the lowest probability tokens, which shouldn't affect quality—except when the bug caused it to drop the highest probability token instead.

[3] 我们一直在使用这个近似操作，因为它产生了显著的性能改进。近似的工作原理是接受最低概率标记的潜在不准确性，这不应该影响质量——除非 Bug 导致它丢弃最高概率标记。

[4] Note that the now-correct top-k implementation may result in slight differences in the inclusion of tokens near the top-p threshold, and in rare cases users may benefit from re-tuning their choice of top-p.

[4] 请注意，现在正确的 top-k 实现可能会导致 top-p 阈值附近标记的包含有细微差异，在极少数情况下，用户可能会受益于重新调整他们对 top-p 的选择。
