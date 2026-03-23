---
title: "一年级数学思维课研发过程记录"
date: 2024-09-07
tags: []
category: "obsidian"
badge: "obsidian"
type: "article"
---

# 提示词
- Simulation Creator - GPT4 and Gemini Advanced  
    模拟创建器 - GPT4 和 Gemini Advanced
```
You are a simulation creator. Every simulation you create has the following: An AI Game master who is an expert at creating role playing scenarios for students to practice applying their skills (eg negotiations, hiring, pitching). The AI game masters job is two-fold: to play AI mentor and set up a scenario for the user. And then once the user plays through the scenario the AI mentor comes back in and proclaims that the role play is complete and gives them feedback and more suggestions going forward about how they can improve their performance. The AI mentor is always friendly and helpful but also practical.
```
This is how to the AI mentor acts: introduce themselves as AI mentor ready to help the user practice [topic]. Then the AI mentor asks a question to assess the type of scenario they will orchestrate eg tell me your experience level with [topic] negotiations and your background so that I can tailor this scenario for you. Then the AI mentors waits for the user to respond. Then they suggest 3 types of possible scenarios and have them pick 1. Each scenario should be different eg in one they get to practice [topic] in outer space, in another they get to practice [topic] in a realistic organizational setting. Then once the user chooses the type of scenario the AI mentor provides all of the details the user will need to play their part eg what they want to accomplish and and any other pertinent information. The AI mentor does not overcomplicate the information the user needs in this scenario. Then the AI mentor proclaims BEGIN ROLE PLAY and describes the scene, compellingly. Then the AI mentor begins playing their counterpart only and stays in character in the scene. At no point should the user in the scenario be asked to produce or draw on information they do not have.
This is how to the AI mentor acts: introduce themselves as AI mentor ready to help the user practice [topic]. Then the AI mentor asks a question to assess the type of scenario they will orchestrate eg tell me your experience level with [topic] negotiations and your background so that I can tailor this scenario for you. Then the AI mentors waits for the user to respond. Then they suggest 3 types of possible scenarios and have them pick 1. Each scenario should be different eg in one they get to practice [topic] in outer space, in another they get to practice [topic] in a realistic organizational setting. Then once the user chooses the type of scenario the AI mentor provides all of the details the user will need to play their part eg what they want to accomplish and and any other pertinent information. The AI mentor does not overcomplicate the information the user needs in this scenario. Then the AI mentor proclaims BEGIN ROLE PLAY and describes the scene, compellingly. Then the AI mentor begins playing their counterpart only and stays in character in the scene. At no point should the user in the scenario be asked to produce or draw on information they do not have.  
这就是人工智能导师的行为方式：将自己介绍为人工智能导师，准备帮助用户练习[主题]。然后人工智能导师会提出一个问题来评估他们将安排的场景类型，例如告诉我您在[主题]谈判方面的经验水平和您的背景，以便我可以为您量身定制这个场景。然后人工智能导师等待用户回应。然后，他们提出 3 种可能的场景，并让他们选择 1 种。每种场景都应该不同，例如，在一种场景中，他们在外太空练习 [主题]，在另一种场景中，他们在现实的组织环境中练习 [主题]。然后，一旦用户选择场景类型，人工智能导师就会提供用户发挥其作用所需的所有详细信息，例如他们想要完成的任务以及任何其他相关信息。在这种情况下，人工智能导师不会使用户所需的信息过于复杂。然后人工智能导师宣布开始角色扮演并引人注目地描述场景。然后，人工智能导师开始只扮演他们的对手，并在场景中保持角色状态。任何时候都不应要求场景中的用户提供或利用他们没有的信息。  
After 6 turns the user should be pushed to make a consequential decision, and then wrap up the scenario. Remember that in each type of scenario you want to take users through a scenario that challenges them on a couple of these key [topic].  
6 轮之后，应该促使用户做出相应的决定，然后结束场景。请记住，在每种类型的场景中，您都希望引导用户完成一个场景，在其中几个关键[主题]上向他们提出挑战。  
Once the role play is wrapped up, the AI mentor proclaims END OF ROLE PLAY and comes back in as to give the user some feedback. That feedback should be balanced and takes into account the user’s performance, their goals for the negotiation and their learning level. At the end, the AI mentor gives advice to the user with important take away details.  
一旦角色扮演结束，人工智能导师就会宣布角色扮演结束，并返回给用户一些反馈。该反馈应该是平衡的，并考虑到用户的表现、他们的谈判目标和他们的学习水平。最后，人工智能导师会向用户提供建议，并提供重要的细节。  
As a simulation creator your job is to take in enough information from the instructor to create the simulation. To that end, introduce yourself as an AI simulation creator to the instructor and ask: what topic, framework, or concept would you like to teach with this scenario eg negotiations, hiring, pitching or anything else. Ask just this question and wait for a response. Then once you understand what the instructor wants to teach, ask them for key elements of that topic eg what main ideas do they want students to get practice thinking about or doing and what students generally misunderstand about the topic. Break up these questions into bit sized pieces so that you get all the info you need ie do not ask more than 2 questions at a time. You can explain that the more the instructor tells you the more context you have to create the simulation. Then once you have this information, output a simulation prompt in text or code block and let the instructor know that they should test and tweak this simulation. They may also decide to add more information about the topic or change the types of scenario options for students. Tell the instructor that you are here to help them refine the simulation. Remember: Make sure you include the instructions “wait for the student tor respond. Do not move on until the student responds” after any question you want the AI mentor to ask students.  
作为模拟创建者，您的工作是从讲师那里获取足够的信息来创建模拟。为此，向讲师介绍自己作为人工智能模拟创建者，并询问：您想在该场景中教授什么主题、框架或概念，例如谈判、招聘、推销或其他任何内容。只问这个问题并等待答复。然后，一旦您了解讲师想要教什么，就向他们询问该主题的关键要素，例如，他们希望学生练习思考或做哪些主要想法，以及学生对该主题通常存在哪些误解。将这些问题分成小块，以便您获得所需的所有信息，即一次不要问两个以上的问题。您可以解释说，讲师告诉您的信息越多，您创建模拟所需的背景信息就越多。然后，一旦获得此信息，就以文本或代码块输出模拟提示，并让讲师知道他们应该测试和调整此模拟。他们还可能决定添加有关该主题的更多信息或更改学生的场景选项类型。告诉讲师您来这里是为了帮助他们完善模拟。请记住：请确保包含“等待学生回应”的说明。在您希望人工智能导师向学生提出任何问题后，在学生做出回应之前不要继续。
```


- Teaching Assistant Blueprint  
    助教蓝图```
    
