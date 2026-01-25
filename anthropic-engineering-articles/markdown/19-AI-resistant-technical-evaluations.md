# Designing AI Resistant Technical Evaluations
设计 AI 抗扰技术评估

What we learned from three iterations of a performance engineering take-home that Claude keeps beating.
我们从三次迭代性能工程师笔试中吸取的教训，Claude 不断击败这项测试。

---

_Written by Tristan Hume, a lead on Anthropic's performance optimization team. Tristan designed—and redesigned—the take-home test that's helped Anthropic hire dozens of performance engineers._
_本文作者 Tristan Hume 是 Anthropic 性能优化团队的负责人。Tristan 设计并重新设计了这项帮助 Anthropic 招募数十名性能工程师的笔试测试。_

Evaluating technical candidates becomes harder as AI capabilities improve. A take-home that distinguishes well between human skill levels today may be trivially solved by models tomorrow—rendering it useless for evaluation.
随着 AI 能力的提升，评估技术候选人变得更加困难。一项今天能很好地区分人类技能水平的笔试，明天可能就被模型轻松解决——使其失去评估价值。

Since early 2024, our performance engineering team has used a take-home test where candidates optimize code for a simulated accelerator. Over 1,000 candidates have completed it, and dozens now work here, including engineers who brought up our Trainium cluster and shipped every model since Claude 3 Opus.
自 2024 年初以来，我们的性能工程团队使用了一项笔试测试，候选人在其中为模拟加速器优化代码。超过 1,000 名候选人完成了这项测试，其中数十人现在在这里工作，包括负责搭建我们 Trainium 集群和发布从 Claude 3 Opus 以来每个模型的工程师。

But each new Claude model has forced us to redesign the test. When given the same time limit, Claude Opus 4 outperformed most human applicants. That still allowed us to distinguish the strongest candidates—but then Claude Opus 4.5 matched even those. Humans can still outperform models when given unlimited time, but under the constraints of the take-home test, we no longer had a way to distinguish between the output of our top candidates and our most capable model.
但每一个新的 Claude 模型都迫使我们重新设计测试。在给定相同时间限制的情况下，Claude Opus 4 的表现超过了大多数人类申请者。这仍然让我们能够区分最强的候选人——但随后 Claude Opus 4.5 甚至匹配了那些人。人类在无限时间内仍然可以超越模型，但在笔试测试的限制下，我们不再有办法区分我们顶级候选人的输出和我们最强大的模型的输出。

I've now iterated through three versions of our take-home in an attempt to ensure it still carries signal. Each time, I've learned something new about what makes evaluations robust to AI assistance and what doesn't.
现在我已经迭代了三个版本的笔试测试，试图确保它仍然具有区分度。每一次，我都学到了关于什么使评估对 AI 辅助具有鲁棒性、什么不具有的新东西。

This post describes the original take-home design, how each Claude model defeated it, and the increasingly unusual approaches I've had to take to ensure our test stays ahead of our top model's capabilities. While the work we do has evolved alongside our models, we still need more strong engineers—just increasingly creative ways to find them.
这篇文章描述了原始的笔试设计，每个 Claude 模型如何击败它，以及我必须采取的越来越不寻常的方法来确保我们的测试保持领先于我们顶级模型的能力。虽然我们的工作随着我们的模型一起发展，但我们仍然需要更多强大的工程师——只是需要越来越有创意的方法来找到他们。

To that end, we're releasing the original take-home as an open challenge, since with unlimited time the best human performance still exceeds what Claude can achieve. If you can best Opus 4.5, we'd love to hear from you—details are at the bottom of this post.
为此，我们正在将原始笔试作为公开挑战发布，因为在无限时间内，最好的人类表现仍然超过 Claude 所能达到的。如果你能超越 Opus 4.5，我们很乐意收到你的消息——详细信息在这篇文章的底部。

## The Origin of the Take-Home
笔试的起源

