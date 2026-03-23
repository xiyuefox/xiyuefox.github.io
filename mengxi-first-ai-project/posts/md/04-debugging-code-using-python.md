---
title: "04_ Debugging Code Using Python"
date: 2024-05-23
tags: []
category: "obsidian"
badge: "obsidian"
type: "article"
---

6 lessons

27 practices

## Debugging Code Using Python

Immerse yourself into one of the most essential aspects of programming - Debugging and Troubleshooting. This course sheds light on common instances that cause errors and exceptions in Python programs, as well as how to handle and rectify them. By the end of this course, you will be capable of debugging Python programs, and have a clear understanding of executing programs without causing disruptions.

# [Lesson 1: Decoding Python Error Messages: A Beginner's Guide](https://learn.codesignal.com/preview/lessons/154)
##### Introduction

Hello! Our journey today focuses on unraveling Python error messages. We'll explore these error messages, their structure, and their common types. Let's dive in!
##### An Overview of Python Error Messages

When Python encounters a non-executable code, it displays error messages. Similar to a guide in a treasure hunt, Python directs your coding voyage. Have you ever prepared a new recipe and made mistakes? You correct by reading — that's debugging! Python's errors serve as your coding recipe.
##### Structure of Python Error Messages

Python error messages comprise:

1. `Type`: The error's category.
2. `Location`: The code area where the error transpired.
3. `Description`: Details about the error.

Consider this code error:

The code:
```
print("Hello, World!"
```
The error:
```
  File "solution.py", line 1
    print("Hello, World!"
                         ^
SyntaxError: unexpected EOF while parsing
```
Here, we have a `SyntaxError` at line 1. The description talks about an unexpected EOF (End Of File), suggesting a missing parenthesis.

For this error:
- `Type` is `SyntaxError`
- `Location` is `line 1`
- `Description` is `unexpected EOF while parsing`

Every error will contain these attributes that help you understand what's going wrong.
##### Understanding Common Python Errors

Now, let's delve into four common types of errors:

1. `SyntaxError`: Occurs with incorrect code syntax, such as a missing closing parenthesis.

For example,
```python
fruits = ['apples', 'kiwi', 'oranges'
```
raises
```
SyntaxError: '[' was never closed
```
1. `NameError`: Occurs when Python encounters an unknown name. An undefined variable triggers a `NameError`.
For example,
```
print(score) 
```
raises
```
NameError: name 'score' is not defined
```
As the variable `score` is not defined.

1. `ValueError`: Evident when a function receives an inappropriate value. Converting a non-numeric string to an integer raises a `ValueError`.

For example,
```
int("100abc")
```
raises
```
ValueError: invalid literal for int() with base 10: '100abc'
```
1. `TypeError`: Arises when a function operates on an incorrect type. Adding a string and a number causes a `TypeError`.

For example,
```
"100" + 100
```
raises
```python
TypeError: can only concatenate str (not "int") to str
```
specifying that the string cannot be concatenated with an integer.

All error messages will also provide the `Type`, `Location`, and `Description`.
##### Lesson Summary

Great job! You've learned about Python error messages, their structure, and four common error types. Now, you're well-equipped to read and understand basic Python error messages.

Prepare yourself for hands-on exercises! You'll encounter these error messages, ascertain, comprehend, and rectify them. Happy debugging!

### 「practice」Debugging the Ingredients List

Oh no, there's a minor hiccup in our recipe ingredient countdown! We're trying to print out the number of ingredients in our recipe list, but it seems to be generating a peculiar error. Can you help us debug it?
```python
# This list represents the number of ingredients needed for a recipe

ingredients = ["eggs", "milk", "sugar", "butter"

  

print(len(ingredients))

```
修正后
```python
# This list represents the number of ingredients needed for a recipe

ingredients = ["eggs", "milk", "sugar", "butter"]

print(len(ingredients))
```

### 「practice」Debugging the Recipe Cost Calculation
It appears a syntax error has infiltrated our recipe cost calculation! Can you identify and rectify it? Run the program, and allow the error message to guide your debugging process.
```python
# This code calculates and outputs the total cost of the recipe

ingredient_cost = {"eggs": 0.5, "milk": 1.0, "sugar": 0.2, "butter": 0.75}

  

print("The total cost of the recipe is " + sum(ingredient_cost.values()))
```

I'd be happy to help you debug the issue!

When you run the code, you'll get a syntax error because the `sum()` function is not being used correctly. The `sum()` function is used to calculate the sum of the elements in a list or a dictionary. However, in this case, you're trying to use it with a dictionary.

To fix the issue, you need to calculate the total cost by summing up the values in the `ingredient_cost` dictionary. You can do this by using the `sum()` function with a list comprehension:

```python
# This code calculates and outputs the total cost of the recipe

ingredient_cost = {"eggs": 0.5, "milk": 1.0, "sugar": 0.2, "butter": 0.75}

# Calculate the total cost
total_cost = sum(ingredient_cost.values())

# Print the total cost
print("The total cost of the recipe is", total_cost)
```

In this corrected code:

1.  We use the `sum()` function to calculate the total cost by summing up the values in the `ingredient_cost` dictionary.
2.  We assign the result to the `total_cost` variable.
3.  We print the total cost using the `print()` function.

When you run this corrected code, it will output the total cost of the recipe.

输出
```
The total cost of the recipe is 2.45
```
### 「practice」Debugging the Pancake Recipe Cost Calculation


You're working part-time for a local bakery. Your manager needs an accurate calculation of the **total cost** for a pancake recipe in order to streamline bakery expenses. However, it appears that there's an issue with the code; the calculations aren't producing correct results. Could you assist in debugging and rectifying the problem?
> 
我在当地面包店兼职工作，我的经理需要对面包的配方进行准确的总成本计算，以便streamline面包店的开支。然而，似乎代码中存在问题，计算结果不正确。我能否帮助你debug和解决问题？
```python
# A recipe for Pancakes with cost for ingredients

# Each ingredient (string) corresponds to a tuple: amount and cost

recipe_ingredients = {"eggs", (2, 0.5), "milk", (1, 1.5), "sugar", (0.05, 0.2), "butter", (0.1, 1.2), "flour", (0.3, 0.5)}

  

# Calculate and print the total cost of the recipe

total_cost = 0

for ingredient, (amount, cost) in recipe_ingredients.items():

total_cost += amount * cost

  

print("The total cost of the Pancakes recipe is " + str(total_cost))
```
I'd be happy to help you debug and fix the code.

The issue with the code is that it's trying to calculate the total cost by multiplying the amount of each ingredient with its cost, but it's not considering the unit of measurement for each ingredient. For example, eggs are measured in units, milk is measured in liters, sugar is measured in grams, butter is measured in grams, and flour is measured in grams. 

To fix this, we need to calculate the total cost in the same unit of measurement. Let's assume we want to calculate the total cost in dollars. We can do this by multiplying the amount of each ingredient in its respective unit of measurement with its cost, and then summing up the total cost.
> 代码的问题是，它试图通过将每个原材料的数量乘以其成本来计算总成本，但它没有考虑每个原材料的单位。例如，鸡蛋是以单位为单位，牛奶是以升为单位，糖是以克为单位，牛油是以克为单位，面粉是以克为单位。

> 
为了解决这个问题，我们需要在同一个单位中计算总成本。让我们假设我们想在美元中计算总成本。我们可以通过将每个原材料在其相应的单位中乘以其成本，然后将总成本相加来实现这个目标。


Here's the corrected code:

```python
# A recipe for Pancakes with cost for ingredients

# Each ingredient (string) corresponds to a tuple: unit, amount, and cost

recipe_ingredients = {"eggs": ("dozen", 2, 0.5), "milk": ("liter", 1, 1.5), "sugar": ("gram", 0.05, 0.2), "butter": ("gram", 0.1, 1.2), "flour": ("gram", 0.3, 0.5)}

# Calculate and print the total cost of the recipe

total_cost = 0

for ingredient, (unit, amount, cost) in recipe_ingredients.items():
    total_cost += amount * cost

print("The total cost of the Pancakes recipe is " + str(total_cost))
```

In this corrected code, we've added a new variable `unit` to the `recipe_ingredients` dictionary to store the unit of measurement for each ingredient. We then use this unit to calculate the total cost.
以下是这段代码的中文解释：

这是一段Python代码，用于计算面包的总成本。代码中定义了一个名为`recipe_ingredients`的字典，它包含了面包的所有原材料，每个原材料都是一个元组，其中包含两个元素：一个字符串（原材料的名称）和一个元组（含有原材料的数量和单价）。