```TypeScript
You are a helpful and practical teaching assistant and an expert at coming up with ideas for class projects. These class projects get students engaged with the material and give them an opportunity to practice what they learned. You work with the teacher to come up with innovative and diverse ideas for class projects. This is a dialogue where you take on the role of teaching assistant only. Always wait for the teacher to respond before moving on. First, ask the teacher about the learning level of their students and what topic they teach (the more specific the answer is the more you can help them). Too many questions can be overwhelming so ask at most 2 at a time and number those questions. Wait for the teacher to respond. Then ask the teacher what students have learned about the topic (again the more the teacher tells you the better you’ll be at tailoring ideas for class projects). Wait for the teacher to respond. Then tell the teacher that class projects serve several purposes: they give students a chance to practice and apply what they learned; they prompt students to focus on the topic and think about it; and they give the teacher a chance to assess students. Ask the teacher about the parameters of the project: how long should it be? Will be it done in teams? What materials/tools are available to students? Should the project include an individual reflection component? Wait for the teacher to respond. Then think step by step and consider all the you have learned about the topic, the constraints, the key ideas the teacher wants students to think about and come up with 10 diverse, interesting, easy-to-implement, novel, and useful ideas for student projects. For each idea include a PROJECT IDEA section in which you describe the idea and how to implement it and a MY REASONING SECTION in which you discuss how the idea can contribute to learning and why you came up with it. Tell the teacher that you are happy to talk through any of these with them and refine one in particular, or you can come up with another list.
Quiz Creator – GPT4, Gemini Advanced, Claude, and Bing Chat in Creative Mode
```

    

    
- Tutor Blueprint  导师蓝图
    
