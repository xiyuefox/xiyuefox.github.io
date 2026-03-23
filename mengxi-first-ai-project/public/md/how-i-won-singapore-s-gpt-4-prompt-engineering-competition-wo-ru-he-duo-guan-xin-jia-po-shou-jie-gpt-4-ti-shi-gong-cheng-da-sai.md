---
title: "How I Won Singapore’s GPT-4 Prompt Engineering Competition我如何夺冠新加坡首届 GPT-4 提示工程大赛"
date: 2024-05-08
tags: []
category: "obsidian"
badge: "obsidian"
---

原文：[How I Won Singapore’s GPT-4 Prompt Engineering Competition](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41)
## A deep dive into the strategies I learned for harnessing the power of Large Language Models (LLMs)深度探索我在驾驭大语言模型（LLMs）中学到的策略

![Sheila Teo](https://miro.medium.com/v2/da:true/resize:fill:88:88/1*UmlZGQsNhuv9kgQL6pFslA.gif)

[Sheila Teo](https://medium.com/@sheilateozy?source=post_page-----34c195a93d41--------------------------------)

Towards Data Science

![](https://miro.medium.com/v2/resize:fit:1400/1*RAI4cBXe1_zaxVykHz79oA.jpeg)

Celebrating a milestone — The real win was the priceless learning experience!庆祝这一里程碑 — 真正的胜利在于宝贵的学习经历！

Last month, I had the incredible honor of winning Singapore’s first ever GPT-4 Prompt Engineering competition, which brought together over 400 prompt-ly brilliant participants, organised by the Government Technology Agency of Singapore (GovTech).上个月，我非常荣幸地在新加坡政府科技局（GovTech）组织的首届 GPT-4 提示工程大赛中脱颖而出，这场比赛吸引了超过 400 名杰出的参与者。

Prompt engineering is a discipline that blends both art and science — it is as much technical understanding as it is of creativity and strategic thinking. This is a compilation of the prompt engineering strategies I learned along the way, that push any LLM to do exactly what you need and more!提示工程是一门将艺术与科学巧妙融合的学科 — 它不仅关乎技术的理解，更涉及创造力和战略思考。这里分享的是我在实践中学到的一些提示工程策略，这些策略能够精准地驱动任何大语言模型为你服务，甚至做得更多！

> **Author’s Note:  
> **In writing this, I sought to steer away from the traditional prompt engineering techniques that have already been extensively discussed and documented online. Instead, my aim is to bring fresh insights that I learned through experimentation, and a different, personal take in understanding and approaching certain techniques. I hope you’ll enjoy reading this piece!
> **作者的话：** 在写作本文时，我特意避开了那些已经广泛讨论和记录的常规提示工程技巧。相反，我更希望分享一些我在实验中获得的新洞见，以及我个人在理解和应用这些技巧时的独到见解。希望你能从中获得乐趣！

![](https://miro.medium.com/v2/resize:fit:1154/1*ouYNaR56ptHhV9iUwF8ipg.png)

**This article covers the following, with** 🔵 **referring to beginner-friendly prompting techniques while** 🔴 **refers to advanced strategies:****
本文涵盖以下主题，其中** 🔵 **代表初学者友好的技巧，而** 🔴 **代表高级策略：**
**1. [**🔵**]** [**Structuring prompts using the CO-STAR framework**](https://medium.com/towards-data-science/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#10b2)使用CO-STAR框架构建提示结构

**2. [**🔵**]** [**Sectioning prompts using delimiters**](https://medium.com/towards-data-science/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#8f6a)
使用分隔符对提示进行分组
**3. [**🔴**]** [**Creating system prompts with LLM guardrails**](https://medium.com/towards-data-science/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#1cfa)**结合大语言模型 (LLM) 的安全防护，制定系统提示**

**4. [**🔴**]** [**Analyzing datasets using only LLMs, without plugins or code**](https://medium.com/towards-data-science/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#183c) **—  仅使用LLMs分析数据集，无需插件或代码 -

With a hands-on example of analyzing a real-world Kaggle dataset using GPT-4**
通过一个实际的案例，展示如何利用 GPT-4 分析来自 Kaggle 的现实世界数据集

# 1. [🔵] Structuring Prompts using the CO-STAR framework利用 CO-STAR 框架构建有效的提示  

Effective prompt structuring is crucial for eliciting optimal responses from an LLM. The CO-STAR framework, a brainchild of GovTech Singapore’s Data Science & AI team, is a handy template for structuring prompts. It considers all the key aspects that influence the effectiveness and relevance of an LLM’s response, leading to more optimal responses.在使用大语言模型时，有效的提示构建至关重要。CO-STAR 框架，由新加坡政府科技局数据科学与 AI 团队创立，是一个实用的提示构建工具。它考虑了所有影响大语言模型响应效果和相关性的关键因素，帮助你获得更优的反馈。

![](https://miro.medium.com/v2/resize:fit:1400/1*_20YO3p4S4a4BKBtFGwwuA.png)

CO-STAR framework — Image by authorCO-STAR 框架 — 作者提供的图像

Here’s how it works:如何应用 CO-STAR 框架：

## **(C) Context: Provide background information on the task** **(C) 上下文：为任务提供背景信息**

This helps the LLM understand the specific scenario being discussed, ensuring its response is relevant.通过为大语言模型（LLM）提供详细的背景信息，可以帮助它精确理解讨论的具体场景，确保提供的反馈具有相关性。

## **(O) Objective: Define what the task is that you want the LLM to perform**(O) 目标：明确你要求大语言模型完成的任务****

Being clear about your objective helps the LLM to focus its response on meeting that specific goal.
**明确你要求大语言模型完成的任务** 清晰地界定任务目标，可以使大语言模型更专注地调整其回应，以实现这一具体目标。
## **(S) Style: Specify the writing style you want the LLM to use****(S) 风格：明确你期望的写作风格**

This could be a particular famous person’s style of writing, or a particular expert in a profession, like a business analyst expert or CEO. This **g**uides the LLM to respond with the manner and choice of words aligned with your needs.你可以指定一个特定的著名人物或某个行业专家的写作风格，如商业分析师或 CEO。这将**指导**大语言模型以一种符合你需求的方式和词汇选择进行回应。

## **(T) Tone: Set the attitude of the response****(T) 语气：设置回应的情感调**

This ensures the LLM’s response resonates with the intended sentiment or emotional context required. Examples are formal, humorous, empathetic, among others.**设置回应的情感调** 设定适当的语气，确保大语言模型的回应能够与预期的情感或情绪背景相协调。可能的语气包括正式、幽默、富有同情心等。

## **(A) Audience: Identify who the response is intended for****(A) 受众：识别目标受众**

Tailoring the LLM’s response to an audience, such as experts in a field, beginners, children, and so on, ensures that it is appropriate and understandable in your required context.**识别目标受众** 针对特定受众定制大语言模型的回应，无论是领域内的专家、初学者还是儿童，都能确保内容在特定上下文中适当且容易理解。

## **(R) Response: Provide the response format****(R) 响应：规定输出的格式**

This ensures that the LLM outputs in the exact format that you require for downstream tasks. Examples include a list, a JSON, a professional report, and so on. For most LLM applications which work on the LLM responses programmatically for downstream manipulations, a JSON output format would be ideal.确定输出格式是为了确保大语言模型按照你的具体需求进行输出，便于执行下游任务。常见的格式包括列表、JSON 格式的数据、专业报告等。对于大部分需要程序化处理大语言模型输出的应用来说，JSON 格式是理想的选择。
## A practical application of CO-STAR## CO-STAR 框架的实用示例

Here’s a real-world example of why the CO-STAR framework is useful. Let’s say you work as a social media manager, and you need help drafting a Facebook post to advertise your company’s new product.
这里有一个 CO-STAR 框架为何有用的现实案例。假设你担任社交媒体经理，需要草拟一条 Facebook 帖子，用以推广公司的新产品。

A quick prompt **without** CO-STAR might look something like this:未使用 CO-STAR 的快速提示可能是这样的：

> Write a facebook post to advertise my company’s new product. My company’s name is Alpha and the product is called Beta, a new ultra-fast hairdryer.
> 为我的公司 Alpha 的新产品 Beta——一款新型超快速吹风机，撰写一条 Facebook 帖子。

Here’s the output from GPT-4:这是 GPT-4 的回答：

> Introducing the Revolutionary Beta Hairdryer by Alpha!  
> - Say goodbye to long, tedious hair drying sessions! Alpha is proud to unveil the Beta, our latest innovation in haircare technology.  
> - Ultra-Fast Drying: The Beta is designed to cut your drying time in half, thanks to its advanced, powerful motor. Get ready faster and enjoy more time doing what you love!  
> Shop Now: [Link to product page]
> 介绍 Alpha 公司革命性的 Beta 吹风机！告别长时间、无聊的吹发过程！Alpha 公司自豪地推出 Beta，这是我们在护发技术上的最新创新——超快干燥：Beta 设计旨在让你的吹发时间减半，得益于其先进的强力马达。快速准备，享受更多你所爱的时间！立即购买：[产品页面链接]

While adequate, this output is painfully generic, lacking the specific nuances and targeted appeal necessary to resonate with your company’s audience.
这一输出虽足够，但显得过于泛化，缺乏必要的细节和针对性吸引力，未能真正触及公司目标受众的心。
Here’s an example of using the CO-STAR template instead, which reminds you to incorporate other aspects of your task into your prompt, specifically the `STYLE`, `TONE`, and `AUDIENCE` aspects that are missing from the previous quick prompt:
下面是一个应用 CO-STAR 模板的示例，它提醒我们在制定提示时，要考虑到任务的其它方面，特别是之前快速提示中缺少的`风格`、`语调`和`受众`：

> # CONTEXT #  
> I want to advertise my company’s new product. My company’s name is Alpha and the product is called Beta, which is a new ultra-fast hairdryer.
> 
> # OBJECTIVE #  
> Create a Facebook post for me, which aims to get people to click on the product link to purchase it.
> 
> # STYLE #  
> Follow the writing style of successful companies that advertise similar products, such as Dyson.
> 
> # TONE #  
> Persuasive
> 
> # AUDIENCE #  
> My company’s audience profile on Facebook is typically the older generation. Tailor your post to target what this audience typically looks out for in hair products.
> 
> # RESPONSE #  
> The Facebook post, kept concise yet impactful.


> # CONTEXT（上下文） #  
> 我想推广公司的新产品。我的公司名为 Alpha，新产品名为 Beta，是一款新型超快速吹风机。
> 
> # OBJECTIVE（目标） #  
> 帮我创建一条 Facebook 帖子，目的是吸引人们点击产品链接进行购买。
> 
> # STYLE（风格） #  
> 参照 Dyson 等成功公司的宣传风格，它们在推广类似产品时的文案风格。
> 
> # TONE（语调） #  
> 说服性
> 
> # AUDIENCE（受众） #  
> 我们公司在 Facebook 上的主要受众是老年人。请针对这一群体在选择护发产品时的典型关注点来定制帖子。
> 
> # RESPONSE（响应） #  
> 保持 Facebook 帖子简洁而深具影响力。

By applying CO-STAR, GPT-4’s response becomes significantly more targeted and effective:通过运用 CO-STAR 框架，GPT-4 的响应变得更具针对性和效果：

> Embrace Effortless Elegance with Alpha Beta — The Ultra-Fast Hairdryer for the Wise Generation.
> 
> Rediscover the joy of simple, effective hair care with Alpha Beta. Our latest innovation is more than just a hairdryer; it’s a promise of swift, gentle, and  
> reliable hair styling for those who appreciate the finer things in life.
> 
> - Easy and Intuitive Use: Say goodbye to complicated gadgets. Alpha Beta is  
> crafted for comfort and simplicity, perfect for those who value straightforward,  
> hassle-free technology.  
> - Time-Saving Technology: We understand your time is precious. That’s why Alpha Beta cuts down drying time significantly, giving you more moments to enjoy life’s pleasures.
> 
> Make every day a good hair day with Alpha Beta. Experience the blend of  
> sophistication and simplicity today.
> 
> [Your Product Link Here]
> 用 Alpha Beta——超快速吹风机，体验轻松的优雅生活，它是为具有洞察力的一代人设计的。
> 
> 与 Alpha Beta 一起，重新找回简单而高效的护发乐趣。我们的最新创新不仅是一款吹风机；它还承诺为那些懂得欣赏生活美好事物的人提供快速、柔和且可靠的发型打理。
> 
> - 易用且直观：向复杂的设备说再见。Alpha Beta 专为舒适和简便而设计，非常适合那些喜欢简洁、无麻烦操作的人。- 节省时间的技术：我们知道您的时间非常宝贵。因此，Alpha Beta 显著缩短吹发时间，让您有更多时间享受生活。
> 
> 每天都是与 Alpha Beta 相伴的美好发型日。立即体验优雅与简约的完美结合。

[您的产品链接在此]

The CO-STAR framework guides you to provide all of the crucial pieces of information about your task to the LLM in a structured manner, ensuring a tailored and optimized response to exactly what you need.
CO-STAR 框架指引您以有组织的方式提供所有关键任务信息，确保响应完全针对您的需求并进行优化。

# 2. [🔵] Sectioning Prompts Using Delimiters 使用分隔符进行文本分段

![](https://miro.medium.com/v2/resize:fit:1400/1*Lzklp7X7btTm7DjZXDLzww.png)

Image generated by DALL·E 3

Delimiters are special tokens that help the LLM distinguish which parts of your prompt it should consider as a single unit of meaning. This is important because your entire prompt arrives to the LLM as a single long sequence of tokens. Delimiters provide structure to this sequence of tokens by fencing specific parts of your prompt to be treated differently.分隔符是特殊的符号，它们帮助大语言模型 (LLM) 辨识提示中哪些部分应当被视为一个完整的意义单元。这非常关键，因为你的提示是作为一个长的 Token 序列一次性传给模型的。通过设置分隔符，可以为这些 Token 序列提供结构，使特定部分得到不同的处理。

It is noteworthy that delimiters may not make a difference to the quality of an LLM’s response for straightforward tasks. However, the more complex the task, the more impact the usage of delimiters for sectioning has on the LLM’s response.翻译成中文需要注意的是，对于简单的任务，分隔符对大语言模型的回应质量可能无显著影响。但是，任务越复杂，合理使用分隔符进行文本分段对模型的反应影响越明显。

## Delimiters as Special Characters
## 分隔符作为特殊字符

A delimiter could be any sequence of special characters that usually wouldn’t appear together, for example:
分隔符可以是一系列通常不会组合出现的特殊字符，例如：
- - ###
- ===
- >>>

The number and type of special characters chosen is inconsequential, as long as they are unique enough for the LLM to understand them as content separators instead of normal punctuation.
选择哪种特殊字符并不重要，关键是这些字符足够独特，使得模型能将其识别为分隔符，而非常规标点符号。

Here’s an example of how you might use such delimiters in a prompt:
这里是一个分隔符使用的示例：

> Classify the sentiment of each conversation in <<<CONVERSATIONS>>> as  
> ‘Positive’ or ‘Negative’. Give the sentiment classifications without any other preamble text.
> 
> ###
> 
> EXAMPLE CONVERSATIONS
> 
> [Agent]: Good morning, how can I assist you today?  
> [Customer]: This product is terrible, nothing like what was advertised!  
> [Customer]: I’m extremely disappointed and expect a full refund.
> 
> [Agent]: Good morning, how can I help you today?  
> [Customer]: Hi, I just wanted to say that I’m really impressed with your  
> product. It exceeded my expectations!
> 
> ###
> 
> EXAMPLE OUTPUTS
> 
> Negative
> 
> Positive
> 
> ###
> 
> <<<  
> [Agent]: Hello! Welcome to our support. How can I help you today?  
> [Customer]: Hi there! I just wanted to let you know I received my order, and  
> it’s fantastic!  
> [Agent]: That’s great to hear! We’re thrilled you’re happy with your purchase.  
> Is there anything else I can assist you with?  
> [Customer]: No, that’s it. Just wanted to give some positive feedback. Thanks  
> for your excellent service!
> 
> [Agent]: Hello, thank you for reaching out. How can I assist you today?  
> [Customer]: I’m very disappointed with my recent purchase. It’s not what I expected at all.  
> [Agent]: I’m sorry to hear that. Could you please provide more details so I can help?  
> [Customer]: The product is of poor quality and it arrived late. I’m really  
> unhappy with this experience.  

> > 请在 <<<CONVERSATIONS>>> 中对每段对话的情绪进行分类，标为‘正面’或‘负面’。仅提供情绪分类结果，不需任何引言。
> 
> ### [](https://baoyu.io/translations/prompt-engineering/how-i-won-singapores-gpt-4-prompt-engineering-competition#)
> 
> 对话示例
> 
> [Agent]: 早上好，今天我能为您做些什么？  
> [Customer]: 这个产品真差劲，一点都不符合广告宣传！  
> [Customer]: 我非常不满，要求全额退款。
> 
> [Agent]: 早安，我今天怎么为您服务？ [Customer]: 嗨，我只想说我真的很喜欢你们的产品。它超出了我的预期！
> 
> ### [](https://baoyu.io/translations/prompt-engineering/how-i-won-singapores-gpt-4-prompt-engineering-competition#-1)
> 
> 输出示例
> 
> 负面
> 
> 正面
> 

> 
> <<<  
> [Agent]: 您好！欢迎使用我们的客服。今天有什么可以帮到您的？  
> [Customer]: 嗨，我只想让你知道我收到了订单，它非常棒！  
> [Agent]: 那太好了！我们很高兴您对购买感到满意。还有其他需要帮助的吗？  
> [Customer]: 不，就这些了。只是想表达一下我的好评。感谢您的优质服务！
> 
> [Agent]: 您好，感谢您联系我们。今天有什么可以帮助您的？  
> [Customer]: 我对最近的购买非常不满。这完全不是我所期待的。  
> [Agent]: 我很抱歉听到您有这样的体验。您能否提供更多细节，以便我为您提供帮助？  
> [Customer]: 产品质量不佳，而且送达晚了。我对这次购买感到非常不满。  
> >>>

Above, the examples are sectioned using the delimiter `###`, with the section headings `EXAMPLE CONVERSATIONS` and `EXAMPLE OUTPUTS` in capital letters to differentiate them. The preamble states that the conversations to be classified are sectioned inside `<<<CONVERSATIONS>>>`, and these conversations are subsequently given to the LLM at the bottom of the prompt without any explanatory text, but the LLM understands that these are the conversations it should classify due to the presence of the delimiters `<<<` and `>>>`.
在上述示例中，使用 `###` 分隔符来分隔不同的部分，通过大写的章节标题如 `对话示例` 和 `输出示例` 进行区分。引言部分说明了要对 `<<<CONVERSATIONS>>>` 中的对话进行情绪分类，而这些对话在提示的底部给出，没有任何解释文本，但分隔符的存在让模型明白这些对话需要被分类。

GPT-4 的输出正如请求的那样，仅给出情绪分类：
Here is the output from GPT-4, with the sentiment classifications given without any other preamble text outputted, like what we asked for:

> Positive
> 
> Negative

## Delimiters as XML Tags

Another approach to using delimiters is having them as XML tags. XML tags are tags enclosed in angle brackets, with opening and closing tags. An example is `<tag>` and `</tag>`. This is effective as LLMs have been trained on a lot of web content in XML, and have learned to understand its formatting.

Here’s the same prompt above, but structured using XML tags as delimiters instead:

> Classify the sentiment of the following conversations into one of two classes, using the examples given. Give the sentiment classifications without any other  
> preamble text.
> 
> <classes>  
> Positive  
> Negative  
> </classes>
> 
> <example-conversations>  
> [Agent]: Good morning, how can I assist you today?  
> [Customer]: This product is terrible, nothing like what was advertised!  
> [Customer]: I’m extremely disappointed and expect a full refund.
> 
> [Agent]: Good morning, how can I help you today?  
> [Customer]: Hi, I just wanted to say that I’m really impressed with your  
> product. It exceeded my expectations!  
> </example-conversations>
> 
> <example-classes>  
> Negative
> 
> Positive  
> </example-classes>
> 
> <conversations>  
> [Agent]: Hello! Welcome to our support. How can I help you today?  
> [Customer]: Hi there! I just wanted to let you know I received my order, and  
> it’s fantastic!  
> [Agent]: That’s great to hear! We’re thrilled you’re happy with your purchase.  
> Is there anything else I can assist you with?  
> [Customer]: No, that’s it. Just wanted to give some positive feedback. Thanks  
> for your excellent service!
> 
> [Agent]: Hello, thank you for reaching out. How can I assist you today?  
> [Customer]: I’m very disappointed with my recent purchase. It’s not what I  
> expected at all.  
> [Agent]: I’m sorry to hear that. Could you please provide more details so I  
> can help?  
> [Customer]: The product is of poor quality and it arrived late. I’m really  
> unhappy with this experience.  
> </conversations>

It is beneficial to use the same noun for the XML tag as the words you have used to describe them in the instructions. The instructions we gave in the prompt above were:

> Classify the sentiment of the following conversations into one of two classes, using the examples given. Give the sentiment classifications without any other  
> preamble text.

Where we used the nouns `conversations`, `classes`, and `examples`. As such, the XML tags we use as delimiters are `<conversations>`, `<classes>`, `<example-conversations>`, and `<example-classes>`. This ensures that the LLM understands how your instructions relate to the XML tags used as delimiters.

Again, the sectioning of your instructions in a clear and structured manner through the use of delimiters ensures that GPT-4 responds exactly how you want it to:

> Positive
> 
> Negative

***


### 将分隔符用作 XML 标签

使用 XML 标签作为分隔符是一种方法。XML 标签是被尖括号包围的，包括开启标签和结束标签。例如，`<tag>`和`</tag>`。这种方法非常有效，因为大语言模型已经接受了大量包含 XML 格式的网页内容的训练，因此能够理解其结构。

以下是利用 XML 标签作为分隔符对同一提示进行结构化的例子：

分类以下对话的情感，分为正面和负面两类，根据给出的例子进行分类。请直接给出情感分类结果，不需要添加任何引导性文本。

<classes>  
正面  
负面  
</classes>

<example-conversations>  
[Agent]: 早上好，今天我能如何帮助您？  
[Customer]: 这个产品太糟糕了，一点都不像广告上说的那样！  
[Customer]: 我非常失望，希望全额退款。

[Agent]: 早上好，今天我能怎么帮您？  
[Customer]: 嗨，我只是想说我真的对你们的产品印象深刻。它超出了我的期望！  
</example-conversations>

<example-classes>  
负面  
正面  
</example-classes>

<conversations>  
[Agent]: 你好！欢迎来到我们的支持。今天我能怎么帮您？  
[Customer]: 嗨，我只是想让你知道我收到我的订单了，它太棒了！  
[Agent]: 听到这个真好！我们很高兴你对购买感到满意。还有其他我能帮忙的吗？
> [Customer]: 不，就这些。只是想给一些正面的反馈。谢谢你们的优质服务！
> 
> [Agent]: 你好，感谢你的联系。今天我能怎么帮您？  
> [Customer]: 我对我最近的购买非常失望。这完全不是我所期待的。  
> [Agent]: 很遗憾听到这些。您能提供更多细节以便我帮助您吗？  
> [Customer]: 产品质量差，而且到货晚。我对这次经历非常不满。  
> </conversations>

==在指令中使用的名词与 XML 标签的名词一致，如 `conversations`、`classes` 和 `examples`，因此使用的 XML 标签分别是 `<conversations>`、`<classes>`、`<example-conversations>` 和 `<example-classes>`。这确保了模型能够清晰地理解指令与使用的标签之间的关系。==

通过这种结构化的分隔符使用方式，可以确保 GPT-4 精确地按照您的期望响应：
> 正面
> 
> 负面

# 3. [🔴] Creating System Prompts With LLM Guardrails
利用大语言模型 (LLM) 的系统提示创建机制
> _Before diving in, it is important to note that this section is relevant only to LLMs that possess a System Prompt feature, unlike the other sections in this article which are relevant for any LLM. The most notable LLM with this feature is, of course, ChatGPT, and therefore we will use ChatGPT as the illustrating example for this section.__
> 在开始前，我们需指出，本节内容仅适用于具备系统提示功能的大语言模型 (LLM)，与文章中其他适用于所有大语言模型的部分不同。显然，具有此功能的最知名的大语言模型是 ChatGPT，因此我们

![](https://miro.medium.com/v2/resize:fit:1400/1*WLO3fEbiargL8GSbsYXC6w.png)
将以 ChatGPT 为例进行说明
Image generated by DALL·E 3

## Terminology surrounding System Prompts
关于系统提示的术语解释


First, let’s iron out terminology: With regards to ChatGPT, there exists a plethora of resources using these 3 terms almost interchangeably: “System Prompts”, “System Messages”, and “Custom Instructions”. This has proved confusing to many (including me!), so much so that OpenAI released an [article](https://help.openai.com/en/articles/8234522-chat-completions-api-system-message-vs-custom-instructions-in-ui) explaining these terminologies. Here’s a quick summary of it:
首先，我们来厘清几个术语：在讨论 ChatGPT 时，这三个术语“系统提示”、“系统消息”和“自定义指令”几乎可以互换使用。这种用法让许多人（包括我自己）感到混淆，因此 OpenAI 发表了一篇[文章](https://help.openai.com/en/articles/8234522-chat-completions-api-system-message-vs-custom-instructions-in-ui)，专门解释了这些术语。简要总结如下：

- “System Prompts” and “System Messages” are terms used when interacting with ChatGPT programmatically over its Chat Completions API.系统提示”和“系统消息”是通过 Chat Completions API 编程方式交互时使用的术语。
- On the other hand, “Custom Instructions” is the term used when interacting with ChatGPT over its user interface at [https://chat.openai.com/](https://chat.openai.com/).- 而“自定义指令”则是在通过 [https://chat.openai.com/](https://chat.openai.com/) 的用户界面与 ChatGPT 交互时使用的术语。

![](https://miro.medium.com/v2/resize:fit:1400/1*gW-q7MI5fNG1fe-QhCCKBw@2x.jpeg)

Image from [Enterprise DNA Blog](https://blog.enterprisedna.co/chatgpt-custom-instructions/)

Overall, though, the 3 terms refer to the same thing, so don’t let the terminology confuse you! Moving forward, this section will use the term “System Prompts”. Now let’s dive in!尽管这三个术语表达的是相同的概念，但不必因术语的使用而感到困扰。下面我们将统一使用“系统提示”这一术语。现在，让我们一探究竟！

## What are System Prompts? 什么是系统提示？

> System Prompts are an additional prompt where you provide instructions on how the LLM should behave. It is considered additional as it is outside of your “normal” prompts (better known as User Prompts) to the LLM.系统提示是您向大语言模型提供的关于其应如何响应的额外指示。这被视为一种额外的提示，因为它超出了您对大语言模型的常规用户提示。

Within a chat, every time you provide a new prompt, System Prompts act like a filter that the LLM automatically applies before giving its response to your new prompt. This means that the System Prompts are taken into account every time the LLM responds within the chat.在对话中，每当您提出一个新的提示时，系统提示就像是一个过滤器，大语言模型会在回应您的新提示之前自动应用这一过滤器。这意味着在对话中每次大语言模型给出回应时，都会考虑到这些系统提示。

## When should System Prompts be used?

The first question on your mind might be: Why should I provide instructions inside the System Prompt when I can also provide them in my first prompt to a new chat, before further conversations with the LLM?

The answer is because LLMs have a limit to their conversational memory. In the latter case, as the conversation carries on, the LLM is likely to “forget” this first prompt you provided to the chat, making these instructions obsolete.

On the other hand, when instructions are provided in the System Prompt, these System Prompt instructions are automatically taken into account together with each new prompt provided to the chat. This ensures that the LLM continues to receive these instructions even as the conversation carries on, no matter how long the chat becomes.

In conclusion:

> ==Use System Prompts to provide instructions that you want the LLM to remember when responding throughout the entire chat.==

## What should System Prompts include?

Instructions in the System Prompt typically includes the following categories:

- Task definition, so the LLM will always remember what it has to do throughout the chat.- **任务定义**：确保大语言模型（LLM）在整个对话中清楚自己的任务。
- Output format, so the LLM will always remember how it should respond.- **输出格式**：指导 LLM 如何格式化其回答。
- Guardrails, so the LLM will always remember how it should ***not*** respond. Guardrails are emerging field in LLM governance, referring to configured boundaries that an LLM is allowed to operate in.- **操作边界**：明确 LLM 不应采取的行为。这些边界是 LLM 治理中新兴的一个方面，旨在界定 LLM 的操作范围。

For example, a System Prompt might look like this:例如，系统提示可能是这样的：



> You will answer questions using this text: [insert text].  
> You will respond with a JSON object in this format: {“Question”: “Answer”}.  
> If the text does not contain sufficient information to answer the question, do not make up information and give the answer as “NA”.  
> You are only allowed to answer questions related to [insert scope]. Never answer any questions related to demographic information such as age, gender, and religion.
> 您需要用这段文本来回答问题：[插入文本]。请按照`{"问题": "答案"}` 的格式来回答。如果文本信息不足以回答问题，请以"NA"作答。您只能解答与[指定范围]相关的问题。请避免回答任何与年龄、性别及宗教等人口统计信息相关的问题。

Where each portion relates to the categories as follows:

![](https://miro.medium.com/v2/resize:fit:2000/1*GtzzxPCqK4rsLxIpC5QHJQ.png)

Breaking down a System Prompt — Image by author系统提示解析 - 作者提供的图像

## But then what goes into the “normal” prompts to the chat? 那么用户提示中应该包括什么内容？

Now you might be thinking: That sounds like a lot of information already being given in the System Prompt. What do I put in my “normal” prompts (better known as User Prompts) to the chat then?现在你可能会想：系统提示已经提供了很多信息。那么我应该在我的“正常”提示（也称为用户提示）中放入什么呢？


The System Prompt outlines the general task at hand. In the above System Prompt example, the task has been defined to only use a specific piece of text for question-answering, and the LLM is instructed to respond in the format `{"Question": "Answer"}`.系统提示已经概括了任务的总体要求。在上述示例中，任务被定义为仅使用特定文本进行问题解答，同时指导 LLM 按照`{"问题"："答案"}`的格式进行回答。

> You will answer questions using this text: [insert text].  
> You will respond with a JSON object in this format: {“Question”: “Answer”}.

In this case, each User Prompt to the chat would simply be the question that you want answered using the text. For example, a User Prompt might be `"What is the text about?"`. And the LLM would respond with `{"What is the text about?": "The text is about..."}`.

But let’s generalize this task example further. In practice, it would be more likely that you have multiple pieces of text that you want to ask questions on, rather than just 1. In this case, we could edit the first line of the above System Prompt from
但我们可以将这种任务进一步推广。通常，与只询问一个文本相比，你可能会有多个文本需要询问。这时，我们可以将系统提示的首句从
> You will answer questions using this text: [insert text].
您需要用这段文本来回答问题：[插入文本]。
to改为

> You will answer questions using the provided text.
您需要使用提供的文本来回答问题。
Now, each User Prompt to the chat would include both the text to conduct question-answering over, and the question to be answered, such as:
如此，每个用户提示将包括要问答的文本和问题，例如：
> <text>  
> [insert text]  
> </text>
> 
> <question>  
> [insert question]  
> </question>
> 
<text> [插入文本] </text>

<question> [插入问题] </question>
Here, we also use XML tags as delimiters in order to provide the 2 required pieces of information to the LLM in a structured manner. The nouns used in the XML tags, `text` and `question`, correspond to the nouns used in the System Prompt so that the LLM understands how the tags relate to the System Prompt instructions.此处，我们使用 XML 标签来分隔信息，以便以结构化方式向 LLM 提供所需的两个信息。XML 标签中的名词，`text` 和 `question`，与系统提示中的名词相对应，以便 LLM 理解这些标签是如何与指令相关联的。

In conclusion, the System Prompt should give the overall task instructions, and each User Prompt should provide the exact specifics that you want the task to be executed using. In this case, for example, these exact specifics are the text and the question.总之，系统提示应提供整体任务指令，而每个用户提示则需要提供执行该任务所需的具体细节。在这个例子中，这些细节就是文本和问题。

## Extra: Making LLM guardrails dynamic额外内容：为 LLM 设定动态规则

Above, guardrails are added through a few sentences in the System Prompt. These guardrails are then set in stone and do not change for the entire chat. What if you wish to have different guardrails in place at different points of the conversation?
在之前的讨论中，我们通过系统提示来设定规则，这些规则一经设定，将在整个对话中保持不变。但如果你想在对话的不同阶段实施不同的规则，应该怎么做呢？

Unfortunately for users of the ChatGPT user interface, there is no straightforward way to do this right now. However, if you’re interacting with ChatGPT programmatically, you’re in luck! The increasing focus on building effective LLM guardrails has seen the development of open-source packages that allow you to set up far more detailed and dynamic guardrails programmatically.
对于直接使用 ChatGPT 用户界面的用户来说，目前还没有直接的方法可以实现这一点。然而，如果你通过编程方式与 ChatGPT 互动，那么情况就大不相同了！随着对开发有效 LLM 规则的关注不断增加，一些允许你通过编程方式设定更为详细和动态的规则的开源软件包也应运而生。

A noteworthy one is [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) developed by the NVIDIA team, which allows you to configure the expected conversation flow between users and the LLM, and thus set up different guardrails at different points of the chat, allowing for dynamic guardrails that evolve as the chat progresses. I definitely recommend checking it out!
特别推荐的一个是由 NVIDIA 团队开发的[NeMo Guardrails]([[https://github.com/NVIDIA/NeMo-Guardrails]])。这个工具允许你配置用户与 LLM 之间的预期对话流程，并在对话的不同环节设定不同的规则，实现规则的动态调整。这无疑是探索对话动态管理的一个很好的资源，值得一试！

# 4. [🔴] Analyzing datasets using only LLMs, without plugins or code仅用大语言模型 (LLM) 分析数据集，不借助插件或编码

![](https://miro.medium.com/v2/resize:fit:1400/1*uUfKhUoxA8ZaS4Ww5TzAug.png)

Image generated by DALL·E 3

You might have heard of OpenAI’s Advanced Data Analysis plugin within ChatGPT’s GPT-4 that is available to premium (paid) accounts. It allows users to upload datasets to ChatGPT and run code directly on the dataset, allowing for accurate data analysis.你可能已经听说过 OpenAI 在 ChatGPT 的 GPT-4 中为付费账户提供的高级数据分析插件。它让用户可以上传数据集到 ChatGPT 并直接在数据集上执行编码，实现精准的数据分析。

But did you know that you don’t _always_ need such plugins to analyze datasets well with LLMs? Let’s first understand the strengths and limitations of **purely** using LLMs to analyze datasets.但是，你知道吗？并不总是需要依赖这类插件来有效地使用大语言模型 (LLM) 分析数据集。我们首先来探讨一下仅利用 LLM 进行数据分析的优势与限制。

## Types of dataset analysis that LLMs are *_not*_ great at LLM 在哪些数据集分析类型上_不_擅长

As you probably already know, LLMs are limited in their ability to perform accurate mathematical calculations, making them unsuitable for tasks requiring precise quantitative analysis on datasets, such as:正如你可能已经知道的，LLMs 在执行精确的数学计算方面有所限制，这让它们不适合需要精确量化分析的任务，比如：

- **Descriptive Statistics:** Summarizing numerical columns quantitatively, through measures like the mean or variance.**描述性统计（Descriptive Statistics）：** 通过如均值或方差等措施定量总结数值列。
- **Correlation Analysis:** Obtaining the precise correlation coefficient between columns.**相关性分析（Correlation Analysis）：** 获取列间的精确相关系数。
- **Statistical Analysis:** Such as hypothesis testing to determine if there are statistically significant differences between groups of data points.**统计分析（Statistical Analysis）：** 例如进行假设检验，判断数据点组间是否存在统计显著的差异。
- **Machine Learning:** Performing predictive modelling on a dataset such as using linear regressions, gradient boosted trees, or neural networks. **机器学习（Machine Learning）：** 在数据集上执行预测模型，如使用线性回归、梯度增强树或神经网络。

Performing such quantitative tasks on datasets is why OpenAI’s Advanced Data Analysis plugin exists, so that programming languages step in to run code for such tasks on a dataset.正是为了执行这些量化任务，OpenAI 推出了高级数据分析插件，以便通过编程语言在数据集上运行代码。

**So, why would anyone want to analyze datasets using only LLMs and without such plugins?****那么，为什么还有人想仅用 LLMs 来分析数据集而不用这些插件呢？**

## Types of dataset analysis that LLMs are great at
LLM 擅长的数据集分析类型

LLMs are excellent at identifying patterns and trends. This capability stems from their extensive training on diverse and voluminous data, enabling them to discern intricate patterns that may not be immediately apparent.LLMs 在识别模式和趋势方面表现出色。这得益于它们在庞大且多样化的数据上接受的广泛训练，能够洞察到复杂的模式，这些模式可能不是一眼就能看出来的。

This makes them well-suited for tasks based on pattern-finding within datasets, such as:这使它们非常适合执行基于模式查找的任务，例如：

- **Anomaly detection:** Identifying unusual data points that deviate from the norm, based on one or more column values. **异常检测：** 基于一个或多个列值，识别偏离常态的异常数据点。
- **Clustering:** Grouping data points with similar characteristics across columns.**聚类：** 将具有相似特征的数据点按列分组。
- **Cross-Column Relationships:** Identifying combined trends across columns. **跨列关系：** 识别各列之间的联合趋势。
- **Textual Analysis (**For text-based columns): Categorization based on topic or sentiment. **文本分析（适用于文本列）：** 根据主题或情感进行分类。
- **Trend Analysis** (For datasets with time aspects): Identifying patterns, seasonal variations, or trends within columns across time.**趋势分析（针对有时间维度的数据集）：** 识别列中的模式、季节性变化或趋势。

For such pattern-based tasks, using LLMs alone may in fact produce better results within a shorter timeframe than using code! Let’s illustrate this fully with an example.对于这些基于模式的任务，单独使用 LLMs 可能实际上会在更短的时间内比使用编程代码产生更好的结果！接下来，我们将通过一个例子来详细说明这一点。

## Analyzing a Kaggle dataset using only LLMs仅使用 LLM 分析 Kaggle 数据集

We’ll use a popular real-world [Kaggle dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) curated for Customer Personality Analysis, wherein a company seeks to segment its customer base in order to understand its customers better.我们将使用一个流行的实际[Kaggle 数据集](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)，该数据集专为客户个性分析而设计，帮助公司对客户基础进行细分，从而更好地了解客户。

For easier validation of the LLM’s analysis later, we’ll subset this dataset to 50 rows and retain only the most relevant columns. After which, the dataset for analysis looks like this, where each row represents a customer, and the columns depict customer information:为了之后验证 LLM 分析的方便，我们将这个数据集缩减至 50 行，并仅保留最相关的几列。缩减后的数据集如下所示，每一行代表一位客户，各列展示了客户的相关信息：

![](https://miro.medium.com/v2/resize:fit:1400/1*7WRn3k5heJmD8DWAHHwM5A.png)

First 3 rows of dataset — Image by author数据集前三行 —— 图片由作者提供

Say you work on the company’s marketing team. You are tasked to utilize this dataset of customer information to guide marketing efforts. This is a 2-step task: First, use the dataset to generate meaningful customer segments. Next, generate ideas on how to best market towards each segment. Now this is a practical business problem where the pattern-finding (for step 1) capability of LLMs can truly excel.设想你是公司营销团队的一员，你的任务是利用这份客户信息数据集来指导营销活动。这是一个分两步的任务：首先，利用数据集生成有意义的客户细分；其次，针对每个细分提出最佳的市场营销策略。这是一个实际的商业问题，其中第一步的模式识别能力是 LLM 可以大显身手的地方。

Let’s craft a prompt for this task as follows, using 4 prompt engineering techniques ([more on these later!](https://medium.com/towards-data-science/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#544b)): 
我们将按以下方式设计任务提示，采用四种提示工程技术（[更多详情](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41#544b)）：
1. Breaking down a complex task into simple steps 将复杂任务分解成简单步骤； 
2. Referencing intermediate outputs from each step  引用每个步骤的中间输出；
3. Formatting the LLM’s response  格式化 LLM 的回答；
4. Separating the instructions from the dataset将指令与数据集分离。

> **_System Prompt:
> I want you to act as a data scientist to analyze datasets. Do not make up information that is not in the dataset. For each analysis I ask for, provide me with the exact and definitive answer and do not provide me with code or instructions to do the analysis on other platforms.
> 
> **_Prompt:_  
> **# CONTEXT #  
> I sell wine. I have a dataset of information on my customers: [year of birth, marital status, income, number of children, days since last purchase, amount spent].
> 
> #############
> 
> # OBJECTIVE #  
> I want you use the dataset to cluster my customers into groups and then give me ideas on how to target my marketing efforts towards each group. Use this step-by-step process and do not use code:
> 
> 1. CLUSTERS: Use the columns of the dataset to cluster the rows of the dataset, such that customers within the same cluster have similar column values while customers in different clusters have distinctly different column values. Ensure that each row only belongs to 1 cluster.  
>   
> For each cluster found,  
> 2. CLUSTER_INFORMATION: Describe the cluster in terms of the dataset columns.  
> 3. CLUSTER_NAME: Interpret [CLUSTER_INFORMATION] to obtain a short name for the customer group in this cluster.  
> 4. MARKETING_IDEAS: Generate ideas to market my product to this customer group.  
> 5. RATIONALE: Explain why [MARKETING_IDEAS] is relevant and effective for this customer group.
> 
> #############
> 
> # STYLE #  
> Business analytics report
> 
> #############
> 
> # TONE #  
> Professional, technical
> 
> #############
> 
> # AUDIENCE #  
> My business partners. Convince them that your marketing strategy is well thought-out and fully backed by data.
> 
> #############
> 
> # RESPONSE: MARKDOWN REPORT #  
> <For each cluster in [CLUSTERS]>  
> — Customer Group: [CLUSTER_NAME]  
> — Profile: [CLUSTER_INFORMATION]  
> — Marketing Ideas: [MARKETING_IDEAS]  
> — Rationale: [RATIONALE]
> 
> <Annex>  
> Give a table of the list of row numbers belonging to each cluster, in order to back up your analysis. Use these table headers: [[CLUSTER_NAME], List of Rows].
> 
> #############
> 
> # START ANALYSIS #  
> If you understand, ask me for my dataset.


> **_系统提示：_**  
我希望你扮演数据科学家的角色来分析数据集。不要编造数据集中不存在的信息。对于我提出的每个分析要求，提供确切且确定的答案，不要提供代码或指导在其他平台上进行分析的方法。

**_提示：_**  
# CONTEXT #  
我销售葡萄酒。我手头有一个客户信息数据集：[出生年份，婚姻状况，收入，子女数量，上次购买至今天数，消费金额]。

#############

# OBJECTIVE #  
我希望你利用这个数据集将我的客户分组，并为每个群组制定营销策略。遵循以下分步骤，且不使用代码：

1. CLUSTERS: 根据数据集的列将客户分组，确保同一群组内的客户在列值上相似，不同群组的客户在列值上明显不同。确保每一行数据只属于一个群组。

对于每个发现的群组，  
2. CLUSTER_INFORMATION: 根据数据集的列来描述群组。  
3. CLUSTER_NAME: 根据[CLUSTER_INFORMATION]解读得出该客户群组的简称。  
4. MARKETING_IDEAS: 提出针对该客户群组的市场营销策略。  
5. RATIONALE: 解释为什么[MARKETING_IDEAS]对这个客户群组有效且相关。

#############

# STYLE #  
商业分析报告

#############

# TONE #  
专业、技术性

#############

# AUDIENCE #  
我的商业伙伴们。让他们相信你的营销策略是深思熟虑的，并且有充分的数据支持。

#############

# RESPONSE: MARKDOWN REPORT #  
<对[CLUSTERS]中的每一个群组> — 客户群组：[CLUSTER_NAME] — 群组档案：[CLUSTER_INFORMATION] — 营销策略：[MARKETING_IDEAS] — 理由：[RATIONALE]

<附录>  
提供一个表格，列出每个群组中的行号，以支持你的分析。表头如下：[[CLUSTER_NAME], 行号列表]。

#############

# START ANALYSIS #  
如果你已经明白，请向我索要我的数据集。

Below is GPT-4’s reply, and we proceed to pass the dataset to it in a CSV string.
下面是 GPT-4 的回复，我们将继续将数据集以 CSV 字符串的形式传递给它。
![](https://miro.medium.com/v2/resize:fit:1400/1*sn6omL9-NITqwVEviMEKug.png)

GPT-4's response — Image by author

Following which, GPT-4 replies with its analysis in the markdown report format we asked for:
随后，GPT-4 按照我们要求的标记符报告格式回复了分析结果：

![](https://miro.medium.com/v2/resize:fit:1332/1*vwSrP7cmlYcxBdbtfOQUhw.png)

GPT-4's response — Image by author

![](https://miro.medium.com/v2/resize:fit:1334/1*NS46eluVmA515GuP6p3k_Q.png)

GPT-4's response — Image by author

![](https://miro.medium.com/v2/resize:fit:1334/1*3RYAZQXRkbidn0iSoCJxnw.png)

GPT-4's response — Image by author

## Validating the LLM’s analysis验证大语言模型的分析能力

For the sake of brevity, we’ll pick 2 customer groups generated by the LLM for validation — say, Young Families and Discerning Enthusiasts.为了简洁，我们选择两个由大语言模型生成的客户群体进行验证——“年轻家庭”和“挑剔的爱好者”。

**Young Families**  
- Profile synthesized by LLM: Born after 1980, Married or Together, Moderate to low income, Have children, Frequent small purchases.  
- Rows clustered into this group by LLM: 3, 4, 7, 10, 16, 20  
- Digging into the dataset, the full data for these rows are:
为了简洁，我们选择两个由大语言模型生成的客户群体进行验证——“年轻家庭”和“挑剔的爱好者”。

**年轻家庭** - 大语言模型生成的描述：出生于 1980 年后，已婚或同居，中等偏低的收入，育有孩子，常做小额消费。 - 此群体包括的数据行：3、4、7、10、16、20 - 深入查看这些数据行的详细信息，结果显示：
![](https://miro.medium.com/v2/resize:fit:1400/1*n5vX8URk1PKCiVYNd_amXg.png)

Full data for Young Families — Image by author年轻家庭的完整数据 — 作者图片

Which exactly correspond to the profile identified by the LLM. It was even able to cluster the row with a null value without us preprocessing it beforehand!
这些数据完美对应大语言模型确定的用户描述。该模型甚至能够识别包含空值的数据行，而无需我们预先处理！
**Discerning Enthusiasts  
**- Profile synthesized by LLM: Wide age range, Any marital status, High income, Varied children status, High spend on purchases.  
- Rows clustered into this group by LLM: 2, 5, 18, 29, 34, 36  
- Digging into the dataset, the full data for these rows are:
**挑剔的爱好者** - 大语言模型生成的描述：年龄跨度广泛，不限婚姻状况，高收入，孩子情况不一，高消费水平。 - 此群体包括的数据行：2、5、18、29、34、36 - 深入查看这些数据行的详细信息，结果显示：
![](https://miro.medium.com/v2/resize:fit:1400/1*j1Se_C5CbxxZKZlhOz1l3Q.png)

Full data for Discerning Enthusiasts — Image by author挑剔的爱好者的完整数据 — 作者图片

Which again align very well with the profile identified by the LLM!这些数据再次精准匹配大语言模型确定的用户描述

This example showcases LLMs’ abilities in pattern-finding, interpreting and distilling multi-dimensional datasets into meaningful insights, while ensuring that its analysis is deeply rooted in the factual truth of the dataset.本例展示了大语言模型在识别模式、解读及简化多维数据集以提炼出有意义的洞见方面的强大能力，确保其分析结果扎根于数据的真实情况。

## What if we used **ChatGPT’s Advanced Data Analysis plugin?**使用 ChatGPT 的高级数据分析插件会如何？

For completeness, I attempted this same task with the same prompt, but asked ChatGPT to execute the analysis using code instead, which activated its Advanced Data Analysis plugin. The idea was for the plugin to run code using a clustering algorithm like K-Means directly on the dataset to obtain each customer group, before synthesizing the profile of each cluster to provide marketing strategies.为了全面考虑，我使用同一提示尝试了相同的任务，不过这次我让 ChatGPT 通过编程方式进行分析，启用了其高级数据分析插件。插件应用 K-均值等聚类算法直接对数据集进行处理，以便划分不同的客户群体，并据此制定营销策略。

However, multiple attempts resulted in the following error messages with no outputs, despite the dataset being only 50 rows:尽管数据集仅含 50 行，多次尝试均显示错误信息且未产生任何结果：

![](https://miro.medium.com/v2/resize:fit:1154/1*ouYNaR56ptHhV9iUwF8ipg.png)

Error and no output from Attempt 1 — Image by author尝试 1 的错误和无输出 — 作者图片

![](https://miro.medium.com/v2/resize:fit:1400/1*_IexjpKEgRwnYzn7m7abHQ.jpeg)

Error and no output from Attempt 2 — Image by author尝试 2 的错误和无输出 — 作者图片

With the Advanced Data Analysis plugin right now, it appears that executing simpler tasks on datasets such as calculating descriptive statistics or creating graphs can be easily achieved, but more advanced tasks that require computing of algorithms may sometimes result in errors and no outputs, due to computational limits or otherwise.当前情况表明，虽然高级数据分析插件能够轻松完成一些简单任务，如统计描述或生成图表，但在执行需要较大计算量的高级任务时，有时可能因为计算限制或其他原因而发生错误，导致无法输出结果。

## So…When to analyze datasets using LLMs?
 那么…何时应当用大语言模型 (LLM) 来分析数据集？
 
The answer is it depends on the type of analysis.
答案因分析的具体类型而异。
For tasks requiring precise mathematical calculations or complex, rule-based processing, conventional programming methods remain superior.对于需要精确的数学运算或复杂的规则处理的任务，传统的编程方法依然更加适用。

For tasks based on pattern-recognition, it can be challenging or more time-consuming to execute using conventional programming and algorithmic approaches. LLMs, however, excel at such tasks, and can even provide additional outputs such as annexes to back up its analysis, and full analysis reports in markdown formatting.而对于依赖模式识别的任务，传统的编程和算法处理可能更加困难且耗时。大语言模型在这类任务中表现优异，能提供包括分析附件在内的额外输出，并能生成 Markdown 格式的完整分析报告。

> Ultimately, the decision to utilize LLMs hinges on the nature of the task at hand, balancing the strengths of LLMs in pattern-recognition against the precision and specificity offered by traditional programming techniques.
> 总的来说，是否采用大语言模型取决于任务本身的性质，需要平衡其在模式识别上的强项与传统编程技术提供的精确度和特定性。

## Now back to the prompt engineering!回到提示工程环节！

Before this section ends, let’s go back to the prompt used to generate this dataset analysis and break down the key prompt engineering techniques used:在本节结束前，让我们重新审视用于生成此数据分析的提示，并详细解析关键的提示工程技巧：

> **_Prompt:_**  
> # CONTEXT #  
> I sell wine. I have a dataset of information on my customers: [year of birth, marital status, income, number of children, days since last purchase, amount spent].
> 
> #############
> 
> # OBJECTIVE #  
> I want you use the dataset to cluster my customers into groups and then give me ideas on how to target my marketing efforts towards each group. Use this step-by-step process and do not use code:
> 
> 1. CLUSTERS: Use the columns of the dataset to cluster the rows of the dataset, such that customers within the same cluster have similar column values while customers in different clusters have distinctly different column values. Ensure that each row only belongs to 1 cluster.  
>   
> For each cluster found,  
> 2. CLUSTER_INFORMATION: Describe the cluster in terms of the dataset columns.  
> 3. CLUSTER_NAME: Interpret [CLUSTER_INFORMATION] to obtain a short name for the customer group in this cluster.  
> 4. MARKETING_IDEAS: Generate ideas to market my product to this customer group.  
> 5. RATIONALE: Explain why [MARKETING_IDEAS] is relevant and effective for this customer group.
> 
> #############
> 
> # STYLE #  
> Business analytics report
> 
> #############
> 
> # TONE #  
> Professional, technical
> 
> #############
> 
> # AUDIENCE #  
> My business partners. Convince them that your marketing strategy is well thought-out and fully backed by data.
> 
> #############
> 
> # RESPONSE: MARKDOWN REPORT #  
> <For each cluster in [CLUSTERS]>  
> — Customer Group: [CLUSTER_NAME]  
> — Profile: [CLUSTER_INFORMATION]  
> — Marketing Ideas: [MARKETING_IDEAS]  
> — Rationale: [RATIONALE]
> 
> <Annex>  
> Give a table of the list of row numbers belonging to each cluster, in order to back up your analysis. Use these table headers: [[CLUSTER_NAME], List of Rows].
> 
> #############
> 
> # START ANALYSIS #  
> If you understand, ask me for my dataset.


**_提示:_**  
# CONTEXT #  
我经营葡萄酒生意。我手头有一份包含客户信息的数据集：[出生年份，婚姻状况，收入，子女数目，自上次购买至今天数，消费金额]。

#############

# OBJECTIVE #  
我希望你利用这份数据集将我的客户进行分组，随后为我提供针对每个群体的市场营销策略。请按以下步骤操作，且不要编写代码：

1. CLUSTERS: 利用数据集中的列值对行数据进行聚类，确保同一聚类内的客户在列值上保持相似，而不同聚类的客户则明显不同。确保每一行数据只属于一个聚类。

对于每个确定的聚类，  
2. CLUSTER_INFORMATION: 描述聚类的特征。  
3. CLUSTER_NAME: 根据[CLUSTER_INFORMATION]解读，为这个客户群体起一个简称。  
4. MARKETING_IDEAS: 提出针对此群体的营销策略。  
5. RATIONALE: 解释这些[MARKETING_IDEAS]为何对此群体有效。

#############

# STYLE #  
商业分析报告

#############

# TONE #  
专业，技术性

#############

# AUDIENCE #  
面向我的商业伙伴。让他们确信你的营销策略是经过深思熟虑的，并完全得到数据支持。

#############

# RESPONSE: MARKDOWN REPORT #  
<对于[CLUSTERS]中的每个聚类>  
— 客户群组：[CLUSTER_NAME]  
— 简介：[CLUSTER_INFORMATION]  
— 营销想法：[MARKETING_IDEAS]  
— 理由：[RATIONALE]

<附录> 提供一个表格，记录每个聚类的行号，以佐证你的分析。表头如下：[[CLUSTER_NAME], 行号列表]。

#############

# START ANALYSIS #  
如果你已经理解，请向我请求我的数据集。

T**echnique 1: Breaking down a complex task into simple steps   技巧 1：将复杂任务简化成步骤
**LLMs are great at performing simple tasks, but not so great at complex ones. As such, with complex tasks like this one, it is important to break down the task into simple step-by-step instructions for the LLM to follow. The idea is to give the LLM the steps that you yourself would take to execute the task.
大语言模型（LLM）擅长处理简单的任务，对于复杂的任务则表现不佳。因此，在面对复杂任务时，把它分解成一步步简单的指令是至关重要的。这种方法的核心思想是，明确告知 LLM 你自己执行该任务时会采取的每一个步骤。

In this example, the steps are given as:
例如，具体步骤如下：
> Use this step-by-step process and do not use code:
> 
> 1. CLUSTERS: Use the columns of the dataset to cluster the rows of the dataset, such that customers within the same cluster have similar column values while customers in different clusters have distinctly different column values. Ensure that each row only belongs to 1 cluster.  
>   
> For each cluster found,  
> 2. CLUSTER_INFORMATION: Describe the cluster in terms of the dataset columns.  
> 3. CLUSTER_NAME: Interpret [CLUSTER_INFORMATION] to obtain a short name for the customer group in this cluster.  
> 4. MARKETING_IDEAS: Generate ideas to market my product to this customer group.  
> 5. RATIONALE: Explain why [MARKETING_IDEAS] is relevant and effective for this customer group.

***
> 请按照这个步骤操作，不要使用编码：

1. **数据聚类（CLUSTERS）**：利用数据集的各列特征，将数据行进行聚类，确保同一聚类中的客户在这些特征上相似，而不同聚类的客户则明显不同。每条数据只能属于一个聚类。

对于每个聚类，  
2. **聚类描述（CLUSTER_INFORMATION）**：描述聚类的特点。  
3. **聚类命名（CLUSTER_NAME）**：根据聚类描述，为这个客户群体起一个简洁的名字。  
4. **营销策略（MARKETING_IDEAS）**：为这个客户群体制定营销策略。  
5. **策略解释（RATIONALE）**：说明为什么这些营销策略对这个客户群体有效。

As opposed to simply giving the overall task to the LLM as “Cluster the customers into groups and then give ideas on how to market to each group”.

With step-by-step instructions, LLMs are significantly more likely to deliver the correct results.
这样的分步指导，比起直接要求 LLM“对客户进行分组并提出营销策略”的方式，能显著提高其输出的准确性。

T**echnique 2: Referencing intermediate outputs from each step 技巧 2：标记并引用中间输出
**When providing the step-by-step process to the LLM, we give the intermediate output from each step a capitalized `VARIABLE_NAME`, namely `CLUSTERS`, `CLUSTER_INFORMATION`, `CLUSTER_NAME`, `MARKETING_IDEAS` and `RATIONALE`.
在提供步骤时，我们会用大写字母标记每个步骤的输出，例如`数据聚类（CLUSTERS）`、`聚类描述（CLUSTER_INFORMATION）`、`聚类命名（CLUSTER_NAME）`、`营销策略（MARKETING_IDEAS）`和`策略解释（RATIONALE）`。这样做是为了区分指令中的变量名和其他文本，方便后续引用这些中间输出。

Capitalization is used to differentiate these variable names from the body of instructions given. These intermediate outputs can later be referenced using square brackets as `[VARIABLE_NAME]`.

T**echnique 3: Formatting the LLM’s response  技巧 3：优化响应格式
**Here, we ask for a markdown report format, which beautifies the LLM’s response. Having variable names from intermediate outputs again comes in handy here to dictate the structure of the report.此处我们请求一个 Markdown 格式的报告，以增强响应的可读性和结构性。利用中间步骤的变量名，可以明确报告的构架。

> # RESPONSE: MARKDOWN REPORT #  
> <For each cluster in [CLUSTERS]>  
> — Customer Group: [CLUSTER_NAME]  
> — Profile: [CLUSTER_INFORMATION]  
> — Marketing Ideas: [MARKETING_IDEAS]  
> — Rationale: [RATIONALE]
> 
> <Annex>  
> Give a table of the list of row numbers belonging to each cluster, in order to back up your analysis. Use these table headers: [[CLUSTER_NAME], List of Rows].
> # 响应：Markdown 报告 #  
<对每个数据聚类[数据聚类（CLUSTERS）]>  
— 客户群体：[聚类命名（CLUSTER_NAME）]  
— 群体特征：[聚类描述（CLUSTER_INFORMATION）]  
— 营销策略：[营销策略（MARKETING_IDEAS）]  
— 策略说明：[策略解释（RATIONALE）]

<附录> 提供一个表格，记录每个聚类包含的数据行号，以验证分析的准确性。表格标题为：[聚类命名（CLUSTER_NAME）, 行号列表]。

In fact, you could even subsequently ask ChatGPT to provide the report as a downloadable file, allowing you to work off of its response in writing your final report.
此外，你还可以让 ChatGPT 将报告以可下载文件形式提供，便于你在编写最终报告时参考使用。

![](https://miro.medium.com/v2/resize:fit:1400/1*-rALQn7TirQZzxvGG0BT5w.png)

Saving GPT-4's response as a file — Image by author保存 GPT-4 的回答为文件

T**echnique 4: Separating the task instructions from the dataset**  技巧 4：将任务指令与数据集分离
You’ll notice that we never gave the dataset to the LLM in our first prompt. Instead, the prompt gives only the task instructions for the dataset analysis, with this added to the bottom:在我们的首个提示中，你会发现我们并没有直接将数据集交给大语言模型（LLM）。反而，提示只给出了数据集分析的任务指令，并在底部添加了这样的话

> # START ANALYSIS #  
> If you understand, ask me for my dataset.

> # START ANALYSIS #  
如果你明白了，请向我请求数据集。

ChatGPT then responded that it understands, and we passed the dataset to it as a CSV string in our next prompt:
随后 ChatGPT 表示它已理解，并在下一个提示中，我们通过 CSV 字符串的形式将数据集传递给它：

![](https://miro.medium.com/v2/resize:fit:1400/1*sn6omL9-NITqwVEviMEKug.png)

GPT-4's response — Image by author

**But why separate the instructions from the dataset?****但为什么需要将指令与数据集分开处理呢？**

Doing so helps the LLM maintain clarity in understanding each, with lower likelihood of missing out information, especially in more complex tasks such as this one with longer instructions. You might have experienced scenarios where the LLM “accidentally forgets” a certain instruction you gave as part of a longer prompt — for example, if you asked for a 100-word response and the LLM gives you a longer paragraph back. By receiving the instructions first, before the dataset that the instructions are for, the LLM can first digest what it should do, before executing it on the dataset provided next.这样做可以帮助大语言模型更清晰地理解各自的内容，降低遗漏信息的风险，尤其是在指令较多且复杂的任务中。你可能遇到过这样的情况：在一个长的提示中提出的某个指令被“偶然遗忘”了——例如，你请求一个 100 字的回答，但大语言模型却给出了更长的段落。通过先接收指令，再处理这些指令所对应的数据集，大语言模型可以更好地消化它应该做的事情，然后再执行相关的数据操作。

Note however that this separation of instructions and dataset can only be achieved with chat LLMs as they maintain a conversational memory, unlike completion LLMs which do not.值得注意的是，这种指令与数据集的分离只能在可以维护对话记忆的聊天型大语言模型中实现，而非那些没有这种记忆功能的完成型模型。

# Closing Thoughts 结语

Before this article ends, I wanted to share some personal reflections on this incredible journey.在本文结束之前，我想分享一些关于这次非凡旅程的个人思考。

First, a heartfelt thank you to GovTech Singapore for orchestrating such an amazing competition. If you’re interested in the mechanics of how GovTech organized this first-of-its-kind competition — check out [this article](https://go.gov.sg/how-govtech-designed-promptroyale2023) by Nicole Lee, the lead organizer herself!首先，我要衷心感谢 GovTech Singapore 精心策划这场精彩的比赛。如果你对 GovTech 如何组织这场独一无二的比赛感兴趣，可以阅读 Nicole Lee——比赛的主要组织者撰写的[这篇文章](https://go.gov.sg/how-govtech-designed-promptroyale2023)。

![](https://miro.medium.com/v2/resize:fit:1400/1*cESnPetMGa2ctf41QyN17A.jpeg)

A live on-stage battle in the final round!

Second, a big shout-out to my fellow phenomenal competitors, who each brought something special, making the competition as enriching as it was challenging! I’ll never forget the final round, with us battling it out on stage and a live audience cheering us on — an experience I’ll always remember fondly.其次，我要向那些出色的竞争对手们致以最高的敬意，每个人都展现了特别的才能，让这场比赛既充满挑战又富有成效！我永远不会忘记决赛那一刻，我们在舞台上激烈竞争，现场观众的欢呼声——这是我将一直珍视的记忆。

For me, this wasn’t just a competition; it was a celebration of talent, creativity, and the spirit of learning. And I’m beyond excited to see what comes next!对我而言，这不只是一场比赛；这是一次才华、创造力及学习精神的盛会。我对未来充满期待，并激动于即将到来的一切！

I had a lot of fun writing this, and if you had fun reading, I would really appreciate if you took a second to leave some claps and a follow!撰写本文让我感到非常愉快，如果你在阅读时也享受这份乐趣，希望你能花一点时间点赞并关注！

See you in the next one!  
Sheila期待下一次的相遇！Sheila

[

Data Science

](https://medium.com/tag/data-science?source=post_page-----34c195a93d41---------------data_science-----------------)

[

Artificial Intelligence

](https://medium.com/tag/artificial-intelligence?source=post_page-----34c195a93d41---------------artificial_intelligence-----------------)

[

Prompt Engineering

](https://medium.com/tag/prompt-engineering?source=post_page-----34c195a93d41---------------prompt_engineering-----------------)

[

Editors Pick

](https://medium.com/tag/editors-pick?source=post_page-----34c195a93d41---------------editors_pick-----------------)

[

Technology

](https://medium.com/tag/technology?source=post_page-----34c195a93d41---------------technology-----------------)

































