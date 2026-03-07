# Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet | 使用 Claude 3.5 Sonnet 提升 SWE-bench Verified 水平

Our latest model, the upgraded Claude 3.5 Sonnet, achieved 49% on SWE-bench Verified, a software engineering evaluation, beating the previous state-of-the-art model's 45%. This post explains the "agent" we built around the model, and is intended to help developers get the best possible performance out of Claude 3.5 Sonnet.

我们的最新模型升级版 Claude 3.5 Sonnet 在 SWE-bench Verified 软件工程评估中取得了 49% 的成绩，超越了之前最先进模型的 45%。这篇文章解释了我们围绕该模型构建的"智能体"，旨在帮助开发者从 Claude 3.5 Sonnet 中获得最佳性能。

---

## SWE-bench | SWE-bench 基准测试

SWE-bench is an AI evaluation benchmark that assesses a model's ability to complete real-world software engineering tasks. Specifically, it tests how the model can resolve GitHub issues from popular open-source Python repositories. For each task in the benchmark, the AI model is given a set up Python environment and the checkout (a local working copy) of the repository from just before the issue was resolved. The model then needs to understand, modify, and test the code before submitting its proposed solution.

SWE-bench 是一个 AI 评估基准，用于评估模型完成真实世界软件工程任务的能力。具体来说，它测试模型如何解决来自流行开源 Python 代码仓库的 GitHub 问题。对于基准中的每个任务，AI 模型会获得一个已设置的 Python 环境以及问题解决之前的代码仓库检出（本地工作副本）。然后模型需要理解、修改和测试代码，再提交其建议的解决方案。

Each solution is graded against the real unit tests from the pull request that closed the original GitHub issue. This tests whether the AI model was able to achieve the same functionality as the original human author of the PR.

每个解决方案都会根据关闭原始 GitHub 问题的 PR 中的真实单元测试进行评分。这测试了 AI 模型是否能够实现与 PR 的原始人类作者相同的功能。

---

## Agents | 智能体

SWE-bench doesn't just evaluate the AI model in isolation, but rather an entire "agent" system. In this context, an "agent" refers to the combination of an AI model and the software scaffolding around it. This scaffolding is responsible for generating the prompts that go into the model, parsing the model's output to take action, and managing the interaction loop where the result of the model's previous action is incorporated into its next prompt. The performance of an agent on SWE-bench can vary significantly based on this scaffolding, even when using the same underlying AI model.

SWE-bench 不仅评估孤立的 AI 模型，而是评估整个"智能体"系统。在这里，"智能体"指的是 AI 模型及其周围的软件脚手架的组合。该脚手架负责生成输入模型的提示、解析模型的输出以采取行动，以及管理交互循环，将模型先前操作的结果整合到其下一个提示中。即使使用相同的底层 AI 模型，智能体在 SWE-bench 上的性能也会因这种脚手架而有显著差异。

There are many other benchmarks for the coding abilities of Large Language Models, but SWE-bench has gained in popularity for several reasons:

还有许多其他基准用于评估大语言模型的编码能力，但 SWE-bench 因以下几个原因而越来越受欢迎：

1. It uses real engineering tasks from actual projects, rather than competition- or interview-style questions;
它使用来自实际项目的真实工程任务，而不是竞赛或面试风格的问题；

2. It is not yet saturated—there's plenty of room for improvement. No model has yet crossed 50% completion on SWE-bench Verified (though the updated Claude 3.5 Sonnet is, at the time of writing, at 49%);
它尚未饱和——还有很大的改进空间。还没有模型在 SWE-bench Verified 上超过 50% 的完成率（尽管在撰写本文时，升级版 Claude 3.5 Sonnet 达到了 49%）；

3. It measures an entire "agent", rather than a model in isolation. Open-source developers and startups have had great success in optimizing scaffoldings to greatly improve the performance around the same model.
它测量整个"智能体"，而不是孤立的模型。开源开发者和初创公司在优化脚手架方面取得了巨大成功，大大提高了相同模型的性能。

Note that the original SWE-bench dataset contains some tasks that are impossible to solve without additional context outside of the GitHub issue (for example, about specific error messages to return). SWE-bench-Verified is a 500 problem subset of SWE-bench that has been reviewed by humans to make sure they are solvable, and thus provides the most clear measure of coding agents' performance. This is the benchmark to which we'll refer in this post.