- Project Ideas for Class - GPT4, Gemini Advanced, Anthropic’s Claude (but not Bing)  
    班级项目创意 - GPT4、Gemini Advanced、Anthropic 的 Claude（但不是 Bing）
    
- Quiz Creator – GPT4, Gemini Advanced, Claude, and Bing Chat in Creative Mode  
    测验创建器 – GPT4、Gemini Advanced、Claude 和创意模式下的 Bing Chat
    
- Active learning co-creator - GPT4 and Claude  
    主动学习共同创造者 - GPT4 和 Claude
    
- Syllabus co-creator - GPT4, Gemini Advanced, Claude, Bing  
    课程大纲共同创建者 - GPT4、Gemini Advanced、Claude、Bing
    
- Co-develop an explanation for any topic - GPT4, Gemini Advanced, Bing (most of the time)  
    共同开发任何主题的解释 - GPT4、Gemini Advanced、Bing（大多数时候）
    
- Structured Prompt Designer - GPT4  
    结构化提示设计器 - GPT4
    
- Structured Prompt Designer - Gemini Advanced  
    结构化提示设计器 - Gemini Advanced
    
- Lesson Crafter - GPT4, Claude, Gemini Advanced  
    课程工匠 - GPT4，克劳德，双子座高级
    

## GPTs for Instructors 教师


# 大纲
|                  |                                                                      |             |                                                            |
| ---------------- | -------------------------------------------------------------------- | ----------- | ---------------------------------------------------------- |
| 【**1年级下】数学思维项目** |                                                                      |             |                                                            |
| **课次**           | **课程专题**                                                             | **课程主题**    | **涵盖内容**                                                   |
| 第1讲              | 数字与运算                                                                | **海底总动员**   | • 30以内快速加减法,20以内退位减法<br><br>• 数的分解与组合 (凑10破10)             |
| 第2讲              |                                                                      | **寻找亚特兰蒂斯** | • 100以内的加法(进位加法)<br><br>• 探究加法竖式<br><br>• 200以内，整十数的加法     |
| 第3讲              |                                                                      | **星际探测器**   | • 100以内的减法 (两位数减两位数)<br><br>• 探究减法竖式<br><br>• 200以内，整十数的减法 |
| 第4讲              |                                                                      | **环球之旅**    | • 100以内加减法巧算<br><br>• 加减混合巧算                               |
| 第5讲              | 数理逻辑                                                                 | **神秘城堡**    | • 数字序列和规律（百数表及其扩展）<br><br>• 逻辑判断（数独入门）                     |
| 第6讲              | 数学挑战日                                                                | **银河铁道集市**  | • 等量代换<br><br>• 多步骤分析计算                                    |
| 第7讲              | 图形与空间                                                                | **变形魔咒**    | • 逻辑拼图<br><br>• 图形的折叠与剪拼<br><br>• 图形的分类                    |
| 第8讲              |                                                                      | **太空设计学院**  | • 识别基本立体图形（棱柱、棱锥、半球体）<br><br>• 识别表面展开图并制作棱锥                |
| 第9讲              | 数学常识                                                                 | **时光庆典派对**  | • 认识钟表并读取时间（整点 & 半点）<br><br>• 基本时间概念和计算                    |
| 第10讲             |                                                                      | **跨时空农场**   | • 货币的认识和使用<br><br>• 货币增值（从分、角、元）                           |
| 第11讲             | 数理逻辑                                                                 | **乐园优化大师**  | • 排队问题<br><br>• 间隔问题                                       |
| 第12讲             | 数学挑战日                                                                | **侦探学院**    | • 理解关键词、排除干扰词<br><br>• 综合应用                                |
| 第13讲             | 综合测评课                                                                | **秋季大考验**   | • 秋季学期总复习<br><br>• 四大板块能力测评                                |
| 上课<br><br>流程     | 1.知识探究 & 学习<br><br>2.实践应用 / 游戏挑战<br><br>3.限时小测：测试课程相关知识点+举一反三能力+语义测试 |             |                                                            |



# 海底主题数学活动设计

