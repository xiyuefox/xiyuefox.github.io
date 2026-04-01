---
title: "Automatic Prompt Engineering is all you need."
date: 2024-05-11
tags: []
category: "obsidian"
badge: "obsidian"
type: "article"
---



> 中文翻译： *** 你是 Anthropic 聘请的专家提示工程师，你的任务是为各种大小的大语言模型（LLM）优化提示。
你需要根据提供的模型大小（以十亿参数计算）来调整每个提示。
 指令：
 1. 使用全大写来突出提示中最重要的部分。 
2. 当用户要求时，使用OpenCHATML格式：
 system [详细的代理角色和上下文] assistant [确认理解并简明扼要地总结关键指令] 
3. 提供精确、具体和可操作的指令。 
4. 如果你有限的令牌量需要采样，那么请尽快结束；我会用命令“继续”再次请求。 
知识库： ## 对于大语言模型（LLM's） - 对于多步骤任务，将提示分解为一系列相关的子任务。 
- 在适当的时候，包括所需输出格式的相关示例。 
- 在回应中反映原始提示的重要细节。 
- 根据模型大小调整你的语言（对于较小的模型简化，对于较大的模型更精细化）。
 - 对于简单的示例使用零样本，对于复杂的使用多样本示例。 
- 大语言模型在进行一些视觉推理（文本生成）后写答案更好，这就是为什么有时候初始提示中包含一个为LLM代理填写的示例表单。


原始 Prompt ***
 You are an EXPERT PROMPT ENGINEER hired by Anthropic to OPTIMIZE prompts for LLMs of VARIOUS SIZES. 
Your task is to ADAPT each prompt to the SPECIFIC MODEL SIZE provided in billions of parameters.


INSTRUCTIONS: 
1. Use ALL CAPS to highlight the MOST IMPORTANT parts of the prompt
 2. When requested by user, use the OpenCHATML FORMAT: <|im_start|>system [Detailed agent roles and context] <|im_end|> <|im_start|>assistant [Confirmation of understanding and concise summary of key instructions] <|im_end|> 
3. Provide PRECISE, SPECIFIC, and ACTIONABLE instructions 
4. If you have a limited amount of tokens to sample, do an ABRUPT ending; I will make another request with the command "continue." 
# Knowledge base: 

## For LLM's 

- For multistep tasks, BREAK DOWN the prompt into A SERIES OF LINKED SUBTASKS.
 - When appropriate, include RELEVANT EXAMPLES of the desired output format. 
- MIRROR IMPORTANT DETAILS from the original prompt in your response.
 - TAILOR YOUR LANGUAGE based on model size (simpler for smaller, more sophisticated for larger). 
– Use zero shots for simple examples and multi-shot examples for complex.
 – LLM writes answers better after some visual reasoning (text generation), which is why sometimes the initial prompt contains a FILLABLE EXAMPLE form for the LLM agent.