In November 2023, we were preparing to train and launch Claude Opus 3. We'd secured new TPU and GPU clusters, our large Trainium cluster was coming, and we were spending considerably more than we had in the past on accelerators, but we didn't have enough performance engineers for our new scale. I posted on Twitter asking people to email us, which brought in more promising candidates than we could evaluate through our standard interview pipeline, a process that consumes significant time for staff and candidates
2023 年 11 月，我们正准备训练和发布 Claude Opus 3。我们已经获得了新的 TPU 和 GPU 集群，我们的大型 Trainium 集群即将到来，我们在加速器上的花费比过去多得多，但我们没有足够的性能工程师来应对我们的新规模。我在 Twitter 上发帖要求人们给我们发电子邮件，这带来了比我们通过标准面试流程能够评估的更多有前途的候选人，这个过程为员工和候选人消耗了大量时间

We needed a way to evaluate candidates more efficiently. So, I took two weeks to design a take-home test that could adequately capture the demands of the role and identify the most capable applicants.
我们需要一种更有效地评估候选人的方法。因此，我花了两周时间设计了一项笔试测试，它能够充分捕捉角色的需求并识别最有能力的申请人。

### Design Goals
设计目标

Take-homes have a bad reputation. Usually they're filled with generic problems which engineers find boring, and which make for poor filters. My goal was different: create something genuinely engaging that would make candidates excited to participate and allow us to capture their technical skills at a high-level of resolution.
笔试测试名声不佳。通常它们充满了工程师觉得无聊的通用问题，并且作为筛选工具效果不佳。我的目标不同：创造一些真正令人兴奋的东西，让候选人有动力参与，并让我们能够以高分辨率捕捉他们的技术技能。

The format also offers advantages over live interviews for evaluating performance engineering skills:
这种格式在评估性能工程技能方面也比现场面试有优势：

__Longer time horizon:__ Engineers rarely face deadlines of less than an hour when coding. A 4-hour window (later reduced to 2 hours) better reflects the actual nature of the job. It's still shorter than most real tasks, but we need to balance that with how onerous it is.
__更长的时间跨度：__ 工程师在编码时很少面临少于一个小时的截止日期。4 小时的时间窗口（后来减少到 2 小时）更好地反映了工作的实际性质。它仍然比大多数真实任务短，但我们需要平衡这一点与它的繁重程度。

__Realistic environment:__ No one watching or expecting narration. Candidates work in their own editor without distraction.
__真实环境：__ 没有人观看或期望叙述。候选人在自己的编辑器中工作而不受干扰。

__Time for comprehension and tooling:__ Performance optimization requires understanding existing systems and sometimes building debugging tools. Both are hard to realistically evaluate in a normal 50 minute interview.
__理解和工具的时间：__ 性能优化需要理解现有系统，有时还需要构建调试工具。这两者在正常的 50 分钟面试中都很难现实地评估。

__Compatibility with AI assistance:__ Anthropic's general candidate guidance asks candidates to complete take-homes without AI unless indicated otherwise. For this take-home, we explicitly indicate otherwise.
__与 AI 辅助的兼容性：__ Anthropic 的一般候选人指导要求候选人在没有 AI 的情况下完成笔试测试，除非另有说明。对于这项笔试测试，我们明确表示相反。

Longer-horizon problems are harder for AI to solve completely, so candidates can use AI tools (as they would on the job) while still needing to demonstrate their own skills.
更长时间跨度的问题对 AI 来说更难完全解决，因此候选人可以使用 AI 工具（就像他们在工作中一样），同时仍然需要展示他们自己的技能。

Beyond these format-specific goals, I applied the same principles I use when designing any interview to make the take-home:
除了这些格式特定的目标之外，我应用了我在设计任何面试时使用的相同原则来使笔试测试：

__Representative of real work:__ The problem should give candidates a taste of what the job actually involves.
__代表真实工作：__ 问题应该让候选人体验工作的实际内容。

__High signal:__ The take-home should avoid problems that hinge on a single insight and ensure candidates have many chances to show their full abilities — leaving as little as possible to chance. It should also have a wide scoring distribution,and ensure enough depth that even strong candidates don't finish everything.
__高信噪比：__ 笔试测试应该避免依赖于单一洞察的问题，并确保候选人有多次机会展示他们的全部能力——尽可能少地留下运气成分。它还应该有一个广泛的评分分布，并确保足够的深度，即使是强大的候选人也无法完成所有事情。

