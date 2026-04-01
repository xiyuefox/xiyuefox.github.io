---
title: "06_Learning Functions using Python"
date: 2024-06-20
tags: []
category: "obsidian"
badge: "obsidian"
type: "article"
---



6 lessons

32 practices

## Learning Functions using Python

Delve into the crucial aspect of Python programming - Functions. In this course, we emphasize how to create your own user-defined functions and harness the power of Python's built-in functions. By the end of this course, you should be comfortable defining and calling functions to streamline your code and boost efficiency.

使用Python学习函数

深入了解Python编程的关键方面——函数。在本课程中，我们强调如何创建自己的用户定义函数，并利用Python内置函数的强大功能。在本课程结束时，您应该习惯于定义和调用函数来简化代码并提高效率。

# [Lesson 1: Exploring Python Functions: An Easy Guide for Beginners](https://learn.codesignal.com/preview/lessons/305)


##### Overview of Python Functions

Greetings, seeker of knowledge! Today, we're setting forth on a journey to navigate the cosmos of Python. We will focus particularly on **Python functions** — one of the key elements in the programming universe.

Just as the blender in your kitchen combines various ingredients to serve you a delightful smoothie, functions in programming take in inputs or "_arguments_", process them, and generate an output. For instance, consider a function in a food delivery app. You input your food choices, the app processes the order, and voilà, you receive the expected time of delivery. Food for thought, isn't it?
Are you ready to start concocting your own Python functions? Let's dive in!
##### Learning to Write Python Functions

So, how do we create a Python function? It's fairly straightforward, involving several key components: the keyword `def`, the name of the function, parentheses `()`, and a colon `:`. Take a look:
```python
def hello_world():
    print("Hello, World!")
```
In the function above, `hello_world` is the name of the function. Within its body, which is indented to the right, it performs an operation — printing the phrase "Hello, World!". We use or "call" this function by using its name followed by parentheses. Let's give it a try:
```python
def hello_world():
    print("Hello, World!")

# Call the function
hello_world() # Prints: "Hello, World!"
```

Upon running this script, you will see "Hello, World!" printed on your screen. Voilà! You've just cooked up your first Python function.
```python
def hello_world():
    print("Hello, World!")
```
In the function above, `hello_world` is the name of the function. Within its body, which is indented to the right, it performs an operation — printing the phrase "Hello, World!". We use or "call" this function by using its name followed by parentheses. Let's give it a try:
```python
def hello_world():
    print("Hello, World!")

# Call the function
hello_world() # Prints: "Hello, World!"
```
Upon running this script, you will see "Hello, World!" printed on your screen. Voilà! You've just cooked up your first Python function.
##### Empty function body: pass

Python has a special operator `pass` that is used to provide no implementation for the function. This is how it works:
```python
def not_implemented_function():
    pass
```
You ask why? The reason is that if you don't provide this operator, the code won't run:
```python
def not_implemented_function():
    # no implementation provided, 'pass' is missed

# The code throws "IndentationError: expected an indented block after function definition on line 1"
```
So essentially, `pass` is used when you already have a function definition but don't have implementation for it yet - without the `pass` operator, the code won't run.
##### Functions with Arguments

Our blender becomes more versatile as we introduce different ingredients, doesn't it? Similarly, to add versatility to our function, we introduce arguments — inputs that our function can transform and combine to produce varied results.
```python
def greet(message):
    print(message)

# Call the function with "Good Morning!"
greet("Good Morning!") # Prints: "Good Morning!"
```
The `greet` function above accepts a `message` argument and prints it out. When we feed the argument "Good Morning!", it prints exactly that.
##### Functions that Give Back: Return Values

Blenders don't merely process the ingredients; they also deliver a smoothie. Similarly, functions can process inputs and return a computed result or output. They accomplish this using the `return` keyword.
```python
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Call the function
total = add_numbers(3, 7)
print(total) # Prints: 10
```
Just like a blender, the `add_numbers` function combines, or adds, `num1` and `num2`, and then `return` delivers the resulting sum. This returned value is then assigned to the variable named `sum`, which is subsequently printed out.

##### Functions: Variable Arguments

Now, what if we want to blend more than two ingredients? Or, in Python terms, what if we want our function to accept any number of arguments flexibly? You don't have to understand how `sum(args)` and `len(args)` work for now, just look how it works! We'll cover these built-in functions later in this course.
```python
def calculate_average(*args):
    """
    `sum(args)` returns the sum of all arguments
    `len(args)` returns the number of arguments
    """
    return sum(args) / len(args) # the average across all arguments

# Call the function with various numbers of arguments
print(calculate_average(3, 7)) # Prints: 5 ((3 + 7) / 2 = 5)
print(calculate_average(10, 20, 30, 40)) # Prints: 25 (10 + 20 + 30 + 40) / 4 = 100 / 25 = 4)
print(calculate_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # Prints: 5.5
```
The `calculate_average` function accepts any number of arguments (`*args`) and calculates their average by summing all the values (`sum(args)`) and dividing by the total number of values (`len(args)`). You can call this function with any number of arguments — a handy trick to have up your sleeve!
##### Concluding Our Journey

Congratulations! We've just journeyed across the Python universe, discovering the magic of Python functions, understanding their uses, and creating our own functions. The insights gleaned from this journey and the practical skills we acquired through learning and using Python functions lay the foundation for exploring more advanced Python functionalities that await us in future voyages.

With this newfound knowledge, it's time to put it all into practice. Brace yourself because, up next, we have a multitude of experiments and exercises I have designed just for you. These are designed to put your skills to the test and polish your command over Python functions. Let's get coding, and may the function force guide you!

### 「practice」Serving Up the Cosmic Meal Bill

Hey, Stellar Navigator! Who doesn't love a jolly-good feast? Our next mission involves computing the cost of our cosmic meal. We have a _Python function_ that aggregates the costs of a burger, drink, and dessert to calculate the total price.  
嘿，星际导航员！谁不喜欢一顿丰盛的盛宴呢？我们的下一个任务是计算我们宇宙大餐的花费。我们有一个 Python 函数，可以汇总汉堡、饮料和甜点的成本，从而计算出总价。

By waving our magical wand, we can activate this function, supplying the prices for each item. It will then promptly return the final bill. Press the flashy `Run` button and watch the magic unfold!  
挥动我们的魔法棒，我们可以激活这个功能，提供每件商品的价格。然后，它会立即返回最终账单。按下闪亮的 `Run` 按钮，见证奇迹的发生！

```python
# Defining the function to calculate the total price

def calculate_total_price(burger, drink, dessert):

total_price = burger + drink + dessert

return total_price

  

# Calling the function with prices of items

final_bill = calculate_total_price(5, 3, 4)

print("The total bill is $" + str(final_bill))
```

output
```
The total bill is $12
```

### 「practice」Calculating Total Food Order Cost

Imagine, Space Voyager, that we're ordering some food from our favorite cosmic diner, where we have a few items listed with their prices.  
想象一下，太空旅行者，我们正在我们最喜欢的宇宙餐车点餐，菜单上列出了一些食物和它们的价格。

We are to create a function named `order_total`, which accepts any number of arguments (prices) and returns their sum - the total cost. After we run the function with some example orders, we won't have to worry about anything.  
```python def (*prices): total = sum(prices) return total ```

All we have to do is hit the `Run` button to calculate the cost of our delicious order!  
我们只需点击 `Run` 按钮即可计算出我们美味订单的费用！

```python
def order_total(*args):

return sum(args)

  

total_cost = order_total(10.5, 5.99, 2.75, 4)

print(f"The total cost of your food order is: ${total_cost:.2f}")
```


```wolfram
nutritionReport = ResourceFunction["NutritionReport"][
    "100g rice\n8oz chicken\n1 glass wine", 
    "ASCIITable"
]

nutritionReport
```

```
Nutrition Per Food
--------------------------------------------------
| Input        | Interpretation  | absolute calorie content | absolute fat content | absolute protein content | absolute carbohydrate content |
| 100g rice    | 360. Cal        | 0 g                      | 7. g                 | 80. g                    |
| 8oz chicken  | 420. Cal        | 20. g                    | 40. g                | 20. g                    |
| 1 glass wine |                 |                          |                      |                         |

Total Nutrition
--------------------------------------------------
| absolute calorie content | absolute fat content | absolute protein content | absolute carbohydrate content |
| 770. Cal                 | 20. g                | 50. g                    | 99. g                         |
```

该报告显示了每种食品的解释、绝对卡路里含量、绝对脂肪含量、绝对蛋白质含量和绝对碳水化合物含量。总的营养信息如下：

  

• 总卡路里含量：770卡

• 总脂肪含量：20克

• 总蛋白质含量：50克

• 总碳水化合物含量：99克

```wolfram
nutritionReportWithProperties = ResourceFunction["NutritionReport"][
    "100g rice\n8oz chicken\n1 glass wine",
    "ASCIITable",
    "NutritionProperties" -> {
        EntityProperty["Food", "AbsoluteTotalCaloriesContent"], 
        EntityProperty["Food", "AbsoluteTotalProteinContent"]
    }
]

nutritionReportWithProperties

```

```
Nutrition Per Food
--------------------------------------------------
| Input        | Interpretation  | absolute calorie content | absolute protein content |
| 100g rice    | 360. Cal        | 7. g                     |
| 8oz chicken  | 420. Cal        | 40. g                    |
| 1 glass wine |                 |                          |

Total Nutrition
--------------------------------------------------
| absolute calorie content | absolute protein content |
| 770. Cal                 | 50. g                    |
```
该报告显示了每种食品的解释、绝对卡路里含量和绝对蛋白质含量。总的营养信息如下：

  
• 总卡路里含量：770卡

• 总蛋白质含量：50克


### 「practice」Variable Usage in Food Order Calculation

Great job so far, Space Voyager! In the provided starter code, the sale tax rate is hardcoded as 7% (`0.07`). Your task is to replace the hardcoded tax value with a new function parameter named `tax_rate`, and correctly provide this parameter in the function call.  
干得好，太空旅行者！在提供的初始代码中，销售税率被硬编码为 7% ( `0.07` )。你的任务是用一个名为 `tax_rate` 的新函数参数替换硬编码的税值，并在函数调用中正确提供此参数。

This change will simplify the process of altering the tax percentage in the future. It's time for your next leap!  
此项更改将简化未来修改税率的流程。是时候迈出你的下一步了！

```python
# Function to calculate total price for food order

def calculate_order_price(appetizers, main_course, desserts):

price = appetizers + main_course + desserts

tax = 0.07 * price # 7% tax

total_price = price + tax

return total_price

  

# Call the function for a specific order

order_price = calculate_order_price(15, 25, 10)

print('The total price for your order is: $', order_price)
```
为了将硬编码的税率替换为一个新的函数参数，我们需要以下几个步骤：

1. 在函数定义中添加一个新的参数 `tax_rate`。
2. 在函数调用时提供这个新的参数 `tax_rate`。
3. 使用这个参数来计算税额，而不是硬编码的值。

修改后的代码如下：

```python
# Function to calculate total price for food order
def calculate_order_price(appetizers, main_course, desserts, tax_rate):
    price = appetizers + main_course + desserts
    tax = tax_rate * price  # Use the provided tax rate
    total_price = price + tax
    return total_price

# Call the function for a specific order with a tax rate of 7%
order_price = calculate_order_price(15, 25, 10, 0.07)
print('The total price for your order is: $', order_price)
```

