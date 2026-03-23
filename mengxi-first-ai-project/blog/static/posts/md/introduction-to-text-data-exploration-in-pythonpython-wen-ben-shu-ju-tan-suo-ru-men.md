---
title: "Introduction to Text Data Exploration in PythonPython文本数据探索入门"
date: 2024-07-01
tags: []
category: "obsidian"
badge: "obsidian"
---

This learning path offers foundational knowledge in Natural Language Processing (NLP). It covers data exploration, preprocessing, text vectorization, and machine learning for text classification. Gain proficiency in transforming text into insights and implementing models to classify text.  
这条学习路径提供了自然语言处理 (NLP) 的基础知识。它涵盖了数据探索、预处理、文本向量化和用于文本分类的机器学习。学习如何将文本转化为洞察力，并实现对文本进行分类的模型。

[Start path 开始路径](https://learn.codesignal.com/course-paths/42)[  
](https://learn.codesignal.com/preview/course-paths/42#courses)
### Introduction to Text Data Exploration in Python  
Python 文本数据探索入门
This introductory course guides you through the initial yet critical steps of any data science project: data exploration. By utilizing Python and specifically pandas, you'll learn to load, inspect, and analyze datasets to gain fundamental insights.
### Text Data Preprocessing in Python  
Python 中文本数据预处理
Learn to clean and prepare textual data for machine learning models using Python. This course teaches you to apply basic preprocessing tasks such as text lowercasing, removing stopwords, tokenization, and stemming on the SMS Spam Collection
### Introduction to TF-IDF Vectorization in Python  
Python 中 TF-IDF 向量化的介绍
### Building and Evaluating Text Classifiers in Python  
在 Python 中构建和评估文本分类器

Progress from preprocessing text data to building predictive models with this practical course. You'll learn how to leverage machine learning algorithms, such as Naive Bayes and logistic regression, to classify text into categories.
![Pasted image 20240701212534.png](/images/obsidian/Pasted-image-20240701212534.png)![Pasted image 20240701212612.png](/images/obsidian/Pasted-image-20240701212612.png)## Text Classification with Natural Language Processing

This NLP learning path is tailored for mastering text classification, spanning from data preparation to model optimization. It includes practice in data collection, feature engineering, diverse modeling techniques, and advanced optimization strategies. It aims to develop comprehensive skills in NLP, ensuring learners can construct and refine text classification models efficiently.
## Introduction and Text Data Collection  
引言和文本数据收集

Welcome to today's lesson! As data science and machine learning professionals, particularly in the Natural Language Processing (NLP) field, we often deal with textual data. Today, we dive into the 'Introduction to Textual Data Collection'. Specifically, we'll explore how to collect, understand and analyze text data using `Python`.  
欢迎来到今天的课程！作为数据科学和机器学习专业人士，特别是在自然语言处理 (NLP) 领域，我们经常处理文本数据。今天，我们将深入探讨“文本数据收集简介”。具体来说，我们将探索如何使用 `Python` 收集、理解和分析文本数据。

Textual data is usually unstructured, being much harder to analyze than structured data. It can take many forms, such as emails, social media posts, books, or transcripts of conversations. Understanding how to handle such data is a critical part of building effective machine learning models, especially for text classification tasks where we 'classify' or categorize texts. The quality of the data we use for these tasks is of utmost importance. Better, well-structured data leads to models that perform better.  
文本数据通常是非结构化的，比结构化数据更难分析。它可以采取多种形式，例如电子邮件、社交媒体帖子、书籍或对话记录。了解如何处理此类数据是构建有效机器学习模型的关键部分，尤其是在文本分类任务中，我们需要“分类”或归类文本。我们用于这些任务的数据质量至关重要。更好、结构良好的数据会带来性能更佳的模型。
## The 20 Newsgroups Dataset  
20 个新闻组数据集

The dataset we'll be working with in today's lesson is the **20 Newsgroups dataset**. For some historical background, newsgroups were the precursors to modern internet forums, where people gathered to discuss specific topics. In our case, the dataset consists of approximately 20,000 documents from newsgroup discussions. These texts were originally exchanged through Usenet, a global discussion system that predates many modern Internet forums.  
今天课程中我们将使用的数据集是 20 Newsgroups 数据集。作为一些历史背景，新闻组是现代互联网论坛的先驱，人们聚集在那里讨论特定的话题。在我们的例子中，数据集包含大约 20,000 篇来自新闻组讨论的文档。这些文本最初是通过 Usenet 交换的，Usenet 是一个全球性的讨论系统，早于许多现代互联网论坛。

The dataset is divided nearly evenly across 20 different newsgroups, each corresponding to a separate topic - this segmentation is one of the main reasons why it is especially useful for text classification tasks. The separation of data makes it excellent for training models to distinguish between different classes, or in our case, newsgroup topics.  
该数据集被几乎均匀地划分到 20 个不同的新闻组中，每个新闻组对应一个独立的主题——这种分割是它特别适用于文本分类任务的主要原因之一。数据的隔离使其非常适合训练模型来区分不同的类别，或者在我们的例子中，区分新闻组主题。

From science and religion to politics and sports, the topics covered provide a diversified range of discussions. This diversity adds another layer of complexity and richness, similar to what we might experience with real-world data.  
从科学与宗教到政治与体育，涵盖的主题提供了多元化的讨论范围。这种多样性增添了另一层复杂性和丰富性，类似于我们从现实世界数据中获得的体验。
## Fetching and Understanding the Data Structure  
获取和理解数据结构

To load this dataset, we use the `fetch_20newsgroups()` function from the `sklearn.datasets` module in Python. This function retrieves the 20 newsgroup dataset in a format that's useful for machine learning purposes. Let's fetch and examine the dataset.  
为了加载此数据集，我们使用 Python 中 `sklearn.datasets` 模块的 `fetch_20newsgroups()` 函数。此函数以一种对机器学习有用的格式检索 20 个新闻组数据集。让我们获取并检查该数据集。

First, let's import the necessary libraries and fetch the data:  
首先，让我们导入必要的库并获取数据：
```python
# Importing necessary libraries
from sklearn.datasets import fetch_20newsgroups

# Fetch data
newsgroups = fetch_20newsgroups(subset='all')
```
The datasets fetched from sklearn typically have three attributes—`data`, `target`, and `target_names`. `data` refers to the actual content, `target` refers to the labels for the texts, and `target_names` provides names for the target labels.  
从 sklearn 获取的数据集通常具有三个属性—— `data` 、 `target` 和 `target_names` 。 `data` 指的是实际内容， `target` 指的是文本的标签，而 `target_names` 提供了目标标签的名称。

Next, let's understand the structure of the fetched data:  
接下来，让我们了解一下获取数据的结构：
```python
# Understanding the structure of the data
print("\n\nData Structure\n-------------")
print(f'Type of data: {type(newsgroups.data)}')
print(f'Type of target: {type(newsgroups.target)}')
```
We are fetching the data and observing the type of the `data` and `target`. The `type of data` tells us what kind of data structure is used to store the text data while the `type of target` shouts what type of structure is used to store the labels. Here is what the output looks like:  
我们正在获取数据并观察 `data` 和 `target` 的类型。 `type of data` 告诉我们使用哪种数据结构来存储文本数据，而 `type of target` 则表明使用哪种结构来存储标签。以下是输出结果：
```python
Data Structure
-------------
Type of data: <class 'list'>
Type of target: <class 'numpy.ndarray'>
```
As printed out, the `data` is stored as a list, and `target` as a numpy array.  
如打印输出所示， `data` 以列表形式存储，而 `target` 则以 NumPy 数组形式存储。
##### Diving Into Data Exploration  
深入数据探索

Now, let's explore the data points, target variables and the potential classes in the dataset:  
现在，让我们探讨一下数据集中的数据点、目标变量和潜在类别：
```python
print("\n\nData Exploration\n----------------")
print(f'Number of datapoints: {len(newsgroups.data)}')
print(f'Number of target variables: {len(newsgroups.target)}')
print(f'Possible classes: {newsgroups.target_names}')
```
We get the length of the `data` list to fetch the number of data points. Also, we get the length of the `target` array. Lastly, we fetch the possible classes or newsgroups in the dataset. Here is what we get:  
我们获取 `data` 列表的长度以获取数据点的数量。此外，我们获取 `target` 数组的长度。最后，我们获取数据集中可能的类别或新闻组。以下是我们得到的结果：
```python
Data Exploration
----------------
Number of datapoints: 18846
Number of target variables: 18846
Possible classes: ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']
```
##### Sample Data Preview 样本数据预览

Lastly, let's fetch and understand what a sample data point and its corresponding label looks like:  
最后，让我们获取并理解一个样本数据点及其对应标签的形态：
```python
print("\n\nSample datapoint\n----------------")
print(f'\nArticle:\n-------\n{newsgroups.data[10]}')
print(f'\nCorresponding Topic:\n------------------\n{newsgroups.target_names[newsgroups.target[10]]}')
```
The `Article` fetched is the 10th article in the dataset and `Corresponding Topic` is the actual topic that the article belongs to. Here's the output:  
获取的 `Article` 是数据集中的第 10 篇文章，而 `Corresponding Topic` 是该文章所属的实际主题。输出如下：
```python
Sample datapoint
----------------

Article:
-------
From: sandvik@newton.apple.com (Kent Sandvik)
Subject: Re: 14 Apr 93   God's Promise in 1 John 1: 7
Organization: Cookamunga Tourist Bureau
Lines: 17

In article <1qknu0INNbhv@shelley.u.washington.edu>, > Christian:  washed in
the blood of the lamb.
> Mithraist:  washed in the blood of the bull.
> 
> If anyone in .netland is in the process of devising a new religion,
> do not use the lamb or the bull, because they have already been
> reserved.  Please choose another animal, preferably one not
> on the Endangered Species List.  

This will be a hard task, because most cultures used most animals
for blood sacrifices. It has to be something related to our current
post-modernism state. Hmm, what about used computers?

Cheers,
Kent
---
sandvik@newton.apple.com. ALink: KSAND -- Private activities on the net.


Corresponding Topic:
------------------
talk.religion.misc
```
##### Lesson Summary 课程总结

Nice work! Through today's lesson, you've learned to fetch and analyze text data for text classification. If you've followed along, you should now understand the structure of text data and how to fetch and analyze it using Python.  
干得好！通过今天的课程，你已经学习了如何获取和分析用于文本分类的文本数据。如果你跟着学习了，你现在应该理解了文本数据的结构，以及如何使用 Python 获取和分析它。

But our journey to text classification is just starting. In upcoming lessons, we'll dive deeper into related topics such as cleaning textual data, handling missing values, and restructuring textual data for analysis. Each step forward improves your expertise in text classification. Keep going!  
但我们通往文本分类的旅程才刚刚开始。在接下来的课程中，我们将深入探讨相关主题，例如清理文本数据、处理缺失值以及重构文本数据以进行分析。每一步都将提升您在文本分类方面的专业知识。继续前进！
## 「Practice」
Excellent job, Space Voyager! Now, make a small alteration to the starter code: change it to **print out the first 150 characters of the 500th article** from our _20 Newsgroups dataset_, and also **display its corresponding topic**.  
干得好，太空旅行者！现在，对 st 做一个小小的改动
```python
# Import necessary libraries and modules

from sklearn.datasets import fetch_20newsgroups

  

# Fetch the dataset

newsgroups = fetch_20newsgroups(subset='all')

  

# Fetch the first 150 characters of the 500th article and its corresponding topic

print(f'\nArticle:')

print(f'{newsgroups.data[500][:150]}')

print(f'\nCorresponding Topic:')

print(f'{newsgroups.target_names[newsgroups.target[500]]}')
```
输出
```
Article:  
From: bluelobster+@cmu.edu (David O Hunt)  
Subject: Re: How I got saved...  
Organization: Carnegie Mellon, Pittsburgh, PA  
Lines: 44  
  
My first and most i  
  
Corresponding Topic:  
soc.religion.christian
```
## 「Practice」
Celestial Traveler, your journey continues! Fill in the blanks (`____`) to import and explore our dataset. We aim to extract and display the **last three articles** and their corresponding **topics**. Can you reveal what's at the end of our dataset?  
天体旅行者，你的旅程仍在继续！填写空格 ( `____` ) 以导入并探索我们的数据集。我们的目标是提取并显示最后三篇文章及其对应的主题。你能揭示我们数据集的末尾是什么吗？
```python
# Import necessary libraries

from sklearn.datasets import fetch_20newsgroups

  

# Fetch the dataset

newsgroups = ____(subset='all')

  

# Fetch last three articles

last_three_articles = newsgroups.____[-3:]

  

# Fetch the corresponding topics

corresponding_topics = [newsgroups.target_names[i] for i in newsgroups.____[-3:]]

  

# Display Last three articles and their corresponding topics

for i in range(3):

print(f'\nLast article {i+1}:')

print(f'{last_three_articles[i]}\n')

print(f'Corresponding Topic {i+1}:')

print(f'{corresponding_topics[i]}\n')
```





