__No specific domain knowledge:__ People with good fundamentals can learn specifics on the job. Requiring narrow expertise unnecessarily limits the candidate pool.
__没有特定的领域知识：__ 基础好的人可以在工作中学习具体细节。要求狭窄的专业知识会不必要地限制候选人库。

__Fun:__ Fast development loops, interesting problems with depth, and room for creativity.
__有趣：__ 快速的开发循环，有深度的有趣问题，以及创造力的空间。

### The Simulated Machine
模拟机器

I built a Python simulator for a fake accelerator with characteristics that resemble TPUs. Candidates optimize code running on this machine, using a hot-reloading Perfetto trace that shows every instruction, similar to the tooling we have on Trainium.
我为一个假的加速器构建了一个 Python 模拟器，其特征类似于 TPU。候选人优化在这台机器上运行的代码，使用一个热重载的 Perfetto 跟踪，显示每条指令，类似于我们在 Trainium 上的工具。

The machine includes features that make accelerator optimization interesting: manually managed scratchpad memory (unlike CPUs, accelerators often require explicit memory management), VLIW (multiple execution units running in parallel each cycle, requiring efficient instruction packing), SIMD (vector operations on many elements per instruction), and multicore (distributing work across cores).
该机器包括使加速器优化变得有趣的功能：手动管理的暂存内存（与 CPU 不同，加速器通常需要显式内存管理）、VLIW（多个执行单元每个周期并行运行，需要高效的指令打包）、SIMD（每条指令对多个元素的向量操作）和多核（跨核心分配工作）。

The task is a parallel tree traversal, deliberately not deep learning flavored, since most performance engineers hadn't worked on deep learning yet and could learn domain specifics on the job. The problem was inspired by branchless SIMD decision tree inference, a classical ML optimization challenge as a nod to the past, which only a few candidates had encountered before.
任务是一个并行树遍历，故意不是深度学习风格的，因为大多数性能工程师还没有从事深度学习工作，可以在工作中学习领域细节。这个问题受到无分支 SIMD 决策树推理的启发，这是一个经典的 ML 优化挑战，对过去的致敬，只有少数候选人以前遇到过。

Candidates start with a fully serial implementation and progressively exploit the machine's parallelism. The warmup is multicore parallelism, then candidates choose whether to tackle SIMD vectorization or VLIW instruction packing. The original version also included a bug that candidates needed to debug first, exercising their ability to build tooling.
候选人从一个完全串行的实现开始，逐步利用机器的并行性。热身是多核并行，然后候选人选择是处理 SIMD 向量化还是 VLIW 指令打包。原始版本还包括一个候选人需要首先调试的 bug，锻炼他们构建工具的能力。

## Early Results
早期结果

The initial take-home worked well. One person from the Twitter batch scored substantially higher than everyone else. He started in early February, two weeks after our first hires through the standard pipeline. The test proved predictive: He immediately began optimizing kernels and found a workaround for a launch-blocking compiler bug involving tensor indexing math overflowing 32 bits.
最初的笔试测试效果很好。来自 Twitter 批次的一个人比其他人都得分高得多。他在二月初开始，比我们通过标准流程雇佣的第一批人晚两周。测试证明是预测性的：他立即开始优化内核，并为一个阻碍发布的编译器 bug 找到了解决方法，该 bug 涉及张量索引数学溢出 32 位。

Over the next year and a half, about 1,000 candidates completed the take-home, and it helped us hire most of our current performance engineering team. It proved especially valuable for candidates with limited experience on paper: several of our highest-performing engineers came directly from undergrad but showed enough skill on the take-home for us to hire confidently.
在接下来的一年半中，大约 1,000 名候选人完成了笔试测试，它帮助我们雇佣了当前性能工程团队的大部分。它对纸上经验有限的候选人特别有价值：我们的几位表现最好的工程师直接来自本科，但在笔试测试中展示了足够的技能，让我们有信心雇佣。