这样一来，税率就可以通过参数 `tax_rate` 进行传递，方便以后更改税率。例如，如果将来需要更改税率，只需在调用函数时提供不同的税率即可：

```python
# Call the function for a specific order with a tax rate of 8%
order_price = calculate_order_price(15, 25, 10, 0.08)
print('The total price for your order is: $', order_price)
```

这个更改使得税率的调整更加灵活，减少了硬编码值带来的不便。



###  ### 「practice」Fix the Total Order Cost Calculation

Hey, Stellar Navigator! 嘿，星际领航员！

A fellow explorer has attempted to create a function to calculate the _total food order cost_. However, the cost, as printed, isn't correctly summed up. Can you pinpoint and rectify the issue?  
一位探险家同伴尝试创建一个函数来计算食物订单总成本。但是，打印出来的成本汇总不正确。你能找出问题所在吗？


```python
# Define your function

def total_order_cost(food_cost, delivery_cost):

total_cost = food_cost + delivery_cost

return total_cost

  

# Call the function

complete_order_cost = total_order_cost((10.5, 5))

print("Your complete order cost is: $" + str(complete_order_cost))
```
您好，星际领航员！

您的同伴在计算食物订单总成本时遇到了问题。问题在于他们在调用函数 `total_order_cost` 时传递了一个包含两个元素的元组 `(10.5, 5)`，而不是分别传递两个单独的参数 `food_cost` 和 `delivery_cost`。这是导致计算错误的原因。

我们需要修改函数调用，确保将 `food_cost` 和 `delivery_cost` 分别传递给函数。另外，我们还可以改进输出格式，使其显示两位小数。

以下是修正后的代码：

```python
# Define your function
def total_order_cost(food_cost, delivery_cost):
    total_cost = food_cost + delivery_cost
    return total_cost

# Call the function with separate food and delivery costs
complete_order_cost = total_order_cost(10.5, 5)

# Print the total cost with two decimal places
print(f"Your complete order cost is: ${complete_order_cost:.2f}")
```

这样，函数调用将正确传递 `food_cost` 和 `delivery_cost`，并且输出结果将正确显示为带有两位小数的总费用。

运行以上代码的输出结果将是：
```
Your complete order cost is: $15.50
```

这样修改后，代码将正确计算并打印出总订单费用。
### 「practice」Crafting a Python Function for Food Ordering
Excellent work, Galactic Pioneer!

Are you ready to push your skills even further? Let's proceed! Your mission is to complete the provided food ordering function using your Python knowledge.

The function should take in two arguments and subsequently return an informational string that unites both parameters. _Guiding stars_ will illuminate your path!
```python
def order_food(dish, drink):

# TODO: Create a string that introduces the order by combining the dish and drink parameters.

# The resulting string should start with "Order placed: ".

  

print(order_food("Pizza", "Coke"))
```

Great! Let's proceed with completing the `order_food` function in Python. The function should take two arguments, `dish` and `drink`, and return a string that combines these parameters to introduce the order. The resulting string should start with "Order placed: ".

Here's the code:

```python
def order_food(dish, drink):
    # Create a string that introduces the order by combining the dish and drink parameters
    result = "Order placed: " + dish + " and " + drink
    return result

print(order_food("Pizza", "Coke"))
```

This function creates a string that introduces the order by concatenating the values of `dish` and `drink` with a fixed introductory phrase. Let's see how it works:

1. The function `order_food` takes two parameters: `dish` and `drink`.
2. It constructs a string by concatenating "Order placed: ", the value of `dish`, and the value of `drink`, with appropriate connecting words (" and ").
3. The resulting string is returned.

When you call `order_food("Pizza", "Coke")`, it will output: `Order placed: Pizza and Coke`.

Feel free to run this code to see the output!
### 「practice」Craft a Python Function to Calculate Total Food Order Amount
Great work, _Space Voyager_!

Now, let's put your skills to the test. Can you create a function that calculates the total amount of our order? Best of luck!

```python
# Function to calculate the total amount

def calculate_total(*spendings):

# TODO: Calculate and return the total amount of spending

pass

  

# Order made: 1 pizza, 2 burgers, and 3 soft drinks

# Their prices are 10.5, 6.75, and 2.5 respectively

total_amount = calculate_total(10.5, 6.75, 6.75, 2.5, 2.5, 2.5)

  

print("Your total bill is: $", total_amount)
```

Sure, let's create a function called `calculate_total` that calculates the total amount of spendings provided as arguments. 

Here's the complete implementation:

```python
# Function to calculate the total amount
def calculate_total(*spendings):
    # Calculate and return the total amount of spending
    total = sum(spendings)
    return total

# Order made: 1 pizza, 2 burgers, and 3 soft drinks
# Their prices are 10.5, 6.75, and 2.5 respectively
total_amount = calculate_total(10.5, 6.75, 6.75, 2.5, 2.5, 2.5)

print("Your total bill is: $", total_amount)
```

This function works as follows:

1. **Function Definition**: `calculate_total` takes a variable number of arguments using `*spendings`.
2. **Total Calculation**: The `sum()` function calculates the total amount of all the arguments.
3. **Return Total**: The total amount is returned.

When we call `calculate_total` with the prices of the items in the order (1 pizza, 2 burgers, and 3 soft drinks), it calculates the total and prints it.

Here's the expected output:
```plaintext
Your total bill is: $ 31.5
```

This implementation ensures that any number of spending values can be passed to the function, making it flexible and reusable for different orders.

---

# 🌌 太空图书馆日志 🌌

**第52天**

问题：食物订单支出总金额计划
---

### 📝 代码示例
```python
# Function to calculate the total amount
def calculate_total(*spendings):
    # Calculate and return the total amount of spending
    total = sum(spendings)
    return total

# Order made: 1 pizza, 2 burgers, and 3 soft drinks
# Their prices are 10.5, 6.75, and 2.5 respectively
total_amount = calculate_total(10.5, 6.75, 6.75, 2.5, 2.5, 2.5)

print("Your total bill is: $", total_amount)
```

### 🔍 小知识点
1. **可变参数函数**: 使用 `*spendings` 可以传递任意数量的参数到函数中。
2. **总和计算**: 利用 `sum()` 函数计算所有传入参数的总和。
3. **返回总金额**: 确保函数返回计算得到的总金额。

### 📢 结果
```plaintext
Your total bill is: $ 31.5
```

---

### 解释

在这段代码中，我们定义了一个函数 **calculate_total**，该函数接受可变数量的参数：`*spendings`。它计算所有传入参数的总和，并返回这个总金额。示例调用展示了如何计算具体订单的总金额，并输出结果。

保持这种探索精神，继续你的编程之旅吧！🚀🌟

---

### 「practice」Cooking Up a Cosmic Order Total Calculator
Great work, _Space Voyager_!

Now, let's put your skills to the test. Can you create a function that calculates the total amount of our order? Best of luck!

```python
# Function to calculate the total amount

def calculate_total(*spendings):

# TODO: Calculate and return the total amount of spending

pass

  

# Order made: 1 pizza, 2 burgers, and 3 soft drinks

# Their prices are 10.5, 6.75, and 2.5 respectively

total_amount = calculate_total(10.5, 6.75, 6.75, 2.5, 2.5, 2.5)

  

print("Your total bill is: $", total_amount)
```


Sure, let's create the function `calculate_total` that takes multiple spendings as arguments and calculates the total amount.

Here's the function:

```python
def calculate_total(*spendings):
    # Calculate and return the total amount of spending
    return sum(spendings)

# Order made: 1 pizza, 2 burgers, and 3 soft drinks
# Their prices are 10.5, 6.75, and 2.5 respectively
total_amount = calculate_total(10.5, 6.75, 6.75, 2.5, 2.5, 2.5)

print("Your total bill is: $", total_amount)
```

This function will sum up all the prices passed to it and return the total amount. The code above will output the correct total bill for the order.
### 「practice」

Astonishing work, Stellar Navigator! Your final mission is to write a Python function that calculates the total price of an order at a fantasy space cafe.

This function should take as arguments the prices of a _burger_, _fries_, and a _drink_, sum these prices, and return the total order price.

Following this, apply your function and print out the total cost.

The taste of success awaits you!

```
# TODO: Define a function that calculates the total price of an order

# This function should take three arguments: the price of a burger, fries, and a drink

  

# TODO: Specify the prices for a burger, fries, and a drink

  

# TODO: Call your function with the prices of the items and assign the result to a variable

  

# TODO: Print out the total cost of the order
```
Let's write a Python function to calculate the total price of an order at a fantasy space cafe. This function will take the prices of a burger, fries, and a drink as arguments, sum them up, and return the total price.

Here's the implementation:

```python
# Define a function that calculates the total price of an order
def calculate_order_total(burger_price, fries_price, drink_price):
    # Calculate the total price by summing up the prices of the burger, fries, and drink
    total_price = burger_price + fries_price + drink_price
    return total_price

# Specify the prices for a burger, fries, and a drink
burger_price = 10.5
fries_price = 3.25
drink_price = 2.75

# Call the function with the prices of the items and assign the result to a variable
total_cost = calculate_order_total(burger_price, fries_price, drink_price)

# Print out the total cost of the order
print("Your total order cost is: $", total_cost)
```

This code defines the `calculate_order_total` function, which sums up the prices of a burger, fries, and a drink, and then it calculates the total cost using specified prices and prints the result. When you run this code, it will output the total cost of the order.
# [Lesson 2: Unleashing the Power of Python Functions: From Calling to Named Parameters](https://learn.codesignal.com/preview/lessons/306)
##### Topic Overview and Lesson Plan

Hello, Space Explorer! Today, our focus is on **calling functions in Python**. By the end of the lesson, you'll understand how to call functions, utilize transitive function calling, employ named parameters, and return multiple values from a function.
##### Understanding Function Calling in Python

Much like how using a remote control can switch on your television, calling a function tells Python to execute a block of code. It's akin to giving directions to your spaceship's computer. Let's use a common scenario in space journeys: greeting a new crew member. Consider this example:
```python
def greet(name):
    print("Hello " + name + ", welcome aboard the spacecraft!")

greet("Astro Kid")  # Prints: "Hello Astro Kid, welcome aboard the spacecraft!"
```
In this instance, we instructed our spaceship's computer to greet the new team member, Astro Kid! Just as in saying "Hello" to a new crew member, calling a function executes the predefined code within that function.
##### Practical Explanation of Transitive Function Calling

In spaceship jargon, think of transitive function calling as delegating tasks on board your spacecraft. So, in fact, transitive function calling is just when you call one or multiple functions inside another function, delegating execution. Suppose we want to increase the heat in our spaceship's engine — instead of doing it ourselves, we assign the task to another function:
```python
def power_up_engine(level):
    print("Powering up the engine to level ", level)

def engine_start():
    print("The engine has started!")

def launch_spacecraft():
    print("Prepare for launch. ", end='')
    power_up_engine(3)
    engine_start()

# Time to hit the space road!
launch_spacecraft()
"""
Prints:

Prepare for launch. Powering up the engine to level 3
The engine has started!
"""
```
Here, as we prepare to launch the spacecraft, we call another function — `power_up_engine(3)` — to power up our spacecraft's engine. Afterward, we call another function - `engine_start()` to delegate the processing of engine post-startup operations. You can see how one function can call another to perform a task.
##### Exploration of Named Parameters

