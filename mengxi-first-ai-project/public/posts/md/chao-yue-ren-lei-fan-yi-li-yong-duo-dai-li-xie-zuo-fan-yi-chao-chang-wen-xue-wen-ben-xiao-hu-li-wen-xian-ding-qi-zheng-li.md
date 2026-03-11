---
title: "超越人类翻译：利用多代理协作翻译超长文学文本(小狐狸文献定期整理)"
date: 2024-05-22
tags: []
category: "obsidian"
badge: "obsidian"
---

**(PERHAPS) BEYOND HUMAN TRANSLATION: HARNESSING MULTI-AGENT COLLABORATION FOR TRANSLATING ULTRA-LONG LITERARY TEXTS**

  

**(或许) 超越人类翻译：利用多代理协作翻译超长文学文本**

  

**作者 (Authors)**

  

Minghao Wu1, Yulin Yuan2, Gholamreza Haffari1, Longyue Wang3

  

1. Monash University

2. University of Macau

3. Tencent AI Lab

  

**摘要 (Abstract)**

  

Recent advancements in machine translation (MT) have significantly enhanced translation quality across various domains. However, the translation of literary texts remains a formidable challenge due to their complex language, figurative expressions, and cultural nuances. In this work, we introduce a novel multi-agent framework based on large language models (LLMs) for literary translation, implemented as a company called TRANSAGENTS, which mirrors the traditional translation publication process by leveraging the collective capabilities of multiple agents, to address the intricate demands of translating literary works. To evaluate the effectiveness of our system, we propose two innovative evaluation strategies: Monolingual Human Preference (MHP) and Bilingual LLM Preference (BLP). MHP assesses translations from the perspective of monolingual readers of the target language, while BLP uses advanced LLMs to compare translations directly with the original texts. Empirical findings indicate that despite lower d-BLEU scores, translations from TRANSAGENTS are preferred by both human evaluators and LLMs over human-written references, particularly in genres requiring domain-specific knowledge. We also highlight the strengths and limitations of TRANSAGENTS through case studies and suggests directions for future research.

  

近些年，机器翻译（MT）的进展显著提升了各领域的翻译质量。然而，文学文本的翻译仍然是一个巨大的挑战，因为它们语言复杂，包含比喻表达和文化细微差别。在这项工作中，我们介绍了一种基于大型语言模型（LLMs）的新型多代理框架用于文学翻译，称为TRANSAGENTS。这一框架借鉴传统翻译出版流程，通过多个代理的协同能力来应对文学作品翻译的复杂需求。为了评估我们系统的效果，我们提出了两种创新的评估策略：单语人类偏好（MHP）和双语LLM偏好（BLP）。MHP从目标语言的单语读者的角度评估翻译，而BLP使用高级LLMs直接将翻译与原文进行比较。实证研究表明，尽管d-BLEU分数较低，TRANSAGENTS的翻译更受人类评估者和LLMs的青睐，特别是在需要特定领域知识的体裁中。我们还通过案例研究展示了TRANSAGENTS的优势和局限性，并提出了未来研究的方向。

  

**引言 (Introduction)**

  

Machine translation (MT) has achieved remarkable advancements in recent years, driven by breakthroughs in deep learning and neural networks. Despite these technological strides, literary translation remains an unresolved challenge for MT systems. Literary texts, characterized by their complex language, figurative expressions, cultural nuances, and unique stylistic elements, pose significant hurdles that are hard for machines to overcome. This complexity makes literary translation one of the most challenging areas within machine translation, often referred to as “the last frontier of machine translation”.

  

机器翻译（MT）近年来在深度学习和神经网络的突破推动下取得了显著进展。然而，文学翻译仍然是MT系统未解决的挑战之一。文学文本以其语言复杂性、比喻表达、文化细微差别和独特的风格元素为特征，构成了机器难以逾越的障碍。这种复杂性使得文学翻译成为机器翻译中最具挑战性的领域之一，被称为“机器翻译的最后堡垒”。

  

In response to complex challenges across various domains, recent research in multi-agent systems, particularly those powered by large language models (LLMs), has shown significant promise. These systems leverage the collective intelligence of multiple agents, enabling superior problem-solving capabilities compared to individual model approaches. Multi-agent systems excel in dynamic environments where intricate problem-solving and collaborative efforts are required.

  

在应对各领域复杂挑战的过程中，基于大型语言模型（LLMs）的多代理系统显示出显著的前景。多代理系统通过多个代理的集体智能，相较于单一模型方法在复杂问题解决上表现出色。鉴于文学翻译的复杂性，我们利用多代理系统的优势，建立了一个新型的多代理文学翻译公司，称为TRANSAGENTS。TRANSAGENTS的翻译过程分为两个主要阶段，每个阶段包含若干子阶段。首先，由我们的预定义CEO代理选择一名高级编辑，后者根据客户的具体需求组建团队，团队成员包括初级编辑、翻译、地方化专家和校对员。各团队成员通过多种协作策略改进和优化翻译输出。

  

**公司概况 (Company Overview)**

  