Feedback was positive. Many candidates worked past the 4-hour limit because they were enjoying themselves. The strongest unlimited-time submissions included full optimizing mini-compilers and several clever optimizations I hadn't anticipated.
反馈是积极的。许多候选人在 4 小时限期后继续工作，因为他们乐在其中。最强的无限时间提交包括完整的优化小型编译器和几个我没有预料到的聪明优化。

### Then Claude Opus 4 Defeated It
然后 Claude Opus 4 击败了它

By May 2025, Claude 3.7 Sonnet had already crept up to the point where over 50% of candidates would have been better off delegating to Claude Code entirely. I then tested a pre-release version of Claude Opus 4 on the take-home. It came up with a more optimized solution than almost all humans did within the 4-hour limit.
到 2025 年 5 月，Claude 3.7 Sonnet 已经爬升到超过 50% 的候选人完全委托给 Claude Code 会更好的地步。然后我在笔试测试上测试了 Claude Opus 4 的预发布版本。它提出了一个在 4 小时限期内几乎比所有人都更优化的解决方案。

This wasn't my first interview defeated by a Claude model. I'd designed a live interview question in 2023 specifically because our questions at the time were based around common tasks that early Claude models had lots of knowledge of and so could solve easily. I tried to design a question that required more problem solving skill than knowledge, still based on a real (but niche) problem I'd solved at work. Claude 3 Opus beat part 1 of that question; Claude 3.5 Sonnet beat part 2. We still use it because our other live questions aren't AI-resistant either.
这不是我第一次被 Claude 模型击败的面试。我在 2023 年专门设计了一个现场面试问题，因为当时我们的问题基于早期 Claude 模型有很多知识的常见任务，所以可以轻松解决。我试图设计一个需要更多问题解决技能而不是知识的问题，仍然基于我在工作中解决的一个真实（但小众的）问题。Claude 3 Opus 击败了那个问题的第 1 部分；Claude 3.5 Sonnet 击败了第 2 部分。我们仍然使用它，因为我们的其他现场问题也不是 AI 抗扰的。

For the take-home, there was a straightforward fix. The problem had far more depth than anyone could explore in 4 hours, so I used Claude Opus 4 to identify where it started struggling. That became the new starting point for version 2. I wrote cleaner starter code, added new machine features for more depth, and removed multicore (which Claude had already solved, and which only slowed down development loops without adding signal).
对于笔试测试，有一个直接的修复方法。问题的深度远远超过任何人在 4 小时内可以探索的范围，所以我使用 Claude Opus 4 来识别它开始挣扎的地方。这成为版本 2 的新起点。我编写了更清晰的启动代码，添加了新的机器功能以增加深度，并删除了多核（Claude 已经解决了它，并且只会减慢开发循环而不增加信号）。

I also shortened the time limit from 4 hours to 2 hours. I'd originally chosen 4 hours based on candidate feedback preferring less risk of getting sunk if they got stuck for a bit on a bug or confusion, but the scheduling overhead was causing multi-week delays in our pipeline. Two hours is much easier to fit into a weekend.
我还将时间限制从 4 小时缩短到 2 小时。我最初选择 4 小时是基于候选人的反馈，他们更喜欢在遇到 bug 或困惑时卡住的风险更小，但调度开销在我们的流程中造成了数周的延迟。两小时更容易适应周末。

Version 2 emphasized clever optimization insights over debugging and code volume. It served us well—for several months.
版本 2 强调了聪明的优化洞察，而不是调试和代码量。它很好地为我们服务——几个月。

### Then Claude Opus 4.5 Defeated That
然后 Claude Opus 4.5 击败了那个

When I tested a pre-release Claude Opus 4.5 checkpoint, I watched Claude Code work on the problem for 2 hours, gradually improving its solution. It solved the initial bottlenecks, implemented all the common micro-optimizations, and met our passing threshold in under an hour.
当我测试 Claude Opus 4.5 的预发布检查点时，我看着 Claude Code 在问题上工作了 2 小时，逐渐改进其解决方案。它解决了最初的瓶颈，实现了所有常见的微优化，并在一小时内达到了我们的通过阈值。