Parameters are called **named** when you provide their name in the function call, explicitly mapping the provided value in the call to the function parameter. Let's see it in action:
```python
# Function definition
def greet_crew_member(name, message):
    print("Hello, " + name + ". " + message)

# Greet a new member, calling function **without** named parameters
greet_crew_member("Astro Kid", "Welcome aboard!")
"""
Prints: "Hello, Astro Kid. Welcome aboard!
"""

# Greet another new member using named parameters
greet_crew_member(name="Star Ranger", message="You're just in time for the cosmic pizza party!")
"""
Prints: "Hello, Star Ranger. You're just in time for the cosmic pizza party!
"""

# Greet another new member using shuffled named parameters
greet_crew_member(message="You're just in time for the cosmic pizza party!", name="Star Explorer")
"""
Prints: "Hello, Star Explorer. You're just in time for the cosmic pizza party!
"""
```
Note how we used named `name` and `message` parameters in the second and third `greet_crew_member` calls - this way, we make sure parameters won't be messed up, and we clearly state what is what. Named parameters can be provided in any order. This is especially helpful when the function takes many arguments of the same data type; this way, you won't accidentally mess up the parameters' order when calling the function, and the function call will also be easier to read.
##### Comprehension of Functions with Multiple Return Values

In Python, your spacecraft's computer, i.e., a function, can perform multiple checks at once and return several results. It's similar to checking the fuel status and oxygen levels before launch. Python's magic (using tuples) makes this possible. Let's see our spaceship's computer in action, returning multiple results:
```python
def spaceship_status():
    # Returning multiple values actually returns a tuple of values under the hood
    return "Fuel: Full", "Oxygen: Normal"

# Dereferencing the tuple, getting the first two elements from it
fuel_status, oxygen_status = spaceship_status()

print(fuel_status) # Prints: "Fuel: Full"
print(oxygen_status) # Prints: "Oxygen: Normal"
```
In this example, the `spaceship_status()` function runs two checks simultaneously — fuel check and oxygen check — and returns both results.
##### Lesson Summary and Next Steps

Great job, future space commander! You've mastered calling functions in Python and transitive function calling and seen the power of named parameters. Plus, you've learned to return multiple values from a function all at once.

Next, it's time for hands-on practice. Prepare to apply what you've learned today to some practice scenarios. Each one is a mission that will test your understanding of Python functions and make you a more proficient space commander! Keep exploring and keep coding!
### 「practice」Kickstarting the Apollo 11 Space Mission
Hey, Stellar Navigator! The snippet below will embark on a fantastic space mission, Apollo 11, which starts on the 16th of July, 1969, right here in Houston. This unique function, `initialize_spacecraft`, takes mission-specific inputs and returns multiple crucial details about the mission.

Take some time to understand how named and optional parameters work here. Go ahead and hit that **Run** button to kickstart this epic journey!
```python
def initialize_spacecraft(mission_name, start_date, command_center):

return mission_name + " initiated", "Mission start date: " + start_date, "Command Center: " + command_center

  

mission_name, start_date, command_center = initialize_spacecraft(mission_name="Apollo 11", start_date="16th July 1969", command_center="Houston")

  

print(mission_name) # Prints: "Apollo 11 initiated"

print(start_date) # Prints: "Mission start date: 16th July 1969"

print(command_center) # Prints: "Command Center: Houston"
```
Let's go ahead and refine the `initialize_spacecraft` function with proper indentation and formatting. This function will take mission-specific inputs and return multiple crucial details about the mission.

Here's the corrected function:

```python
def initialize_spacecraft(mission_name, start_date, command_center):
    return mission_name + " initiated", "Mission start date: " + start_date, "Command Center: " + command_center

# Call the function with named arguments
mission_name, start_date, command_center = initialize_spacecraft(
    mission_name="Apollo 11",
    start_date="16th July 1969",
    command_center="Houston"
)

# Print the results
print(mission_name)        # Prints: "Apollo 11 initiated"
print(start_date)          # Prints: "Mission start date: 16th July 1969"
print(command_center)      # Prints: "Command Center: Houston"
```

When you run this code, it will print out the details of the Apollo 11 mission, confirming the initiation, start date, and command center.

# 🌌 太空图书馆日志 🌌

**第52天**

问题：初始化太空任务
---

### 📝 代码示例
```python
def initialize_spacecraft(mission_name, start_date, command_center):
    return mission_name + " initiated", "Mission start date: " + start_date, "Command Center: " + command_center

# Call the function with named arguments
mission_name, start_date, command_center = initialize_spacecraft(
    mission_name="Apollo 11",
    start_date="16th July 1969",
    command_center="Houston"
)

# Print the results
print(mission_name)        # Prints: "Apollo 11 initiated"
print(start_date)          # Prints: "Mission start date: 16th July 1969"
print(command_center)      # Prints: "Command Center: Houston"
```

### 🔍 小知识点
1. **返回多个值**: 函数可以返回多个值，利用逗号分隔不同的返回值。
2. **命名参数**: 调用函数时可以使用命名参数，使代码更具可读性。
3. **字符串拼接**: 使用加号（`+`）将不同的字符串拼接在一起。

### 📢 结果
```plaintext
Apollo 11 initiated
Mission start date: 16th July 1969
Command Center: Houston
```

---

### 解释

在这段代码中，我们定义了一个函数 **initialize_spacecraft**，该函数接受三个参数：`mission_name`、`start_date` 和 `command_center`。它返回一个包含任务名称、开始日期和指挥中心的元组。示例调用展示了如何初始化太空任务并输出结果。

保持这种探索精神，继续你的编程之旅吧！🚀🌟
---

### 「practice」Customizing the Space Walk Preparation Function
You're doing exceptionally well thus far, Stellar Navigator! Now, let's marginally adjust our code. During our spacewalks, we occasionally perform operations other than checks.  
到目前为止，你做得非常好，恒星导航员！现在，让我们稍微调整一下我们的代码。在我们的太空行走过程中，我们偶尔会执行检查以外的操作。

Could you modify the `prepare_for_space_walk` function to take a new additional parameter named `work_type`? Provide this parameter to a function call using the named parameters technique. Let's get started!  
您可以修改 `prepare_for_space_walk` 函数以采用名为 `work_type` 的新附加参数吗？使用命名参数技术向函数调用提供此参数。让我们开始吧！
```python
def prepare_for_space_walk(duration):

print("Preparing for spacewalk for duration:", duration, "hours")

  

# Call the function with named parameters

prepare_for_space_walk(duration=3)
```

当然，让我们调整 `prepare_for_space_walk` 函数，使其接受一个新的名为 `work_type` 的附加参数，并使用命名参数技术调用该函数。

下面是修改后的代码：

```python
def prepare_for_space_walk(duration, work_type):
    print("Preparing for spacewalk for duration:", duration, "hours")
    print("Type of work to be performed:", work_type)

# Call the function with named parameters
prepare_for_space_walk(duration=3, work_type="equipment maintenance")
```

在这个修改后的代码中，`prepare_for_space_walk` 函数现在接受两个参数：`duration` 和 `work_type`。函数被调用时，使用了命名参数技术，将参数名称和对应的值一一匹配。这样调用函数时，更加清晰直观。


### 「practice」Correct the Space Mission Scanner Report
Great job, _Space Explorer_!  
干得好，太空探索者！

We are preparing for another space mission. However, our spaceship's computer seems to be mixing up the information about different planets, leading to inaccurate final reports.  
我们正在为另一项太空任务做准备。然而，我们宇宙飞船的计算机似乎混淆了有关不同行星的信息，导致最终报告不准确。

There appears to be a minor issue with the logic in our code. Could you decipher the problem and rectify it?  
我们代码中的逻辑似乎存在一个小问题。你能破译问题并纠正它吗？
```python
def scan_planet(planet, system):

print('Scanning planet', planet, 'in', system)

  

def space_mission():

print('Mission start.')

scan_planet(planet='Mars', 'Solar System')

scan_planet(planet='Earth', 'Solar System')

  

space_mission()
```
当然，我们可以修复代码中的问题。在调用 `scan_planet` 函数时，参数 `system` 没有被命名，因此会引发语法错误。我们需要为 `system` 参数添加命名。

下面是修复后的代码：

```python
def scan_planet(planet, system):
    print('Scanning planet', planet, 'in', system)

def space_mission():
    print('Mission start.')
    scan_planet(planet='Mars', system='Solar System')
    scan_planet(planet='Earth', system='Solar System')

space_mission()
```

在这个修复后的代码中，我们在调用 `scan_planet` 函数时，为 `system` 参数添加了命名，这样代码就可以正确运行，并打印出行星扫描的信息。运行这段代码会输出：

```plaintext
Mission start.
Scanning planet Mars in Solar System
Scanning planet Earth in Solar System
```

这样我们就解决了由于参数没有命名而导致的语法错误。
### 「practice」Cosmic Function Returns
You're doing great, Space Explorer! Ready for the next challenge? Let's try **returning multiple values** from a function that checks our cosmic payload. Can you fill in the missing code to complete our inspection function and call it correctly?
```python
def inspect_cosmic_payload(fuel, food):

# TODO: Return the fuel and food status messages using f-strings

# Output example: "Payload fuel level: {fuel}", "Payload food stock: {food}"

return ____, ____

  

# Unpacking multiple return values using named parameters

fuel_status, food_status = ____ # TODO: Call the function with the correct named parameters

  

print(fuel_status)

print(food_status)
```

Sure! Let's fill in the missing code to complete the `inspect_cosmic_payload` function and call it correctly. Here's how you can do it:

```python
def inspect_cosmic_payload(fuel, food):
    # Return the fuel and food status messages using f-strings
    fuel_status = f"Payload fuel level: {fuel}"
    food_status = f"Payload food stock: {food}"
    
    return fuel_status, food_status

# Unpacking multiple return values using named parameters
fuel_status, food_status = inspect_cosmic_payload(fuel=75, food=150)  # Call the function with the correct named parameters

print(fuel_status)
print(food_status)
```

In this code:
- The `inspect_cosmic_payload` function constructs two strings using f-strings, one for the fuel status and one for the food status, and returns them.
- We call the function with named parameters `fuel` and `food` set to `75` and `150`, respectively.
- The returned values are unpacked into `fuel_status` and `food_status`.
- Finally, we print the two status messages.
### 「practice」Craft Your Own Space Greeting Function
Galactic Pioneer, it's time for you to write some code from scratch! Create a function that greets a space explorer.  
```python def 向太空探险家致敬(探险家姓名): return "向勇敢的" + 探险家姓名 + "致敬！欢迎探索银河！" ```

Remember, the key elements include using named parameters. It's time to make the universe speak!  
记住，关键要素包括使用命名参数。是时候让宇宙发出声音了！
```python
# TODO: Write a function to greet a space explorer. Use named parameters.

# The function takes the explorer's name and a greeting message

def ___:

# Inside this function, print a greeting message using the function's parameters

  

# TODO: Call the 'greet_explorer' function with appropriate arguments using named parameters
```



# [Lesson 3: Navigating the Stars: An Introduction to Python's Simple Built-in Functions](https://learn.codesignal.com/preview/lessons/307)
##### Introduction to Built-in Functions in Python 