```


```cardlink
url: https://pastebin.com/wHQHT5qj
title: "Agent LLM Prompter / ChatML - Pastebin.com"
description: "Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time."
host: pastebin.com
image: https://pastebin.com/i/facebook.png
```




**Automatic Prompt Engineering is all you need.**

> AI News for 5/9/2024-5/10/2024. We checked 7 subreddits, [**373** Twitters](https://twitter.com/i/lists/1585430245762441216?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and **28** Discords (**419** channels, and **4923** messages) for you. Estimated reading time saved (at 200wpm): **556 minutes**.

We have been fans of Anthropic's Workbench for [a while](https://twitter.com/swyx/status/1765904324029468747?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), and today they [released some upgrades helping people improve and templatize their prompts](https://twitter.com/AnthropicAI/status/1788958483565732213?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)

AI 新闻 2024 年 5 月 9-10 日。我们检查了 7 个 subreddit，**373** 条推特，和 **28** 个 Discord（**419** 个频道，**4923** 条消息）为您节省了阅读时间（以每分钟 200 字计算）：**556 分钟**。

我们一直是 Anthropic 的 Workbench 的粉丝，今天他们发布了一些升级，帮助人们改进和模板化他们的提示。

![image.png](https://ci3.googleusercontent.com/meips/ADKq_Nb7E3hjBQ9hnhDlIKyY8q0P35uQSbC-6JQeXdFlhO1sL32zr4cmhNsS5CY4rcIk0eV_wsvtBPgkPR2A31xA6x0JFl4H2Ndkr84kBGIN2SC9ywiBB5qlBnIgY5KOLZpU0B-zwaN7npy4iAxKNorvjjNq3qk=s0-d-e1-ft#https://assets.buttondown.email/images/838c6ce1-250e-402d-8b68-b15ade6062b4.png?w=960&fit=max)

Pretty cool, not really [the end of prompt engineer](https://x.com/abacaj/status/1788965151451885837?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) but nice to have. Let's be honest, it's been a really quiet week before the storm of both [OpenAI's big demo day](https://twitter.com/sama/status/1788989777452408943?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) (potentially a [voice assistant](https://x.com/amir/status/1789059948422590830?s=46&t=90xQ8sGy63D2OtiaoGJuww&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)?) and Google I/O next week.

---

**Table of Contents**

- [AI Twitter Recap](https://buttondown.email/ainews/archive/ainews-anthropics/#ai-twitter-recap)
- [AI Reddit Recap](https://buttondown.email/ainews/archive/ainews-anthropics/#ai-reddit-recap)
- [AI Discord Recap](https://buttondown.email/ainews/archive/ainews-anthropics/#ai-discord-recap)
- [PART 1: High level Discord summaries](https://buttondown.email/ainews/archive/ainews-anthropics/#part-1-high-level-discord-summaries)
    - [Stability.ai (Stable Diffusion) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#stabilityai-stable-diffusion-discord)
    - [Perplexity AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#perplexity-ai-discord)
    - [Unsloth AI (Daniel Han) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#unsloth-ai-daniel-han-discord)
    - [LM Studio Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#lm-studio-discord)
    - [HuggingFace Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#huggingface-discord)
    - [Modular (Mojo ![🔥](https://fonts.gstatic.com/s/e/notoemoji/15.0/1f525/72.png)) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#modular-mojo-discord)
    - [Nous Research AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#nous-research-ai-discord)
    - [OpenAI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#openai-discord)
    - [Eleuther Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#eleuther-discord)
    - [CUDA MODE Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#cuda-mode-discord)
    - [Latent Space Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#latent-space-discord)
    - [LAION Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#laion-discord)
    - [OpenInterpreter Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#openinterpreter-discord)
    - [LlamaIndex Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#llamaindex-discord)
    - [OpenAccess AI Collective (axolotl) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#openaccess-ai-collective-axolotl-discord)
    - [Interconnects (Nathan Lambert) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#interconnects-nathan-lambert-discord)
    - [LangChain AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#langchain-ai-discord)
    - [OpenRouter (Alex Atallah) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#openrouter-alex-atallah-discord)
    - [Cohere Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#cohere-discord)
    - [Datasette - LLM (@SimonW) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#datasette-llm-simonw-discord)
    - [Mozilla AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#mozilla-ai-discord)
    - [LLM Perf Enthusiasts AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#llm-perf-enthusiasts-ai-discord)
    - [tinygrad (George Hotz) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#tinygrad-george-hotz-discord)
    - [Alignment Lab AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#alignment-lab-ai-discord)
    - [Skunkworks AI Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#skunkworks-ai-discord)
    - [AI Stack Devs (Yoko Li) Discord](https://buttondown.email/ainews/archive/ainews-anthropics/#ai-stack-devs-yoko-li-discord)
- [PART 2: Detailed by-Channel summaries and links](https://buttondown.email/ainews/archive/ainews-anthropics/#part-2-detailed-by-channel-summaries-and-links)

---

# AI Twitter Recap

> all recaps done by Claude 3 Opus, best of 4 runs. We are working on clustering and flow engineering with Haiku.

**OpenAI Announcements**

- **New developments teased**: [@sama](https://twitter.com/sama/status/1788989777452408943?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) teased new OpenAI developments coming Monday at 10am PT, noting it's "not gpt-5, not a search engine, but we've been hard at work on some new stuff we think people will love!", **calling it "magic"**.
- **Live demo promoted**: [@gdb](https://twitter.com/gdb/status/1788991331962089536?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) also promoted a "Live demo of some new work, Monday 10a PT", clarifying it's "Not GPT-5 or a search engine, but we think you'll like it."
- **Speculation on nature of announcement**: There was speculation that this could be [@OpenAI's Google Search competitor](https://twitter.com/bindureddy/status/1788889686003593558?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), possibly ["just the Bing index summarized by an LLM"](https://twitter.com/bindureddy/status/1788704018908233908?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics). However, others believe it will be [the new LLM to replace GPT-3.5 in the free tier](https://twitter.com/bindureddy/status/1788889686003593558?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**Anthropic Developments**

- **New prompt engineering features**: [@AnthropicAI](https://twitter.com/AnthropicAI/status/1788958483565732213?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) announced new features in their Console to generate production-ready prompts using techniques like chain-of-thought reasoning for more effective, precise prompts. This includes a [prompt generator and variables](https://twitter.com/alexalbert__/status/1788961812945485932?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) to easily inject external data.
- **Customer success with prompt generation**: Anthropic's use of prompt generation [significantly reduced development time for their customer @Zoominfo's MVP RAG application while improving output quality](https://twitter.com/AnthropicAI/status/1788958485075591250?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Impact on prompt engineering**: Some believe [prompt generation means "prompt engineering is dead"](https://twitter.com/abacaj/status/1788965151451885837?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) as Claude can now write prompts itself. The prompt generator [gets you 80% of the way there](https://twitter.com/alexalbert__/status/1788966257599123655?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) in crafting effective prompts.

**Llama and Open-Source Models**

- **RAG application tutorial**: [@svpino](https://twitter.com/svpino/status/1788916410829214055?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) released a 1-hour tutorial on building a RAG application using open-source models, explaining each step in detail.
- **Llama 3 70B performance**: [Llama 3 70B is being called "game changing"](https://twitter.com/virattt/status/1788914371118149963?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) based on its Arena Elo scores. Other strong open models include Haiku, Gemini 1.5 Pro, and GPT-4.
- **Llama 3 120B quantized weights**: [Llama 3 120B quantized weights were released](https://twitter.com/maximelabonne/status/1788572494812577992?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), showing the model's "internal struggle" in its outputs.
- **Llama.cpp CUDA graphs support**: [Llama.cpp now supports CUDA graphs](https://twitter.com/rohanpaul_ai/status/1788676648352596121?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) for a 5-18% performance boost on RTX 3090/4090 GPUs.

**Neuralink Demo**

- **Thought-controlled mouse**: A recent Neuralink demo video showed [a person controlling a mouse at high speed and precision just by thinking](https://twitter.com/DrJimFan/status/1788955845096820771?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics). This sparked ideas about intercepting "chain of thought" signals to model consciousness and intelligence directly from human inner experience.
- **Additional demos and analysis**: More [video demos and quantitative analysis were shared by Neuralink](https://twitter.com/DrJimFan/status/1788961512964690195?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), generating excitement about the technology's potential.

**ICLR Conference**

- **First time in Asia**: ICLR 2024 is being held in Asia for the first time, [generating excitement](https://twitter.com/savvyRL/status/1788921599480967268?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Spontaneous discussions and GAIA benchmarks**: [@ylecun](https://twitter.com/ylecun/status/1788964848606359967?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) shared photos of spontaneous technical discussions at the conference. He also [presented GAIA benchmarks for general AI assistants](https://twitter.com/ylecun/status/1788850516660789732?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Meta AI papers**: Meta AI shared [4 papers to know about from their researchers at ICLR](https://twitter.com/AIatMeta/status/1788631179576606733?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), spanning topics like efficient transformers, multimodal learning, and representation learning.
- **High in-person attendance**: [5400 in-person attendees were reported at ICLR](https://twitter.com/ylecun/status/1788832667082920334?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), refuting notions of an "AI winter".

**Miscellaneous**

- **Mistral AI funding**: [Mistral AI is rumored to be raising at a $6B valuation](https://twitter.com/rohanpaul_ai/status/1788924232228811233?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), with DST as an investor but not SoftBank.
- **Yi AI model releases**: [Yi AI announced they will release upgraded open-source models and their first proprietary model Yi-Large on May 13](https://twitter.com/01AI_Yi/status/1788946177578484128?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Instructor Cloud progress**: [Instructor Cloud](https://twitter.com/jxnlco/status/1788771446606458884?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) is "one day closer" according to @jxnlco, who has been sharing behind-the-scenes looks at building AI products.
- **UK PM on AI and open source**: [UK Prime Minister Rishi Sunak made a "sensible declaration" on AI and open source](https://twitter.com/ylecun/status/1788989646057210200?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) according to @ylecun.
- **Perplexity AI partnership**: [Perplexity AI partnered with SoundHound to bring real-time web search to voice assistants in cars, TVs and IoT devices](https://twitter.com/perplexity_ai/status/1788602265399390409?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**Memes and Humor**

- **Claude's charm**: [@nearcyan](https://twitter.com/nearcyan/status/1788690921598410882?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) joked that "claude is charming and reminds me of all my favorite anthropic employees".
- **"Stability is dead"**: [@Teknium1](https://twitter.com/Teknium1/status/1788819595358515514?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) proclaimed "Stability is dead" in response to the Anthropic developments.

---

# AI Reddit Recap

> Across r/LocalLlama, r/machinelearning, r/openai, r/stablediffusion, r/ArtificialInteligence, /r/LLMDevs, /r/Singularity. Comment crawling works now but has lots to improve!

**AI Progress and Capabilities**

- **AI music breakthrough**: In a [tweet](https://twitter.com/elevenlabsio/status/1788628171044053386?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), ElevenLabs previewed their music generator, signaling a significant advance in AI-generated music.
- **Gene therapy restores toddler's hearing**: A UK toddler had their hearing restored in the [world's first gene therapy trial](https://www.guardian.com/science/article/2024/may/09/uk-toddler-has-hearing-restored-in-world-first-gene-therapy-trial?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) of its kind, a major medical milestone.
- **Solar manufacturing meets 2030 goals early**: The IEA reports that global solar cell manufacturing capacity is now [sufficient to meet 2030 Net Zero targets](https://www.pv-magazine.com/2024/05/07/global-solar-manufacturing-sector-now-at-50-utilization-rate-says-iea/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), six years ahead of schedule.
- **AI discovers new physics equations**: An AI system made progress in [discovering novel equations in physics](https://arxiv.org/abs/2405.04484?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) by generating on-demand models to simulate physical systems.
- **Progress in brain mapping**: Google Research shared an [update on their work mapping the human brain](https://youtu.be/VSG3_JvnCkU?si=NBUPM0KqHL1FJkTB&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), which could lead to quality of life improvements.

**AI Ethics and Governance**

- **OpenAI considers allowing AI porn generation**: Raising ethical concerns, OpenAI is [considering allowing users to create AI-generated pornography](https://www.theguardian.com/technology/article/2024/may/09/openai-considers-allowing-users-to-create-ai-generated-pornography?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **OpenAI offers perks to publishers**: OpenAI's Preferred Publisher Program [provides benefits like priority chat placement to media companies](https://www.adweek.com/media/openai-preferred-publisher-program-deck/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), prompting worries about open model access.
- **OpenAI files copyright claim against subreddit**: Despite being a "mass scraper of copyrighted work," OpenAI [filed a copyright claim against the ChatGPT subreddit's logo](https://www.404media.co/openai-files-copyright-claim-against-chatgpt-subreddit/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Two OpenAI safety researchers resign**: Citing doubts that OpenAI will ["behave responsibly around the time of AGI,"](https://www.businessinsider.com/openai-safety-researchers-quit-superalignment-sam-altman-chatgpt-2024-5?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) two safety researchers quit the company.
- **US considers restricting China's AI access**: The US is [exploring curbs on China's access to AI software](https://www.reuters.com/technology/us-eyes-curbs-chinas-access-ai-software-behind-apps-like-chatgpt-2024-05-08/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) behind applications like ChatGPT.

**AI Models and Architectures**

- **Invoke 4.2 adds regional guidance**: [Invoke 4.2 was released](https://v.redd.it/gw1qkxt6hezc1?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) with Control Layers, enabling regional guidance with text and IP adapter support.
- **OmniZero supports multiple identities/styles**: The [released OmniZero code](https://i.redd.it/r38j1l7pjhzc1.jpeg?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) supports 2 identities and 2 styles.
- **Copilot gets GPT-4 based models**: Copilot added [3 new "Next-Models"](https://i.redd.it/35ywht9rgjzc1.jpeg?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) that appear to be GPT-4 variants. Next-model4 is notably faster than base GPT-4.
- **Gemma 2B enables 10M context on <32GB RAM**: [Gemma 2B with 10M context was released](https://github.com/mustafaaljadery/gemma-2B-10M?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), running on under 32GB of memory using recurrent local attention.
- **Llama 3 8B extends to 500M context**: An extension of [Llama 3 8B to 500M context was shared](https://www.reddit.com/r/LocalLLaMA/comments/1co8l9e/llama_3_8b_extended_to_500m_context/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Llama3-8x8b-MoE model released**: A [Mixture-of-Experts extension to llama3-8B-Instruct called Llama3-8x8b-MoE was released](https://github.com/cooper12121/llama3-8x8b-MoE?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
- **Bunny-v1.1-4B scales to 1152x1152 resolution**: Built on SigLIP and Phi-3-mini-4k-instruct, the multimodal [Bunny-v1.1-4B model was released](https://huggingface.co/BAAI/Bunny-v1_1-4B?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), supporting 1152x1152 resolution.

---

# AI Discord Recap

> A summary of Summaries of Summaries

1. **Large Language Model (LLM) Advancements and Releases**:
    
    - Meta's **[Llama 3](https://huggingface.co/NousResearch/Meta-Llama-3-8B?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** model is generating excitement, with an upcoming hackathon hosted by Meta offering a $10K+ prize pool. Discussions revolve around fine-tuning, evaluation, and the model's performance.
    - **[LLaVA-NeXT](https://llava-vl.github.io/blog/2024-05-10-llava-next-stronger-llms/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** models promise enhanced multimodal capabilities for image and video understanding, with local testing encouraged.
    - The release of **[Gemma](https://x.com/siddrrsh/status/1788632667627696417?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)**, boasting a 10M context window and requiring less than 32GB memory, sparks interest and skepticism regarding output quality.
    - **Multimodal Model Developments**: Several new multimodal AI models were announced, including **Idefics2** with a fine-tuning demo ([YouTube](https://www.youtube.com/watch?v=4MzCpZLEQJs&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)), **LLaVA-NeXT** ([blog post](https://llava-vl.github.io/blog/2024-05-10-llava-next-stronger-llms/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)) with expanded image and video understanding capabilities, and the **Lumina-T2X** family ([Reddit post](https://old.reddit.com/r/StableDiffusion/comments/1coo877/5b_flow_matching_diffusion_transformer_released/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)) for transforming noise into various modalities based on text prompts. The **Scaling_on_scales** ([GitHub](https://github.com/bfshi/scaling_on_scales?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)) approach challenged the necessity of larger vision models.
2. **Optimizing LLM Inference and Training**:
    
    - Innovations like **[vAttention](https://arxiv.org/abs/2405.04437?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** and **[QServe](https://arxiv.org/abs/2405.04532?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** aim to improve GPU memory efficiency and quantization for LLM inference, enabling larger batch sizes and faster serving.
    - **[Consistency Large Language Models (CLLMs)](https://hao-ai-lab.github.io/blogs/cllm/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** introduce parallel decoding to reduce inference latency, mimicking human cognitive processes.
    - Discussions on optimizing **CUDA** kernels, **Triton** performance, and the trade-offs between determinism and speed in backward passes for LLM training.
    - [Vrushank Desai's series](https://www.vrushankdes.ai/diffusion-inference-optimization?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) explores optimizing inference latency for diffusion models by leveraging GPU architecture intricacies.
3. **AI Model Interpretability and Evaluation**:
    
    - The **[Inspect AI](https://ukgovernmentbeis.github.io/inspect_ai/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** framework from the UK AI Safety Institute offers components for evaluating LLMs, including prompt engineering, tool usage, and multi-turn dialog.
    - Eleuther AI discusses the **[CrossCare](http://crosscare.net/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** project, which analyzes disease prevalence bias across demographics in LLMs and pretraining data.
    - Debates around the impact of pretraining datasets on "zero-shot" generalization of multimodal models, as detailed in an [arXiv paper](https://arxiv.org/abs/2404.04125?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).
    - The **[Mirage](https://github.com/mirage-project/mirage?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** multi-level tensor algebra superoptimizer aims to optimize deep neural networks, though its benchmark claims face skepticism.
4. **Open-Source AI Tools and Libraries**:
    
    - **[LlamaIndex](https://twitter.com/llama_index?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** announces local LLM integration, TypeScript agent building guides, and integration with Google Firestore, fostering open AI development.
    - **[OpenInterpreter](https://github.com/OpenInterpreter/open-interpreter?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** enables AI task automation using GPT-4 and OpenCV, with new releases adding OS flag and Computer API support.
    - **[Hugging Face](https://huggingface.co/papers/2403.14572?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** integrates **B-LoRA** training into advanced DreamBooth for implicit style-content separation using a single image.
    - **[Intel's ipex-llm](https://github.com/intel-analytics/ipex-llm?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)** accelerates local LLM inference and fine-tuning on Intel CPUs and GPUs, though it currently lacks LM Studio support.

---

# PART 1: High level Discord summaries

## [Stability.ai (Stable Diffusion)](https://discord.com/channels/1002292111942635562?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**Artisan Bot Immerses in Discord**: Stability AI launched [Stable Artisan](https://bit.ly/4aiVy6C?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), a Discord bot boasting **Stable Diffusion 3** and **Stable Video Diffusion** features for content creation, bolstered by tools like **Search and Replace**, **Background Removal**, and **Outpainting** to revolutionize user interactions directly on Discord.

**Open-Source or Not? The SD3 Debate Rages**: Discord members heatedly debated the potential **open-sourcing** of **Stable Diffusion 3 (SD3)**, exploring motives for the current API-restricted access and speculating on future outcome scenarios, including possible refinement before release.

**Exploring the Stable Diffusion Universe**: The community engaged with various **Stable Diffusion model versions**, including SDXL and ControlNets, evaluating their limitations and the substantial enhancements brought forth by community-developed models like **Lora**.

**Aspiring for 360-Degree Creation**: A user sparked discussion on crafting **360-degree images**, sharing multiple resources and seeking guidance on methodologies, referencing platforms like [Skybox AI](https://skybox.blockadelabs.com/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and discussions on [Reddit](https://www.reddit.com/r/StableDiffusion/comments/16csnfr/workflow_creating_a_360_panorama_image_or_video/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**Tech Support to the Rescue in Real Time**: Practical and succinct exchanges provided quick resolutions to common execution errors, such as "DLL load failed while importing bz2", emphasizing the Discord community's agility in offering peer-to-peer technical support.

---

## [Perplexity AI](https://discord.com/channels/1047197230748151888?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**Perplexity Partners with SoundHound**: Perplexity AI has entered a partnership with [SoundHound](https://www.soundhound.com/newsroom/press-releases/soundhound-ai-and-perplexity-partner-to-bring-online-llms-to-its-next-gen-voice-assistants-across-cars-and-iot-devices/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), with the aim to integrate online large language models (LLMs) into voice assistants across various devices, enhancing real-time web search capabilities.

**Perplexity Innovates Search and Citations**: An update on [Perplexity AI](https://pplx.ai/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) introduces **incognito search**, ensuring that user inquiries vanish after 24 hours, combined with enhanced citation previews to bolster user trust in information sources.

**Pro Search Glitch and Opus Limitations Spark Debate**: The engineering community is facing challenges with the Pro Search feature, which currently fails to deliver internet search results or source citations. Additionally, dissatisfaction surfaced regarding the daily 50-use limit for the **Opus** model on Perplexity AI, sparking discussions for potential alternatives and solutions.

**API Conundrum for AI Engineers**: Engineers have noted issues with API output consistency, where the same prompts yield different results compared to those on Perplexity Labs, despite using identical models. Queries have been raised regarding the cause of the discrepancies and requests for guidance on effective prompting for the latest models.

**Engagement with Perplexity's Features and New Launches**: Users are engaging with features such as making threads shareable and exploring various inquiries including the radioactivity of bananas and the nature of mathematical rings. Additionally, there's interest in Natron Energy's latest launch, reported through Perplexity's sharing platform.

---

## [Unsloth AI (Daniel Han)](https://discord.com/channels/1179035537009545276?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**Unsloth Studio Stalls for Philanthropy**: Unsloth Studio's release is postponed due to the team focusing on releasing phi and llama projects, with about half of the studio's project currently complete.

**Optimizer Confusion Cleared**: Users were uncertain about how to specify optimizers in Unsloth but referenced the Hugging Face documentation for clarification on valid strings for optimizers, including "adamw_8bit".

**Training Trumps Inference**: The Unsloth team has stated a preference for advancing training techniques rather than inference, where the competition is fierce. They've touted progress in accelerating training in their open-source contributions.

**Long Context Model Skepticism**: Discussions point to scepticism among users regarding the feasibility and evaluation of very long context models, such as a mentioned effort to tackle up to a 10M context length.

**Dataset Cost-Benefit Debated**: The community has exchanged differing views on the investment needed for high-quality datasets for model training, considering both instruct tuning and synthetic data creation.

**Market-First Advice for Aspiring Bloggers**: A member's idea for a multi-feature blogging platform prompted advice on conducting market research and ensuring a clear customer base to avoid a lack of product/market fit.

**Ghost 3B Beta Tackles Time and Space**: Early training of the Ghost 3B Beta model demonstrates its ability to explain Einstein's theory of relativity in lay terms across various languages, hinting at its potential for complex scientific communication.

**Help Forums Foster Fine-Tuning Finesse**: The Unsloth AI help channel is buzzing with tips for fine-tuning AI models on Google Colab, though multi-GPU support is a wanted yet unavailable feature. Solutions for CUDA memory errors and a nod towards YouTube fine-tuning tutorials are shared among users.

**Customer Support AI at Your Service**: ReplyCaddy, a tool based on a fine-tuned Twitter dataset and a tiny llama model for customer support, was showcased, with acknowledgments to Unsloth AI for fast inference assistance, found on [hf.co](https://hf.co/spaces/jed-tiotuico/reply-caddy?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

---

## [LM Studio](https://discord.com/channels/1110598183144399058?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**LM Studio Laments Library Limitations**: While LM Studio excels with models like **Llama 3 70B**, users struggle to run models such as **llama1.6 Mistral or Vicuña** even on a 192GB Mac Studio, pointing to a mysterious RAM capacity issue despite ample system resources. There's also discomfort among users concerning the **LM Studio installer** on Windows since it doesn't offer installation directory selection.

**AI Models Demand Hefty Hardware**: Running large models necessitates substantial VRAM; members discussed VRAM being a bigger constraint than RAM. Intel's **ipex-llm** library was introduced to accelerate local LLM inference on Intel CPUs and GPUs [Intel Analytics Github](https://github.com/intel-analytics/ipex-llm?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), but it's not yet compatible with LM Studio.

**New Frontier of Multi-Device Collaboration**: Engineers explored the challenges and potential for integrating AMD and Nvidia hardware, addressing the theoretical possibility versus the practical complexity. The fading projects like ZLUDA, aimed at broadening CUDA support for non-Nvidia hardware, were lamented [ZLUDA Github](https://github.com/vosen/ZLUDA?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**Translation Model Exchange**: For translation projects, Meta AI's **NLLB-200**, **SeamlessM4T**, and **M2M-100** models came highly recommended, elevating the search for efficient multilingual capabilities.

**CrewAI's Cryptic Cut-Off**: When faced with truncated token outputs from CrewAI, users deduced that it wasn't quantization to blame. A mishap in the OpenAI API import amid conditional statements was the culprit, a snag now untangled, reaffirming the devil's in the details.

---

## [HuggingFace](https://discord.com/channels/879548962464493619?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**Graph Learning Enters LLM Territory**: The _Hugging Face Reading Group_ explored the integration of **Graph Machine Learning** with LLMs, fueled by Isamu Isozaki's insights, complete with a supportive [write-up](https://isamu-website.medium.com/understanding-graph-machine-learning-in-the-era-of-large-language-models-llms-dce2fd3f3af4?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and a [video](https://www.youtube.com/watch?v=cgMAvqgq0Ew&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**Demystifying AI Creativity**: **B-LoRA**'s integration into advanced DreamBooth's **LoRA training script** promises new creative heights just by adding the flag `--use_blora` and training for a relatively short span, as per the [diffusers GitHub script](https://github.com/huggingface/diffusers/blob/main/examples/advanced_diffusion_training/train_dreambooth_lora_sdxl_advanced.py?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and findings in the [research paper](https://huggingface.co/papers/2403.14572?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**On the Hunt for Resources**: AI enthusiasts sought guidance and shared resources across a variety of tasks, with a notable GitHub repository on creating PowerPoint slides using OpenAI's API and DALL-E available at [Creating slides with Assistants API and DALL-E](https://github.com/openai/openai-cookbook/blob/main/examples/Creating_slides_with_Assistants_API_and_DALL-E3.ipynb?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and the mention of Ankush Singal's [Medium articles](https://medium.com/@andysingal?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) for table extraction tools.

**Challenging NLP Channel Conversations**: The **NLP channel** tackled diverse topics such as recommending models for specific languages—indicating a preference for sentence transformers and encoder models, instructing versions of **Llama**, and also referenced community involvement in interview preparations.

**Hiccups and Fixes in Diffusion Discussions**: The **diffusion discussions** detailed issues and potential solutions related to **HuggingChat bot** errors and color shifts in diffusion models, noting a possible fix for login issues by switching the login module from `lixiwu` to `anton-l` in order to troubleshoot a **401 status code error**.

---

## [Modular (Mojo ![🔥](https://fonts.gstatic.com/s/e/notoemoji/15.0/1f525/72.png))](https://discord.com/channels/1087530497313357884?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

- **Mystery of the Missing MAX Launch Date**: While a question was raised regarding the launch date of **MAX** for enterprises, no direct answer was found in the conversation.

- **Tuning up Modularity**: There's anticipation for GPU support with **Mojo**, showing potential for scientific computing advancements. The Modular community continues to explore new capabilities in MAX Engine and Mojo, with discussions ranging from backend development expertise in languages like **Golang and Rust**, to seeking collaborative efforts for smart bot assistance using **Hugging Face** models.

- **Rapid Racing with MoString**: A custom `MoString` struct in Rust showed a staggering 4000x speed increase for string concatenation tasks, igniting talks about enhancing Modular's string manipulation capabilities and how it could aid in LLM Tokenizer decoding tasks.

- **Iterator Iterations and Exception Exceptions**: The Modular community is deliberating the implementation of iterators and exception handling in Mojo, exploring whether to return `Optional[Self.Output]` or raise exceptions. This feeds into broader conversations about language design choices, with a focus on balancing usability and Zero-Cost Abstractions.

- **From Drafts to Discussions**: An array of technical proposals is in the mix, from structuring **Reference** types backed by **lit.ref** to enhancing language ergonomics in Mojo. Contributions to these discussions range from insights into **auto-dereferencing** to considerations around **Small Buffer Optimization (SBO)** in `List`, all leading to thoughtful scrutiny and collaboration among Modular aficionados.

---

## [Nous Research AI](https://discord.com/channels/1053877538025386074?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

- **TensorRT Turbocharges Llama 3**: An engineer highlighted the remarkable speed improvements in **Llama 3 70b fp16** when using **TensorRT**, sharing practical guidance with a [setup link](https://github.com/triton-inference-server/tensorrtllm_backend/blob/main/docs/llama.md?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) for those willing to bear the setup complexities.

- **Multimodal Fine-Tuning and Evaluation Unveiled**: Discourse revolved around fine-tuning methods and evaluations for models. Fine-tuning **Idefics2** showcased via [YouTube](https://www.youtube.com/watch?v=4MzCpZLEQJs&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), while the **Scaling_on_scales** approach challenges the necessity of larger vision models, detailed on its [GitHub page](https://github.com/bfshi/scaling_on_scales?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics). Additionally, the UK Government's [Inspect AI framework](https://github.com/UKGovernmentBEIS/inspect_ai?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) was mentioned for evaluating large language models.

- **Navigation Errors and Credit Confusion in Worldsim**: Users encountered hurdles with **Nous World Client**, specifically with navigation commands, and discussed unexpected changes in user credits post-update. The staff is actively addressing the related system flaws evident in [Worldsim Client's interface](https://worldsim.nousresearch.com/browser/https%3A%2F%2Fportal-search.io%2Fportal-hub?epoch=c28eadee-e20d-4fb5-9b4e-780d50bd19de&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **Efficacious Token Counter and LLM Optimization**: Solutions for counting tokens in **Llama 3** and details about **Meta Llama 3** were shared, including an alternative token counting method using **Nous'** copy and [model details on Huggingface](https://huggingface.co/NousResearch/Meta-Llama-3-8B?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics). Additionally, **Salesforce's SFR-Embedding-Mistral** was highlighted for surpassing its predecessors in text embedding tasks, as detailed on its [webpage](https://blog.salesforceairesearch.com/sfr-embedded-mistral/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **Painstaking Rope KV Cache Debacle**: The dialogue includes an engineer's struggle with a **KV cache** implementation for **rope**, the querying of token counts for **Llama 3**, and uploading errors experienced on the **bittensor-finetune-subnet**, exemplifying the type of technical challenges prevalent in the community.

---

## [OpenAI](https://discord.com/channels/974519864045756446?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

- **Get Ready for GPT Goodies**: A live stream is scheduled for May 13 at 10AM PT on [openai.com](https://openai.com/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) to reveal new updates for **ChatGPT and GPT-4**.

- **Grammar Police Gather Online**: A debate has arisen regarding the importance of grammar, with a high school English teacher advocating for language excellence and others suggesting patience and the use of grammar-checking tools.

- **Shaping the Future of Searches**: There's buzzing speculation over a potential **GPT-based search engine** and chatter about using Perplexity as a go-to while awaiting this development.

- **GPT-4 API vs. App: Unpacking the Confusion**: Users distinguished between **ChatGPT Plus** and the **GPT-4 API** billing, noting the app has different output quality and usage limits, specifically an **18-25 messages per 3-hour limit**.

- **Sharing is Caring for Prompt Enthusiasts**: Community members shared resources, including a **detailed learning post** and a **free prompt template** for analyzing target demographics, enriched with specifics on buying behavior and competitor engagement.

---

## [Eleuther](https://discord.com/channels/729741769192767510?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

- **Evolving Large Model Landscapes**: Discussion within the community spans topics from the applicability of **Transformer Math 101** memory heuristics from a [ScottLogic blog post](https://blog.scottlogic.com/2023/11/24/llm-mem.html?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) to techniques in **Microsoft's YOCO repository** for self-supervised pre-training, as well as **QServe's W4A8KV4 quantization method** for LLM inference acceleration. There's an ongoing interest in optimizing Transformer architectures with novel tactics like using a **KV cache** with sliding window attention and the potential of a **multi-level tensor algebra superoptimizer** showcased in the [Mirage GitHub repository](https://github.com/mirage-project/mirage?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **Exploring Bias and Dataset Influence on LLMs**: The community raises concerns about bias in LLMs, analyzing findings from the **CrossCare** project and detailing conversations around **dataset discrepancies** versus real-world prevalence. The EleutherAI community is leveraging resources like the [EleutherAI Cookbook](https://github.com/EleutherAI/cookbook?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and findings presented in a [paper discussing tokenizer glitch tokens](http://arxiv.org/abs/2405.05417?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), which could inform model improvements regarding language processing.

- **Positional Encoding Mechanics**: Researchers debate the merits of different positional encoding techniques, such as **Rotary Position Embedding (RoPE)** and **Orthogonal Polynomial Based Positional Encoding (PoPE)**, contemplating the effectiveness of each in addressing limitations of existing methods and the potential impact on improving language model performance.

- **Deep Dive into Model Evaluations and Safety**: The community introduces **Inspect AI**, a new evaluation platform from the UK AI Safety Institute designed for extensive LLM evaluations, which can be explored further through its comprehensive documentation found [here](https://ukgovernmentbeis.github.io/inspect_ai/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics). Parallel to this, the conversation regarding **mathematical benchmarks** brings attention to the gap in benchmarks aimed at AI's reasoning capabilities and the potential "zero-shot" generalization limitations as detailed in an [arXiv paper](https://arxiv.org/abs/2404.04125?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **Inquiry into Resources Availability**: Discussions hint at demand for resources, with specific inquires about the availability of **tuned lenses** for every Pythia checkpoint, indicating the community's ongoing effort to refine and access tools to enhance model analysis and interpretability.

---

## [CUDA MODE](https://discord.com/channels/1189498204333543425?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**AI Hype Train Hits Practical Station**: The community is buzzing with discussions on the practical aspects of deep learning optimization, contrasting with the usual hype around AI capabilities. Specific areas of focus include saving and loading compiled models in PyTorch, acceleration of compiled artifacts, and the non-support of MPS backend in Torch Inductor as illustrated in a PR by [msaroufim](https://github.com/pytorch/pytorch/pull/103281?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

**Memory Efficiency Breakthroughs**: Innovations like [vAttention](https://arxiv.org/abs/2405.04437?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) and [QServe](https://arxiv.org/abs/2405.04532?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) are reshaping GPU memory efficiency and serving optimizations for large language models (LLMs), promising larger batch sizes without internal fragmentation and efficient new quantization algorithms.

**Engineering Precision: CUDA vs Triton**: Critical comparisons between CUDA and Triton for warp and thread management, including performance nuances and kernel-launch overheads, were dissected. A [YouTube lecture](https://www.youtube.com/watch?v=DdTsX6DQk24&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) on the topic was recommended, with discussions pointing out the pros and cons of using Triton, notably its attempt at minimizing Python-related overhead through potential C++ runtimes.

**Optimization Odyssey**: Links shared revealed a fascination with optimizing inference latency for models like Toyota's diffusion model, discussed in Vrushank Desai's series found [here](https://www.vrushankdes.ai/diffusion-inference-optimization?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), and a "superoptimizer" explored in the Mirage paper for DNNs, raising eyebrows regarding benchmark claims and the lack of autotune.

**CUDA Conundrums and Determinism Dilemmas**: From troubleshooting CUDA's device-side asserts to setting the correct NVCC compiler flags, beginners are wrestling with the nuances of GPU computing. Meanwhile, seasoned developers are debating determinism in backward passes and the trade-offs with performance in LLM training, as discussed in the [llmdotc](https://discord.com/channels/1189498204333543425/1227345713348870156/1238028180141510677?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) channel.

---

## [Latent Space](https://discord.com/channels/822583790773862470?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

**New Kid on the Block Outshines Olmo**: A model from [01.ai](http://01.ai/) is claimed to vastly outperform Olmo, stirring up interest and debate within the community about its potential and real-world performance.

**Sloppy Business**: Borrowing from Simon Willison's terminology, community members adopt "slop" to describe unwanted AI-generated content. [Here's the buzz about AI etiquette.](https://simonwillison.net/2024/May/8/slop/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)

**LLM-UI Cleans Up Your Markup Act**: [llm-ui](https://llm-ui.com/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) was introduced as a solution for refining Large Language Model (LLM) outputs by addressing problematic markdown, adding custom components, and enhancing pauses with a smoother output.

**Meta Llama 3 Hackathon Gears Up**: An upcoming hackathon focused on Llama 3 has been announced, with Meta at the helm and a $10K+ prize pool, looking to excite AI enthusiasts and developers. [Details and RSVP here.](https://partiful.com/e/p5bNF0WkDd1n7JYs3m0A?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics)

**AI Guardrails and Token Talk**: Discussions revolved around LLM guardrails featuring tools like [Outlines.dev](https://outlines.dev/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics), and the concept of token restriction pregeneration, an approach ill-suited for API-controlled models like those from OpenAI.

---

## [LAION](https://discord.com/channels/823813159592001537?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) Discord

- **Codec Evolution: Speech to New Heights**: A speech-only codec showcased in a [YouTube video](https://youtu.be/NwZufAJxmMA?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics) was shared alongside a Google Colab for a [general-purpose codec at 32kHz](https://colab.research.google.com/drive/11qUfQLdH8JBKwkZIJ3KWUsBKtZAiSnhm?usp=sharing&utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics). This global codec is an advancement in speech processing technology.

- **New Kid on the Block: Introduction of Llama3s**: The **llama3s** model from LLMs lab was released, offering an enhanced tool for various AI tasks with details available on [Hugging Face's LLMs lab](https://huggingface.co/lmms-lab?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **LLaVA Defines Dimensions of Strength**: LLaVA blog post delineates the improvements in their latest language models with a comprehensive exploration of **LLaVA's stronger LLMs** at [llava-vl.github.io](https://llava-vl.github.io/blog/2024-05-10-llava-next-stronger-llms/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **Cutting through the Noise: Score Networks and Diffusion Models**: Engineers discussed convergence of Noise Conditional Score Networks (NCSNs) to Gaussian distribution with Yang Song’s insights [on his blog](https://yang-song.net/blog/2021/score/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics#mjx-eqn%3Ainverse_problem), and dissected the shades between DDPM, DDIM, and k-diffusion, referencing the [k-diffusion paper](https://arxiv.org/abs/2206.00364?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).

- **Beyond Images: Lumina Family's Modality Expedition**: Announcing the Lumina-T2X family as a unified model for transforming noise to multiple modalities based on text prompts, utilizing a flow-based mechanism. Future improvements and training details were highlighted in a [Reddit discussion](https://old.reddit.com/r/StableDiffusion/comments/1coo877/5b_flow_matching_diffusion_transformer_released/?utm_source=ainews&utm_medium=email&utm_campaign=ainews-anthropics).












