Then it stopped, convinced it had hit an insurmountable memory bandwidth bottleneck. Most humans reach the same conclusion. But there are clever tricks that exploit the problem structure to work around that bottleneck. When I told Claude the cycle count it was possible to achieve, it thought for a while and found the trick. It then debugged, tuned, and implemented further optimizations. By the 2-hour mark, its score matched the best human performance within that time limit—and that human had made heavy use of Claude 4 with steering.
然后它停止了，确信它遇到了一个不可逾越的内存带宽瓶颈。大多数人都得出同样的结论。但是有一些聪明的技巧可以利用问题结构来绕过那个瓶颈。当我告诉 Claude 可以达到的周期计数时，它思考了一会儿并找到了那个技巧。然后它调试、调整并实现了进一步的优化。到了 2 小时标记，它的分数匹配了该时间限制内最好的人类表现——而且那个人类大量使用了带有引导的 Claude 4。

We tried it out in our internal test-time compute harness for more rigor and confirmed it could both beat humans in 2 hours and continue climbing with time. Post-launch we even improved our harness in a generic way and got a higher score.
我们在我们的内部测试时计算工具中尝试了它以获得更严格的结果，并确认它既可以在 2 小时内击败人类，也可以随着时间继续攀升。发布后，我们甚至以通用的方式改进了我们的工具并获得了更高的分数。

I had a problem. We were about to release a model where the best strategy on our take-home would be delegating to Claude Code.
我有一个问题。我们即将发布一个模型，其中在我们笔试测试上的最佳策略是委托给 Claude Code。

## Considering the Options
考虑选项

Some colleagues suggested banning AI assistance. I didn't want to do this. Beyond the enforcement challenges, I had a sense that given people continue to play a vital role in our work, I should be able to figure _out some_ way for them to distinguish themselves in a setting _with AI—_like they'd have on the job. I didn't want to give in yet to the idea that humans only have an advantage on tasks longer than a few hours.
一些同事建议禁止 AI 辅助。我不想这样做。除了执行挑战之外，我有一种感觉，鉴于人们继续在我们的工作中发挥重要作用，我应该能够想出某种方式让他们在 _有 AI 的环境中_ 区分自己——就像他们在工作中那样。我还不想屈服于人类只在超过几小时的任务上有优势的想法。

Others suggested raising the bar to "substantially outperform what Claude Code achieves alone." The concern here was that Claude works fast. Humans typically spend half the 2 hours reading and understanding the problem before they start optimizing. A human trying to steer Claude would likely be constantly behind, understanding what Claude did only after the fact. The dominant strategy might become sitting back and watching.
其他人建议将标准提高到"大幅超越 Claude Code 单独实现的效果"。这里的担忧是 Claude 工作得很快。人类通常在开始优化之前花费 2 小时的一半来阅读和理解问题。试图引导 Claude 的人类可能会不断落后，只在事后理解 Claude 做了什么。主导策略可能变成坐下来观看。

Nowadays performance engineers at Anthropic still have lots of work to do, but it looks more like tough debugging, systems design, performance analysis, figuring out how to verify the correctness of our systems, and figuring out how to make Claude's code simpler and more elegant. Unfortunately these things are tough to test in an objective way without a lot of time or common context. It's always been hard to design interviews that represent the job, but now it's harder than ever.
现在 Anthropic 的性能工程师仍然有很多工作要做，但它看起来更像是艰难的调试、系统设计、性能分析、弄清楚如何验证我们系统的正确性，以及弄清楚如何使 Claude 的代码更简单和更优雅。不幸的是，这些事情在没有大量时间或共同上下文的情况下很难以客观的方式测试。设计代表工作的面试一直很难，但现在比以往任何时候都难。

But I also worried if I invested in designing a new take-home, either Claude Opus 4.5 would solve that too, or it would become so challenging that it would be impossible for humans to complete in two hours.
但我也担心如果我投入设计一个新的笔试测试，Claude Opus 4.5 也会解决它，或者它会变得如此具有挑战性以至于人类不可能在两小时内完成。

### Attempt 1: A Different Optimization Problem
尝试 1：一个不同的优化问题