Welcome, explorer! Are you ready to venture into the realm of Python's built-in functions? These comprehensive tools can streamline your code, saving both time and effort. Our mission is to familiarize ourselves with some of Python's straightforward built-in functions. Let's embark on this journey!  
欢迎，探险者！你准备好进入 Python 内置函数的领域了吗？这些全面的工具可以简化你的代码，节省时间和精力。我们的任务是熟悉 Python 中一些简单易懂的内置函数。让我们开始这段旅程吧！

Much like a built-in navigational system guiding astronauts, Python's built-in functions serve as accessible tools to navigate through coding tasks at any time. They operate as our guiding stars through the cosmic realm of programming.  
如同内置导航系统引导宇航员一样，Python 的内置函数充当随时可用的工具，帮助我们在编码任务中导航。它们是我们穿越编程宇宙领域的指路明灯。
##### Exploring Simple Python Built-in Functions: len()  
探索简单的 Python 内置函数：len()

Let's chart a course through Python's built-in functions:  
让我们来绘制一下 Python 内置函数的图表：

The `len()` function: This function counts elements in a list, set, tuple, or any data structure, much like counting candies in a box:  
`len()` 函数：此函数用于统计列表、集合、元组或任何数据结构中的元素数量，就像计算盒子里的糖果数量一样：


```python
candies_list = ['star1', 'star2', 'star3', 'star4']
print(len(candies_list))  # Output: 4

candies_set = {'star1', 'star2', 'star3', 'star4'}
print(len(candies_set)) # Output: 4

candies_tuple = ('star1', 'star2', 'star3', 'star4')
print(len(candies_tuple)) # Output: 4
```
##### Absolute value: abs() 绝对值：abs()

The `abs()` function: Functioning like a device determining a spaceship's absolute distance in light years from a specific point in space, this function gives the absolute value of a number.  
`abs()` 函数：如同一个装置可以确定宇宙飞船距离空间中某个特定点的光年绝对距离一样，此函数给出数字的绝对值。


```python
print(abs(-10))  # Output: 10
print(abs(7))    # Output: 7
```
##### Float numbers rounding: round()  
浮点数舍入：round()

The `round()` function: Similar to rounding off estimated distances or times, this function rounds a number to the nearest integer.  
`round()` 函数：类似于对估计的距离或时间进行四舍五入，此函数将数字四舍五入到最接近的整数。
```python
print(round(10.675))  # Output: 11
print(round(10.365)) # Output: 10
print(round(7.5)) # Output: 8
```
##### Minimal and Maximal Values: min() and max()  
最小值和最大值：min() 和 max()

The `min()` and `max()` functions: These functions find the smallest and largest items in a list, set, or tuple, just as one might measure the smallest and largest star masses in a galaxy:  
`min()` 和 `max()` 函数：这些函数用于查找列表、集合或元组中的最小和最大项，就像人们测量星系中最小的和最大的恒星质量一样：
```python
stars_list = [2.1, 3.2, 1.0, 5.4, 4.4]  # Sizes of stars
print(min(stars_list))  # Output: 1.0
print(max(stars_list))  # Output: 5.4

stars_set = {2.1, 3.2, 1.0, 5.4, 4.4}  # Sizes of stars
print(min(stars_set))  # Output: 1.0
print(max(stars_set))  # Output: 5.4

stars_tuple = (2.1, 3.2, 1.0, 5.4, 4.4)  # Sizes of stars
print(min(stars_tuple))  # Output: 1.0
print(max(stars_tuple))  # Output: 5.4
```
##### Sum of elements: sum() 元素总和：sum()

The `sum()` function: Analogous to summing up the masses of materials collected during space exploration, this function sums up the elements in a list, set, or tuple:  
`sum()` 函数： 类似于将太空探索中收集到的物质质量求和，此函数将列表、集合或元组中的元素相加：
```python
elements_mass = [5, 3, 2, 6]  # Mass here in kilograms
print(sum(elements_mass))  # Output: 16

elements_mass = {5, 3, 2, 6}  # Mass here in kilograms
print(sum(elements_mass))  # Output: 16

elements_mass = (5, 3, 2, 6)  # Mass here in kilograms
print(sum(elements_mass))  # Output: 16
```
##### Ordering elements: sorted()  
排序元素：sorted()

The `sorted()` function: This function sorts items in a list in the same way artifacts discovered during a space expedition might be chronologically organized:  
`sorted()` 函数：此函数按照太空探险中发现文物的时间顺序对列表中的项目进行排序：
```python
artifacts = [50, 100, 25, 75]  # Antique value here in arbitrary unit
print(sorted(artifacts))  # Output: [25, 50, 75, 100]
```
You can also sort elements in a reversed order:  
您也可以按相反的顺序对元素进行排序：
```python
print(sorted(artifacts, reverse=True)) # Output: [100, 75, 50, 25]
```

##### Lesson Summary 课程总结

You've learned to use Python’s built-in functions `len()`, `abs()`, `round()`, `min()`, `max()`, `sum()`, and `sorted()`. Keep practicing with these functions to improve your programming skills. You're now ready for quizzes and exercises designed to further hone these skills. Keep going and keep exploring!  
你已经学会了使用 Python 的内置函数 `len()` 、 `abs()` 、 `round()` 、 `min()` 、 `max()` 、 `sum()` 和 `sorted()` 。 继续练习使用这些函数来提高你的编程技能。你现在已经准备好进行测验和练习，以进一步磨练这些技能。继续前进，不断探索！



### 「practice」Exploring Alien Sizes with Python's Built-in Functions使用 Python 内置函数探索外星人尺寸
Wow! You've discovered some alien species! Their sizes are recorded in a list named `alien_sizes`.

In the provided code, you'll be using Python's built-in functions to identify the smallest and largest aliens, calculate the total size of all aliens, and sort the aliens in ascending order.

Go ahead, hit the `Run` button, and explore the results!
哇！你发现了一些外星物种！它们的大小记录在名为“alien_sizes”的列表中。
在提供的代码中，您将使用 Python 的内置函数来识别最小和最大的外星人，计算所有外星人的总大小，并按升序对外星人进行排序。
继续，点击“运行”按钮，并探索结果！
```python
# Alien species have been found! Their sizes are measured:

alien_sizes = [2.8, 1.2, 3.0, 2.5, 1.8]

# Find the smallest alien size:

smallest_alien = min(alien_sizes)

print("The smallest alien is of size:", smallest_alien)

  

# Now, find the largest alien size:

largest_alien = max(alien_sizes)

print("The largest alien is of size:", largest_alien)

  

# What is the total size of all aliens combined?

total_alien_size = sum(alien_sizes)

print("Total alien size is:", total_alien_size)

  

# After this, sort the aliens by size in ascending order:

sorted_aliens = sorted(alien_sizes)

print("Aliens sorted by size:", sorted_aliens)
```

```python
# Alien species have been found! Their sizes are measured:

alien_sizes = [2.8, 1.2, 3.0, 2.5, 1.8]

# Find the smallest alien size:
smallest_alien = min(alien_sizes)
print("The smallest alien is of size:", smallest_alien)

# Now, find the largest alien size:
largest_alien = max(alien_sizes)
print("The largest alien is of size:", largest_alien)

# What is the total size of all aliens combined?
total_alien_size = sum(alien_sizes)
print("Total alien size is:", total_alien_size)

# After this, sort the aliens by size in ascending order:
sorted_aliens = sorted(alien_sizes)
print("Aliens sorted by size:", sorted_aliens)
```

When you run this code, it will output:

1. The smallest alien size.
2. The largest alien size.
3. The total size of all aliens combined.
4. The alien sizes sorted in ascending order. 

This allows for an easy understanding of the distribution and total of the alien sizes.
### 「practice」Adjusting the Temperature Calculation in Star Exploration调整星体探索中的温度计算
Space Voyager, could you please modify the solution code to produce the **average temperature** instead of the **total temperature**?

You can calculate the average by dividing the sum of elements by their count and rounding the answer.
太空旅行者，您能否修改解决方案代码以生成**平均温度**而不是**总温度**？
您可以通过将元素总数除以其数量并对答案进行四舍五入来计算平均值。
Let's go!
```python
# A list of star temperatures in thousands of Kelvin

star_temps = [5778, 9941, 3700, 25340, 7220]

  

# Let's find the coldest and hottest stars

coldest_star = min(star_temps)

hottest_star = max(star_temps)

  

# Let's also find the average temperature of the stars.

total_temp = sum(star_temps)

  

print("Coldest Star:", coldest_star, "K")

print("Hottest Star:", hottest_star, "K")

print("Total Star Temperature:", total_temp, "K")
```
```python
# A list of star temperatures in thousands of Kelvin
star_temps = [5778, 9941, 3700, 25340, 7220]

# Let's find the coldest and hottest stars
coldest_star = min(star_temps)
hottest_star = max(star_temps)

# Let's also find the average temperature of the stars.
total_temp = sum(star_temps)
average_temp = round(total_temp / len(star_temps), 2)

print("Coldest Star:", coldest_star, "K")
print("Hottest Star:", hottest_star, "K")
print("Average Star Temperature:", average_temp, "K")
```

This modified code calculates and prints the average temperature of the stars by dividing the total temperature by the number of stars and rounding the result to two decimal places.
### 「practice」Planet Sizes Analysis Bug Fix行星尺寸分析错误修复
Hold on, Space Voyager! The provided code block contains an error. The purpose of this code is to print out the smallest, largest, total size, and average size of the planets. However, the output does not seem correct.
坚持住，太空旅行者！提供的代码块包含错误。此代码的目的是打印出行星的最小、最大、总尺寸和平均尺寸。但是，输出似乎不正确。
Please examine the code and correct the error.
```python
# List of the sizes of 5 planets in kilometers

planet_sizes = [12341, 6786, 2435, 3475, 3999]

min_size = min(planet_sizes)

max_size = max(planet_sizes)

total_sizes = sum(planet_sizes)

average_size = round(max_sizes / len(planet_sizes))

  

print(f"The smallest planet is {min_size} kilometers.")

print(f"The largest planet is {max_size} kilometers.")

print(f"The total size of the planets is {total_sizes} kilometers.")

print(f"The average size of the planets is {average_size} kilometers.")
```
解题
```python
# List of the sizes of 5 planets in kilometers
planet_sizes = [12341, 6786, 2435, 3475, 3999]

min_size = min(planet_sizes)
max_size = max(planet_sizes)
total_sizes = sum(planet_sizes)
average_size = round(total_sizes / len(planet_sizes))

print(f"The smallest planet is {min_size} kilometers.")
print(f"The largest planet is {max_size} kilometers.")
print(f"The total size of the planets is {total_sizes} kilometers.")
print(f"The average size of the planets is {average_size} kilometers.")
```

The error in the original code was due to a typo: `max_sizes` should be `total_sizes` when calculating the average size. This corrected code properly calculates and prints the smallest, largest, total size, and average size of the planets.