请注意，原始 SWE-bench 数据集包含一些无法解决的任务，需要 GitHub 问题之外的额外上下文（例如，关于要返回的特定错误消息）。SWE-bench-Verified 是 SWE-bench 的 500 个问题子集，已经过人工审查以确保它们可解决，因此提供了对编码智能体性能的最清晰的衡量标准。这是本文将参考的基准。

---

## Achieving state-of-the-art | 达到最先进水平

### Tool Using Agent | 工具使用智能体

Our design philosophy when creating the agent scaffold optimized for updated Claude 3.5 Sonnet was to give as much control as possible to the language model itself, and keep the scaffolding minimal. The agent has a prompt, a Bash Tool for executing bash commands, and an Edit Tool, for viewing and editing files and directories. We continue to sample until the model decides that it is finished, or exceeds its 200k context length. This scaffold allows the model to use its own judgment of how to pursue the problem, rather than be hardcoded into a particular pattern or workflow.

我们在创建针对升级版 Claude 3.5 Sonnet 优化的智能体脚手架时的设计理念是，尽可能多地给予语言模型本身的控制权，并保持脚手架的最小化。智能体有一个提示、一个用于执行 bash 命令的 Bash 工具，以及一个用于查看和编辑文件和目录的编辑工具。我们继续采样，直到模型决定完成，或者超过其 200k 上下文长度。这个脚手架允许模型使用自己的判断来处理问题，而不是硬编码到特定的模式或工作流中。

The prompt outlines a suggested approach for the model, but it's not overly long or too detailed for this task. The model is free to choose how it moves from step to step, rather than having strict and discrete transitions. If you are not token-sensitive, it can help to explicitly encourage the model to produce a long response.

该提示概述了模型的建议方法，但对于这个任务来说，它不会过于冗长或详细。模型可以自由选择如何从一步移动到另一步，而不是有严格的和离散的转换。如果您不关心 token，显式鼓励模型产生长响应可能会有所帮助。

The following code shows the prompt from our agent scaffold:

以下代码显示了我们的智能体脚手架中的提示：

```python
<uploaded_files>
{location}
</uploaded_files>
I've uploaded a python code repository in the directory {location} (not in /tmp/inputs). Consider the following PR description:

<pr_description>
{pr_description}
</pr_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <pr_description> are met?
I've already taken care of all changes to any of the test files described in the <pr_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!

Your task is to make the minimal changes to non-tests files in the {location} directory to ensure the <pr_description> is satisfied.

Follow these steps to resolve the issue:
1. As a first step, it might be a good idea to explore the repo to familiarize yourself with its structure.
2. Create a script to reproduce the error and execute it with `python <filename.py>` using the BashTool, to confirm the error
3. Edit the sourcecode of the repo to resolve the issue
4. Rerun your reproduce script and confirm that the error is fixed!
5. Think about edgecases and make sure your fix handles them as well

Your thinking should be thorough and so it's fine if it's very long.
```

The model's first tool executes Bash commands. The schema is simple, taking only the command to be run in the environment. However, the description of the tool carries more weight. It includes more detailed instructions for the model, including escaping inputs, lack of internet access, and how to run commands in the background.

模型的第一个工具执行 bash 命令。模式很简单，只需要在环境中运行的命令。然而，工具的描述承载了更多的权重。它包括为模型提供的更详细的说明，包括转义输入、缺乏互联网访问以及如何在后台运行命令。

Next, we show the spec for the Bash Tool:

接下来，我们展示 Bash 工具的规范：

```json
{
   "name": "bash",
   "description": "Run commands in a bash shell\n\n* When invoking this tool, the contents of the \"command\" parameter does NOT need to be XML-escaped.\n\n* You don't have access to the internet via this tool.\n\n* You do have access to a mirror of common linux and python packages via apt and pip.\n\n* State is persistent across command calls and discussions with the user.\n\n* To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.\n\n* Please avoid commands that may produce a very large amount of output.\n\n* Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.",
   "input_schema": {
       "type": "object",
       "properties": {
           "command": {
               "type": "string",
               "description": "The bash command to run."
           }
       },
       "required": ["command"]
   }
}
```

The model's second tool (the Edit Tool) is much more complex, and contains everything the model needs for viewing, creating, and editing files. Again, our tool description contains detailed information for the model about how to use the tool.

模型的第二个工具（编辑工具）更加复杂，包含了模型查看、创建和编辑文件所需的一切。同样，我们的工具描述包含了关于如何使用工具的详细信息。