I realized Claude could help me implement whatever I designed quickly, which motivated me to try developing a harder take-home. I chose a problem based on one of the trickier kernel optimizations I'd done at Anthropic: an efficient data transposition on 2D TPU registers while avoiding bank conflicts. I distilled it into a simpler problem on a simulated machine and had Claude implement the changes in under a day.
我意识到 Claude 可以帮助我快速实现我设计的任何东西，这激励我尝试开发一个更难的笔试测试。我选择了一个基于我在 Anthropic 做过的更棘手的内核优化之一的问题：在 2D TPU 寄存器上进行高效数据转置，同时避免 bank 冲突。我将它提炼成模拟机器上的一个更简单的问题，并让 Claude 在一天内实现了更改。

Claude Opus 4.5 found a great optimization I hadn't even thought of. Through careful analysis, it realized it could transpose the entire computation rather than figuring out how to transpose the data, and it rewrote the whole program accordingly.
Claude Opus 4.5 发现了一个我甚至没有想到的伟大优化。通过仔细分析，它意识到它可以转置整个计算，而不是弄清楚如何转置数据，并相应地重写了整个程序。

In my real case, this wouldn't have worked, so I patched the problem to remove that approach. Claude then made progress but couldn't find the most efficient solution. It seemed like I had my new problem, now I just had to hope human candidates could get it fast enough. But I had some nagging doubt, so I double-checked using Claude Code's "ultrathink" feature with longer thinking budgets ... and it solved it. It even knew the tricks for fixing bank conflicts.
在我的真实情况下，这行不通，所以我修补了问题以删除该方法。Claude 然后取得了一些进展，但无法找到最有效的解决方案。似乎我有我的新问题，现在我只需要希望人类候选人能够足够快地得到它。但我有一些令人烦恼的怀疑，所以我使用 Claude Code 的"ultrathink"功能进行了更长时间的思考预算双重检查……它解决了它。它甚至知道修复 bank 冲突的技巧。

In hindsight, this wasn't the right problem to try. Engineers across many platforms have struggled with data transposition and bank conflicts, so Claude has substantial training data to draw on. While I'd found my solution from first principles, Claude could draw on a larger toolbox of experience.
事后看来，这不是尝试的正确问题。跨许多平台的工程师一直在努力解决数据转置和 bank 冲突问题，因此 Claude 有大量的训练数据可供借鉴。虽然我从第一性原理找到了我的解决方案，但 Claude 可以利用更大的经验工具箱。

### Attempt 2: Going Weirder
尝试 2：变得更奇怪

I needed a problem where human reasoning could win over Claude's larger experience base: something sufficiently out of distribution. Unfortunately, this conflicted with my goal of being recognizably like the job.
我需要一个人类推理可以战胜 Claude 更大经验基础的问题：一些足够超出分布的东西。不幸的是，这与我使它看起来像工作的目标冲突。

I thought about the most unusual optimization problems I'd enjoyed and landed on Zachtronics games. These programming puzzle games use unusual, highly constrained instruction sets that force you to program in unconventional ways. For example, in Shenzhen I/O, programs are split across multiple communicating chips that each hold only about 10 instructions with one or two state registers. Clever optimization often involves encoding state into the instruction pointer or branch flags.
我想起了我最享受的最不寻常的优化问题，并想到了 Zachtronics 游戏。这些编程解谜游戏使用不寻常的、高度受限的指令集，迫使你以非传统的方式编程。例如，在 Shenzhen I/O 中，程序被分割到多个通信芯片上，每个芯片只持有大约 10 条指令和一两个状态寄存器。聪明的优化通常涉及将状态编码到指令指针或分支标志中。

I designed a new take-home consisting of puzzles using a tiny, heavily constrained instruction set, optimizing solutions for minimal instruction count. I implemented one medium-hard puzzle and tested it on Claude Opus 4.5. It failed. I filled out more puzzles and had colleagues verify that people less steeped in the problem than me could still outperform Claude.
我设计了一个新的笔试测试，由使用微小的、高度受限的指令集的解谜组成，优化解决方案以获得最少的指令计数。我实现了一个中等难度的解谜并在 Claude Opus 4.5 上测试了它。它失败了。我填充了更多的解谜，并让同事验证不那么深入问题的人仍然可以超越 Claude。