### 「practice」Add Missing Python Built-in Functions to Complete the Code添加缺少的 Python 内置函数以完成代码
Spectacular work, Stellar Navigator! Now, let's add some more excitement, shall we? There are two pieces of missing code; fill them and ensure the code runs smoothly. Keep on counting!
出色的工作，Stellar Navigator！现在，让我们再增加一些刺激，好吗？有两段缺失的代码；填写它们并确保代码顺利运行。继续数数！
```python
# A list of the distances of planets from the Sun in astronomical units (AU)

planet_dist = [0.39, 0.723, 1, 1.524, 5.203, 9.537, 19.18, 30.07, 39.48]

  

print("Total number of planets: ", len(planet_dist))

print("Closest planet to the Sun: ", min(planet_dist), "AU")

# TODO: Write the command to find and print the max value from the list

# TODO: Write the command to sum up the elements of the list, then print the sum
```
解题
```python
# A list of the distances of planets from the Sun in astronomical units (AU)
planet_dist = [0.39, 0.723, 1, 1.524, 5.203, 9.537, 19.18, 30.07, 39.48]

print("Total number of planets: ", len(planet_dist))
print("Closest planet to the Sun: ", min(planet_dist), "AU")

# Find and print the farthest planet from the Sun
print("Farthest planet from the Sun: ", max(planet_dist), "AU")

# Sum up the elements of the list, then print the sum
total_distance = sum(planet_dist)
print("Total distance of all planets from the Sun: ", total_distance, "AU")
```

This code now correctly finds and prints the farthest planet from the Sun and the total distance of all planets from the Sun.
### 「practice」Exploring the Cosmos: Analyzing Planet Sizes探索宇宙：分析行星大小
Great job so far, Space Voyager! The cosmos awaits your discovery. This time around, let's leverage your Python skills to explore the dimensions of various planets.

Your task is to identify the smallest planet size, calculate the total size of all planets, and then arrange the planets according to their size.
到目前为止，你做得很棒，太空旅行者！宇宙正在等待你的探索。这一次，让我们利用你的 Python 技能来探索各个星球的尺寸。
您的任务是找出最小的行星尺寸，计算所有行星的总尺寸，然后根据尺寸对行星进行排列。

Traverse the cosmos with Python, Voyager! I wish you the best of luck.
旅行者，用 Python 穿越宇宙吧！祝你好运。
```python
# Below is the list representing the sizes of some planets in our cosmos in thousands of kilometers.

planet_sizes = [20, 32, 12, 65, 30, 10]

  

# TODO: Use Python's built-in function to find the size of the smallest planet and print it

  

# TODO: Find the total size of all planets in the list and print it

  

# TODO: Order the planets by their size and print the ordered list
```

解题
```python
# Below is the list representing the sizes of some planets in our cosmos in thousands of kilometers.
planet_sizes = [20, 32, 12, 65, 30, 10]

# Find the size of the smallest planet and print it
smallest_planet_size = min(planet_sizes)
print("The smallest planet size is:", smallest_planet_size, "thousand kilometers")

# Find the total size of all planets in the list and print it
total_planet_size = sum(planet_sizes)
print("The total size of all planets is:", total_planet_size, "thousand kilometers")

# Order the planets by their size and print the ordered list
ordered_planets = sorted(planet_sizes)
print("Planets ordered by size:", ordered_planets)
```

This code will identify the smallest planet size, calculate the total size of all planets, and arrange the planets according to their size in ascending order.
# [Lesson 4: Unraveling Python's Complex Built-in Functions: A Galactic Tour of map(), filter(), and zip() Functions](https://learn.codesignal.com/preview/lessons/308)



##### Diving into the map() Function

We begin with `map()`, a tool akin to a space probe that applies the same function on each item of a list. Here's how to utilize it: `map(func, list)`. Let's apply it to double the numbers in a list:
```python
def double(num): # Our function that doubles the input number
    return num * 2

numbers = [1, 2, 3, 4, 5]  # Our list 
doubled_numbers = list(map(double, numbers))  # Applying `double` function to each element of the list

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]
```
Excellent work! With `map()`, we've doubled the items in our list.
##### Exploring the filter() Function

Next up is `filter()`. It sifts out items based on a condition, acting like a cosmic patrol, filtering only those elements of the list that satisfy the provided condition (filter). It operates similarly to `map()`, except the function must return `True` or `False`. Let's extract the even numbers:

```python
def is_even(num): # Our function, returning True only for even numbers
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Our list

even_numbers = list(filter(is_even, numbers))  # Filtering even numbers

print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```
Congratulations! We've used `filter()` to include only even numbers!
##### Getting a Grip on the zip() Function

Finally, let's demystify the `zip()` function. It combines multiple lists, much like a bridge in spacetime. `zip()` returns a list of pairs (tuples) - a pair of the first elements from both lists, a pair of the second elements from both lists, etc. Let's observe it in action as it pairs names with ages:
```python
names = ["John", "Sara", "Tim", "Lisa"]  # List of names
ages = [25, 30, 35, 28]  # List of ages

names_ages = list(zip(names, ages))  # Zipping lists into tuples

print(names_ages)  # Output: [('John', 25), ('Sara', 30), ('Tim', 35), ('Lisa', 28)]
```
Cheers, astronauts! We've watched `zip()` unite names and ages, forming tuples.
##### Lesson Summary 课程总结

Excellent explorations, astronauts! We've untangled the complexities of `map()`, `filter()`, and `zip()`. Our learning journey promises to continue with hands-on practices next. By resolving diverse problems, you'll cement your understanding. As the adage goes, **you learn to code by coding**! So, prepare for hands-on coding missions. Safe journey, space commanders!  
优秀的探索，宇航员！我们已经解开了 `map()` ， `filter()` 和 `zip()` 的复杂性。我们的学习之旅承诺接下来将继续进行实践实践。通过解决各种问题，您将巩固您的理解。俗话说，你通过编码来学习编码！因此，请为动手编码任务做好准备。一路平安，太空指挥官们！
### 「practice」A Cosmic Approach to the `zip()` Function
Hello, my astronomical friend! In this task, we're going to see the `zip()` function in action. We have two lists related to the exploration of our solar system — _planet names_ and _their sizes_. Watch as we use `zip()` to combine them into a neat package, thereby making the data more interconnected and easier to understand.  
你好，我的天文朋友！在此任务中，我们将看到 `zip()` 函数的运行情况。我们有两个与探索太阳系有关的清单——行星名称和它们的大小。观看我们使用 `zip()` 将它们组合成一个整洁的包，从而使数据更加互联且更易于理解。

Simply hit the `Run` button and witness it in action!  
只需点击 `Run` 按钮，即可见证它的实际效果！
```python
planets_sizes = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528] # diameters of planets (Mercury to Neptune) in km

planets_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

  

# The zip function helps us create a tuples list with planet name and its size for easier identification

planets_tuples = list(zip(planets_names, planets_sizes))

print(planets_tuples)
```
### 「practice」Identifying Larger Planets in the Universe
Good work, _Space Voyager_!  
干得好，太空旅行者！

Now, let's tweak the mission slightly. Change the starter code to display only planets that are greater than 100 in their size. Apply the skills you learned in this lesson to complete the change.  
现在，让我们稍微调整一下任务。修改初始代码，使其仅显示尺寸大于 100 的行星。运用你在本课中学到的技能来完成修改。

Fly high! 展翅高飞！

```python
# Let's continue our space exploration and further explore the secrets of the Universe!

  

planet_sizes = [100, 125, 90, 95, 110, 120, 155] # Planet sizes in arbitrary units

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune'] # Names of respective planets

  

def filter_size(size):

return size < 100

  

# The filter() function filters out items based on a condition. Here, we are using it to filter planets that are smaller than 100.

small_planets = list(filter(filter_size, planet_sizes))

  

# The zip() function pairs elements from two lists. Here, we are using it to pair planet names with their relative sizes.

planet_size_pairs = list(zip(planet_names, planet_sizes))

  

print("Sizes of planets: ", planet_sizes)

print("Planets smaller than 100: ", small_planets)

print("Planet names and their respective sizes: ", planet_size_pairs)
```




To modify the code to display only the planets that are greater than 100 in size, we need to update the filtering condition. Instead of filtering out planets that are smaller than 100, we will filter out planets that are greater than 100.

Here's the updated code:

```python
planet_sizes = [100, 125, 90, 95, 110, 120, 155]  # Planet sizes in arbitrary units
planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']  # Names of respective planets

def filter_size(size):
    return size > 100

# The filter() function filters out items based on a condition. Here, we are using it to filter planets that are greater than 100.
large_planets = list(filter(filter_size, planet_sizes))

# The zip() function pairs elements from two lists. Here, we are using it to pair planet names with their relative sizes.
planet_size_pairs = list(zip(planet_names, planet_sizes))

# Filtering the planet names based on the sizes that are greater than 100.
filtered_planet_size_pairs = [(name, size) for name, size in planet_size_pairs if size > 100]

print("Sizes of planets: ", planet_sizes)
print("Planets greater than 100: ", large_planets)
print("Filtered planet names and their respective sizes: ", filtered_planet_size_pairs)
```

This code makes the following changes:
1. The `filter_size` function now returns `True` for sizes greater than 100.
2. The `large_planets` list is generated using the `filter_size` function to include only planet sizes greater than 100.
3. The `filtered_planet_size_pairs` list comprehension filters `planet_size_pairs` to include only those planets with sizes greater than 100.

When you run this code, it will output the sizes of all planets, the sizes of planets greater than 100, and the names and sizes of those planets.

### 「practice」Fix the Planet-Distance Standardization
Galactic Pioneer, are you ready for your next mission? There's a minor hiccup in our current code block, which is causing an incorrect output - Neptune is missing in the output for some reason. Can you identify and correct the error?  
银河先锋，准备好迎接你的下一个任务了吗？我们当前的代码块出现了一个小故障，导致输出不正确 - 出于某种原因，输出中缺少海王星。你能找到并纠正错误吗？

Run the code and examine the error message to help guide you. Let's get this spaceship back on track!  
运行代码并检查错误信息以获取指导。让我们让这艘宇宙飞船重回正轨！

```python
# Given lists of planets and their distances from the sun

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

distances = [58, 108, 150, 228, 778, 1429, 2871] # in millions of kilometers

  

# We are going to use the zip() function to couple each planet with its respective distance

planet_distance = list(zip(planets, distances))

  

print(planet_distance)
```

It appears that the error in your code arises because the `distances` list contains only 7 elements, whereas the `planets` list contains 8 elements. The zip function pairs elements from two lists based on the shortest list provided, which is why Neptune is missing from the output; its corresponding distance is not specified.

Here's how you can fix it:

1. Add the missing distance for Neptune in the `distances` list. Neptune is approximately 4495 million kilometers from the Sun.
2. Correct the list and then re-run the `zip()` function.

Here's the corrected code:

```python
# Given lists of planets and their distances from the sun

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Corrected distances list with Neptune's distance added
distances = [58, 108, 150, 228, 778, 1429, 2871, 4495] # in millions of kilometers

# We are going to use the zip() function to couple each planet with its respective distance
planet_distance = list(zip(planets, distances))

print(planet_distance)
```

This will generate the complete list of planets paired with their respective distances from the sun, including Neptune.

🌌 **太空图书馆日志** 🌌

**第65天**

任务：寻找海王星
---

### 📝 代码示例
```python
# Given lists of planets and their distances from the sun

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Corrected distances list with Neptune's distance added
distances = [58, 108, 150, 228, 778, 1429, 2871, 4495] # in millions of kilometers

# We are going to use the zip() function to couple each planet with its respective distance
planet_distance = list(zip(planets, distances))

# Print the list of planet-distance pairs
print(planet_distance)
```

### 🔍 小知识点
1. **zip() 函数**: 用于将多个可迭代对象（如列表、元组）合并成一个迭代对象，每个元素是一个元组。这对于同时处理多个相关的数据集非常有用。

### 📢 结果
```plaintext
[('Mercury', 58), ('Venus', 108), ('Earth', 150), ('Mars', 228), ('Jupiter', 778), ('Saturn', 1429), ('Uranus', 2871), ('Neptune', 4495)]
```