To simulate the entire book translation process, in addition to the designated CEO, we have a diverse array of roles, including senior editors, junior editors, translators, localization specialists, and proofreaders in our company TRANSAGENTS. Each of these roles carries its own set of responsibilities:

  

为了模拟整个书籍翻译过程，除了指定的CEO，我们在TRANSAGENTS中拥有多样化的角色，包括高级编辑、初级编辑、翻译、地方化专家和校对员。每个角色都有自己的职责：

  

• Senior Editors: Senior editors are responsible for overseeing the content production process. Their primary duties encompass setting editorial standards, guiding junior editors, and ensuring that the content aligns with the company’s objectives.

• 高级编辑：负责监督内容制作过程，设置编辑标准，指导初级编辑，并确保内容符合公司的目标。

• Junior Editors: Junior editors work closely under the guidance of senior editors. Their responsibilities typically include managing the day-to-day editorial workflow, editing content, and assisting in content planning. They also handle communications with various other roles within the organization.

• 初级编辑：在高级编辑的指导下工作，负责日常编辑工作流程，编辑内容，协助内容规划，并处理与组织内各角色的沟通。

• Translators: Translators are tasked with converting written material from one language to another while preserving the tone, style, and context of the original text. Translators must possess a profound understanding of both the source and target languages, as well as a familiarity with the subject matter they are translating.

• 翻译：负责将书面材料从一种语言转换为另一种语言，同时保持原文的语气、风格和上下文。翻译必须深刻理解源语言和目标语言，并熟悉所翻译的主题。

• Localization Specialists: Localization specialists go beyond simple translation; they adapt content for specific regions or markets. This role involves not only translating language but also adjusting cultural references, idioms, and images to resonate with local audiences.

• 地方化专家：不仅仅是翻译语言，还需要调整文化参考、习语和图像，使其符合当地受众的习惯。

• Proofreaders: Proofreaders perform final checks for grammar, spelling, punctuation, and formatting errors. Their role is crucial in ensuring that content is polished and adheres to high-quality standards before publication.

• 校对员：执行最后的语法、拼写、标点和格式错误检查，确保内容在发布前达到高质量标准。

  

**评估策略 (Evaluation Strategies)**

  

We propose two innovative evaluation strategies:

  

我们提出了两种创新的评估策略：

  

1. **Monolingual Human Preference (MHP)**: The Monolingual Human Preference strategy simulates the realistic scenario of reading a translated work. It engages human evaluators from the target audience who assess translations without the influence of the original text.

**单语人类偏好（MHP）**：模拟目标语言读者的真实阅读场景，由目标受众的人类评估者在没有原文影响的情况下评估翻译。

2. **Bilingual LLM Preference (BLP)**: The Bilingual LLM Preference uses advanced LLMs to compare translations directly with the original texts, leveraging the superior translation capabilities of advanced LLMs.

**双语LLM偏好（BLP）**：利用高级LLMs直接将翻译与原文进行比较，借助先进LLMs的翻译能力，减轻参考翻译不完美的影响。

  

**实验设置 (Experimental Setup)**

  

Our experimental setup primarily follows the WMT2023 shared task on discourse-level literary translation (DLLT), including baseline models, datasets, and evaluation approaches.

  

我们主要遵循WMT2023在话语级文学翻译（DLLT）共享任务中的实验设置，包括基线模型、数据集和评估方法。基线模型包括LLAMA-MT、GPT-4、GOOGLE TRANSLATE、DUT和HW-TSC等。

  

**TRANSAGENTS翻译工作流程 (Translation Workflow of TRANSAGENTS)**

  

The translation workflow is divided into preparation and execution phases. The preparation phase includes project member selection and translation guideline documentation, while the execution phase includes translation, cultural adaptation, proofreading, and final review.

  

翻译工作流程分为准备阶段和执行阶段。准备阶段包括项目成员选择和翻译指南文件编制，执行阶段包括翻译、文化适应、校对和最终审查。


**实验结果 (Experimental Results)**

  

We present the performance of TRANSAGENTS in terms of d-BLEU scores and through preference evaluations by human evaluators and large language models (LLMs). Despite the lower d-BLEU scores, the translations produced by TRANSAGENTS are more preferred by evaluators.

  

我们展示了TRANSAGENTS在d-BLEU分数上的表现，并通过人类和LLM的偏好评估，发现尽管d-BLEU分数较低，TRANSAGENTS的翻译更受评估者的青睐。

  

**案例研究 (Case Study)**

  

Through case studies, we highlight the strengths and weaknesses of TRANSAGENTS in cultural adaptation and content omission, supported by insights from professional translators.

  

通过案例研究展示了TRANSAGENTS在文化适应和内容遗漏方面的优势和局限性，并结合专业翻译员的意见进行深入分析。

  

**结论 (Conclusion)**

  

TRANSAGENTS demonstrates the potential of multi-agent collaboration in translating literary texts. Despite some performance drawbacks in certain evaluation metrics, it performs well in actual preference evaluations, indicating its effectiveness in handling complex translation tasks.

  

TRANSAGENTS展示了通过多代理协作来翻译文学文本的潜力，尽管在某些评估标准下表现不佳，但在实际偏好评估中表现优异，显示出其在处理复杂翻译任务中的有效性。