We put a lot of effort into the descriptions and specs for these tools across a wide variety of agentic tasks. We tested them to uncover any ways that the model might misunderstand the spec, or the possible pitfalls of using the tools, then edited the descriptions to preempt these problems. We believe that much more attention should go into designing tool interfaces for models, in the same way that a large amount of attention goes into designing tool interfaces for humans.

我们在各种智能体任务中为这些工具的描述和规范投入了大量精力。我们测试它们以发现模型可能误解规范的任何方式，或使用工具的可能陷阱，然后编辑描述以预先解决这些问题。我们认为，应该更多地关注为模型设计工具接口，就像为人类设计工具接口一样需要大量关注。

The following code shows the description for our Edit Tool:

以下代码显示了我们的编辑工具的描述：

```json
{
   "name": "str_replace_editor",
   "description": "Custom editing tool for viewing, creating and editing files\n\n* State is persistent across command calls and discussions with the user\n\n* If `path` is a file, `view` displays the result of applying `cat -n`. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep\n\n* The `create` command cannot be used if the specified `path` already exists as a file\n\n* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`\n\n* The `undo_edit` command will revert the last edit made to the file at `path`\n\n\nNotes for using the `str_replace` command:\n\n* The `old_str` parameter should match EXACTLY one or more consecutive lines from the original file. Be mindful of whitespaces!\n\n* If the `old_str` parameter is not unique in the file, the replacement will not be performed. Make sure to include enough context in `old_str` to make it unique\n\n* The `new_str` parameter should contain the edited lines that should replace the `old_str`"
   ...
}
```

One way we improved performance was to "error-proof" our tools. For instance, sometimes models could mess up relative file paths after the agent had moved out of the root directory. To prevent this, we simply made the tool always require an absolute path.

我们提高性能的一种方法是"防错"我们的工具。例如，有时模型在智能体移出根目录后可能会搞乱相对文件路径。为了防止这种情况，我们简单地使工具始终需要绝对路径。

We experimented with several different strategies for specifying edits to existing files and had the highest reliability with string replacement, where the model specifies `old_str` to replace with `new_str` in the given file. The replacement will only occur if there is exactly one match of `old_str`. If there are more or fewer matches, the model is shown an appropriate error message for it to retry.

我们试验了几种不同的策略来指定对现有文件的编辑，并且通过字符串替换获得了最高的可靠性，其中模型指定 `old_str` 用 `new_str` 替换。只有当 `old_str` 恰好有一个匹配时，才会进行替换。如果有更多或更少的匹配，模型会看到相应的错误消息以重试。

The spec for our Edit Tool is shown below:

我们的编辑工具的规范如下所示：

```json
...
   "input_schema": {
       "type": "object",
       "properties": {
           "command": {
               "type": "string",
               "enum": ["view", "create", "str_replace", "insert", "undo_edit"],
               "description": "The commands to run. Allowed options are: `view`, `create`, `str_replace`, `insert`, `undo_edit`."
           },
           "file_text": {
               "description": "Required parameter of `create` command, with the content of the file to be created.",
               "type": "string"
           },
           "insert_line": {
               "description": "Required parameter of `insert` command. The `new_str` will be inserted AFTER the line `insert_line` of `path`.",
               "type": "integer"
           },
           "new_str": {
               "description": "Required parameter of `str_replace` command containing the new string. Required parameter of `insert` command containing the string to insert.",
               "type": "string"
           },
           "old_str": {
               "description": "Required parameter of `str_replace` command containing the string in `path` to replace.",
               "type": "string"
           },
           "path": {
               "description": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.",
               "type": "string"
           },
           "view_range": {
               "description": "Optional parameter of `view` command when `path` points to a file. If none is given, the full file is shown. If provided, the file will be shown in the indicated line number range, e.g. [11, 12] will show lines 11 and 12. Indexing at 1 to start. Setting `[start_line, -1]` shows all lines from `start_line` to the end of the file.",
               "items": {
                   "type": "integer"
               },
               "type": "array"
           }
       },
       "required": ["command", "path"]
   }
}
```

---

## Results | 结果

In general, the upgraded Claude 3.5 Sonnet demonstrates higher reasoning, coding, and mathematical abilities than our prior models, and the previous state-of-the-art model. It also demonstrates improved agentic capabilities: the tools and scaffolding help put those improved abilities to their best use.

总的来说，升级版 Claude 3.5 Sonnet 展示了比我们之前的模型和之前最先进的模型更高的推理、编码和数学能力。它还展示了改进的智能体能力：工具和脚手架有助于将这些改进的能力发挥到最佳。

| Model | 模型 | Claude 3.5 Sonnet (new) | Claude 3.5 Sonnet（新） | Previous SOTA | 之前的最先进模型 | Claude 3.5 Sonnet (old) | Claude 3.5 Sonnet（旧） | Claude 3 Opus | Claude 3 Opus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SWE-bench Verified score | SWE-bench Verified 分数 | **49%** | **49%** | 45% | 45% | 33% | 33% | 22% | 22% |

---

## Examples of agent behavior | 智能体行为示例

For running the benchmark, we used the SWE-Agent framework as a foundation for our agent code. In our logs below, we render the agent's text output, tool calls, and tool responses as THOUGHT, ACTION, and OBSERVATION, even though we don't constrain the model to a fixed ordering.

为了运行基准，我们使用 SWE-Agent 框架作为我们的智能体代码的基础。在下面的日志中，我们将智能体的文本输出、工具调用和工具响应呈现为 THOUGHT、ACTION 和 OBSERVATION，即使我们没有将模型约束到固定顺序。

The code blocks below will walk through a typical case of the Sonnet 3.5 solving a SWE-bench problem.

下面的代码块将遍历 Sonnet 3.5 解决 SWE-bench 问题的典型案例。

In this first block, you can see part of the initial prompt given to the model, with `{pr_description}` filled in with the real value from a SWE-bench task. Importantly, this task contains steps to reproduce the issue, which will give the model a valuable starting point to investigate.

在第一个块中，您可以看到给模型的初始提示的一部分，其中 `{pr_description}` 填充了来自 SWE-bench 任务的真实值。重要的是，这个任务包含重现问题的步骤，这将为模型提供一个有价值的起点来调查。

```python
<uploaded_files>
/repo
</uploaded_files>
I've uploaded a python code repository in the directory /repo (not in /tmp/inputs). Consider the following PR description:

<pr_description>
linear_model.RidgeClassifierCV's Parameter store_cv_values issue
#### Description | 描述

#### Steps/Code to Reproduce | 重现步骤/代码
import numpy as np
from sklearn import linear_model as lm

#test database
n = 100
x = np.random.randn(n, 30)
y = np.random.normal(size = n)

rr = lm.RidgeClassifierCV(alphas = np.arange(0.1, 1000, 0.1), normalize = True,
                                         store_cv_values = True).fit(x, y)

#### Expected Results | 预期结果
Expected to get the usual ridge regression model output, keeping the cross validation predictions as attribute.

#### Actual Results | 实际结果
TypeError: *init*() got an unexpected keyword argument 'store_cv_values'

lm.RidgeClassifierCV actually has no parameter store_cv_values, even though some attributes depends on it.
```

The model responds and first uses the Edit Tool to view the repository structure. You can see the model's text output and tool call arguments under THOUGHT and ACTION, and part of the tool's output under OBSERVATION:

模型响应并首先使用编辑工具查看代码仓库结构。您可以在 THOUGHT 和 ACTION 下看到模型的文本输出和工具调用参数，以及在 OBSERVATION 下的工具输出的一部分：

```python
THOUGHT:
I'll help you implement the changes to satisfy the PR description. Let's follow the steps you outlined.

1. First, let's explore the repo structure:
ACTION (str_replace_editor):
command:
view

path:
/repo

OBSERVATION:
Here's the files and directories up to 2 levels deep in /repo, excluding hidden items:
/repo
/repo/PULL_REQUEST_TEMPLATE.md
/repo/ISSUE_TEMPLATE.md
/repo/sklearn
/repo/sklearn/decomposition
/repo/sklearn/kernel_ridge.py
/repo/sklearn/model_selection
/repo/sklearn/covariance
/repo/sklearn/cluster
/repo/sklearn/base.py
/repo/sklearn/dummy.py
/repo/sklearn/naive_bayes.py
...
```

Now that the model has a better understanding of the repository structure, it uses the Edit Tool to create a new script that it will use to reproduce the issue and test its fix:

现在模型对代码仓库结构有了更好的了解，它使用编辑工具创建一个新脚本，用于重现问题并测试其修复：

```python
THOUGHT:
Based on the repository structure, we'll need to modify the Ridge Classifier in the `sklearn/linear_model` directory.