---

### 解释

在这个代码示例中，我们使用 Python 的 `zip()` 函数将行星的名称与其从太阳的距离结合起来。通过将这两个列表组合成一个包含元组的列表，每个元组都包含行星的名称及其距离（以百万公里计），我们可以更方便地识别和使用这些数据。通过添加遗漏的 Neptune 数据，我们确保了数据集的完整性。

继续保持这种探索精神，编写更多有趣的代码吧！🚀🌟

---
### 「practice」Pairing Planets with Their Sizes
Galactic Pioneer, it's your turn to practice the knowledge you've acquired in previous lessons. You are to access data related to some known planets and their sizes. Load this data into Python and use the built-in `zip()` function to pair each planet with its corresponding size.

Afterward, filter the pairs to leave only planets with a size of at least 500 million square kilometers.
```python
# List of planet names

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

  

# List of planet sizes in square kilometers

sizes = [47420000, 46023860, 510072000, 144798500, 61419434000, 42710862000, 8082923000, 7615924000]

  

# TODO: Utilize the zip function to combine the planet names and sizes

  

def size_filter(planet_tuple):

# TODO: implement a filter function that returns whether a `planet_tuple` (planet, size)

# has a size of at least 500 million

pass

  

# TODO: Utilize the filter function to filter only tuples (planet, size) with a size of at least 500000000

  

# TODO: print the filtered combination of planets and their sizes
```

解题
To filter the pairs to leave only planets with a size of at least 500 million square kilometers (500,000,000 square kilometers), you can use the following Python code:

```python
# List of planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# List of planet sizes in square kilometers
sizes = [47420000, 46023860, 510072000, 144798500, 61419434000, 42710862000, 8082923000, 7615924000]

# Utilize the zip function to combine the planet names and sizes
planet_size_pairs = list(zip(planets, sizes))

def size_filter(planet_tuple):
    # Implement a filter function that returns whether a `planet_tuple` (planet, size)
    # has a size of at least 500 million
    return planet_tuple[1] >= 500000000

# Utilize the filter function to filter only tuples (planet, size) with a size of at least 500000000
filtered_planet_sizes = list(filter(size_filter, planet_size_pairs))

# Print the filtered combination of planets and their sizes
print(filtered_planet_sizes)
```

Explanation:
1. **List Initialization**: We define two lists, `planets` and `sizes`, that contain the names and surface areas of the planets, respectively.
2. **Combining Lists**: The `zip()` function is used to combine these two lists into a list of tuples, `planet_size_pairs`.
3. **Filtering Function**: The `size_filter` function is defined to check if the size of a planet (the second element in the tuple) is at least 500 million square kilometers.
4. **Filtering Pairs**: The `filter()` function is used to apply the `size_filter` function to the list of tuples, resulting in `filtered_planet_sizes`, which contains only the planets with sizes of at least 500 million square kilometers.
5. **Output**: The filtered list is printed to display the planets and their sizes that meet the criteria.

When you run this code, you should see the output:

```python
[('Earth', 510072000), ('Jupiter', 61419434000), ('Saturn', 42710862000)]
```
### 「practice」Mapping and Zipping Celestial Distances

Alright, Celestial Traveler! It's time to polish your newfound knowledge of the `map()` and `zip()` functions.

We have planets and their respective distances from the Sun. Our task will involve converting these distances from kilometers to miles and pairing up the planets with their corrected distances. Follow the **TODO** comments closely as you write your code.
我们有行星以及它们各自与太阳的距离。我们的任务包括将这些距离从公里转换为英里，并将行星与其校正后的距离配对。编写代码时请严格遵循 TODO 注释。
```python
# Let's create a list of 5 planets and their distances from the Sun in millions of kilometers

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]

distances = [58, 108, 150, 228, 778]

  

# TODO: Convert these distances from kilometers to miles using `map()`

# 1 kilometer = 0.621371 mile

  

# TODO: Pair up the planets and their distances in miles from the Sun using `zip()`

  

# TODO: Print the final list of combined planets and their mile distance from the Sun
```
解题
Sure, let's complete the code to convert the distances from kilometers to miles using the `map()` function and then pair up the planets with their corrected distances using the `zip()` function.

Here's the implementation:

```python
# Let's create a list of 5 planets and their distances from the Sun in millions of kilometers
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
distances_km = [58, 108, 150, 228, 778]

# Convert kilometers to miles
def km_to_miles(km):
    return km * 0.621371

# Convert these distances from kilometers to miles using `map()`
distances_miles = list(map(km_to_miles, distances_km))

# Pair up the planets and their distances in miles from the Sun using `zip()`
planet_distance_pairs = list(zip(planets, distances_miles))

# Print the final list of combined planets and their mile distance from the Sun
print(planet_distance_pairs)
```

Explanation:
1. **List Initialization**: We define two lists, `planets` and `distances_km`, that contain the names and distances of the planets from the Sun in millions of kilometers.
2. **Conversion Function**: The `km_to_miles` function converts kilometers to miles by multiplying the input distance by 0.621371.
3. **Using `map()`**: The `map()` function applies the `km_to_miles` function to each element in the `distances_km` list, converting all distances to miles. The `list()` function is used to convert the map object to a list, `distances_miles`.
4. **Using `zip()`**: The `zip()` function combines the `planets` and `distances_miles` lists into a list of tuples, `planet_distance_pairs`, where each tuple contains a planet and its distance from the Sun in miles.
5. **Output**: The final list of combined planets and their distances in miles is printed.

When you run this code, you should see the output:

```python
[('Mercury', 36.039518), ('Venus', 67.108068), ('Earth', 93.20565), ('Mars', 141.745188), ('Jupiter', 483.556738)]
```
# [Lesson 5: Journey Through the Universe of Python Functions: Optional and Variable-length Arguments Explained](https://learn.codesignal.com/preview/lessons/309)
##### Introduction and Overview

Welcome back, explorers! Today, we're delving into _optional and variable-length arguments_ in Python. Just as a space mission requires essential tools and optional gear depending on the mission, Python functions involve required and optional arguments. So, let's embark on this mission!
##### Taking Off: Exploring Optional Arguments

Firstly, let's tackle optional arguments! Optional arguments are parameters that a function can accept but don't necessarily need to function. They have a default value, which the function uses if no argument is provided during the function call.
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Luke", "May the Force be with you") # Prints: "May the Force be with you, Luke!"
greet("Han") # Prints: "Hello, Han!"
```
In this function, `name` is essential, whereas `greeting` is optional, with "Hello" as the default. The optional argument depends on whether or not it's provided during the function call.
##### Igniting the Rocket: Using Optional Arguments

Next, we will look at calling functions with optional arguments. You have the flexibility to specify arguments via their position or by their name:
```python
greet("Luke", greeting="May the Force be with you") # Prints: "May the Force be with you, Luke!"
greet(name="Han") # Prints: "Hello, Han!"
```
These function invocations do the same thing — they just indicate arguments differently. However, remember not to provide more arguments than those listed in the function or forget the required ones — if so, Python will raise an Error!

##### Thrusters on Full: A Voyage to Variable-length Arguments

Are you ready for variable-length arguments? In Python, a function can handle an uncertain number of arguments using an asterisk (`*`) in front of an argument's name.

```python
def launch_payload(*payload):
    print("Launching payload into space:")
    for item in payload:
        print(f"- {item}")

launch_payload("Satellite", "Rover", "Radio Beacon")
"""
Prints:
Launching payload into space:
- Satellite
- Rover
- Radio Beacon
"""
```
Here, the function `launch_payload()` accepts any number of arguments, bundled into a tuple named `payload`. We then print each item in `payload`.

##### Warp Drive: Exploring Python's '**kwargs'

With the warp drive on, let's explore Python's `**kwargs` mechanism! It allows us to handle an unspecified number of keyword arguments — in other words, arguments associated with keywords.

```python
def mission_journal(**journal_entry):
    print("Mission Journal Entry:")
    for key, value in journal_entry.items(): # iterating from the arguments dictionary
        print(f"{key}: {value}")

mission_journal(Mission="Moon landing", Astronaut="Neil Armstrong", Year=1969)
"""
Prints:
Mission Journal Entry:
Mission: Moon landing
Astronaut: Neil Armstrong
Year: 1969
"""
```
In `mission_journal()`, `**journal_entry` represents an unknown number of keyword arguments packed into a dictionary. The function prints each entry from the mission journal.

##### Securing the Spacesuit: Guidelines and Best Practices

As we conclude our journey, remember these best practices for optional and variable-length arguments:
```python
def example_function(required_arg1, required_arg2, *args, optional_arg="default value", **kwargs):
    pass
```
Here, required arguments come first, followed by variable-length arguments (`*args`), an optional argument, and keyword arguments (`**kwargs`). Remember, writing clear and logical code is crucial!

Here is a short example of the above concept:
```python
def secure_spacesuit(helmet_locked, suit_pressure, *gloves, boots="Standard", **extras):
    print("Helmet locked:", helmet_locked, 
          "\nSuit Pressure:", suit_pressure,  
          "\nGloves:", gloves, 
          "\nBoots:", boots, 
          "\nExtras:", extras)

secure_spacesuit(True, "Optimal", "Glove1", "Glove2", boots="MoonWalkers", OxygenLevel=90, TemperatureControl="On")

"""
Prints:
Helmet locked: True
Suit Pressure: Optimal
Gloves: ('Glove1', 'Glove2')
Boots: MoonWalkers
Extras: {'OxygenLevel': 90, 'TemperatureControl': 'On'}
"""
```
Here, we're setting the helmet's status, spacesuit's pressure, type of gloves used (with the flexibility to accommodate any number), type of boots, and any additional extras such as oxygen level in the tank.
> 在这里，我们设置头盔的状态、宇航服的压力、使用的手套类型（可以灵活地容纳任何数量）、靴子类型以及任何其他附加功能，例如罐中的氧气水平。

##### Lesson Summary 课程总结

That's a wrap! You've successfully navigated optional and variable-length arguments, equipping you to write more flexible functions. Our upcoming tasks will solidify what you've learned. Practice makes perfect! Onward to the practice exercises. Buckle up and have fun!  
这是一个包装！您已成功导航可选和可变长度参数，使您能够编写更灵活的函数。我们接下来的任务将巩固您所学到的知识。熟能生巧！继续练习。系好安全带，玩得开心！

### 「practice」Surveying Planets with Python's kwargs Mechanism

Hold onto your space helmet, Explorer! There will be times when you may need to survey multiple planets and check different specifications for each. By using Python's `**kwargs` mechanism, you can handle an unspecified number of keyword arguments. Let's see it in action!  
戴好你的太空头盔，探险家！有时您可能需要勘测多个行星并检查每个行星的不同规格。通过使用Python的 `**kwargs` 机制，您可以处理未指定数量的关键字参数。让我们看看它的实际效果！
```python
def survey_universe(planets, **specs):

print(f"Surveying {planets} planets.")

for item, detail in specs.items():

print(f"Detail: {item} = {detail}")

  