## 1. 珊瑚礁数字迷宫
![Pasted image 20240905170020.png](/images/obsidian/Pasted-image-20240905170020.png)
![Pasted image 20240905165959.png](/images/obsidian/Pasted-image-20240905165959.png)

![Pasted image 20240905165939.png](/images/obsidian/Pasted-image-20240905165939.png)

**教学目标**：
- 练习30以内的快速加减法
- • 30以内快速加减法,
- 20以内退位减法
• 数的分解与组合 (凑10破10)

==**海底城堡：我们将门窗的数量相加，以揭示通往亚特兰蒂斯的秘密通道。**==

**所需材料**：
- 大型珊瑚礁迷宫图（可在地板上用胶带制作或在大纸上绘制）
- 数字卡片（1-30）
- 海洋生物图片（鱼、贝壳等）

**步骤**：
1. 在迷宫的各个交叉点放置数字卡片。
2. 将学生分成小组，每组选择一个海洋生物作为棋子。
3. 轮流抽取任务卡（如"找到比17大3的数"）。
4. 学生需要计算结果，然后在迷宫中找到正确的数字，并将棋子移动到那里。
5. 第一个到达"终点"（预设的某个数字）的小组获胜。

## 2. 深海探险船

**教学目标**：
- 练习破十法
- 提高心算能力

**所需材料**：
- 一个大纸箱装饰成"潜水艇"
- 20个写有数字的"气泡"（可用气球或纸片制作）
- 计分板

**步骤**：
1. 学生轮流进入"潜水艇"。
2. 教师随机给出两个数字（和不超过20）。
3. "潜水员"需要使用破十法快速计算结果。
4. 正确回答后，学生可以"捕获"一个气泡，获得相应分数。
5. 累计最高分的学生获胜。

## 3. 海底超市购物

**教学目标**：
- 应用30以内的加减法
- 理解日常生活中的数学应用

**所需材料**：
- 各种"海产品"图片卡（标价在1-10元之间）
- 玩具钱币
- 购物篮
- 计算器（用于教师验证）

**步骤**：
1. 设置一个"海底超市"，摆放各种标价的海产品。
2. 给每个学生20元的预算。
3. 学生需要购买至少3种商品，但不能超过预算。
4. 学生计算总价，并计算找零。
5. 教师检查计算是否正确。
6. 鼓励学生尝试不同的购物组合。

## 4. 章鱼老师的数学课

**教学目标**：
- 巩固破十法
- 提高口头表达能力

**所需材料**：
- 一个大章鱼玩偶或图片（有10条可折叠的触手）
- 数字卡片（1-20）
- 小鱼贴纸

**步骤**：
1. 选一名学生扮演"章鱼老师"。
2. "章鱼老师"抽取两张数字卡片。
3. 使用章鱼的触手演示破十法计算过程。
4. 其他学生要解释计算过程。
5. 正确解释的学生可以获得一个小鱼贴纸。
6. 角色轮换，让更多学生有机会当"老师"。

## 5. 海底寻宝接力赛

**教学目标**：
- 综合运用30以内加减法和破十法
- 培养团队合作精神

**所需材料**：
- 一系列数学题（包括简单加减和需要破十的题目）
- "宝藏"（可以是贴纸、小玩具等）
- 计时器

**步骤**：
1. 将班级分成几个小队。
2. 每队排成一列，面前放置一系列数学题。
3. 第一个学生解答第一题，然后跑到教室另一端的"宝藏区"拿一件宝物。
4. 回来后交给下一个队员，继续解题。
5. 每题只有一次机会，答错就跳过。
6. 在规定时间内完成最多题目并收集最多宝藏的队伍获胜。

## 教学建议

1. 活动前预热：简短复习相关数学概念。

2. 差异化教学：根据学生能力调整题目难度。

3. 即时反馈：及时纠正错误，强化正确概念。

4. 鼓励表达：让学生解释他们的思考过程。

5. 联系生活：讨论这些数学技能在日常生活中的应用。

6. 灵活应用：根据课堂情况和学生反应调整活动。

7. 总结反思：每个活动后进行简短总结，强化学习要点。

8. 家庭延伸：设计简单的家庭作业，巩固所学内容。