Let's create a script to reproduce the error:
ACTION (str_replace_editor):
command:
create

path:
/repo/reproduce_error.py

file_text:
import numpy as np
from sklearn import linear_model as lm

#test database
n = 100
x = np.random.randn(n, 30)
y = np.random.normal(size = n)

rr = lm.RidgeClassifierCV(alphas=np.arange(0.1, 1000, 0.1), normalize=True,
                         store_cv_values=True).fit(x, y)

OBSERVATION:
File created successfully at: /repo/reproduce_error.py
```

The model then uses the Bash Tool to execute the script it wrote, and successfully reproduces the issue from the task:

然后模型使用 Bash 工具执行它编写的脚本，并成功重现任务中的问题：

```python
THOUGHT:
Let's verify that we can reproduce the error:
ACTION (bash):
command:
python3 /repo/reproduce_error.py

OBSERVATION:
Traceback (most recent call last):
  File "/repo/reproduce_error.py", line 10, in <module>
    store_cv_values=True).fit(x, y)
TypeError: *init*() got an unexpected keyword argument 'store_cv_values'
```

From here on, the model uses the Edit Tool to change the source code in the repository and reruns its script to verify whether the change has resolved the issue:

从这里开始，模型使用编辑工具更改代码仓库中的源代码，并重新运行其脚本以验证更改是否解决了问题：

```python
THOUGHT:
The error is reproducible. Looking at the code, I can see that the issue is that while the `RidgeClassifierCV` class inherits from `_BaseRidgeCV`, it fails to pass the `store_cv_values` parameter from its constructor through to the base class constructor.

Let's fix this:
ACTION (str_replace_editor):
command:
str_replace

path:
/repo/sklearn/linear_model/ridge.py

old_str:
    def *init*(self, alphas=(0.1, 1.0, 10.0), fit_intercept=True,
                 normalize=False, scoring=None, cv=None, class_weight=None):
        super(RidgeClassifierCV, self).*init*(
            alphas=alphas, fit_intercept=fit_intercept, normalize=normalize,
            scoring=scoring, cv=cv)
        self.class_weight = class_weight

new_str:
    def *init*(self, alphas=(0.1, 1.0, 10.0), fit_intercept=True,
                 normalize=False, scoring=None, cv=None, class_weight=None,
                 store_cv_values=False):
        super(RidgeClassifierCV, self).*init*(
            alphas=alphas, fit_intercept=fit_intercept, normalize=normalize,
            scoring=scoring, cv=cv, store_cv_values=store_cv_values)
        self.class_weight = class_weight