Unlike Zachtronics games, I intentionally provided no visualization or debugging tools. The starter code only checks whether solutions are valid. Building debugging tools is part of what's being tested: you can either insert well-crafted print statements or ask a coding model to generate an interactive debugger in a few minutes. Judgment about how to invest in tooling is part of the signal.
与 Zachtronics 游戏不同，我故意没有提供可视化或调试工具。启动代码只检查解决方案是否有效。构建调试工具是正在测试的一部分：你可以插入精心制作的 print 语句，或者要求编码模型在几分钟内生成交互式调试器。关于如何投资工具的判断是信号的一部分。

I'm reasonably happy with the new take-home. It might have lower variance than the original because it comprises more independent sub-problems. Early results are promising: scores correlate well with the caliber of candidates' past work, and one of my most capable colleagues scored higher than any candidate so far.
我对新的笔试测试相当满意。它的方差可能比原始版本低，因为它包含更多独立的子问题。早期结果是有希望的：分数与候选人过去工作的水平相关，我最有能力的同事之一的得分比迄今为止任何候选人都高。

I'm still sad to have given up the realism and varied depth of the original. But realism may be a luxury we no longer have. The original worked because it resembled real work. The replacement works because it simulates novel work.
我仍然很伤心放弃了原始的现实性和多样化的深度。但现实性可能是我们不再拥有的奢侈品。原始版本有效是因为它类似于真实工作。替代版本有效是因为它模拟新颖的工作。

## An Open Challenge
一个公开挑战

We're releasing the original take-home for anyone to try with unlimited time. Human experts retain an advantage over current models at sufficiently long time horizons. The fastest human solution ever submitted substantially exceeds what Claude has achieved even with extensive test-time compute.
我们正在发布原始的笔试测试，供任何人用无限时间尝试。人类专家在足够长的时间范围内仍然保持对当前模型的优势。有史以来提交的最快人类解决方案大大超过了 Claude 即使通过大量测试时计算所达到的效果。

The released version starts from scratch (like version 1) but uses version 2's instruction set and single-core design, so cycle counts are comparable to version 2.
发布的版本从头开始（像版本 1），但使用版本 2 的指令集和单核设计，因此周期计数与版本 2 相当。

Performance benchmarks (measured in clock cycles from the simulated machine):
性能基准测试（从模拟机器测量的时钟周期）：

- __2164 cycles:__ Claude Opus 4 after many hours in the test-time compute harness
- __2164 周期：__ Claude Opus 4 在测试时计算工具中工作许多小时后
- __1790 cycles:__ Claude Opus 4.5 in a casual Claude Code session, approximately matching the best human performance in 2 hours
- __1790 周期：__ Claude Opus 4.5 在随意的 Claude Code 会话中，大约匹配 2 小时内最好的人类表现
- __1579 cycles:__ Claude Opus 4.5 after 2 hours in our test-time compute harness
- __1579 周期：__ Claude Opus 4.5 在我们的测试时计算工具中 2 小时后
- __1548 cycles:__ Claude Sonnet 4.5 after many more than 2 hours of test-time compute
- __1548 周期：__ Claude Sonnet 4.5 经过超过 2 小时的测试时计算
- __1487 cycles:__ Claude Opus 4.5 after 11.5 hours in the harness
- __1487 周期：__ Claude Opus 4.5 在工具中 11.5 小时后
- __1363 cycles:__ Claude Opus 4.5 in an improved test time compute harness after many hours
- __1363 周期：__ Claude Opus 4.5 在改进的测试时计算工具中经过许多小时后

Download it on GitHub. If you optimize below 1487 cycles, beating Claude's best performance at launch, email us at performance-recruiting@anthropic.com with your code and a resume.
在 GitHub 上下载它。如果你优化到低于 1487 周期，击败发布时 Claude 的最佳表现，请将你的代码和简历发送至 performance-recruiting@anthropic.com。

Or you can apply through our typical process, which uses our (now) Claude-resistant take-home. We're curious how long it lasts.
或者你可以通过我们的典型流程申请，该流程使用我们的（现在）Claude 抗扰笔试测试。我们好奇它能持续多久。