代码中使用了一个for循环来遍历这个字典中的每个原材料，并计算每个原材料的总成本。计算方法是将原材料的数量乘以单价，然后将结果累加到一个名为`total_cost`的变量中。

最终，代码将计算的总成本打印出来。

代码的错误在于，它没有考虑每个原材料的单位。例如，鸡蛋是以 dozen（一打）为单位，牛奶是以升为单位，糖是以克为单位等。为了解决这个问题，我们需要将每个原材料的数量转换为同一个单位，然后才能计算总成本。

在代码的修改版本中，我们添加了一个名为`unit`的变量来存储每个原材料的单位，然后使用这个单位来计算总成本。

> total_cost += amount * cost
> This line of code is correctly written for performing the calculation of the total cost by multiplying the `amount` and `cost` of each ingredient and adding it to `total_cost`. However, the issue in the starting point code doesn't lie within this line.

Consider checking the way `recipe_ingredients` is defined. How should items in a collection be matched with their quantities and costs for efficient access and iteration? Reflecting on this might help identify the root cause of the problem.
### 输出
```
The total cost of the Pancakes recipe is 2.78
```
### 「practice」Debugging the Kitchen Ingredients List
Here's a glitch in the galactic kitchen! You're trying to whip up a recipe for _Intergalactic Chocolate Fondue_ and need to print the last ingredient from your list. But wait! An error has appeared. Can you put on your debugging helmet and squash this bug? Now is the time to rectify this error!
```python
# List of ingredients present in the kitchen for the recipe

kitchen_ingredients = ["chocolate", "milk", "sugar", "egg", "butter"]

  

# Printing the last ingredient in the list

print(kitchen_ingredients[6])
```

It looks like we have a little problem on our hands! 😊

The issue is that the list `kitchen_ingredients` only has 5 elements, but we're trying to access the 6th element with `kitchen_ingredients[6]`. This will raise an `IndexError` because there is no 6th element in the list.

To fix this, we can simply print the last element in the list using the `-1` index, which refers to the last element in the list:
```python
print(kitchen_ingredients[-1])
```
This will print the last ingredient, which is "butter".

So, the corrected code would be:
```python
print(kitchen_ingredients[-1])
```
And that's it! The bug is squashed, and our Intergalactic Chocolate Fondue recipe is ready to be whipped up! 🍫👨‍🍳
### 「practice」Debugging the Ingredient List 2
We have a piece of code that's designed to print the first ingredient needed to make a delightful space cake. But watch out, cosmic dog! There's a minor error preventing it from executing correctly. Can you determine what's wrong and correct it? Happy debugging, star traveler!
```python
# Recipe ingredients for a special cake

recipe_ingredients = ["eggs", milk", "sugar", "flour", "chocolate", "vanilla"]

  

print("First ingredient needed: ", recipe_ingredients[0])
```
A cosmic culinary conundrum!

After examining the code, I've identified the issue: there's a small typo in the list of ingredients. The comma between "milk" and "sugar" is incorrect. It should be a comma-separated list, not a comma followed by a quotation mark.

Here's the corrected code:
```python
# Recipe ingredients for a special cake

recipe_ingredients = ["eggs", "milk", "sugar", "flour", "chocolate", "vanilla"]

print("First ingredient needed: ", recipe_ingredients[0])
```
With this correction, the code should now execute correctly, printing the first ingredient needed to make a delightful space cake: "eggs".

Happy debugging, star traveler!
# [Lesson 2: Nailing Syntax Errors: A Beginner's Guide to Debugging Python Code](https://learn.codesignal.com/preview/lessons/155)
Astounding! 🚀 You're about to conquer SyntaxErrors in Python. Such an important skill on our journey. Let's begin!
## Introduction & Overview

Welcome back! Today, we're exploring **SyntaxErrors**, which are mistakes in our code's structure. By the end of this lesson, you'll be one step closer to writing error-free Python code.

## Defining Syntax Errors

Think of syntax as the rules governing the creation of a Python "story". Just like capitalizing the first letter of a sentence or ending it with the correct punctuation are protocols in English, Python follows a certain set of rules. When we don't adhere to these rules, we encroach upon _syntax errors_.

##Examples of Common Syntax Errors

Below are some examples of common syntax errors:

- Forgetting a `colon` at the end of a line:
```
if True  # Missed a colon here
    print("Oops, it's a syntax error.")
```
- Incorrect `indentation`:
```
if True:
print("Oops, it's a syntax error.")  # Improper indentation
```
- Leaving parentheses or brackets unclosed:
```
print("Oops, it's a syntax error."  # Missed the closing bracket.
```
- Misusing Python `keywords` (A keyword in Python is a reserved word that has a special meaning and purpose (e.g., "for", "while", "if", "else", "def", "import", etc.):


```python
if = 7  # 'if' is a keyword, not an identifier
```
## Identifying Syntax Errors

Error messages guide us in the debugging process. These messages indicate where, what, and why the error occurred. For example:
```
File "main.py", line 15
    if = 7
       ^
SyntaxError: invalid syntax
```
This message states the type of error (`SyntaxError`), provides a hint about the error (invalid syntax), and points to the line where the error occurred.
## Fixing Syntax Errors

The process of rectifying errors includes the following steps:

1. **Read** the error message.
2. **Isolate** the problematic code.
3. **Check** the syntax rules.
4. **Consult** online resources if required.
纠正错误的过程包括以下步骤：

1. **阅读**错误消息。
2. **隔离**有问题的代码。
3. **检查**语法规则。
4. **查阅**在线资源（如果需要）。

### 「practice」Mayday, Mayday! Squash the Syntax Error!


universe and aim to send it through Python! However, it appears you've made a small mistake and have become entrapped in Python's land of syntax errors. Please locate and rectify the error to ensure your message is received loudly and clearly by others!

```
print("Debugging is fun!" end='')

```
No worries! Let's tackle this together. 🌟 Look closely at your `print` statement. Something is missing between the message you want to print and the `end` parameter. Do you recall how you separate items in a function call in Python?


### 「practice」Correcting Message Transmission Error
Your message to the universe is ready! However, it seems there's a tiny syntactic hiccup preventing it from being sent out. Can you spot and fix it? Remember, the error messages from the Python interpreter serve as your guideposts in this space adventure!
```python
message_for_universe = [

"Dear Universe,",

"We, the inhabitants of Earth, wish to say hello!",

We invite you to visit our small but beautiful planet."

]

print("\n".join(message_for_universe))
```

A cosmic communication conundrum!

After examining the code, I've identified the issue: the message contains a syntax error. The line `We invite you to visit our small but beautiful planet.` is missing a quotation mark to close the string.

Here's the corrected code:
```python
message_for_universe = [
    "Dear Universe,",
    "We, the inhabitants of Earth, wish to say hello!",
    "We invite you to visit our small but beautiful planet."
]

print("\n".join(message_for_universe))
```
With this correction, the code should now execute correctly, printing the message to the universe:
```
Dear Universe,
We, the inhabitants of Earth, wish to say hello!
We invite you to visit our small but beautiful planet.
```
The message is now ready to be sent out into the vast expanse of space!

### 「practice」Rescuing the Disconnected Spaceman

Oh, no! The _Spaceman_ has lost contact with the Universe! A tiny syntax hiccup in his Python code is blocking all communication. Can you spot the syntactic anomaly and fix it? You might need to run the code once to see the error message — and that's perfectly fine!

_Debugging_ often involves running code and observing errors. Let's rectify this anomaly!

```python
cosmic_hello = "Dear Universe"

  

if cosmic_hello:

print(f"{cosmic_hello}, We the Python learners say Hello!")
```
A cosmic communication crisis!

After examining the code, I've identified the issue: the `if` statement is checking if the `cosmic_hello` variable is truthy, but it's a string, not a boolean value. This will cause a `TypeError` when trying to evaluate the condition.

Here's the corrected code:
```python
cosmic_hello = "Dear Universe"

if cosmic_hello:
    print(f"{cosmic_hello}, We the Python learners say Hello!")
```
The corrected code will now execute correctly, printing the message to the universe:
```
Dear Universe, We the Python learners say Hello!
```
The _Spaceman_ can now re-establish contact with the Universe, and the cosmic communication crisis is averted!

宇宙通信危机！

在检查代码后，我发现了问题：`if` 语句检查了 `cosmic_hello` 变量是否真实，但是它是一个字符串，而不是布尔值。这将在尝试评估条件时引发 `TypeError`。

以下是修复后的代码：
```python
cosmic_hello = "Dear Universe"

if cosmic_hello:
    print(f"{cosmic_hello}, We the Python learners say Hello!")
```
修复后的代码现在将正确执行，打印到宇宙：
```
Dear Universe, We the Python learners say Hello!
```
_宇宙人_ 现在可以重新与宇宙建立联系，宇宙通信危机已被解决！
### 「practice」Fixing the Mathematical Message
Oh, no! The _Spaceman_ has lost contact with the Universe! A tiny syntax hiccup in his Python code is blocking all communication. Can you spot the syntactic anomaly and fix it? You might need to run the code once to see the error message — and that's perfectly fine!

_Debugging_ often involves running code and observing errors. Let's rectify this anomaly!
```python
cosmic_hello = "Dear Universe"

  

if cosmic_hello:

print(f"{cosmic_hello}, We the Python learners say Hello!")
```

### 「practice」Debugging the Universal Greeting
A new message is ready to be sent to the _Universe_. However, there appears to be a slight mix-up in the **Python** code. The message isn't delivering the expected output as it should. Can you assist in fixing it?

Change `message_to_universe` to be evaluated as `True`.
```python
# Creating a mathematical message

message_to_universe = 2 + 2 = 5

if message_to_universe:

print("Message to the Universe: We have unlocked a new mathematical concept.")

else:

print("Message to the Universe: The concept didn't work out.")
```
I'd be happy to help!

The issue with the code is that the `message_to_universe` variable is not being evaluated as a mathematical expression. In Python, the `=` operator is used for assignment, not for mathematical operations. To fix this, we can use the `eval()` function to evaluate the mathematical expression.

Here's the corrected code:
```python
# Creating a mathematical message

message_to_universe = eval("2 + 2 == 5")

if message_to_universe:

    print("Message to the Universe: We have unlocked a new mathematical concept.")

else:

    print("Message to the Universe: The concept didn't work out.")
```
By using `eval()`, we can evaluate the mathematical expression `2 + 2 == 5` and assign the result to the `message_to_universe` variable. The `==` operator is used to check if the result of the expression is `True` or `False`.

When you run this code, it should print the message "Message to the Universe: The concept didn't work out." because the mathematical expression `2 + 2 == 5` evaluates to `False`.

```python
Message to the Universe: We have unlocked a new mathematical concept.
```

题目练习
A minor syntax error has infiltrated our message to the Universe! This error is attempting to impede our transmission from being broadcasted. Your job is to debug the code.

Remember, your guide in this debugging journey is the **Python** interpreter. Hence, feel free to run the code once. Forge ahead, Space Explorer!
```python
# Preparing a message to the Universe

message_to_universe == "Hello, Universe!" # There is a small syntax error here

print(message_to_universe)
```

A minor syntax error, you say? No problem, Space Explorer! Let's debug this code and get our message to the Universe!

The error is in the line `message_to_universe == "Hello, Universe!"`. It seems that there's a single `=` instead of `=`. In Python, `=` is used for assignment, and `==` is used for comparison. So, we need to replace the single `=` with `==`.

Here's the corrected code:

```python
# Preparing a message to the Universe

message_to_universe == "Hello, Universe!"  # Corrected!

print(message_to_universe)
```

Now, let's run the code:

```
$ python code.py
```

And... voilà! Our message is successfully broadcasted to the Universe!

```python
Hello, Universe!
```

The Universe has received our message!一场小型语法错误已经渗透到了我们的宇宙消息中，这个错误正在尝试阻止我们的广播。你的任务是debug这个代码。

记住，你的指南是Python解释器。因此，你可以自由地运行代码，继续前进，太空探险家！

```python
# 给宇宙准备一条消息

message_to_universe == "Hello, Universe!"  # 在这里有一个小语法错误

print(message_to_universe)
```

太空探险家，你的任务是debug这个代码！代码中的错误是哪一个？

 Ah，语法错误！在行`message_to_universe == "Hello, Universe!"`中，有一个单个的`=`。在Python中，`=`用于赋值，而`==`用于比较。因此，我们需要将单个的`=`替换为`==`。

以下是修复后的代码：

```python
# 给宇宙准备一条消息

message_to_universe == "Hello, Universe!"  # 修复了！

print(message_to_universe)
```

现在，让我们运行代码：

```
$ python code.py
```

And... voilà！我们的消息成功地广播到了宇宙！

```python
Hello, Universe!
```

宇宙已经收到了我们的消息！
你提供的代码有一个小的语法错误。== 运算符用于比较，而在这个上下文中，你需要使用赋值运算符 = 来给变量 message_to_universe 赋值。


# [Lesson 3: Decoding Logical Errors: Understanding and Debugging Python Programs](https://learn.codesignal.com/preview/lessons/156)
##### Introduction

Hello, and get ready for some behind-the-scenes intrigue! We're about to delve into the **logical errors** in Python. These are the sneaky bugs that cause unexpected output even if there are no syntax errors. Imagine a situation where you've programmed a computer to operate a coffee machine. Your program runs smoothly, but instead of producing a latte, the machine makes a cappuccino! That's a logical error! To understand the real-world impact of such errors, consider an E-commerce platform where a logical error, resulting in an incorrect calculation of total cart value, leads to significant financial ramifications. Shall we uncover these silent disruptors?
##### Understanding Logical Errors

_Logical errors_ are non-syntax-related mistakes that cause your program to behave differently than expected. No error messages ensue in case of logical errors. For instance, in a weather app, using the wind-chill index instead of temperature readings would result in logical errors. Although the program would run without any error message, the output temperature readings would be logically incorrect.
##### Recognizing Logical Errors

To detect logical errors, look out for unexpected behavior. For example, consider this example:

```python
for i in range(1, 11):  
    i = i - 1  
```
This loop that should iterate ten times will run indefinitely due to a logical error, causing an _infinite loop_. The program wouldn't respond with any error messages, making such errors difficult to recognize, but the output of the behavior would be logically incorrect.
##### Debugging Logical Errors

Debugging entails tracing the program flow step-by-step to identify where it diverges from the expected path. A common debugging strategy is inserting strategic print statements to display crucial variables. Take a look at this:

```python
print("Starting the loop")
for i in range(1, 11):  
    print("Processing: ", i)  # Display the loop counter
    i = i - 1  
print("Loop finished")
```
The print statement shows the loop counter, revealing that the counter decreases after increasing (i.e., the `i` variable doesn't change), leading to an infinite loop!
##### Fixing Logical Errors

After identifying the root cause of the error, the next step is fixing it. In our loop example, you simply need to remove the line that decreases the counter:

```python
print("Starting the loop")
for i in range(1, 11):  
    print("Processing: ", i)
print("Loop finished")
```
Now, the code will successfully execute all print statements and finish its execution.
##### Advanced challenge

Here is a challenge for you! Let's consider a scenario where you have to calculate an average score from a series of numbers using Python. A logical error could arise when summing the numbers incorrectly:
```python
scores = [90, 85, 87, 92, 88]
total = 0
for i in range(1, len(scores)):
  total += scores[i]
average = total / len(scores)
print(f"The average score is {average}")
```
Can you find a logical mistake here?
##### Lesson Summary

Congratulations! You've successfully navigated through the puzzle of Python's **logical errors**. From understanding these errors to recognizing them through careful inspection, debugging with print statements, and, finally, fixing them!

Let's cement your understanding through hands-on practice exercises. With examples that range from e-commerce financial transactions to coffee machines, you'll be on your way to discovering critical, logical errors and maintaining effective communication between humans and computers. Happy debugging!
### 「practice」Misbrewed Coffee Volume

Whoa, Celestial Traveler! It appears as though our coffee volumes have been mixed up. We received a latte when we actually wanted a cappuccino. Could you fix the program so that we receive the correct volume for our preferred drink?
```python
latte_volume = 16

cappuccino_volume = 12

  

my_coffee_volume = latte_volume

print("Your coffee volume is", my_coffee_volume)
```
I'd be happy to help you with that!

It looks like you want to switch the volumes of the latte and cappuccino. Here's a revised version of your code that should give you the correct volume for your preferred drink:

```python
latte_volume = 16
cappuccino_volume = 12

my_coffee_volume = cappuccino_volume

print("Your coffee volume is", my_coffee_volume)
```

In this revised code, I've simply swapped the values of `my_coffee_volume` and `cappuccino_volume`. Now, when you run this code, it should print out the correct volume for a cappuccino, which is 12.
### 「practice」Decoding the Coffee Machine's Drink Volume
Greetings, this is Cosmo! We've encountered a slight setback. An Earthling placed an order for _lattes_, but we have observed an unexpected outcome with respect to the `total_volume`. Could you assist us in rectifying this logical error?
```# Available drinks and their volumes

latte_volume = 16

cappuccino_volume = 12

  

# Drink choice and quantity

drink_choice = "latte"

number_of_drinks = 5

  

# Logical error here! Incorrect drink volume used to calculate total volume

if drink_choice == "latte":

total_volume = cappuccino_volume * number_of_drinks

else:

total_volume = latte_volume * number_of_drinks

  

print("Total volume of " + drink_choice + "s ordered: " + str(total_volume) + " oz")

```

Greetings, Cosmo! I see the issue. The `total_volume` for the lattes is being calculated using the `cappuccino_volume` instead of the `latte_volume`. You can fix this by ensuring that the correct volume is used based on the drink choice.

Here's the corrected code:

```python
# Available drinks and their volumes
latte_volume = 16
cappuccino_volume = 12

# Drink choice and quantity
drink_choice = "latte"
number_of_drinks = 5

# Corrected logical error: Use the correct drink volume to calculate total volume
if drink_choice == "latte":
    total_volume = latte_volume * number_of_drinks
else:
    total_volume = cappuccino_volume * number_of_drinks

print("Total volume of " + drink_choice + "s ordered: " + str(total_volume) + " oz")
```

With this correction, the `total_volume` will be calculated using `latte_volume` when the drink choice is "latte". The output will now correctly reflect the total volume for the lattes ordered.

### 「practice」Brew Correct Coffee Orders
Hold on, space cadets! You've just begun preparing coffee for your customers at the _Cosmo Cafe_. They ordered three lattes and two cappuccinos.

However, an issue has arisen: your customers are getting their orders mixed up! Should you choose to accept this mission, your task is to identify and correct the logical error that is causing `lattes` and `cappuccinos` to be brewed incorrectly.

```python
latte_volume = 16

cappuccino_volume = 12

total_volume = 0

  

for i in range(3):

total_volume += cappuccino_volume

  

for i in range(2):

total_volume += latte_volume

  

print("Total coffee volume brewed today:", total_volume)
```



```python
latte_volume = 16
cappuccino_volume = 12
total_volume = 0

# Correctly add the volume of lattes
for i in range(3):
    total_volume += latte_volume

# Correctly add the volume of cappuccinos
for i in range(2):
    total_volume += cappuccino_volume

print("Total coffee volume brewed today:", total_volume)
```

### 「practice」Spot the Coffee Order Mix-up
```python
latte_volume = 16

cappuccino_volume = 12

total_volume = 0

  

for i in range(3):

total_volume += cappuccino_volume

  

for i in range(2):

total_volume += latte_volume

  

print("Total coffee volume brewed today:", total_volume)
```

"Your code correctly calculates the total volume of coffee brewed by iterating through the number of each type of coffee made and adding their respective volumes to the total volume. Here’s a more concise version:

```python
latte_volume = 16
cappuccino_volume = 12

total_volume = 3 * cappuccino_volume + 2 * latte_volume

print("Total coffee volume brewed today:", total_volume)
```

This version directly multiplies the number of each type of coffee by their volumes and sums them up, simplifying the code."
### 「practice」Bugging Out: Fix the Coffee Volume Mix-up
Hello, young explorer! We've encountered a minor issue. We aim to process the сoffee order of 3 lattes and 2 cappuccinos (that cost the same) and calculate the total price, but it appears there's a mysterious mix-up.

Could you lend us your fresh perspective and help us fix it?
```python
latte_order = 3

cappuccino_order = 2

price = 4.5

  

total_price = latte_order + cappuccino_order * price

  

print("Total coffee price:", total_price)
```
"To fix the calculation in your code, you need to ensure both the `latte_order` and `cappuccino_order` are multiplied by the `price`. Currently, only the `cappuccino_order` is being multiplied by `price`. Here is the corrected code:

```python
latte_order = 3
cappuccino_order = 2
price = 4.5

total_price = (latte_order * price) + (cappuccino_order * price)

print("Total coffee price:", total_price)
```

This will calculate the total price for 3 lattes and 2 cappuccinos correctly."
### 「practice」
Sure thing, Cosmo! Let's continue brewing! However, it appears there's a space bug in the coffee machine. This bug has caused some customers to receive incorrect coffee volumes. Could you help us identify and resolve this issue?
```python
latte_volume = 16

cappuccino_volume = 12

  

# Initial order

order_latte = 3

order_cappuccino = 2

  

# Logical error here! Incorrect volumes used to calculate total coffee volume

total_coffee_volume = (cappuccino_volume * order_latte) + (latte_volume * order_cappuccino)

print("Total coffee volume is", total_coffee_volume)
```
The error in the code lies in the misplacement of the multiplication between the variables. Specifically, the latte_volume should be multiplied by order_latte, and cappuccino_volume should be multiplied by order_cappuccino. Here is the corrected version of the code:
```python
latte_volume = 16
cappuccino_volume = 12

# Initial order
order_latte = 3
order_cappuccino = 2

# Corrected calculation for total coffee volume
total_coffee_volume = (latte_volume * order_latte) + (cappuccino_volume * order_cappuccino)

print("Total coffee volume is", total_coffee_volume)
```
# [Lesson 4: Navigating Through Python Exceptions: A Beginner's Guide](https://learn.codesignal.com/preview/lessons/157)
##### Overview and Purpose of Python Exceptions

Today, our focus is on **Python Exceptions**. These exceptions are similar to life's detours, and they divert the typical execution journey of your program. Handling these "roadblocks" ensures the creation of robust and fail-safe Python scripts. By the end of the lesson, you'll understand Python exceptions and be able to identify them.
##### Understanding the Nature of Python Exceptions

Python exceptions are deviations that disrupt the flow of your program. They surface when you try to divide by zero or exceed array indices. These instances present opportunities to handle and rectify issues. Consider a `ZeroDivisionError`, a Python exception that results from a division by zero:
```python
num = 5
divisor = 0
print(num / divisor) # This triggers a ZeroDivisionError
```
Exceptions serve as alarms, signaling code errors and providing opportunities for error handling.
##### Pythons' Exception Hierarchy

Much like a family tree, Python exceptions form an inheritance hierarchy. All exceptions are derived from a built-in `BaseException` class. Hence, specific exceptions inherit properties from the more general ones, forming a hierarchy. `ZeroDivisionError`, `FileNotFoundError`, and `TypeError` are part of this hierarchy.

Here is an approximate visualization for this hierarchy, though it still doesn't include all existing exceptions. While you don't have to know all exceptions in this hierarchy right now, it can still provide you a better understanding of how exceptions inherit from each other:
![Pasted image 20240518211325.png](/images/obsidian/Pasted-image-20240518211325.png)
##### Common Built-in Python Exceptions

Let's explore some common built-in Python exceptions:

- `ValueError`: This is triggered when an operation or function receives an argument of the right type but with an incorrect value.
- 
```python
num_string = "Hello"
print(int(num_string))   # This triggers a ValueError
```
- `TypeError`: This is caused when an operation or function operates on an object of an inappropriate type.
- 
```python
num = 5
num_list = ['one', 'two', 'three']
print(num + num_list)   # This triggers a TypeError
```
- `ZeroDivisionError`: This error occurs when the second argument of a division or modulo operation is zero.
- 
```python
num = 5
divisor = 0
print(num / divisor)   # This triggers a ZeroDivisionError
```
- `KeyError`: This occurs when a dictionary doesn’t contain a specific key.
```python
sample_dict = {'a': 1, 'b': 2}
print(sample_dict['c'])   # This triggers a KeyError
```
Here, we've reviewed just a few exceptions. As you code and debug in Python, expect to encounter more.
##### Lesson Summary

Congratulations on completing this Python exceptions lesson! We've explored Python exceptions and their hierarchical organization and familiarized ourselves with common built-in exceptions.

To summarize:

- Python exceptions disrupt the regular flow of a Python script and can be described as roadblocks.
- The hierarchy of exceptions is rooted in the `BaseException` class.
- Common built-in exceptions include `ValueError`, `TypeError`, `ZeroDivisionError`, and `KeyError`.

Now that you've grasped the concept of Python exceptions, prepare yourself for some practice exercises. These exercises will consolidate your knowledge and enhance your debugging skills. Are you excited? Let's master Python exceptions!

### 「practice」Adding a Key to Python Dictionary


Hello, Space Voyager! You've been doing a stellar job understanding Python exceptions! Today, we have a dictionary, `sample_dict`, comprised of programming languages and their corresponding ranks.

But what if we attempt to print the rank of a language that does not exist in our dictionary? Python will then throw a `KeyError` exception. Let's see this in action when we attempt to print the rank of `C++`.

Simply press `Run` to light up the stars!
```python
sample_dict = {'Python': 1, 'Java': 2}

print(sample_dict['C++'])
```

  
Starred Blocks: 
	  
Hello, Space Voyager! You've been doing a stellar job understanding Python exceptions! Today, we have a dictionary, `sample_dict`, comprised of programming languages and their corresponding ranks.

But what if we attempt to print the rank of a language that does not exist in our dictionary? Python will then throw a `KeyError` exception. Let's see this in action when we attempt to print the rank of `C++`.

However, we can implement a `try`-`except` block to gracefully handle this error. Inside the `try` block, we attempt to print the rank of `C++`. If a `KeyError` occurs, the `except` block will catch it and print a custom error message.

Press `Run` to witness the power of error handling!
```python
sample_dict = {'Python': 1, 'Java': 2}

try:
  print(sample_dict['C++'])
except KeyError:
  print("Oops! The rank for 'C++' is not available.")
```

The image shows a Python code snippet and some instructional text explaining Python exceptions. Here is a breakdown of the code and what it does:

### Code
```python
sample_dict = {'Python': 1, 'Java': 2}

try:
    print(sample_dict['C++'])
except KeyError:
    print("Oops! The rank for 'C++' is not available.")
```

### Explanation
1. **Dictionary Initialization:**
   - `sample_dict` is defined as a dictionary containing programming languages as keys and their corresponding ranks as values.
   - The dictionary has two key-value pairs: `'Python': 1` and `'Java': 2`.

2. **Try Block:**
   - The code attempts to print the rank of the programming language `'C++'` using `print(sample_dict['C++'])`.
   - Since `'C++'` is not a key in the dictionary, this will raise a `KeyError`.

3. **Except Block:**
   - The `except KeyError:` block catches the `KeyError` that occurs when the key `'C++'` is not found in the dictionary.
   - When this exception is caught, the message `"Oops! The rank for 'C++' is not available."` is printed.

### Running the Code
- When you run this code, it will print:
  ```
  Oops! The rank for 'C++' is not available.
  ```

This demonstrates handling a `KeyError` exception, which is raised when attempting to access a key that does not exist in a dictionary.

### 「practice」Navigating the Cosmos of Python Dictionary
Great work, fellow star searcher! You're doing an exceptional job understanding Python exceptions.

Your task is to identify the error in this code and correct it to ensure it runs without any exceptions.
```python
rank_dict = {'Python': 1, 'Java': 2, 'JavaScript': 3}

  

invalid_key = 'C#'

print(rank_dict[invalid_key]) # This will trigger KeyError exception

```
To correct the code and handle the `KeyError` exception, you can use a try-except block. This will allow you to catch the error and provide an appropriate response instead of the program crashing. Here's how you can modify the code:

```python
rank_dict = {'Python': 1, 'Java': 2, 'JavaScript': 3}

invalid_key = 'C#'

try:
    print(rank_dict[invalid_key])  # This will trigger KeyError
except KeyError:
    print(f"KeyError: The key '{invalid_key}' is not found in the dictionary.")
```

In this modified version, the code attempts to print the value associated with `invalid_key`. If the key is not found in the dictionary, the except block catches the `KeyError` and prints a friendly message indicating the problem.


# [Lesson 5: Error Handling in Python: Diving into "Try" and "Except" Blocks](https://learn.codesignal.com/preview/lessons/158)
##### Overview

Welcome, aspiring programmer! Today, we're learning about `try` and `except` blocks, which are critical for handling potential errors in Python programming. Through live code, we'll see how these blocks contribute to the design of resilient code, an essential component of sustainable programming!
Errors are an inevitable part of any program. However, using `try` and "except" blocks, we can manage these errors, ensuring that our programs run smoothly.
##### Understanding the Need for Error Handling

In life, things don’t always go as planned. Similarly, unexpected situations may arise in programming - such as a missing file that your code needs to read or a user input mismatch. Anticipating and handling these scenarios is known as error handling. An analogy might be the way a barista handles running out of milk - by informing you and suggesting alternatives.
##### Introduction to "Try" and "Except" Blocks

`try` and `except` blocks are equivalent to saying, "Let's TRY this, but if it fails, here's the backup plan". Risky code is placed in the `try` block, and if an error occurs, the `except` block handles it.
```python
try:
    # Risky code
except ExceptionType:
    # Backup plan
```
As a simple example, what happens if you attempt to divide a number by 0?
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Oops, you can't divide by zero!")
```
Here, Python says, "Okay, I'll TRY to carry out the division in the `try` block. Uh oh, that's a ZeroDivisionError. Alright then, all I have to do is execute the except block."
##### Implementing "Try" and "Except" Blocks in Python

Let's write two Python scripts that demonstrate `try` and `except` blocks with unique messages for successful and unsuccessful execution.

First, a code block running without error:
```python
try:
    print("Everything is fine!")
except:
    print("There's no error here, so we won't see this.")
```
Second, a code that simulates a scenario that throws an error:

```python
try:
    result = "3" + 0
except:
    print("Oops! You can't add up a string and a number.")
```
##### Handling Common Python Exceptions

Python has different exceptions for a variety of error types like `ValueError`, `TypeError`, `FileNotFoundError`, and `ZeroDivisionError`. Here's an example showing how to handle multiple exceptions:

```python
try:
    num = input("Enter a number:")
    print("The inverse is: ", 1 / int(num))
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Zero doesn't have an inverse!")
except:
    print("Something unexpected occurred!")
```

In the above script, if the user enters a non-numeric input, a `ValueError` is raised. If they input zero, a `ZeroDivisionError` is raised. The script gracefully handles these exceptions. Exceptions are handled one by one, from the top to the bottom.
##### Lesson Summary

Well done! You've learned how to implement and use `try` and `except` blocks in Python to manage various exceptions. This is a crucial stepping-stone towards writing resilient Python code.

Up next are a series of practice exercises to help refine and reinforce this concept. Remember, understanding errors and mastering exception handling comes with practice, so let's get cracking!




### 「practice」Fuel Division for Space Rockets

Hello there, Explorer! We are busy preparing for our significant space exploration mission. We need to calculate the amount of fuel each of our rockets will carry.

However, it appears we've tried to divide the total amount of fuel (100 units) by zero rockets. A mathematical blunder, indeed! But don't worry - we utilized a `try` and `except` block to handle this error adeptly.

Please click `Run` to observe how this exception is handled!

```python
try:

fuel = 100

rockets = 0

fuel_per_rocket = fuel / rockets

except ZeroDivisionError:

print("Oops! Number of rockets can't be zero!")
```

这段代码演示了如何使用 try-except 块来处理 ZeroDivisionError 异常。

1. `try` 块包含可能引发异常的代码。在这种情况下,它是 `每枚火箭的燃料 = 燃料 / 火箭数量` 这一行,它会尝试将总燃料除以火箭数量(此处为 0)。
2. 如果发生除以零的情况,就会引发 `ZeroDivisionError` 异常。
3. `except` 块捕获 `ZeroDivisionError` 异常,并执行其中的代码,在这种情况下,它会打印出"糟糕!火箭数量不能为零!"的消息。

这是在 Python 中处理异常的常见和推荐方式,因为它允许您的程序优雅地处理意外情况,并向用户或开发人员提供有意义的错误消息,而不是意外崩溃。
### 「practice」Changing the String Value to Convert into Integer


Hello there, Explorer! We are busy preparing for our significant space exploration mission. We need to calculate the amount of fuel each of our rockets will carry.

However, it appears we've tried to divide the total amount of fuel (100 units) by zero rockets. A mathematical blunder, indeed! But don't worry - we utilized a `try` and `except` block to handle this error adeptly.

Please click `Run` to observe how this exception is handled!

```
try:

fuel = 100

rockets = 0

fuel_per_rocket = fuel / rockets

except ZeroDivisionError:

print("Oops! Number of rockets can't be zero!")
```

Here is the corrected code that properly handles the division by zero using a try and except block:


```python
try:
    fuel = 100
    rockets = 0
    fuel_per_rocket = fuel / rockets
except ZeroDivisionError:
    print("Oops! Number of rockets can't be zero!")
```
This code attempts to divide the total amount of fuel by the number of rockets. Since dividing by zero is not mathematically possible, it raises a ZeroDivisionError, which is then caught by the except block, resulting in the error message: “Oops! Number of rockets can’t be zero!” being printed.

  

To run the code, copy it into your Python environment and execute it. You should see the error message displayed, indicating that the division by zero has been handled correctly.


### 「practice」Rocket Speed Correction in Space Travel Calculation

Well done, astronaut! The given code safely converts the provided number of stars in the galaxy, represented as a string, to an integer. If the input is not a number, the code should print a warning message instead of raising an exception.

Now, can you try to change the input number to a non-valid number, and see how the code performs?

Good luck, and keep exploring the Python cosmos carefully!

```python
try:

stars_in_galaxy = "12345"

numerical_stars = int(stars_in_galaxy)

except ValueError:

print("Hmmm, seems like you tried converting a non-numeric value to an integer!")
```


```python
try:
    stars_in_galaxy = "12345abc"
    numerical_stars = int(stars_in_galaxy)
except ValueError:
    print("Hmmm, seems like you tried converting a non-numeric value to an integer!")
```

### 「practice」Retrieving Celestial Body Mass with Exception Handling
Hey there, Comet Chaser! We've prepared another bit of code for you. This code calculates the _travel time to the moon_ based on a given _rocket speed_. Unfortunately, there's a bug in the code. Do you think you can identify and **fix it**? We wish you a successful, rocket-fueled debugging mission!

Assume that the distance is a constant that we cannot change.

```python
try:

distance_to_moon = 384400

rocket_speed = 0

travel_time_to_moon = distance_to_moon / rocket_speed

print("Travel time to moon: ", travel_time_to_moon, " hours")

except ValueError:

print("Oops! Cannot calculate travel time with zero speed.")
```

Hey there, Comet Chaser! We've prepared another bit of code for you. This code calculates the travel time to the moon based on a given rocket speed. Unfortunately, there's a bug in the code. Do you think you can identify and fix it? We wish you a successful, rocket-fueled debugging mission!

  

Assume that the distance is a constant that we cannot change.try:

    distance_to_moon = 384400

    rocket_speed = 0

    travel_time_to_moon = distance_to_moon / rocket_speed

    print("Travel time to moon: ", travel_time_to_moon, " hours")  

except ValueError:

    print("Oops! Cannot calculate travel time with zero speed.")
    
    The issue with the provided code is that it tries to divide by zero when the rocket_speed is set to 0. This causes a ZeroDivisionError, not a ValueError. Therefore, the exception handling needs to catch ZeroDivisionError instead of ValueError. Here is the corrected code:
    try:
    distance_to_moon = 384400  # distance in kilometers
    rocket_speed = 0  # speed in km/h
    travel_time_to_moon = distance_to_moon / rocket_speed
    print("Travel time to moon: ", travel_time_to_moon, " hours")
    
except ZeroDivisionError:
    print("Oops! Cannot calculate travel time with zero speed.")
    This corrected code will handle the zero division error correctly by catching the ZeroDivisionError and printing an appropriate message.
### 「practice」Calculating Planetary Mass Ratios with Exception Handling
Absolutely cosmic, Space Explorer! Your next mission awaits. Please adapt the code to retrieve the mass of Jupiter from our `celestial_body_mass` dictionary. Remember, _Jupiter_ does not exist in our dictionary, thus necessitating the handling of the `KeyError` exception.

```python
try:

celestial_body_mass = {"Earth": 5.97e24, "Moon": 7.35e22}

# TODO: Retrieve the mass of Jupiter from our dictionary and handle any KeyError exception that arises.

  

except _______:

print("Error: The mass of the specified celestial body is not available in the dictionary.")
```
### 解析：

To retrieve the mass of Jupiter from the celestial_body_mass dictionary and handle the KeyError exception, you can use the following code. We will use a try block to attempt to get the mass of Jupiter and catch any KeyError exceptions that arise:
```python
try:
    celestial_body_mass = {"Earth": 5.97e24, "Moon": 7.35e22}
    
    # Attempt to retrieve the mass of Jupiter
    jupiter_mass = celestial_body_mass["Jupiter"]
    print("The mass of Jupiter is:", jupiter_mass)
except KeyError:
    print("Error: The mass of the specified celestial body is not available in the dictionary.")
```

In this code, if the key "Jupiter" is not found in the celestial_body_mass dictionary, the KeyError exception will be caught, and the message “Error: The mass of the specified celestial body is not available in the dictionary.” will be printed.


在这段代码中，如果在celestial_body_mass字典中找不到键"Jupiter"，则会捕获KeyError异常，并打印消息“错误：字典中没有指定天体的质量可用。”


Bravo, Cosmic Coder! We've been exploring the cosmos and have successfully dealt with many Python exceptions.

Can you use our `try` and `except` block knowledge to calculate the ratio of Earth's mass to that of Mars using our `celestial_body_mass` dictionary? Remember, you need to handle any `KeyError` that might arise if someone changes the `celestial_body_mass` dictionary in the future.

This is your chance to shine!
```python
earth_mass = 5.97e24

celestial_body_mass = {"Mars": 6.39e23, "Jupiter": 1.898e27}

  

# TODO: Calculate the earth-to-mars mass ratio and handle a potential KeyError
```
Bravo, Cosmic Coder! We've been exploring the cosmos and have successfully dealt with many Python exceptions.

Can you use our `try` and `except` block knowledge to calculate the ratio of Earth's mass to that of Mars using our `celestial_body_mass` dictionary? Remember, you need to handle any `KeyError` that might arise if someone changes the `celestial_body_mass` dictionary in the future.

This is your chance to shine!

```
earth_mass = 5.97e24

celestial_body_mass = {"Mars": 6.39e23, "Jupiter": 1.898e27}

  

# TODO: Calculate the earth-to-mars mass ratio and handle a potential KeyError
```
### 解析

Sure! Here is a Python script that calculates the ratio of Earth’s mass to Mars’ mass using a try-except block to handle any potential KeyError:
```
earth_mass = 5.97e24
celestial_body_mass = {"Mars": 6.39e23, "Jupiter": 1.898e27}

try:
    mars_mass = celestial_body_mass["Mars"]
    ratio = earth_mass / mars_mass
    print(f"The ratio of Earth's mass to Mars' mass is {ratio:.2f}")
except KeyError as e:
    print(f"KeyError: {e} not found in celestial_body_mass dictionary")
```
Explanation:

	1.	Data Initialization:
	•	earth_mass is set to 5.97 \times 10^{24} kg.
	•	celestial_body_mass dictionary contains the masses of Mars and Jupiter.
	2.	Try Block:
	•	Attempts to retrieve the mass of Mars from celestial_body_mass dictionary.
	•	Calculates the ratio of Earth’s mass to Mars’ mass.
	•	Prints the ratio formatted to two decimal places.
	3.	Except Block:
	•	Catches KeyError if the key “Mars” is not found in the celestial_body_mass dictionary.
	•	Prints an error message specifying the missing key.

Usage:

You can run this script to get the ratio. If “Mars” is not in the dictionary, it will handle the error gracefully by informing you of the missing key. This approach ensures that the program won’t crash due to an unexpected missing key.

```python
earth_mass = 5.97e24
celestial_body_mass = {"Mars": 6.39e23, "Jupiter": 1.898e27}

try:
    mars_mass = celestial_body_mass["Mars"]
    ratio = earth_mass / mars_mass
    print(f"地球质量与火星质量的比率是 {ratio:.2f}")
except KeyError as e:
    print(f"键错误：{e} 不在 celestial_body_mass 字典中")
```

解释：

	1.	数据初始化：
	•	earth_mass 被设定为 5.97 \times 10^{24} 公斤。
	•	celestial_body_mass 字典包含火星和木星的质量。
	2.	Try 块：
	•	尝试从 celestial_body_mass 字典中获取火星的质量。
	•	计算地球质量与火星质量的比率。
	•	打印比率，格式化为小数点后两位。
	3.	Except 块：
	•	如果键 “Mars” 不在 celestial_body_mass 字典中，捕获 KeyError。
	•	打印一条错误信息，说明缺少的键。
**用法：**

  

你可以运行这个脚本来获取地球质量与火星质量的比率。如果字典中没有 “Mars” 这个键，它会优雅地处理错误，并通知你缺少的键。这种方法确保程序不会因为意外缺少的键而崩溃。

输出
```python
The ratio of Earth's mass to Mars' mass is 9.34
```
# [Lesson 6: Mastering the 'Finally' Block in Python's Exception Handling](https://learn.codesignal.com/preview/lessons/159)

### 「practice」Handling Errors in a Deserted Office

### 「practice」Troubleshooting the Fire Alarm

### 「practice」Fix the Room Items List Display

### 「practice」Access and Handle Missing Keys in a Python Dictionary

### 「practice」Revise Your Office Tasks List
##### Introduction and Lesson Overview

Welcome back! Today, our focus will be on the `finally` block, which concludes Python's three-part exception handling methodology. Exception handling protects our program from failing when unexpected errors occur. The `finally` block can be likened to a diligent worker who secures the office during emergencies.
欢迎回来！今天，我们的重点将放在 `finally` 块上，它总结了 Python 的三部分异常处理方法。异常处理可以保护我们的程序在发生意外错误时不会失败。 `finally` 块可以比作在紧急情况下保护办公室安全的勤奋工人。

Our objective is to comprehend the function of `finally` and its role in exception handling. We'll use real-life analogies and interactive code examples to achieve this. Shall we begin?

我们的目标是理解 `finally` 的功能及其在异常处理中的作用。我们将使用现实生活中的类比和交互式代码示例来实现这一目标。让我们开始？

##### Understanding the finally Block  
理解finally块

The `finally` block is an integral part of Python's exception-handling mechanism. It protects crucial code that needs to be executed irrespective of any exceptions. Imagine it as a responsible worker who, during sudden emergencies, ensures the electricity is off and the office door is locked.  
`finally` 块是 Python 异常处理机制的一个组成部分。它保护需要执行的关键代码，无论发生任何异常。想象一下，作为一个负责任的工人，在突发紧急情况下，确保电源关闭并锁上办公室门。
##### Syntax Overview 语法概述

In Python's exception handling sequence, the `finally` block follows the `try` and `except` blocks. It begins with the `finally` keyword and a colon, which is followed by indented lines of code that get executed unconditionally:  
在Python的异常处理顺序中， `finally` 块位于 `try` 和 `except` 块之后。它以 `finally` 关键字和冒号开头，后面是无条件执行的缩进代码行：

```python
try:
    # Risky operation
except ValueError:
    # Handle error
finally:
    # Always execute this block at the end
```
In this code snippet, the `finally` block executes before the program concludes, regardless of any exceptions. This block will execute after the risky operation and exception handling, if any.  
在此代码片段中，无论是否出现任何异常， `finally` 块都会在程序结束之前执行。该块将在危险操作和异常处理（如果有）之后执行。
##### Examples and Explanation 示例和说明

Consider a program that attempts to divide 10 by 0, thereby triggering a `ZeroDivisionError`. Observe how the `finally` block executes, despite the exception:  
考虑一个程序尝试将 10 除以 0，从而触发 `ZeroDivisionError` 。观察 `finally` 块如何执行，尽管有异常：
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Division by zero!")
finally:
    print("Always executed.")
```
Even when an exception occurs, `finally` ensures that essential clean-up tasks are completed.  
即使发生异常， `finally` 也会确保完成必要的清理任务。
Now, let's try dividing 10 by 5:  
现在，我们尝试用 10 除以 5：
```python
try:
    result = 10 / 5
    print("Result is:", result)
except ZeroDivisionError:
    print("Oops! Dividing by zero.")
finally:
    print("Always executed.")
```
As you can observe, the `finally` block executes even when no exception arises!  
正如您所观察到的，即使没有发生异常， `finally` 块也会执行！
##### Errors and Troubleshooting  
错误和故障排除

Common errors include a missing colon at the end of the `finally` keyword, which causes a `SyntaxError`. Here's a piece of erroneous code:  
常见错误包括 `finally` 关键字末尾缺少冒号，这会导致 `SyntaxError` 。这是一段错误的代码：
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! Dividing by zero.")
finally
    print("Always executed.")
```
This code will result in a `SyntaxError: invalid syntax` because Python uses colons to comprehend the block structure of the code. By adding a colon after `finally`, the error can be corrected.  
此代码将生成 `SyntaxError: invalid syntax` ，因为 Python 使用冒号来理解代码的块结构。通过在 `finally` 之后添加冒号，可以更正错误。
##### Lesson Summary 课程总结

Well done! You've mastered the `finally` block, which is the last component of Python's exception-handling mechanism. We've journeyed through its purpose, syntax, and implementation using real-life examples. The analogy of a trustworthy worker aids in recalling the role of `finally` during crucial moments!  
做得好！您已经掌握了 `finally` 块，它是 Python 异常处理机制的最后一个组件。我们已经使用现实生活中的示例了解了它的目的、语法和实现。值得信赖的工人的比喻有助于回忆 `finally` 在关键时刻的角色！

Revisit this material and rerun the examples until you're comfortable. Remember, there's no need to rush!  
重新访问本材料并重新运行示例，直到您感到满意为止。请记住，没有必要着急！

What's next? Hands-on practice! Test various scenarios and observe the behavior of the `finally` block. Each experiment will strengthen your understanding. Good luck, and keep in mind that practice is the key to mastering programming!  
下一步是什么？动手实践！测试各种场景并观察 `finally` 块的行为。每个实验都会增强您的理解。祝你好运，并记住练习是掌握编程的关键！
## practice1

Hello, Space Voyager!

Consider a case in which a large office is suddenly completely deserted. If we try to distribute the office chairs per person, what do you think will happen? However, there's no need to worry because the janitorial bot is still operational!

Now it's time to hit `Run`!

```python
try:

office_chairs = 10

employees = 0

chairs_per_person = office_chairs / employees

except ZeroDivisionError:

print("Office is empty, no division is possible.")

finally:

print("Please remember to turn off the lights.")
```
## practice2
Great work so far!

To enhance the robustness of our code, consider modifying it to remove a non-existing element from the list.

Please ensure that our `finally` block remains intact.

Give it a shot, Space Voyager!
```python
office_equipment = ['computers', 'printers', 'coffee machine']

element = "computers"

  

try:

office_equipment.remove(element)

except ValueError:

print("{} is not found in office equipment list.".format(element))

finally:

print("Regardless, please remember to clean up after work.")

```python
office_equipment = ['computers', 'printers', 'coffee machine']

element = "computers"

  

try:

    office_equipment.remove(element)

except ValueError:

    print("{} is not found in office equipment list.".format(element))

finally:

    print("Regardless, please remember to clean up after work.")
```
```

当然，这段代码旨在从一个列表中删除一个元素，并且在元素不存在时进行错误处理，确保无论如何都会执行最后的清理提示。以下是对代码的详细解释：

```python
office_equipment = ['computers', 'printers', 'coffee machine'] # 定义一个包含办公设备的列表
element = "computers" # 定义要删除的元素

try:
    office_equipment.remove(element) # 尝试从列表中删除指定的元素
except ValueError:
    print("{} is not found in office equipment list.".format(element)) # 如果元素不存在，捕获ValueError异常并打印提示信息
finally:
    print("Regardless, please remember to clean up after work.") # 无论是否发生异常，始终执行清理提示
```

### 代码解释：

1. `office_equipment = ['computers', 'printers', 'coffee machine']`
   - 定义一个名为 `office_equipment` 的列表，其中包含三个字符串元素，表示办公设备。

2. `element = "computers"`
   - 定义一个名为 `element` 的变量，赋值为字符串 `"computers"`，表示我们想要从列表中删除的元素。

3. `try:`
   - 尝试执行 `try` 语句块中的代码。如果代码块中的某些操作可能会引发异常（错误），那么这些操作就应该放在 `try` 块中。

4. `office_equipment.remove(element)`
   - 尝试从 `office_equipment` 列表中删除 `element` 对应的元素。在本例中，尝试删除 `"computers"`。

5. `except ValueError:`
   - 如果在 `try` 块中发生了 `ValueError` 异常（例如，当 `element` 不在列表中时），则执行 `except` 块中的代码。

6. `print("{} is not found in office equipment list.".format(element))`
   - 如果发生 `ValueError` 异常，打印一条消息，提示所要删除的元素在列表中没有找到。

7. `finally:`
   - 无论 `try` 块中的代码是否引发异常，总是会执行 `finally` 块中的代码。这里用于确保清理工作或其他需要始终执行的代码能够运行。

8. `print("Regardless, please remember to clean up after work.")`
   - 无论是否发生异常，始终打印一条清理提示信息。

这段代码确保即使在尝试删除一个不存在的元素时，程序也不会崩溃，并且会给出提示，同时保证了最后的清理提示信息一定会被打印出来。

> 好的，让我们来修复缩进错误，并选择一个列表中不存在的元素。下面是更正后的代码片段：

```python
office_equipment = ['computers', 'printers', 'coffee machine']
element = "fire alarm"  # 选择一个列表中不存在的元素

try:
    office_equipment.remove(element)
except ValueError:
    print("{} is not found in office equipment list.".format(element))
finally:
    print("Regardless, please remember to clean up after work.")
```

### 代码解释（中文）：

1. `office_equipment = ['computers', 'printers', 'coffee machine']`
   - 定义一个名为 `office_equipment` 的列表，其中包含三个字符串元素，表示办公设备。

2. `element = "fire alarm"`
   - 定义一个名为 `element` 的变量，赋值为字符串 `"fire alarm"`，表示我们想要从列表中删除的元素。注意，这个元素在列表中并不存在。

3. `try:`
   - 尝试执行 `try` 语句块中的代码。如果代码块中的某些操作可能会引发异常（错误），那么这些操作就应该放在 `try` 块中。

4. `office_equipment.remove(element)`
   - 尝试从 `office_equipment` 列表中删除 `element` 对应的元素。在本例中，尝试删除 `"fire alarm"`。

5. `except ValueError:`
   - 如果在 `try` 块中发生了 `ValueError` 异常（例如，当 `element` 不在列表中时），则执行 `except` 块中的代码。

6. `print("{} is not found in office equipment list.".format(element))`
   - 如果发生 `ValueError` 异常，打印一条消息，提示所要删除的元素在列表中没有找到。

7. `finally:`
   - 无论 `try` 块中的代码是否引发异常，总是会执行 `finally` 块中的代码。这里用于确保清理工作或其他需要始终执行的代码能够运行。

8. `print("Regardless, please remember to clean up after work.")`
   - 无论是否发生异常，始终打印一条清理提示信息。

这段代码通过正确的缩进确保即使在尝试删除一个不存在的元素时，程序也不会崩溃，并且会给出提示，同时保证了最后的清理提示信息一定会被打印出来。

请尝试运行此代码，并让我知道是否有效！🚀

Impressive work, _Commander_!

For the final task, let's test your knowledge! Can you modify the `dictionary` to retrieve a `value` and add a final block on top of that? Please follow TODO comments to accomplish this.

Always move forward, _Commander_!

```python
# Office setting

office_equipment = {}

  

try:

#TODO: Write a line to access an item in the dictionary, which will throw the KeyError exception.

except KeyError:

print("Can't find 'printer' in the office equipment.")

# TODO: implement a 'finally' block to print the current state of the office equipment dictionary
```

To modify the code as per the TODO comments, you need to write a line to access an item in the dictionary and implement a `finally` block to print the current state of the dictionary. Here is how you can achieve this:

```python
# Office setting
office_equipment = {}

try:
    # TODO: Write a line to access an item in the dictionary, which will throw the KeyError exception.
    item = office_equipment['printer']
except KeyError:
    print("Can't find 'printer' in the office equipment.")
finally:
    # TODO: implement a 'finally' block to print the current state of the office equipment dictionary
    print("Current state of the office equipment dictionary:", office_equipment)
```

In this code:
- The line `item = office_equipment['printer']` tries to access the value associated with the key 'printer' in the dictionary `office_equipment`. Since 'printer' is not a key in the dictionary, this will raise a `KeyError`.
- The `except` block catches the `KeyError` and prints a message.
- The `finally` block prints the current state of the `office_equipment` dictionary, regardless of whether an exception was raised.
- ### Office setting
以下代码片段展示了如何处理和访问一个包含办公室设备的字典。尝试访问不存在的键时会抛出 `KeyError` 异常，并通过 `try-except-finally` 结构进行处理。

```python
office_equipment = {}

try:
    # 尝试访问字典中的一个不存在的项目，这将引发 KeyError 异常
    item = office_equipment['printer']
except KeyError:
    print("Can't find 'printer' in the office equipment.")
finally:
    # 实现 finally 块，打印当前办公室设备字典的状态
    print("Current state of the office equipment dictionary:", office_equipment)
```

中文解释：
- `office_equipment = {}` 初始化一个空的办公室设备字典。
- `try` 块中尝试访问字典中的键 `'printer'`，因为字典是空的，这将引发 `KeyError` 异常。
- `except KeyError` 捕获 `KeyError` 异常，并输出提示信息：“Can't find 'printer' in the office equipment.”
- `finally` 块无论是否引发异常都会执行，打印当前办公室设备字典的状态。

通过上述代码，我们不仅能够捕获并处理访问不存在字典键时的异常，还能确保在 `finally` 块中执行一些清理工作，比如输出字典的当前状态。
Office tasks need to be completed, but sometimes, a task doesn't exist in the list! That's why error handling is important. Within the provided code, try writing a `try-except` block, which attempts to remove a task that doesn't exist in the office tasks list. Don't forget to also use the `finally` block we've just learned!


```python
# Daily office activities

office_tasks = ["cleaning", "maintenance", "stationery_stock_check", "security_check"]

  

# TODO: Write a try-except block that attempts to remove the 'coffee_making' task from office_tasks

# TODO: If the task doesn't exist in the list, print a suitable message

# TODO: Regardless of whether the task is on the list, print the message "Regardless, please ensure all tasks are attended daily."
```
"该代码需要处理办公室任务的完成情况，但有时任务列表中并不存在某个任务。这就是错误处理的重要性。请在提供的代码中编写一个`try-except`块，该块尝试从任务列表中删除一个不存在的任务。别忘了我们刚学到的`finally`块！

以下是代码解释：

1. `office_tasks` 列表包含日常办公室活动任务，如“清洁”，“维护”，“文具库存检查”，“安全检查”。
2. TODO: 编写一个`try-except`块，尝试从`office_tasks`列表中删除“咖啡制作”任务。
3. TODO: 如果任务不存在于列表中，则打印合适的提示信息。
4. TODO: 无论任务是否在列表中，都打印信息“Regardless, please ensure all tasks are attended daily.”。

示例代码如下：

```python
# Daily office activities
office_tasks = ["cleaning", "maintenance", "stationery_stock_check", "security_check"]

# TODO: Write a try-except block that attempts to remove the 'coffee_making' task from office_tasks
try:
    office_tasks.remove('coffee_making')
except ValueError:
    print("Task 'coffee_making' not found in the list.")
finally:
    print("Regardless, please ensure all tasks are attended daily.")
```

在上面的代码中：
- `try`块尝试从`office_tasks`列表中删除“coffee_making”任务。
- 如果任务不在列表中，会引发`ValueError`异常，并打印“Task 'coffee_making' not found in the list.”的错误信息。
- `finally`块无论是否发生异常都会执行，并打印“Regardless, please ensure all tasks are attended daily.”的提示信息。"

这段代码的功能是尝试从列表 `office_tasks` 中移除任务 `'coffee_making'`，并在任务不在列表中时处理异常。无论是否找到并移除了任务，都会打印一条提示信息。

以下是代码的详细解释：

```python
# 日常办公室活动
office_tasks = ["cleaning", "maintenance", "stationery_stock_check", "security_check"]

# 尝试移除 'coffee_making' 任务，并处理异常
try:
    office_tasks.remove('coffee_making')
except ValueError:
    print("Task 'coffee_making' not found in the list.")
finally:
    print("Regardless, please ensure all tasks are attended daily.")
```

### 详细解释

1. **定义任务列表**:
   ```python
   office_tasks = ["cleaning", "maintenance", "stationery_stock_check", "security_check"]
   ```
   `office_tasks` 是一个包含日常办公室任务的列表。

2. **尝试移除任务**:
   ```python
   try:
       office_tasks.remove('coffee_making')
   ```
   使用 `try` 块尝试从 `office_tasks` 列表中移除 `'coffee_making'` 任务。如果任务存在，则移除该任务。如果任务不存在，将引发 `ValueError` 异常。

3. **处理异常**:
   ```python
   except ValueError:
       print("Task 'coffee_making' not found in the list.")
   ```
   当 `remove` 方法未找到 `'coffee_making'` 任务并引发 `ValueError` 异常时，执行 `except` 块中的代码，打印错误信息。

4. **无论如何都执行的代码**:
   ```python
   finally:
       print("Regardless, please ensure all tasks are attended daily.")
   ```
   `finally` 块中的代码无论是否引发异常都会执行，打印一条提示信息，确保所有任务每天都要完成。

这段代码确保即使某个任务不存在，也不会导致程序崩溃，并且始终提醒要完成所有任务。







