```

In this particular example, the model worked for 12 steps before deciding that it was ready to submit. The task's tests then ran successfully, verifying that the model's solution addressed the problem. Some tasks took more than 100 turns before the model submitted its solution; in others, the model kept trying until it ran out of context.

在这个特定的示例中，模型工作了 12 步才决定准备提交。然后任务的测试成功运行，验证了模型的解决方案解决了问题。一些任务在模型提交解决方案之前花费了超过 100 轮；在其他任务中，模型一直尝试直到用完上下文。

From reviewing attempts from the updated Claude 3.5 Sonnet compared to older models, updated 3.5 Sonnet self-corrects more often. It also shows an ability to try several different solutions, rather than getting stuck making the same mistake over and over.

通过审查升级版 Claude 3.5 Sonnet 与旧模型的尝试，升级版 3.5 Sonnet 更经常自我纠正。它还展示了一种尝试几种不同解决方案的能力，而不是陷入一遍又一遍地犯同样的错误。

---

## Challenges | 挑战

SWE-bench Verified is a powerful evaluation, but it's also more complex to run than simple, single-turn evals. These are some of the challenges that we faced in using it—challenges that other AI developers might also encounter.

SWE-bench Verified 是一个强大的评估，但它比简单的单轮评估更复杂。以下是我们在使用它时面临的一些挑战——其他 AI 开发者可能也会遇到这些挑战。

1. **Duration and high token costs.** The examples above are from a case that was successfully completed in 12 steps. However, many successful runs took hundreds of turns for the model to resolve, and >100k tokens. The updated Claude 3.5 Sonnet is tenacious: it can often find its way around a problem given enough time, but that can be expensive;

**持续时间和高 token 成本。** 上面的示例来自一个在 12 步内成功完成的案例。然而，许多成功的运行需要模型花费数百轮来解决，并且超过 100k token。升级版 Claude 3.5 Sonnet 是坚持不懈的：只要有足够的时间，它通常可以找到解决问题的方法，但这可能会很昂贵；

2. **Grading.** While inspecting failed tasks, we found cases where the model behaved correctly, but there were environment setup issues, or problems with install patches being applied twice. Resolving these systems issues is crucial for getting an accurate picture of an AI agent's performance.

**评分。** 在检查失败的任务时，我们发现了一些模型行为正确的情况，但存在环境设置问题或安装补丁被应用两次的问题。解决这些系统问题对于准确了解 AI 智能体的性能至关重要。

3. **Hidden tests.** Because the model cannot see the tests it's being graded against, it often "thinks" that it has succeeded when the task actually is a failure. Some of these failures are because the model solved the problem at the wrong level of abstraction (applying a bandaid instead of a deeper refactor). Other failures feel a little less fair: they solve the problem, but do not match the unit tests from the original task.

**隐藏测试。** 因为模型无法看到它被评分的测试，它经常"认为"它已经成功了，而实际上任务失败了。其中一些失败是因为模型在错误的抽象级别上解决了问题（应用了创可贴而不是更深层的重构）。其他失败感觉有点不太公平：它们解决了问题，但不匹配原始任务的单元测试。

4. **Multimodal.** Despite the updated Claude 3.5 Sonnet having excellent vision and multimodal capabilities, we did not implement a way for it to view files saved to the filesystem or referenced as URLs. This made debugging certain tasks (especially those from Matplotlib) especially difficult, and also prone to model hallucinations. There is definitely low-hanging fruit here for developers to improve upon—and SWE-bench has launched a new evaluation focused on multi-modal tasks. We look forward to seeing developers achieve higher scores on this eval with Claude in the near future.

**多模态。** 尽管升级版 Claude 3.5 Sonnet 具有出色的视觉和多模态能力，但我们没有实现一种让它查看保存到文件系统或作为 URL 引用的文件的方法。这使得调试某些任务（尤其是来自 Matplotlib 的任务）特别困难，并且容易导致模型幻觉。这里绝对有开发者可以改进的低垂果实——SWE-bench 已经推出了一种专注于多模态任务的新评估。我们期待看到开发者在不久的将来使用 Claude 在这个评估上取得更高的分数。

The upgraded Claude 3.5 Sonnet achieved 49% on SWE-bench Verified, beating the previous state-of-the-art (45%), with a simple prompt and two general purpose tools. We feel confident that developers building with the new Claude 3.5 Sonnet will quickly find new, better ways to improve SWE-bench scores over what we've initially demonstrated here.

升级版 Claude 3.5 Sonnet 在 SWE-bench Verified 上取得了 49% 的成绩，超越了之前的最先进水平（45%），使用的是简单的提示和两个通用工具。我们相信，使用新的 Claude 3.5 Sonnet 构建的开发者将很快找到新的、更好的方法来提高 SWE-bench 分数，超越我们在这里最初展示的。

---

## Acknowledgements | 致谢

Erik Schluntz optimized the SWE-bench agent and wrote this blog post. Simon Biggs, Dawn Drain, and Eric Christiansen helped implement the benchmark. Shauna Kravec, Dawn Drain, Felipe Rosso, Nova DasSarma, Ven Chandrasekaran, and many others contributed to training Claude 3.5 Sonnet to be excellent at agentic coding.

Erik Schluntz 优化了 SWE-bench 智能体并撰写了这篇博客文章。Simon Biggs、Dawn Drain 和 Eric Christiansen 帮助实现了基准。Shauna Kravec、Dawn Drain、Felipe Rosso、Nova DasSarma、Ven Chandrasekaran 和许多其他人贡献了训练 Claude 3.5 Sonnet 在智能体编码方面的出色表现。

---

## Sources | 来源

- [SWE-bench](https://www.swebench.com/) - Official SWE-bench website
- [SWE-bench](https://www.swebench.com/) - SWE-bench 官方网站

- [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench) - Official repository
- [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench) - 官方代码仓库

- [SWE-Agent](https://github.com/princeton-nlp/SWE-agent) - Agent framework used for running the benchmark
- [SWE-Agent](https://github.com/princeton-nlp/SWE-agent) - 用于运行基准的智能体框架

- [Anthropic Research](https://www.anthropic.com/research) - Anthropic research publications
- [Anthropic Research](https://www.anthropic.com/research) - Anthropic 研究出版物