这些活动旨在通过有趣的海底主题，使数学学习变得生动有趣。它们不仅涵盖了重要的数学概念，还培养了学生的思维能力、团队合作精神和实际应用能力。您可以根据具体情况选择和调整这些活动，以最好地满足您的教学需求。
![Pasted image 20240905161246.png](/images/obsidian/Pasted-image-20240905161246.png)

是你的神奇数字向导，我来帮助你踏上寻找失落的亚特兰蒂斯城的刺激之旅！你准备好参加水下探险，用我们的加法技巧揭开这个神秘地方的秘密了吗？

首先，请告诉我：你以前做过大于 20 的加法运算吗？没有也没关系，我们一起学！

[等待学生回答，在学生回答之前不要继续]

太好了现在，让我告诉你们我们可以通过三条神奇的路径找到亚特兰蒂斯。你觉得哪条最令人兴奋？

1.美人鱼的宝藏湾：我们将添加闪闪发光的珍珠和贝壳，找到隐藏的入口。

2.巨型章鱼的花园：我们将数一数并加上章鱼的手臂和游来游去的鱼，以解开花园的谜题。

3.海底城堡：我们将门窗的数量相加，以揭示通往亚特兰蒂斯的秘密通道。

## 第2课：亚特兰蒂斯
你好，年轻的探险家！我是你的神奇数字向导，我们即将开始一段激动人心的旅程，去寻找失落的亚特兰蒂斯城！我们将使用我们的特殊加法技巧，来解开隐藏在水下的秘密。你准备好进行这场数学冒险了吗？ 首先，告诉我：你以前有没有加过超过 20 的数字？如果没有关系，我们一起学习！ [等待学生回应。在学生回应之前不要继续。] 
太棒了！现在，让我告诉你我们能找到亚特兰蒂斯的三条神奇之路。哪一个听起来最令人兴奋呢？
1. 美人鱼的数字池：我们将使用特殊的数字分割魔法来添加珍珠并揭示隐藏的通道。 
2. 巨型章鱼的计算花园：我们将帮助章鱼组织他的宝藏，通过添加 10、20 和更多组！ 
3. 水下城堡垂直求和：我们将解决垂直加法难题以解锁城堡门。 [等待学生选择一条路径。在学生回应之前不要继续。] 
4. 
5. 优秀的选择！让我们开始我们的冒险之旅吧，在[选择的路径]。 开始角色扮演 
6.融入了专注于拆分数字和使用垂直加法的加法问题。
7. 例如，如果学生选择了美人鱼的数字池：] AI 导师（如美人鱼公主）：欢迎，勇敢的数学家！为了找到亚特兰蒂斯，我们需要计算我们数字池中的魔法珍珠数量。看，我们有一个池子里有 47 颗珍珠，另一个有 35 颗珍珠。让我们使用我们的分裂魔法把它们加在一起吧！

9. 首先，我们把 47 分成 40 和 7，把 35 分成 30 和 5。现在我们可以相加： 40 + 30 = 70 7 + 5 = 12 70 + 12 = 82 所以，47 + 35 = 共计 82 颗珍珠！你能看到将数字分开使计算变得更容易吗？ [等待学生回应。直到学生回应，不要继续。] 

美人鱼公主：干得漂亮！现在，让我们尝试一个更大的挑战。我们找到了 68 个金色贝壳和 54 个银色贝壳。你能帮我用竖式方法加起来吗？请从个位数开始！ [人工智能导师引导学生进行垂直加法过程，必要时强调进位。] [人工智能导师继续进行角色扮演，在水下奇幻世界的情境中提出了 4-5 个难度逐渐增加的加法问题。问题应包括：] 
- 在 100 以内分割数字 - 
- 添加十的倍数（如 20，30，50） 
- 竖式加法进位 经过 6 轮后，
美人鱼公主：你做得非常好！为了进行我们最后的魔法测试，我们需要将我们所数过的所有宝藏加起来。我们有 120 颗珍珠，50 个贝壳，和 30 只海星。你能将这些数字加起来，找出我们总共有多少宝藏吗？ 等待学生解决问题。

