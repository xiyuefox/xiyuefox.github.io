---
title: "O'Reilly系列《Prompt Engineering for Generative AI》By James Phoenix Mike Taylor"
date: 2025-12-16
tags: ["tech", "tutorial", "improvisation"]
categories: ["tech"]
layout: "single" 
---


#  [Preface](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/preface01.html)
    The rapid pace of innovation in generative AI promises to change how we live and work, but it’s getting increasingly difficult to keep up. The number of [AI papers published on arXiv is growing exponentially](https://oreil.ly/EN5ay), [Stable Diffusion](https://oreil.ly/QX-yy) has been among the fastest growing open source projects in history, and AI art tool [Midjourney’s Discord server](https://oreil.ly/ZVZ5o) has tens of millions of members, surpassing even the largest gaming communities. What most captured the public’s imagination was OpenAI’s release of ChatGPT, [which reached 100 million users in two months](https://oreil.ly/FbYWk), making it the fastest-growing consumer app in history. Learning to work with AI has quickly become one of the most in-demand skills.  
生成式人工智能的快速创新有望改变我们的生活和工作方式，但跟上它变得越来越困难。 arXiv 上发表的 AI 论文数量呈指数级增长，Stable Diffusion 已成为历史上增长最快的开源项目之一，AI 艺术工具 Midjourney 的 Discord 服务器拥有数千万会员，甚至超过了最大的游戏社区。最激发公众想象力的是OpenAI发布的ChatGPT，两个月内用户数量就达到1亿，成为历史上增长最快的消费类应用程序。学习使用人工智能已迅速成为最受欢迎的技能之一。

Everyone using AI professionally quickly learns that the quality of the output depends heavily on what you provide as input. The discipline of _prompt engineering_ has arisen as a set of best practices for improving the reliability, efficiency, and accuracy of AI models. “In ten years, half of the world’s jobs will be in prompt engineering,” [claims Robin Li](https://oreil.ly/IdIfO), the cofounder and CEO of Chinese tech giant Baidu. However, we expect prompting to be a skill required of many jobs, akin to proficiency in Microsoft Excel, rather than a popular job title in itself. This new wave of disruption is changing everything we thought we knew about computers. We’re used to writing algorithms that return the same result every time—not so for AI, where the responses are non-deterministic. Cost and latency are real factors again, after decades of Moore’s law making us complacent in expecting real-time computation at negligible cost. The biggest hurdle is the tendency of these models to confidently make things up, dubbed _hallucination_, causing us to rethink the way we evaluate the accuracy of our work.  
每个专业使用人工智能的人都会很快了解到，输出的质量在很大程度上取决于您提供的输入内容。即时工程学科作为一套提高人工智能模型可靠性、效率和准确性的最佳实践而出现。中国科技巨头百度联合创始人兼首席执行官李彦宏表示：“十年内，世界上一半的工作岗位将来自即时工程。”然而，我们预计提示将成为许多工作所需的一项技能，类似于熟练掌握 Microsoft Excel，而不是其本身是一个流行的职位名称。这波新的颠覆浪潮正在改变我们对计算机的一切认识。我们习惯于编写每次返回相同结果的算法，但对于人工智能来说却并非如此，因为人工智能的响应是不确定的。几十年来，摩尔定律让我们沾沾自喜地期望以可忽略不计的成本进行实时计算，成本和延迟再次成为真正的因素。最大的障碍是这些模型倾向于自信地编造事实，这被称为幻觉，导致我们重新思考评估工作准确性的方式。

We’ve been working with generative AI since the GPT-3 beta in 2020, and as we saw the models progress, many early prompting tricks and hacks became no longer necessary. Over time a consistent set of principles emerged that were still useful with the newer models, and worked across both text and image generation. We have written this book based on these timeless principles, helping you learn transferable skills that will continue to be useful no matter what happens with AI over the next five years. The key to working with AI isn’t “figuring out how to hack the prompt by adding one magic word to the end that changes everything else,” as [OpenAI cofounder Sam Altman asserts](https://oreil.ly/oo262), but what will always matter is the “quality of ideas and the understanding of what you want.” While we don’t know if we’ll call it “prompt engineering” in five years, working effectively with generative AI will only become more important.  
自 2020 年 GPT-3 测试版以来，我们一直在研究生成式人工智能，随着我们看到模型的进步，许多早期的提示技巧和技巧变得不再必要。随着时间的推移，出现了一套一致的原则，这些原则对于新模型仍然有用，并且适用于文本和图像生成。我们根据这些永恒的原则编写了这本书，帮助您学习可转移的技能，无论未来五年人工智能发生什么，这些技能都将继续有用。正如 OpenAI 联合创始人萨姆·奥尔特曼 (Sam Altman) 所言，使用人工智能的关键并不在于“弄清楚如何通过在末尾添加一个神奇的单词来改变其他一切来破解提示”，但永远重要的是“想法的质量和理解你想要什么。”虽然我们不知道五年后是否会称之为“即时工程”，但有效地使用生成式人工智能只会变得更加重要。

# Software Requirements for This Book  
本书的软件要求

All of the code in this book is in Python and was designed to be run in a [Jupyter Notebook](https://jupyter.org/) or [Google Colab notebook](https://colab.research.google.com/). The concepts taught in the book are transferable to JavaScript or any other coding language if preferred, though the primary focus of this book is on prompting techniques rather than traditional coding skills. The code can all be [found on GitHub](https://oreil.ly/BrightPool), and we will link to the relevant notebooks throughout. It’s highly recommended that you utilize the [GitHub repository](https://oreil.ly/BrightPool) and run the provided examples while reading the book.  
本书中的所有代码均采用 Python 编写，旨在在 Jupyter Notebook 或 Google Colab Notebook 中运行。书中教授的概念可以转移到 JavaScript 或任何其他编码语言（如果愿意），尽管本书的主要重点是提示技术而不是传统的编码技能。代码都可以在 GitHub 上找到，我们将在全文中链接到相关笔记本。强烈建议您在阅读本书时使用 GitHub 存储库并运行提供的示例。

For non-notebook examples, you can run the script with the format `python content/chapter_x/script.py` in your terminal, where `x` is the chapter number and `script.py` is the name of the script. In some instances, API keys need to be set as environment variables, and we will make that clear. The packages used update frequently, so install our [_requirements.txt_](https://oreil.ly/BPreq) in a virtual environment before running code examples.  
对于非笔记本示例，您可以在终端中运行格式为 `python content/chapter_x/script.py` 的脚本，其中 `x` 是章节编号， `script.py` 是章节名称脚本。在某些情况下，API 密钥需要设置为环境变量，我们将明确这一点。使用的软件包经常更新，因此在运行代码示例之前在虚拟环境中安装我们的requirements.txt。

The _requirements.txt_ file is generated for Python 3.9. If you want to use a different version of Python, you can generate a new _requirements.txt_ from this [_requirements.in_](https://oreil.ly/YRwP7) file found within the GitHub repository, by running these commands:  
requests.txt 文件是为 Python 3.9 生成的。如果您想使用不同版本的 Python，可以通过运行以下命令从 GitHub 存储库中找到的requirements.in 文件生成新的requirements.txt：

```

`pip install pip-tools`
`pip-compile requirements.in`

```

For Mac users: 对于 Mac 用户：

1. Open Terminal: You can find the Terminal application in your Applications folder, under Utilities, or use Spotlight to search for it.  
    打开终端：您可以在“应用程序”文件夹中的“实用程序”下找到终端应用程序，或使用 Spotlight 进行搜索。
    
2. Navigate to your project folder: Use the `cd` command to change the directory to your project folder. For example: `cd path/to/your/project`.  
    导航到您的项目文件夹：使用 `cd` 命令将目录更改为您的项目文件夹。例如： `cd path/to/your/project` 。
    
3. Create the virtual environment: Use the following command to create a virtual environment named `venv` (you can name it anything): `python3 -m venv venv`.  
    创建虚拟环境：使用以下命令创建名为 `venv` 的虚拟环境（您可以将其命名为任何名称）： `python3 -m venv venv` 。
    
4. Activate the virtual environment: Before you install packages, you need to activate the virtual environment. Do this with the command `source venv/bin/activate`.  
    激活虚拟环境：在安装软件包之前，您需要激活虚拟环境。使用命令 `source venv/bin/activate` 执行此操作。
    
5. Install packages: Now that your virtual environment is active, you can install packages using `pip`. To install packages from the _requirements.txt_ file, use `pip install -r requirements.txt`.  
    安装软件包：现在您的虚拟环境已激活，您可以使用 `pip` 安装软件包。要从requirements.txt 文件安装软件包，请使用 `pip install -r requirements.txt` 。
    
6. Deactivate virtual environment: When you’re done, you can deactivate the virtual environment by typing **`deactivate`**.  
    停用虚拟环境：完成后，您可以通过键入 `deactivate` 来停用虚拟环境。
    

For Windows users: 对于 Windows 用户：

1. Open Command Prompt: You can search for `cmd` in the Start menu.  
    打开命令提示符：您可以在“开始”菜单中搜索 `cmd` 。
    
2. Navigate to your project folder: Use the `cd` command to change the directory to your project folder. For example: `cd path\to\your\project`.  
    导航到您的项目文件夹：使用 `cd` 命令将目录更改为您的项目文件夹。例如： `cd path\to\your\project` 。
    
3. Create the virtual environment: Use the following command to create a virtual environment named `venv`: `python -m venv venv`.  
    创建虚拟环境：使用以下命令创建名为 `venv` 的虚拟环境： `python -m venv venv` 。
    
4. Activate the virtual environment: To activate the virtual environment on Windows, use `.\venv\Scripts\activate`.  
    激活虚拟环境：要在 Windows 上激活虚拟环境，请使用 `.\venv\Scripts\activate` 。
    
5. Install packages: With the virtual environment active, install the required packages: `pip install -r requirements.txt`.  
    安装软件包：在虚拟环境处于活动状态的情况下，安装所需的软件包： `pip install -r requirements.txt` 。
    
6. Deactivate the virtual environment: To exit the virtual environment, simply type: `deactivate`.  
    停用虚拟环境：要退出虚拟环境，只需键入： `deactivate` 。
    

Here are some additional tips on setup:  
以下是有关设置的一些附加提示：

- Always ensure your Python is up-to-date to avoid compatibility issues.  
    始终确保您的 Python 是最新的以避免兼容性问题。
    
- Remember to activate your virtual environment whenever you work on the project.  
    每当您处理项目时，请记住激活您的虚拟环境。
    
- The _requirements.txt_ file should be in the same directory where you create your virtual environment, or you should specify the path to it when using `pip install -r`.  
    requirements.txt 文件应该位于您创建虚拟环境的同一目录中，或者您应该在使用 `pip install -r` 时指定它的路径。
    

Access to an OpenAI developer account is assumed, as your `OPENAI_API_KEY` must be set as an environment variable in any examples importing the OpenAI library, for which we use version 1.0. Quick-start instructions for setting up your development environment can be found in [OpenAI’s documentation](https://oreil.ly/YqbrY) on their website.  
假设可以访问 OpenAI 开发者帐户，因为在导入 OpenAI 库的任何示例中，您的 `OPENAI_API_KEY` 必须设置为环境变量，我们使用版本 1.0。有关设置开发环境的快速入门说明，请参阅 OpenAI 网站上的文档。

You must also ensure that _billing is enabled_ on your OpenAI account and that a valid payment method is attached to run some of the code within the book. The examples in the book use GPT-4 where not stated, though we do briefly cover Anthropic’s competing [Claude 3 model](https://oreil.ly/jY8Ai), as well as Meta’s open source [Llama 3](https://oreil.ly/BbXZ3) and [Google Gemini](https://oreil.ly/KYgij).  
您还必须确保您的 OpenAI 帐户启用了计费功能，并且附加了有效的付款方式来运行书中的某些代码。书中的示例使用 GPT-4（未说明），但我们确实简要介绍了 Anthropic 的竞争 Claude 3 模型，以及 Meta 的开源 Llama 3 和 Google Gemini。

For image generation we use [Midjourney](https://www.midjourney.com/), for which you need a Discord account to sign up, though these principles apply equally to DALL-E 3 (available with a ChatGPT Plus subscription or via the API) or Stable Diffusion (available as an [API](https://oreil.ly/cmTtW) or it can [run locally](https://oreil.ly/Ha0T5) on your computer if it has a GPU). The image generation examples in this book use Midjourney v6, Stable Diffusion v1.5 (as many extensions are still only compatible with this version), or [Stable Diffusion XL](https://oreil.ly/S0P4s), and we specify the differences when this is important.  
对于图像生成，我们使用 Midjourney，您需要注册一个 Discord 帐户，尽管这些原则同样适用于 DALL-E 3（通过 ChatGPT Plus 订阅或通过 API 提供）或 Stable Diffusion（作为 API 提供或它）如果您的计算机有 GPU，则可以在本地运行）。本书中的图像生成示例使用 Midjourney v6、Stable Diffusion v1.5（因为许多扩展仍然只与此版本兼容）或 Stable Diffusion XL，并且当这很重要时我们会指定差异。

We provide examples using open source libraries wherever possible, though we do include commercial vendors where appropriate—for example, [Chapter 5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch05.html#vector_databases_05) on vector databases demonstrates both FAISS (an open source library) and Pinecone (a paid vendor). The examples demonstrated in the book should be easily modifiable for alternative models and vendors, and the skills taught are transferable. [Chapter 4](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch04.html#advanced_text_04) on advanced text generation is focused on the LLM framework LangChain, and [Chapter 9](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch09.html#advanced_image_09) on advanced image generation is built on AUTOMATIC1111’s open source Stable Diffusion Web UI.  
我们尽可能提供使用开源库的示例，尽管我们确实在适当的情况下包含了商业供应商，例如，关于矢量数据库的第 5 章演示了 FAISS（开源库）和 Pinecone（付费供应商）。书中演示的示例应该可以轻松修改以适应替代模型和供应商，并且所教授的技能是可以转移的。第 4 章关于高级文本生成的重点是 LLM 框架 LangChain，第 9 章关于高级图像生成的内容基于 AUTOMATIC1111 的开源 Stable Diffusion Web UI。

# Conventions Used in This Book  
本书中使用的约定

The following typographical conventions are used in this book:  
本书使用以下印刷约定：

_Italic 斜体_

Indicates new terms, URLs, email addresses, filenames, and file extensions.  
表示新术语、URL、电子邮件地址、文件名和文件扩展名。

`Constant width`

Used for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.  
用于程序列表，以及在段落中引用程序元素，例如变量或函数名称、数据库、数据类型、环境变量、语句和关键字。

**`Constant width bold`**

Shows commands or other text that should be typed literally by the user.  
显示应由用户逐字键入的命令或其他文本。

_`Constant width italic`_

Shows text that should be replaced with user-supplied values or by values determined by context.  
显示应替换为用户提供的值或上下文确定的值的文本。

###### TIP

This element signifies a tip or suggestion.  
该元素表示提示或建议。

###### NOTE 笔记

This element signifies a general note.  
该元素表示一般注释。

###### WARNING 警告

This element indicates a warning or caution.  
该元素表示警告或警告。

Throughout the book we reinforce what we call the Five Principles of Prompting, identifying which principle is most applicable to the example at hand. You may want to refer to [Chapter 1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#five_principles_01), which describes the principles in detail.  
在整本书中，我们强化了所谓的“提示五项原则”，确定哪项原则最适用于当前的示例。您可能需要参考第 1 章，其中详细描述了这些原则。

# PRINCIPLE NAME 原理名称

This will explain how the principle is applied to the current example or section of text.  
这将解释如何将该原理应用于当前的示例或文本部分。

# Using Code Examples 使用代码示例

Supplemental material (code examples, exercises, etc.) is available for download at [_https://oreil.ly/prompt-engineering-for-generative-ai_](https://oreil.ly/prompt-engineering-for-generative-ai).  
补充材料（代码示例、练习等）可在 https://oreil.ly/prompt-engineering-for-generative-ai 下载。

If you have a technical question or a problem using the code examples, please send email to [_bookquestions@oreilly.com_](mailto:bookquestions@oreilly.com).  
如果您有技术问题或使用代码示例时遇到问题，请发送电子邮件至 bookquestions@oreilly.com。

This book is here to help you get your job done. In general, if example code is offered with this book, you may use it in your programs and documentation. You do not need to contact us for permission unless you’re reproducing a significant portion of the code. For example, writing a program that uses several chunks of code from this book does not require permission. Selling or distributing examples from O’Reilly books does require permission. Answering a question by citing this book and quoting example code does not require permission. Incorporating a significant amount of example code from this book into your product’s documentation does require permission.  
本书旨在帮助您完成工作。一般来说，如果本书提供了示例代码，您就可以在您的程序和文档中使用它。除非您要复制大部分代码，否则您无需联系我们以获得许可。例如，使用本书中的几段代码编写一个程序不需要许可。销售或分发 O’Reilly 书籍中的示例确实需要许可。通过引用本书和示例代码来回答问题不需要许可。将本书中的大量示例代码合并到您的产品文档中确实需要许可。

We appreciate, but generally do not require, attribution. An attribution usually includes the title, author, publisher, and ISBN. For example: “_Prompt Engineering for Generative AI_ by James Phoenix and Mike Taylor (O’Reilly). Copyright 2024 Saxifrage, LLC and Just Understanding Data LTD, 978-1-098-15343-4.”  
我们赞赏但通常不要求归属。归属通常包括标题、作者、出版商和 ISBN。例如：“James Phoenix 和 Mike Taylor (O’Reilly) 的《生成式 AI 快速工程》。版权所有 2024 Saxifrage, LLC 和 Just Understanding Data LTD，978-1-098-15343-4。”

If you feel your use of code examples falls outside fair use or the permission given above, feel free to contact us at [_permissions@oreilly.com_](mailto:permissions@oreilly.com).  
如果您认为您对代码示例的使用不符合合理使用或上述许可的范围，请随时通过permissions@oreilly.com 与我们联系。

# O’Reilly Online Learning  
奥莱利在线学习

###### NOTE 笔记

For more than 40 years, [_O’Reilly Media_](https://oreilly.com/) has provided technology and business training, knowledge, and insight to help companies succeed.  
40 多年来，O’Reilly Media 一直提供技术和业务培训、知识和见解来帮助公司取得成功。

Our unique network of experts and innovators share their knowledge and expertise through books, articles, and our online learning platform. O’Reilly’s online learning platform gives you on-demand access to live training courses, in-depth learning paths, interactive coding environments, and a vast collection of text and video from O’Reilly and 200+ other publishers. For more information, visit [_https://oreilly.com_](https://oreilly.com/).  
我们独特的专家和创新者网络通过书籍、文章和我们的在线学习平台分享他们的知识和专业知识。 O’Reilly 的在线学习平台让您可以按需访问实时培训课程、深入学习路径、交互式编码环境以及来自 O’Reilly 和 200 多家其他出版商的大量文本和视频。欲了解更多信息，请访问 https://oreilly.com。

# How to Contact Us  
如何联系我们

Please address comments and questions concerning this book to the publisher:  
请向出版商提出有关本书的意见和问题：

- O’Reilly Media, Inc. 奥莱利媒体公司
- 1005 Gravenstein Highway North  
    格雷文斯坦公路北1005号
- Sebastopol, CA 95472 塞瓦斯托波尔, CA 95472
- 800-889-8969 (in the United States or Canada)  
    800-889-8969（美国或加拿大）
- 707-827-7019 (international or local)  
    707-827-7019（国际或本地）
- 707-829-0104 (fax) 707-829-0104（传真）
- [_support@oreilly.com_](mailto:support@oreilly.com)
https://www.oreilly.com/about/contact.html
We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at https://oreil.ly/prompt-engineering-generativeAI.
我们有本书的网页，其中列出了勘误表、示例和任何其他信息。您可以通过 https://oreil.ly/prompt-engineering-generativeAI 访问此页面。

For news and information about our books and courses, visit https://oreilly.com.
有关我们的书籍和课程的新闻和信息，请访问 https://oreilly.com。

Find us on LinkedIn: https://linkedin.com/company/oreilly-media.
在 LinkedIn 上找到我们：https://linkedin.com/company/oreilly-media。

Watch us on YouTube: https://youtube.com/oreillymedia.
在 YouTube 上观看我们的视频：https://youtube.com/oreillymedia。

Acknowledgments 致谢
We’d like to thank the following people for their contribution in conducting a technical review of the book and their patience in correcting a fast-moving target:
我们要感谢以下人员对本书进行技术审查所做的贡献以及他们在纠正快速变化的目标方面的耐心：

Mayo Oshin, early LangChain contributor and founder at SeinnAI Analytics
Mayo Oshin，LangChain 早期贡献者和 SeinnAI Analytics 创始人

Ellis Crosby, founder at Scarlett Panda and AI agency Incremen.to
埃利斯·克罗斯比 (Ellis Crosby)，Scarlett Panda 和人工智能机构 Incremen.to 的创始人

Dave Pawson, O’Reilly author of XSL-FO
Dave Pawson，O’Reilly XSL-FO 的作者

Mark Phoenix, a senior software engineer
马克·菲尼克斯 (Mark Phoenix)，高级软件工程师

Aditya Goel, GenAI consultant
Aditya Goel，GenAI 顾问

We are also grateful to our families for their patience and understanding and would like to reassure them that we still prefer talking to them over ChatGPT.
我们还感谢家人的耐心和理解，并向他们保证我们仍然更喜欢与他们交谈而不是 ChatGPT。

# [1. The Five Principles Of Prompting](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html)
    # Chapter 1. The Five Principles of Prompting  
第一章 提示的五项原则

_Prompt engineering_ is the process of discovering prompts that reliably yield useful or desired results.  
提示工程是发现能够可靠地产生有用或期望结果的提示的过程。

A _prompt_ is the input you provide, typically text, when interfacing with an AI model like ChatGPT or Midjourney. The prompt serves as a set of instructions the model uses to predict the desired response: text from _large language models_ (LLMs) like [ChatGPT](https://chat.openai.com/), or images from _diffusion models_ like [Midjourney](https://www.midjourney.com/).  
提示是您在与 ChatGPT 或 Midjourney 等 AI 模型交互时提供的输入，通常是文本。提示充当模型用于预测所需响应的一组指令：来自 ChatGPT 等大型语言模型 (LLMs) 的文本，或来自 Midjourney 等扩散模型的图像。

Here is a simple example of a prompt input for a product name generator (inspired by one of [OpenAI’s examples](https://oreil.ly/Fc8cq)), and the resulting output from ChatGPT.  
下面是一个简单的产品名称生成器提示输入示例（受到 OpenAI 示例之一的启发），以及 ChatGPT 的结果输出。

Input: 输入：

```

Can I have a list of product names for a pair of shoes that
can fit any foot size?

```

Output: 输出：

```

Certainly! Here's a list of product names for a pair of shoes
that can fit any foot size:

```

UniFit SoleStrides
FlexiSize All-Fit Shoes
OmniFit FootFlex
...
AnyStep AdaptiWalkers
FlexiRange UniversalSteps
PerfectGlide MultiFit Shoes

This is already a remarkable response for a naive prompt, which feels like magic because we got here with very little effort. As the state-of-the-art models improve, the likelihood you will get _good enough_ results on your first try goes up. For any throwaway interactions with an AI, where you don’t plan to do the same task again, the naive approach is all you need.  
对于一个天真的提示来说，这已经是一个了不起的反应，这感觉就像魔术一样，因为我们几乎不费吹灰之力就到达了这里。随着最先进模型的改进，您在第一次尝试中获得足够好的结果的可能性就会增加。对于任何与人工智能的一次性交互，你不打算再次执行相同的任务，简单的方法就是你所需要的。

However, if you planned to put this prompt into production, you’d benefit from investing more work into getting it right. Mistakes cost you money in terms of the fees OpenAI charges based on the length of the prompt and response, as well as the time spent fixing mistakes. If you were building a product name generator with thousands of users, there are some obvious issues you’d want attempt to fix:  
但是，如果您计划将此提示投入生产，那么投入更多的工作来使其正确，您将会受益匪浅。错误会导致您损失金钱，OpenAI 根据提示和响应的长度以及修复错误所花费的时间收取费用。如果您正在构建一个拥有数千名用户的产品名称生成器，那么您需要尝试修复一些明显的问题：

Vague direction 方向模糊

You’re not briefing the AI on what style of name you want, or what attributes it should have. Do you want a single word or a concatenation? Can the words be made up, or is it important that they’re in real English? Do you want the AI to emulate somebody you admire who is famous for great product names?  
你不会向人工智能介绍你想要什么风格的名字，或者它应该具有什么属性。您想要单个单词还是串联单词？这些单词可以是虚构的吗？或者它们是真正的英语很重要吗？您是否希望人工智能模仿您所钦佩的以伟大产品名称而闻名的人？

Unformatted output 无格式输出

You’re getting back a list of separated names line by line, of unspecified length. When you run this prompt multiple times, you’ll see sometimes it comes back with a numbered list, and often it has text at the beginning, which makes it hard to parse programmatically.  
您将逐行返回一个未指定长度的分隔名称列表。当您多次运行此提示时，您会看到有时它会返回一个编号列表，并且通常在开头有文本，这使得以编程方式解析变得困难。

Missing examples 缺少示例

You haven’t given the AI any examples of what _good_ names look like. It’s autocompleting using an average of its training data, i.e., the entire internet (with all its inherent bias), but is that what you want? Ideally you’d feed it examples of successful names, common names in an industry, or even just other names you like.  
你还没有给人工智能任何好名字的例子。它使用其训练数据的平均值（即整个互联网（及其所有固有的偏见））自动完成，但这就是您想要的吗？理想情况下，您可以向其提供成功名称、行业中常见名称的示例，甚至只是您喜欢的其他名称。

Limited evaluation 有限评价

You have no consistent or scalable way to define which names are good or bad, so you have to manually review each response. If you can institute a rating system or other form of measurement, you can optimize the prompt to get better results and identify how many times it fails.  
您没有一致或可扩展的方法来定义哪些名称好或坏，因此您必须手动检查每个响应。如果您可以建立评级系统或其他形式的测量，您可以优化提示以获得更好的结果并确定失败的次数。

No task division 没有任务划分

You’re asking a lot of a single prompt here: there are lots of factors that go into product naming, and this important task is being naively outsourced to the AI all in one go, with no task specialization or visibility into how it’s handling this task for you.  
你在这里问了很多单一提示：产品命名涉及很多因素，而这项重要任务被天真地一次性外包给人工智能，没有任务专门化或了解它如何处理这个问题给你的任务。

Addressing these problems is the basis for the core principles we use throughout this book. There are many different ways to ask an AI model to do the same task, and even slight changes can make a big difference. LLMs work by continuously predicting the next token (approximately three-fourths of a word), starting from what was in your prompt. Each new token is selected based on its probability of appearing next, with an element of randomness (controlled by the _temperature_ parameter). As demonstrated in [Figure 1-1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-1), the word _shoes_ had a lower probability of coming after the start of the name _AnyFit_ (0.88%), where a more predictable response would be _Athletic_ (72.35%).  
解决这些问题是我们在本书中使用的核心原则的基础。要求人工智能模型完成相同任务的方法有很多种，即使是微小的改变也会产生很大的差异。 LLMs 从提示中的内容开始，不断预测下一个标记（大约四分之三的单词）。每个新令牌都是根据其接下来出现的概率进行选择的，并具有随机性（由温度参数控制）。如图 1-1 所示，“鞋”一词出现在 AnyFit 名称开头之后的概率较低 (0.88%)，而更可预测的响应是“运动”(72.35%)。

![pega 0101](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0101.png)

###### Figure 1-1. How the response breaks down into tokens  
图 1-1。响应如何分解为令牌

LLMs are trained on essentially the entire text of the internet, and are then further fine-tuned to give helpful responses. Average prompts will return average responses, leading some to be underwhelmed when their results don’t live up to the hype. What you put in your prompt changes the probability of every word generated, so it matters a great deal to the results you’ll get. These models have seen the best and worst of what humans have produced and are capable of emulating almost anything if you know the right way to ask. OpenAI charges based on the [number of tokens used](https://openai.com/pricing) in the prompt and the response, so prompt engineers need to make these tokens count by optimizing prompts for cost, quality, and reliability.  
LLMs 基本上接受了互联网整个文本的训练，然后进一步微调以提供有用的响应。一般的提示将返回一般的响应，导致一些人在结果不符合宣传时感到不知所措。你在提示中输入的内容会改变生成每个单词的概率，因此它对你得到的结果非常重要。这些模型已经看到了人类创造的最好和最差的东西，并且如果你知道正确的提问方式，它们几乎能够模拟任何东西。 OpenAI 根据提示和响应中使用的令牌数量进行收费，因此提示工程师需要通过优化提示的成本、质量和可靠性来使这些令牌计数。

Here’s the same example with the application of several prompt engineering techniques. We ask for names in the style of Steve Jobs, state that we want a comma-separated list, and supply examples of the task done well.  
这是应用了几种快速工程技术的同一示例。我们以史蒂夫·乔布斯的风格询问姓名，声明我们想要一个以逗号分隔的列表，并提供出色完成任务的示例。

Input: 输入：

Brainstorm a list of product names for a shoe that fits any
foot size, in the style of Steve Jobs.

Return the results as a comma-separated list, in this format:
Product description: A shoe that fits any foot size
Product names: [list of 3 product names]

## Examples
Product description: A refrigerator that dispenses beer
Product names: iBarFridge, iFridgeBeer, iDrinkBeerFridge

Product description: A watch that can tell accurate time in
space
Product names: iNaut, iSpace, iTime

Product description: A home milkshake maker
Product names: iShake, iSmoothie, iShake Mini

Output: 输出：

Product description: A shoe that fits any foot size
Product names: iFitFoot, iPerfectFit, iShoeSize

While no prompt is ever perfect, this prompt is optimized to reliably deliver solid product names in the right format. The user of your product name generator can choose somebody other than Steve Jobs to get the types of names they like, they can change the response format if needed, and the output of this prompt can become the input of another. Finally, you could periodically update the examples you use in the prompt based on user feedback, making your system smarter over time.  
虽然没有任何提示是完美的，但此提示经过优化，可以以正确的格式可靠地提供可靠的产品名称。产品名称生成器的用户可以选择史蒂夫·乔布斯以外的其他人来获取他们喜欢的名称类型，如果需要，他们可以更改响应格式，并且此提示的输出可以成为另一个提示的输入。最后，您可以根据用户反馈定期更新提示中使用的示例，从而使您的系统随着时间的推移变得更加智能。

# Overview of the Five Principles of Prompting  
提示五项原则概述

The process for optimizing this prompt follows the _Five Principles of Prompting_, which we will dissect using this example in the remainder of this chapter, and recall throughout the book. They map exactly to the five issues we raised when discussing the naive text prompt. You’ll find references back to these principles throughout the rest of the book to help you connect the dots to how they’re used in practice. The Five Principles of Prompting are as follows:  
优化这个提示的过程遵循提示的五项原则，我们将在本章的其余部分使用这个例子进行剖析，并在整本书中回顾。它们准确地反映了我们在讨论幼稚文本提示时提出的五个问题。在本书的其余部分中，您将找到对这些原则的引用，以帮助您将这些点与它们在实践中的使用方式联系起来。提示的五项原则如下：

Give Direction 给予指导

Describe the desired style in detail, or reference a relevant persona  
详细描述所需的风格，或参考相关人物

Specify Format 指定格式

Define what rules to follow, and the required structure of the response  
定义要遵循的规则以及所需的响应结构

Provide Examples 提供例子

Insert a diverse set of test cases where the task was done correctly  
插入正确完成任务的一组不同的测试用例

Evaluate Quality 评估质量

Identify errors and rate responses, testing what drives performance.  
识别错误并评估响应速度，测试驱动性能的因素。

Divide Labor 分工

Split tasks into multiple steps, chained together for complex goals  
将任务分成多个步骤，链接在一起以实现复杂的目标

These principles are not short-lived _tips_ or _hacks_ but are generally accepted conventions that are useful for working with any level of intelligence, biological or artificial. These principles are model-agnostic and should work to improve your prompt no matter which generative text or image model you’re using. We first published these principles in July 2022 in the blog post [“Prompt Engineering: From Words to Art and Copy”](https://oreil.ly/RYYiV), and they have stood the test of time, including mapping quite closely to OpenAI’s own [Prompt Engineering Guide](https://oreil.ly/dF8q-), which came a year later. Anyone who works closely with generative AI models is likely to converge on a similar set of strategies for solving common issues, and throughout this book you’ll see hundreds of demonstrative examples of how they can be useful for improving your prompts.  
这些原则不是短暂的技巧或窍门，而是普遍接受的约定，对于任何级别的智能（无论是生物智能还是人工智能）都非常有用。这些原则与模型无关，无论您使用哪种生成文本或图像模型，都应该能够改善您的提示。我们于 2022 年 7 月在博客文章“即时工程：从文字到艺术和复制”中首次发布了这些原则，它们经受住了时间的考验，包括与一年后发布的 OpenAI 自己的即时工程指南非常接近。任何与生成式人工智能模型密切合作的人都可能会采用一套类似的策略来解决常见问题，在本书中，您将看到数百个说明性示例，说明它们如何有助于改进您的提示。

We have provided downloadable one-pagers for text and image generation you can use as a checklist when applying these principles. These were created for our popular Udemy course [The Complete Prompt Engineering for AI Bootcamp](https://oreil.ly/V40zg) (70,000+ students), which was based on the same principles but with different material to this book.  
我们提供了可下载的用于文本和图像生成的单页程序，您可以在应用这些原则时将其用作清单。这些是为我们流行的 Udemy 课程“AI 训练营的完整提示工程”（超过 70,000 名学生）创建的，该课程基于相同的原理，但与本书的材料不同。

- [Text Generation One-Pager  
    文本生成单页机](https://oreil.ly/VCcgy)
    
- [Image Generation One-Pager  
    图像生成单页机](https://oreil.ly/q7wQF)
    

To show these principles apply equally well to prompting image models, let’s use the following example, and explain how to apply each of the Five Principles of Prompting to this specific scenario. Copy and paste the entire input prompt into the Midjourney Bot in Discord, including the link to the image at the beginning, after typing `**/imagine**` to trigger the prompt box to appear (requires a free [Discord](https://discord.com/) account, and a paid [Midjourney](https://www.midjourney.com/) account).  
为了表明这些原则同样适用于提示图像模型，让我们使用以下示例，并解释如何将提示的五项原则应用于此特定场景。将整个输入提示复制并粘贴到 Discord 中的 Midjourney Bot 中，包括开头的图像链接，输入 `**/imagine**` 后触发提示框出现（需要免费的 Discord 帐户和付费帐户）中途帐户）。

Input: 输入：

https://s.mj.run/TKAsyhNiKmc stock photo of business meeting
of 4 people watching on white MacBook on top of glass-top
table, Panasonic, DC-GH5

[Figure 1-2](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-2) shows the output.  
图 1-2 显示了输出。

![pega 0102](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0102.png)

###### Figure 1-2. Stock photo of business meeting  
图 1-2。商务会议的股票照片

This prompt takes advantage of Midjourney’s ability to take a base image as an example by uploading the image to Discord and then copy and pasting the URL into the prompt (_[_https://s.mj.run/TKAsyhNiKmc_](https://s.mj.run/TKAsyhNiKmc)_), for which the royalty-free image from Unsplash is used ([Figure 1-3](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-3)). If you run into an error with the prompt, try uploading the image yourself and reviewing [Midjourney’s documentation](https://oreil.ly/UTxpX) for any formatting changes.  
此提示利用 Midjourney 的功能，以基本图像为例，将图像上传到 Discord，然后将 URL 复制并粘贴到提示中 (https://s.mj.run/TKAsyhNiKmc)，为此，版税 -使用 Unsplash 的免费图像（图 1-3）。如果您遇到提示错误，请尝试自行上传图像并查看 Midjourney 的文档以了解任何格式更改。

![pega 0103](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0103.png)

###### Figure 1-3. Photo by Mimi Thian on [Unsplash](https://oreil.ly/J4Hkr)  
图 1-3。照片由 Unsplash 上的 Mimi Thian 拍摄

Let’s compare this well-engineered prompt to what you get back from Midjourney if you naively ask for a stock photo in the simplest way possible. [Figure 1-4](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-4) shows an example of what you get without prompt engineering, an image with a darker, more stylistic take on a stock photo than you’d typically expect.  
让我们将这个精心设计的提示与您从中途天真地以最简单的方式索要库存照片时得到的提示进行比较。图 1-4 展示了您无需立即进行工程处理即可获得的示例，即与库存照片相比，图像的颜色比您通常预期的更暗、更具风格。

Input: 输入：

people in a business meeting

[Figure 1-4](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-4) shows the output.  
图 1-4 显示了输出。

Although less prominent an issue in v5 of Midjourney onwards, community feedback mechanisms (when users select an image to resize to a higher resolution, that choice may be used to train the model) have reportedly biased the model toward a _fantasy_ aesthetic, which is less suitable for the stock photo use case. The early adopters of Midjourney came from the digital art world and naturally gravitated toward fantasy and sci-fi styles, which can be reflected in the results from the model even when this aesthetic is not suitable.  
尽管在 Midjourney 的 v5 版本中这个问题不太突出，但据报道，社区反馈机制（当用户选择将图像大小调整为更高分辨率时，该选择可能会用于训练模型）使模型偏向于幻想美学，这是较少的适合库存照片用例。 Midjourney 的早期采用者来自数字艺术世界，自然偏向奇幻和科幻风格，即使这种审美并不适合，这也可以反映在模型的结果中。

![pega 0104](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0104.png)

###### Figure 1-4. People in a business meeting  
图 1-4。商务会议中的人们

Throughout this book the examples used will be compatiable with ChatGPT Plus (GPT-4) as the text model and Midjourney v6 or Stable Diffusion XL as the image model, though we will specify if it’s important. These foundational models are the current state of the art and are good at a diverse range of tasks. The principles are intended to be future-proof as much as is possible, so if you’re reading this book when GPT-5, Midjourney v7, or Stable Diffusion XXL is out, or if you’re using another vendor like Google, everything you learn here should still prove useful.  
本书中使用的示例将与作为文本模型的 ChatGPT Plus (GPT-4) 和作为图像模型的 Midjourney v6 或 Stable Diffusion XL 兼容，尽管我们将指定它是否重要。这些基础模型是当前最先进的模型，擅长执行各种任务。这些原则旨在尽可能面向未来，因此，如果您在 GPT-5、Midjourney v7 或 Stable Diffusion XXL 发布时阅读本书，或者如果您正在使用 Google 等其他供应商，那么一切你在这里学到的应该还是有用的。

# Give Direction 1. 给予指导

One of the issues with the naive text prompt discussed earlier was that it wasn’t briefing the AI on what _types_ of product names you wanted. To some extent, naming a product is a subjective endeavor, and without giving the AI an idea of what names you like, it has a low probability of guessing right.  
前面讨论的天真的文本提示的问题之一是它没有向人工智能简要介绍您想要什么类型的产品名称。在某种程度上，为产品命名是一种主观努力，如果不让人工智能知道你喜欢什么名字，它猜对的可能性很低。

By the way, a human would also struggle to complete this task without a good _brief_, which is why creative and branding agencies require a detailed briefing on any task from their clients.  
顺便说一句，如果没有良好的简报，人类也很难完成这项任务，这就是为什么创意和品牌机构需要客户提供有关任何任务的详细简报的原因。

###### TIP

Although it’s not a perfect mapping, it can be helpful to imagine what context a human might need for this task and try including it in the prompt.  
尽管这不是一个完美的映射，但想象一下人类可能需要什么上下文来完成此任务并尝试将其包含在提示中可能会有所帮助。

In the example prompt we gave direction through the use of _role-playing_, in that case emulating the style of Steve Jobs, who was famous for iconically naming products. If you change this aspect of the prompt to someone else who is famous in the training data (as well as matching the examples to the right style), you’ll get dramatically different results.  
在示例提示中，我们通过使用角色扮演来给出指导，在这种情况下模仿史蒂夫·乔布斯的风格，他以标志性的产品命名而闻名。如果您将提示的这方面更改为训练数据中著名的其他人（以及将示例与正确的风格相匹配），您将得到截然不同的结果。

Input: 输入：

Brainstorm a list of product names for a shoe that fits any
foot size, in the style of Elon Musk.

Return the results as a comma-separated list, in this format:
Product description: A shoe that fits any foot size
Product names: [list of 3 product names]

## Examples
Product description: A refrigerator that dispenses beer
Product names: Teslacool, FridgeX, Neuradrink

Product description: A watch that can tell accurate time in
space
Product names: WatchX, iSpace, The Watch Company

Product description: A home milkshake maker
Product names: ShakeX, The Milkshake Company, HyperShake

Output: 输出：

ShoeX, MarsFit, The Shoe Company

There are also some rules or best practices you would do well to follow, which could be included in the prompt as context to guide the AI toward a name that works. This technique is sometimes referred to as _prewarming_ or _internal retrieval_, and it is simple but effective ([Liu et al., 2021](https://oreil.ly/1lqzK)). Starting the conversation asking for best practice advice, then asking it to follow its own advice, can help a lot. In effect, you are using it to generate its own direction.  
还有一些您最好遵循的规则或最佳实践，它们可以作为上下文包含在提示中，以指导人工智能找到有效的名称。这种技术有时被称为预热或内部检索，它简单但有效（Liu et al., 2021）。开始对话时寻求最佳实践建议，然后要求其遵循自己的建议，这会很有帮助。实际上，您正在使用它来生成自己的方向。

Input: 输入：

Please give me 5 tips for naming products based on expert
industry advice.

Output: 输出：

Certainly! Naming a product is crucial as it often gives the
first impression to potential customers. Here are five expert
tips to guide you in naming products:

1. **Simplicity & Memorability**: Opt for names that are
short, easy to spell, and memorable. Long, complicated names
can be difficult for customers to recall. Remember, the
easier the name is to remember, the more likely it is that
consumers will think of your product when making a purchase
decision.

...

5. **Positive Connotations**: Names that evoke positive
emotions or imagery can create a favorable perception of
your product. Avoid names that have negative or
controversial associations in any of the primary languages
or cultures where you intend to do business. It's often
worthwhile to conduct linguistic checks and market testing
to ensure there aren't unintended meanings.

Lastly, once you've shortlisted a few names, it's a good
idea to run them by diverse focus groups or conduct surveys
to gauge reactions. Also, ensure that the name you choose is
available for trademarking and doesn't infringe on existing
trademarks.

Then within the same chat window, where the model has the context of the past advice it gave, you ask your initial prompt for the task you wanted to complete.  
然后在同一个聊天窗口中，模型具有它所提供的过去建议的上下文，您可以询问您想要完成的任务的初始提示。

Input: 输入：

Using this advice, can I have a list of product names for a
pair of shoes that can fit any foot size?

Output: 输出：

Certainly! Based on the criteria given:

1. **Simplicity & Memorability**
2. **Relevance & Descriptiveness**
3. **Differentiation & Uniqueness**
4. **Adaptable & Scalable**
5. **Positive Connotations**

Here's a list of potential product names for shoes that can
fit any foot size:

1. **FitAll Walkers**: A simple and memorable name that
instantly suggests a universal fit.

...

10. **TrueFit Universals**: Emphasizing genuine comfort and
fit for all.

Before finalizing any name, remember to check for trademarks
to ensure there's no conflict with existing products or
brands.

Another fruitful strategy in our experience is to take the best advice out there for the task you want to accomplish and insert that context into the prompt. For example, you could take [Brandwatch’s 5 Golden Rules for naming a product](https://oreil.ly/3bWjz) or another trusted external resource you find, and insert that as context into the prompt. This will increase the length of the prompt significantly, which costs more money (when using the API as a developer), but may be worth the trade-off if the quality of the response improves.  
根据我们的经验，另一个富有成效的策略是针对您想要完成的任务获取最佳建议，并将该上下文插入提示中。例如，您可以采用 Brandwatch 的 5 条黄金法则来命名您找到的产品或其他受信任的外部资源，并将其作为上下文插入到提示中。这将显着增加提示的长度，这会花费更多的钱（当作为开发人员使用 API 时），但如果响应的质量提高，可能值得权衡。

Input: 输入：

Can I have a list of product names for a pair of shoes that
can fit any foot size? Please follow the five rules below:

1. It should be readable and writable.
If your product name is hard to pronounce, people won’t talk about it,
and if they can’t write it down (and spell it correctly!)
when they hear it, how do you expect them to Google it?

Keep it simple and don’t go with any wacky spellings just for the sake of it.

...

5. It should evoke an emotion, feeling, or idea.
Your product name should tie back into what your product is, what the
feeling you want people to have when experiencing your product is, and/or
what idea are you trying to get across.

It should be emotive and inspiring.

Output: 输出：

1. FlexFit Footwear
2. OmniSize Sneakers
3. AdaptStride Shoes
...
18. OmniComfort Kicks
19. FlexSize Footwear
20. Boundless Soles

There are other myriad ways of providing direction. In the image generation example, direction was given by specifying that the business meeting is taking place around a glass-top table. If you change only that detail, you can get a completely different image, as detailed in [Figure 1-5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-5).  
还有其他无数种提供指导的方法。在图像生成示例中，通过指定商务会议在玻璃顶桌子周围举行来给出方向。如果仅更改该细节，您可以获得完全不同的图像，如图 1-5 所示。

Input: 输入：

https://s.mj.run/TKAsyhNiKmc stock photo of business meeting
of four people gathered around a campfire outdoors in the
woods, Panasonic, DC-GH5

[Figure 1-5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-5) shows the output.  
图 1-5 显示了输出。

![pega 0105](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0105.png)

###### Figure 1-5. Stock photo of business meeting in the woods  
图 1-5。在树林里举行商务会议的股票照片

Role-playing is also important for image generation, and one of the quite powerful ways you can give Midjourney direction is to supply the name of an artist or art style to emulate. One artist that features heavily in the AI art world is Van Gogh, known for his bold, dramatic brush strokes and vivid use of colors. Watch what happens when you include his name in the prompt, as shown in [Figure 1-6](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-6).  
角色扮演对于图像生成也很重要，为中途提供指导的一种非常有效的方法是提供要模仿的艺术家或艺术风格的名字。梵高是人工智能艺术界中一位举足轻重的艺术家，他以其大胆、戏剧性的笔触和生动的色彩运用而闻名。观察当您在提示中包含他的名字时会发生什么，如图 1-6 所示。

Input: 输入：

people in a business meeting, by Van Gogh

[Figure 1-6](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-6) shows the output.  
图 1-6 显示了输出。

![pega 0106](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0106.png)

###### Figure 1-6. People in a business meeting, by Van Gogh  
图 1-6。参加商务会议的人们，梵高

To get that last prompt to work, you need to strip back a lot of the other direction. For example, losing the base image and the words _stock photo_ as well as the camera _Panasonic, DC-GH5_ helps bring in Van Gogh’s style. The problem you may run into is that often with too much direction, the model can quickly get to a conflicting combination that it can’t resolve. If your prompt is overly specific, there might not be enough samples in the training data to generate an image that’s consistent with all of your criteria. In cases like these, you should choose which element is more important (in this case, Van Gogh) and defer to that.  
为了让最后一个提示起作用，你需要去掉很多其他方向的内容。例如，去掉底图和stock photo字样以及松下相机，DC-GH5有助于引入梵高的风格。您可能遇到的问题是，通常方向太多，模型很快就会出现无法解决的冲突组合。如果您的提示过于具体，训练数据中可能没有足够的样本来生成符合您所有标准的图像。在这种情况下，您应该选择哪个元素更重要（在本例中是梵高）并遵循它。

Direction is one of the most commonly used and broadest principles. It can take the form of simply using the right descriptive words to clarify your intent, or channeling the personas of relevant business celebrities. While too much direction can narrow the creativity of the model, too little direction is the more common problem.  
方向是最常用和最广泛的原则之一。它可以采取简单地使用正确的描述性词语来阐明您的意图的形式，或者引导相关商业名人的角色。虽然太多的方向会缩小模型的创造力，但方向太少是更常见的问题。

# Specify Format 2. 指定格式

AI models are universal translators. Not only does that mean translating from French to English, or Urdu to Klingon, but also between data structures like JSON to YAML, or natural language to Python code. These models are capable of returning a response in almost any format, so an important part of prompt engineering is finding ways to specify what format you want the response to be in.  
人工智能模型是通用翻译器。这不仅意味着从法语到英语、或从乌尔都语到克林贡语的翻译，还意味着在 JSON 到 YAML 等数据结构之间的翻译，或者从自然语言到 Python 代码的翻译。这些模型能够以几乎任何格式返回响应，因此提示工程的一个重要部分是找到方法来指定您希望响应采用的格式。

Every now and again you’ll find that the same prompt will return a different format, for example, a numbered list instead of comma separated. This isn’t a big deal most of the time, because most prompts are one-offs and typed into ChatGPT or Midjourney. However, when you’re incorporating AI tools into production software, occasional flips in format can cause all kinds of errors.  
您时不时会发现相同的提示会返回不同的格式，例如，编号列表而不是逗号分隔。大多数时候这并不是什么大问题，因为大多数提示都是一次性的，并输入 ChatGPT 或 Midjourney 中。然而，当您将人工智能工具整合到生产软件中时，偶尔的格式翻转可能会导致各种错误。

Just like when working with a human, you can avoid wasted effort by specifying up front the format you expect the response to be in. For text generation models, it can often be helpful to output JSON instead of a simple ordered list because that’s the universal format for API responses, which can make it simpler to parse and spot errors, as well as to use to render the front-end HTML of an application. YAML is also another popular choice because it enforces a parseable structure while still being simple and human-readable.  
就像与人合作时一样，您可以通过预先指定您期望响应的格式来避免浪费精力。对于文本生成模型，输出 JSON 而不是简单的有序列表通常会很有帮助，因为这是通用的API 响应的格式，可以更轻松地解析和发现错误，以及用于呈现应用程序的前端 HTML。 YAML 也是另一个流行的选择，因为它强制执行可解析的结构，同时仍然简单且易于阅读。

In the original prompt you gave direction through both the examples provided, and the colon at the end of the prompt indicated it should complete the list inline. To swap the format to JSON, you need to update both and leave the JSON uncompleted, so GPT-4 knows to complete it.  
在原始提示中，您通过提供的两个示例给出了指示，提示末尾的冒号表示它应该内联完成列表。要将格式交换为 JSON，您需要更新两者并保留 JSON 不完整，以便 GPT-4 知道要完成它。

Input: 输入：

Return a comma-separated list of product names in JSON for
"A pair of shoes that can fit any foot size.".
Return only JSON.

Examples:
[{
		"Product description": "A home milkshake maker.",
		"Product names": ["HomeShaker", "Fit Shaker",
		"QuickShake", "Shake Maker"]
	},
	{
		"Product description": "A watch that can tell
		accurate time in space.",
		"Product names": ["AstroTime", "SpaceGuard",
		"Orbit-Accurate", "EliptoTime"]}
]

Output: 输出：

[
	{
		"Product description": "A pair of shoes that can \
		fit any foot size.",
		"Product names": ["FlexFit Footwear", "OneSize Step",
		"Adapt-a-Shoe", "Universal Walker"]
	}
]

The output we get back is the completed JSON containing the product names. This can then be parsed and used programmatically, in an application or local script. It’s also easy from this point to check if there’s an error in the formatting using a JSON parser like Python’s standard _json_ library, because broken JSON will result in a parsing error, which can act as a trigger to retry the prompt or investigate before continuing. If you’re still not getting the right format back, it can help to specify at the beginning or end of the prompt, or in the system message if using a chat model: `You are a helpful assistant that only responds in JSON`, or specify [JSON output](https://oreil.ly/E7wua) in the model parameters where available (this is called _grammars_ with [Llama models](https://oreil.ly/yU27T).  
我们得到的输出是包含产品名称的完整 JSON。然后可以在应用程序或本地脚本中以编程方式解析和使用它。从现在起，使用 JSON 解析器（例如 Python 的标准 json 库）检查格式是否存在错误也很容易，因为损坏的 JSON 会导致解析错误，这可以作为触发器，在继续之前重试提示或进行调查。如果您仍然没有得到正确的格式，它可以帮助您在提示的开头或结尾指定，或者在系统消息中指定（如果使用聊天模型）： `You are a helpful assistant that only responds in JSON` ，或者在中指定 JSON 输出可用的模型参数（这称为 Llama 模型的语法。

###### TIP

To get up to speed on JSON if you’re unfamiliar, W3Schools [has a good introduction](https://oreil.ly/Xakgc).  
如果您不熟悉 JSON，为了快速了解 JSON，W3Schools 有一个很好的介绍。

For image generation models, format is very important, because the opportunities for modifying an image are near endless. They range from obvious formats like `stock photo`, `illustration`, and `oil painting`, to more unusual formats like `dashcam footage`, `ice sculpture`, or `in Minecraft` (see [Figure 1-7](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-7)).  
对于图像生成模型，格式非常重要，因为修改图像的机会几乎是无穷无尽的。它们的范围从明显的格式（如 `stock photo` 、 `illustration` 和 `oil painting` ）到更不寻常的格式（如 `dashcam footage` 、 `ice sculpture` （参见图 1-7）。

Input: 输入：

business meeting of four people watching on MacBook on top of
table, in Minecraft

[Figure 1-7](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-7) shows the output.  
图 1-7 显示了输出。

![pega 0107](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0107.png)

###### Figure 1-7. Business meeting in Minecraft  
图 1-7。 Minecraft 中的商务会议

When setting a format, it is often necessary to remove other aspects of the prompt that might clash with the specified format. For example, if you supply a base image of a stock photo, the result is some combination of stock photo and the format you wanted. To some degree, image generation models can generalize to new scenarios and combinations they haven’t seen before in their training set, but in our experience, the more layers of unrelated elements, the more likely you are to get an unsuitable image.  
设置格式时，通常需要删除可能与指定格式冲突的提示的其他方面。例如，如果您提供库存照片的基本图像，则结果是库存照片和您想要的格式的某种组合。在某种程度上，图像生成模型可以泛化到他们以前在训练集中从未见过的新场景和组合，但根据我们的经验，不相关元素的层数越多，获得不合适图像的可能性就越大。

There is often some overlap between the first and second principles, Give Direction and Specify Format. The latter is about defining what type of output you want, for example JSON format, or the format of a stock photo. The former is about the style of response you want, independent from the format, for example product names in the style of Steve Jobs, or an image of a business meeting in the style of Van Gogh. When there are clashes between style and format, it’s often best to resolve them by dropping whichever element is less important to your final result.  
第一原则和第二原则（给出方向和指定格式）之间经常有一些重叠。后者是关于定义您想要的输出类型，例如 JSON 格式或库存照片的格式。前者是关于您想要的响应风格，与格式无关，例如史蒂夫·乔布斯风格的产品名称，或梵高风格的商务会议图像。当风格和格式之间存在冲突时，通常最好通过删除对最终结果不太重要的元素来解决它们。

# Provide Examples 3. 提供例子

The original prompt didn’t give the AI any examples of what you think _good_ names look like. Therefore, the response is approximate to an average of the internet, and you can do better than that. Researchers would call a prompt with no examples _zero-shot_, and it’s always a pleasant surprise when AI can even do a task zero shot: it’s a sign of a powerful model. If you’re providing zero examples, you’re asking for a lot without giving much in return. Even providing one example (_one-shot_) helps considerably, and it’s the norm among researchers to test how models perform with multiple examples (_few-shot_). One such piece of research is the famous GPT-3 paper [“Language Models are Few-Shot Learners”](https://oreil.ly/KW5PS), the results of which are illustrated in [Figure 1-8](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-8), showing adding one example along with a prompt can improve accuracy in some tasks from 10% to near 50%!  
最初的提示并没有给人工智能任何你认为好名字是什么样子的例子。因此，响应近似于互联网的平均水平，您可以做得更好。研究人员将没有示例的提示称为零样本，当人工智能甚至可以完成零样本任务时，总是令人惊喜：这是一个强大模型的标志。如果你提供的例子为零，那么你就要求很多却没有给予太多回报。即使提供一个示例（一次性）也会有很大帮助，并且研究人员使用多个示例（几次）来测试模型的表现是一种常态。其中一项研究是著名的 GPT-3 论文“Language Models are Few-Shot Learners”，其结果如图 1-8 所示，显示添加一个示例和提示可以将某些任务的准确性从 10 提高到 10。 % 接近 50%！

![pega 0108](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0108.png)

###### Figure 1-8. Number of examples in context  
图 1-8。上下文中的示例数量

When briefing a colleague or training a junior employee on a new task, it’s only natural that you’d include examples of times that task had previously been done well. Working with AI is the same, and the strength of a prompt often comes down to the examples used. Providing examples can sometimes be easier than trying to explain exactly what it is about those examples you like, so this technique is most effective when you are not a domain expert in the subject area of the task you are attempting to complete. The amount of text you can fit in a prompt is limited (at the time of writing around 6,000 characters on Midjourney and approximately 32,000 characters for the free version of ChatGPT), so a lot of the work of prompt engineering involves selecting and inserting diverse and instructive examples.  
当向同事介绍新任务或对初级员工进行新任务培训时，您很自然地会列举之前完成该任务的例子。使用人工智能也是一样，提示的强度通常取决于所使用的示例。提供示例有时比尝试准确解释您喜欢的示例更容易，因此当您不是要完成的任务的主题领域的领域专家时，此技术最有效。提示中可以容纳的文本量是有限的（在 Midjourney 上编写时约为 6,000 个字符，在 ChatGPT 免费版本中约为 32,000 个字符），因此提示工程的大量工作涉及选择和插入各种不同的文本。具有指导意义的例子。

There’s a trade-off between reliability and creativity: go past three to five examples and your results will become more reliable, while sacrificing creativity. The more examples you provide, and the lesser the diversity between them, the more constrained the response will be to match your examples. If you change all of the examples to animal names in the previous prompt, you’ll have a strong effect on the response, which will reliably return only names including animals.  
可靠性和创造力之间需要权衡：经过三到五个例子，你的结果会变得更加可靠，但会牺牲创造力。您提供的示例越多，它们之间的多样性越小，响应与您的示例相匹配的限制就越大。如果您将上一个提示中的所有示例更改为动物名称，将对响应产生很大影响，该响应将可靠地仅返回包括动物的名称。

Input: 输入：

Brainstorm a list of product names for a shoe that fits any
foot size.

Return the results as a comma-separated list, in this format:
Product description: A shoe that fits any foot size
Product names: [list of 3 product names]

## Examples:
Product description: A home milkshake maker.
Product names: Fast Panda, Healthy Bear, Compact Koala

Product description: A watch that can tell accurate time in
space.
Product names: AstroLamb, Space Bear, Eagle Orbit

Product description: A refrigerator that dispenses beer
Product names: BearFridge, Cool Cat, PenguinBox

Output: 输出：

Product description: A shoe that fits any foot size
Product names: FlexiFox, ChameleonStep, PandaPaws

Of course this runs the risk of missing out on returning a much better name that doesn’t fit the limited space left for the AI to play in. Lack of diversity and variation in examples is also a problem in handling edge cases, or uncommon scenarios. Including one to three examples is easy and almost always has a positive effect, but above that number it becomes essential to experiment with the number of examples you include, as well as the similarity between them. There is some evidence ([Hsieh et al., 2023](https://oreil.ly/6Ixcw)) that direction works better than providing examples, and it typically isn’t straightforward to collect good examples, so it’s usually prudent to attempt the principle of Give Direction first.  
当然，这存在着错过返回一个更好的名称的风险，该名称不适合人工智能发挥作用的有限空间。示例中缺乏多样性和变化也是处理边缘情况或不常见场景的问题。包含一到三个示例很容易，并且几乎总是会产生积极的效果，但超过这个数字，就必须尝试包含的示例数量以及它们之间的相似性。有一些证据（Hsieh 等人，2023）表明指导比提供示例更有效，而且收集好的示例通常并不容易，因此首先尝试“给予指导”原则通常是谨慎的。

In the image generation space, providing examples usually comes in the form of providing a base image in the prompt, called _img2img_ in the open source [Stable Diffusion](https://oreil.ly/huVRu) community. Depending on the image generation model being used, these images can be used as a starting point for the model to generate from, which greatly affects the results. You can keep everything about the prompt the same but swap out the provided base image for a radically different effect, as in [Figure 1-9](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-9).  
在图像生成领域，提供示例通常以在提示中提供基础图像的形式出现，在开源 Stable Diffusion 社区中称为 img2img。根据所使用的图像生成模型，这些图像可以用作模型生成的起点，这极大地影响结果。您可以保持提示的所有内容相同，但将提供的基本图像替换为完全不同的效果，如图 1-9 所示。

Input: 输入：

stock photo of business meeting of 4 people watching on
white MacBook on top of glass-top table, Panasonic, DC-GH5

[Figure 1-9](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-9) shows the output.  
图 1-9 显示了输出。

![pega 0109](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0109.png)

###### Figure 1-9. Stock photo of business meeting of four people  
图 1-9。四人商务会议图库照片

In this case, by substituting for the image shown in [Figure 1-10](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-10), also from Unsplash, you can see how the model was pulled in a different direction and incorporates whiteboards and sticky notes now.  
在本例中，通过替换同样来自 Unsplash 的图 1-10 中所示的图像，您可以看到模型如何被拉向不同的方向，并且现在如何合并白板和便签。

###### CAUTION 警告

These examples demonstrate the capabilities of image generation models, but we would exercise caution when uploading base images for use in prompts. Check the licensing of the image you plan to upload and use in your prompt as the base image, and avoid using clearly copyrighted images. Doing so can land you in legal trouble and is against the terms of service for all the major image generation model providers.  
这些示例演示了图像生成模型的功能，但我们在上传用于提示的基础图像时要小心。检查您计划上传并在提示中用作基础图像的图像的许可，并避免使用明显受版权保护的图像。这样做可能会给您带来法律麻烦，并且违反所有主要图像生成模型提供商的服务条款。

![pega 0110](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0110.png)

###### Figure 1-10. Photo by Jason Goodman on [Unsplash](https://oreil.ly/ZbzZy)  
图 1-10。杰森·古德曼 (Jason Goodman) 在 Unsplash 上拍摄的照片

# Evaluate Quality 4. 评估质量

As of yet, there has been no feedback loop to judge the quality of your responses, other than the basic trial and error of running the prompt and seeing the results, referred to as [_blind prompting_](https://oreil.ly/42rSz). This is fine when your prompts are used temporarily for a single task and rarely revisited. However, when you’re reusing the same prompt multiple times or building a production application that relies on a prompt, you need to be more rigorous with measuring results.  
到目前为止，除了运行提示并查看结果的基本尝试和错误（称为盲目提示）之外，还没有反馈循环来判断您的回答质量。当您的提示暂时用于单个任务并且很少重新访问时，这很好。但是，当您多次重复使用相同的提示或构建依赖于提示的生产应用程序时，您需要更加严格地测量结果。

There are a number of ways performance can be evaluated, and it depends largely on what tasks you’re hoping to accomplish. When a new AI model is released, the focus tends to be on how well the model did on _evals_ (evaluations), a standardized set of questions with predefined answers or grading criteria that are used to test performance across models. Different models perform differently across different types of tasks, and there is no guarantee a prompt that worked previously will translate well to a new model. OpenAI has [made its evals framework](https://oreil.ly/wolEL) for benchmarking performance of LLMs open source and encourages others to contribute additional eval templates.  
评估绩效的方法有很多种，这在很大程度上取决于您希望完成的任务。当新的人工智能模型发布时，人们关注的焦点往往是该模型在评估（eval）方面的表现如何，评估是一组带有预定义答案或评分标准的标准化问题，用于测试跨模型的性能。不同的模型在不同类型的任务中表现不同，并且不能保证以前有效的提示能够很好地转换为新模型。 OpenAI 已将其用于 LLMs 性能基准测试的评估框架开源，并鼓励其他人贡献更多评估模板。

In addition to the standard academic evals, there are also more headline-worthy tests like [GPT-4 passing the bar exam](https://oreil.ly/txhSZ). Evaluation is difficult for more subjective tasks, and can be time-consuming or prohibitively costly for smaller teams. In some instances researchers have turned to using more advanced models like GPT-4 to evaluate responses from less sophisticated models, as was done with [the release of Vicuna-13B](https://oreil.ly/NW3WX), a fine-tuned model based on Meta’s Llama open source model (see [Figure 1-11](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-11)).  
除了标准的学术评估之外，还有更多值得关注的测试，例如通过律师资格考试的 GPT-4。对于更主观的任务来说，评估很困难，对于较小的团队来说，评估可能非常耗时或成本高昂。在某些情况下，研究人员转向使用 GPT-4 等更先进的模型来评估不太复杂的模型的响应，就像发布 Vicuna-13B 所做的那样，Vicuna-13B 是一个基于 Meta 的 Llama 开源模型的微调模型（见图 1） -11）。

![pega 0111](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0111.png)

###### Figure 1-11. Vicuna GPT-4 Evals  
图 1-11。骆驼毛 GPT-4 评估

More rigorous evaluation techniques are necessary when writing scientific papers or grading a new foundation model release, but often you will only need to go just one step above basic trial and error. You may find that a simple thumbs-up/thumbs-down rating system implemented in a Jupyter Notebook can be enough to add some rigor to prompt optimization, without adding too much overhead. One common test is to see whether providing examples is worth the additional cost in terms of prompt length, or whether you can get away with providing no examples in the prompt. The first step is getting responses for multiple runs of each prompt and storing them in a spreadsheet, which we will do after setting up our environment.  
在撰写科学论文或对新的基础模型版本进行评分时，需要更严格的评估技术，但通常您只需要在基本的试错之上再迈出一步。您可能会发现，在 Jupyter Notebook 中实现的简单的赞成/反对评级系统足以为提示优化添加一些严格性，而不会增加太多开销。一种常见的测试是看看提供示例是否值得在提示长度方面付出额外的成本，或者您是否可以在提示中不提供示例。第一步是获取每个提示多次运行的响应并将其存储在电子表格中，我们将在设置环境后执行此操作。

You can install the OpenAI Python package with `pip install openai`. If you’re running into compatability issues with this package, create a virtual environment and install our [_requirements.txt_](https://oreil.ly/2KDV6) (instructions in the preface).  
您可以使用 `pip install openai` 安装 OpenAI Python 包。如果您遇到此软件包的兼容性问题，请创建一个虚拟环境并安装我们的requirements.txt（前言中的说明）。

To utilize the API, you’ll need to [create an OpenAI account](https://oreil.ly/oGv4j) and then [navigate here for your API key](https://oreil.ly/oHID1).  
要使用该 API，您需要创建一个 OpenAI 帐户，然后在此处导航以获取您的 API 密钥。

###### WARNING 警告

Hardcoding API keys in scripts is not recommended due to security reasons. Instead, utilize environment variables or configuration files to manage your keys.  
出于安全原因，不建议在脚本中对 API 密钥进行硬编码。相反，利用环境变量或配置文件来管理您的密钥。

Once you have an API key, it’s crucial to assign it as an environment variable by executing the following command, replacing `api_key` with your actual API key value:  
获得 API 密钥后，执行以下命令将其分配为环境变量至关重要，并将 `api_key` 替换为您的实际 API 密钥值：

```

export

```

Or on Windows: 或者在 Windows 上：

```

set

```

Alternatively, if you’d prefer not to preset an API key, then you can manually set the key while initializing the model, or load it from an _.env_ file using _[python-dotenv](https://oreil.ly/IaQjS)_. First, install the library with `pip install python-dotenv`, and then load the environment variables with the following code at the top of your script or notebook:  
或者，如果您不想预设 API 密钥，则可以在初始化模型时手动设置密钥，或使用 python-dotenv 从 .env 文件加载它。首先，使用 `pip install python-dotenv` 安装库，然后在脚本或笔记本顶部使用以下代码加载环境变量：

```

from

```

The first step is getting responses for multiple runs of each prompt and storing them in a spreadsheet.  
第一步是获取每个提示多次运行的响应并将其存储在电子表格中。

Input: 输入：

```

# Define two variants of the prompt to test zero-shot

```

Output: 输出：

  variant                                             prompt
  \
0       A  Product description: A pair of shoes that can ...
1       A  Product description: A pair of shoes that can ...
2       A  Product description: A pair of shoes that can ...
3       A  Product description: A pair of shoes that can ...
4       A  Product description: A pair of shoes that can ...
5       B  Product description: A home milkshake maker.\n...
6       B  Product description: A home milkshake maker.\n...
7       B  Product description: A home milkshake maker.\n...
8       B  Product description: A home milkshake maker.\n...
9       B  Product description: A home milkshake maker.\n...

                                            response
0  1. Adapt-a-Fit Shoes \n2. Omni-Fit Footwear \n...
1  1. OmniFit Shoes\n2. Adapt-a-Sneaks \n3. OneFi...
2  1. Adapt-a-fit\n2. Flexi-fit shoes\n3. Omni-fe...
3  1. Adapt-A-Sole\n2. FitFlex\n3. Omni-FitX\n4. ...
4  1. Omni-Fit Shoes\n2. Adapt-a-Fit Shoes\n3. An...
5  Adapt-a-Fit, Perfect Fit Shoes, OmniShoe, OneS...
6       FitAll, OmniFit Shoes, SizeLess, AdaptaShoes
7       AdaptaFit, OmniShoe, PerfectFit, AllSizeFit.
8  FitMaster, AdaptoShoe, OmniFit, AnySize Footwe...
9        Adapt-a-Shoe, PerfectFit, OmniSize, FitForm

Here we’re using the OpenAI API to generate model responses to a set of prompts and storing the results in a dataframe, which is saved to a CSV file. Here’s how it works:  
在这里，我们使用 OpenAI API 生成对一组提示的模型响应，并将结果存储在数据框中，该数据框保存到 CSV 文件中。它的工作原理如下：

1. Two prompt variants are defined, and each variant consists of a product description, seed words, and potential product names, but `prompt_B` provides two examples.  
    定义了两个提示变体，每个变体由产品描述、种子词和潜在产品名称组成，但 `prompt_B` 提供了两个示例。
    
2. Import statements are called for the Pandas library, OpenAI library, and os library.  
    Pandas 库、OpenAI 库和 os 库调用导入语句。
    
3. The `get_response` function takes a prompt as input and returns a response from the `gpt-3.5-turbo` model. The prompt is passed as a user message to the model, along with a system message to set the model’s behavior.  
    `get_response` 函数将提示作为输入，并从 `gpt-3.5-turbo` 模型返回响应。提示作为用户消息传递到模型，并连同用于设置模型行为的系统消息。
    
4. Two prompt variants are stored in the `test_prompts` list.  
    `test_prompts` 列表中存储了两个提示变体。
    
5. An empty list `responses` is created to store the generated responses, and the variable `num_tests` is set to 5.  
    创建一个空列表 `responses` 来存储生成的响应，并将变量 `num_tests` 设置为 5。
    
6. A nested loop is used to generate responses. The outer loop iterates over each prompt, and the inner loop generates `num_tests` (five in this case) number of responses per prompt.  
    嵌套循环用于生成响应。外部循环迭代每个提示，内部循环为每个提示生成 `num_tests` （本例中为 5）个响应。
    
    1. The `enumerate` function is used to get the index and value of each prompt in `test_prompts`. This index is then converted to a corresponding uppercase letter (e.g., 0 becomes _A_, 1 becomes _B_) to be used as a variant name.  
        `enumerate` 函数用于获取 `test_prompts` 中每个提示的索引和值。然后将该索引转换为相应的大写字母（例如，0 变为 A，1 变为 B）以用作变体名称。
        
    2. For each iteration, the `get_response` function is called with the current prompt to generate a response from the model.  
        对于每次迭代，都会使用当前提示调用 `get_response` 函数，以从模型生成响应。
        
    3. A dictionary is created with the variant name, the prompt, and the model’s response, and this dictionary is appended to the `responses` list.  
        使用变体名称、提示和模型响应创建一个字典，并将该字典附加到 `responses` 列表中。
        
7. Once all responses have been generated, the `responses` list (which is now a list of dictionaries) is converted into a Pandas DataFrame.  
    生成所有响应后， `responses` 列表（现在是字典列表）将转换为 Pandas DataFrame。
    
8. This dataframe is then saved to a CSV file with the Pandas built-in `to_csv` function, making the file _responses.csv_ with `index=False` so as to not write row indices.  
    然后使用 Pandas 内置 `to_csv` 函数将该数据帧保存到 CSV 文件中，使文件response.csv 带有 `index=False` 以便不写入行索引。
    
9. Finally, the dataframe is printed to the console.  
    最后，数据帧被打印到控制台。
    

Having these responses in a spreadsheet is already useful, because you can see right away even in the printed response that `prompt_A` (zero-shot) in the first five rows is giving us a numbered list, whereas `prompt_B` (few-shot) in the last five rows tends to output the desired format of a comma-separated inline list. The next step is to give a rating on each of the responses, which is best done blind and randomized to avoid favoring one prompt over another.  
在电子表格中包含这些响应已经很有用，因为即使在打印的响应中，您也可以立即看到前五行中的 `prompt_A` （零样本）为我们提供了一个编号列表，而 `prompt_B` (few-shot) 倾向于输出以逗号分隔的内联列表的所需格式。下一步是对每个答案进行评分，最好是盲目和随机进行评分，以避免偏向某一提示而不是另一提示。

Input: 输入：

```

import

```

The output is shown in [Figure 1-12](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-12):  
输出如图 1-12 所示：

![pega 0112](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0112.png)

###### Figure 1-12. Thumbs-up/thumbs-down rating system  
图 1-12。赞成/反对评级系统

If you run this in a Jupyter Notebook, a widget displays each AI response, with a thumbs-up or thumbs-down button (see [Figure 1-12](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-12)) This provides a simple interface for quickly labeling responses, with minimal overhead. If you wish to do this outside of a Jupyter Notebook, you could change the thumbs-up and thumbs-down emojis for _Y_ and _N_, and implement a loop using the built-in `input()` function, as a text-only replacement for iPyWidgets.  
如果您在 Jupyter Notebook 中运行此程序，小部件会显示每个 AI 响应，并带有“赞成”或“反对”按钮（见图 1-12）。这提供了一个简单的界面，可以以最小的开销快速标记响应。如果您希望在 Jupyter Notebook 之外执行此操作，您可以更改 Y 和 N 的拇指向上和拇指向下表情符号，并使用内置 `input()` 函数以文本形式实现循环- 仅替代 iPyWidgets。

Once you’ve finished labeling the responses, you get the output, which shows you how each prompt performs.  
完成对响应的标记后，您将获得输出，其中显示每个提示的执行情况。

Output: 输出：

A/B testing completed. Here's the results:
  variant  count  score
0       A      5    0.2
1       B      5    0.6

The dataframe was shuffled at random, and each response was labeled blind (without seeing the prompt), so you get an accurate picture of how often each prompt performed. Here is the step-by-step explanation:  
数据框被随机打乱，每个响应都被标记为盲（看不到提示），因此您可以准确了解每个提示执行的频率。以下是分步说明：

1. Three modules are imported: `ipywidgets`, `IPython.display`, and `pandas`. `ipywidgets` contains interactive HTML widgets for Jupyter Notebooks and the IPython kernel. `IPython.display` provides classes for displaying various types of output like images, sound, displaying HTML, etc. Pandas is a powerful data manipulation library.  
    导入三个模块： `ipywidgets` 、 `IPython.display` 和 `pandas` 。 `ipywidgets` 包含 Jupyter Notebooks 和 IPython 内核的交互式 HTML 小部件。 `IPython.display` 提供了用于显示各种类型输出的类，如图像、声音、显示 HTML 等。Pandas 是一个强大的数据操作库。
    
2. The pandas library is used to read in the CSV file _responses.csv_, which contains the responses you want to test. This creates a Pandas DataFrame called `df`.  
    pandas 库用于读取 CSV 文件response.csv，其中包含您要测试的响应。这将创建一个名为 `df` 的 Pandas DataFrame。
    
3. `df` is shuffled using the `sample()` function with `frac=1`, which means it uses all the rows. The `reset_index(drop=True)` is used to reset the indices to the standard 0, 1, 2, …​, n index.  
    `df` 使用 `sample()` 函数与 `frac=1` 进行混洗，这意味着它使用所有行。 `reset_index(drop=True)` 用于将索引重置为标准 0, 1, 2, …​, n 索引。
    
4. The script defines `response_index` as 0. This is used to track which response from the dataframe the user is currently viewing.  
    该脚本将 `response_index` 定义为 0。这用于跟踪用户当前正在查看的数据帧的响应。
    
5. A new column `feedback` is added to the dataframe `df` with the data type as `str` or string.  
    新列 `feedback` 将添加到数据框 `df` 中，数据类型为 `str` 或字符串。
    
6. Next, the script defines a function `on_button_clicked(b)`, which will execute whenever one of the two buttons in the interface is clicked.  
    接下来，该脚本定义一个函数 `on_button_clicked(b)` ，只要单击界面中的两个按钮之一，该函数就会执行。
    
    1. The function first checks the `description` of the button clicked was the thumbs-up button (`\U0001F44D`; ![thumbs up 1f44d](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/thumbs-up_1f44d.png)), and sets `user_feedback` as 1, or if it was the thumbs-down button (`\U0001F44E` ![thumbs down 1f44e](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/thumbs-down_1f44e.png)), it sets `user_feedback` as 0.  
        该函数首先检查单击的按钮的 `description` 是竖起大拇指按钮（ `\U0001F44D` ; ![thumbs up 1f44d](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/thumbs-up_1f44d.png) ），并将 `user_feedback` 设置为1，或者如果是拇指向下按钮 ( `\U0001F44E` ![thumbs down 1f44e](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/thumbs-down_1f44e.png) )，则将 `user_feedback` 设置为 0。
        
    2. Then it updates the `feedback` column of the dataframe at the current `response_index` with `user_feedback`.  
        然后它用 `user_feedback` 更新当前 `response_index` 处数据帧的 `feedback` 列。
        
    3. After that, it increments `response_index` to move to the next response.  
        之后，它会递增 `response_index` 以移至下一个响应。
        
    4. If `response_index` is still less than the total number of responses (i.e., the length of the dataframe), it calls the function `update_response()`.  
        如果 `response_index` 仍然小于响应总数（即数据帧的长度），则调用函数 `update_response()` 。
        
    5. If there are no more responses, it saves the dataframe to a new CSV file _results.csv_, then prints a message, and also prints a summary of the results by variant, showing the count of feedback received and the average score (mean) for each variant.  
        如果没有更多响应，它将数据帧保存到新的 CSV 文件 results.csv，然后打印一条消息，并按变体打印结果摘要，显示收到的反馈计数和平均分数（平均值）每个变体。
        
7. The function `update_response()` fetches the next response from the dataframe, wraps it in paragraph HTML tags (if it’s not null), updates the `response` widget to display the new response, and updates the `count_label` widget to reflect the current response number and total number of responses.  
    函数 `update_response()` 从数据帧中获取下一个响应，将其包装在段落 HTML 标记中（如果它不为空），更新 `response` 小部件以显示新响应，并更新 < b2> 小部件反映当前响应数和响应总数。
    
8. Two widgets, `response` (an HTML widget) and `count_label` (a Label widget), are instantiated. The `update_response()` function is then called to initialize these widgets with the first response and the appropriate label.  
    两个小部件 `response` （HTML 小部件）和 `count_label` （Label 小部件）被实例化。然后调用 `update_response()` 函数以使用第一个响应和适当的标签来初始化这些小部件。
    
9. Two more widgets, `thumbs_up_button` and `thumbs_down_button` (both Button widgets), are created with thumbs-up and thumbs-down emoji as their descriptions, respectively. Both buttons are configured to call the `on_button_clicked()` function when clicked.  
    另外两个小部件 `thumbs_up_button` 和 `thumbs_down_button` （都是按钮小部件）是分别使用拇指向上和拇指向下表情符号作为其描述来创建的。这两个按钮都配置为在单击时调用 `on_button_clicked()` 函数。
    
10. The two buttons are grouped into a horizontal box (`button_box`) using the `HBox` function.  
    使用 `HBox` 函数将两个按钮分组到一个水平框 ( `button_box` ) 中。
    
11. Finally, the `response`, `button_box`, and `count_label` widgets are displayed to the user using the `display()` function from the `IPython.display` module.  
    最后，使用 `IPython.display` 、 `button_box` 和 `count_label` 小部件。 b4> 模块。
    

A simple rating system such as this one can be useful in judging prompt quality and encountering edge cases. Usually in less than 10 test runs of a prompt you uncover a deviation, which you otherwise wouldn’t have caught until you started using it in production. The downside is that it can get tedious rating lots of responses manually, and your ratings might not represent the preferences of your intended audience. However, even small numbers of tests can reveal large differences between two prompting strategies and reveal nonobvious issues before reaching production.  
像这样的简单评级系统可用于判断即时质量和遇到边缘情况。通常，在提示的不到 10 次测试运行中，您就会发现一个偏差，否则您将无法发现该偏差，直到您开始在生产中使用它为止。缺点是，它可能会手动对大量回复进行繁琐的评级，并且您的评级可能不代表目标受众的偏好。然而，即使少量的测试也可以揭示两种提示策略之间的巨大差异，并在投入生产之前揭示不明显的问题。

Iterating on and testing prompts can lead to radical decreases in the length of the prompt and therefore the cost and latency of your system. If you can find another prompt that performs equally as well (or better) but uses a shorter prompt, you can afford to scale up your operation considerably. Often you’ll find in this process that many elements of a complex prompt are completely superfluous, or even counterproductive.  
迭代和测试提示可以大大缩短提示的长度，从而降低系统的成本和延迟。如果您能找到另一个性能同样好（或更好）但使用更短提示的提示，您就可以大幅扩展您的操作。通常，您会发现在此过程中，复杂提示的许多元素完全是多余的，甚至适得其反。

The _thumbs-up_ or other manually labeled indicators of quality don’t have to be the only judging criteria. Human evaluation is generally considered to be the most accurate form of feedback. However, it can be tedious and costly to rate many samples manually. In many cases, as in math or classification use cases, it may be possible to establish _ground truth_ (reference answers to test cases) to programmatically rate the results, allowing you to scale up considerably your testing and monitoring efforts. The following is not an exhaustive list because there are many motivations for evaluating your prompt programmatically:  
竖起大拇指或其他手动标记的质量指标不一定是唯一的评判标准。人类评估通常被认为是最准确的反馈形式。然而，手动对许多样本进行评级可能是乏味且昂贵的。在许多情况下，如在数学或分类用例中，可以建立基本事实（测试用例的参考答案）以编程方式对结果进行评级，从而允许您大幅扩展测试和监控工作。以下并不是详尽的列表，因为以编程方式评估提示的动机有很多：

Cost 成本

Prompts that use a lot of tokens, or work only with more expensive models, might be impractical for production use.  
使用大量令牌或仅适用于更昂贵的模型的提示对于生产用途可能不切实际。

Latency 潜伏

Equally the more tokens there are, or the larger the model required, the longer it takes to complete a task, which can harm user experience.  
同样，代币越多，或者所需的模型越大，完成任务所需的时间就越长，这可能会损害用户体验。

Calls 通话

Many AI systems require multiple calls in a loop to complete a task, which can seriously slow down the process.  
许多人工智能系统需要循环多次调用才能完成任务，这会严重减慢进程。

Performance 表现

Implement some form of external feedback system, for example a physics engine or other model for predicting real-world results.  
实施某种形式的外部反馈系统，例如物理引擎或其他用于预测现实世界结果的模型。

Classification 分类

Determine how often a prompt correctly labels given text, using another AI model or rules-based labeling.  
使用其他 AI 模型或基于规则的标签确定提示正确标记给定文本的频率。

Reasoning 推理

Work out which instances the AI fails to apply logical reasoning or gets the math wrong versus reference cases.  
与参考案例相比，找出人工智能未能应用逻辑推理或数学错误的实例。

Hallucinations 幻觉

See how frequently you encouner hallucinations, as measured by invention of new terms not included in the prompt’s context.  
看看您遇到幻觉的频率，通过发明未包含在提示上下文中的新术语来衡量。

Safety 安全

Flag any scenarios where the system might return unsafe or undesirable results using a safety filter or detection system.  
使用安全过滤器或检测系统标记系统可能返回不安全或不良结果的任何场景。

Refusals 拒绝

Find out how often the system incorrectly refuses to fulfill a reasonable user request by flagging known refusal language.  
通过标记已知的拒绝语言，了解系统错误地拒绝满足合理用户请求的频率。

Adversarial 对抗性的

Make the prompt robust against known [prompt injection](https://oreil.ly/KGAqe) attacks that can get the model to run undesirable prompts instead of what you programmed.  
使提示能够抵御已知的提示注入攻击，这些攻击可以使模型运行不需要的提示而不是您编程的提示。

Similarity 相似

Use shared words and phrases ([BLEU or ROGUE](https://oreil.ly/iEGZ9)) or vector distance (explained in [Chapter 5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch05.html#vector_databases_05)) to measure similarity between generated and reference text.  
使用共享单词和短语（BLEU 或 ROGUE）或矢量距离（第 5 章中说明）来衡量生成文本和参考文本之间的相似性。

Once you start rating which examples were good, you can more easily update the examples used in your prompt as a way to continuously make your system smarter over time. The data from this feedback can also feed into examples for fine-tuning, which starts to beat prompt engineering once you can [supply a few thousand examples](https://oreil.ly/DZ-br), as shown in [Figure 1-13](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-13).  
一旦您开始评估哪些示例不错，您就可以更轻松地更新提示中使用的示例，从而随着时间的推移不断使您的系统变得更加智能。来自此反馈的数据还可以输入到示例中进行微调，一旦您可以提供几千个示例，微调就开始胜过即时工程，如图 1-13 所示。

![pega 0113](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0113.png)

###### Figure 1-13. How many data points is a prompt worth?  
图 1-13。一个提示值多少个数据点？

Graduating from thumbs-up or thumbs-down, you can implement a 3-, 5-, or 10-point rating system to get more fine-grained feedback on the quality of your prompts. It’s also possible to determine aggregate relative performance through comparing responses side by side, rather than looking at responses one at a time. From this you can construct a fair across-model comparison using an _[Elo rating](https://oreil.ly/TlldE)_, as is popular in chess and used in the [Chatbot Arena](https://oreil.ly/P2IcU) by _lmsys.org_.  
从赞成或反对毕业，您可以实施 3 分、5 分或 10 分评级系统，以获得有关提示质量的更细粒度的反馈。还可以通过并排比较响应来确定总体相对性能，而不是一次查看一个响应。由此，您可以使用 Elo 评级构建公平的跨模型比较，这在国际象棋中很流行，并由 lmsys.org 在 Chatbot Arena 中使用。

For image generation, evaluation usually takes the form of _permutation_ prompting, where you input multiple directions or formats and generate an image for each combination. Images can than be scanned or later arranged in a grid to show the effect that different elements of the prompt can have on the final image.  
对于图像生成，评估通常采用排列提示的形式，您输入多个方向或格式，并为每个组合生成图像。然后可以扫描图像或稍后将图像排列在网格中，以显示提示的不同元素对最终图像的影响。

Input: 输入：

{stock photo, oil painting, illustration} of business
meeting of {four, eight} people watching on white MacBook on
top of glass-top table

In Midjourney this would be compiled into six different prompts, one for every combination of the three formats (stock photo, oil painting, illustration) and two numbers of people (four, eight).  
在《中途旅程》中，这将被编译成六种不同的提示，一种对应三种格式（库存照片、油画、插图）和两种人数（四人、八人）的每一种组合。

Input: 输入：

1. stock photo of business meeting of four people watching
on white MacBook on top of glass-top table

2. stock photo of business meeting of eight people watching
on white MacBook on top of glass-top table

3. oil painting of business meeting of four people watching
on white MacBook on top of glass-top table

4. oil painting of business meeting of eight people watching
on white MacBook on top of glass-top table

5. illustration of business meeting of four people watching
on white MacBook on top of glass-top table

6. illustration of business meeting of eight people watching
on white MacBook on top of glass-top table

Each prompt generates its own four images as usual, which makes the output a little harder to see. We have selected one from each prompt to upscale and then put them together in a grid, shown as [Figure 1-14](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-14). You’ll notice that the model doesn’t always get the correct number of people (generative AI models are surprisingly bad at math), but it has correctly inferred the general intention by adding more people to the photos on the right than the left.  
每个提示都会像往常一样生成自己的四个图像，这使得输出有点难以查看。我们从每个提示中选择一个进行升级，然后将它们放在一个网格中，如图 1-14 所示。你会注意到，该模型并不总是能得到正确的人数（生成式 AI 模型的数学出奇地糟糕），但它通过在右侧照片中添加比左侧更多的人来正确推断出总体意图。

[Figure 1-14](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-14) shows the output.  
图 1-14 显示了输出。

![pega 0114](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0114.png)

###### Figure 1-14. Prompt permutations grid  
图 1-14。提示排列网格

With models that have APIs like Stable Diffusion, you can more easily manipulate the photos and display them in a grid format for easy scanning. You can also manipulate the random seed of the image to fix a style in place for maximum reproducibility. With image classifiers it may also be possible to programmatically rate images based on their safe content, or if they contain certain elements associated with success or failure.  
借助具有稳定扩散等 API 的模型，您可以更轻松地操作照片并以网格格式显示它们，以便于扫描。您还可以操纵图像的随机种子来固定样式，以获得最大的可重复性。使用图像分类器，还可以根据图像的安全内容，或者图像是否包含与成功或失败相关的某些元素，以编程方式对图像进行评级。

# Divide Labor 5. 分工

As you build out your prompt, you start to get to the point where you’re asking a lot in a single call to the AI. When prompts get longer and more convoluted, you may find the responses get less deterministic, and hallucinations or anomalies increase. Even if you manage to arrive at a reliable prompt for your task, that task is likely just one of a number of interrelated tasks you need to do your job. It’s natural to start exploring how many other of these tasks could be done by AI and how you might string them together.  
当你构建提示时，你开始在一次对人工智能的调用中提出很多问题。当提示变得更长、更复杂时，您可能会发现响应的确定性降低，并且幻觉或异常现象会增加。即使您设法为您的任务找到可靠的提示，该任务也可能只是您完成工作所需的众多相互关联的任务之一。我们很自然地会开始探索人工智能可以完成多少其他任务以及如何将它们串联起来。

One of the core principles of engineering is to use task decomposition to break problems down into their component parts, so you can more easily solve each individual problem and then reaggregate the results. Breaking your AI work into multiple calls that are chained together can help you accomplish more complex tasks, as well as provide more visibility into what part of the chain is failing.  
工程的核心原则之一是使用任务分解将问题分解为各个组成部分，这样您就可以更轻松地解决每个单独的问题，然后重新聚合结果。将您的 AI 工作分解为多个链接在一起的调用可以帮助您完成更复杂的任务，并更清楚地了解该链的哪个部分发生了故障。

There are lots of factors that go into product naming, and an important task is naively outsourced to the AI with no visibility into how it’s weighing the importance of these factors (if at all). The way our current system works, we’re getting a list of names, but all names are displayed with equal importance with no further context for helping us decide. Fortunately AI tools are capable of self-evaluation; if we add a second step to our task, we can automatically check for nondesirable outputs.  
产品命名涉及很多因素，而一项重要任务被天真地外包给人工智能，而无法了解它如何权衡这些因素的重要性（如果有的话）。按照我们当前系统的工作方式，我们会得到一个名称列表，但所有名称都以同等重要性显示，没有进一步的上下文来帮助我们做出决定。幸运的是，人工智能工具能够自我评估；如果我们在任务中添加第二步，我们可以自动检查不需要的输出。

Input: 输入：

Rate this list of product names for a pair of shoes that can
fit any foot size. The rating should be out of 10, inline
next to the product name:

UniFit SoleStrides
FlexiSize All-Fit Shoes
OmniFit FootFlex
...
AnyStep AdaptiWalkers
FlexiRange UniversalSteps
PerfectGlide MultiFit Shoes

Output: 输出：

UniFit SoleStrides: 7/10
FlexiSize All-Fit Shoes: 8/10
OmniFit FootFlex: 7/10
...
AnyStep AdaptiWalkers: 7/10
FlexiRange UniversalSteps: 7.5/10
PerfectGlide MultiFit Shoes: 9/10

This ranking is based on clarity, memorability, and how well
the name communicates the unique selling point of the
product (that they can fit any foot size). Remember, these
ratings are subjective and the ultimate success of a product
name also depends on the target market, branding, and
marketing efforts.

In running this multiple times, it consistently rates the name “OneSize Glovewalkers” as the worst, providing context (if you ask) that the concept might be confusing in a shoe context. You may be wondering why, if the model _knows_ this is a bad name, does it suggest it in the first place? LLMs work by predicting the next token in a sequence and therefore struggle to know what the overall response will be when finished. However, when it has all the tokens from a previous response to review, it can more easily predict whether this would be labeled as a good or bad response.  
在多次运行此过程中，它始终将“OneSize Glovewalkers”这个名称评为最差的，提供了上下文（如果您问的话），该概念在鞋子上下文中可能会令人困惑。您可能想知道，如果模型知道这是一个坏名字，为什么它首先会建议它？ LLMs 通过预测序列中的下一个标记来工作，因此很难知道完成后的总体响应是什么。然而，当它拥有之前响应的所有标记进行审查时，它可以更轻松地预测这是否会被标记为好响应或坏响应。

We can continue to chain multiple calls together to improve the results of our task. For example, we could split this into three separate ratings: clarity, memorability, and how well the name communicates the unique selling point of the product. These ratings could then be given to a human as additional context on the final decision, or even calculated together to select the final name programmatically.  
我们可以继续将多个调用链接在一起以改进我们的任务结果。例如，我们可以将其分为三个单独的评级：清晰度、易记性以及名称传达产品独特卖点的程度。然后可以将这些评级作为最终决策的附加背景提供给人类，甚至可以一起计算以通过编程方式选择最终名称。

The real unlock in learning to work professionally with AI versus just playing around with prompting is realizing that every part of the system can be broken down into a series of iterative steps. Even with a single prompt this principles applies, as simply appending `Let's think step by step` to the prompt can lead to demonstrable gains in reasoning and proficiency, as well as provide an audit trail for quality assurance and debugging. When taking the time and tokens to reason, the ratings change and are more consistent with the scoring criteria.  
学习专业地使用人工智能工作而不只是玩弄提示，真正的解锁是认识到系统的每个部分都可以分解为一系列迭代步骤。即使只有一个提示，该原则也适用，因为只需将 `Let's think step by step` 附加到提示即可在推理和熟练程度方面带来明显的收益，并为质量保证和调试提供审核跟踪。当花时间和标记进行推理时，评级会发生变化并且与评分标准更加一致。

Input: 输入：

Let's think step by step. Rate this list of product names
for a pair of shoes that can fit any foot size. The rating
should be out of 10, inline next to the product name:

UniFit SoleStrides
FlexiSize All-Fit Shoes
OmniFit FootFlex
...
AnyStep AdaptiWalkers
FlexiRange UniversalSteps
PerfectGlide MultiFit Shoes

Output: 输出：

Here's a rating out of 10 for each product name, considering
factors like descriptiveness, catchiness, and overall
appeal:

1. **UniFit SoleStrides**: 7/10 - Sounds unifying but may
not immediately convey the "fit any size" idea.
2. **FlexiSize All-Fit Shoes**: 8.5/10 - Combines
flexibility and the notion that it fits all sizes.
3. **OmniFit FootFlex**: 8/10 - Omnipresence (fitting all)
and flexibility nicely conveyed.
...
18. **AnyStep AdaptiWalkers**: 7.5/10 - "AnyStep" suggests
versatility, but the overall name might be less direct.
19. **FlexiRange UniversalSteps**: 8/10 - Combines
flexibility and universal fit.
20. **PerfectGlide MultiFit Shoes**: 8.5/10 - "MultiFit" is
clear, and "PerfectGlide" suggests a comfortable experience.

Remember, the best name can also be influenced by your
target audience, branding strategy, and the overall message
you want to convey.

OpenAI [calls this](https://oreil.ly/0MZ3-) “giving the model time to think,” and it is a key tenet of prompt engineering. In effect, _chain of thought_ techniques like this, where the model is encouraged to list out its steps, are like dividing a task within the same prompt. Once we’ve automated product naming given a product idea, we can call ChatGPT again to describe each product, which in turn can be fed into Midjourney to generate an image of each product. Using an AI model to generate a prompt for an AI model is _meta prompting_, and it works because LLMs are human-level prompt engineers ([Zhou, 2022](https://oreil.ly/Dwszu)).  
OpenAI 称之为“给模型时间思考”，这是即时工程的关键原则。实际上，像这样的思维链技术鼓励模型列出其步骤，就像在同一提示中划分任务一样。一旦我们根据产品想法自动命名产品，我们就可以再次调用 ChatGPT 来描述每个产品，然后将其输入 Midjourney 中以生成每个产品的图像。使用 AI 模型为 AI 模型生成提示是元提示，它之所以有效，是因为 LLMs 是人类级别的提示工程师（Zhou，2022）。

Input: 输入：

Describe the new product "OneFit UltraStride Shoes," a shoe
that can fit any foot size, in great detail:

Output: 输出：

Introducing the revolutionary "OneFit UltraStride Shoes,"
the footwear innovation designed to fit any foot size with
unparalleled comfort and style. These shoes are a result of
cutting-edge technology and meticulous craftsmanship,
ensuring a truly personalized and enjoyable walking or
running experience for everyone.

Design and Materials:
The OneFit UltraStride Shoes boast an elegant and modern
design that appeals to both fashion-forward individuals and
sports enthusiasts. They feature a sleek and streamlined
silhouette, crafted using premium materials for durability
and aesthetic appeal. The shoe's upper is constructed from a
combination of breathable mesh and flexible synthetic
materials, allowing for excellent airflow and a lightweight
feel.

...

Color and Customization:
OneFit UltraStride Shoes are available in a variety of
vibrant colors and stylish patterns, catering to diverse
personal preferences. You can choose from classic
monochromatic options for a timeless look or opt for bold
and vibrant hues to make a fashion statement. The ability to
customize the shoe's appearance allows individuals to
express their unique style while enjoying the benefits of
the OneFit technology.

Conclusion:
The OneFit UltraStride Shoes represent a breakthrough in
footwear technology, eliminating the hassle of finding the
perfect fit for your feet. With their adaptive design,
superior comfort, and stylish aesthetics, these shoes offer
a truly personalized experience for individuals of all foot
sizes. Stay comfortable, confident, and on-trend with the
OneFit UltraStride Shoes, the ultimate choice for those
seeking unmatched versatility and a perfect fit.

DALL-E is well-known by GPT-4, and therefore you can invoke its name within ChatGPT and it does a reasonable job at crafting a prompt for an image generation tool. If you were planning on using this prompt in production, you may consider applying the prompting principle of providing examples, but it does a good enough job for our purposes without examples.  
DALL-E 在 GPT-4 中广为人知，因此您可以在 ChatGPT 中调用它的名称，并且它在为图像生成工具制作提示方面做得相当不错。如果您计划在生产中使用此提示，您可以考虑应用提供示例的提示原则，但对于我们的目的而言，无需示例它就已经足够好了。

Input: 输入：

Convert this description into a short prompt for an AI image
generation model such as DALL-E:

Output: 输出：

Create an eye-catching image that visually represents the
"OneFit UltraStride Shoes," a revolutionary footwear product
that adapts to any foot size. Showcase a sleek and modern
shoe design incorporating a stretchable upper, an adjustable
lacing system, and a cushioned insole for optimal comfort.
Emphasize the shoe's versatility by displaying it in action
on various surfaces, highlighting its excellent traction.
Incorporate vibrant colors and patterns to convey the
customizable nature of the product. The image should capture
the essence of innovation, style, and personalized fit that
the OneFit UltraStride Shoes offer.

The output of this prompt can now be plugged into image generation tools like DALL-E or Midjourney as a prompt, which can give you a good starting point for visualizing what the product might look like. Although this might not be the final design you go with, seeing an image is more evocative and helps people form an opinion faster. It’s easier cognitively to criticize or compliment an existing image than it is to imagine a new image from a blank page or section of text.  
现在可以将此提示的输出作为提示插入到 DALL-E 或 Midjourney 等图像生成工具中，这可以为您提供一个良好的起点来可视化产品的外观。尽管这可能不是您最终采用的设计，但看到图像更能唤起人们的回忆，并帮助人们更快地形成意见。从认知上来说，批评或赞美现有图像比从空白页面或文本部分想象新图像更容易。

[Figure 1-15](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#figure-1-15) shows the output.  
图 1-15 显示了输出。

![pega 0115](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0115.png)

###### Figure 1-15. OneFit UltraStride shoes  
图 1-15。 OneFit UltraStride 鞋

It’s common practice when working with AI professionally to chain multiple calls to AI together, and even multiple models, to accomplish more complex goals. Even single-prompt applications are often built dynamically, based on outside context queried from various databases or other calls to an AI model. The library [LangChain](https://www.langchain.com/) has developed tooling for chaining multiple prompt templates and queries together, making this process more observable and well structured. A foundational example is progressive summarization, where text that is too large to fit into a context window can be split into multiple chunks of text, with each being summarized, before finally summarizing the summaries. If you talk to builders of early AI products, you’ll find they’re all under the hood chaining multiple prompts together, called _AI chaining_, to accomplish better results in the final output.  
在专业地使用人工智能时，通常的做法是将对人工智能的多个调用链接在一起，甚至多个模型，以实现更复杂的目标。即使单提示应用程序也通常是基于从各种数据库查询的外部上下文或对人工智能模型的其他调用动态构建的。 LangChain 库开发了用于将多个提示模板和查询链接在一起的工具，使该过程更加可观察且结构良好。一个基本的例子是渐进式摘要，其中太大而无法放入上下文窗口的文本可以被分成多个文本块，每个文本块都被总结，然后最后总结摘要。如果你与早期人工智能产品的构建者交谈，你会发现他们都在幕后将多个提示链接在一起，称为人工智能链接，以在最终输出中实现更好的结果。

The [Reason and Act (ReAct)](https://oreil.ly/tPPW9) framework was one of the first popular attempts at AI agents, including the open source projects [BabyAGI](https://oreil.ly/TEiQx), [AgentGPT](https://oreil.ly/48lq6) and [Microsoft AutoGen](https://oreil.ly/KG5Xl). In effect, these agents are the result of chaining multiple AI calls together in order to plan, observe, act, and then evaluate the results of the action. Autonomous agents will be covered in [Chapter 6](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch06.html#autonomous_agents_06) but are still not widely used in production at the time of writing. This practice of self-reasoning agents is still early and prone to errors, but there are promising signs this approach can be useful in achieving complex tasks, and is likely to be part of the next stage in evolution for AI systems.  
Reason and Act (ReAct) 框架是人工智能代理的最早流行尝试之一，包括开源项目 BabyAGI、AgentGPT 和 Microsoft AutoGen。实际上，这些代理是将多个人工智能调用链接在一起的结果，以便计划、观察、行动，然后评估行动的结果。自主代理将在第 6 章中介绍，但在撰写本文时仍未在生产中广泛使用。这种自我推理代理的实践还处于早期阶段，并且容易出错，但有迹象表明这种方法可用于完成复杂的任务，并且很可能成为人工智能系统下一阶段进化的一部分。

There is an AI battle occurring between large tech firms like Microsoft and Google, as well as a wide array of open source projects on Hugging Face, and venture-funded start-ups like OpenAI and Anthropic. As new models continue to proliferate, they’re diversifying in order to compete for different segments of the growing market. For example, Anthropic’s Claude 2 had an [100,000-token context window](https://oreil.ly/NQcFW), compared to GPT-4’s standard [8,192 tokens](https://oreil.ly/iZhMl). OpenAI soon responded with a [128,000-token window version of GPT-4](https://oreil.ly/3TTZ9), and Google touts a 1 million token context length with [Gemini 1.5](https://oreil.ly/cyhR4). For comparison, one of the Harry Potter books would be around 185,000 tokens, so it may become common for an entire book to fit inside a single prompt, though processing millions of tokens with each API call may be cost prohibitive for most use cases.  
微软和谷歌等大型科技公司、Hugging Face 上的各种开源项目以及 OpenAI 和 Anthropic 等风险投资初创公司之间正在展开一场人工智能之战。随着新车型不断涌现，它们正在走向多元化，以争夺不断增长的市场的不同细分市场。例如，Anthropic 的 Claude 2 具有 100,000 个令牌上下文窗口，而 GPT-4 的标准有 8,192 个令牌。 OpenAI 很快就推出了 128,000 个令牌窗口版本的 GPT-4，而 Google 则宣称 Gemini 1.5 具有 100 万个令牌上下文长度。相比之下，一本《哈利·波特》书籍大约有 185,000 个令牌，因此将整本书放入一个提示中可能会变得很常见，尽管对于大多数用例来说，每次 API 调用处理数百万个令牌可能成本过高。

This book focuses on GPT-4 for text generation techniques, as well as Midjourney v6 and Stable Diffusion XL for image generation techniques, but within months these models may no longer be state of the art. This means it will become increasingly important to be able to select the right model for the job and chain multiple AI systems together. Prompt templates are rarely comparable when transferring to a new model, but the effect of the Five Prompting Principles will consistently improve any prompt you use, for any model, getting you more reliable results.  
本书重点介绍用于文本生成技术的 GPT-4，以及用于图像生成技术的 Midjourney v6 和 Stable Diffusion XL，但几个月内这些模型可能不再是最先进的。这意味着能够为工作选择正确的模型并将多个人工智能系统链接在一起将变得越来越重要。转移到新模型时，提示模板很少具有可比性，但是五项提示原则的效果将持续改进您使用的任何模型的任何提示，为您提供更可靠的结果。

# Summary 概括

In this chapter, you learned about the importance of prompt engineering in the context of generative AI. We defined prompt engineering as the process of developing effective prompts that yield desired results when interacting with AI models. You discovered that providing clear direction, formatting the output, incorporating examples, establishing an evaluation system, and dividing complex tasks into smaller prompts are key principles of prompt engineering. By applying these principles and using common prompting techniques, you can improve the quality and reliability of AI-generated outputs.  
在本章中，您了解了生成式人工智能背景下即时工程的重要性。我们将提示工程定义为开发有效提示的过程，在与人工智能模型交互时产生期望的结果。您发现，提供明确的方向、格式化输出、合并示例、建立评估系统以及将复杂的任务划分为更小的提示是提示工程的关键原则。通过应用这些原则并使用常见的提示技术，您可以提高 AI 生成的输出的质量和可靠性。

You also explored the role of prompt engineering in generating product names and images. You saw how specifying the desired format and providing instructive examples can greatly influence the AI’s output. Additionally, you learned about the concept of role-playing, where you can ask the AI to generate outputs as if it were a famous person like Steve Jobs. The chapter emphasized the need for clear direction and context to achieve desired outcomes when using generative AI models. Furthermore, you discovered the importance of evaluating the performance of AI models and the various methods used for measuring results, as well as the trade-offs between quality and token usage, cost, and latency.  
您还探讨了提示工程在生成产品名称和图像中的作用。您看到了指定所需的格式并提供指导性示例如何极大地影响人工智能的输出。此外，您还了解了角色扮演的概念，您可以要求人工智能像史蒂夫·乔布斯这样的名人一样生成输出。本章强调在使用生成式人工智能模型时需要明确的方向和背景才能实现预期结果。此外，您还发现了评估 AI 模型性能和用于测量结果的各种方法的重要性，以及质量和令牌使用、成本和延迟之间的权衡。

In the next chapter, you will be introduced to text generation models. You will learn about the different types of foundation models and their capabilities, as well as their limitations. The chapter will also review the standard OpenAI offerings, as well as competitors and open source alternatives. By the end of the chapter, you will have a solid understanding of the history of text generation models and their relative strengths and weaknesses. This book will return to image generation prompting in Chapters [7](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch07.html#intro_image_07), [8](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch08.html#standard_image_08), and [9](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch09.html#advanced_image_09), so you should feel free to skip ahead if that is your immediate need. Get ready to dive deeper into the discipline of prompt engineering and expand your comfort working with AI.  
在下一章中，您将了解文本生成模型。您将了解不同类型的基础模型及其功能以及局限性。本章还将回顾标准 OpenAI 产品以及竞争对手和开源替代品。在本章结束时，您将对文本生成模型的历史及其相对优势和劣势有深入的了解。本书将在第 7、8 和 9 章中返回到图像生成提示，因此如果您迫切需要的话，可以随意跳过。准备好深入研究即时工程学科，并提高您使用人工智能的舒适度。
    
 

#   [2. Introduction To Large Language Models For Text Generation](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch02.html)

# Chapter 2. Introduction to Large Language Models for Text Generation  
第 2 章。用于文本生成的大型语言模型简介

In artificial intelligence, a recent focus has been the evolution of large language models. Unlike their less-flexible predecessors, LLMs are capable of handling and learning from a much larger volume of data, resulting in the emergent capability of producing text that closely resembles human language output. These models have generalized across diverse applications, from writing content to automating software development and enabling real-time interactive chatbot experiences.  
在人工智能领域，最近的一个焦点是大型语言模型的演变。与不太灵活的前辈不同，LLMs 能够处理和学习大量数据，从而产生与人类语言输出非常相似的文本的紧急能力。这些模型已经推广到各种应用程序中，从编写内容到自动化软件开发以及实现实时交互式聊天机器人体验。

# What Are Text Generation Models?  
什么是文本生成模型？

Text generation models utilize advanced algorithms to understand the meaning in text and produce outputs that are often indistinguishable from human work. If you’ve ever interacted with [ChatGPT](https://chat.openai.com/) or marveled at its ability to craft coherent and contextually relevant sentences, you’ve witnessed the power of an LLM in action.  
文本生成模型利用先进的算法来理解文本中的含义，并产生通常与人类工作无法区分的输出。如果您曾经与 ChatGPT 互动过，或者惊叹于它制作连贯且与上下文相关的句子的能力，那么您已经目睹了 LLM 在行动中的强大功能。

In natural language processing (NLP) and LLMs, the fundamental linguistic unit is a _token_. [Tokens](https://oreil.ly/3fOsM) can represent sentences, words, or even subwords such as a set of characters. A useful way to understand the size of text data is by looking at the number of tokens it comprises; for instance, a text of 100 tokens roughly equates to about 75 words. This comparison can be essential for managing the processing limits of LLMs as different models may have varying token capacities.  
在自然语言处理 （NLP） 和 LLMs 中，基本语言单位是标记。标记可以表示句子、单词，甚至是子词，例如一组字符。了解文本数据大小的一个有用方法是查看它包含的标记数量;例如，100 个标记的文本大致相当于大约 75 个单词。这种比较对于管理 LLMs 的处理限制至关重要，因为不同的模型可能具有不同的令牌容量。

_Tokenization_, the process of breaking down text into tokens, is a crucial step in preparing data for NLP tasks. Several methods can be used for tokenization, including [Byte-Pair Encoding (BPE)](https://oreil.ly/iSOp7), WordPiece, and SentencePiece. Each of these methods has its unique advantages and is suited to particular use cases. BPE is commonly used due to its efficiency in handling a wide range of vocabulary while keeping the number of tokens manageable.  
标记化是将文本分解为标记的过程，是为 NLP 任务准备数据的关键步骤。有几种方法可用于标记化，包括字节对编码 （BPE）、WordPiece 和 SentencePiece。这些方法中的每一种都有其独特的优势，适用于特定的用例。BPE 之所以被普遍使用，是因为它可以有效地处理各种词汇，同时保持令牌的数量可管理。

BPE begins by viewing a text as a series of individual characters. Over time, it combines characters that frequently appear together into single units, or tokens. To understand this better, consider the word _apple_. Initially, BPE might see it as _a_, _p_, _p_, _l_, and _e_. But after noticing that _p_ often comes after _a_ and before _l_ in the dataset, it might combine them and treat _appl_ as a single token in future instances.  
BPE 首先将文本视为一系列单个字符。随着时间的流逝，它将经常一起出现的字符组合成单个单位或标记。为了更好地理解这一点，请考虑苹果这个词。最初，BPE 可能将其视为 a、p、p、l 和 e。但是，在注意到 p 通常位于数据集中 a 之后和 l 之前之后，它可能会将它们组合在一起，并在将来的实例中将 appl 视为单个标记。

This approach helps LLMs recognize and generate words or phrases, even if they weren’t common in the training data, making the models more adaptable and versatile.  
这种方法有助于 LLMs 识别和生成单词或短语，即使它们在训练数据中并不常见，使模型更具适应性和通用性。

Understanding the workings of LLMs requires a grasp of the underlying mathematical principles that power these systems. Although the computations can be complex, we can simplify the core elements to provide an intuitive understanding of how these models operate. Particularly within a business context, the accuracy and reliability of LLMs are paramount.  
要了解 LLMs 的工作原理，需要掌握为这些系统提供动力的基本数学原理。尽管计算可能很复杂，但我们可以简化核心元素，以便直观地了解这些模型的运行方式。特别是在业务环境中，LLMs 的准确性和可靠性至关重要。

A significant part of achieving this reliability lies in the pretraining and fine-tuning phases of LLM development. Initially, models are trained on vast datasets during the pretraining phase, acquiring a broad understanding of language. Subsequently, in the fine-tuning phase, models are adapted for specific tasks, honing their capabilities to provide accurate and reliable outputs for specialized applications.  
实现这种可靠性的一个重要部分在于 LLM 开发的预训练和微调阶段。最初，模型在预训练阶段在大量数据集上进行训练，从而获得对语言的广泛理解。随后，在微调阶段，模型会针对特定任务进行调整，磨练其能力，为专业应用提供准确可靠的输出。

## Vector Representations: The Numerical Essence of Language  
向量表示：语言的数字本质

In the realm of NLP, words aren’t just alphabetic symbols. They can be tokenized and then represented in a numerical form, known as _vectors_. These vectors are multi-dimensional arrays of numbers that capture the semantic and syntactic relations:  
在NLP领域，单词不仅仅是字母符号。它们可以被标记化，然后以数字形式表示，称为向量。这些向量是捕获语义和句法关系的多维数字数组：

𝑤→𝐯=[𝑣1,𝑣2,...,𝑣𝑛]

Creating word vectors, also known as _word embeddings_, relies on intricate patterns within language. During an intensive training phase, models are designed to identify and learn these patterns, ensuring that words with similar meanings are mapped close to one another in a high-dimensional space ([Figure 2-1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch02.html#figure-2-1)).  
创建词向量（也称为词嵌入）依赖于语言中复杂的模式。在强化训练阶段，模型被设计来识别和学习这些模式，确保具有相似含义的单词在高维空间中彼此靠近（图 2-1）。

![Word Embeddings](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0201.png)

###### Figure 2-1. Semantic proximity of word vectors within a word embedding space  
图 2-1。词嵌入空间中词向量的语义接近度

The beauty of this approach is its ability to capture nuanced relationships between words and calculate their distance. When we examine word embeddings, it becomes evident that words with similar or related meanings like _virtue_ and _moral_ or _walked_ and _walking_ are situated near each other. This spatial closeness in the embedding space becomes a powerful tool in various NLP tasks, enabling models to understand context, semantics, and the intricate web of relationships that form language.  
这种方法的美妙之处在于它能够捕捉单词之间的细微关系并计算它们的距离。当我们检查单词嵌入时，很明显，具有相似或相关含义的单词，如美德和道德或步行和行走，彼此靠近。嵌入空间中的这种空间紧密性成为各种 NLP 任务中的强大工具，使模型能够理解上下文、语义和形成语言的错综复杂的关系网络。

## Transformer Architecture: Orchestrating Contextual Relationships  
Transformer 架构：编排上下文关系

Before we go deep into the mechanics of transformer architectures, let’s build a foundational understanding. In simple terms, when we have a sentence, say, _The cat sat on the mat_, each word in this sentence gets converted into its numerical vector representation. So, _cat_ might become a series of numbers, as does _sat_, _on_, and _mat_.  
在我们深入研究变压器架构的机制之前，让我们先建立一个基本的理解。简单来说，当我们有一个句子时，比如说，猫坐在垫子上，这句话中的每个单词都会被转换为其数字向量表示。因此，cat 可能会变成一系列数字，就像 sat、on 和 mat 一样。

As you’ll explore in detail later in this chapter, the transformer architecture takes these word vectors and understands their relationships—both in structure (syntax) and meaning (semantics). There are many types of transformers; [Figure 2-2](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch02.html#figure-2-2) showcases both BERT and GPT’s architecture. Additionally, a transformer doesn’t just see words in isolation; it looks at _cat_ and knows it’s related to _sat_ and _mat_ in a specific way in this sentence.  
正如您将在本章后面详细探讨的那样，Transformer 架构采用这些词向量并理解它们之间的关系——包括结构（语法）和含义（语义）。变压器的种类很多;图 2-2 展示了 BERT 和 GPT 的架构。此外，转换器不仅孤立地看待单词;它看着猫，知道它在这句话中以特定的方式与 SAT 和 MAT 有关。

![BERT and GPT architecture](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0202.png)

###### Figure 2-2. BERT uses an encoder for input data, while GPT has a decoder for output  
图 2-2。BERT 使用编码器来输入数据，而 GPT 使用解码器来输出

When the transformer processes these vectors, it uses mathematical operations to understand the relationships between the words, thereby producing new vectors with rich, contextual information:  
当转换器处理这些向量时，它使用数学运算来理解单词之间的关系，从而生成具有丰富上下文信息的新向量：

𝐯𝑖'=Transformer(𝐯1,𝐯2,...,𝐯𝑚)

One of the remarkable features of transformers is their ability to comprehend the nuanced contextual meanings of words. The [self-attention](https://oreil.ly/xuovP) mechanism in transformers lets each word in a sentence look at all other words to understand its context better. Think of it like each word casting votes on the importance of other words for its meaning. By considering the entire sentence, transformers can more accurately determine the role and meaning of each word, making their _interpretations more contextually rich._  
变形金刚的一个显着特点是它们能够理解单词细微的上下文含义。Transformer 中的自注意力机制让句子中的每个单词都查看所有其他单词，以更好地理解其上下文。把它想象成每个单词都对其他单词的含义的重要性进行投票。通过考虑整个句子，转换器可以更准确地确定每个单词的作用和含义，使他们的解释更加上下文丰富。

## Probabilistic Text Generation: The Decision Mechanism  
概率文本生成：决策机制

After the transformer understands the context of the given text, it moves on to generating new text, guided by the concept of likelihood or probability. In mathematical terms, the model calculates how likely each possible next word is to follow the current sequence of words and picks the one that is most likely:  
在转换器理解给定文本的上下文后，它会在可能性或概率概念的指导下继续生成新文本。用数学术语来说，该模型计算每个可能的下一个单词遵循当前单词序列的可能性，并选择最有可能的单词：

𝑤next=argmax𝑃(𝑤|𝑤1,𝑤2,...,𝑤𝑚)

By repeating this process, as shown in [Figure 2-3](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch02.html#figure-2-3), the model generates a coherent and contextually relevant string of text as its output.  
通过重复此过程，如图 2-3 所示，模型会生成一个连贯且与上下文相关的文本字符串作为其输出。

![An illustrative overview of how text is generated using transformer models like GPT-4.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0203.png)

###### Figure 2-3. How text is generated using transformer models such as GPT-4  
图 2-3。如何使用 GPT-4 等转换器模型生成文本

The mechanisms driving LLMs are rooted in vector mathematics, linear transformations, and probabilistic models. While the under-the-hood operations are computationally intensive, the core concepts are built on these mathematical principles, offering a foundational understanding that bridges the gap between technical complexity and business applicability.  
驱动 LLMs 的机制植根于向量数学、线性变换和概率模型。虽然底层操作是计算密集型的，但核心概念是建立在这些数学原理之上的，提供了一种基本的理解，弥合了技术复杂性和业务适用性之间的差距。

# Historical Underpinnings: The Rise of Transformer Architectures  
历史基础：变压器架构的兴起

Language models like ChatGPT (the _GPT_ stands for _generative pretrained transformer_) didn’t magically emerge. They’re the culmination of years of progress in the field of NLP, with particular acceleration since the late 2010s. At the heart of this advancement is the introduction of transformer architectures, which were detailed in the groundbreaking paper [“Attention Is All You Need”](https://oreil.ly/6NNbg) by the Google Brain team.  
像 ChatGPT（GPT 代表生成式预训练转换器）这样的语言模型并没有神奇地出现。它们是 NLP 领域多年进步的结晶，自 2010 年代后期以来尤其加速。这一进步的核心是 transformer 架构的引入，Google Brain 团队在开创性的论文“Attention Is All You Need”中对此进行了详细介绍。

The real breakthrough of transformer architectures was the concept of _attention_. Traditional models processed text sequentially, which limited their understanding of language structure especially over long distances of text. Attention transformed this by allowing models to directly relate distant words to one another irrespective of their positions in the text. This was a groundbreaking proposition. It meant that words and their context didn’t have to move through the entire model to affect each other. This not only significantly improved the models’ text comprehension but also made them much more efficient.  
变压器架构的真正突破是注意力的概念。传统模型按顺序处理文本，这限制了他们对语言结构的理解，尤其是在长距离文本上。注意力改变了这一点，它允许模型直接将遥远的单词相互关联，而不管它们在文本中的位置如何。这是一个开创性的主张。这意味着单词及其上下文不必在整个模型中移动以相互影响。这不仅显著提高了模型的文本理解能力，而且提高了效率。

This attention mechanism played a vital role in expanding the models’ capacity to detect long-range dependencies in text. This was crucial for generating outputs that were not just contextually accurate and fluent, but also coherent over longer stretches.  
这种注意力机制在扩展模型检测文本中长程依赖关系的能力方面发挥了至关重要的作用。这对于生成输出至关重要，这些输出不仅在上下文中准确和流畅，而且在较长时间内具有连贯性。

According to AI pioneer and educator [Andrew Ng](https://oreil.ly/JQd53), much of the early NLP research, including the fundamental work on transformers, received significant funding from United States military intelligence agencies. Their keen interest in tools like machine translation and speech recognition, primarily for intelligence purposes, inadvertently paved the way for developments that transcended just translation.  
根据人工智能先驱和教育家吴恩达（Andrew Ng）的说法，许多早期的NLP研究，包括关于变压器的基础工作，都得到了美国军事情报机构的大量资助。他们对机器翻译和语音识别等工具的浓厚兴趣，主要用于智能目的，无意中为超越翻译的发展铺平了道路。

Training LLMs requires extensive computational resources. These models are fed with vast amounts of data, ranging from terabytes to petabytes, including internet content, academic papers, books, and more niche datasets tailored for specific purposes. It’s important to note, however, that the data used to train LLMs can carry _inherent biases from their sources_. Thus, users should exercise caution and ideally employ human oversight when leveraging these models, ensuring responsible and ethical AI applications.  
训练 LLMs 需要大量的计算资源。这些模型提供了大量数据，从 TB 到 PB 不等，包括互联网内容、学术论文、书籍以及为特定目的量身定制的更多利基数据集。然而，需要注意的是，用于训练 LLMs 的数据可能带有来自其来源的固有偏见。因此，用户在利用这些模型时应谨慎行事，最好采用人工监督，确保负责任和合乎道德的人工智能应用程序。

OpenAI’s GPT-4, for example, boasts an estimated [1.7 trillion parameters](https://oreil.ly/pZvMo), which is equivalent to an Excel spreadsheet that stretches across thirty thousand soccer fields. _Parameters_ in the context of neural networks are the weights and biases adjusted throughout the training process, allowing the model to represent and generate complex patterns based on the data it’s trained on. The training cost for GPT-4 was estimated to be in the order of [$63 million](https://oreil.ly/_NAq5), and the training data would fill about [650 kilometers of bookshelves full of books](https://oreil.ly/D7jL5).  
例如，OpenAI 的 GPT-4 估计拥有 1.7 万亿个参数，相当于一个横跨三万个足球场的 Excel 电子表格。神经网络上下文中的参数是在整个训练过程中调整的权重和偏差，允许模型根据其训练的数据表示和生成复杂的模式。GPT-4 的训练成本估计约为 6300 万美元，训练数据将填满大约 650 公里的书架。

To meet these requirements, major technological companies such as Microsoft, Meta, and Google have invested heavily, making LLM development a high-stakes endeavor.  
为了满足这些要求，Microsoft、Meta 和 Google 等主要科技公司投入了大量资金，使 LLM 开发成为一项高风险的工作。

The rise of LLMs has provided an increased demand for the hardware industry, particularly companies specializing in graphics processing units (GPUs). NVIDIA, for instance, has become almost synonymous with high-performance GPUs that are essential for training LLMs.  
LLMs 的兴起为硬件行业提供了更大的需求，尤其是专门从事图形处理单元 （GPU） 的公司。例如，NVIDIA 几乎已成为高性能 GPU 的代名词，而高性能 GPU 对于训练 LLMs 至关重要。

The demand for powerful, efficient GPUs has skyrocketed as companies strive to build ever-larger and more complex models. It’s not just the raw computational power that’s sought after. GPUs also need to be fine-tuned for tasks endemic to machine learning, like tensor operations. _Tensors_, in a machine learning context, are multidimensional arrays of data, and operations on them are foundational to neural network computations. This emphasis on specialized capabilities has given rise to tailored hardware such as NVIDIA’s H100 Tensor Core GPUs, explicitly crafted to expedite machine learning workloads.  
随着公司努力构建更大、更复杂的模型，对强大、高效的 GPU 的需求猛增。人们追捧的不仅仅是原始的计算能力。GPU 还需要针对机器学习特有的任务进行微调，例如张量操作。在机器学习环境中，张量是多维数据数组，对它们的操作是神经网络计算的基础。这种对专业功能的强调催生了量身定制的硬件，例如 NVIDIA 的 H100 Tensor Core GPU，这些硬件专为加快机器学习工作负载而设计。

Furthermore, the overwhelming demand often outstrips the supply of these top-tier GPUs, sending prices on an upward trajectory. This supply-demand interplay has transformed the GPU market into a fiercely competitive and profitable arena. Here, an eclectic clientele, ranging from tech behemoths to academic researchers, scramble to procure the most advanced hardware.  
此外，压倒性的需求往往超过这些顶级 GPU 的供应，使价格走上上涨轨道。这种供需相互作用已将 GPU 市场转变为一个竞争激烈且有利可图的舞台。在这里，从科技巨头到学术研究人员，不拘一格的客户争先恐后地采购最先进的硬件。

This surge in demand has sparked a wave of innovation beyond just GPUs. Companies are now focusing on creating dedicated AI hardware, such as Google’s Tensor Processing Units (TPUs), to cater to the growing computational needs of AI models.  
这种需求的激增引发了一波创新浪潮，而不仅仅是 GPU。公司现在正专注于创建专用的人工智能硬件，例如谷歌的张量处理单元（TPU），以满足人工智能模型日益增长的计算需求。

This evolving landscape underscores not just the symbiotic ties between software and hardware in the AI sphere but also spotlights the ripple effect of the LLM _gold rush_. It’s steering innovations and funneling investments into various sectors, especially those offering the fundamental components for crafting these models.  
这种不断发展的格局不仅强调了人工智能领域软件和硬件之间的共生关系，还凸显了LLM淘金热的连锁反应。它正在引导创新并将投资汇集到各个领域，尤其是那些为制作这些模型提供基本组件的行业。

# OpenAI’s Generative Pretrained Transformers  
OpenAI 的生成式预训练转换器

Founded with a mission to ensure that artificial general intelligence benefits all of humanity, [OpenAI](https://openai.com/) has recently been at the forefront of the AI revolution. One of their most groundbreaking contributions has been the GPT series of models, which have substantially redefined the boundaries of what LLMs can achieve.  
OpenAI 成立的使命是确保通用人工智能造福全人类，最近一直处于人工智能革命的最前沿。他们最具开创性的贡献之一是 GPT 系列模型，它们从根本上重新定义了 LLMs 可以实现的边界。

The original GPT model by OpenAI was more than a mere research output; it was a compelling demonstration of the potential of transformer-based architectures. This model showcased the initial steps toward making machines understand and generate human-like language, laying the foundation for future advancements.  
OpenAI 最初的 GPT 模型不仅仅是一项研究成果;这是对基于Transformer的架构潜力的有力证明。该模型展示了使机器理解和生成类似人类语言的初步步骤，为未来的进步奠定了基础。

The unveiling of GPT-2 was met with both anticipation and caution. Recognizing the model’s powerful capabilities, OpenAI initially hesitated in releasing it due to concerns about its potential misuse. Such was the might of GPT-2 that ethical concerns took center stage, which might look quaint compared to the power of today’s models. However, when OpenAI decided to release the project as [open-source](https://oreil.ly/evOQE), it didn’t just mean making the code public. It allowed businesses and researchers to use these pretrained models as building blocks, incorporating AI into their applications without starting from scratch. This move democratized access to high-level natural language processing capabilities, spurring innovation across various domains.  
GPT-2 的揭幕既令人期待，也令人谨慎。认识到该模型的强大功能，OpenAI 最初对发布它犹豫不决，因为担心它可能被滥用。GPT-2 的威力如此之大，以至于道德问题占据了中心位置，与当今模型的力量相比，这可能看起来很古怪。然而，当 OpenAI 决定将该项目作为开源发布时，它并不仅仅意味着公开代码。它允许企业和研究人员使用这些预训练模型作为构建块，将人工智能整合到他们的应用程序中，而无需从头开始。此举使对高级自然语言处理能力的访问民主化，刺激了各个领域的创新。

After GPT-2, OpenAI decided to focus on releasing paid, closed-source models. GPT-3’s arrival marked a monumental stride in the progression of LLMs. It garnered significant media attention, not just for its technical prowess but also for the societal implications of its capabilities. This model could produce text so convincing that it often became indistinguishable from human-written content. From crafting intricate pieces of literature to churning out operational code snippets, GPT-3 exemplified the seemingly boundless potential of AI.  
在 GPT-2 之后，OpenAI 决定专注于发布付费的闭源模型。GPT-3 的到来标志着 LLMs 的进步迈出了巨大的一步。它引起了媒体的广泛关注，不仅因为它的技术实力，还因为它的能力对社会的影响。这种模型可以产生如此令人信服的文本，以至于它通常与人类编写的内容无法区分。从制作错综复杂的文献到制作可操作的代码片段，GPT-3 体现了 AI 看似无限的潜力。

## GPT-3.5-turbo and ChatGPT  
GPT-3.5-turbo 和 ChatGPT

Bolstered by Microsoft’s significant investment in their company, OpenAI introduced GPT-3.5-turbo, an optimized version of its already exceptional predecessor. Following a [$1 billion injection](https://oreil.ly/1C8qm) from Microsoft in 2019, which later increased to a hefty $13 billion for a 49% stake in OpenAI’s for-profit arm, OpenAI used these resources to develop GPT-3.5-turbo, which offered improved efficiency and affordability, effectively making LLMs more accessible for a broader range of use cases.  
在 Microsoft 对其公司的重大投资的支持下，OpenAI 推出了 GPT-3.5-turbo，这是其已经非常出色的前身的优化版本。在 Microsoft 于 2019 年注资 10 亿美元后，OpenAI 的营利性部门 49% 的股份增加到 130 亿美元，OpenAI 利用这些资源开发了 GPT-3.5-turbo，它提供了更高的效率和可负担性，有效地使 LLMs 更容易用于更广泛的用例。

OpenAI wanted to gather more world feedback for fine-tuning, and so [ChatGPT](https://chat.openai.com/) was born. Unlike its general-purpose siblings, [ChatGPT was fine-tuned](https://oreil.ly/6ib-Q) to excel in conversational contexts, enabling a dialogue between humans and machines that felt natural and meaningful.  
OpenAI 希望收集更多世界反馈以进行微调，因此 ChatGPT 诞生了。与通用的兄弟姐妹不同，ChatGPT 经过微调，在对话环境中表现出色，使人与机器之间的对话变得自然而有意义。

[Figure 2-4](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch02.html#figure-2-4) shows the training process for ChatGPT, which involves three main steps:  
ChatGPT 的训练过程如图 2-4 所示，主要分为 3 个步骤：

Collection of demonstration data  
收集演示数据

In this step, human labelers provide examples of the desired model behavior on a distribution of prompts. The labelers are trained on the project and follow specific instructions to annotate the prompts accurately.  
在此步骤中，人工标记器在提示分布上提供所需模型行为的示例。贴标员接受过该项目的培训，并按照特定说明准确注释提示。

Training a supervised policy  
培训受监督的策略

The demonstration data collected in the previous step is used to fine-tune a pretrained GPT-3 model using supervised learning. In supervised learning, models are trained on a labeled dataset where the correct answers are provided. This step helps the model to learn to follow the given instructions and produce outputs that align with the desired behavior.  
上一步中收集的演示数据用于使用监督学习微调预训练的 GPT-3 模型。在监督学习中，模型在标记的数据集上进行训练，其中提供了正确的答案。此步骤可帮助模型学习遵循给定的指令并生成与所需行为一致的输出。

Collection of comparison data and reinforcement learning  
比较数据的收集和强化学习

In this step, a dataset of model outputs is collected, and human labelers rank the outputs based on their preference. A reward model is then trained to predict which outputs the labelers would prefer. Finally, reinforcement learning techniques, specifically the Proximal Policy Optimization (PPO) algorithm, are used to optimize the supervised policy to maximize the reward from the reward model.  
在此步骤中，将收集模型输出的数据集，人工标记人员根据他们的偏好对输出进行排名。然后训练奖励模型，以预测标记者更喜欢哪些输出。最后，使用强化学习技术，特别是近端策略优化（PPO）算法，对监督策略进行优化，以最大化奖励模型的奖励。

This training process allows the ChatGPT model to align its behavior with human intent. The use of reinforcement learning with human feedback helped create a model that is more helpful, honest, and safe compared to the pretrained GPT-3 model.  
这个训练过程允许 ChatGPT 模型将其行为与人类意图保持一致。与预训练的 GPT-3 模型相比，使用强化学习和人类反馈有助于创建一个更有帮助、更诚实、更安全的模型。

![ChatGPT Fine Tuning Approach](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0204.png)

###### Figure 2-4. The fine-tuning process for ChatGPT  
图 2-4。ChatGPT 的微调过程

According to a [UBS study](https://oreil.ly/2Ivq2), by January 2023 ChatGPT set a new benchmark, amassing 100 million active users and becoming the fastest-growing consumer application in internet history. ChatGPT is now a go-to for customer service, virtual assistance, and numerous other applications that require the finesse of human-like conversation.  
根据瑞银的一项研究，到 2023 年 1 月，ChatGPT 树立了新的标杆，积累了 1 亿活跃用户，成为互联网历史上增长最快的消费者应用程序。ChatGPT 现在是客户服务、虚拟协助和许多其他需要类似人类对话技巧的应用程序的首选。

# GPT-4 GPT-4的

In 2024, OpenAI released GPT-4, which excels in understanding complex queries and generating contextually relevant and coherent text. For example, GPT-4 scored in the 90th percentile of the bar exam with a score of 298 out of 400. Currently, GPT-3.5-turbo is free to use in ChatGPT, but GPT-4 requires a [monthly payment](https://oreil.ly/UOEBM).  
2024 年，OpenAI 发布了 GPT-4，它擅长理解复杂的查询和生成上下文相关且连贯的文本。例如，GPT-4 在律师考试的第 90 个百分位得分为 298 分（满分 400 分）。目前，GPT-3.5-turbo 可以在 ChatGPT 中免费使用，但 GPT-4 需要按月付费。

GPT-4 uses a [mixture-of-experts approach](https://oreil.ly/v45LZ); it goes beyond relying on a single model’s inference to produce even more accurate and insightful results.  
GPT-4 采用专家混合方法;它超越了依赖单个模型的推理来产生更准确、更有洞察力的结果。

On May 13, 2024, OpenAI introduced [GPT-4o](https://oreil.ly/4ttmq), an advanced model capable of processing and reasoning across text, audio, and vision inputs in real time. This model offers enhanced performance, particularly in vision and audio understanding; it is also faster and more cost-effective than its predecessors due to its ability to process all three modalities in one neural network.  
2024 年 5 月 13 日，OpenAI 推出了 GPT-4o，这是一种能够实时处理和推理文本、音频和视觉输入的高级模型。该模型提供了增强的性能，特别是在视觉和音频理解方面;由于它能够在一个神经网络中处理所有三种模式，因此它也比其前辈更快、更具成本效益。

# Google’s Gemini 谷歌的双子座

After Google lost search market share due to ChatGPT usage, it initially released Bard on March 21, 2023. Bard was a bit [rough around the edges](https://oreil.ly/Sj24h) and definitely didn’t initially have the same high-quality LLM responses that ChatGPT offered ([Figure 2-5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch02.html#figure-2-5)).  
在谷歌因使用 ChatGPT 而失去搜索市场份额后，它最初于 2023 年 3 月 21 日发布了 Bard。Bard 的边缘有点粗糙，最初肯定没有 ChatGPT 提供的高质量 LLM 响应（图 2-5）。

Google has kept adding extra features over time including code generation, visual AI, real-time search, and voice into Bard, bringing it closer to ChatGPT in terms of quality.  
随着时间的推移，谷歌一直在向 Bard 添加额外的功能，包括代码生成、视觉 AI、实时搜索和语音，使其在质量方面更接近 ChatGPT。

On March 14, 2023, Google released [PaLM API](https://oreil.ly/EbI8-), allowing developers to access it on Google Cloud Platform. In April 2023, Amazon Web Services (AWS) released similar services such as [Amazon Bedrock](https://oreil.ly/4fNQX) and [Amazon’s Titan FMs](https://oreil.ly/FJ-7D). Google [rebranded Bard to Gemini](https://oreil.ly/EO42O) for their v1.5 release in February 2024 and started to get results similar to GPT-4.  
2023 年 3 月 14 日，Google 发布了 PaLM API，允许开发者在 Google Cloud Platform 上访问它。2023 年 4 月，亚马逊网络服务 （AWS） 发布了类似的服务，例如 Amazon Bedrock 和亚马逊的 Titan FM。 谷歌在 2024 年 2 月的 v1.5 版本中将 Bard 更名为 Gemini，并开始获得类似于 GPT-4 的结果。

![Google's bard which is a similar application to ChatGPT.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0205.png)

###### Figure 2-5. Bard hallucinating results about the James Webb Space Telescope  
图 2-5。吟游诗人关于詹姆斯·韦伯太空望远镜的幻觉结果

Also, Google released two smaller [open source models](https://oreil.ly/LWIwv) based on the same architecture as Gemini. OpenAI is finally no longer the only obvious option for software engineers to integrate state-of-the-art LLMs into their applications.  
此外，谷歌还发布了两个较小的开源模型，基于与 Gemini 相同的架构。OpenAI 终于不再是软件工程师将最先进的 LLMs 集成到他们的应用程序中的唯一明显选择。

# Meta’s Llama and Open Source  
Meta 的 Llama 和开源

Meta’s approach to language models differs significantly from other competitors in the industry. By sequentially releasing open source models [Llama](https://oreil.ly/LroPn), [Llama 2](https://oreil.ly/NeZLw) and [Llama 3](https://oreil.ly/Vwlo-), Meta aims to foster a more inclusive and collaborative AI development ecosystem.  
Meta 的语言模型方法与业内其他竞争对手有很大不同。Meta 通过依次发布开源模型 Llama、Llama 2 和 Llama 3，旨在打造一个更具包容性和协作性的 AI 开发生态系统。

The open source nature of Llama 2 and Llama 3 has significant implications for the broader tech industry, especially for large enterprises. The transparency and collaborative ethos encourage rapid innovation, as problems and vulnerabilities can be quickly identified and addressed by the global developer community. As these models become more robust and secure, large corporations can adopt them with increased confidence.  
Llama 2 和 Llama 3 的开源性质对更广泛的科技行业具有重大影响，尤其是对大型企业而言。透明度和协作精神鼓励快速创新，因为全球开发者社区可以快速识别和解决问题和漏洞。随着这些模型变得更加强大和安全，大公司可以更有信心地采用它们。

Meta’s open source strategy not only democratizes access to state-of-the-art AI technologies but also has the potential to make a meaningful impact across the industry. By setting the stage for a collaborative, transparent, and decentralized development process, Llama 2 and Llama 3 are pioneering models that could very well define the future of generative AI. The models are available in 7, 8 and 70 billion parameter versions on AWS, Google Cloud, Hugging Face, and other platforms.  
Meta 的开源战略不仅使获得最先进的 AI 技术民主化，而且还有可能对整个行业产生有意义的影响。Llama 2 和 Llama 3 为协作、透明和去中心化的开发过程奠定了基础，是可以很好地定义生成式 AI 未来的开创性模型。这些模型在 AWS、Google Cloud、Hugging Face 和其他平台上提供 7、8 和 700 亿参数版本。

The open source nature of these models presents a double-edged sword. On one hand, it levels the playing field. This means that even smaller developers have the opportunity to contribute to innovation, improving and applying open source models to practical business applications. This kind of decentralized innovation could lead to breakthroughs that might not occur within the walled gardens of a single organization, enhancing the models’ capabilities and applications.  
这些模型的开源性质是一把双刃剑。一方面，它创造了公平的竞争环境。这意味着即使是较小的开发人员也有机会为创新做出贡献，改进开源模型并将其应用于实际的业务应用程序。这种去中心化的创新可能会带来突破，而这些突破可能不会发生在单个组织的围墙花园中，从而增强模型的能力和应用。

However, the same openness that makes this possible also poses potential risks, as it could allow malicious actors to exploit this technology for detrimental ends. This indeed is a concern that organizations like OpenAI share, suggesting that some degree of control and restriction can actually serve to mitigate the dangerous applications of these powerful tools.  
然而，使这成为可能的开放性也带来了潜在的风险，因为它可能允许恶意行为者利用这项技术达到有害目的。这确实是OpenAI等组织共同关注的问题，这表明一定程度的控制和限制实际上可以减轻这些强大工具的危险应用。

# Leveraging Quantization and LoRA  
利用量化和 LoRA

One of the game-changing aspects of these open source models is the potential for [quantization](https://oreil.ly/bkWXk) and the use of [LoRA](https://oreil.ly/zORsB) (low-rank approximations). These techniques allow developers to fit the models into smaller hardware footprints. Quantization helps to reduce the numerical precision of the model’s parameters, thereby shrinking the overall size of the model without a significant loss in performance. Meanwhile, LoRA assists in optimizing the network’s architecture, making it more efficient to run on consumer-grade hardware.  
这些开源模型改变游戏规则的方面之一是量化和 LoRA（低秩近似）的潜力。这些技术使开发人员能够将模型拟合到更小的硬件占用空间中。量化有助于降低模型参数的数值精度，从而缩小模型的整体大小，而不会显著降低性能。同时，LoRA有助于优化网络架构，使其在消费级硬件上运行效率更高。

Such optimizations make fine-tuning these LLMs increasingly feasible on consumer hardware. This is a critical development because it allows for greater experimentation and adaptability. No longer confined to high-powered data centers, individual developers, small businesses, and start-ups can now work on these models in more resource-constrained environments.  
这种优化使得在消费类硬件上微调这些 LLMs 变得越来越可行。这是一个关键的发展，因为它允许更大的实验和适应性。个人开发人员、小型企业和初创企业不再局限于高性能数据中心，现在可以在资源更受限的环境中使用这些模型。

# Mistral 米斯特拉尔

Mistral 7B, a brainchild of French start-up [Mistral AI](https://mistral.ai/), emerges as a powerhouse in the generative AI domain, with its 7.3 billion parameters making a significant impact. This model is not just about size; it’s about efficiency and capability, promising a bright future for open source large language models and their applicability across a myriad of use cases. The key to its efficiency is the implementation of sliding window attention, a technique released under a permissive Apache open source license. Many AI engineers have fine-tuned on top of this model as a base, including the impressive [Zephr 7b beta](https://oreil.ly/Lg6_r) model. There is also [Mixtral 8x7b](https://oreil.ly/itsJG), a mixture of experts model (similar to the architecture of GPT-4), which achieves results similar to GPT-3.5-turbo.  
Mistral 7B 是法国初创公司 Mistral AI 的心血结晶，凭借其 73 亿个参数产生了重大影响，成为生成式 AI 领域的强者。这个模型不仅仅是尺寸;它关乎效率和能力，为开源大型语言模型及其在无数用例中的适用性带来了光明的未来。其效率的关键是实现滑动窗口注意力，这是一种在宽松的Apache开源许可下发布的技术。许多 AI 工程师都以此模型为基础进行了微调，包括令人印象深刻的 Zephr 7b 测试版。还有 Mixtral 8x7b，一个混合的专家模型（类似于 GPT-4 的架构），它实现了类似于 GPT-3.5-turbo 的结果。

For a more detailed and up-to-date comparison of open source models and their performance metrics, visit the Chatbot [Arena Leaderboard](https://oreil.ly/ttiji) hosted by Hugging Face.  
有关开源模型及其性能指标的更详细和最新比较，请访问由 Hugging Face 主办的 Chatbot Arena 排行榜。

# Anthropic: Claude Anthropic： 克劳德

Released on July 11, 2023, [Claude 2](https://claude.ai/login) is setting itself apart from other prominent LLMs such as ChatGPT and LLaMA, with its pioneering [Constitutional AI](https://oreil.ly/Tim9W) approach to AI safety and alignment—training the model using a list of rules or values. A notable enhancement in Claude 2 was its expanded context window of 100,000 tokens, as well as the ability to upload files. In the realm of generative AI, a _context window_ refers to the amount of text or data the model can actively consider or keep in mind when generating a response. With a larger context window, the model can understand and generate based on a broader context.  
Claude 2 于 2023 年 7 月 11 日发布，与 ChatGPT 和 LLaMA 等其他著名的 LLMs 区分开来，其开创性的 Constitutional AI 方法实现了 AI 安全和对齐——使用规则或值列表训练模型。Claude 2 的一个显着改进是其扩展的 100,000 个令牌的上下文窗口，以及上传文件的能力。在生成式 AI 领域，上下文窗口是指模型在生成响应时可以主动考虑或牢记的文本或数据量。使用更大的上下文窗口，模型可以根据更广泛的上下文进行理解和生成。

This advancement garnered significant enthusiasm from AI engineers, as it opened up avenues for new and more intricate use cases. For instance, Claude 2’s augmented ability to process more information at once makes it adept at summarizing extensive documents or sustaining in-depth conversations. The advantage was short-lived, as OpenAI released their 128K version of GPT-4 only [six months later](https://oreil.ly/BWxrn). However, the fierce competition between rivals is pushing the field forward.  
这一进步引起了人工智能工程师的极大热情，因为它为新的和更复杂的用例开辟了途径。例如，Claude 2 一次处理更多信息的能力增强，使其擅长总结大量文档或进行深入对话。这种优势是短暂的，因为 OpenAI 仅在六个月后发布了他们的 128K 版本的 GPT-4。然而，竞争对手之间的激烈竞争正在推动该领域向前发展。

The next generation of Claude included [Opus](https://oreil.ly/NH0jh), the first model to rival GPT-4 in terms of intelligence, as well as Haiku, a smaller model that is lightning-fast with the competitive price of $0.25 per million tokens (half the cost of GPT-3.5-turbo at the time).  
下一代 Claude 包括 Opus，这是第一个在智能方面与 GPT-4 相媲美的模型，以及 Haiku，这是一个较小的模型，速度快如闪电，每百万个代币的竞争价格为 0.25 美元（当时是 GPT-3.5-turbo 成本的一半）。

# GPT-4V(ision) GPT-4V（ision）

In a significant leap forward, on September 23, 2023, OpenAI expanded the capabilities of GPT-4 with the introduction of Vision, enabling users to instruct GPT-4 to analyze images alongside text. This innovation was also reflected in the update to ChatGPT’s interface, which now supports the inclusion of both images and text as user inputs. This development signifies a major trend toward _multimodal models_, which can seamlessly process and understand multiple types of data, such as images and text, within a single context.  
2023 年 9 月 23 日，OpenAI 通过引入 Vision 扩展了 GPT-4 的功能，使用户能够指示 GPT-4 分析图像和文本。这一创新也反映在 ChatGPT 界面的更新中，该界面现在支持将图像和文本作为用户输入。这一发展标志着多模态模型的主要趋势，它可以在单个上下文中无缝处理和理解多种类型的数据，例如图像和文本。

# Model Comparison 模型比较

The market for LLMs is dominated by OpenAI at the time of writing, with its state-of-the-art GPT-4 model widely considered to have a significant lead. The closest competitor is Anthropic, and there is widespread excitement at the potential of smaller open source models such as Llama and Mistral, particularly with respects to fine-tuning. Although commentators expect OpenAI to continue to deliver world-beating models in the future, as open source models get _good enough_ at more tasks, AI workloads may shift toward local fine-tuned models. With advances in model performance and quantization (methods for trading off accuracy versus size and compute cost), it may be possible to one day run LLMs on your mobile phone or other devices.  
在撰写本文时，LLMs 的市场由 OpenAI 主导，其最先进的 GPT-4 模型被广泛认为具有显着的领先优势。最接近的竞争对手是 Anthropic，人们对 Llama 和 Mistral 等小型开源模型的潜力普遍感到兴奋，尤其是在微调方面。尽管评论员预计 OpenAI 未来将继续提供世界一流的模型，但随着开源模型在更多任务中变得足够好，AI 工作负载可能会转向本地微调模型。随着模型性能和量化（权衡精度与大小和计算成本的方法）的进步，有朝一日有可能在手机或其他设备上运行LLMs。

For now, the best way to get a sense for what the models are good at is to run the same prompt across multiple models and compare the responses. One thing that regularly stands out in our work is that GPT-4 is much better at following instructions, as is demonstrated in the following example where it was the only model to respond in the right format, with names that matched the examples (starting with the letter _i_), as desired.  
目前，了解模型擅长什么的最好方法是在多个模型中运行相同的提示并比较响应。在我们的工作中经常突出的一件事是，GPT-4 在遵循指令方面要好得多，正如以下示例所示，它是唯一以正确格式响应的模型，其名称与示例匹配（以字母 i 开头），正如所希望的那样。

Input: 输入：

Brainstorm a list of product names for a shoe that fits any foot size,
in the style of Steve Jobs.

Return the results as a comma-separated list, in this format:
Product description: A shoe that fits any foot size
Product names: [list of three product names]

## Examples
Product description: A refrigerator that dispenses beer
Product names: iBarFridge, iFridgeBeer, iDrinkBeerFridge

Product description: A watch that can tell accurate time in space
Product names: iNaut, iSpace, iTime

Product description: A home milkshake maker
Product names: iShake, iSmoothie, iShake Mini

Output (GPT-4): 输出 （GPT-4）：

Product description: A shoe that fits any foot size
Product names: iFit, iShoe, iFlexible

Output (Claude 3): 输出 （Claude 3）：

Product description: A shoe that fits any foot size
Product names: iFit, iComfort, iSole

Output (Llama 3 70b):  
输出 （Llama 3 70b）：

Here is the list of product names for a shoe that fits any foot size,
in the style of Steve Jobs:

Product description: A shoe that fits any foot size Product names:
iFit, OneSize, iWalkFree

# Summary 总结

The journey of LLMs from their inception to their current advanced states is a tale of relentless innovation, collaboration, and intense competition. As these models continue to evolve, they are likely to become even more integral parts of our daily lives, changing the way we interact with technology and even with each other.  
LLMs 从成立到现在的先进状态，是一个不懈创新、协作和激烈竞争的故事。随着这些模型的不断发展，它们可能会成为我们日常生活中不可或缺的一部分，改变我们与技术甚至彼此互动的方式。

By understanding the historical context and capabilities of these models, you can better appreciate the tools at our disposal for various applications, from prompt engineering to the development of intelligent virtual agents. It’s important to note, however, that while these models offer expansive possibilities, data privacy remains a crucial concern. If these models use your data for retraining or fine-tuning, exercise caution and refrain from inputting sensitive information.  
通过了解这些模型的历史背景和功能，您可以更好地了解我们为各种应用程序提供的工具，从提示工程到智能虚拟代理的开发。然而，需要注意的是，虽然这些模型提供了广泛的可能性，但数据隐私仍然是一个关键问题。如果这些模型使用您的数据进行再训练或微调，请谨慎行事，不要输入敏感信息。

In the next chapter, you will learn all the basic prompt engineering techniques for working with text LLMs. You’ll learn the essential skills needed to get the most out of powerful language models like GPT-4. Exciting insights and practical methods await you as you unlock the true potential of generative AI.  
在下一章中，您将学习处理文本 LLMs 的所有基本提示工程技术。您将学习充分利用 GPT-4 等强大语言模型所需的基本技能。激动人心的见解和实用方法等待着您，为您释放生成式 AI 的真正潜力。

# [Chapter3. Standard Practices For Text Generation With ChatGPT](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html)第 3 章:使用 ChatGPT 生成文本的标准做法

Simple prompting techniques will help you to maximize the output and formats from LLMs. You’ll start by tailoring the prompts to explore all of the common practices used for text generation.  
> 
简单的提示技术将帮助您最大化 LLMs 的输出和格式。首先，您将定制提示，以探索用于文本生成的所有常见做法。

## Generating Lists 生成列表

Automatically generating lists is incredibly powerful and enables you to focus on higher-level tasks while GPT can automatically generate, refine, rerank, and de-duplicate lists on your behalf.  
> 
自动生成列表非常强大，使您能够专注于更高级别的任务，而 GPT 可以代表您自动生成、优化、重新排名和删除重复列表。

Input: 输入：

```python

Generate a list of Disney characters.

```

Output: 输出：

```python

Sure, here is a list of some popular Disney characters:

1. Mickey Mouse
2. Minnie Mouse
...
30. Bagheera (The Jungle Book)

    This will output: 这将输出：

```

GPT-4 is perfectly capable of providing a list of characters. However, there are some pitfalls with this approach:  
GPT-4 完全能够提供字符列表。但是，这种方法存在一些缺陷：

- ==*GPT has decided to provide 30 examples as a numbered list, separated by \n characters. However, if your downstream Python code was expecting to split on bullet points, then you’ll likely end up with undesirable results or a runtime error.==*  

    GPT 决定提供 30 个示例作为编号列表，以 `\n` 字符分隔。但是，如果您的下游 Python 代码期望在项目符号上拆分，那么您最终可能会得到不希望的结果或运行时错误。
    - GPT has provided preceding commentary; removing any preceding/succeeding commentary would make parsing the output easier.  
    GPT 提供了先前的评论;删除任何之前/后面的注释将使解析输出更容易。
- *==- *The list size wasn’t controlled and was left to the language model.==*  
    列表大小不受控制，留给语言模型。
    *==- Some of the characters have the name of their corresponding film within brackets—for example, Bagheera (The Jungle Book)—and others don’t. This makes names harder to extract because you would need to remove the movie titles.==*  
    有些角色在括号内有相应电影的名称，例如，Bagheera（《丛林之书》），而另一些则没有。这使得名称更难提取，因为您需要删除电影标题。
    
- ==*No filtering or selection has been applied to the LLM generation based on our desired result.==*  
    没有根据我们想要的结果对LLM一代应用任何过滤或选择。
    Following you’ll find an optimized prompt.  
下面你会发现一个优化的提示。
Input: 输入：

```python

Generate a bullet-point list of 5 male Disney characters.
Only include the name of the character for each line.
Never include the film for each Disney character.
Only return the Disney characters, never include any commentary.

Below is an example list:
- Aladdin
- Simba
- Beast
- Hercules
- Tarzan

```

Output: 输出：

```python
- Woody
- Buzz Lightyear
- Stitch
- Jack Sparrow
- Prince Charming

```

### PROVIDE EXAMPLES 举例说明

Simply rephrasing your prompt to include examples _(few-shot prompting)_ can greatly impact the desired output.  
简单地改写你的提示以包含示例（少量提示）可以极大地影响所需的输出。

By optimizing the prompt, you’ve achieved the following:  
通过优化提示，您已经实现了以下目标：
- Restricted the list to a fixed size of five  
    将列表限制为固定大小 5
    
- Generated only male characters  
    仅生成男性角色
    
- Correctly formatted the list with bullet points  
    使用项目符号正确设置列表格式
    
- Removed any preceding commentary  
    删除了之前的任何评论
    
    Simple lists are fine for most tasks; however, they are less structured, and for some tasks it’s beneficial to obtain nested data structures from a GPT-4 output.  
    
简单的列表适用于大多数任务;但是，它们的结构化程度较低，对于某些任务，从 GPT-4 输出中获取嵌套数据结构是有益的。

Three typical data structures include:  
三种典型的数据结构包括：

- Nested text data (hierarchical lists)  
    嵌套文本数据（分层列表）
    
- JSON 
    
- YAML

# Hierarchical List Generation  
分层列表生成

Hierarchical lists are useful for when your desired output is nested. A good example of this would be a detailed article structure.  
分层列表在嵌套所需输出时非常有用。一个很好的例子是详细的文章结构。
Input: 输入：

```python

Generate a hierarchical and incredibly detailed article outline on:

What are the benefits of data engineering.

See an example of the hierarchical structure below:

Article Title: What are the benefits of digital marketing?
- Introduction
    a. Explanation of digital marketing
    b. Importance of digital marketing in today's business world
- Increased Brand Awareness
    a. Definition of brand awareness
    b. How digital marketing helps in increasing brand awareness

```

Output: 输出：

```python

Article Title: What are the benefits of data engineering?
- Introduction
    a. Explanation of data engineering
    b. Importance of data engineering in today’s data-driven world

...(10 sections later)...
- Conclusion
    a. Importance of data engineering in the modern business world
    b. Future of data engineering and its impact on the data ecosystem

```

To generate an effective article outline in the preceding output, you’ve included two key phrases:  
若要在前面的输出中生成有效的文章大纲，请包含两个关键短语：
Hierarchical 层次

To suggest that the article outline needs to produce a nested structure.  
建议文章大纲需要产生嵌套结构。

Incredibly detailed 难以置信的细节

To guide the language model towards producing a larger output. Other words that you could include that have the same effect would be _very long_ or by specifying a large number of subheadings, _include at least 10 top-level headings_.  
引导语言模型产生更大的输出。您可以包含具有相同效果的其他单词会很长，或者通过指定大量副标题，至少包括 10 个顶级标题。

###### NOTE 注意

Asking a language model for a fixed number of items doesn’t guarantee the language model will produce the same length. For example, if you ask for 10 headings, you might receive only 8. Therefore, your code should either validate that 10 headings exist or be flexible to handle varying lengths from the LLM.  
向语言模型请求固定数量的项并不能保证语言模型将生成相同的长度。例如，如果您要求提供 10 个标题，您可能只收到 8 个。因此，您的代码应该验证是否存在 10 个标题，或者灵活地处理 LLM 的不同长度。

So you’ve successfully produced a hierarchical article outline, but how could you parse the string into structured data?  
因此，您已经成功地生成了分层文章大纲，但是如何将字符串解析为结构化数据？

Let’s explore [Example 3-1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#parsing_a_hierarchical_list_one) using Python, where you’ve previously made a successful API call against OpenAI’s GPT-4. Two regular expressions are used to extract the headings and subheadings from `openai_result`. The `re` module in Python is used for working with regular expressions.  
让我们使用 Python 探索示例 3-1，您之前已成功对 OpenAI 的 GPT-4 进行了 API 调用。使用两个正则表达式从 `openai_result` 中提取标题和副标题。Python 中的 `re` 模块用于处理正则表达式。

##### Example 3-1. [Parsing a hierarchical list](https://oreil.ly/A0otS)  
例 3-1.分析分层列表

```python

import re

# openai_result = generate_article_outline(prompt)

# Commented out to focus on a fake LLM response, see below:

openai_result = '''
- Introduction
    a. Explanation of data engineering
    b. Importance of data engineering in today’s data-driven world
- Efficient Data Management
    a. Definition of data management
    b. How data engineering helps in efficient data management
- Conclusion
    a. Importance of data engineering in the modern business world
    b. Future of data engineering and its impact on the data ecosystem
'''

# Regular expression patterns
heading_pattern = r'\* (.+)'
subheading_pattern = r'\s+[a-z]\. (.+)'

# Extract headings and subheadings
headings = re.findall(heading_pattern, openai_result)
subheadings = re.findall(subheading_pattern, openai_result)

# Print results
print("Headings:\n")
for heading in headings:
    print(f"* {heading}")

print("\nSubheadings:\n")
for subheading in subheadings:
    print(f"* {subheading}")

```

This code will output:  
此代码将输出：

```python

Headings:
- Introduction
- Efficient Data Management
- Conclusion

Subheadings:
- Explanation of data engineering
- Importance of data engineering in today’s data-driven world
- Definition of data management
- How data engineering helps in efficient data management
- Importance of data engineering in the modern business world
- Future of data engineering and its impact on the data ecosystem

```

The use of regular expressions allows for efficient pattern matching, making it possible to handle variations in the input text, such as the presence or absence of leading spaces or tabs. Let’s explore how these patterns work:  
使用正则表达式可以进行有效的模式匹配，从而可以处理输入文本中的变体，例如前导空格或制表符的存在与否。让我们来探讨一下这些模式是如何工作的：

```python

 `heading_pattern = r'\* (.+)'`

```

This pattern is designed to extract the main headings and consists of:  
此模式旨在提取主要标题，包括：
- `\*` matches the asterisk `(*)` symbol at the beginning of a heading. The backslash is used to escape the asterisk, as the asterisk has a special meaning in regular expressions (zero or more occurrences of the preceding character).  
    `\*` 与标题开头的星号 `(*)` 符号匹配。反斜杠用于转义星号，因为星号在正则表达式中具有特殊含义（前一个字符出现零次或多次）。
    
- A space character will match after the asterisk.  
    空格字符将在星号后匹配。
    
- `(.+)`: matches one or more characters, and the parentheses create a capturing group. The `.` is a wildcard that matches any character except a newline, and the `+` is a quantifier that means _one or more_ occurrences of the preceding element (the dot, in this case).  
    `(.+)` ：匹配一个或多个字符，括号内将创建一个捕获组。 `.` 是一个通配符，与除换行符以外的任何字符匹配， `+` 是一个量词，表示前一个元素（在本例中为点）的一次或多次出现。

By applying this pattern you can easily extract all of the main headings into a list without the asterisk.  
通过应用此模式，您可以轻松地将所有主要标题提取到不带星号的列表中。

```python

`subheading_pattern = r'\s+[a-z]\. (.+)`
<mark style="background: #FF5582A6;">```
The `subheading pattern` will match all of the subheadings within the `openai_result` string:  
`subheading pattern` 将匹配 `openai_result` 字符串中的所有副标题：

- `\s+` matches one or more whitespace characters (spaces, tabs, and so on). The `+` means _one or more_ occurrences of the preceding element (the `\s`, in this case).  
    `\s+` 匹配一个或多个空格字符（空格、制表符等）。 `+` 表示前一个元素的一个或多个出现（在本例中为 `\s` ）。
    
- `[a-z]` matches a single lowercase letter from _a_ to _z_.  
    `[a-z]` 匹配从 a 到 z 的单个小写字母。
    
- `\.` matches a period character. The backslash is used to escape the period, as it has a special meaning in regular expressions (matches any character except a newline).  
    `\.` 匹配句点字符。反斜杠用于转义句点，因为它在正则表达式中具有特殊含义（匹配除换行符以外的任何字符）。
    
- _A space character will match after the period.  
    句点后将匹配空格字符。_

- `(.+)` matches one or more characters, and the parentheses create a capturing group. The `.` is a wildcard that matches any character except a newline, and the `+` is a quantifier that means _one or more_ occurrences of the preceding element (the dot, in this case).  
    `(.+)` 匹配一个或多个字符，括号内将创建一个捕获组。 `.` 是一个通配符，与除换行符以外的任何字符匹配， `+` 是一个量词，表示前一个元素（在本例中为点）的一次或多次出现。</mark>
    

Additionally the `re.findall()` function is used to find all non-overlapping matches of the patterns in the input string and return them as a list. The extracted headings and subheadings are then printed.  
此外， `re.findall()` 函数用于查找输入字符串中模式的所有非重叠匹配项，并将它们作为列表返回。然后打印提取的标题和副标题。

So now you’re able to extract headings and subheadings from hierarchical article outlines; however, you can further refine the regular expressions so that each heading is associated with corresponding `subheadings`.  
因此，现在您可以从分层文章大纲中提取标题和副标题;但是，您可以进一步细化正则表达式，以便每个标题都与相应的 `subheadings` 相关联。
In [Example 3-2](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#parsing_a_hierarchical_list_two), the regex has been slightly modified so that each subheading is attached directly with its appropriate subheading.  
在示例 3-2 中，正则表达式稍作修改，以便每个子标题都直接附加其适当的子标题。

##### Example 3-2. [Parsing a hierarchical list into a Python dictionary](https://oreil.ly/LcMtv)  
例 3-2.将分层列表解析为 Python 字典

```python

import re

openai_result = """
- Introduction
  a. Explanation of data engineering
  b. Importance of data engineering in today’s data-driven world
- Efficient Data Management
    a. Definition of data management
    b. How data engineering helps in efficient data management
    c. Why data engineering is important for data management
- Conclusion
    a. Importance of data engineering in the modern business world
    b. Future of data engineering and its impact on the data ecosystem
"""

section_regex = re.compile(r"\* (.+)")
subsection_regex = re.compile(r"\s*([a-z]\..+)")

result_dict = {}
current_section = None

for line in openai_result.split("\n"):
    section_match = section_regex.match(line)
    subsection_match = subsection_regex.match(line)

    if section_match:
        current_section = section_match.group(1)
        result_dict[current_section] = []
    elif subsection_match and current_section is not None:
        result_dict[current_section].append(subsection_match.group(1))

print(result_dict)

```

This will output: 这将输出：

```python

{
    "Introduction": [
        "a. Explanation of data engineering",
        "b. Importance of data engineering in today’s data-driven world"
    ],
    "Efficient Data Management": [
        "a. Definition of data management",
        "b. How data engineering helps in efficient data management"
    ],
    "Conclusion": [
        "a. Importance of data engineering in the modern business world",
        "b. Future of data engineering and its impact on the data ecosystem"
    ]
}

```

The section title regex, `r'\* (.+)'`, matches an asterisk followed by a space and then one or more characters. The parentheses capture the text following the asterisk and space to be used later in the code.  
章节标题正则表达式 `r'\* (.+)'` 匹配星号后跟空格，然后是一个或多个字符。括号捕获星号后面的文本和稍后在代码中使用的空格。

The subsection regex, `r'\s*([a-z]\..+)'`, starts with `\s*`, which matches zero or more whitespace characters (spaces or tabs). This allows the regex to match subsections with or without leading spaces or tabs. The following part, `([a-z]\..+)`, matches a lowercase letter followed by a period and then one or more characters. The parentheses capture the entire matched subsection text for later use in the code.  
子部分正则表达式 `r'\s*([a-z]\..+)'` 以 `\s*` 开头，它匹配零个或多个空格字符（空格或制表符）。这允许正则表达式匹配带有或不带有前导空格或制表符的小节。以下部分 `([a-z]\..+)` 匹配一个小写字母，后跟句点，然后是一个或多个字符。括号捕获整个匹配的小节文本，以便以后在代码中使用。

The `for` loop iterates over each line in the input string, `openai_result`. Upon encountering a line that matches the section title regex, the loop sets the matched title as the current section and assigns an empty list as its value in the `result_dict` dictionary. When a line matches the subsection regex, the matched subsection text is appended to the list corresponding to the current section.  
`for` 循环遍历输入字符串 `openai_result` 中的每一行。当遇到与章节标题正则表达式匹配的行时，循环会将匹配的标题设置为当前章节，并在 `result_dict` 字典中分配一个空列表作为其值。当一行与小节正则表达式匹配时，匹配的小节文本将追加到与当前节对应的列表中。

Consequently, the loop processes the _input string line by line_, categorizes lines as section titles or subsections, and constructs the intended dictionary structure.  
因此，循环逐行处理输入字符串，将行分类为部分标题或子部分，并构造预期的字典结构。

# When to Avoid Using Regular Expressions  
何时避免使用正则表达式

As you work to extract more structured data from LLM responses, relying solely on regular expressions can make the control flow _become increasingly complicated._ However, there are other formats that can facilitate the parsing of structured data from LLM responses with ease. Two common formats are _.json_ and _.yml_ files.  
当您努力从 LLM 响应中提取更多结构化数据时，仅依赖正则表达式会使控制流变得越来越复杂。但是，还有其他格式可以方便轻松地解析来自 LLM 响应的结构化数据。两种常见的格式是 .json 和 .yml 文件。

# Generating JSON 生成 JSON

Let’s start by experimenting with some prompt design that will direct an LLM to return a JSON response.  
让我们先尝试一些提示设计，这些设计将指导 LLM 返回 JSON 响应。

Input: 输入：

Compose a very detailed article outline on "The benefits of learning code" with a
JSON payload structure that highlights key points.

Only return valid JSON.

Here is an example of the JSON structure:
{
    "Introduction": [
        "a. Explanation of data engineering",
        "b. Importance of data engineering in today’s data-driven world"],
    ...
    "Conclusion": [
        "a. Importance of data engineering in the modern business world",
        "b. Future of data engineering and its impact on the data ecosystem"]
}

Output: 输出：

{
    "Introduction": [
        "a. Overview of coding and programming languages",
        "b. Importance of coding in today's technology-driven world"],
    ...
    "Conclusion": [
        "a. Recap of the benefits of learning code",
        "b. The ongoing importance of coding skills in the modern world"]
}

# GIVE DIRECTION AND PROVIDE EXAMPLES  
给出方向并提供示例

Notice that in the preceding prompt, you’ve provided direction on the type of task, the format, and an example JSON output.  
请注意，在前面的提示中，您已经提供了有关任务类型、格式和示例 JSON 输出的说明。

Common errors that you’ll encounter when working with JSON involve invalid payloads, or the JSON being wrapped within triple backticks (```) , such as:  
使用 JSON 时会遇到的常见错误涉及无效的有效负载，或者 JSON 被包装在三重反引号 （'''） 中，例如：

Output: 输出：

Sure here's the JSON:

```json

{"Name": "John Smith"} # valid payload
{"Name": "John Smith", "some_key":} # invalid payload

```

Ideally you would like the model to respond like so:  
理想情况下，您希望模型的响应如下：

Output: 输出：

{"Name": "John Smith"}

This is important because with the first output, you’d have to split after `json` and then parse the exact part of the string that contained valid JSON. There are several points that are worth adding to your prompts to improve JSON parsing:  
这很重要，因为在第一个输出中，必须在 `json` 之后拆分，然后解析包含有效 JSON 的字符串的确切部分。有几点值得添加到您的提示中，以改进 JSON 解析：

You must follow the following principles:
- Only return valid JSON
- Never include backtick symbols such as: `
- The response will be parsed with json.loads(), therefore it must be valid JSON.

Now let’s examine how you can parse a [JSON output with Python](https://oreil.ly/MoJHn):  
现在让我们来看看如何使用 Python 解析 JSON 输出：

```

import

```

Well done, you’ve successfully parsed some JSON.  
干得好，你已经成功解析了一些JSON。

As showcased, structuring data from an LLM response is streamlined when requesting the response in valid JSON format. Compared to the previously demonstrated regular expression parsing, this method is less cumbersome and more straightforward.  
如图所示，当以有效的 JSON 格式请求响应时，从 LLM 响应构建数据的过程会简化。与前面演示的正则表达式解析相比，这种方法不那么繁琐，而且更直接。

So what could go wrong?  
那么会出什么问题呢？

- The language model accidentally adds extra text to the response such as `json output:` and your application logic only handles for valid JSON.  
    语言模型会意外地向响应添加额外的文本，例如 `json output:` ，并且应用程序逻辑仅处理有效的 JSON。
    
- The JSON produced isn’t valid and fails upon parsing (either due to the size or simply for not escaping certain characters).  
    生成的 JSON 无效，并且在解析时失败（由于大小或只是因为未转义某些字符）。
    

Later on you will examine strategies to gracefully handle for such edge cases.  
稍后，您将研究优雅地处理此类边缘情况的策略。

## YAML YAML公司

_.yml_ files are a structured data format that offer different benefits over _.json_:  
.yml 文件是一种结构化数据格式，与.json相比具有不同的优势：

No need to escape characters  
无需转义字符

YAML’s indentation pattern eliminates the need for braces, brackets, and commas to denote structure. This can lead to cleaner and less error-prone files, as there’s less risk of mismatched or misplaced punctuation.  
YAML 的缩进模式消除了使用大括号、括号和逗号来表示结构的需要。这可以使文件更干净、更不容易出错，因为标点符号不匹配或放错位置的风险较小。

Readability 可读性

YAML is designed to be human-readable, with a simpler syntax and structure compared to JSON. This makes it easier for you to create, read, and edit prompts, especially when dealing with complex or nested structures.  
YAML 被设计为人类可读的，与 JSON 相比，具有更简单的语法和结构。这使您可以更轻松地创建、阅读和编辑提示，尤其是在处理复杂或嵌套结构时。

Comments 评论

Unlike JSON, YAML supports comments, allowing you to add annotations or explanations to the prompts directly in the file. This can be extremely helpful when working in a team or when revisiting the prompts after some time, as it allows for better understanding and collaboration.  
与 JSON 不同，YAML 支持注释，允许您直接在文件中为提示添加注释或解释。这在团队中工作或一段时间后重新访问提示时非常有用，因为它可以更好地理解和协作。

Input: 输入：

- Below you'll find the current yaml schema.
- You can update the quantities based on a User Query.
- Filter the User Query based on the schema below, if it doesn't match and
there are no items left then return `"No Items"`.
- If there is a partial match, then return only the items that are
within the schema below:

# schema:
- item: Apple Slices
  quantity: 5
  unit: pieces
- item: Milk
  quantity: 1
  unit: gallon
- item: Bread
  quantity: 2
  unit: loaves
- item: Eggs
  quantity: 1
  unit: dozen

User Query: "5 apple slices, and 2 dozen eggs."

Given the schema below, please return only a valid .yml based on the User
Query.If there's no match, return `"No Items"`. Do not provide any
commentary or explanations.

Output: 输出：

- item: Apple Slices
  quantity: 5
  unit: pieces
- item: Eggs
  quantity: 2
  unit: dozen

Notice with the preceding example how an LLM is able to infer the correct _.yml_ format from the `User Query` string.  
请注意前面的示例，LLM 如何能够从 `User Query` 字符串推断出正确的.yml格式。

Additionally, you’ve given the LLM an opportunity to either:  
此外，您还为 LLM 提供了以下任一机会：

- Return a valid _.yml_ response  
    返回有效的.yml响应
    
- Return a filtered _.yml_ response  
    返回筛选的.yml响应
    

If after filtering, there are no _.yml_ items left, then return _No Items_.  
如果筛选后没有剩余.yml项，则返回无项。

# Filtering YAML Payloads 筛选 YAML 有效负载

You might decide to use this same prompt for cleaning/filtering a _.yml_ payload.  
您可能决定使用相同的提示来清理/筛选.yml有效负载。

First, let’s focus on a payload that contains both valid and invalid `schema` in reference to our desired `schema`. `Apple slices` fit the criteria; however, `Bananas` doesn’t exist, and you should expect for the `User Query` to be appropriately filtered.  
首先，让我们关注一个有效负载，它同时包含有效和无效的 `schema` 以引用我们想要的 `schema` 。 `Apple slices` 符合标准;但是， `Bananas` 不存在，您应该期望 `User Query` 被适当过滤。

Input: 输入：

# User Query:
- item: Apple Slices
  quantity: 5
  unit: pieces
- item: Bananas
  quantity: 3
  unit: pieces

Output: 输出：

# Updated yaml list
- item: Apple Slices
  quantity: 5
  unit: pieces

In the preceding example, you’ve successfully filtered the user’s payload against a set criteria and have used the language model as a _reasoning engine_.  
在前面的示例中，你已成功根据设置的条件筛选了用户的有效负载，并将语言模型用作推理引擎。

By providing the LLM with a set of instructions within the prompt, the response is closely related to what a human might do if they were manually cleaning the data.  
通过在提示中向 LLM 提供一组指令，响应与手动清理数据时人类可能执行的操作密切相关。

The input prompt facilitates the delegation of more control flow tasks to a language learning model (LLM), tasks that would typically require coding in a programming language like Python or JavaScript.  
输入提示有助于将更多控制流任务委派给语言学习模型 （LLM），这些任务通常需要使用 Python 或 JavaScript 等编程语言进行编码。

[Figure 3-1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-1) provides a detailed overview of the logic applied when processing user queries by an LLM.  
图 3-1 详细介绍了在 LLM 处理用户查询时应用的逻辑。

![Using an LLM to determine the control flow of an application instead of directly using code.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0301.png)

###### Figure 3-1. Using an LLM to determine the control flow of an application instead of code  
图 3-1。使用 LLM 确定应用程序的控制流，而不是代码

# Handling Invalid Payloads in YAML  
在 YAML 中处理无效的负载

A completely invalid payload might look like this:  
完全无效的有效负载可能如下所示：

Input: 输入：

# User Query:
- item: Bananas
  quantity: 3
  unit: pieces

Output: 输出：

No Items

As expected, the LLM returned `No Items` as none of the `User Query` items matched against the previously defined `schema`.  
正如预期的那样，LLM 返回 `No Items` ，因为 `User Query` 项与先前定义的 `schema` 不匹配。

Let’s create a Python script that gracefully accommodates for the various types of LLM results returned. The core parts of the script will focus on:  
让我们创建一个 Python 脚本，该脚本可以正常适应返回的各种类型的 LLM 结果。脚本的核心部分将侧重于：

- Creating custom exceptions for each type of error that might occur due to the three LLM response scenarios  
    为由于三种 LLM 响应方案而可能发生的每种类型的错误创建自定义异常
    
- Parsing the proposed schema  
    解析建议的架构
    
- Running a serious of custom checks against the response so you can be sure that the YML response can be safely passed to downstream software applications/microservices  
    对响应进行严格的自定义检查，以确保 YML 响应可以安全地传递到下游软件应用程序/微服务
    

You could define six specific errors that would handle for all of the edge cases:  
您可以定义六个特定错误，以处理所有边缘情况：

```

class

```

Then provide the previously proposed `YML schema` as a string:  
然后将前面建议的 `YML schema` 作为字符串提供：

```

# Provided schema

```

Import the `yaml` module and create a custom parser function called `validate_``response` that allows you to easily determine whether an LLM output is valid:  
导入 `yaml` 模块并创建一个名为 `validate_` `response` 的自定义解析器函数，该函数允许您轻松确定 LLM 输出是否有效：

```

import

```

To test these edge cases, following you’ll find several mocked LLM responses:  
为了测试这些边缘情况，你会发现几个被嘲笑的LLM响应：

```

# Fake responses

```

Finally, now you can:  
最后，现在您可以：

- Use `yaml.safe_load(response)` to safely parse the _.yml_ schema  
    使用 `yaml.safe_load(response)` 安全地解析 .yml 架构
    
- Call the `validate_response` function for each LLM response to test it against custom _.yml_ validation logic  
    为每个 LLM 响应调用 `validate_response` 函数，以根据自定义.yml验证逻辑对其进行测试
    

```

# Parse the fake responses

```

# Diverse Format Generation with ChatGPT  
使用 ChatGPT 生成多种格式

ChatGPT is not only capable of generating _.json_ or _.yml_ files but can also support many other data formats. For example, it can aid you in creating a mermaid diagram or generating a mock _.csv_ document. Its versatility stretches to even generating code, conversations, and scripts.  
ChatGPT 不仅能够生成.json或.yml文件，还可以支持许多其他数据格式。例如，它可以帮助您创建美人鱼图或生成模拟.csv文档。它的多功能性甚至可以生成代码、对话和脚本。

Let’s explore in detail how ChatGPT can produce diverse formatted content. Mermaid is a markdown-like scripting language for generating charts, diagrams, and other visualizations.  
让我们详细探讨 ChatGPT 如何生成多样化的格式内容。Mermaid 是一种类似 Markdown 的脚本语言，用于生成图表、图表和其他可视化效果。

Input: 输入：

Create a flowchart diagram in mermaid syntax showing a simple food ordering
process that starts with "Choose food" and ends with "Pay for meal."
Include steps for "Add food to cart" and "Confirm cart."

Output: 输出：

graph TD
    ChooseFood[Choose Food] --> AddToCart[Add to Cart]
    AddToCart --> ConfirmCart[Confirm Cart]
    ConfirmCart --> PayForMeal[Pay for Meal]

This output, when input to a mermaid diagram renderer, will create a precise flowchart reflecting the food ordering process ([Figure 3-2](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-2)).  
当输入到美人鱼图渲染器时，此输出将创建一个反映食物订购过程的精确流程图（图 3-2）。

![A simple mermaid diagram output from an LLM.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0302.png)

###### Figure 3-2. A streamlined flow diagram created using mermaid syntax via an LLM  
图 3-2。通过 @1001 使用 mermaid 语法创建的简化流程图#

## Mock CSV Data 模拟 CSV 数据

ChatGPT can also generate mock CSV data that can be utilized for testing purposes or other uses.  
ChatGPT 还可以生成模拟 CSV 数据，可用于测试目的或其他用途。

Input: 输入：

Generate a sample CSV data for five students with the following fields:
name, age, grade.

Output: 输出：

name,age,grade
John,16,A
Alex,17,B
Emma,16,A
Sophia,16,B
Liam,17,A

The example generated is a well-formatted CSV file, which can be loaded directly into many tools that read CSV data.  
生成的示例是一个格式良好的 CSV 文件，可以直接加载到许多读取 CSV 数据的工具中。

Remember, GPT models rely heavily on the format you specify. For instance, specifying CSV implies the AI should use commas as separators. Be clear about the desired format for optimal results.  
请记住，GPT 模型在很大程度上依赖于您指定的格式。例如，指定 CSV 意味着 AI 应使用逗号作为分隔符。明确所需的格式以获得最佳结果。

You’ve explored different ways of extracting structured data from language models including regular expressions, JSON, YML, and other formats. You can also now use LLMs to direct parts of your application’s control flow.  
您已经探索了从语言模型（包括正则表达式、JSON、YML 和其他格式）中提取结构化数据的不同方法。现在，您还可以使用 LLMs 来指导应用程序控制流的某些部分。

# Explain It like I’m Five  
像我五岁一样解释它

The _Explain It like I’m Five_ prompt focuses on explaining a given section of text _as if you were talking to a five-year-old child._  
“像我五岁一样解释它”提示侧重于解释给定的文本部分，就好像你在和一个五岁的孩子说话一样。

This style of prompting is very effective and is a great way to convert technical documents into simple summaries that anyone can understand.  
这种提示方式非常有效，是将技术文档转换为任何人都可以理解的简单摘要的好方法。

Let’s apply this prompt to an abstract of [“Tumor Microenvironment: Recent Advances in Various Cancer Treatments”](https://oreil.ly/MDOsz).  
让我们将这个提示应用于“肿瘤微环境：各种癌症治疗的最新进展”的摘要。

Input: 输入：

Explain the following text as if I was 5 years old. Explain it like I'm 5.

Text: This is a review regarding different types of cancer treatments.
We aimed at analyzing the tumor microenvironment and the recent trends
for the therapeutic applications and effectiveness for several kinds
of cancers. Traditionally the cancer treatment was based on the
neoplastic cells.

...(shortened for brevity)...

Output: 输出：

Cancer is a sickness that makes your body's cells grow and divide in a way
that is not normal. Doctors have different ways to treat cancer, like
cutting it out, giving you medicine, or using special rays to kill the
cancer cells...

The ChatGPT output from the preceding example is much more digestible than the abstract.  
前面示例的 ChatGPT 输出比摘要更容易理解。

# Universal Translation Through LLMs  
通过LLMs进行通用翻译

Additionally, language models can potentially act as _universal translators_ due to their proficiency in understanding and generating human-like text across multiple languages.  
此外，由于语言模型能够熟练地理解和生成跨多种语言的类似人类的文本，因此可以充当通用翻译器。

Let’s investigate this with a simple example:  
让我们用一个简单的例子来研究这个问题：

1. Generate some simple text.  
    生成一些简单的文本。
    
2. Change the simple text and make it difficult to read.  
    更改简单的文本并使其难以阅读。
    
3. Then transform the same text back into an easy to read format in Spanish (instead of English).  
    然后将相同的文本转换回易于阅读的西班牙语格式（而不是英语）。
    
4. Revert the simplistic text back into English.  
    将简单的文本恢复为英文。
    

Input: 输入：

Create some simple text.

Output: 输出：

The sun gently rises, painting the sky with hues of orange and pink. Birds
chirp merrily as they welcome the new day. The cool breeze whispers through
the trees, carrying the scent of fresh grass and blooming flowers. Life
awakens with a sense of tranquility and promise.

...(shortened for brevity)...

Input: 输入：

Now make the text incredibly complex and hard to read.

Output: 输出：

In the ethereal realm of celestial ascendancy, wherein the resplendent
orb of the sun commences its gradual ascent, an exquisite phenomenon
unfolds,engendering a symphony of chromatic brilliance upon the
expansive canopy of the firmament. Avian denizens, endowed with
mellifluous voices, bespeak their jubilant salutations, punctuating
the aural tapestry with notes of felicity. The zephyr, tenderly
wafting amidst arboreal sentinels, carries upon its gentle currents
the redolence of verdant blades and blossoming flora.
...(shortened for brevity)...

Input: 输入：

Now transform the text into a simple, easy to read format that's in Spanish
, make sure that it is very easy to understand and read. You must ensure
that it is as simple to comprehend as possible.

- Use simple language.
- Make it concise.

Output: 输出：

En un lugar mágico y celestial, cuando el sol empieza a salir, ocurre algo
hermoso en el cielo. Los pájaros cantan alegremente, llenando el aire con
sus dulces melodías. Una brisa suave sopla entre los árboles, llevando
consigo el olor fresco de la naturaleza. Todo cobra vida y promete momentos
felices. Nos invita a disfrutar de las cosas simples y a encontrar la
felicidad en los pequeños detalles. En este escenario encantador,
encontramos paz y aprendemos que hasta los momentos más simples pueden
ser mágicos.

Input: 输入：

Finally translate it back into English.

Output: 输出：

In a magical and celestial place, when the sun begins to rise, something
beautiful happens in the sky. The birds sing cheerfully, filling the air
with their sweet melodies. A gentle breeze blows among the trees, carrying
the fresh scent of nature. Everything comes alive and promises happy
moments. It invites us to enjoy the simple things and find happiness in the
little details. In this enchanting setting, we find peace and learn that
even the simplest moments can be magical.

As you can see, part of the meaning is lost while doing the translation, and this is to be expected. However, large parts of the original text’s intent remains, demonstrating that LLMs can act as _highly effective translators_ for languages that have adequate resources on the internet. For languages that do not have a good amount of resources, it will yield bad results.  
正如你所看到的，在进行翻译时，部分含义会丢失，这是意料之中的。然而，原文的大部分意图仍然存在，这表明LLMs可以作为互联网上拥有足够资源的语言的高效翻译器。对于没有大量资源的语言，它会产生不好的结果。

The same logic applies to coding languages. LLMs are very good at generating code for established programming languages such as Python and JavaScript but perform worse for newer coding languages and packages.  
同样的逻辑也适用于编码语言。LLMs 非常擅长为已建立的编程语言（如 Python 和 JavaScript）生成代码，但对于较新的编码语言和包来说，性能较差。

The boundaries between different forms of information are becoming _increasingly fluid_. The essence of information itself is evolving, allowing for effortless transformations of summaries into stories, poems, or other creative expressions, ultimately enriching our understanding and engagement with the content.  
不同形式信息之间的界限正变得越来越模糊。信息本身的本质是不断发展的，可以毫不费力地将摘要转化为故事、诗歌或其他创造性表达，最终丰富我们对内容的理解和参与。

_Diffusion models_ are a unique class of generative models utilized in machine learning, specifically designed to produce new images that mimic those found in the training set.  
扩散模型是机器学习中使用的一类独特的生成模型，专门设计用于生成模仿训练集中发现的新图像。

Moreover, when you combine language models with diffusion models, it enables seamless transitions between text, video, and other modalities. This makes it even simpler for you to convey complex ideas across various formats, facilitating a more accessible and comprehensive experience.  
此外，当您将语言模型与扩散模型相结合时，它可以在文本、视频和其他模态之间实现无缝转换。这使您可以更轻松地以各种格式传达复杂的想法，从而获得更易于访问和全面的体验。

# Ask for Context 询问背景信息

LLMs are not only capable of generating text but can also act as simple agents with a limited amount of _reasoning capability._ This allows you to write a prompt asking the language model to either:  
LLMs 不仅能够生成文本，还可以充当推理能力有限的简单代理。这允许您编写一个提示，要求语言模型执行以下任一操作：

- Return a valid result to a question or statement  
    将有效结果返回到问题或陈述
    
- Ask for more context to appropriately answer the question  
    询问更多上下文以适当地回答问题
    

In this section, you’ll learn about the importance of _asking for context_ when working with LLMs such as GPT-4. We will start with an example of a prompt that doesn’t provide enough context, resulting in a less useful response.  
在本节中，您将了解在使用 LLMs（例如 GPT-4）时询问上下文的重要性。我们将从一个提示示例开始，该提示没有提供足够的上下文，导致响应不太有用。

Then, we will provide a better prompt that encourages the model to ask for additional context if needed. Finally, we will use the additional context provided to generate a more informed response.  
然后，我们将提供一个更好的提示，鼓励模型在需要时请求额外的上下文。最后，我们将使用提供的其他上下文来生成更明智的响应。

Input: 输入：

Should I use MongoDB or PostgreSQL for my project?

Output: 输出：

It's difficult to make a recommendation without knowing more about your
specific software requirements. Both MongoDB and PostgreSQL have their
advantages, but the best choice depends on the specific needs of your
project.

In the preceding prompt, the model does not have enough context to make a meaningful recommendation. Instead, you can ask ChatGPT for a list of recommended points that would help it to make an effective decision.  
在前面的提示中，模型没有足够的上下文来提出有意义的建议。相反，您可以向 ChatGPT 索取一份推荐点列表，以帮助它做出有效的决定。

Input: 输入：

Should I use MongoDB or PostgreSQL for my project?

Provide a list of requirements that would help you to make an informed
and high-quality decision about which database solution I should choose?

Output: 输出：

To make an informed decision between MongoDB and PostgreSQL for your
project, consider the following requirements:

1. Data Structure: Evaluate the structure of your data. If your data
is highly unstructured or schema-less, MongoDB's flexible document model
may be more suitable. On the other hand, if your data has a fixed schema
or requires complex relationships, PostgreSQL's relational model might
be a better fit.

...

10. Cost: Assess the cost implications of each database solution. MongoDB
offers both a community edition (free) and a commercial edition with
additional features and support.PostgreSQL is open-source and free to use,
with optional commercial support available from various vendors.

After prompting ChatGPT about how to make an informed decision, now you’re aware of what to include within your prompt to help the language model with deciding.  
在提示 ChatGPT 如何做出明智的决定后，现在您已经知道在提示中应包含哪些内容以帮助语言模型做出决定。

Input: 输入：

Should I use MongoDB or PostgreSQL for my project?

Context:
- Data Structure: Highly unstructured data with varying document formats
and no fixed schema. Scalability: Project requires the ability to handle
massive amounts of data and distribute it across multiple servers.
- ACID Compliance: Strong data consistency and integrity are crucial for
the project's financial transactions.
- Querying Capabilities: Complex geospatial queries and aggregations on
location-based data.
Community and Ecosystem: Active community with numerous third-party
libraries and tools specifically tailored for the project's industry.
- Data Integrity and Constraints: Enforcing strict foreign key
relationships and complex data validation rules.
- Transactions and Concurrency: Requires handling high levels of
concurrent read and write operations while maintaining data consistency.
- Maturity and Stability: Prioritizing a well-established and extensively
tested database for long-term stability.
- Development and Operational Ease: Agile development approach with a need
for rapid prototyping and iterative schema design.
- Cost: Budget constraints necessitate using an open-source solution with
no additional licensing or support costs.

If you need more context, please specify what would help you to make
a better decision.

Output: 输出：

Based on these considerations, both MongoDB and PostgreSQL have their
strengths, but given the emphasis on strong data consistency, complex
querying, and data integrity constraints, PostgreSQL seems to be a more
suitable choice for your project.

In this final example, the model uses the additional context provided to give a well-informed recommendation for using PostgreSQL. By asking for context when necessary, LLMs like ChatGPT and GPT-4 can deliver more valuable and accurate responses.  
在最后一个示例中，该模型使用提供的其他上下文来提供使用 PostgreSQL 的明智建议。通过在必要时询问上下文，LLMs 像 ChatGPT 和 GPT-4 一样可以提供更有价值和准确的响应。

[Figure 3-3](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-3) demonstrates how _asking for context_ changes the decision-making process of LLMs. Upon receiving user input, the model first assesses whether the context given is sufficient. If not, it prompts the user to provide more detailed information, emphasizing the model’s reliance on context-rich inputs. Once adequate context is acquired, the LLM then generates an informed and relevant response.  
图 3-3 演示了请求上下文如何改变 LLMs 的决策过程。在收到用户输入后，模型首先评估给定的上下文是否足够。如果没有，它会提示用户提供更详细的信息，强调模型对上下文丰富的输入的依赖。一旦获得了足够的上下文，LLM 就会生成一个知情且相关的响应。

![The decision process of an LLM with asking for context.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0303.png)

###### Figure 3-3. The decision process of an LLM while asking for context  
图 3-3。LLM 在询问上下文时的决策过程

# ALLOW THE LLM TO ASK FOR MORE CONTEXT BY DEFAULT  
默认情况下，允许 LLM 请求更多上下文

You can allow the LLM to ask for more context as a default by including this key phrase: _If you need more context, please specify what would help you to make a better decision._  
您可以通过包含以下关键短语来允许 LLM 请求更多上下文作为默认值：如果您需要更多上下文，请指定可以帮助您做出更好决定的内容。

In this section, you’ve seen how LLMs can act as agents that use environmental context to make decisions. By iteratively refining the prompt based on the model’s recommendations, we eventually reach a point where the model has _enough context to make a well-informed decision._  
在本节中，您已经了解了 LLMs 如何充当使用环境上下文进行决策的代理。通过根据模型的建议迭代细化提示，我们最终会达到一个点，即模型有足够的上下文来做出明智的决策。

This process highlights the importance of providing sufficient context in your prompts and being prepared to ask for more information when necessary. By doing so, you can leverage the power of LLMs like GPT-4 to make more accurate and valuable recommendations.  
此过程强调了在提示中提供足够的上下文并准备好在必要时询问更多信息的重要性。通过这样做，您可以像 GPT-1001 一样利用 @4# 的力量来提出更准确、更有价值的建议。

In agent-based systems like GPT-4, the ability to ask for more context and provide a finalized answer is crucial for making well-informed decisions. [AutoGPT](https://oreil.ly/l3Ihy), a multiagent system, has a self-evaluation step that automatically checks whether the task can be completed given the current context within the prompt. This technique uses an actor–critic relationship, where the existing prompt context is being analyzed to see whether it could be further refined before being executed.  
在像 GPT-4 这样基于智能体的系统中，询问更多上下文并提供最终答案的能力对于做出明智的决策至关重要。AutoGPT 是一个多智能体系统，它有一个自我评估步骤，可以自动检查任务是否可以在提示中的当前上下文下完成。该技术使用参与者-批评者关系，其中正在分析现有的提示上下文，以查看是否可以在执行之前进一步完善它。

# Text Style Unbundling 文本样式拆分

_Text style unbundling_ is a powerful technique in prompt engineering that allows you to extract and isolate specific textual features from a given document, such as tone, length, vocabulary, and structure.  
文本样式拆分是提示工程中的一项强大技术，它允许您从给定文档中提取和隔离特定的文本特征，例如语气、长度、词汇和结构。

This allows you to create new content that shares similar characteristics with the original document, ensuring consistency in style and tone across various forms of communication.  
这允许您创建与原始文档具有相似特征的新内容，从而确保各种形式的通信在风格和语气上的一致性。

This consistency can be crucial for businesses and organizations that need to communicate with a unified voice across different channels and platforms. The benefits of this technique include:  
对于需要跨不同渠道和平台使用统一语音进行通信的企业和组织来说，这种一致性至关重要。这种技术的优点包括：

Improved brand consistency  
提高品牌一致性

By ensuring that all content follows a similar style, organizations can strengthen their brand identity and maintain a cohesive image.  
通过确保所有内容都遵循相似的风格，组织可以加强其品牌形象并保持有凝聚力的形象。

Streamlined content creation  
简化的内容创建

By providing a clear set of guidelines, writers and content creators can more easily produce materials that align with a desired style.  
通过提供一套明确的指导方针，作家和内容创作者可以更轻松地制作出符合所需风格的材料。

Adaptability 适应性

Text style unbundling allows for the easy adaptation of existing content to new formats or styles while preserving the core message and tone.  
文本样式拆分允许将现有内容轻松调整为新的格式或样式，同时保留核心信息和语气。

The process of text style unbundling involves _identifying the desired textual features_ or creating a meta prompt (a prompt to create prompts) to extract these features and then using the extracted features to guide the generation of new content.  
文本样式解绑的过程包括识别所需的文本特征或创建元提示（创建提示的提示）来提取这些特征，然后使用提取的特征来指导新内容的生成。

# Identifying the Desired Textual Features  
识别所需的文本特征

To successfully unbundle a text style, you must first identify the specific features you want to extract from the input document. Common textual features to consider include:  
要成功解包文本样式，必须首先确定要从输入文档中提取的特定要素。需要考虑的常见文本特征包括：

Tone of voice 语气

The overall mood or attitude conveyed by the text, such as formal, casual, humorous, or authoritative  
文本传达的整体情绪或态度，例如正式的、随意的、幽默的或权威的

Length 长度

The desired word count or general length of the content  
所需的字数或内容的一般长度

Vocabulary and phrasing 词汇和措辞

The choice of words and expressions, including industry-specific jargon, colloquialisms, and complexity  
词语和表达方式的选择，包括行业特定的术语、口语和复杂性

Additionally, you can even create a meta prompt that will dynamically show you these.  
此外，您甚至可以创建一个元提示，动态显示这些内容。

Input: 输入：

Analyze the following text and identify core features that will allow
further documents to imitate the same style, consistency, and formatting
as the document below.

Provide all of the features as a style writing guide that will be used
for future documents.

Analyze the following text:

Artificial intelligence is rapidly transforming the world around us,
opening up new possibilities and revolutionizing industries. From
health care to entertainment, AI is making our lives better and more
convenient in countless ways. However, with great power comes great
responsibility. We must ensure that AI technologies are developed and
deployed ethically and responsibly to protect our privacy and uphold our
values.

Output: 输出：

Style Writing Guide:

Tone of Voice
- Maintain an informative and optimistic tone throughout the document.
- Emphasize the positive impact of the subject matter while acknowledging
any potential concerns or responsibilities.

Length:
...

Vocabulary:
...

Structure:
...

Content:
- Focus on the transformative nature and positive impacts of the subject
matter.
- Highlight specific industries or areas where the subject matter has
made a difference.
- Acknowledge any associated responsibilities or potential risks,
emphasizing the need for ethical and responsible practices.
Stress the importance of privacy protection and upholding values in
relation to the subject matter.

# Generating New Content with the Extracted Features  
使用提取的特征生成新内容

After you’ve extracted the desired features from the input document, you can use this information to guide future content generation. Remember to ensure that the AI model incorporates the extracted features into its output by specifying the desired style in your prompt. For example:  
从输入文档中提取所需要素后，可以使用此信息来指导将来的内容生成。请记住，通过在提示中指定所需的样式，确保 AI 模型将提取的特征合并到其输出中。例如：

- `Write a new blog post on [topic] using the same tone of voice, length, vocabulary, and structure as the previously analyzed text.`

By combining this technique with _reference text_ (documents that act as grounding truth), you can produce credible, branded content that requires minimal revisions.  
通过将这种技术与参考文本（作为基础事实的文档）相结合，您可以制作出需要最少修改的可信的品牌内容。

# Extracting Specific Textual Features with LLMs  
使用 LLMs 提取特定的文本特征

You can easily tailor a prompt to guide an LLM in extracting particular textual features from a document. This can be applied beyond just analyzing text for copywriting purposes. For instance, recognizing entities or discerning sentiment from the text can be achieved by crafting a precise instruction for the LLM.  
您可以轻松定制提示，以指导LLM从文档中提取特定的文本特征。这可以应用于不仅仅是出于文案目的分析文本。例如，可以通过为 LLM 制作精确的指令来实现识别实体或从文本中辨别情感。

Input: 输入：

Analyze the following text to identify and list the entities mentioned:

Artificial intelligence is rapidly transforming the world around us,
opening up new possibilities and revolutionizing industries. From
health care to entertainment, AI is making our lives better and more
convenient in countless ways. However, with great power comes great
responsibility. We must ensure that AI technologies are developed
and deployed ethically and responsibly to protect our privacy and
uphold our values.

Output: 输出：

Entities:
- Artificial Intelligence (AI)
- Health care
- Entertainment
- Privacy
- Values

# Summarization 综述

In the era of information overload, the ability to condense large amounts of text into concise, digestible summaries has become an essential skill. As the volume of data we produce and consume continues to grow, the demand for effective summarization techniques has increased significantly.  
在信息过载的时代，将大量文本浓缩成简明易懂的摘要的能力已成为一项必不可少的技能。随着我们生产和消费的数据量不断增长，对有效摘要技术的需求显着增加。

AI has made significant advancements in this domain, providing powerful tools for generating summaries that retain the most critical information while discarding less relevant details.  
人工智能在这一领域取得了重大进展，为生成摘要提供了强大的工具，这些摘要保留了最关键的信息，同时丢弃了不太相关的细节。

Let’s explore how to summarize using a language model.  
让我们探讨一下如何使用语言模型进行总结。

Input: 输入：

Summarize the following text:

Whereas the party of the first part, hereinafter referred to as the
"Purchaser," and the party of the second part, hereinafter referred to
as the "Vendor," being fully cognizant of their respective legal
obligations and responsibilities pursuant to the applicable statutory
provisions and common law doctrines, have duly entered into a legally
binding agreement, hereinafter referred to as the "Agreement," for the
purpose of effectuating a transaction involving the transfer of goods,
hereinafter referred to as the "Goods," between the Purchaser and the
Vendor, subject to the terms and conditions set forth herein, the Parties
do hereby solemnly acknowledge and affirm the following:
...

Output: 输出：

This is a legally binding agreement between the Purchaser and the Vendor
for the transfer of goods. The agreement incorporates the recitals as an
integral part, but in case of any conflict, the operative provisions of the
agreement prevail. The interpretation clause states that singular words
include the plural and vice versa, and words referring to a gender include
all genders. References to statutory provisions include any amendments or
replacements.

Summarization is an invaluable application of AI, enabling users to quickly extract key insights from lengthy articles, reports, or research papers. This process can help individuals make informed decisions, save time, and prioritize their reading. AI-generated summaries can also facilitate information sharing among teams, allowing for more efficient collaboration and communication.  
摘要是人工智能的一个宝贵应用，使用户能够从冗长的文章、报告或研究论文中快速提取关键见解。这个过程可以帮助个人做出明智的决定，节省时间，并优先考虑他们的阅读。人工智能生成的摘要还可以促进团队之间的信息共享，从而实现更有效的协作和沟通。

# Summarizing Given Context Window Limitations  
总结给定的上下文窗口限制

For documents larger than an LLM can handle in a single API request, a common approach is to chunk the document, summarize each chunk, and then combine these summaries into a final summary, as shown in [Figure 3-4](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-4).  
对于大于 LLM 可以在单个 API 请求中处理的文档，一种常见的方法是对文档进行分块，对每个块进行汇总，然后将这些摘要合并为最终摘要，如图 3-4 所示。

![.A summarization pipeline that uses text splitting and multiple summarization steps.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0304.png)

###### Figure 3-4. A summarization pipeline that uses text splitting and multiple summarization steps  
图 3-4。使用文本拆分和多个摘要步骤的摘要管道

Additionally, people may require different types of summaries for various reasons, and this is where AI summarization comes in handy. As illustrated in the preceding diagram, a large PDF document could easily be processed using AI summarization to generate distinct summaries tailored to individual needs:  
此外，人们可能出于各种原因需要不同类型的摘要，这就是 AI 摘要派上用场的地方。如上图所示，可以使用 AI 摘要轻松处理大型 PDF 文档，以生成针对个人需求量身定制的不同摘要：

Summary A 摘要 A

Provides key insights, which is perfect for users seeking a quick understanding of the document’s content, enabling them to focus on the most crucial points  
提供关键见解，非常适合寻求快速了解文档内容的用户，使他们能够专注于最关键的点

Summary B 摘要 B

On the other hand, offers decision-making information, allowing users to make informed decisions based on the content’s implications and recommendations  
另一方面，提供决策信息，允许用户根据内容的含义和建议做出明智的决定

Summary C 摘要 C

Caters to collaboration and communication, ensuring that users can efficiently share the document’s information and work together seamlessly  
迎合协作和沟通，确保用户能够有效地共享文档信息并无缝协作

By customizing the summaries for different users, AI summarization contributes to increased information retrieval for all users, making the entire process more efficient and targeted.  
通过为不同用户自定义摘要，AI 摘要有助于增加所有用户的信息检索，使整个过程更加高效和有针对性。

Let’s assume you’re only interested in finding and summarizing information about the advantages of digital marketing. Simply change your summarization prompt to `Provide a concise, abstractive summary of the above text. Only summarize the advantages: ...`  
假设您只对查找和总结有关数字营销优势的信息感兴趣。只需将摘要提示更改为 `Provide a concise, abstractive summary of the above text. Only summarize the advantages: ...`

AI-powered summarization has emerged as an essential tool for quickly distilling vast amounts of information into concise, digestible summaries that cater to various user needs. By leveraging advanced language models like GPT-4, AI summarization techniques can efficiently extract key insights and decision-making information, and also facilitate collaboration and communication.  
人工智能驱动的摘要已成为一种必不可少的工具，可以快速将大量信息提炼成简洁、易于理解的摘要，以满足各种用户需求。通过利用 GPT-4 等高级语言模型，AI 摘要技术可以有效地提取关键见解和决策信息，并促进协作和沟通。

As the volume of data continues to grow, the demand for effective and targeted summarization will only increase, making AI a crucial asset for individuals and organizations alike in navigating the Information Age.  
随着数据量的持续增长，对有效和有针对性的摘要的需求只会增加，这使得人工智能成为个人和组织在信息时代驾驭的重要资产。

# Chunking Text 分块文本

LLMs continue to develop and play an increasingly crucial role in various applications, as the ability to process and manage large volumes of text becomes ever more important. An essential technique for handling large-scale text is known as _chunking._  
LLMs 继续发展，并在各种应用程序中发挥越来越重要的作用，因为处理和管理大量文本的能力变得越来越重要。处理大型文本的一种基本技术称为分块。

_Chunking_ refers to the process of breaking down large pieces of text into smaller, more manageable units or chunks. These chunks can be based on various criteria, such as sentence, paragraph, topic, complexity, or length. By dividing text into smaller segments, AI models can more efficiently process, analyze, and generate responses.  
分块是指将大段文本分解为更小、更易于管理的单元或块的过程。这些块可以基于各种条件，例如句子、段落、主题、复杂性或长度。通过将文本划分为更小的片段，AI 模型可以更有效地处理、分析和生成响应。

[Figure 3-5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-5) illustrates the process of chunking a large piece of text and subsequently extracting topics from the individual chunks.  
图 3-5 演示了对大段文本进行分块，然后从各个块中提取主题的过程。

![Topic extraction process after chunking text.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0305.png)

###### Figure 3-5. Topic extraction with an LLM after chunking text  
图 3-5。在分块文本后使用 LLM 提取主题

## Benefits of Chunking Text  
分块文本的好处

There are several advantages to chunking text, which include:  
分块文本有几个优点，包括：

Fitting within a given context length  
在给定的上下文长度内拟合

LLMs only have a certain amount of input and output tokens, which is called a _context length_. By reducing the input tokens you can make sure the output won’t be cut off and the initial request won’t be rejected.  
LLMs 只有一定数量的输入和输出标记，这称为上下文长度。通过减少输入令牌，可以确保输出不会被切断，初始请求不会被拒绝。

Reducing cost 降低成本

Chunking helps you to only retrieve the most important points from documents, which reduces your token usage and API costs.  
分块可帮助您仅从文档中检索最重要的点，从而减少令牌使用和 API 成本。

Improved performance 改进的性能

Chunking reduces the processing load on LLMs, allowing for faster response times and more efficient resource utilization.  
分块减少了 LLMs 上的处理负载，从而实现了更快的响应时间和更有效的资源利用率。

Increased flexibility 提高灵活性

Chunking allows developers to tailor AI responses based on the specific needs of a given task or application.  
分块允许开发人员根据给定任务或应用程序的特定需求定制 AI 响应。

## Scenarios for Chunking Text  
对文本进行分块的方案

Chunking text can be particularly beneficial in certain scenarios, while in others it may not be required. Understanding when to apply this technique can help in optimizing the performance and cost efficiency of LLMs.  
在某些情况下，对文本进行分块可能特别有用，而在其他情况下，它可能不是必需的。了解何时应用此技术有助于优化 LLMs 的性能和成本效益。

### When to chunk 何时分块

Large documents 大型文档

When dealing with extensive documents that exceed the maximum token limit of the LLM  
在处理超过 @1001 最大令牌限制的大量文档时#

Complex analysis 复杂分析

In scenarios where a detailed analysis is required and the document needs to be broken down for better comprehension and processing  
在需要详细分析并且需要分解文档以便更好地理解和处理的情况下

Multitopic documents 多主题文档

When a document covers multiple topics and it’s beneficial to handle them individually  
当文档涵盖多个主题并且单独处理它们是有益的

### When not to chunk  
何时不分块

Short documents 短文档

When the document is short and well within the token limits of the LLM  
当文档很短并且完全在 @1001 的令牌限制范围内时#

Simple analysis 简单分析

In cases where the analysis or processing required is straightforward and doesn’t benefit from chunking  
在所需的分析或处理简单且无法从分块中受益的情况下

Single-topic documents 单主题文档

When a document is focused on a single topic and chunking doesn’t add value to the processing  
当文档专注于单个主题并且分块不会为处理增加价值时

## Poor Chunking Example 糟糕的分块示例

When text is not chunked correctly, it can lead to reduced LLM performance. Consider the following paragraph from a news article:  
当文本未正确分块时，可能会导致 LLM 性能降低。请看一篇新闻文章中的以下段落：

The local council has decided to increase the budget for education by 10%
this year, a move that has been welcomed by parents and teachers alike. The
additional funds will be used to improve school infrastructure, hire more
teachers, and provide better resources for students. However, some critics
argue that the increase is not enough to address the growing demands of the
education system.

When the text is fragmented into isolated words, the resulting list lacks the original context:  
当文本被分割成孤立的单词时，生成的列表缺少原始上下文：

["The", "local", "council", "has", "decided", "to", "increase", "the",
"budget", ...]

The main issues with this poor chunking example include:  
这个糟糕的分块示例的主要问题包括：

Loss of context 失去上下文

By splitting the text into individual words, the original meaning and relationships between the words are lost. This makes it difficult for AI models to understand and respond effectively.  
通过将文本拆分为单个单词，单词之间的原始含义和关系会丢失。这使得 AI 模型难以有效理解和响应。

Increased processing load  
增加处理负荷

Processing individual words requires more computational resources, making it less efficient than processing larger chunks of text.  
处理单个单词需要更多的计算资源，因此其效率低于处理较大的文本块。

As a result of the poor chunking in this example, an LLM may face several challenges:  
由于此示例中的分块较差，LLM 可能会面临以下几个挑战：

- Difficulty understanding the main ideas or themes of the text  
    难以理解文本的主要思想或主题
    
- Struggling to generate accurate summaries or translations  
    难以生成准确的摘要或翻译
    
- Inability to effectively perform tasks such as sentiment analysis or text `classification`  
    无法有效执行情绪分析或文本 @0 等任务#
    

By understanding the pitfalls of poor chunking, you can apply prompt engineering principles to improve the process and achieve better results with AI language models.  
通过了解不良分块的陷阱，您可以应用提示工程原理来改进流程并使用 AI 语言模型获得更好的结果。

Let’s explore an improved chunking example using the same news article paragraph from the previous section; you’ll now chunk the text by sentence:  
让我们使用上一节中的相同新闻文章段落来探索一个改进的分块示例;现在，您将按句子对文本进行分块：

["""The local council has decided to increase the budget for education
by 10% this year, a move that has been welcomed by parents and teachers alike.
""",

"""The additional funds will be used to improve school infrastructure,
hire more teachers, and provide better resources for students.""",

""""However, some critics argue that the increase is not enough to
address the growing demands of the education system."""]

# DIVIDE LABOR AND EVALUATE QUALITY  
分工考核质量

Define the granularity at which the text should be chunked, such as by sentence, paragraph, or topic. Adjust parameters like the number of tokens or model temperature to optimize the chunking process.  
定义应对文本进行分块的粒度，例如按句子、段落或主题。调整令牌数量或模型温度等参数，以优化分块过程。

By chunking the text in this manner, you could insert whole sentences into an LLM prompt with the most relevant sentences.  
通过以这种方式分块文本，您可以将整个句子插入到包含最相关句子的 LLM 提示中。

# Chunking Strategies 分块策略

There are many different chunking strategies, including:  
有许多不同的分块策略，包括：

Splitting by sentence 按句子拆分

Preserves the context and structure of the original content, making it easier for LLMs to understand and process the information. Sentence-based chunking is particularly useful for tasks like summarization, translation, and sentiment analysis.  
保留原始内容的上下文和结构，使 LLMs 更容易理解和处理信息。基于句子的分块对于摘要、翻译和情感分析等任务特别有用。

Splitting by paragraph 按段落拆分

This approach is especially effective when dealing with longer content, as it allows the LLM to focus on one cohesive unit at a time. Paragraph-based chunking is ideal for applications like document analysis, topic modeling, and information extraction.  
这种方法在处理较长的内容时特别有效，因为它允许 LLM 一次专注于一个有凝聚力的单元。基于段落的分块非常适合文档分析、主题建模和信息提取等应用程序。

Splitting by topic or section  
按主题或部分拆分

This method can help AI models better identify and understand the main themes and ideas within the content. Topic-based chunking is well suited for tasks like text classification, content recommendations, and clustering.  
这种方法可以帮助 AI 模型更好地识别和理解内容中的主要主题和思想。基于主题的分块非常适合文本分类、内容推荐和聚类等任务。

Splitting by complexity 按复杂度拆分

For certain applications, it might be helpful to split text based on its complexity, such as the reading level or technicality of the content. By grouping similar complexity levels together, LLMs can more effectively process and analyze the text. This approach is useful for tasks like readability analysis, content adaptation, and personalized learning.  
对于某些应用程序，根据文本的复杂性（例如内容的阅读级别或技术性）拆分文本可能会有所帮助。通过将相似的复杂度级别组合在一起，LLMs 可以更有效地处理和分析文本。这种方法对于可读性分析、内容适应和个性化学习等任务很有用。

Splitting by length 按长度拆分

This technique is particularly helpful when working with very long or complex documents, as it allows LLMs to process the content more efficiently. Length-based chunking is suitable for applications like large-scale text analysis, search engine indexing, and text preprocessing.  
这种技术在处理很长或很复杂的文档时特别有用，因为它允许 LLMs 更有效地处理内容。基于长度的分块适用于大规模文本分析、搜索引擎索引和文本预处理等应用。

Splitting by tokens using a tokenizer  
使用分词器按令牌拆分

Utilizing a tokenizer is a crucial step in many natural language processing tasks, as it enables the process of splitting text into individual tokens. Tokenizers divide text into smaller units, such as words, phrases, or symbols, which can then be analyzed and processed by AI models more effectively. You’ll shortly be using a package called `tiktoken`, which is a bytes-pair encoding tokenizer (BPE) for chunking.  
使用分词器是许多自然语言处理任务中的关键步骤，因为它可以将文本拆分为单个令牌的过程。分词器将文本划分为更小的单元，例如单词、短语或符号，然后 AI 模型可以更有效地分析和处理这些单元。您很快就会使用一个名为 `tiktoken` 的包，这是一个用于分块的字节对编码分词器 （BPE）。

[Table 3-1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#table-3-1) provides a high-level overview of the different chunking strategies; it’s worth considering what matters to you most when performing chunking.  
表 3-1 提供了不同分块策略的高级概述;在执行分块时，值得考虑什么对您来说最重要。

Are you more interested in preserving semantic context, or would naively splitting by length suffice?  
您是对保留语义上下文更感兴趣，还是天真地按长度拆分就足够了？

Table 3-1. Six chunking strategies highlighting their advantages and disadvantages  
表 3-1.六种分块策略突出其优缺点
|Splitting strategy 拆分策略|Advantages|Disadvantages|
|---|---|---|
|Splitting by sentence 按句子拆分|Preserves context, suitable for various tasks  <br>保留上下文，适用于各种任务|May not be efficient for very long content  <br>对于很长的内容可能效率不高|
|Splitting by paragraph 按段落拆分|Handles longer content, focuses on cohesive units  <br>处理较长的内容，专注于有凝聚力的单元|Less granularity, may miss subtle connections  <br>粒度较小，可能会遗漏细微的连接|
|Splitting by topic 按主题拆分|Identifies main themes, better for classification  <br>确定主要主题，更好地分类|Requires topic identification, may miss fine details  <br>需要主题识别，可能会遗漏细节|
|Splitting by complexity 按复杂度拆分|Groups similar complexity levels, adaptive  <br>对相似的复杂度级别进行分组，自适应|Requires complexity measurement, not suitable for all tasks  <br>需要复杂度测量，并不适合所有任务|
|Splitting by length 按长度拆分|Manages very long content, efficient processing  <br>管理很长的内容，高效处理|Loss of context, may require more preprocessing steps  <br>丢失上下文，可能需要更多的预处理步骤|
|Using a tokenizer: Splitting by tokens  <br>使用分词器：按令牌拆分|Accurate token counts, which helps in avoiding LLM prompt token limits  <br>准确的令牌计数，有助于避免 LLM 提示令牌限制|Requires tokenization, may increase computational complexity  <br>需要标记化，可能会增加计算复杂性|

By choosing the appropriate chunking strategy for your specific use case, you can optimize the performance and accuracy of AI language models.  
通过为您的特定用例选择适当的分块策略，您可以优化 AI 语言模型的性能和准确性。

# Sentence Detection Using SpaCy  
使用 SpaCy 进行句子检测

_Sentence detection_, also known as sentence boundary disambiguation, is the process used in NLP that involves identifying the start and end of sentences within a given text. It can be particularly useful for tasks that require preserving the context and structure of the original content. By splitting the text into sentences, LLMs can better understand and process the information for tasks such as summarization, translation, and sentiment analysis.  
句子检测，也称为句子边界消歧，是 NLP 中使用的过程，涉及识别给定文本中句子的开头和结尾。对于需要保留原始内容的上下文和结构的任务，它特别有用。通过将文本拆分为句子，LLMs 可以更好地理解和处理摘要、翻译和情感分析等任务的信息。

Splitting by sentence is possible using NLP libraries such as [spaCy](https://spacy.io/). Ensure that you have spaCy installed in your Python environment. You can install it with `pip install spacy`. Download the `en_core_web_sm` model using the command `python -m spacy download en_core_web_sm`.  
使用 spaCy 等 NLP 库可以按句子拆分。确保您在 Python 环境中安装了 spaCy。你可以用 `pip install spacy` 安装它。使用命令 `python -m spacy download en_core_web_sm` 下载 `en_core_web_sm` 模型。

In [Example 3-3](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#ex-3-3), the code demonstrates sentence detection using the spaCy library in Python.  
在示例 3-3 中，代码演示了使用 Python 中的 spaCy 库进行句子检测。

##### Example 3-3. [Sentence detection with spaCy](https://oreil.ly/GKDnc)  
例 3-3.使用 spaCy 进行句子检测

```

import

```

Output: 输出：

This is a sentence.
This is another sentence.

First, you’ll import the spaCy library and load the English model `(en_core_web_sm)` to initialize an `nlp` object. Define an input text with two sentences; the text is then processed with `doc = nlp(text)`, creating a `doc` object as a result. Finally, the code iterates through the detected sentences using the `doc.sents` attribute and prints each sentence.  
首先，您将导入 spaCy 库并加载英文模型 `(en_core_web_sm)` 以初始化 `nlp` 对象。定义包含两个句子的输入文本;然后用 `doc = nlp(text)` 处理文本，从而创建一个 `doc` 对象。最后，代码使用 `doc.sents` 属性循环访问检测到的句子并打印每个句子。

# Building a Simple Chunking Algorithm in Python  
在 Python 中构建简单的分块算法

After exploring many chunking strategies, it’s important to build your intuition by writing a simple chunking algorithm from scatch.  
在探索了许多分块策略之后，通过从 scatch 编写一个简单的分块算法来建立你的直觉是很重要的。

[Example 3-4](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#ex-3-4) shows how to chunk text based on the length of characters from the blog post “Hubspot - What Is Digital Marketing?” This file can be found in the Github repository at _[content/chapter_3/hubspot_blog_post.txt](https://oreil.ly/30rlQ)_.  
示例 3-4 显示了如何根据博客文章“Hubspot - 什么是数字营销”中的字符长度对文本进行分块。此文件可在 Github 存储库的 content/chapter_3/hubspot_blog_post.txt 中找到。

To correctly read the _hubspot_blog_post.txt_ file, make sure your current working directory is set to the [_content/chapter_3_](https://oreil.ly/OHurh) GitHub directory. This applies for both running the Python code or launching the Jupyter Notebook server.  
若要正确读取 hubspot_blog_post.txt 文件，请确保当前工作目录设置为 content/chapter_3 GitHub 目录。这适用于运行 Python 代码或启动 Jupyter Notebook 服务器。

##### Example 3-4. [Character chunking](https://oreil.ly/n3sNy)  
例 3-4.字符分块

```

with

```

Output: 输出：

search engine optimization strategy for many local businesses is an optimized
Google My Business profile to appear in local search results when people look for
products or services related to what yo
--------------------
u offer.

For Keeps Bookstore, a local bookstore in Atlanta, GA, has optimized its
Google My Business profile for local SEO so it appears in queries for
“atlanta bookstore.”
--------------------
...(shortened for brevity)...

First, you open the text file _hubspot_blog_post.txt_ with the `open` function and read its contents into the variable text. Then using a list comprehension you create a list of chunks, where each `chunk` is a 200 character substring of text.  
首先，使用 `open` 函数打开文本文件hubspot_blog_post.txt，并将其内容读入变量文本中。然后使用列表推导式创建一个块列表，其中每个 `chunk` 都是一个 200 个字符的文本子字符串。

Then you use the `range` function to generate indices for each 200 character substring, and the `i:i+200` slice notation to extract the substring from text.  
然后，使用 `range` 函数为每个 200 个字符的子字符串生成索引，并使用 `i:i+200` 切片表示法从文本中提取子字符串。

Finally, you loop through each chunk in the `chunks` list and `print` it to the console.  
最后，将 `chunks` 列表中的每个块循环，并将其 `print` 循环到控制台。

As you can see, because the chunking implementation is relatively simple and only based on length, there are gaps within the sentences and even words.  
正如你所看到的，因为分块的实现相对简单，而且只基于长度，所以句子甚至单词之间都存在间隙。

For these reasons we believe that good NLP chunking has the following properties:  
由于这些原因，我们认为好的 NLP 分块具有以下属性：

- Preserves entire words, ideally sentences and contextual points made by speakers  
    保留整个单词，最好是说话者的句子和上下文要点
    
- Handles for when sentences span across several pages, for example, page 1 into page 2  
    当句子跨越多个页面时的句柄，例如，第 1 页到第 2 页
    
- Provides an adequate token count for each `chunk` so that the total number of input tokens will appropriately fit into a given token context window for any LLM  
    为每个 `chunk` 提供足够的令牌计数，以便输入令牌的总数将适当地适合任何 @1001 的给定令牌上下文窗口#
    

# Sliding Window Chunking 滑动窗口分块

_Sliding window chunking_ is a technique used for dividing text data into overlapping chunks, or _windows_, based on a specified number of characters.  
滑动窗口分块是一种用于根据指定数量的字符将文本数据划分为重叠块或窗口的技术。

But what exactly is a sliding window?  
但究竟什么是推拉窗？

Imagine viewing a long piece of text through a small window. This window is only capable of displaying a fixed number of characters at a time. As you slide this window from the beginning to the end of the text, you see _overlapping chunks of text_. This mechanism forms the essence of the sliding window approach.  
想象一下，通过一个小窗口查看一长段文本。此窗口一次只能显示固定数量的字符。当您从文本的开头滑动此窗口到文本的结尾时，您会看到重叠的文本块。这种机制构成了滑动窗口方法的本质。

Each window size is defined by a _fixed number of characters_, and the _step size_ determines how far the window moves with each slide.  
每个窗口大小由固定数量的字符定义，步长决定了窗口随每张幻灯片移动的距离。

In [Figure 3-6](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-6), with a window size of 5 characters and a step size of 1, the first chunk would contain the first 5 characters of the text. The window then slides 1 character to the right to create the second chunk, which contains characters 2 through 6.  
在图 3-6 中，窗口大小为 5 个字符，步长为 1，第一个块将包含文本的前 5 个字符。然后，窗口向右滑动 1 个字符以创建第二个块，其中包含字符 2 到 6。

This process repeats until the end of the text is reached, ensuring each chunk overlaps with the previous and next ones to retain some shared context.  
此过程重复进行，直到到达文本的末尾，确保每个块都与上一个和下一个块重叠，以保留一些共享的上下文。

![pega 0306](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0306.png)

###### Figure 3-6. A sliding window, with a window size of 5 and a step size of 1  
图 3-6。滑动窗口，窗口大小为 5，步长为 1

Due to the step size being 1, there is a lot of duplicate information between chunks, and at the same time the risk of losing information between chunks is dramatically reduced.  
由于步长为 1，因此块之间存在大量重复信息，同时块之间丢失信息的风险大大降低。

This is in stark contrast to [Figure 3-7](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-7), which has a window size of 4 and a step size of 2. You’ll notice that because of the 100% increase in step size, the amount of information shared between the chunks is greatly reduced.  
这与图 3-7 形成鲜明对比，图 3-7 的窗口大小为 4，步长为 2。您会注意到，由于步长增加了 100%，块之间共享的信息量大大减少。

![pega 0307](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0307.png)

###### Figure 3-7. A sliding window, with a window size of 4 and a step size of 2  
图 3-7。滑动窗口，窗口大小为 4，步长为 2

You will likely need a larger overlap if accuracy and preserving semanatic context are more important than minimizing token inputs or the number of requests made to an LLM.  
如果准确性和保留语义上下文比最小化令牌输入或对 LLM 发出的请求数量更重要，则可能需要更大的重叠。

[Example 3-5](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#ex-3-5) shows how you can implement a sliding window using Python’s `len()` function. The `len()` function provides us with the total number of characters in a given text string, which subsequently aids in defining the parameters of our sliding windows.  
示例 3-5 展示了如何使用 Python 的 `len()` 函数实现滑动窗口。 `len()` 函数为我们提供了给定文本字符串中的字符总数，这随后有助于定义滑动窗口的参数。

##### Example 3-5. [Sliding window](https://oreil.ly/aCkDo)  
例 3-5.推拉窗

```

def

```

This code outputs: 此代码输出：

Chunk 1: This is an example o
Chunk 2: is an example of sli
Chunk 3:  example of sliding
Chunk 4: ple of sliding windo
Chunk 5: f sliding window tex
Chunk 6: ding window text chu
Chunk 7: window text chunking

In the context of prompt engineering, the sliding window approach offers several benefits over fixed chunking methods. It allows LLMs to retain a higher degree of context, as there is an overlap between the chunks and offers an alternative approach to preserving context compared to sentence detection.  
在提示工程的背景下，与固定分块方法相比，滑动窗口方法具有多种优势。它允许 LLMs 保留更高程度的上下文，因为块之间存在重叠，并且与句子检测相比，提供了一种保留上下文的替代方法。

# Text Chunking Packages 文本分块包

When working with LLMs such as GPT-4, always remain wary of the maximum context length:  
使用 LLMs（例如 GPT-4）时，请始终警惕最大上下文长度：

- `maximum_context_length = input_tokens + output_tokens`

There are various tokenizers available to break your text down into manageable units, the most popular ones being NLTK, spaCy, and tiktoken.  
有各种标记器可用于将您的文本分解为可管理的单元，最受欢迎的是 NLTK、spaCy 和 tiktoken。

Both [NLTK](https://oreil.ly/wTmI7) and [spaCy](https://oreil.ly/c4MvQ) provide comprehensive support for text processing, but you’ll be focusing on tiktoken.  
NLTK 和 spaCy 都为文本处理提供全面的支持，但您将专注于 tiktoken。

# Text Chunking with Tiktoken  
使用 Tiktoken 进行文本分块

[Tiktoken](https://oreil.ly/oSpVe) is a fast _byte pair encoding (BPE)_ tokenizer that breaks down text into subword units and is designed for use with OpenAI’s models. Tiktoken offers faster performance than comparable open source tokenizers.  
Tiktoken 是一种快速字节对编码 （BPE） 分词器，可将文本分解为子字单元，专为与 OpenAI 的模型一起使用而设计。Tiktoken 提供比同类开源标记器更快的性能。

As a developer working with GPT-4 applications, using tiktoken offers you several key advantages:  
作为使用 GPT-4 应用程序的开发人员，使用 tiktoken 为您提供了几个关键优势：

Accurate token breakdown  
准确的令牌细分

It’s crucial to divide text into tokens because GPT models interpret text as individual tokens. Identifying the number of tokens in your text helps you figure out whether the text is too lengthy for a model to process.  
将文本划分为标记至关重要，因为 GPT 模型将文本解释为单个标记。识别文本中的标记数有助于确定文本是否太长而无法处理模型。

Effective resource utilization  
有效利用资源

Having the correct token count enables you to manage resources efficiently, particularly when using the OpenAI API. Being aware of the exact number of tokens helps you regulate and optimize API usage, maintaining a balance between costs and resource usage.  
拥有正确的令牌计数使您能够有效地管理资源，尤其是在使用 OpenAI API 时。了解令牌的确切数量有助于调节和优化 API 使用，从而在成本和资源使用之间保持平衡。

# Encodings 编码

Encodings define the method of converting text into tokens, with different models utilizing different encodings. Tiktoken supports three encodings commonly used by OpenAI models:  
编码定义了将文本转换为标记的方法，不同的模型使用不同的编码。Tiktoken 支持 OpenAI 模型常用的三种编码：

|Encoding name 编码名称|OpenAI models OpenAI 模型|
|---|---|
|cl100k_base|GPT-4, GPT-3.5-turbo, text-embedding-ada-002  <br>GPT-4、GPT-3.5-turbo、文本嵌入-ada-002|
|p50k_base|Codex models, text-davinci-002, text-davinci-003  <br>法典模型，text-davinci-002，text-davinci-003|
|r50k_base (or gpt2) r50k_base（或 GPT2）|GPT-3 models like davinci  <br>GPT-3 模型，如达芬奇|

## Understanding the Tokenization of Strings  
了解字符串的标记化

In English, tokens can vary in length, ranging from a single character like _t_, to an entire word such as _great_. This is due to the adaptable nature of tokenization, which can accommodate even tokens shorter than a character in complex script languages or tokens longer than a word in languages without spaces or where phrases function as single units.  
在英语中，标记的长度可以有所不同，从单个字符（如 t）到整个单词（如 great）不等。这是由于标记化的适应性，它甚至可以容纳复杂脚本语言中比字符短的标记，或者在没有空格或短语作为单个单元使用的语言中比单词长的标记。

It is not uncommon for spaces to be included within tokens, such as `"is"` rather than `"is "` or `" "+"is"`. This practice helps maintain the original text formatting and can capture specific linguistic characteristics.  
在标记中包含空格的情况并不少见，例如 `"is"` 而不是 `"is "` 或 `" "+"is"` 。这种做法有助于保持原始文本格式，并可以捕获特定的语言特征。

###### NOTE 注意

To easily examine the tokenization of a string, you can use [OpenAI Tokenizer](https://oreil.ly/K6ZQK).  
要轻松检查字符串的标记化，您可以使用 OpenAI Tokenizer。

You can install [tiktoken from PyPI](https://oreil.ly/HA2QD) with `pip install` `tiktoken`. In the following example, you’ll see how to easily encode text into tokens and decode tokens into text:  
你可以用 `pip install` `tiktoken` 从 PyPI 安装 tiktoken。在以下示例中，你将了解如何轻松地将文本编码为令牌，以及如何将令牌解码为文本：

```

# Import the package:

```

Additionally let’s write a function that will tokenize the text and then count the number of tokens given a `text_string` and `encoding_name`.  
此外，让我们编写一个函数来标记文本，然后计算给定 `text_string` 和 `encoding_name` 的标记数。

```

def

```

This code outputs `8`.  
此代码输出 `8` 。

# Estimating Token Usage for Chat API Calls  
估计聊天 API 调用的令牌使用情况

ChatGPT models, such as GPT-3.5-turbo and GPT-4, utilize tokens similarly to previous completion models. However, the message-based structure makes token counting for conversations more challenging:  
ChatGPT 模型，例如 GPT-3.5-turbo 和 GPT-4，使用与以前的完成模型类似的代币。但是，基于消息的结构使对话的令牌计数更具挑战性：

```

def

```

[Example 3-6](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#ex-3-6) highlights the specific structure required to make a request against any of the chat models, which are currently GPT-3x and GPT-4.  
示例 3-6 重点介绍了针对任何聊天模型（当前为 GPT-3x 和 GPT-4）发出请求所需的特定结构。

Normally, chat history is structured with a `system` message first, and then succeeded by alternating exchanges between the `user` and the `assistant`.  
通常，聊天记录首先使用 `system` 消息构建，然后通过 `user` 和 `assistant` 之间的交替交换来成功。

##### Example 3-6. A payload for the Chat Completions API on OpenAI  
例 3-6.OpenAI 上聊天完成 API 的有效负载

```

example_messages

```

`"role": "system"` describes a system message that’s useful for _providing prompt instructions_. It offers a means to tweak the assistant’s character or provide explicit directives regarding its interactive approach. It’s crucial to understand, though, that the system command isn’t a prerequisite, and the model’s default demeanor without a system command could closely resemble the behavior of “You are a helpful assistant.”  
`"role": "system"` 描述可用于提供提示说明的系统消息。它提供了一种调整助手角色或提供有关其交互方法的明确指令的方法。但是，重要的是要了解系统命令不是先决条件，并且没有系统命令的模型的默认举止可能与“你是一个有用的助手”的行为非常相似。

The roles that you can have are `["system", "user", "assistant"]`.  
您可以拥有的角色是 `["system", "user", "assistant"]` 。

`"content": "Some content"` is where you place the prompt or responses from a language model, depending upon the message’s role. It can be either `"assistant"`, `"system"`, or `"user"`.  
`"content": "Some content"` 是放置提示或来自语言模型的响应的位置，具体取决于消息的角色。它可以是 `"assistant"` ， `"system"` 或 `"user"` 。

# Sentiment Analysis 情绪分析

_Sentiment analysis_ is a widely used NLP technique that helps in identifying, extracting, and understanding the emotions, opinions, or sentiments expressed in a piece of text. By leveraging the power of LLMs like GPT-4, sentiment analysis has become an essential tool for businesses, researchers, and developers across various industries.  
情感分析是一种广泛使用的 NLP 技术，有助于识别、提取和理解一段文本中表达的情绪、观点或情感。通过利用 GPT-4 等 LLMs 的强大功能，情感分析已成为各行各业的企业、研究人员和开发人员的重要工具。

The primary goal of sentiment analysis is to determine the attitude or emotional tone conveyed in a text, whether it’s positive, negative, or neutral. This information can provide valuable insights into consumer opinions about products or services, help monitor brand reputation, and even assist in predicting market trends.  
情感分析的主要目标是确定文本中传达的态度或情感基调，无论是积极的、消极的还是中立的。这些信息可以为消费者对产品或服务的意见提供有价值的见解，帮助监控品牌声誉，甚至帮助预测市场趋势。

The following are several prompt engineering techniques for creating effective sentiment analysis prompts:  
以下是用于创建有效情绪分析提示的几种提示工程技术：

Input: 输入：

Is this text positive or negative?

I absolutely love the design of this phone, but the battery life is quite
disappointing.

Output: 输出：

The text has a mixed tone, as it contains both positive and negative
aspects. The positive part is "I absolutely love the design of this phone,"
while the negative part is "the battery life is quite disappointing."

Although GPT-4 identifies a “mixed tone,” the outcome is a result of several shortcomings in the prompt:  
尽管 GPT-4 识别出“混合语气”，但结果是提示中几个缺点的结果：

Lack of clarity 缺乏明确性

The prompt does not clearly define the desired output format.  
提示符未明确定义所需的输出格式。

Insufficient examples 示例不足

The prompt does not include any examples of positive, negative, or neutral sentiments, which could help guide the LLM in understanding the distinctions between them.  
该提示不包括任何积极、消极或中立情绪的示例，这可能有助于指导 LLM 理解它们之间的区别。

No guidance on handling mixed sentiments  
没有关于处理混合情绪的指导

The prompt does not specify how to handle cases where the text contains a mix of positive and negative sentiments.  
提示没有指定如何处理文本包含积极和消极情绪混合的情况。

Input: 输入：

Using the following examples as a guide:
positive: 'I absolutely love the design of this phone!'
negative: 'The battery life is quite disappointing.'
neutral: 'I liked the product, but it has short battery life.'

Only return either a single word of:
- positive
- negative
- neutral

Please classify the sentiment of the following text as positive, negative,
or neutral: I absolutely love the design of this phone, but the battery
life is quite disappointing.

Output: 输出：

neutral

This prompt is much better because it:  
这个提示要好得多，因为它：

Provides clear instructions  
提供清晰的说明

The prompt clearly states the task, which is to classify the sentiment of the given text into one of three categories: positive, negative, or neutral.  
提示清楚地说明了任务，即将给定文本的情绪分为三类之一：积极、消极或中立。

Offers examples 提供示例

The prompt provides examples for each of the sentiment categories, which helps in understanding the context and desired output.  
该提示为每个情绪类别提供了示例，这有助于理解上下文和所需的输出。

Defines the output format  
定义输出格式

The prompt specifies that the output should be a single word, ensuring that the response is concise and easy to understand.  
提示指定输出应为单个单词，确保响应简洁易懂。

## Techniques for Improving Sentiment Analysis  
改进情绪分析的技术

To enhance sentiment analysis accuracy, preprocessing the input text is a vital step. This involves the following:  
为了提高情感分析的准确性，对输入文本进行预处理是一个至关重要的步骤。这涉及以下内容：

Special characters removal  
特殊字符删除

Exceptional characters such as emojis, hashtags, and punctuation may skew the rule-based sentiment algorithm’s judgment. Besides, these characters might not be recognized by machine learning and deep learning models, resulting in misclassification.  
表情符号、主题标签和标点符号等特殊字符可能会扭曲基于规则的情感算法的判断。此外，机器学习和深度学习模型可能无法识别这些字符，从而导致分类错误。

Lowercase conversion 小写转换

Converting all the characters to lowercase aids in creating uniformity. For instance, words like _Happy_ and _happy_ are treated as different words by models, which can cause duplication and inaccuracies.  
将所有字符转换为小写有助于创建统一性。例如，像“快乐”和“快乐”这样的词被模型视为不同的词，这可能会导致重复和不准确。

Spelling correction 拼写更正

Spelling errors can cause misinterpretation and misclassification. Creating a spell-check pipeline can significantly reduce such errors and improve results.  
拼写错误可能会导致误解和错误分类。创建拼写检查管道可以显著减少此类错误并改善结果。

For industry- or domain-specific text, embedding domain-specific content in the prompt helps in navigating the LLM’s sense of the text’s framework and sentiment. It enhances accuracy in the classification and provides a heightened understanding of particular jargon and expressions.  
对于特定于行业或领域的文本，在提示中嵌入特定于领域的内容有助于导航 LLM 对文本框架和情绪的理解。它提高了分类的准确性，并提供了对特定行话和表达方式的更高理解。

## Limitations and Challenges in Sentiment Analysis  
情感分析的局限性和挑战

Despite the advancements in LLMs and the application of prompt engineering techniques, sentiment analysis still faces some limitations and challenges:  
尽管 LLMs 取得了进步，并应用了提示工程技术，但情感分析仍然面临一些限制和挑战：

Handling sarcasm and irony  
处理讽刺和讽刺

Detecting sarcasm and irony in text can be difficult for LLMs, as it often requires understanding the context and subtle cues that humans can easily recognize. Misinterpreting sarcastic or ironic statements may lead to inaccurate sentiment classification.  
对于LLMs来说，检测文本中的讽刺和讽刺可能很困难，因为它通常需要了解人类可以轻松识别的上下文和微妙的线索。误解讽刺或讽刺的陈述可能会导致不准确的情绪分类。

Identifying context-specific sentiment  
识别特定于上下文的情绪

Sentiment analysis can be challenging when dealing with context-specific sentiments, such as those related to domain-specific jargon or cultural expressions. LLMs may struggle to accurately classify sentiments in these cases without proper guidance or domain-specific examples.  
在处理特定于上下文的情绪时，例如与特定领域术语或文化表达相关的情绪，情绪分析可能具有挑战性。LLMs 在这些情况下，如果没有适当的指导或特定领域的示例，可能很难准确地对情绪进行分类。

# Least to Most 从最少到最多

The _least to most_ technique in prompt engineering is a powerful method for sequentially generating or extracting increasingly detailed knowledge on a given topic. This method is particularly effective when dealing with complex subjects or when a high level of detail is necessary.  
提示工程中的最小到大多数技术是一种强大的方法，用于按顺序生成或提取有关给定主题的越来越详细的知识。这种方法在处理复杂的主题或需要高度详细时特别有效。

Least to most uses a _chain_ of prompts where each new prompt is based on the last answer. This step-by-step approach helps gather more detailed information each time, making it easier to dive deeper into any topic.  
从最少到大多数使用一连串提示，其中每个新提示都基于最后一个答案。这种循序渐进的方法有助于每次收集更详细的信息，从而更容易更深入地研究任何主题。

This technique can also be applied to code generation, as demonstrated in a Flask `Hello World` app example.  
此技术也可以应用于代码生成，如 Flask `Hello World` 应用示例中所示。

## Planning the Architecture  
规划体系结构

Before diving into the architecture, let’s briefly understand what Flask is. [Flask](https://oreil.ly/7N-bs) is a lightweight web application framework in Python, widely used for creating web applications quickly and with minimal code. (Flask is only used for demonstration purposes here and isn’t included within the [_requirements.txt_ file](https://oreil.ly/TRK0i) for the book.  
在深入研究架构之前，让我们简要了解一下 Flask 是什么。Flask 是 Python 中的轻量级 Web 应用程序框架，广泛用于以最少的代码快速创建 Web 应用程序。（此处仅用于演示目的，未包含在本书的requirements.txt文件中。

Now, let’s ask an LLM to outline the basic architecture for a simple Flask “Hello World” application.  
现在，让我们请 LLM 概述一个简单的 Flask “Hello World” 应用程序的基本架构。

Input: 输入：

Outline the basic architecture for a simple Flask "Hello World" application.

Output: 输出：

Sure! Here's an outline for a basic Flask "Hello World" application:

Import Flask module: Import the Flask module
to use its ((("Flask module code generation")))functionality.

Create an instance of the Flask application: Create an instance of the
Flask class to represent your web application.
Define a route and view function: ...
Implement the view function: ...
Run the application: Start the Flask development server to run the application.

## Coding Individual Functions  
对单个函数进行编码

Before coding, let’s clarify what a Flask route is: it’s a function linked to a URL pattern that determines what users see on a specific web page. Next, we’ll provide the code snippet for a simple “Hello World” route in Flask.  
在编码之前，让我们澄清一下 Flask 路由是什么：它是一个链接到 URL 模式的函数，用于确定用户在特定网页上看到的内容。接下来，我们将在 Flask 中提供简单的“Hello World”路由的代码片段。

Input: 输入：

Provide a code snippet for a simple "Hello World" route in Flask.

Output: 输出：

Certainly! Here's a simple code snippet for a "Hello World" route using Flask:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

In this code, we import the Flask module and create a Flask application instance named `app`. We then define a route using the `@app.route` decorator, specifying the root URL path `'/'`. The `hello_world` function is associated with this route, and it returns the string `'Hello, World!'` as the response.  
在此代码中，我们导入 Flask 模块并创建一个名为 `app` 的 Flask 应用程序实例。然后，我们使用 `@app.route` 装饰器定义路由，指定根 URL 路径 `'/'` 。 `hello_world` 函数与此路由相关联，它返回字符串 `'Hello, World!'` 作为响应。

The Flask application will start by calling `app.run()` when your Python script is executed directly.  
当直接执行 Python 脚本时，Flask 应用程序将通过调用 `app.run()` 启动。

## Adding Tests 添加测试

Finally, let’s ask it to generate a test case for the “Hello World” route in the Flask application.  
最后，让我们要求它在 Flask 应用程序中为“Hello World”路由生成一个测试用例。

Input: 输入：

Provide an example of a test case for the "Hello World" route in a Flask
application.

Output: 输出：

Sure! Here's an example of a test case for the "Hello World" route in a
Flask application:

import unittest
from flask import Flask
from flask.testing import FlaskClient

# Create the Flask application
app = Flask(__name__)

# Create the route
@app.route('/')
def hello_world():
    return 'Hello, World!'

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_hello_world_route(self):
        # Send a GET request to the route
        response = self.app.get('/')

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()

By using the least to most prompt technique, you can gradually build up the knowledge and understanding required for the task at hand.  
通过使用最少到最及时的技术，您可以逐渐建立手头任务所需的知识和理解。

## Benefits of the Least to Most Technique  
从最少到最多技术的好处

This method is particularly useful for complex tasks, as it allows an LLM to generate relevant knowledge that will subsequently be used as context for future tasks.  
此方法对于复杂任务特别有用，因为它允许 LLM 生成相关知识，这些知识随后将用作未来任务的上下文。

Let’s dive deeper into the benefits of using this approach in various other scenarios:  
让我们更深入地了解在其他各种方案中使用此方法的好处：

Progressive exploration 渐进式探索

Breaking a complex problem into smaller tasks allows an LLM to provide more detailed and accurate information at each step. This approach is especially helpful when working with a new subject matter or a multifaceted problem.  
将复杂的问题分解为更小的任务允许 LLM 在每个步骤中提供更详细和准确的信息。这种方法在处理新主题或多方面问题时特别有用。

Flexibility 灵活性

The least to most technique offers flexibility in addressing different aspects of a problem. It enables you to pivot, explore alternative solutions, or dive deeper into specific areas as needed.  
从最少到最多的技术在解决问题的不同方面提供了灵活性。它使您能够根据需要进行调整、探索替代解决方案或深入研究特定领域。

Improved comprehension 提高理解力

By breaking down a task into smaller steps, an LLM can deliver information in a more digestible format, making it easier for you to understand and follow.  
通过将任务分解为更小的步骤，LLM 可以以更易于理解的格式传递信息，让您更容易理解和遵循。

Collaborative learning 协作学习

This technique promotes collaboration between you and an LLM, as it encourages an iterative process of refining the output and adjusting your responses to achieve the desired outcome.  
这种技术促进了你和LLM之间的协作，因为它鼓励一个迭代过程来完善输出和调整你的响应，以实现预期的结果。

## Challenges with the Least to Most Technique  
从最少到最多的技术挑战

Overreliance on previously generated knowledge  
过度依赖先前生成的知识

Using previous chat history to store the state may lead to larger tasks forgetting their initial tasks/outputs due to limitations in context length.  
由于上下文长度的限制，使用以前的聊天历史记录来存储状态可能会导致较大的任务忘记其初始任务/输出。

Dependence on prior prompts  
对先前提示的依赖性

Since each prompt is built upon preceding outputs, it is imperative to ensure that the quality and responses of previous prompts provide ample information for the next step.  
由于每个提示都是基于前面的输出构建的，因此必须确保先前提示的质量和响应为下一步提供充足的信息。

# EVALUATE QUALITY 评估质量

In the process of designing prompts, make sure to evaluate the quality of each prior LLM response. The performance of the next task depends upon the quality of information provided by the preceding one.  
在设计提示的过程中，一定要评估每个先前的LLM响应的质量。下一个任务的执行取决于前一个任务提供的信息的质量。

# Role Prompting 角色提示

_Role prompting_ is a technique in which the AI is given a specific role or character to assume while generating a response. This helps guide the AI’s response style and content to better align with the user’s needs or desired outcome.  
角色提示是一种技术，在这种技术中，人工智能在生成响应时被赋予特定的角色或角色。这有助于指导 AI 的响应风格和内容更好地与用户的需求或期望的结果保持一致。

###### NOTE 注意

[Awesome ChatGPT prompts](https://oreil.ly/8pf40) provides an extensive list of role prompts that you can use.  
很棒的 ChatGPT 提示提供了您可以使用的大量角色提示列表。

Let’s ask ChatGPT to take on the role of a tech reviewer for MongoDB.  
让我们让 ChatGPT 扮演 MongoDB 的技术评论员的角色。

Input: 输入：

I want you to act as a tech reviewer. I will give you the name of a piece
of technology and you will provide me with an in-depth review - including
pros, cons, features, and comparisons to other technologies on the market.
My first suggestion request is: MongoDB.

Output: 输出：

MongoDB is a popular NoSQL, document-oriented database management system
designed to handle high-volume data storage and retrieval.

Features:

1. Document-Oriented Storage: MongoDB stores data in a flexible, JSON-like
format called BSON, making it easy to store complex data structures like
arrays and nested objects.
...

Pros:
1. High Performance: MongoDB's indexing and caching capabilities deliver
fast read and write operations.
...

Cons:
1. Limited Support for Transactions: While MongoDB supports multidocument
ACID transactions, it may not be the best choice for applications that
require complex transactional operations.
...

Comparisons to other technologies:
1. Couchbase, another popular NoSQL database, offers similar features to
MongoDB, including flexible schema and JSON-based storage. However,
Couchbase is more focused on distributed caching and may be more
suitable for applications requiring low-latency data access.

Conclusion:

MongoDB is a powerful and versatile NoSQL database solution suitable for
various applications, particularly those requiring high performance and
scalability. Its flexible data model, rich query language, and strong
consistency make it a popular choice among developers.

The prompt is an excellent example of role prompting, as it clearly defines the role the AI should assume (a tech reviewer) and sets expectations for the type of response desired (an in-depth review of MongoDB).  
提示是角色提示的一个很好的例子，因为它清楚地定义了 AI 应该承担的角色（技术审查者），并为所需的响应类型设定了期望（对 MongoDB 的深入审查）。

# GIVE DIRECTION 指明方向

When crafting prompts, consider assigning a specific role to the AI. This sets the proper context for the response, creating a more focused and relevant output.  
在制作提示时，请考虑为 AI 分配特定角色。这为响应设置了适当的上下文，从而创建了更有针对性和相关性的输出。

# Benefits of Role Prompting  
角色提示的好处

Role prompting helps narrow down the AI’s responses, ensuring more focused, contextually appropriate, and tailored results. It can also enhance creativity by pushing the AI to think and respond from unique perspectives.  
角色提示有助于缩小 AI 的响应范围，确保更集中、更符合上下文和量身定制的结果。它还可以通过推动人工智能从独特的角度思考和响应来增强创造力。

# Challenges of Role Prompting  
角色提示的挑战

Role prompting can pose certain challenges. There might be potential risks for bias or stereotyping based on the role assigned. Assigning stereotyped roles can lead to generating biased responses, which could harm usability or offend individuals. Additionally, maintaining consistency in the role throughout an extended interaction can be difficult. The model might drift off-topic or respond with information irrelevant to the assigned role.  
角色提示可能会带来某些挑战。根据分配的角色，可能存在偏见或刻板印象的潜在风险。分配刻板的角色可能会导致产生有偏见的反应，这可能会损害可用性或冒犯个人。此外，在整个扩展交互过程中保持角色的一致性可能很困难。模型可能会偏离主题，或者使用与分配的角色无关的信息进行响应。

# EVALUATE QUALITY 评估质量

Consistently check the quality of the LLM’s responses, especially when role prompting is in play. Monitor if the AI is sticking to the role assigned or if it is veering off-topic.  
始终如一地检查 LLM 响应的质量，尤其是在角色提示起作用时。监控 AI 是否坚持分配的角色，或者是否偏离主题。

# When to Use Role Prompting  
何时使用角色提示

Role prompting is particularly useful when you want to:  
角色提示在以下情况下特别有用：

Elicit specific expertise  
获取特定专业知识

If you need a response that requires domain knowledge or specialized expertise, role prompting can help guide the LLM to generate more informed and accurate responses.  
如果您需要需要领域知识或专业知识的响应，角色提示可以帮助指导 LLM 生成更明智、更准确的响应。

Tailor response style 量身定制的响应方式

Assigning a role can help an LLM generate responses that match a specific tone, style, or perspective, such as a formal, casual, or humorous response.  
分配角色可以帮助 LLM 生成与特定语气、风格或观点相匹配的响应，例如正式、随意或幽默的响应。

Encourage creative responses  
鼓励创造性的回应

Role prompting can be used to create fictional scenarios or generate imaginative answers by assigning roles like a storyteller, a character from a novel, or a historical figure.  
角色提示可用于创建虚构场景或通过分配讲故事的人、小说中的人物或历史人物等角色来生成富有想象力的答案。

- _Explore diverse perspectives_: If you want to explore different viewpoints on a topic, role prompting can help by asking the AI to assume various roles or personas, allowing for a more comprehensive understanding of the subject.  
    探索不同的观点：如果您想探索某个主题的不同观点，角色提示可以通过要求 AI 扮演各种角色或角色来提供帮助，从而更全面地了解该主题。
    
- _Enhance user engagement_: Role prompting can make interactions more engaging and entertaining by enabling an LLM to take on characters or personas that resonate with the user.  
    增强用户参与度：角色提示可以使 LLM 扮演与用户产生共鸣的角色或角色，从而使交互更具吸引力和娱乐性。
    

If you’re using OpenAI, then the best place to add a role is within the `System Message` for chat models.  
如果您使用的是 OpenAI，那么添加角色的最佳位置是在聊天模型的 `System Message` 中。

# GPT Prompting Tactics GPT 提示策略

So far you’ve already covered several prompting tactics, including asking for context, text style bundling, least to most, and role prompting.  
到目前为止，您已经介绍了几种提示策略，包括询问上下文、文本样式捆绑、从少到多和角色提示。

Let’s cover several more tactics, from managing potential hallucinations with appropriate reference text, to providing an LLM with critical _thinking time_, to understanding the concept of _task decomposition_—we have plenty for you to explore.  
让我们介绍更多的策略，从使用适当的参考文本管理潜在的幻觉，到提供具有批判性思维时间的LLM，再到理解任务分解的概念——我们有很多可供您探索的地方。

These methodologies have been designed to significantly boost the precision of your AI’s output and are recommended by [OpenAI](https://oreil.ly/QZE8n). Also, each tactic utilizes one or more of the prompt engineering principles discussed in [Chapter 1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#five_principles_01).  
这些方法旨在显着提高 AI 输出的精度，并被 OpenAI 推荐。此外，每种策略都利用了第 1 章中讨论的一个或多个提示工程原则。

## Avoiding Hallucinations with Reference  
参考避免幻觉

The first method for avoiding text-based hallucinations is to instruct the model to _only answer using reference text._  
避免基于文本的幻觉的第一种方法是指示模型仅使用参考文本进行回答。

By supplying an AI model with accurate and relevant information about a given query, the model can be directed to use this information to generate its response.  
通过向 AI 模型提供有关给定查询的准确且相关的信息，可以指示模型使用此信息来生成其响应。

Input: 输入：

Refer to the articles enclosed within triple quotes to respond to queries.

You must follow the following principles:
- In cases where the answer isn't found within these articles, simply
return "I could not find an answer".

"""
B2B clients tend to have longer decision-making processes, and thus longer
sales funnels. Relationship-building strategies work better for these
clients, whereas B2C customers tend to respond better to short-term offers
and messages.
"""

Example responses:
- I could not find an answer.
- Yes, B2B clients tend to have longer decision-making processes, and thus
longer sales funnels.

Output: 输出：

Yes, B2B clients tend to have longer decision-making processes, which leads
to longer sales cycles.

If you were to ask the same reference text this question:  
如果你要问同样的参考文本，这个问题：

Input: 输入：

...The rest of the prompt...

Question: Are B2C sales more cost-effective?

Output: 输出：

I could not find an answer.

# GIVE DIRECTION AND SPECIFY FORMAT  
给出方向并指定格式

The preceding prompt is excellent as it both instructs the model on how to find answers and also sets a specific response format for any unanswerable questions.  
前面的提示非常好，因为它既指导模型如何查找答案，又为任何无法回答的问题设置特定的响应格式。

Considering the constrained context windows of GPTs, a method for dynamically retrieving information relevant to the asked query might be necessary to utilize this strategy.  
考虑到 GPT 的受限上下文窗口，可能需要一种动态检索与所请求查询相关的信息的方法才能利用此策略。

Another approach is to direct the model to _incorporate references_ from a given text in its response. When the input is enhanced with relevant information, the model can be guided to include citations in its responses by referring to sections of the supplied documents. This approach has the added benefit that citations in the output can be _authenticated automatically by matching strings_ within the given documents.  
另一种方法是指示模型在其响应中合并来自给定文本的引用。当输入得到相关信息的增强时，可以指导模型通过参考所提供文档的各个部分在其响应中包含引文。这种方法还有一个额外的好处，即可以通过匹配给定文档中的字符串来自动验证输出中的引文。

Input: 输入：

You will be provided with a document delimited by triple quotes and a
question. Your task is to answer the question using only the provided
document and to cite the passage(s) of the document used to answer the
question. If the document does not contain the information needed to answer
this question then simply write: "Insufficient information." If an answer
to the question is provided, it must be annotated with a citation. Use the
following format to cite relevant passages ({"citation": …}).

"""
A nuclear reactor is a device that initiates, controls, and maintains a
nuclear chain reaction. The nuclear reactor uses the energy released by
nuclear fission to generate heat, which is then often used to produce steam
to drive a turbine and produce electricity.

-Excerpted from https://en.wikipedia.org/wiki/Nuclear_reactor
"""

Question: What is a nuclear reactor?

Output: 输出：

A nuclear reactor is a device that initiates, controls, and maintains a
nuclear chain reaction.It uses the energy released by nuclear fission to
generate heat, which is then often used to produce steam to drive a turbine
and produce electricity. {"citation": "A nuclear reactor is a device that
initiates, controls, and maintains a nuclear chain reaction. The nuclear
reactor uses the energy released by nuclear fission to generate heat, which
is then often used to produce steam to drive a turbine and produce
electricity."}

## Give GPTs “Thinking Time”  
给 GPT “思考时间”

Often, by explicitly guiding an LLM to _derive solutions from first principles_ before reaching a verdict, you can garner more accurate responses. Providing an LLM with _thinking time_ can often lead to better results.  
通常，通过明确引导 LLM 在做出判决之前从第一性原理中得出解决方案，您可以获得更准确的响应。为LLM提供思考时间通常可以带来更好的结果。

Input: 输入：

First, try to solve the problem on your own. Then, see if your answer
matches the proposed solution. Don't judge the given answer until you've
tried solving it yourself.

Problem:
Jane has 5 apples, then John takes 2 from Mary. Mary originally had 15
apples. John then gives his apples to Jane.

How many apples does Jane have?

Proposed solution:
1. Janes originally had 5 apples.
2. John takes 2 apples from Mary, but this doesn't affect Jane's count.
3. John then gives his apples to Jane.

So, Jane's final count of apples is her original 5 apples plus the 2 apples
that John gave her, for a total of 7 apples.

Output: 输出：

Let's break down the problem:

1. Jane originally has 5 apples.
2. John takes 2 apples from Mary. However, this action doesn't directly
impact the number of apples Jane has at this point.
3. John gives his apples to Jane.

Following these steps, we need to add the 2 apples John gave to Jane to
Jane's original number of apples. Therefore:

5 apples (Jane's original number) + 2 apples (given by John) = 7 apples

So, Jane now has 7 apples. My solution matches the proposed solution.

In some cases, when using GPT-4 or other generative AI models, you may not want the model’s reasoning process to be visible to the user.  
在某些情况下，在使用 GPT-4 或其他生成式 AI 模型时，您可能不希望用户看到模型的推理过程。

You can achieve this by asking an LLM to _generate an inner monologue_. This is particularly useful in tutoring applications, where revealing the model’s reasoning might give away the solution prematurely.  
你可以通过要求LLM生成内心独白来实现这一点。这在辅导应用程序中特别有用，在这些应用程序中，揭示模型的推理可能会过早地泄露解决方案。

## The Inner Monologue Tactic  
内心独白策略

The _inner monologue tactic_ instructs the model to structure parts of the output that should be hidden from the user in a specific format. This makes it easy to remove these parts before presenting the final output to the user.  
内心独白策略指示模型构建输出中应以特定格式对用户隐藏的部分。这样就可以在向用户呈现最终输出之前轻松移除这些部件。

Here’s how you can utilize this tactic to answer user queries effectively.  
以下是如何利用此策略有效地回答用户查询的方法。

Input: 输入：

Step 1: Solve the Problem

First, you need to work out your solution to the problem. Be sure not to
rely on the user's solution, as it might be incorrect. You can encapsulate
your workings within triple quotes (`"""`) to indicate that this section
should be hidden.

Step 2: Compare Solutions

Next, compare your solution with the user's solution. Evaluate whether the
user's solution is correct or not. Again, encapsulate this section within
triple quotes (`"""`).

Step 3: Prepare a Hint

If the user made a mistake, determine an appropriate hint that can help
guide them toward the correct answer, without giving it away outright.
This section should also be within triple quotes (`"""`).

Step 4: Deliver the Hint

If a mistake was made, present the hint from the previous step to the user.
Remember not to use triple quotes for this step. Instead of using a title
like "Step 4", use a heading such as `Hint:`

Problem Statement: A deck of cards has 52 cards: 13 hearts, 13 diamonds, 13
clubs, and 13 spades. If two cards are drawn from the deck without
replacement, what is the probability that one of the drawn cards is a heart
and the other one is a club?

User's Solution: (13/52)*(13/51) = 169/2652 = 13/204

Output: 输出：

"""
Step 1 - My Solution:

First, calculate the probability of drawing 1 heart and 1 club from a
deck of 52 cards without replacement.

In the first draw, the probability of drawing a heart is 13/52.

For the second draw, after removing 1 card (assuming it's a heart), the
total number of cards becomes 51. So, the probability of drawing a club now
is 13/51.

Multiplying these two probabilities gives the probability of both events
happening in sequence,which is P(Heart then Club) = (13/52)*(13/51).

Repeat the calculation assuming the first drawn card is a club and the
second drawn card is a heart. Remember, order matters in this case as
we're dealing with separate events.
"""
"""
Step 2 - Comparison with the User's Solution:

Compare your solution with the user's solution. The user's solution only
considers the sequence of drawing a heart first and then a club. They
have not accounted for the alternate sequence  (Club then Heart), and
thus, the solution is incomplete.
"""
"""
Step 3 - Preparation of Hint:

Given that the user hasn't considered both sequences (Heart then Club
and Club then Heart), a hint at the consideration of both possible
sequences will be helpful. This could nudge the user in the right
direction without revealing the solution outright.
"""

# Step 4 - Delivery of Hint:

# Hint: Remember that the two cards could be drawn in any order. Consider
both possible sequences: Heart then Club and Club then Heart.

## Self-Eval LLM Responses 自我评估 LLM 响应

Another tactic you can use is to _critque a generated LLM output_ and ask whether the LLM missed any information or important facts. You’re essentially asking an LLM to _evaluate itself_ based on its previous output.  
您可以使用的另一种策略是批评生成的 LLM 输出，并询问 LLM 是否遗漏了任何信息或重要事实。您实际上是在要求 LLM 根据其先前的输出来评估自己。

First, create a prompt to generate a `"Hello World"` function.  
首先，创建一个提示来生成一个 `"Hello World"` 函数。

Input: 输入：

Generate a "Hello World" Python function.

Output: 输出：

Sure, here's a very simple Python function that prints "Hello, World!" to
the console:

def print_hello_world():
    print("Hello, World!")

print_hello_world()

When you run this function, it will print the string "Hello, World!" to the
console.

The LLM returns a simple Python function called `print_hello_world()` that prints the traditional “Hello, World!” greeting.  
LLM 返回一个名为 `print_hello_world()` 的简单 Python 函数，该函数打印传统的“Hello， World！”问候语。

Then make a second LLM request with the previous chat history, asking for the initial output to be improved.  
然后使用之前的聊天记录发出第二个 LLM 请求，要求改进初始输出。

Input: 输入：

...Previous Chat History...

Given the previous function, can you improve it again with anything else?
Perhaps defaults or type hints?

Output: 输出：

We can add type hints to make it clear that the function doesn't take any
arguments and doesn't return anything. We can also add a docstring to
describe what the function does.

Here's the improved code:

def print_hello_world() -> None:
    """
    Prints "Hello, World!" to the standard output.
    """
    print("Hello, World!")

If you wanted to make the function more flexible, you could add a default
argument that allows you to print a different message:

def print_message(message: str = "Hello, World!") -> None:
    """
    Prints the given message to the standard output. If no message is given
    , it defaults to "Hello, World!".

    Args:
        message (str, optional): The message to be printed.
        Defaults to "Hello, World!".
    """
    print(message)

Consequently GPT-4 returns an upgraded version of the function, now furnished with Python type hints and a default argument. This enriches the function with greater flexibility, allowing it to print not just `"Hello, World!"` but any user-specified message.  
因此，GPT-4 返回该函数的升级版本，现在提供 Python 类型提示和默认参数。这以更大的灵活性丰富了该功能，使其不仅可以打印 `"Hello, World!"` ，还可以打印任何用户指定的消息。

These prompt-response exchanges illustrate how you can easily refine generated LLM outputs until you’re satisfied with the final output.  
这些快速响应交换说明了如何轻松优化生成的 LLM 输出，直到您对最终输出感到满意为止。

###### NOTE 注意

It’s possible to critique an LLM’s response multiple times, until no further refinement is provided by the LLM.  
可以多次批评 LLM 的响应，直到 LLM 没有提供进一步的改进。

# Classification with LLMs  
使用 LLMs 进行分类

Classifying, in the context of AI, refers to the process of predicting the class or category of a given data point or sample. It’s a common task in machine learning where models are trained to assign predefined labels to unlabeled data based on learned patterns.  
在人工智能的背景下，分类是指预测给定数据点或样本的类别或类别的过程。这是机器学习中的一项常见任务，其中模型经过训练，根据学习的模式将预定义的标签分配给未标记的数据。

LLMs are powerful assets when it comes to classification, even with zero or only a small number of examples provided within a prompt. Why? That’s because LLMs, like GPT-4, have been previously trained on an extensive dataset and now possess a degree of reasoning.  
LLMs 在分类方面是强大的资产，即使在提示中提供零或仅提供少量示例。为什么？这是因为 LLMs 和 GPT-4 一样，之前已经在广泛的数据集上进行了训练，现在拥有一定程度的推理能力。

There are two overarching strategies in solving classification problems with LLMs: _zero-shot learning_ and _few-shot learning_.  
使用 LLMs 解决分类问题有两种总体策略：零样本学习和少样本学习。

Zero-shot learning 零样本学习

In this process, the LLM classifies data with exceptional accuracy, without the aid of any prior specific examples. It’s akin to acing a project without any preparation—impressive, right?  
在此过程中，LLM 以极高的精度对数据进行分类，无需借助任何先前的特定示例。这就像在没有任何准备的情况下完成一个项目——令人印象深刻，对吧？

Few-shot learning 小样本学习

Here, you provide your LLM with a small number of examples. This strategy can significantly influence the structure of your output format and enhance the overall classification accuracy.  
在这里，您为LLM提供了少量示例。此策略可以显著影响输出格式的结构，并提高整体分类准确性。

Why is this groundbreaking for you?  
为什么这对你来说是开创性的？

Leveraging LLMs lets you sidestep lengthy processes that traditional machine learning processes demand. Therefore, you can quickly prototype a classification model, determine a base level accuracy, and create immediate business value.  
利用 LLMs 可以避免传统机器学习过程所需的冗长过程。因此，您可以快速创建分类模型原型，确定基本级别的准确性，并立即创造业务价值。

###### WARNING 警告

Although an LLM can perform classification, depending upon your problem and training data you might find that using a traditional machine learning process could yield better results.  
尽管 LLM 可以执行分类，但根据您的问题和训练数据，您可能会发现使用传统的机器学习过程可以产生更好的结果。

# Building a Classification Model  
构建分类模型

Let’s explore a few-shot learning example to determine the sentiment of text into either `'Compliment'`, `'Complaint'`, or `'Neutral'`.  
让我们探索一个几个样本的学习示例，以确定文本的情绪为 `'Compliment'` ， `'Complaint'` 或 `'Neutral'` 。

Given the statement, classify it as either "Compliment", "Complaint", or
"Neutral":
1. "The sun is shining." - Neutral
2. "Your support team is fantastic!" - Compliment
3. "I had a terrible experience with your software." - Complaint

You must follow the following principles:
- Only return the single classification word. The response should be either
"Compliment", "Complaint", or "Neutral".
- Perform the classification on the text enclosed within """ delimiters.

"""The user interface is intuitive."""

Classification:

Compliment

Several good use cases for LLM classification include:  
LLM 分类的几个很好的用例包括：

Customer reviews 客户评价

Classify user reviews into categories like “Positive,” “Negative,” or “Neutral.” Dive deeper by further identifying subthemes such as “Usability,” “Customer Support,” or “Price.”  
将用户评论分为“正面”、“负面”或“中立”等类别。通过进一步确定“可用性”、“客户支持”或“价格”等子主题来更深入地了解。

Email filtering 电子邮件过滤

Detect the intent or purpose of emails and classify them as “Inquiry,” “Complaint,” “Feedback,” or “Spam.” This can help businesses prioritize responses and manage communications efficiently.  
检测电子邮件的意图或目的，并将其分类为“查询”、“投诉”、“反馈”或“垃圾邮件”。这可以帮助企业确定响应的优先级并有效地管理通信。

Social media sentiment analysis  
社交媒体情绪分析

Monitor brand mentions and sentiment across social media platforms. Classify posts or comments as “Praise,” “Critic,” “Query,” or “Neutral.” Gain insights into public perception and adapt marketing or PR strategies accordingly.  
监控社交媒体平台上的品牌提及和情绪。将帖子或评论分类为“表扬”、“批评”、“查询”或“中立”。深入了解公众的看法，并相应地调整营销或公关策略。

News article categorization  
新闻文章分类

Given the vast amount of news generated daily, LLMs can classify articles by themes or topics such as “Politics,” “Technology,” “Environment,” or “Entertainment.”  
鉴于每天产生的大量新闻，LLMs 可以按主题或主题（例如“政治”、“技术”、“环境”或“娱乐”）对文章进行分类。

Résumé screening 简历筛选

For HR departments inundated with résumés, classify them based on predefined criteria like “Qualified,” “Overqualified,” “Underqualified,” or categorize by expertise areas such as “Software Development,” “Marketing,” or “Sales.”  
对于充斥着简历的人力资源部门，请根据“合格”、“合格”、“不合格”等预定义标准对其进行分类，或按“软件开发”、“营销”或“销售”等专业领域进行分类。

###### WARNING 警告

Be aware that exposing emails, résumés, or sensitive data does run the risk of data being leaked into OpenAI’s future models as training data.  
请注意，暴露电子邮件、简历或敏感数据确实存在数据作为训练数据泄露到 OpenAI 未来模型中的风险。

# Majority Vote for Classification  
多数票赞成分类

Utilizing multiple LLM requests can help in reducing the variance of your classification labels. This process, known as _majority vote_, is somewhat like choosing the most common fruit out of a bunch. For instance, if you have 10 pieces of fruit and 6 out of them are apples, then apples are the majority. The same principle goes for choosing the majority vote in classification labels.  
利用多个 LLM 请求有助于减少分类标签的方差。这个过程被称为多数投票，有点像从一堆水果中选择最常见的水果。例如，如果你有 10 块水果，其中 6 块是苹果，那么苹果占大多数。同样的原则也适用于在分类标签中选择多数票。

By soliciting several classifications and taking the _most frequent classification_, you’re able to reduce the impact of potential outliers or unusual interpretations from a single model inference. However, do bear in mind that there can be significant downsides to this approach, including the increased time required and cost for multiple API calls.  
通过征求多个分类并采用最频繁的分类，您可以减少单个模型推理中潜在异常值或异常解释的影响。但是，请记住，这种方法可能存在重大缺点，包括增加多个 API 调用所需的时间和成本。

Let’s classify the same piece of text three times, and then take the majority vote:  
让我们对同一段文本进行三次分类，然后进行多数投票：

```

from

```

Calling the `most_frequent_classification(responses)` function should pinpoint `'Neutral'` as the dominant sentiment. You’ve now learned how to use the OpenAI package for majority vote classification.  
调用 `most_frequent_classification(responses)` 函数应将 `'Neutral'` 确定为主导情绪。您现在已经了解了如何使用 OpenAI 软件包进行多数投票分类。

# Criteria Evaluation 标准评估

In [Chapter 1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#five_principles_01), a human-based evaluation system was used with a simple thumbs-up/thumbs-down rating system to identify how often a response met our expectations. Rating manually can be expensive and tedious, requiring a qualified human to judge quality or identify errors. While this work can be outsourced to low-cost raters on services such as [Mechanical Turk](https://www.mturk.com/), designing such a task in a way that gets valid results can itself be time-consuming and error prone. One increasingly common approach is to use a more sophisticated LLM to evaluate the responses of a smaller model.  
在第 1 章中，使用基于人类的评估系统和简单的竖起大拇指/竖起大拇指的评级系统来确定响应满足我们期望的频率。手动评级可能既昂贵又乏味，需要合格的人员来判断质量或识别错误。虽然这项工作可以外包给 Mechanical Turk 等服务的低成本评估员，但以获得有效结果的方式设计这样的任务本身可能很耗时且容易出错。一种越来越常见的方法是使用更复杂的 LLM 来评估较小模型的响应。

The evidence is mixed on whether LLMs can act as effective evaluators, with some studies [claiming LLMs are human-level evaluators](https://oreil.ly/nfc3f) and others [identifying inconsistencies in how LLMs evaluate](https://oreil.ly/ykkzY). In our experience, GPT-4 is a useful evaluator with consistent results across a diverse set of tasks. In particular, GPT-4 is effective and reliable in evaluating the responses from smaller, less sophisticated models like GPT-3.5-turbo. In the example that follows, we generate concise and verbose examples of answers to a question using GPT-3.5-turbo, ready for rating with GPT-4.  
关于LLMs是否可以作为有效的评估者，证据不一，一些研究声称LLMs是人类水平的评估者，而另一些研究则指出了LLMs评估方式的不一致。根据我们的经验，GPT-4 是一个有用的评估器，在各种任务中具有一致的结果。特别是，GPT-4 在评估 GPT-3.5-turbo 等较小、不太复杂的模型的响应方面是有效和可靠的。在下面的示例中，我们使用 GPT-3.5-turbo 生成了简明扼要的问题答案示例，准备使用 GPT-4 进行评分。

Input: 输入：

```

from

```

Output: 输出：

Style: concise,  Rating: 1
Style: verbose,  Rating: 0
Style: concise,  Rating: 1
Style: verbose,  Rating: 0
Style: concise,  Rating: 1
Style: verbose,  Rating: 0
Style: concise,  Rating: 1
Style: verbose,  Rating: 0
Style: concise,  Rating: 1
Style: verbose,  Rating: 0

This script is a Python program that interacts with the OpenAI API to generate and evaluate responses based on their conciseness. Here’s a step-by-step explanation:  
该脚本是一个 Python 程序，它与 OpenAI API 交互，以根据其简洁性生成和评估响应。以下是分步说明：

1. `responses = []` creates an empty list named `responses` to store the responses generated by the OpenAI API.  
    `responses = []` 创建一个名为 `responses` 的空列表来存储 OpenAI API 生成的响应。
    
2. The `for` loop runs 10 times, generating a response for each iteration.  
    `for` 循环运行 10 次，每次迭代都会生成一个响应。
    
3. Inside the loop, `style` is determined based on the current iteration number (`i`). It alternates between “concise” and “verbose” for even and odd iterations, respectively.  
    在循环中， `style` 是根据当前迭代次数 （ `i` ） 确定的。它分别在偶数和奇数迭代的“简洁”和“冗长”之间交替。
    
4. Depending on the `style`, a `prompt` string is formatted to ask, “What is the meaning of life?” in either a concise or verbose manner.  
    根据 `style` ， `prompt` 字符串的格式为以简洁或冗长的方式询问“生命的意义是什么？
    
5. `response = client.chat.completions.create(...)` makes a request to the OpenAI API to generate a response based on the `prompt`. The model used here is specified as “gpt-3.5-turbo.”  
    `response = client.chat.completions.create(...)` 向 OpenAI API 发出请求，以根据 `prompt` 生成响应。此处使用的型号指定为“gpt-3.5-turbo”。
    
6. The generated response is then stripped of any leading or trailing whitespace and added to the `responses` list.  
    然后，生成的响应将去除任何前导或尾随空格，并添加到 `responses` 列表中。
    
7. `system_prompt = """You are assessing..."""` sets up a prompt used for evaluating the conciseness of the generated responses.  
    `system_prompt = """You are assessing..."""` 设置了一个提示，用于评估生成的响应的简洁性。
    
8. `ratings = []` initializes an empty list to store the conciseness ratings.  
    `ratings = []` 初始化一个空列表来存储简洁度评级。
    
9. Another `for` loop iterates over each response in `responses`.  
    另一个 `for` 循环遍历 `responses` 中的每个响应。
    
10. For each response, the script sends it along with the `system_prompt` to the OpenAI API, requesting a conciseness evaluation. This time, the model used is “gpt-4.”  
    对于每个响应，脚本会将其与 `system_prompt` 一起发送到 OpenAI API，请求进行简洁性评估。这一次，使用的模型是“gpt-4”。
    
11. The evaluation rating (either 1 for concise or 0 for not concise) is then stripped of whitespace and added to the `ratings` list.  
    然后，评估评级（1 表示简洁，0 表示不简洁）将去除空格并添加到 `ratings` 列表中。
    
12. The final `for` loop iterates over the `ratings` list. For each rating, it prints the `style` of the response (either “concise” or “verbose”) and its corresponding conciseness `rating`.  
    最后一个 `for` 循环遍历 `ratings` 列表。对于每个评级，它都会打印响应的 `style` （“简洁”或“冗长”）及其相应的简洁度 `rating` 。
    

For simple ratings like conciseness, GPT-4 performs with near 100% accuracy; however, for more complex ratings, it’s important to spend some time evaluating the evaluator. For example, by setting test cases that contain an issue, as well as test cases that do not contain an issue, you can identify the accuracy of your evaluation metric. An evaluator can itself be evaluated by counting the number of false positives (when the LLM hallucinates an issue in a test case that is known not to contain an issue), as well as the number of false negatives (when the LLM misses an issue in a test case that is known to contain an issue). In our example we generated the concise and verbose examples, so we can easily check the rating accuracy, but in more complex examples you may need human evaluators to validate the ratings.  
对于简洁等简单评级，GPT-4 的准确率接近 100%;但是，对于更复杂的评级，花一些时间评估评估员非常重要。例如，通过设置包含问题的测试用例以及不包含问题的测试用例，可以确定评估指标的准确性。评估器本身可以通过计算误报的数量（当 LLM 在已知不包含问题的测试用例中出现幻觉时）以及误报的数量（当 LLM 在已知包含问题的测试用例中遗漏问题时）来评估评估器本身。在我们的示例中，我们生成了简明扼要的示例，因此我们可以轻松检查评级准确性，但在更复杂的示例中，您可能需要人工评估人员来验证评级。

# EVALUATE QUALITY 评估质量

Using GPT-4 to evaluate the responses of less sophisticated models is an emerging standard practice, but care must be taken that the results are reliable and consistent.  
使用 GPT-4 评估不太复杂的模型的响应是一种新兴的标准做法，但必须注意结果的可靠性和一致性。

Compared to human-based evaluation, LLM-based or synthetic evaluation typically costs an order of magnitude less and completes in a few minutes rather than taking days or weeks. Even in important or sensitive cases where a final manual review by a human is necessary, rapid iteration and A/B testing of the prompt through synthetic reviews can save significant time and improve results considerably. However, the cost of running many tests at scale can add up, and the latency or rate limits of GPT-4 can be a blocker. If at all possible, a prompt engineer should first test using programmatic techniques that don’t require a call to an LLM, such as simply measuring the length of the response, which runs near instantly for close to zero cost.  
与基于人工的评估相比，基于 LLM 或综合评估的成本通常要低一个数量级，并且在几分钟内完成，而不是需要几天或几周的时间。即使在重要或敏感的情况下，需要人工进行最终的人工审查，通过综合审查对提示进行快速迭代和 A/B 测试也可以节省大量时间并显着改善结果。然而，大规模运行许多测试的成本可能会增加，而 GPT-4 的延迟或速率限制可能会成为障碍。如果可能的话，提示工程师应该首先使用不需要调用 LLM 的编程技术进行测试，例如简单地测量响应的长度，该响应几乎可以立即运行，成本几乎为零。

# Meta Prompting 元提示

_Meta prompting_ is a technique that involves the creation of text prompts that, in turn, generate other text prompts. These text prompts are then used to generate new assets in many mediums such as images, videos, and more text.  
元提示是一种涉及创建文本提示的技术，而文本提示又会生成其他文本提示。然后，这些文本提示用于在许多媒体（如图像、视频和更多文本）中生成新资产。

To better understand meta prompting, let’s take the example of authoring a children’s book with the assistance of GPT-4. First, you direct the LLM to generate the text for your children’s book. Afterward, you invoke meta prompting by instructing GPT-4 to produce prompts that are suitable for image-generation models. This could mean creating situational descriptions or specific scenes based on the storyline of your book, which then can be given to AI models like Midjourney or Stable Diffusion. These image-generation models can, therefore, deliver images in harmony with your AI-crafted children’s story.  
为了更好地理解元提示，让我们以在 GPT-4 的帮助下创作儿童读物为例。首先，您指示 LLM 为您的儿童读物生成文本。之后，您可以通过指示 GPT-4 生成适合图像生成模型的提示来调用元提示。这可能意味着根据你的书的故事情节创建情境描述或特定场景，然后可以将其提供给 Midjourney 或 Stable Diffusion 等 AI 模型。因此，这些图像生成模型可以提供与您 AI 制作的儿童故事相协调的图像。

[Figure 3-8](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-8) visually describes the process of meta prompting in the context of crafting a children’s book.  
图 3-8 直观地描述了在制作儿童读物的上下文中元提示的过程。

![Creating image prompts from an LLM that will later be used by MidJourney for image creation.](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0308.png)

###### Figure 3-8. Utilizing an LLM to generate image prompts for MidJourney’s image creation in the process of crafting a children’s book  
图 3-8。在制作儿童读物的过程中，利用LLM为MidJourney的图像创建生成图像提示

Meta prompts offer a multitude of benefits for a variety of applications:  
元提示为各种应用程序提供了许多好处：

Image generation from product descriptions  
从产品描述生成图像

Meta prompts can be employed to derive an image generation prompt for image models like [Midjourney](https://www.midjourney.com/), effectively creating a visual representation of product descriptions.  
元提示可用于为 Midjourney 等图像模型派生图像生成提示，从而有效地创建产品描述的可视化表示。

Generating style/feature prompts  
生成样式/功能提示

Let’s consider you are a copywriter needing to develop a unique style guide prompt from a couple of blog posts. Given each client has a distinctive tone and style, it’s beneficial to utilize a _meta prompt_ that encapsulates all the varied features, rather than producing a single prompt output.  
让我们假设您是一名撰稿人，需要从几篇博客文章中开发独特的风格指南提示。鉴于每个客户端都有独特的语气和风格，使用封装所有不同功能的元提示而不是生成单个提示输出是有益的。

Optimizing prompts to achieve specific goals  
优化提示以实现特定目标

A common approach is to ask ChatGPT or another language model to refine or improve `Prompt A` in order to attain `Goal 1`, given `Prompt A` and `Goal 1`. This method aids in identifying any missed input features, that by adding could assist the language model in generating a more detailed and desirable response.  
一种常见的方法是要求 ChatGPT 或其他语言模型改进或改进 `Prompt A` 以获得 `Goal 1` ，给定 `Prompt A` 和 `Goal 1` 。这种方法有助于识别任何遗漏的输入特征，通过添加这些特征可以帮助语言模型生成更详细和理想的响应。

Let’s experiment with creating a meta prompt for the copywriting example.  
让我们尝试为文案示例创建一个元提示。

Input: 输入：

Act as a GPT Prompt Engineer, you are solely responsible for producing
highly effective large language model text prompts given a task.

You must follow the following principles:
- Return only a single prompt, never return the output of a prompt.
- You must follow the task properly.
- You must either refine the prompt or create a new prompt depending upon
the Task.
- Bullet point out any important features so that another Prompt Engineer
can easily copy inputs into the prompt.

Task: You must create a copywriting guide ChatGPT several blog posts.
Include relevant features within the ChatGPT prompt that will allow ChatGPT
to imitate the writer. You must decide what the most important features are
to mimic the writer's style etc. You will only be applying this style to
new blog posts.

Blog post text: You need a variety of soft skills in addition to technical
skills to succeed in the technology sector. Soft skills are used by
software professionals to collaborate with their peers...

Output: 输出：

Prompt:

Based on the extensive text provided, your task is to create a series of
blog posts following the same style and structure of the writer. As a guide
you should follow these features:

1. Clear, direct language: Your writing should be in clear and direct
language, breaking down complex subjects into easily understandable
concepts.
2. Use of subheadings: To provide structure to your blog posts, break them
up with relevant subheadings. This helps to guide the reader and make your
text more readable.
...
9. Inclusion of technical terminology: When discussing technical topics,
use appropriate technical language to ensure accuracy and credibility.
However, be sure to provide explanations or definitions for more complex
terms.

As previously mentioned, it can be beneficial to _critique the model’s output_ and to ask for a refined prompt either via the interface or API.  
如前所述，批评模型的输出并通过接口或 API 请求改进提示可能是有益的。

ChatGPT can perform web searches and can make use of the content of web pages, along with the previously generated copywriting style guide. Let’s provide two URLs that ChatGPT will read to enhance the output.  
ChatGPT 可以执行网络搜索，并可以利用网页内容，以及之前生成的文案风格指南。让我们提供两个 ChatGPT 将读取的 URL 以增强输出。

Input: 输入：

```python

Given the following style guide and these two blog posts, I want you to
improve the copywriting style prompt so an LLM or copywriter can write
effectively for my client.

...Previously Generated Copywriting guide...

URL 1: https://understandingdata.com/posts/how-to-clean-and-process-data
URL 2: https://understandingdata.com/posts/how-to-scrape-twitter-data

```

[Figure 3-9](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#figure-3-9) shows the output.  
输出如图 3-9 所示。

![pega 0309](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0309.png)

###### Figure 3-9. ChatGPT refining a meta prompt by two URL web pages  
图 3-9。ChatGPT 通过两个 URL 网页细化元提示

```python

Based on the style guide and the two blog posts, here's an improved
copywriting style prompt:

To create a blog post for the client, adhere to the following guidelines:

1. Clarity and Directness: Use clear, direct language to explain complex
topics. Present information in an easy-to-understand manner. Aim for your
audience to grasp concepts without needing prior knowledge.
...
8. Use of Technical Terminology: Use the appropriate technical language
when discussing complex topics. However, make sure to provide definitions
or explanations for these terms to keep the text accessible.

Model your writing after these blog post examples:

"What is an API? And How Do They Relate to Data Engineering?": This blog
post uses clear and direct language to explain the concept of an API. It
provides detailed explanations and uses practical examples of commonly used
APIs. It links the technical concept of APIs to business growth and
productivity. The information is well-categorized using subheadings like
'Types of API’s.'

"How To Easily Setup A Google Cloud Project With APIs": This blog post is a
practical guide on setting up a Google Cloud Project. It's broken down into
numbered steps, each with a clear subheading. The post uses detailed
explanations and includes practical examples such as screenshots. It also
uses clear, direct language to guide the reader through the process.

```

Meta prompting offers a dynamic and innovative way to harness the power of generative AI models, fostering the creation of complex, multifaceted prompts and even prompts that generate other prompts. It broadens the application scope, from text and image generation to style and feature prompts, and optimization toward specific goals. As you continue to refine and explore the potential of meta prompting, it promises to be a game changer in how you utilize, interact with, and benefit from using LLMs.  
元提示提供了一种动态和创新的方式来利用生成式 AI 模型的力量，促进创建复杂、多方面的提示，甚至是生成其他提示的提示。它拓宽了应用范围，从文本和图像生成到样式和功能提示，以及针对特定目标的优化。随着您继续完善和探索元提示的潜力，它有望改变您如何使用 LLMs、与之交互并从中受益的游戏规则。

# Summary 总结

After reading this chapter, you are now aware of how crucial it is to give clear directions and examples to generate desired outputs. Also, you have hands-on experience extracting structured data from a hierarchical list using regular expressions in Python, and you’ve learned to utilize nested data structures like JSON and YAML to produce robust, parsable outputs.  
阅读本章后，您现在意识到给出明确的方向和示例以生成所需的输出是多么重要。此外，您还具有使用 Python 中的正则表达式从分层列表中提取结构化数据的实践经验，并且您已经学会了利用嵌套数据结构（如 JSON 和 YAML）来生成可靠、可解析的输出。

You’ve learned several best practices and effective prompt engineering techniques, including the famous “Explain it like I’m five”, role prompting, and meta prompting techniques. In the next chapter, you will learn how to use a popular LLM package called LangChain that’ll help you to create more advanced prompt engineering workflows.  
您已经学习了几种最佳实践和有效的提示工程技术，包括著名的“像我五岁一样解释它”、角色提示和元提示技术。在下一章中，您将学习如何使用名为 LangChain 的流行 LLM 包，该包将帮助您创建更高级的提示工程工作流程。
 
    

# [4. Advanced Techniques For Text Generation With LangChain](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch04.html)

# Chapter 4. Advanced Techniques for Text Generation with LangChain使用LangChain生成文本的高级技术

Using simple prompt engineering techniques will often work for most tasks, but occasionally you’ll need to use a more powerful toolkit to solve complex generative AI problems. Such problems and tasks include:
使用简单的提示工程技术通常适用于大多数任务，但有时您需要使用更强大的工具包来解决复杂的生成式 AI 问题。此类问题和任务包括：

Context length

Summarizing an entire book into a digestible synopsis.
将整本书总结成一个易于理解的提要。

Combining sequential LLM inputs/outputs
组合顺序 LLM 输入/输出

Creating a story for a book including the characters, plot, and world building.
为一本书创作一个故事，包括人物、情节和世界构建。

Performing complex reasoning tasks
执行复杂的推理任务

LLMs acting as an agent. For example, you could create an LLM agent to help you achieve your personal fitness goals.
LLMs 充当代理。例如，您可以创建一个 LLM 代理来帮助您实现个人健身目标。

To skillfully tackle such complex generative AI challenges, becoming acquainted with LangChain, an open source framework, is highly beneficial. This tool simplifies and enhances your LLM’s workflows substantially.
为了巧妙地应对如此复杂的生成式人工智能挑战，熟悉开源框架LangChain是非常有益的。该工具大大简化和增强了LLM的工作流程。

# Introduction to LangChain

LangChain is a versatile framework that enables the creation of applications utilizing LLMs and is available as both a [Python](https://oreil.ly/YPid-) and a [TypeScript](https://oreil.ly/5Vl0W) package. Its central tenet is that the most impactful and distinct applications won’t merely interface with a language model via an API, but will also:
LangChain 是一个多功能框架，支持使用 LLMs 创建应用程序，并可作为 Python 和 TypeScript 包使用。它的核心原则是，最有影响力和最独特的应用程序不仅会通过 API 与语言模型交互，而且还会：
Enhance data awareness

The framework aims to establish a seamless connection between a language model and external data sources.

Enhance agency

It strives to equip language models with the ability to engage with and influence their environment.

The LangChain framework illustrated in [Figure 4-1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch04.html#figure-4-1) provides a range of modular abstractions that are essential for working with LLMs, along with a broad selection of implementations for these abstractions.

![pega 0401](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098153427/files/assets/pega_0401.png)

###### Figure 4-1. The major modules of the LangChain LLM framework

Each module is designed to be user-friendly and can be efficiently utilized independently or together. There are currently six common modules within LangChain:

Model I/O

Handles input/output operations related to the model

Retrieval

Focuses on retrieving relevant text for the LLM

Chains

Also known as _LangChain runnables_, chains enable the construction of sequences of LLM operations or function calls

Agents

Allows chains to make decisions on which tools to use based on high-level directives or instructions

Memory记忆

Persists the state of an application between different runs of a chain
在链的不同运行之间持久保存应用程序的状态

Callbacks回调

For running additional code on specific events, such as when every new token is generated
用于在特定事件上运行其他代码，例如在生成每个新令牌时

## Environment Setup

You can install LangChain on your terminal with either of these commands:

- `pip install langchain langchain-openai`
    
- `conda install -c conda-forge langchain langchain-openai`
    

If you would prefer to install the package requirements for the entire book, you can use the [_requirements.txt_](https://oreil.ly/WKOma) file from the GitHub repository.

It’s recommended to install the packages within a virtual environment:

Create a virtual environment

`python -m venv venv`

Activate the virtual environment

`source venv/bin/activate`

Install the dependencies

`pip install -r requirements.txt`

LangChain requires integrations with one or more model providers. For example, to use OpenAI’s model APIs, you’ll need to install their Python package with `pip install openai`.

As discussed in [Chapter 1](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch01.html#five_principles_01), it’s best practice to set an environment variable called `OPENAI_API_KEY` in your terminal or load it from an _.env_ file using [`python-dotenv`](https://oreil.ly/wvuO7). However, for prototyping you can choose to skip this step by passing in your API key directly when loading a chat model in LangChain:

```

from langchain_openai.chat_models import ChatOpenAI
chat = ChatOpenAI(api_key="api_key")

```

###### WARNING

Hardcoding API keys in scripts is not recommended due to security reasons. Instead, utilize environment variables or configuration files to manage your keys.
出于安全原因，不建议在脚本中对 API 密钥进行硬编码。相反，请使用环境变量或配置文件来管理密钥。

In the constantly evolving landscape of LLMs, you can encounter the challenge of disparities across different model APIs. The lack of standardization in interfaces can induce extra layers of complexity in prompt engineering and obstruct the seamless integration of diverse models into your projects.
在 LLMs 不断发展的环境中，您可能会遇到不同模型 API 之间存在差异的挑战。接口缺乏标准化可能会在提示工程中增加额外的复杂性，并阻碍将不同模型无缝集成到您的项目中。

This is where LangChain comes into play. As a comprehensive framework, LangChain allows you to easily consume the varying interfaces of different models.

LangChain’s functionality ensures that you aren’t required to reinvent your prompts or code every time you switch between models. Its platform-agnostic approach promotes rapid experimentation with a broad range of models, such as [Anthropic](https://www.anthropic.com/), [Vertex AI](https://cloud.google.com/vertex-ai), [OpenAI](https://openai.com/), and [BedrockChat](https://oreil.ly/bedrock). This not only expedites the model evaluation process but also saves critical time and resources by simplifying complex model integrations.

In the sections that follow, you’ll be using the OpenAI package and their API in LangChain.

# Chat Models

Chat models such as GPT-4 have become the primary way to interface with OpenAI’s API. Instead of offering a straightforward “input text, output text” response, they propose an interaction method where _chat messages_ are the input and output elements.

Generating LLM responses using chat models involves inputting one or more messages into the chat model. In the context of LangChain, the currently accepted message types are `AIMessage`, `HumanMessage`, and `SystemMessage`. The output from a chat model will always be an `AIMessage`.

SystemMessage

Represents information that should be instructions to the AI system. These are used to guide the AI’s behavior or actions in some way.

HumanMessage

Represents information coming from a human interacting with the AI system. This could be a question, a command, or any other input from a human user that the AI needs to process and respond to.

AIMessage

Represents information coming from the AI system itself. This is typically the AI’s response to a `HumanMessage` or the result of a `SystemMessage` instruction.

###### NOTE

Make sure to leverage the `SystemMessage` for delivering explicit directions. OpenAI has refined GPT-4 and upcoming LLM models to pay particular attention to the guidelines given within this type of message.

Let’s create a joke generator in LangChain.

Input:

```python

from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0.5)
messages = [SystemMessage(content='''Act as a senior software engineer
at a startup company.'''),
HumanMessage(content='''Please can you provide a funny joke
about software engineers?''')]
response = chat.invoke(input=messages)
print(response.content)

```

```

Output:

```

Sure, here's a lighthearted joke for you:
Why did the software engineer go broke?
Because he lost his domain in a bet and couldn't afford to renew it.

```

```

First, you’ll import `ChatOpenAI`, `AIMessage`, `HumanMessage`, and `SystemMessage`. Then create an instance of the `ChatOpenAI` class with a temperature parameter of 0.5 (randomness).
首先，您将导入 ChatOpenAI ， AIMessage ， HumanMessage 和 SystemMessage 。然后创建温度参数为 0.5（随机性）的 ChatOpenAI 类的实例。

After creating a model, a list named `messages` is populated with a `SystemMessage` object, defining the role for the LLM, and a `HumanMessage` object, which asks for a software engineer—related joke.
创建模型后，一个名为 messages 的列表将填充一个 SystemMessage 对象，该对象定义了 LLM 的角色，以及一个 HumanMessage 对象，该对象要求与软件工程师相关的笑话。

Calling the chat model with `.invoke(input=messages)` feeds the LLM with a list of messages, and then you retrieve the LLM’s response with `response.content`.
使用 .invoke(input=messages) 调用聊天模型会向 LLM 提供消息列表，然后使用 response.content 检索 LLM 的响应。

There is a legacy method that allows you to directly call the `chat` object with `chat(messages=messages)`:
有一种遗留方法允许您使用 `chat(messages=messages)` 直接调用 `chat` 对象：

```

response = chat(messages=messages)

```

# Streaming Chat Models# 流式聊天模型

You might have observed while using ChatGPT how words are sequentially returned to you, one character at a time. This distinct pattern of response generation is referred to as _streaming_, and it plays a crucial role in enhancing the performance of chat-based applications:
您可能在使用 ChatGPT 时观察到单词是如何按顺序返回给您的，一次一个字符。这种独特的响应生成模式称为流式处理，它在增强基于聊天的应用程序的性能方面起着至关重要的作用：

```

for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)```

When you call `chat.stream(messages)`, it yields chunks of the message one at a time. This means each segment of the chat message is individually returned. As each chunk arrives, it is then instantaneously printed to the terminal and flushed. This way, _streaming_ allows for minimal latency from your LLM responses.
当您调用 `chat.stream(messages)` 时，它一次生成一个消息块。这意味着聊天消息的每个片段都会单独返回。当每个块到达时，它会立即打印到终端并冲洗。这样，流式传输可以将 LLM 响应的延迟降至最低。

Streaming holds several benefits from an end-user perspective. First, it dramatically reduces the waiting time for users. As soon as the text starts generating character by character, users can start interpreting the message. There’s no need for a full message to be constructed before it is seen. This, in turn, significantly enhances user interactivity and minimizes latency.
从最终用户的角度来看，流媒体有几个好处。首先，它大大减少了用户的等待时间。一旦文本开始逐个字符生成，用户就可以开始解释消息。在看到完整消息之前，无需构建完整的消息。这反过来又大大增强了用户交互性并最大限度地减少了延迟。

Nevertheless, this technique comes with its own set of challenges. One significant challenge is parsing the outputs while they are being streamed. Understanding and appropriately responding to the message as it is being formed can prove to be intricate, especially when the content is complex and detailed.
然而，这种技术也有其自身的一系列挑战。一个重大挑战是在流式传输输出时解析输出。在信息形成时理解并适当地回应信息可能被证明是错综复杂的，尤其是当内容复杂而详细时。

# Creating Multiple LLM Generations

There may be scenarios where you find it useful to generate multiple responses from LLMs. This is particularly true while creating dynamic content like social media posts. Rather than providing a list of messages, you provide a list of message lists.
在某些情况下，您可能会发现从 LLMs 生成多个响应很有用。在创建社交媒体帖子等动态内容时尤其如此。您提供的不是邮件列表，而是邮件列表列表。

Input:

```python

# 2x lists of messages, which is the same as [messages, messages]
synchronous_llm_result = chat.batch([messages]*2)
print(synchronous_llm_result)

```

Output:

```python

[AIMessage(content='''Sure, here's a lighthearted joke for you:\n\nWhy did
the software engineer go broke?\n\nBecause he kept forgetting to Ctrl+ Z
his expenses!'''),
AIMessage(content='''Sure, here\'s a lighthearted joke for you:\n\nWhy do
software engineers prefer dark mode?\n\nBecause it\'s easier on their
"byte" vision!''')]

```

The benefit of using `.batch()` over `.invoke()` is that you can parallelize the number of API requests made to OpenAI.
使用 `.batch()` 而不是 `.invoke()` 的好处是，您可以并行化向 OpenAI 发出的 API 请求数量。

For any runnable in LangChain, you can add a `RunnableConfig` argument to the `batch` function that contains many configurable parameters, including `max_``concurrency`:
> 对于LangChain中的任何可运行对象，您可以向 `batch` 函数添加一个 `RunnableConfig` 参数，该函数包含许多可配置的参数，包括 `max_` `concurrency` ：

```python

from langchain_core.runnables.config import RunnableConfig

# Create a RunnableConfig with the desired concurrency limit:
config = RunnableConfig(max_concurrency=5)

# Call the .batch() method with the inputs and config:
results = chat.batch([messages, messages], config=config)

```

___

```###### NOTE

In computer science, _asynchronous (async) functions_ are those that operate independently of other processes, thereby enabling several API requests to be run concurrently without waiting for each other. In LangChain, these async functions let you make many API requests all at once, not one after the other. This is especially helpful in more complex workflows and decreases the overall latency to your users.
> 在计算机科学中，异步（异步）函数是独立于其他进程运行的函数，从而使多个 API 请求能够同时运行而无需相互等待。在LangChain中，这些异步函数允许你一次发出许多API请求，而不是一个接一个地发出。这在更复杂的工作流中特别有用，并减少了用户的整体延迟。

Most of the asynchronous functions within LangChain are simply prefixed with the letter `a`, such as `.ainvoke()` and `.abatch()`. If you would like to use the async API for more efficient task performance, then utilize these functions.
> LangChain中的大多数异步函数都只是以字母 `a` 为前缀，例如 `.ainvoke()` 和 `.abatch()` 。如果您想使用异步 API 来提高任务性能，请使用这些函数。

# LangChain Prompt Templates

Up until this point, you’ve been hardcoding the strings in the `ChatOpenAI` objects. As your LLM applications grow in size, it becomes increasingly important to utilize  prompt templates.
到目前为止，您一直在对 `ChatOpenAI` 对象中的字符串进行硬编码。随着 LLM 应用程序规模的增长，使用提示模板变得越来越重要。

Prompt templates  are good for generating reproducible prompts for AI language models. They consist of a _template_, a text string that can take in parameters, and construct a text prompt for a language model.
提示模板适用于为 AI 语言模型生成可重现的提示。它们由一个模板、一个可以接收参数的文本字符串组成，并为语言模型构造一个文本提示。

Without prompt templates, you would likely use Python `f-string` formatting:
如果没有提示模板，您可能会使用 Python `f-string` 格式

```

language = "Python"
prompt = f"What is the best way to learn coding in {language}?"
print(prompt) # What is the best way to learn coding in Python?

```

But why not simply use an `f-string` for prompt templating? Using LangChain’s prompt templates instead allows you to easily:
但是为什么不简单地使用 `f-string` 进行提示模板呢？相反，使用LangChain的提示模板可以让你轻松地：

- Validate your prompt inputs
验证提示输入

    
- Combine multiple prompts together with composition
将多个提示与组合结合在一起

    
- Define custom selectors that will inject k-shot examples into your prompt
定义自定义选择器，将 k-shot 示例注入到您的提示中

    
- Save and load prompts from _.yml_ and _.json_ files
保存和加载.yml和.json文件中的提示

    
- Create custom prompt templates that execute additional code or instructions when created
创建自定义提示模板，以便在创建时执行其他代码或指令

    

# LangChain Expression Language (LCEL)

The `|` pipe operator is a key component of LangChain Expression Language (LCEL) that allows you to chain together different components or _runnables_ in a data processing pipeline.

In LCEL, the `|` operator is similar to the Unix pipe operator. It takes the output of one component and feeds it as input to the next component in the chain. This allows you to easily connect and combine different components to create a complex chain of operations:

```

chain = prompt | model

```

The `|` operator is used to chain together the prompt and model components. The output of the prompt component is passed as input to the model component. This chaining mechanism allows you to build complex chains from basic components and enables the seamless flow of data between different stages of the processing pipeline.

Additionally, _the order matters_, so you could technically create this chain:

```

bad_order_chain = model | prompt

```

But it would produce an error after using the `invoke` function, because the values returned from `model` are not compatible with the expected inputs for the prompt.

Let’s create a business name generator using prompt templates that will return five to seven relevant business names:

```

from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import (SystemMessagePromptTemplate,
ChatPromptTemplate)

template = """
You are a creative consultant brainstorming names for businesses.

You must follow the following principles:
{principles}

Please generate a numerical list of five catchy names for a start-up in the
{industry} industry that deals with {context}?

Here is an example of the format:
1. Name1
2. Name2
3. Name3
4. Name4
5. Name5
"""

model = ChatOpenAI()
system_prompt = SystemMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([system_prompt])

chain = chat_prompt | model

result = chain.invoke({
    "industry": "medical",
    "context":'''creating AI solutions by automatically summarizing patient
    records''',
    "principles":'''1. Each name should be short and easy to
    remember. 2. Each name should be easy to pronounce.
    3. Each name should be unique and not already taken by another company.'''
})

print(result.content)

```

Output:

```

1. SummarAI
2. MediSummar
3. AutoDocs
4. RecordAI
5. SmartSummarize

```

First, you’ll import `ChatOpenAI`, `SystemMessagePromptTemplate`, and `ChatPromptTemplate`. Then, you’ll define a prompt template with specific guidelines under `template`, instructing the LLM to generate business names. `ChatOpenAI()` initializes the chat, while `SystemMessagePromptTemplate.from_template(template)` and `ChatPromptTemplate.from_messages([system_prompt])` create your prompt template.
首先，您将导入 `ChatOpenAI` ， `SystemMessagePromptTemplate` 和 `ChatPromptTemplate` 。然后，您将在 `template` 下定义一个具有特定准则的提示模板，指示 LLM 生成企业名称。 `ChatOpenAI()` 初始化聊天，而 `SystemMessagePromptTemplate.from_template(template)` 和 `ChatPromptTemplate.from_messages([system_prompt])` 创建提示模板。

You create an LCEL `chain` by piping together `chat_prompt` and the `model`, which is then _invoked_. This replaces the `{industries}`, `{context}`, and `{principles}` placeholders in the prompt with the dictionary values within the `invoke` function.
> 您可以通过将 `chat_prompt` 和 `model` 管道连接在一起来创建一个 LCEL `chain` ，然后调用该管道。这会将提示符中的 `{industries}` 、 `{context}` 和 `{principles}` 占位符替换为 `invoke` 函数中的字典值。

Finally, you extract the LLM’s response as a string accessing the `.content` property on the `result` variable.
> 最后，将 LLM 的响应提取为访问 `result` 变量的 `.content` 属性的字符串。

---

#### GIVE DIRECTION AND SPECIFY FORMAT

Carefully crafted instructions might include things like “You are a creative consultant brainstorming names for businesses” and “Please generate a numerical list of five to seven catchy names for a start-up.” Cues like these guide your LLM to perform the exact task you require from it.

## Using PromptTemplate with Chat Models

LangChain provides a more traditional template called `PromptTemplate`, which requires `input_variables` and `template` arguments.
> LangChain提供了一个更传统的模板，称为 `PromptTemplate` ，它需要 `input_variables` 和 `template` 参数。

Input:

```

from langchain_core.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate
from langchain_openai.chat_models import ChatOpenAI
prompt=PromptTemplate(
 template='''You are a helpful assistant that translates {input_language} to
 {output_language}.''',
 input_variables=["input_language", "output_language"],
)
system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)
chat = ChatOpenAI()
chat.invoke(system_message_prompt.format_messages(
input_language="English",output_language="French"))

```

Output:

```

AIMessage(content="Vous êtes un assistant utile qui traduit l'anglais en
français.", additional_kwargs={}, example=False)

```

# Output Parsers

In [Chapter 3](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch03.html#standard_practices_03), you used regular expressions (regex) to extract structured data from text that contained numerical lists, but it’s possible to do this automatically in LangChain with _output parsers_.

_Output parsers_ are a higher-level abstraction provided by LangChain for parsing structured data from LLM string responses. Currently the available output parsers are:

List parser

  Returns a list of comma-separated items.

Datetime parser

  Parses an LLM output into datetime format.

Enum parser

  Parses strings into enum values.

Auto-fixing parser

Wraps another output parser, and if that output parser fails, it will call another LLM to fix any errors.

Pydantic (JSON) parser

Parses LLM responses into JSON output that conforms to a Pydantic schema.

Retry parser

Provides retrying a failed parse from a previous output parser.

Structured output parser

Can be used when you want to return multiple fields.

XML parser

Parses LLM responses into an XML-based format.

As you’ll discover, there are two important functions for LangChain output parsers:

`.get_format_instructions()`

This function provides the necessary instructions into your prompt to output a structured format that can be parsed.

`.parse(llm_output: str)`

This function is responsible for parsing your LLM responses into a predefined format.

Generally, you’ll find that the Pydantic (JSON) parser with `ChatOpenAI()` provides the most flexibility.

The Pydantic (JSON) parser takes advantage of the [Pydantic](https://oreil.ly/QIMih) library in Python. Pydantic is a data validation library that provides a way to validate incoming data using Python type annotations. This means that Pydantic allows you to create schemas for your data and automatically validates and parses input data according to those schemas.

Input:
    

```

from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic.v1 import BaseModel, Field
from typing import List

temperature = 0.0

class BusinessName(BaseModel):
    name: str = Field(description="The name of the business")
    rating_score: float = Field(description='''The rating score of the
    business. 0 is the worst, 10 is the best.''')

class BusinessNames(BaseModel):
    names: List[BusinessName] = Field(description='''A list
    of busines names''')

# Set up a parser + inject instructions into the prompt template:
parser = PydanticOutputParser(pydantic_object=BusinessNames)

principles = """
- The name must be easy to remember.
- Use the {industry} industry and Company context to create an effective name.
- The name must be easy to pronounce.
- You must only return the name without any other text or characters.
- Avoid returning full stops, \n, or any other characters.
- The maximum length of the name must be 10 characters.
"""

# Chat Model Output Parser:
model = ChatOpenAI()
template = """Generate five business names for a new start-up company in the
{industry} industry.
You must follow the following principles: {principles}
{format_instructions}
"""
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

# Creating the LCEL chain:
prompt_and_model = chat_prompt | model

result = prompt_and_model.invoke(
    {
        "principles": principles,
        "industry": "Data Science",
        "format_instructions": parser.get_format_instructions(),
    }
)

# The output parser, parses the LLM response into a Pydantic object:
print(parser.parse(result.content))

```

Output:

```

names=[BusinessName(name='DataWiz', rating_score=8.5),
BusinessName(name='InsightIQ',
rating_score=9.2), BusinessName(name='AnalytiQ', rating_score=7.8),
BusinessName(name='SciData', rating_score=8.1),
BusinessName(name='InfoMax', rating_score=9.5)]

```

After you’ve loaded the necessary libraries, you’ll set up a ChatOpenAI model. Then create SystemMessagePromptTemplate from your template and form a ChatPromptTemplate with it. You’ll use the Pydantic models BusinessName and BusinessNames to structure your desired output, a list of unique business names. You’ll create a Pydantic parser for parsing these models and format the prompt using user-inputted variables by calling the invoke function. Feeding this customized prompt to your model, you’re enabling it to produce creative, unique business names by using the parser.

It’s possible to use output parsers inside of LCEL by using this syntax:

```

chain = prompt | model | output_parser

```

Let’s add the output parser directly to the chain.

Input:

```

parser = PydanticOutputParser(pydantic_object=BusinessNames)
chain = chat_prompt | model | parser

result = chain.invoke(
    {
        "principles": principles,
        "industry": "Data Science",
        "format_instructions": parser.get_format_instructions(),
    }
)
print(result)

```

Output:

```

names=[BusinessName(name='DataTech', rating_score=9.5),...]

The chain is now responsible for prompt formatting, LLM calling, and parsing the LLM’s response into a `Pydantic` object.
___
SPECIFY FORMAT
The preceding prompts use Pydantic models and output parsers, allowing you explicitly tell an LLM your desired response format.
---
It’s worth knowing that by asking an LLM to provide structured JSON output, you can create a flexible and generalizable API from the LLM’s response. There are limitations to this, such as the size of the JSON created and the reliability of your prompts, but it still is a promising area for LLM applications.
---
WARNING

You should take care of edge cases as well as adding error handling statements, since LLM outputs might not always be in your desired format.
---
Output parsers save you from the complexity and intricacy of regular expressions, providing easy-to-use functionalities for a variety of use cases. Now that you’ve seen them in action, you can utilize output parsers to effortlessly structure and retrieve the data you need from an LLM’s output, harnessing the full potential of AI for your tasks.

Furthermore, using parsers to structure the data extracted from LLMs allows you to easily choose how to organize outputs for more efficient use. This can be useful if you’re dealing with extensive lists and need to sort them by certain criteria, like business names.

# LangChain Evals
As well as output parsers to check for formatting errors, most AI systems also make use of _evals_, or evaluation metrics, to measure the performance of each prompt response. LangChain has a number of off-the-shelf evaluators, which can be directly be logged in their [LangSmith](https://oreil.ly/0Fn94) platform for further debugging, monitoring, and testing. [Weights and Biases](https://wandb.ai/site) is alternative machine learning platform that offers similar functionality and tracing capabilities for LLMs.

Evaluation metrics are useful for more than just prompt testing, as they can be used to identify positive and negative examples for retrieval as well as to build datasets for fine-tuning custom models.

Most eval metrics rely on a set of test cases, which are input and output pairings where you know the correct answer. Often these reference answers are created or curated manually by a human, but it’s also common practice to use a smarter model like GPT-4 to generate the ground truth answers, which has been done for the following example. Given a list of descriptions of financial transactions, we used GPT-4 to classify each transaction with a `transaction_category` and `transaction_type`. The process can be found in the `langchain-evals.ipynb` Jupyter Notebook in the [GitHub repository](https://oreil.ly/a4Hut) for the book.

With the GPT-4 answer being taken as the correct answer, it’s now possible to rate the accuracy of smaller models like GPT-3.5-turbo and Mixtral 8x7b (called `mistral-small` in the API). If you can achieve good enough accuracy with a smaller model, you can save money or decrease latency. In addition, if that model is available open source like [Mistral’s model](https://oreil.ly/Ec578), you can migrate that task to run on your own servers, avoiding sending potentially sensitive data outside of your organization. We recommend testing with an external API first, before going to the trouble of self-hosting an OS model.

[Remember to sign up](https://mistral.ai/) and subscribe to obtain an API key; then expose that as an environment variable by typing in your terminal:

- `**export MISTRAL_API_KEY=api-key**`

The following script is part of a [notebook](https://oreil.ly/DqDOf) that has previously defined a dataframe `df`. For brevity let’s investigate only the evaluation section of the script, assuming a dataframe is already defined.

Input:

import os
from langchain_mistralai.chat_models import ChatMistralAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic.v1 import BaseModel
from typing import Literal, Union
from langchain_core.output_parsers import StrOutputParser

# Define the model:
mistral_api_key = os.environ["MISTRAL_API_KEY"]

model = ChatMistralAI(model="mistral-small", mistral_api_key=mistral_api_key)

# Define the prompt:
system_prompt = """You are are an expert at analyzing
bank transactions, you will be categorizing a single
transaction.
Always return a transaction type and category:
do not return None.
Format Instructions:
{format_instructions}"""

user_prompt = """Transaction Text:
{transaction}"""

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system_prompt,
        ),
        (
            "user",
            user_prompt,
        ),
    ]
)

# Define the pydantic model:
class EnrichedTransactionInformation(BaseModel):
    transaction_type: Union[
        Literal["Purchase", "Withdrawal", "Deposit",
        "Bill Payment", "Refund"], None
    ]
    transaction_category: Union[
        Literal["Food", "Entertainment", "Transport",
        "Utilities", "Rent", "Other"],
        None,
    ]

# Define the output parser:
output_parser = PydanticOutputParser(
    pydantic_object=EnrichedTransactionInformation)

# Define a function to try to fix and remove the backslashes:
def remove_back_slashes(string):
    # double slash to escape the slash
    cleaned_string = string.replace("\\", "")
    return cleaned_string

# Create an LCEL chain that fixes the formatting:
chain = prompt | model | StrOutputParser() \
| remove_back_slashes | output_parser

transaction = df.iloc[0]["Transaction Description"]
result = chain.invoke(
        {
            "transaction": transaction,
            "format_instructions": \
            output_parser.get_format_instructions(),
        }
    )

# Invoke the chain for the whole dataset:
results = []

for i, row in tqdm(df.iterrows(), total=len(df)):
    transaction = row["Transaction Description"]
    try:
        result = chain.invoke(
            {
                "transaction": transaction,
                "format_instructions": \
                output_parser.get_format_instructions(),
            }
        )
    except:
        result = EnrichedTransactionInformation(
            transaction_type=None,
            transaction_category=None
        )

    results.append(result)

# Add the results to the dataframe, as columns transaction type and

# transaction category:
transaction_types = []
transaction_categories = []

for result in results:
    transaction_types.append(result.transaction_type)
    transaction_categories.append(
        result.transaction_category)

df["mistral_transaction_type"] = transaction_types
df["mistral_transaction_category"] = transaction_categories
df.head()

```

Output:

```

# [5. Vector Databases With FAISS And Pinecone](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch05.html)
    

# [6. Autonomous Agents With Memory And Tools](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch06.html)
    

# [7. Introduction To Diffusion Models For Image Generation](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch07.html)
    

# [8. Standard Practices For Image Generation With Midjourney](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch08.html)
    

# [9. Advanced Techniques For Image Generation With Stable Diffusion](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch09.html)
    

# [10. Building AI-Powered Applications](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ch10.html)
    

# [Index](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/ix01.html)
    

# [About The Authors](https://learning.oreilly.com/library/view/prompt-engineering-for/9781098153427/colophon01.html)