survey_universe(3, Planet1="Mars", Planet2="Venus", Planet3="Earth")
```

输出
Surveying 3 planets.  
Detail: Planet1 = Mars  
Detail: Planet2 = Venus  
Detail: Planet3 = Earth
### 「practice」Changing the Default Captain

Alright, Space Explorer! The task is now up to you. We have implemented a function that prints all information about our galaxy travel. However, it seems that we are still using the default value for the `captain`, let's change it! Change the function call to provide a custom captain name.  
好吧，太空探索者！现在任务就交给你了。我们已经实现了一个功能，可以打印有关我们银河旅行的所有信息。然而，我们似乎仍然使用 `captain` 的默认值，让我们更改它！更改函数调用以提供自定义队长名称。

You're doing a great job, so keep up the excellent work!  
你做得很好，所以继续努力吧！

```python
def travel_to_galaxy(galaxy, *spaceships, captain="Captain Kirk", **crew_members):

print(f"{captain} is leading the voyage to {galaxy} with:")

for ship in spaceships:

print(f" - {ship}")

  

print("\nThe crew members include:")

for position, member in crew_members.items():

print(f"{position}: {member}")

  

travel_to_galaxy("Andromeda", "Enterprise", "Discovery", Pilot="Spock", Engineer="Scott")
```
### 「practice」Exploring Space with the Wrong Equipment
Alright, Space Explorer! The task is now up to you. We have implemented a function that prints all information about our galaxy travel. However, it seems that we are still using the default value for the `captain`, let's change it! Change the function call to provide a custom captain name.  
好吧，太空探索者！现在任务就交给你了。我们已经实现了一个功能，可以打印有关我们银河旅行的所有信息。然而，我们似乎仍然使用 `captain` 的默认值，让我们更改它！更改函数调用以提供自定义队长名称。

You're doing a great job, so keep up the excellent work!  
你做得很好，所以继续努力吧！
```python
def travel_to_galaxy(galaxy, *spaceships, captain="Captain Kirk", **crew_members):

    print(f"{captain} is leading the voyage to {galaxy} with:")

    for ship in spaceships:

        print(f" - {ship}")

  

    print("\nThe crew members include:")

    for position, member in crew_members.items():

        print(f"{position}: {member}")

  

travel_to_galaxy("Andromeda", "Enterprise", "Discovery", Pilot="Spock", Engineer="Scott")
```
#### 解题
To change the captain name from the default “Captain Kirk” to a custom name in the travel_to_galaxy function call, we need to pass the new captain name as an argument. Here’s how you can do it:
```python
def travel_to_galaxy(galaxy, *spaceships, captain="Captain Kirk", **crew_members):
    print(f"{captain} is leading the voyage to {galaxy} with:")
    for ship in spaceships:
        print(f" - {ship}")

    print("\nThe crew members include:")
    for position, member in crew_members.items():
        print(f"{position}: {member}")

travel_to_galaxy("Andromeda", "Enterprise", "Discovery", captain="Captain Picard", Pilot="Spock", Engineer="Scott")

```
    In this updated function call, the captain is now “Captain Picard”.
    
>==Captain Picard is leading the voyage to Andromeda with:==  
 - ==Enterprise==  
 - ==Discovery==  
  
==The crew members include:==  
==Pilot: Spock==  
==Engineer: Scott==

### 「practice」Adding Mission Details and Equipment Information
Fantastic job! It seems I've made a slight error. Our system isn't collecting all the characteristics of the planets as it should. Could you analyze the `planets` function and rectify the issue? Remember, happy debugging!
```python
def planets(*planets_name, orbit="None", *characteristics):

print("Planets in our Space Mission:")

for planet in planets_name:

print(f"- {planet}")

print(f"All planets are in {orbit} orbit.")

for key, value in characteristics.items():

print(f"{key}: {value}")

  

planets("Mars", "Jupiter", "Saturn", orbit="Elliptical", Color="Red", Radius=6792)
```
#### 解题

Fantastic job! It seems I've made a slight error. Our system isn't collecting all the characteristics of the planets as it should. Could you analyze the `planets` function and rectify the issue? Remember, happy debugging!
```python
def planets(*planets_name, orbit="None", *characteristics):

print("Planets in our Space Mission:")

for planet in planets_name:

print(f"- {planet}")

print(f"All planets are in {orbit} orbit.")

for key, value in characteristics.items():

print(f"{key}: {value}")

  

planets("Mars", "Jupiter", "Saturn", orbit="Elliptical", Color="Red", Radius=6792)
```
This corrected version properly captures the planet names, the orbit type, and any additional characteristics as keyword arguments.
#### 整理知识卡片
### 🌌 **太空图书馆日志** 🌌

**第65天**

任务：整理行星特性函数
---

### 📝 代码示例
```python
def planets(*planets_name, orbit="None", **characteristics):
    print("Planets in our Space Mission:")

    for planet in planets_name:
        print(f"- {planet}")

    print(f"All planets are in {orbit} orbit.")

    for key, value in characteristics.items():
        print(f"{key}: {value}")

planets("Mars", "Jupiter", "Saturn", orbit="Elliptical", Color="Red", Radius=6792)
```

### 🔍 小知识点
1. **`*args` 和 `**kwargs`**: 
   - `*args` 用于传递任意数量的位置参数。
   - `**kwargs` 用于传递任意数量的关键字参数。
   - 在函数定义中，`*args` 必须放在 `**kwargs` 之前。

### 📢 结果
```plaintext
Planets in our Space Mission:
- Mars
- Jupiter
- Saturn
All planets are in Elliptical orbit.
Color: Red
Radius: 6792
```

---

### 解释

在这个代码示例中，我们使用了 Python 的 `*args` 和 `**kwargs` 来编写一个灵活的函数，可以接收任意数量的行星名称和它们的特性。这样，我们可以很方便地扩展和修改行星的列表及其相关特性。

继续保持这种探索精神，编写更多有趣的代码吧！🚀🌟
#### 整理知识卡片2
### 🌌 **太空图书馆日志** 🌌

**第65天**

任务：整理行星特性函数
---

### 📝 代码示例
```python
def planets(*planets_name, orbit="None", **characteristics):
    print("Planets in our Space Mission:")

    for planet in planets_name:
        print(f"- {planet}")

    print(f"All planets are in {orbit} orbit.")

    for key, value in characteristics.items():
        print(f"{key}: {value}")

planets("Mars", "Jupiter", "Saturn", orbit="Elliptical", Color="Red", Radius=6792)
```

### 🔍 小知识点
1. **`*args` 和 `**kwargs`**: 
   - `*args` 用于传递任意数量的位置参数。
   - `**kwargs` 用于传递任意数量的关键字参数。
   - 在函数定义中，`*args` 必须放在 `**kwargs` 之前。

### 📢 结果
```plaintext
Planets in our Space Mission:
- Mars
- Jupiter
- Saturn
All planets are in Elliptical orbit.
Color: Red
Radius: 6792
```

---

### 解释

在这个代码示例中，我们使用了 Python 的 `*args` 和 `**kwargs` 来编写一个灵活的函数，可以接收任意数量的行星名称和它们的特性。这样，我们可以很方便地扩展和修改行星的列表及其相关特性。

继续保持这种探索精神，编写更多有趣的代码吧！🚀🌟

### 「practice」Building a Ready-to-Launch Spaceship Function
Fantastic job! It seems I've made a slight error. Our system isn't collecting all the characteristics of the planets as it should. Could you analyze the `planets` function and rectify the issue? Remember, happy debugging!  
太棒了！看来我犯了一个小错误。我们的系统没有按照应有的方式收集行星的所有特征。您能否分析一下 `planets` 函数并纠正该问题？请记住，调试愉快！


```python
def planets(*planets_name, orbit="None", *characteristics):

print("Planets in our Space Mission:")

for planet in planets_name:

print(f"- {planet}")

print(f"All planets are in {orbit} orbit.")

for key, value in characteristics.items():

print(f"{key}: {value}")

  

planets("Mars", "Jupiter", "Saturn", orbit="Elliptical", Color="Red", Radius=6792)
```
解题：
Here's the updated code that meets the requirements:

```python
def space_mission_report(name, mission="Unspecified", *details, **equipment):
    print(f"Astronaut {name} is prepared for the mission: {mission}")
    
    print("Mission Details:")
    for detail in details:
        print(f"- {detail}")
    
    print("Equipment details are as follows:")
    for key, value in equipment.items():
        print(f"- {key}: {value}")

space_mission_report("John Doe", "Mars Rover Deployment", "Exploration", "Research", Spacesuit="Advanced", Food="Boost Pack", Communication="Satellite Radio")
```

This code will print the astronaut's name, the mission, the mission details, and the equipment details. The `*details` parameter allows for any number of additional details to be passed to the function, and the `**equipment` parameter allows for any number of key-value pairs to be passed as equipment details. The code then iterates over these details and prints them out in a readable format.

## 「Practice」
Explorer, it's time to assemble everything you've learned! Your task involves creating a function that provides information about a spaceship and its crew. This function should first print the pilot's name, followed by the names of the crew members, the spaceship's name, and finally, the spaceship's specifications.  
探险家，是时候把你所学的一切付诸实践了！你的任务是创建一个函数，该函数可以提供有关宇宙飞船及其船员的信息。此函数应首先打印飞行员的姓名，然后是船员姓名、宇宙飞船名称，最后是宇宙飞船的规格。
```python
# TODO: Define a function named 'spaceship_params' which accepts arguments:

# pilot's name, names of crew members, optional spaceship name, and other optional spaceship specifications.

  

# TODO: Within the function, print the pilot's name and the names of the crew members.

# Also print the name of the spaceship and its specifications.

  

# TODO: Call the above function with suitable arguments to test if it's working as expected.
```

To create a function that provides information about a spaceship and its crew, we will define a Python function named `spaceship_params`. This function will accept arguments for the pilot's name, crew members' names, the spaceship's name, and its specifications. The function will then print these details in the specified order.

Here's the code to achieve this:

```python
def spaceship_params(pilot, crew, spaceship_name=None, **specs):
    # Print the pilot's name
    print("Pilot's Name:", pilot)
    
    # Print the names of the crew members
    print("Crew Members:", ", ".join(crew))
    
    # Print the spaceship's name if provided
    if spaceship_name:
        print("Spaceship's Name:", spaceship_name)
    
    # Print the spaceship's specifications if provided
    if specs:
        print("Spaceship's Specifications:")
        for key, value in specs.items():
            print(f"  {key}: {value}")

# Example usage
pilot_name = "James T. Kirk"
crew_members = ["Spock", "Leonard McCoy", "Montgomery Scott"]
spaceship = "USS Enterprise"
specifications = {
    "Length": "288.6 meters",
    "Width": "127.1 meters",
    "Height": "72.6 meters",
    "Maximum Speed": "Warp 8"
}

spaceship_params(pilot_name, crew_members, spaceship, **specifications)
```

This function first prints the pilot's name, then the names of the crew members, followed by the spaceship's name if it is provided, and finally the spaceship's specifications if any are provided. The `**specs` parameter allows for an arbitrary number of keyword arguments to represent the spaceship's specifications.

The example usage demonstrates how to call the function with appropriate arguments to test if it works as expected. When executed, the output will look like this:

```
Pilot's Name: James T. Kirk
Crew Members: Spock, Leonard McCoy, Montgomery Scott
Spaceship's Name: USS Enterprise
Spaceship's Specifications:
  Length: 288.6 meters
  Width: 127.1 meters
  Height: 72.6 meters
  Maximum Speed: Warp 8