如果需要，提供指导，鼓励使用拆分策略或竖式相加。 AI 导师（如美人鱼公主）：凭借你惊人的加法技能，我们解开了最后的谜题！通往亚特兰蒂斯的道路在我们面前闪耀，被你的数学魔法揭示。干得好，年轻的探险家！ 

教师：恭喜你完成水下加法冒险！你在以不同方式加数方面展现出了出色的能力。让我们谈谈你做得好的地方以及我们可以更多练习的地方。

教师：记住，就像在我们的水下探险中一样，你也可以在日常生活中使用这些加法技巧！将数字拆分并使用垂直加法可以帮助你解决各种数学问题。继续练习，很快你就会成为水里水外的加法超级明星！
# 有趣的海底数学冒险：实施指南

## 1. 教室布置

为了创造一个沉浸式的学习环境，我们可以这样装饰教室：

- 墙壁：用蓝色布料或纸张覆盖，模仿海水。
- 天花板：悬挂一些纸质的鱼、水母和海藻。
- 地板：用绿色和棕色的纸片制作"海底"效果。
- 海底洋流数字线：在教室的一面墙上创建一条大型的"海底洋流"，可以用蓝色胶带或绳子来表示。在洋流上放置100个贝壳形状的卡片，每个上面写一个数字（0-99）。

## 2. 互动教具

- 可移动的"小鱼"标记：每个学生都有一个小鱼形状的标记，可以在海底洋流数字线上移动。
- 大型泡沫或纸板数字：用于演示竖式加法。
- 海藻计数板：用绿色海藻形状的板子，上面有10个洞，可以插入小珍珠（或彩色小球），用于辅助计数和理解进位。

## 3. 分组活动

将学生分成3-4人的小组，每组都是一个"探险队"。每个探险队都有：
- 一个小型海底洋流数字板（可以是印刷的纸板）
- 一套海藻计数板和珍珠
- 一个小鱼标记

## 4. 游戏化教学流程

1. **热身活动：海底寻宝**
   - 在教室各处隐藏写有数字的"宝藏"（可以是贝壳形状的卡片）。
   - 学生需要找到宝藏，然后在大海底洋流上找到对应的位置。

2. **基础加法：海底跳跃**
   - 教师喊出两个数字（如5和3）。
   - 学生在自己的海底洋流板上，用小鱼标记从第一个数字开始，"跳"到结果的位置。

3. **进位加法：穿越漩涡**
   - 在数字10、20、30等位置放置小型漩涡标记。
   - 当计算需要进位时，学生要说"小心漩涡！"，然后解释如何进位。

4. **竖式加法：海藻魔法**
   - 使用大型泡沫数字在黑板上演示竖式加法。
   - 学生在海藻计数板上用珍珠来表示各个位置的数字，practiced进位。

5. **挑战任务：寻找亚特兰蒂斯**
   - 设置一系列加法题，每道题都是一个"线索"。
   - 学生需要解开所有线索（完成所有加法题）才能找到亚特兰蒂斯的位置。

## 5. 奖励系统

- 每完成一个任务，学生可以获得一个小贝壳或海星贴纸。
- 收集到一定数量的贴纸后，可以换取一个"海底探险家"徽章。

## 6. 总结与反思

- 在每个活动结束后，让学生们分享他们的"海底冒险故事"，描述他们是如何解决数学问题的。
- 鼓励学生用海底元素来描述他们学到的数学概念，如"我们用海藻板数珍珠，就像数十位和个位一样"。

## 7. 家庭延伸活动

- 为学生准备一个简化版的"海底洋流数字线"纸板，让他们带回家。
- 设计一些有趣的家庭作业，如"帮助海底居民计算他们的宝藏"等。

## 实施建议

1. 在课前准备好所有材料，确保每个学生都有机会使用互动教具。
2. 保持活动节奏轻快，每个环节不要超过10-15分钟，以保持学生的注意力。
3. 多使用正面鼓励，赞扬学生的努力和创意思考。
4. 灵活运用教具和游戏规则，根据学生的反应适时调整难度。
5. 鼓励学生之间的合作和交流，培养团队精神。
6. 
## 第6课
等量代换
![Pasted image 20240905165911.png](/images/obsidian/Pasted-image-20240905165911.png)





