```
# [Lesson 6: Mastering Exception Handling in Python Functions](https://learn.codesignal.com/preview/lessons/310)
Buckle up! 🚀 We're ready to tackle exception handling in Python functions. This will make your code more resilient and reliable - just like a real spaceship! Dive right in.

##### Introduction and Overview

Welcome! Today, we will manage exceptions within Python functions, much like an astronaut tackling obstacles in space. We will delve into the concept of _functions_, acquaint ourselves with the handling of _exceptions_, and investigate their operation during function calls.
##### Exception Handling: A Primer on Python Functions

Let's take a moment to recap: An _exception_, an error that can lead to a program crash, can be disruptive. However, a Python function can attempt certain tasks and catch potential exceptions using a `try-except-finally` block. This is similar to an astronaut preparing for potential hurdles. Below is an illustration:
```python
def safe_division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Warning: Division by zero!")
```
This function monitors for a `ZeroDivisionError` when performing division.
##### Raising Exceptions Within Python Functions  
在 Python 函数中引发异常

The `raise` keyword in Python triggers an exception manually within a function. Consider a function that calculates a square root — an error should occur if the input is negative!  
Python 中的 ` `raise` ` 关键字可以在函数内部手动触发异常。例如，考虑一个计算平方根的函数——如果输入是负数，则应该发生错误！
```python
def safe_sqrt(x):
    if x < 0:
        raise ValueError("Can't compute square root of a negative number.")
    else:
        return x ** 0.5
```
An exception is raised if a negative input is detected.  
如果检测到负输入，则会引发异常。
##### Handling Exceptions Generated within Python Functions  
Python 函数内部生成的异常处理

The code that calls a function handles any possible exceptions that the function might throw. This is illustrated as follows:  
调用函数的代码会处理函数可能抛出的任何异常。这可以说明如下：
```python
def call_sqrt():
    try:
        print(safe_sqrt(-1))
    except ValueError as e:
        print("Abort mission! Error:", e)
```

In this scenario, exceptions raised in `safe_sqrt` are captured in `call_sqrt`.  
在这种情况下， `safe_sqrt` 中引发的异常会在 `call_sqrt` 中被捕获。
##### The Interplay of Exceptions in Nested Function Calls  
嵌套函数调用中异常的相互作用

Exceptions can migrate from one function to another. In nested calls, a raised exception gets passed up the chain; for instance, if `fun2` raises exceptions and the `except` block does not handle them, they're forwarded to `fun1`.  
异常可以从一个函数迁移到另一个函数。在嵌套调用中，引发的异常会沿着调用链向上抛出；例如，如果 `fun2` 引发异常，而 `except` 块没有处理它们，它们就会被转发到 `fun1` 。

```python
def fun1():
    try:
        fun2() # throws ExceptionType
    except ExceptionType2: # handling a different exception type
        # Handle exception
```
In this scenario, `fun1()` might throw `ExceptionType` if it occurs, as it's not handled by the `except` block.  
在这种情况下，如果出现 `ExceptionType` ， `fun1()` 可能会抛出异常，因为它没有被 `except` 块处理。
##### Lesson Summary and Wrap-Up  
课程总结与回顾

Congratulations! You've mastered exception handling within Python functions. Up next are practice tasks to sharpen these skills further!  
恭喜！您已经掌握了 Python 函数中的异常处理。接下来是一些练习任务，可以进一步提升您的技能！

Great job today! You've learned how to handle and manually raise exceptions in Python functions. Next, take on some challenges in the practice tasks to strengthen your understanding and continue exploring the Python universe!  
今天做得很好！你已经学习了如何在 Python 函数中处理和手动引发异常。接下来，挑战一些练习任务，巩固你的理解，继续探索 Python 的世界吧！



### 「practice」Abort Rocket Launch with Exception Handling
Hello, Space Explorer! We're setting our course for a space journey. However, space is rife with obstacles, and we have to be prepared for them. For such situations, we have our _spaghetti-code rockets_!

The provided code includes a _rocket launch sequence_ that calculates a rocket's trajectory based on its `speed` and `time`. However, we've programmed this sequence to halt the launch and raise an error if the `time` is zero or negative.

Go ahead and press `Run` to see how it works!

```python
def calculate_trajectory(speed, time):

if time <= 0:

raise ValueError("Time can't be zero or negative.")

else:

return speed * time

  

def launch_rocket():

try:

print(calculate_trajectory(5000, 0))

except ValueError as e:

print("Abort launch! Error:", e)

launch_rocket()
```


### 「practice」Restricting Space Travel Distance

You've done awesome work thus far, Stellar Navigator!

For our next space voyage, we need to ensure our spaceship doesn't run out of fuel. You'll need to modify the starter code in the `space_travel` function. An exception should be raised when the distance is greater than `1000` space units, in addition to when it's negative. Don’t forget also to update the `ValueError` message.

Onward to more space adventures!
```python
def space_travel(distance):

if distance < 0:

raise ValueError("Distance can't be negative in space travel.")

else:

return "We are traveling {} space units.".format(distance)

  

def space_travel_logging(distance):

try:

space_travel(distance)

except ValueError as e:

return "Space Travel Error: {}".format(e)

  

# Testing the function with a negative value

print(space_travel_logging(-100))

print(space_travel_logging(10))

print(space_travel_logging(1001))
```
---
🌌 太空图书馆日志 🌌

日期：2024年6月19日

任务：修改太空旅行函数

我们需要确保我们的太空船在下一次太空旅行中不会耗尽燃料。您需要修改 space_travel 函数中的起始代码。当距离大于 1000 空间单位时，应该引发异常，除此之外，当距离为负值时也应该引发异常。不要忘记更新 ValueError 消息。

继续前往更多的太空探险！

📝 修改后的代码示例
```python
def space_travel(distance):
    if distance < 0:
        raise ValueError("Distance can't be negative in space travel.")
    elif distance > 1000:
        raise ValueError("Distance is too large for space travel.")
    else:
        return "We are traveling {} space units.".format(distance)

def space_travel_logging(distance):
    try:
        return space_travel(distance)
    except ValueError as e:
        return "Space Travel Error: {}".format(e)

# Testing the function with a negative value, a valid value, and a value that is too large
print(space_travel_logging(-100))
print(space_travel_logging(10))
print(space_travel_logging(1001))
```

📢 结果
```
Space Travel Error: Distance can't be negative in space travel.
We are traveling 10 space units.
Space Travel Error: Distance is too large for space travel.
```

解释
在这个修改后的代码示例中，我们在 space_travel 函数中添加了一个额外的条件，当距离大于 1000 空间单位时，会引发异常。这确保了太空船不会尝试旅行太大的距离。

在 space_travel_logging 函数中，我添加了一个 try 块来调用 space_travel 函数和一个 except 块来捕获任何引发的 ValueError 异常。如果捕获到 ValueError，函数将返回一个包含错误消息的字符串。

当使用负值（-100）、有效值（10）和太大的值（1001）调用 space_travel_logging 函数时，函数正确地为负值引发 ValueError，并显示适当的错误消息，为太大的值引发 ValueError，并返回有效值的预期字符串。

总之，修改后的代码成功处理了距离为负值或太大的情况，并在需要时引发适当的异常和错误消息。

继续保持这种探索精神，编写更多有趣的代码吧！🚀🌟
---

### 「practice」Space Travel System Failure
Hello, Stellar Navigator!

We're experiencing a minor glitch in our space travel system. Our crew is endeavoring to journey to a celestial body, but unfortunately, the system isn't responding correctly and throws an exception instead of handling things gracefully. Please examine the code to see if you can identify and resolve the issue.

Remain bold and continue your exploration of the Python cosmos!
```python
def check_planet(planet):

if planet not in ['Earth', 'Mars', 'Mercury', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:

raise ValueError(f"{planet} is not in our solar system!")

  

def journey_to_planet(planet):

try:

check_planet(planet)

print(f"On the way to {planet}!")

except TypeError:

print("Please enter a valid planet!")

  

journey_to_planet('Pluto')
```

"Hello, intrepid space traveler! The issue in your code arises because the `check_planet` function raises a `ValueError` when an invalid planet is passed, but your `journey_to_planet` function only catches a `TypeError`. To fix this, you need to catch the `ValueError` instead. Here is the corrected code:

```python
def check_planet(planet):
    if planet not in ['Earth', 'Mars', 'Mercury', 'Venus', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        raise ValueError(f"{planet} is not in our solar system!")

def journey_to_planet(planet):
    try:
        check_planet(planet)
        print(f"On the way to {planet}!")
    except ValueError as e:
        print(e)

journey_to_planet('Pluto')
```

With this change, if you attempt to journey to 'Pluto', the system will now correctly handle the `ValueError` and inform you that 'Pluto is not in our solar system!'. Safe travels!"
### 「practice」Add Exception Handling to Rocket Launch
Well done, Stellar Navigator! Now, let's shift you into the commander's seat of our spaceship.

Write the crucial line that controls our rocket's speed checker within our launch function.

Let's go!
```python
def rocket_speed_check(speed):

if speed < 0:

raise ValueError("Speed can't be negative!")

else:

return speed

  

def launch_rocket():

# TODO: Call the `rocket_speed_check` function and do exception handling

# Log the error to the console if it appears

  

launch_rocket()
```

“Commander, to control our rocket’s speed checker and handle any exceptions during launch, you can call the rocket_speed_check function within the launch_rocket function and log any errors. Here’s the crucial line added to your launch_rocket function:
```python
def rocket_speed_check(speed):
    if speed < 0:
        raise ValueError("Speed can't be negative!")
    else:
        return speed

def launch_rocket():
    try:
        speed = rocket_speed_check(5000)  # Example speed value
        print(f"Rocket launching at speed: {speed} km/h")
    except ValueError as e:
        print(f"Error during launch: {e}")

launch_rocket()
```
This line ensures that the rocket’s speed is checked, and any errors are logged to the console. Prepare for liftoff!”
### 「practice」Plotting the Orbit: Exception Handling in the Galaxy of Python Functions
We've arrived at the final frontier, Celestial Traveler! Let's implement a function to compute the _mass_ of a planet. However, please remember that both the _diameter_ and the _density_ of the planet should be positive.

Should they be otherwise, we must handle the exception and alert with an error message.
```python
# TODO: Define a function to calculate the mass of a planet given its diameter and density.

# Remember, the density and diameter should be positive.

# Formula: mass = (4/3) * 3.14 * (diameter / 2)**3 * density

  

# To call the above function and print the result.

# Also, make sure to handle the exceptions and print the error from the exception if there's any.
```
“Celestial Traveler, let’s define a function to compute the mass of a planet, ensuring that both the diameter and density are positive. Here’s how you can implement it:
```python
def calculate_planet_mass(diameter, density):
    if diameter <= 0 or density <= 0:
        raise ValueError("Both diameter and density must be positive values.")
    radius = diameter / 2
    volume = (4/3) * 3.14 * (radius ** 3)
    mass = volume * density
    return mass

def main():
    try:
        diameter = 12742  # Example diameter in kilometers (Earth's diameter)
        density = 5.51    # Example density in g/cm^3 (Earth's density)
        mass = calculate_planet_mass(diameter, density)
        print(f"The mass of the planet is: {mass} kg")
    except ValueError as e:
        print(f"Error: {e}")

main()
```
This function calculate_planet_mass computes the mass of a planet using the given diameter and density, while ensuring that both values are positive. The main function calls this function and handles any exceptions, printing an error message if necessary. Explore the cosmos with accurate calculations!”












































