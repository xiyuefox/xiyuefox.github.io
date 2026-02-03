---
title: "Python_Iterations and Loops in Python"
date: 2026-02-03
tags: ["tech", "tutorial", "improvisation"]
categories: ["tech"]
layout: "single" 
---


6 lessons
32 practices

## Iterations and Loops in Python

Saddle up for a thrilling ride through Python's looping mechanisms! This course is ingeniously crafted to make you loop literate. By the end of this adventure, you'll be spinning through data with for and while loops, and streamlining code with Pythonic iteration patterns.

# [Lesson 1: The Interstellar For Loop Journey: Traversing Collections With Ease in Python](https://learn.codesignal.com/preview/lessons/148)

## Introduction to The For Loop Journey

Welcome! In programming, just like playing a favorite song on repeat, loops execute code repeatedly. Here, we'll explore the **"For Loop"** in Python, an iteration construct over sequences such as lists or strings.

Imagine a train journey: the train represents our loop, stopping at each station. Each station represents an item on its route, which is the `iterable`.

欢迎！在编程中，就像重复播放最喜欢的歌曲一样，循环重复执行代码。在这里，我们将探索Python中的“For Loop”，这是对列表或字符串等序列的迭代构造。

想象一次火车旅行：火车代表我们的循环，停在每个车站。每个车站代表其路线上的一个项目，即可迭代的。

## Understanding the Concept of Loops

Like replaying a song or game level, a loop continually executes a block of code until a defined condition is met. It's akin to saying, "Keep the popcorn machine running as long as the popcorn _keeps popping!_"

就像重播歌曲或游戏关卡一样，循环不断地执行代码块，直到满足定义的条件。这就像说：“只要爆米花一直在爆炸，就保持爆米花机运行！”

## Introduction to For Loops in Python

A Python For Loop looks like this:

```Python

for variable in iterable_object:
    # executable code

```

In this construct, `for` and `in` are keywords. The `variable` holds the current item in each iteration, while `iterable_object` can be a list, string, or any object that provides an item sequentially.

Let's print all elements of a list:

```Python

# List of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Print each planet
for planet in planets:
  print(planet)
"""
Prints:
Mercury
Venus
Earth
Mars
Jupiter
Saturn
Uranus
Neptune
""" 

```

This code will print every planet from the list (`Mercury`, `Venus`, `Earth`, ...), each on a separate line.

## Riding through Python For Loops: Lists and Sets

Let's delve further into For Loops by printing each number from a list:

```Python

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Print each number
for num in numbers:
  print(num)
"""
Prints:
1
2
3
4
5
"""

```

The same works for sets:

```Python

# Set of numbers
numbers = {1, 2, 5, 4, 3}

# Prints each number in the set
for num in numbers:
  print(num)
"""
Prints:
1
2
3
4
5
"""

```

Note that because sets are unordered, results might appear in any order.

## Riding through Python For Loops: Strings

Strings in Python are also `iterable`, meaning we can iterate over each character:

Python中的字符串也是可迭代的，这意味着我们可以迭代每个字符：

```Python

# A string
word = "Python"

# Print each character
for letter in word:
  print(letter)
"""
Prints:
P
y
t
h
o
n
"""

```

## Riding through Python For Loops: Dictionaries

Finally, you can also iterate over dictionaries, traversing all its keys:
最后，您也可以遍历字典，遍历其所有键：

```python

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

```

Output:

```

a
b
c

```

```Python

# A dictionary
fruit_colors = {'Apple': 'Red', 'Banana': 'Yellow', 'Grape': 'Purple'}

# Printing fruit's color for each fruit key in the dictionary
for fruit in fruit_colors:
    print("The color of", fruit, "is", fruit_colors[fruit])
"""
Prints:
The color of Apple is Red
The color of Banana is Yellow
The color of Grape is Purple
"""

```

### 「practice」Revealing the Years of Notable Space Missions

Astronaut, we've received a transmission that has decrypted the years of key space missions! Look! We have a list, `mission_years`.

I created a code that uses our trusted Python skills with a `For Loop` to print out each year. Are you ready for the revelation? Click `Run` to see them appear!

宇航员，我们接收到了一个解密了关键太空任务年份的传输！看！我们有一份清单，任务年份。
我创建了一个代码，它使用我们信赖的Python技能，通过一个for循环来打印出每一年。你准备好迎接这个启示了吗？点击运行，就可以看到它们出现！(kimi翻译)

```Python

 we've received a transmission that has decrypted the years of key space missions! Look! We have a list, mission_years.
I created a code that uses our trusted Python skills with a For Loop to print out each year. Are you ready for the revelation? Click Run to see them appear!

# List of numbers representing space mission years
mission_years = [1961, 1962, 1969, 1971, 1981, 1990, 1998, 2001, 2010]

# Using a For Loop to print each year when a notable space mission occurred
for year in mission_years:
    print("A notable space mission occurred in the year:", year)
 _______________

# List of numbers representing space mission years
mission_years = [1961, 1962, 1969, 1971, 1981, 1990, 1998, 2001, 2010]

# Using a For Loop to print each year when a notable space mission occurred
for year in mission_years:
    print("A notable space mission occurred in the year:", year)
_______________

```

  

### 「practice」Star Coordinates Calculation Fix

Let's continue with our interstellar exploration. It seems that a minor bug has surfaced in our calculation of star coordinates. At the moment, the total output of the stars' coordinates is incorrect. Could you identify and rectify this issue?

Onward to glory and beyond!

```Python

It seems that a minor bug has surfaced in our calculation of star coordinates. At the moment, the total output of the stars' coordinates is incorrect. Could you identify and rectify this issue?
___________

# List representing star coordinates in space
stars = [1, 2, 3, 4, 5]

# Initialize sum
sum_coords = 0

# Add each star coordinate to sum_coords
for coord in stars:
  sum_coords = coord

# Print sum
print("The sum of star coordinates is", sum_coords)
_______________

```

> The issue in your Python code arises from the way the sum of the coordinates is being calculated within the loop. Currently, the loop is replacing the value of `sum_coords` with each `coord` in the list `stars`, rather than adding each `coord` to the existing total of `sum_coords`. This results in `sum_coords` containing only the last coordinate value from the list, rather than the sum of all coordinates.
> 
>   
> 
> Here's how you can fix the code to correctly calculate the sum of the star coordinates:
> 
>   
> 
> ```Python
> # List representing star coordinates in space
> stars = [1, 2, 3, 4, 5]
> 
> # Initialize sum
> sum_coords = 0
> 
> # Add each star coordinate to sum_coords
> for coord in stars:
>   sum_coords += coord  # This line is corrected to add each coord to sum_coords
> 
> # Print sum
> print("The sum of star coordinates is", sum_coords)
> ```
> 
>   
> 
> With this correction (`sum_coords += coord`), each coordinate in the list `stars` is added to the total `sum_coords`. When you run this corrected code, it will output the correct sum of the coordinates:
> 
>   
> 
> ```Plain
> The sum of star coordinates is 15
> ```
> 
>   
> 
> This sum is the result of adding 1 + 2 + 3 + 4 + 5. This should resolve the issue and correctly calculate the total output of the stars' coordinates.

### 「practice」Space Race: Finding the Fastest Spaceship

Bingo, Space Adventurer! Let's make a small detour. In the provided code snippet, your task is to find the top speed from our list of spaceship speeds. You are required to replace the placeholder and complete the loop.

Remember, we have many more galaxies to explore!

```Python

# List of spaceship speeds in km/s
speeds = {28, 50, 120, 75, 98}

# Initialize variable
fastest_speed = 0

# TODO: Write a loop to go through each speed in the list.

# If the speed element from the list is faster than the current 'fastest_speed', update 'fastest_speed' to this new speed.

# Print the fastest speed
print("The fastest spaceship speed is", fastest_speed, "km/s.")

```

```Python

 Let's make a small detour. In the provided code snippet, your task is to find the top speed from our list of spaceship speeds. You are required to replace the placeholder and complete the loop.
 _____________
 # List of spaceship speeds in km/s
speeds = {28, 50, 120, 75, 98}

# Initialize variable
fastest_speed = 0

# TODO: Write a loop to go through each speed in the list.

# If the speed element from the list is faster than the current 'fastest_speed', update 'fastest_speed' to this new speed.

# Print the fastest speed
print("The fastest spaceship speed is", fastest_speed, "km/s.")
_________________

```

> Here's the completed version of your code snippet with the loop implemented to find the fastest speed from the list of spaceship speeds:
> 
>   
> 
> ```Python
> # List of spaceship speeds in km/s
> speeds = {28, 50, 120, 75, 98}
> 
> # Initialize variable
> fastest_speed = 0
> 
> # Loop through each speed in the set
> for speed in speeds:
>     # If the current speed is faster than the 'fastest_speed', update it
>     if speed > fastest_speed:
>         fastest_speed = speed
> 
> # Print the fastest speed
> print("The fastest spaceship speed is", fastest_speed, "km/s.")
> ```
> 
>   
> 
> This code correctly iterates over the set of speeds, compares each speed with the current `fastest_speed`, and updates `fastest_speed` if a faster speed is found. Finally, it prints the fastest speed from the list.

### 「practice」Unveiling the List of Earth-Like Planets

Excellent work, Space Explorer!

Let's give it another go! There are some space suit models out there.

Can you traverse the suits dictionary and calculate the total weight of all suits there? Give it a try!

```Python

# Dictionary of space suits and their weights in kg
space_suit_weights = {'Mercury suit': 21, 'Gemini suit': 16, 'Apollo suit': 32, 'Space Shuttle suit': 50}

total_weight = 0

# TODO: Use a For Loop to calculate the total weight of all space suits
print('Total suits weight:', total_weight)

```

```Python

Let's give it another go! There are some space suit models out there.
Can you traverse the suits dictionary and calculate the total weight of all suits there? Give it a try!
__________

# Dictionary of space suits and their weights in kg
space_suit_weights = {'Mercury suit': 21, 'Gemini suit': 16, 'Apollo suit': 32, 'Space Shuttle suit': 50}

total_weight = 0

# TODO: Use a For Loop to calculate the total weight of all space suits
print('Total suits weight:', total_weight)
__________

```

> To calculate the total weight of all space suits in the dictionary `space_suit_weights`, you need to iterate over the values of the dictionary and sum them up. Here's how you can modify the code snippet to achieve this:
> 
> 要计算字典space_suit_weights中所有太空服的总重量，您需要遍历字典的值并将它们相加。以下是如何修改代码片段以实现此目的：
> 
> ```Python
> # Dictionary of space suits and their weights in kg
> space_suit_weights = {'Mercury suit': 21, 'Gemini suit': 16, 'Apollo suit': 32, 'Space Shuttle suit': 50}
> 
> total_weight = 0
> # Use a For Loop to calculate the total weight of all space suits
> for weight in space_suit_weights.values():
>     total_weight += weight
> 
> print('Total suits weight:', total_weight)
> ```
> 
>   
> 
> This code correctly sums up the weights of all the suits in the `space_suit_weights` dictionary and prints the total weight.
> 
> 此代码正确求和space_suit_weights字典中所有套装的重量并打印总重量。

### 「practice」Charting the Orbits of Planets

Take a look at these planets and their orbits. Your next task is to `print` the **name** of each planet along with its **orbit period in Earth days**. Are you ready, Space Explorer?

```Python

# List of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# A dictionary of orbit periods (days) for planets
orbit_periods = {
    'Mercury': 88,
    'Venus': 225,
    'Earth': 365,
    'Mars': 687,
    'Jupiter': 4333,
    'Saturn': 10759,
    'Uranus': 30687,
    'Neptune': 60190,
}

# TODO: For each planet in the 'planets' list, print the name of the planet

# and its orbit period in Earth days, from the 'orbit_periods' dictionary.

```

```Python

Take a look at these planets and their orbits. Your next task is to print the name of each planet along with its orbit period in Earth days. Are you ready, Space Explorer?
_______

# List of planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# A dictionary of orbit periods (days) for planets
orbit_periods = {
    'Mercury': 88,
    'Venus': 225,
    'Earth': 365,
    'Mars': 687,
    'Jupiter': 4333,
    'Saturn': 10759,
    'Uranus': 30687,
    'Neptune': 60190,
}

# TODO: For each planet in the 'planets' list, print the name of the planet

# and its orbit period in Earth days, from the 'orbit_periods' dictionary.
_______

```

> It looks like there's a typo in the list of planets in your Python code snippet. The planet 'Uranus' is missing an opening quotation mark. Here's the corrected version:

```Python

> # List of planets
> planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
> 
> # A dictionary of orbit periods (days) for planets
> orbit_periods = {
>     'Mercury': 88,
>     'Venus': 225,
>     'Earth': 365,
>     'Mars': 687,
>     'Jupiter': 4333,
>     'Saturn': 10759,
>     'Uranus': 30687,
>     'Neptune': 60190,
> }
> 
> # For each planet in the 'planets' list, print the name of the planet and its orbit period in Earth days
> for planet in planets:
>     print(f"{planet}: {orbit_periods[planet]} days")

```

> 
> Now, the list of planets is correctly formatted, and this script should work without syntax errors.
>
output

```Python

> Mercury: 88 days
> Venus: 225 days
> Earth: 365 days
> Mars: 687 days
> Jupiter: 4333 days
> Saturn: 10759 days
> Uranus: 30687 days
> Neptune: 60190 days
> ```

```

```

# [Lesson 2: Navigating For Loops in Python: Deep Dive into Range and Enumerate](https://learn.codesignal.com/preview/lessons/149)

Blast off! We're about to explore the exciting world of `range()` and `enumerate()`, co-steering our for loop spaceship! 🚀 Let's navigate through this together and get started on this interstellar journey!

Introduction to Range and Enumerate in For Loops

Greetings, Explorer! In today's adventure, we're traversing the vast expanse of `range()` and `enumerate()`. These two functions will serve as your co-pilots, guiding your spaceship, the for loop, through the expansive universe of Python. We're set to delve into each function, uncovering hands-on examples and real-life applications.

你好，探险家！在今天的冒险中，我们将穿越range（）和enumerate（）的广阔领域。这两个函数将作为你的共同飞行员，引导你的飞船for循环穿越广阔的Python宇宙。我们将深入研究每个函数，揭示动手示例和实际应用。

Exploring the Range Function

Our first destination is the planet `range()`. This Python function generates a sequence of numbers, which are pivotal when directing a loop a specified number of times.

The `range()` function can accept three different sets of parameters:

- `range(stop)`: generates numbers from `0` to `stop - 1`.
    
- `range(start, stop)`: generates numbers from `start` to `stop - 1`.
    
- `range(start, stop, step)`: generates numbers from `start` to `stop - 1` in steps of `step`.
    

The `start` parameter specifies the starting point of the sequence, `stop` marks the endpoint (which isn't included in the sequence), and `step` is the increment amount for the sequence. By default, `start` is `0`, and `step` is `1`.

> **Title:** Iterations and Loops in Python
> 
> **Starred Blocks:**
> 
> * The `start` parameter specifies the starting point of the sequence.
> * The `stop` parameter marks the endpoint (which isn't included in the sequence).
> * The `step` parameter is the increment amount for the sequence.
> 
> **Default Values:**
> 
> * If `start` is not specified, it defaults to `0`.
> * If `step` is not specified, it defaults to `1`.

我们的第一个目标是行星range（）。这个Python函数生成一个数字序列，当引导一个循环指定次数时，这是关键的。

range（）函数可以接受三组不同的参数：

range（stop）：生成从0到stop-1的数字。

range（start， stop）：从开始到停止生成数字-1。

range（start， stop，step）：从开始到停止生成数字-步长为1。

start参数指定序列的起点，stop标记终点（不包含在序列中），step是序列的增量。默认情况下，start为0，step为1。

Range Function: Examples

Let's see it in action with a simple `for loop`.

```Python

for i in range(5):
    print(i)

```

```Python

0
1
2
3
4

```

The `range(5)` command generates numbers from `0` to `4`.

Now, let's experiment with a different value for `start` and a `step`:

```Python

for i in range(1, 10, 2):
    print(i)

```

Output:

```Python

1
3
5
7
9

```

As you can see, the above code starts at `1` and goes up to `9`, but it only prints every second number due to the `step` of `2`.

如您所见，上面的代码从1开始，一直到9，但由于2的步骤，它只打印每秒钟的数字。

## Enumerate: Indexing the Elements

Our next stop is galaxy `enumerate()`. This function serves as our real-time radar when voyaging through a list, as it provides both the index and value of each item. Here's how:

```Python

check_points = ['start', 'midpoint', 'end']

for index, check_point in enumerate(check_points):
    print('At index', index, 'we are at the', check_point, 'of the journey.')

```

Output:

```Python

At index 0 we are at the start of the journey.
At index 1 we are at the midpoint of the journey.
At index 2 we are at the end of the journey.

```

It gives both the index (index) and corresponding checkpoint (check_point) in the journey.

## Range Function: Use Case

Time to dock `range()` and `enumerate()` together on one spaceship! To illustrate their combined use, let's consider a group of space cadets and their corresponding IDs.

```Python

cadets = ["Neo", "Trinity", "Morpheus", "Agent Smith"]
ids = [101, 102, 103, 104]

for i in range(len(cadets)):
    print('Cadet', cadets[i], 'has id', ids[i])
for i, cadet in enumerate(cadets):
    print('Cadet', cadet, 'has id', i)

```

Here, `range(len(cadets))` creates indices for the list `cadets` from `0` to `len(cadets) - 1`, allowing us to access both `cadets` and `ids`.

## Conclusion: Mastery Check and Recap

Great work, Space Explorer! You've decoded the mysteries of `range()` and `enumerate()`, preparing yourself for a robust `for` loop journey through your Python universe. Solidify your skills with some practice tasks and build confidence in your newly acquired expertise. Happy coding!

干得好，太空探险家！你已经破译了range（）和enumerate（）的奥秘，为穿越Python宇宙的强大for循环之旅做好了准备。通过一些练习任务巩固你的技能，并对你新获得的专业知识建立信心。快乐编码！

### 「practice」Exploring Space with Enumerate and Range

Welcome back, Space Explorer!

Now that we've finished learning about the `enumerate()` and `range()` functions let's apply that knowledge to a practical scenario. We possess a list of _space objects_ that we intend to iterate over in two distinct ways: using the `enumerate()` and `range()` functions.

But don't worry, I've already made all the necessary arrangements for you. Your task is simply to click `Run` and observe.

```Python

space_objects = ['Sun', 'Earth', 'Moon', 'Mars', 'Jupiter']

# Enumerate the space_objects list and print each object with its index
for index, space_object in enumerate(space_objects):
    print('The object at index', index, 'is', space_object)

print()

# Use the range function to iterate over space_objects in reverse order

# Start from the last element, and make the negative step to get to the previous element
for i in range(len(space_objects) - 1, -1, -1):
    print('The object at index', i, 'is', space_objects[i])

```

Output

```python

The object at index 0 is Sun  
The object at index 1 is Earth  
The object at index 2 is Moon  
The object at index 3 is Mars  
The object at index 4 is Jupiter  
  
The object at index 4 is Jupiter  
The object at index 3 is Mars  
The object at index 2 is Moon  
The object at index 1 is Earth  
The object at index 0 is Sun

```

> You're diving into a hands-on exploration of Python's `enumerate()` and `range()` functions by applying them to iterate over a list of space objects like the Sun, Earth, Moon, Mars, and Jupiter. Your setup aims to demonstrate two approaches: the direct association of indices and objects using `enumerate()`, and the manual control of index order using `range()` for reverse iteration.
> 
> The code you've presented provides an excellent practical demonstration of these concepts:
> 
> 1. **Using `enumerate()`:** This part of your code uses the `enumerate()` function to loop through `space_objects`. It automatically provides each item with its corresponding index, enhancing readability and reducing the risk of off-by-one errors which are common in manual index handling.
> 
> 2. **Using `range()`:** This section leverages the `range()` function to iterate over the indices of `space_objects` in reverse order. It starts from the last element (index `len(space_objects) - 1`) and decrements the index until it reaches 0 (the step is `-1`). This method is particularly useful when you need to traverse a list backwards, but want to maintain access to the indices for operations like reordering or specific access patterns.
> 
> By running the provided code, you'll see a straightforward output showing the index and the associated space object for each position, first in natural order and then in reverse. This kind of iteration can be crucial for tasks that require specific order processing, such as reversing data, creating stacks, or simply when the logic depends on the position of the elements within a list.
> 你正在深入实践探索Python的enumerate()和range()函数，通过将它们应用于遍历太阳、地球、月亮、火星和木星等空间对象的列表。你的设置旨在展示两种方法：使用enumerate()直接关联索引和对象，以及使用range()手动控制索引顺序以进行反向迭代。
> > 你提供的代码为这些概念提供了一个很好的实践演示：
> > 1. 使用enumerate()：这部分代码使用enumerate()函数遍历space_objects。它自动为每个项目提供相应的索引，增强了可读性，并减少了手动索引处理中常见的偏移误差。
> > 2. 使用range()：这一节利用range()函数反向迭代space_objects的索引。它从最后一个元素（索引len(space_objects) - 1）开始，并递减索引直到达到0（步长是-1）。当你需要反向遍历列表，但希望保持对索引的访问以进行排序或特定访问模式的操作时，这种方法特别有用。
> > 通过运行提供的代码，你将看到一个简单的输出，显示每个位置的索引和相关联的空间对象，首先是自然顺序，然后是反向。这种迭代对于需要特定顺序处理的任务至关重要，例如反转数据、创建栈，或者简单地当逻辑依赖于列表中元素的位置时。
> 

Your solution is spot on! Stellar job applying your knowledge of `enumerate()` and `range()` functions. 

 **Starred Blocks:**

Starred blocks are used to unpack collections into individual variables. They can be used with the `enumerate()` and `range()` functions.

**`enumerate()` function:**

The `enumerate()` function takes an iterable (such as a list, tuple, or string) and returns an object that provides both the index and the value of each element. This can be useful for iterating over a collection and keeping track of the current index.

```python

my_list = [1, 2, 3, 4, 5]

for index, value in enumerate(my_list):
  print(f"Index: {index}, Value: {value}")

```

Output:

```

Index: 0, Value: 1
Index: 1, Value: 2
Index: 2, Value: 3
Index: 3, Value: 4
Index: 4, Value: 5

```

**`range()` function:**

The `range()` function generates a sequence of numbers within a specified range. It can be used to create a loop with a fixed number of iterations.

```python

for i in range(5):
  print(i)

```

Output:

```

0
1
2
3
4

```

You can also specify a starting and ending point for the range:

```python

for i in range(2, 7):
  print(i)

```

Output:

```

2
3
4
5
6

```

**Example using both `enumerate()` and `range()`:**

```python

my_list = ["apple", "banana", "cherry", "dog", "elephant"]

for index, value in enumerate(my_list):
  if index >= 2 and index < 4:
    print(f"Index: {index}, Value: {value}")

```

Output:

```

Index: 2, Value: cherry
Index: 3, Value: dog

```

Ready for the next challenge? 🚀
你的解决方案非常准确！在应用 enumerate() 和 range() 函数的知识方面做得很棒。准备好迎接下一个挑战了吗？🚀

### 「practice」Changing Civilizations to Cosmic Objects
Fantastic! Now, it's time for a minor adjustment. Instead of traversing the list using the `range` function, change the code to use `enumerate`, doing the same thing.
太棒了！现在，是时候进行一个小调整了。不要使用`range`函数遍历列表，而是将代码改为使用`enumerate`，做同样的事情。
You can do it! Let's go!
  

```python

cosmic_objects = ['Nebula', 'Black Hole', 'Galaxy']

  

# Use the enumerate function to iterate over cosmic_objects

for index in range(len(cosmic_objects)):

print("Object", index + 1, "in my list is", cosmic_objects[index])

```

Output

```python

Object 1 in my list is Nebula  
Object 2 in my list is Black Hole  
Object 3 in my list is Galaxy

```

> Good try, but it looks like there’s a mix-up. The task was to use the `enumerate` function to iterate over the list, but your code still uses `range`. Remember, with `enumerate`, you get both the index and the item itself in the loop. How about giving it another shot? Need a hint?

RaR-GPT

> It seems you are trying to refactor your code snippet to use the Python `enumerate` function for iterating over items in a list, while also accessing their indices. The `enumerate` function is very useful for this because it automatically provides a counter alongside the value from the iterable (like a list), which simplifies the loop and makes the code more Pythonic compared to using `range` and indexing. Here’s how you can correctly use the `enumerate` function for your list of cosmic objects:您似乎正在尝试重构代码片段以使用 Python `enumerate` 函数来迭代列表中的项目，同时还访问它们的索引。 `enumerate` 函数对此非常有用，因为它会自动在可迭代的值（如列表）旁边提供一个计数器，这简化了循环并使代码比使用 `range` 更Pythonic b2> 和索引。以下是如何正确使用 `enumerate` 函数来获取宇宙天体列表：

```python

cosmic_objects = ['Nebula', 'Black Hole', 'Galaxy']

# Using the enumerate function to iterate over cosmic_objects
for index, obj in enumerate(cosmic_objects, start=1):
    print("Object", index, "in my list is", obj)

```

> 
This version of the code uses `enumerate` directly on the list `cosmic_objects`. Notice that I added the `start=1` argument to `enumerate` so that indexing starts from 1 instead of the default 0. This aligns the displayed index numbers with the way you formatted your output in your original snippet, making it easier to read and understand in contexts where indexing traditionally starts from 1.此版本的代码直接在列表 `cosmic_objects` 上使用 `enumerate` 。请注意，我将 `start=1` 参数添加到 `enumerate` 中，以便索引从 1 而不是默认的 0 开始。这会将显示的索引号与您在原始代码段中格式化输出的方式对齐，使得在传统上索引从 1 开始的上下文中更容易阅读和理解。

### 「practice」Planetary Index Error Fix
Greetings, Space Voyager!

The names of planets are stored in our database. However, something seems amiss. When we attempt to list the names alongside their corresponding index, an error appears. Could you assist us in resolving this issue?
问候，太空航行者！
行星的名称存储在我们的数据库中。然而，似乎有些不对劲。当我们尝试列出名称及其对应的索引时，出现了一个错误。您能帮助我们解决这个问题吗？

```python

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

  

# Enumerate the planets list and print each planet with its index

for index, planet in range(planets):

print("The planet at index", index, "is", planet)

```

> It looks like you are trying to iterate over the list of planets and print each planet's name and index position. However, there's a small mistake in the loop statement which is causing an error.![[8D4474F3-F517-426B-A81D-6BB307C9D03F.jpeg]] You need to use the `enumerate` function to correctly loop through the list with both index and the corresponding value. Here’s how you can correct and enhance your code snippet to achieve this:
> 看起来你正尝试遍历行星列表并打印每个行星的名称以及它的索引位置。然而，循环语句中有一个小错误导致了一个错误。你需要使用 enumerate 函数来正确地遍历列表，同时获取索引和相应的值。以下是你可以如何修正并改进你的代码片段以达到这个目的：(kimi免费翻译)
> 
 ```python
> planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
> 
> # Enumerate the planets list and print each planet with its index
> for index, planet in enumerate(planets):
>     print("The planet at index", index, "is", planet)

```

> 
> In this corrected version, I've used the `enumerate` function, which is designed to return both the index and the value when iterating over a list. This will resolve the error and successfully output each planet with its corresponding index.
> 在这次修正的版本中，我使用了enumerate函数，它被设计为在迭代列表时返回索引和值。这将解决错误并成功输出每个行星及其对应的索引。(kimi免费翻译)

### 「practice」Contemplating the Constellations: Indexing and Iterating Star Names
Excellent work so far, Star Navigator!

Your next mission involves arranging our list of stars in two distinct ways, utilizing the functions we've learned. Be attentive! You must complete the sections marked with `TODOs`.

Iterate through the given list using `enumerate` in direct order and using `range` in reverse order.

Good luck, Cosmos Conqueror!

```python

stars = ["Sun", "Polaris", "Betelgeuse", "Sirius", "Vega"]

  

# TODO: Enumerate over the stars list and print each star with its index

for index, star in enumerate(___):

# Star indices should start with 1: 1, 2, 3, ...

print("Star", ___, "in my list is", ___)

  

# TODO: Use the range function to iterate over the stars list **in reverse order**

# and print each star with its index

for i in range(___, ___, ___):

# Star indices should start with 1: len(stars), len(stars) - 1, ..., 1

print("Star", ___, "in my list is", ___)

```

> Alright, let's break down your tasks into clear steps and then provide the Python code to achieve your goals.
> 
> ### Task 1: Enumerate the Stars List with Indices Starting from 1
> 
> You need to iterate over the list of stars, `stars = ["Sun", "Polaris", "Betelgeuse", "Sirius", "Vega"]`, and print each star with its index, where indexing should start from 1 instead of the default 0. Python's `enumerate()` function starts indexing from 0 by default, but you can adjust the starting index by providing a second argument.
> 
> Here's how you can accomplish this:
> 
 ```python
stars = ["Sun", "Polaris", "Betelgeuse", "Sirius", "Vega"]

# Enumerate over the stars list and print each star with its index starting from 1
for index, star in enumerate(stars, start=1):
    print("Star", index, "in my list is", star)

```

>
> 
> ### Task 2: Iterate Over the Stars List in Reverse Order Using Range
> 
> Now, you want to iterate over the same list in reverse order and also print each star with its index, which should be counted backwards from the length of the list. You can use the `range()` function for this, which allows you to specify the start, stop, and step. To iterate in reverse, you set the start at the last index (length of the list), stop before the index 0, and use a negative step.
> 
> Here's the code for this:

```python

# Use the range function to iterate over the stars list in reverse order

# and print each star with its index
 for i in range(len(stars), 0, -1):
     print("Star", i, "in my list is", stars[i-1])

```

> 
> Both of these tasks utilize Python's powerful enumeration and iteration capabilities to manage lists effectively. Each snippet accomplishes a specific arrangement and presentation of the data in your list of celestial names. Enjoy navigating through the cosmos with your Python skills!

```python

stars = ["Sun", "Polaris", "Betelgeuse", "Sirius", "Vega"]

# Enumerate over the stars list and print each star with its index starting from 1
for index, star in enumerate(stars, start=1):
    print("Star", index, "in my list is", star)

# Use the range function to iterate over the stars list in reverse order

# and print each star with its index
for i in range(len(stars), 0, -1):
    print("Star", i, "in my list is", stars[i-1])

```

##### output

```python

Star 1 in my list is Sun  
Star 2 in my list is Polaris  
Star 3 in my list is Betelgeuse  
Star 4 in my list is Sirius  
Star 5 in my list is Vega  
Star 5 in my list is Vega  
Star 4 in my list is Sirius  
Star 3 in my list is Betelgeuse  
Star 2 in my list is Polaris  
Star 1 in my list is Sun

```

### 「practice」Generating and Enumerating the First Letters of Planetary Names
Excellent work, Space Explorer! Now, let's construct a program to explore our planetary systems even more. Please write a program that generates a list of the initial letters from all the planet names and then utilizes the `enumerate` function to display each letter accompanied by its index number on the console.

```python

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

first_letters = []

  

# TODO: Write a for loop with a range to iterate through each planet in the planets list.

# Inside the loop, add the first letter of each planet to the first_letters list.

  

# TODO: Write a for loop using enumerate to print out each first letter and its corresponding planet index.

```

>   It seems like you're interested in developing a program that not only lists the initial letters of planet names but also uses Python's enumerate function to pair these letters with their indices for better visualization and understanding. This approach allows for an engaging way to explore planetary names in a programming context.
> 
> Here’s a Python program that will achieve your objectives. The program starts by extracting the first letter from each planet's name and storing these in a list. Then, it utilizes the `enumerate` function to iterate through this list, printing both the index and the letter, thus providing a clear, indexed list of the first letters of the planetary names.

```python

# List of planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Initialize an empty list to store the first letters
first_letters = []

# Iterate through each planet in the planets list
for planet in planets:
    # Add the first letter of each planet to the first_letters list
    first_letters.append(planet[0])

# Use enumerate in a for loop to print out each first letter with its corresponding index
for index, letter in enumerate(first_letters):
    print(f"{index}: {letter}")

```

```python

0: M  
1: V  
2: E  
3: M  
4: J  
5: S  
6: U  
7: N

```

> In this code:
> - We iterate over each planet in the `planets` list and extract the first character using indexing (`planet[0]`).
> - These characters are then added to the `first_letters` list.
> - The `enumerate` function is used to loop over `first_letters`, providing both the index and the value (letter). Each pair is printed in a formatted string that shows the index followed by the corresponding letter.
> 
> This will output the index and the first letter of each planet, facilitating a straightforward way to reference them by their position in the list.
>

# [Lesson 3: Embarking on the While Loop Journey: Steering Through Python's Control Flow Mechanics](https://learn.codesignal.com/preview/lessons/150)

### 「practice」Exploration of Earth Using a While Loop
Alright, we're about to unlock the mystery of While Loops in Python! Such an important mission ahead. Let's crush it together! 💪

## Topic Overview and Actualization

Let's buckle up for our journey into the fascinating world of **While Loops**. Visualize piloting a spaceship on an uncharted route, making a pit stop at every interesting planet until you find the one that harbors intelligent life. This adventure encapsulates what While Loops do: they continue running tasks until a specific condition changes. In this lesson, we aim to master the usage of While Loops, understand the concept of '_indefinite iteration_', and control the loop's execution effectively.

## While Loop Discovery

A `while` loop allows the code to execute repeatedly based on a specific condition. If the condition remains `True`, it continues to run, similar to an `if` statement. Let's look at a while loop that counts from 1 to 5:

```python

count = 1
while count <= 5:
    print(count) # Will print numbers from 1 to 5, inclusive
    count += 1

```

The output of the code is:

```markdown

1
2
3
4
5

```

Here's the basic structure of a `while` loop:

```python

while condition:
    # code to be executed

```

In our example, `count <= 5` is the condition, and `print(count); count += 1` is the code to be executed. As long as the condition `count <= 5` holds `True`, the loop repeats and eventually prints numbers from 1 to 5, inclusive.

## Journey through the While Loop Galaxy

Let's delve into the intricacies of While Loops:

1. Firstly, Python checks if the `while` loop's condition is `True`.
2. If the condition is `True`, it executes the loop's code.
3. Then, it cycles back to the first step.

This continues until the condition becomes `False`.

## Steering the While Loop Spaceship - Control Flow

While writing a `while` loop, make sure the loop's condition eventually turns `False` to avoid infinite loops. An infinite loop could potentially crash your system. Here's an example:

```python

# INFINITE LOOP EXAMPLE - DO NOT RUN!
count = 1
while count <= 5: 
    print(count) # Always prints 1
    # Forgetting to increment count results in an infinite loop.

```

To prevent such a catastrophe, we often use the `break` statement. The `break` statement provides an escape hatch, immediately terminating the loop it's in. We will cover the `break` operator more extensively later in this course.

## The Universe of Indefinite Iteration

`while` loops offer indefinite iteration, repeating an unknown number of times until a specific goal is achieved. This real-life example demonstrates it:

```python

score = 0
while score < 10:
    score += 2
    print("Current score: ", score)
    if score == 10:
        print("You won the game!")

```

```markdown

Current score: 2
Current score: 4
Current score: 6
Current score: 8
Current score: 10
You won the game!

```

In this game, your score starts at 0. Every loop iteration increments your score by 2, until you reach a score of 10, at which point you win the game!

Note that if we check for score == 9, this loop will never print the "You won the game!" string.

## Lesson Summary

Excellent work! You have just experienced the magic of While Loops! Be observant when crafting While Loops to avoid the dreaded infinite loops.

Now is the time to put your skills to use in the hands-on exercises. You'll be crafting your `while` loops, integrating the lessons we've learned together. Remember, practice is key to refining your skills! So, wield your _coding wand_ and take on the exercise. If you get stuck, don't hesitate to ask for help. Happy coding!

### 「practice」Adjusting Cruise Distance While Approaching Saturn
Alright, Space Wanderer! Let's get started on our _While Loop_ space mission! We're staying around Earth, exploring it year by year until we reach 2030.

Observe how Python repeats the `print` statement as it thoroughly explores the `while` loop — the starship of our course!

```python

# Space Exploration

planet = "Earth"

year = 2022

while year < 2030:

print("Exploring the planet", planet, "in the year", year)

year += 1

```

output

```markdown

  

Exploring the planet Earth in the year 2022  
Exploring the planet Earth in the year 2023  
Exploring the planet Earth in the year 2024  
Exploring the planet Earth in the year 2025  
Exploring the planet Earth in the year 2026  
Exploring the planet Earth in the year 2027  
Exploring the planet Earth in the year 2028  
Exploring the planet Earth in the year 2029

```

Great job on navigating those while loops! You've successfully completed the exploration mission. 🚀 Ready for the next adventure?

### 「practice」Programming the Mars Landing

Fantastic job, Space Voyager! Let's shake things up a bit. Why don't we alter the code to stop the ship when it's 500 million km away from Saturn? Let's put this to the test!

```python

planet = "Saturn"

distance_from_saturn = 1433.5 # in millions of kilometers

while ___:

print("Navigating towards", planet, "which is", distance_from_saturn, "million km away")

distance_from_saturn -= 100.0

print("Hello:", planet)

```

It sounds like you're aiming to modify a loop within a script that controls a space voyage simulation, specifically to halt the ship when it is exactly 500 million kilometers away from Saturn. The task involves altering the loop condition so that the loop ceases once the ship's distance to Saturn reaches or falls below this threshold.

Here’s how you can adjust your loop to meet this new requirement:

```python

planet = "Saturn"
distance_from_saturn = 1433.5  # in millions of kilometers

# The loop should continue as long as the distance is greater than 500 million km
while distance_from_saturn > 500.0:
    print("Navigating towards", planet, "which is", distance_from_saturn, "million km away")
    distance_from_saturn -= 100.0  # reduce the distance by 100 million km each iteration

print("Hello:", planet)  # This line executes once the ship is 500 million km away or less

```

With this alteration, the `while` loop will repeatedly execute, decrementing the distance by 100 million kilometers each time, until `distance_from_saturn` exceeds 500 million kilometers. Once it's equal to or less than 500, the loop terminates, and the program prints a greeting indicating arrival in proximity to Saturn. This effectively simulates stopping the ship at the designated distance from the planet.

### 「practice」Adding Print Statement to Track Orbits

Oh dear, _Star Voyager_! There's a minor hiccup in our Mars mission code. It appears our spaceship perpetually voyages to Mars without ever landing. We entrust you to find and rectify this bug! Good luck!

```python

# Space Exploration

planet = "Mars"

distance = 0

landed = False

  

while not landed:

print("Currently traveling to", planet, "and covered", distance, "million km")

distance += 10

if distance == 85:

print("Landed on", planet, "after covering", distance, "million km!")

landed = True

```

It seems like the primary issue you're encountering is that the spaceship continues to travel towards Mars but never executes the landing sequence properly. From your description, it sounds as if the spaceship's loop is designed to run until it has successfully landed, which is controlled by the `landed` variable. However, despite reaching the correct distance, the loop might not be terminating correctly.

Let's examine the logic you've shared. You have a loop that increments the `distance` by 10 million km each cycle and checks if the `distance` equals 85 million km to determine if the spaceship should land. This logic appears sound for landing exactly when the distance is 85 million km. If there are no other conditions affecting the `landed` variable or other interruptions in your broader codebase affecting this segment, this specific portion should function as intended.

However, if the spaceship is "perpetually voyaging" despite this logic, there are a few potential issues to consider:
1. **Infinite Loop**: If the loop continues beyond the specified landing condition, it could be due to the loop condition not updating as expected. Make sure `landed` is correctly set to `True`.
2. **Condition Miss**: If the increment leads the `distance` to skip over exactly 85 (like if distance changes due to other conditions elsewhere in the code), the condition to land won't be met. This doesn't seem to be the case here since you're incrementing by 10, but it's a common issue in similar scenarios.
3. **External Modifications**: Ensure no external modifications to `distance` or `landed` from other parts of the program that might affect the execution flow here.

Based on the provided code snippet, the program should correctly report landing when the distance reaches exactly 85 million km. If the problem persists, I would recommend checking for any external interferences or modifications to the `distance` or `landed` variables outside the shown code block. If the issue is solely within the provided code, then it should function as expected under normal circumstances.

Thank you for your patience! It seems like I need to look closer at the loop's termination condition based on the hint you provided. Currently, the loop increments the distance by 10 million km each iteration, and the landing is supposed to occur when the distance is exactly 85 million km. However, if there is any inconsistency or missed increment that causes the distance to overshoot 85 million km without hitting it exactly, the landing would indeed not trigger, causing the spaceship to continue indefinitely.

One way to solve this problem would be to adjust the landing condition from an equality check (`==`) to a greater than or equal to check (`>=`). This change ensures that even if the distance overshoots 85 million km due to modifications elsewhere or potential rounding errors, the spaceship will still land. Here’s how you could adjust the code:

```python

planet = "Mars"
distance = 0
landed = False

while not landed:
    print("Currently traveling to", planet, "and covered", distance, "million km")
    distance += 10
    if distance >= 85:  # Changed from '==' to '>='
        print("Landed on", planet, "after covering", distance, "million km!")
        landed = True

```

This adjustment will ensure that the spaceship lands once it reaches or exceeds 85 million km, preventing it from continuing indefinitely if it somehow misses the exact 85 million km mark. This might be particularly important in a more complex program where `distance` could be influenced by other functions or conditions in ways that might cause unexpected behavior.

```

Currently traveling to Mars and covered 0 million km  
Currently traveling to Mars and covered 10 million km  
Currently traveling to Mars and covered 20 million km  
Currently traveling to Mars and covered 30 million km  
Currently traveling to Mars and covered 40 million km  
Currently traveling to Mars and covered 50 million km  
Currently traveling to Mars and covered 60 million km  
Currently traveling to Mars and covered 70 million km  
Currently traveling to Mars and covered 80 million km  
Landed on Mars after covering 90 million km!

```

### 「practice」Reverse Engineering the Voyage to Venus
You've done a stellar job so far, Space Explorer! Let's continue our exploration of the universe. This time, you'll need to write some code on your own. Complete the `TODO` comment in the code to maintain the orbit of the Earth!

```python

planet = "Earth"

orbit_cycles = 0

  

# TODO: keep looping while orbit cycles is less than 10

while ___:

# TODO: add a print statement to indicate the number of orbits completed by the planet

orbit_cycles += 1

```

You're gearing up to track the Earth's orbit through a loop in Python, and you need to complete the loop and print statements. Here’s a clear way to complete the provided code:

1. **Condition for the While Loop**: The loop should continue as long as `orbit_cycles` is less than 10.
2. **Print Statement**: Every iteration (orbit) should print out the current number of orbits completed by Earth.

Here's the completed code:

```python

planet = "Earth"
orbit_cycles = 0

# Keep looping while orbit cycles is less than 10
while orbit_cycles < 10:
    # Print the number of orbits completed by the planet
    print(f"{planet} has completed {orbit_cycles + 1} orbits.")
    orbit_cycles += 1

```

This script initializes the number of orbits at 0 and uses a `while` loop to increment this number until it reaches 10. Each time through the loop, it prints a message stating how many orbits Earth has completed. The output is updated each loop, so it accurately reflects the new number of completed orbits.

##### output

```python

Earthhas completed 1 orbits.  
Earthhas completed 2 orbits.  
Earthhas completed 3 orbits.  
Earthhas completed 4 orbits.  
Earthhas completed 5 orbits.  
Earthhas completed 6 orbits.  
Earthhas completed 7 orbits.  
Earthhas completed 8 orbits.  
Earthhas completed 9 orbits.  
Earthhas completed 10 orbits.

```

Time to wrap up our exploration journey, Pilot! Let's reverse-engineer the journey from Venus to Earth. Please modify the given starter code to have the spacecraft start from Venus and move closer to the Earth by a million km increment until it reaches Earth.

Use TODO comments as a reference. Let's go!

```python

planet = "Venus"

distance = 10 # distance, in millions of km

  

# TODO: Write a while loop that:

# Prints the current distance to Earth

# Decreases the distance between the Earth and the spacecraft by 1 million km until it reaches Earth.

```

Here is your modified code, reflecting a journey from Venus to Earth with the spacecraft reducing its distance by 1 million km on each loop iteration until it reaches Earth:

```python

planet = "Venus"
distance = 10  # distance, in millions of km

# TODO: Write a while loop that:

# Prints the current distance to Earth

# Decreases the distance between the Earth and the spacecraft by 1 million km until it reaches Earth
while distance > 0:
    print(f"Current distance from {planet} to Earth: {distance} million km")
    distance -= 1  # Decrease the distance by 1 million km each iteration
print("The spacecraft has reached Earth!")

```

This script will output the distance from Venus to Earth in each iteration of the loop, decreasing the distance by 1 million kilometers each time, and it will stop when the spacecraft has reached Earth.

##### output

```python

Current distance from Venus to Earth: 10 million km  
Current distance from Venus to Earth: 9 million km  
Current distance from Venus to Earth: 8 million km  
Current distance from Venus to Earth: 7 million km  
Current distance from Venus to Earth: 6 million km  
Current distance from Venus to Earth: 5 million km  
Current distance from Venus to Earth: 4 million km  
Current distance from Venus to Earth: 3 million km  
Current distance from Venus to Earth: 2 million km  
Current distance from Venus to Earth: 1 million km  
The spacecraft has reached Earth!

```

# [Lesson 4: Interstellar Strolls Through Python: Loop and Conditional Symbiosis](https://learn.codesignal.com/preview/lessons/151)

## Lesson Introduction: Combining Loops with Conditionals - The Power Duo

Greetings, student! Today, we're fusing Python **loops** and **conditionals** together. Conditionals empower our code to make decisions, while loops enable the execution of repetitive tasks. Let's master this synergy!

## The Basics of Conditions in Loops

Loops, such as `for` and `while`, repeat specific tasks, and conditionals — `if`, `elif`, and `else` — guide the path of the code. Combining these constructs equips us with a virtual super robot that performs repeated tasks with decision-making abilities.

Let's consider sending personalized party invitations. In this context, loops go through each guest, and conditionals decide the style of the invitation:

```python

# Invite guests using a loop with a conditional

# Each guest has a name and invitation type - VIP or Regular
guests = [('Alice', 'VIP'), ('Bob', 'VIP'), ('Tom', 'Regular'), ('Jerry', 'Regular')]

for guest in guests:
    if guest[1] == 'VIP':
        print("Dear", guest[0], ", join us for a grand celebration!")
    elif guest[1] == 'Regular':
        print("Hi", guest[0], ", you are invited!")

```

This code prints:

```python

Dear Alice , join us for a grand celebration!
Dear Bob , join us for a grand celebration!
Hi Tom , you are invited!
Hi Jerry , you are invited!

```

## Working with Conditionals in For Loops

Python’s For Loop iterates over a defined sequence of elements. When we pair a conditional with the loop, the execution adjusts with each iteration based on the condition.

For instance, consider hosting a party. We have a `guest_list` and an `unwanted_list`. By pairing a For Loop with a conditional, we can ensure that only welcomed guests gain admission:

```python

# For Loop with a conditional
guest_list = ['Alice', 'Bob', 'Tom', 'Jerry', 'Snow']
unwanted_guests = ['Tom', 'Snow']

for guest in guest_list:
    if guest not in unwanted_guests:
        print("Welcome,", guest, "!")
    else:
        print("Sorry,", guest, ", the party is full.")

```

The code prints:

```python

Welcome, Alice !
Welcome, Bob !
Sorry, Tom , the party is full.
Welcome, Jerry !
Sorry, Snow , the party is full.

```

## Implementing Conditionals in While Loops

A While Loop continues as long as its condition remains valid. Inserting a conditional within it can alter or halt its iterations based on changing conditions.

Suppose that when an unwanted guest arrives, the doorman closes the gate:

```python

# While Loop with a conditional
guest_list = ['Alice', 'Bob', 'Tom', 'Jerry', 'Snow']
unwanted_guests = ['Tom', 'Snow']
guest_index = 0

while guest_index < len(guest_list):
    if guest_list[guest_index] not in unwanted_guests:
        print("Please come in,", guest_list[guest_index], "!")
    else:
        print("Party Over:", guest_list[guest_index], "showed up!")
        break # This will stop the while loop completely
    guest_index += 1

```

### The code prints:

```python

Please come in, Alice !
Please come in, Bob !
Party Over: Tom showed up!

```

It looks like you've shared a Python code snippet using a while loop to manage a list of guests at a party, including a condition to check for unwanted guests. The code iterates over the guest list, inviting each one unless they are found in the unwanted guests list. When an unwanted guest is encountered, the loop terminates with a specific message indicating the party is over because of that guest's arrival.

To clarify and expand upon the explanation: In your script, `guest_list` contains names of all invited people, while `unwanted_guests` lists those whose arrival would end the party. You initialize `guest_index` to 0 to start checking from the first guest in the list. The while loop continues as long as `guest_index` is less than the number of guests. Inside the loop, there's a condition to check if the current guest (`guest_list[guest_index]`) is not in the `unwanted_guests` list. If true, a welcoming message is printed. If false, a message indicating the end of the party due to the unwanted guest is printed, and the loop is immediately stopped with `break`. The `guest_index` is incremented at the end of each loop iteration to move to the next guest.

This mechanism ensures that as long as no unwanted guests show up, everyone on the list is welcomed sequentially. The party continues until an unwanted guest arrives, at which point the script stops checking further guests. If you have any questions about modifying or understanding this script further, feel free to ask!

## Understanding Different Scenarios

The combination of loops and conditionals provides immense versatility. For instance, consider these scenarios:

1. Picking out even numbers from a list.
2. Find all duplicates in the list of numbers.

Here's how we can address these scenarios:

```python

# Filter out even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num % 2 != 0:  # if the number is not divisible by 2
        print(num)
"""
Prints:
1
3
5
7
9
"""

# Find all duplicates in the list of numbers
num_list = [1, 3, 5, 3, 7, 2, 1]
unique_list = []
for num in num_list:
    if num not in unique_list:
        unique_list.append(num)
    else:
        print("Duplicate number found:", num)
"""
Prints:
Duplicate number found: 3
Duplicate number found: 1
"""

```

output

```python

1  
3  
5  
7  
9  
Duplicate number found: 3  
Duplicate number found: 1

```

## Lesson Summary: The Power Duo in Action

Fantastic! You've learned to combine Python's **loops** and **conditionals**. We've covered `for` and `while` loops coupled with conditionals and showcased Python examples, using our combination to solve various scenarios.

Now, it's time to exercise this new skill through practice. Just as a dancer perfects a dance routine by repeating each step, mastering these concepts requires ample practice. Let's continue our journey to Python mastery!

### 「practice」Welcome the Party Guests
Welcome to our space party planner, Space Explorer! The guest list is quite extensive, but the party room, unlike the TARDIS, has limited _space_ and _time_. Consequently, I designed a code that utilizes _loops_ and _conditionals_, and invites VIP and Regular guests until the `time_left` becomes `0`, while avoiding Unwanted guests.

Please press `Run` to see how it operates.

```python

# You are hosting a party, and you have guests in line.

# You will invite-only VIPs and Regular guests until the time is up!

# Your goal is to greet as many people as you can, or else the party might be too quiet.

  

guests = [('Alice', 'VIP'), ('Bob', 'VIP'), ('Charlie', 'Regular'), ('Daisy', 'Unwanted'), ('Eve', 'VIP'), ('Frank', 'Regular'), ('Marcelo', 'VIP')]

time_left = 5

  

for guest in guests:

if time_left == 0:

break

if guest[1] != 'Unwanted':

print("Welcome,", guest[0], "!")

time_left -= 1

else:

print("Sorry,", guest[0], ", we cannot invite you this time!")

```

以上运行🙅❌
guest[1] ,guest[0]，# You are hosting a party, and you have guests in line.

You will invite-only VIPs and Regular guests until the time is up!

Your goal is to greet as many people as you can, or else the party might be too quiet.

自动生成

 ```python
def party(guests):
    """
    Invites VIPs and Regular guests to a party until the time is up.

    Args:
        guests (list): A list of guests, where each guest is a tuple
            containing the guest's name (string) and type (string, either
            "VIP" or "Regular").

    Returns:
        int: The number of guests invited to the party.
    """

    # Initialize the number of guests invited to 0.
    num_invited = 0

    # Iterate over the list of guests.
    for guest_name, guest_type in guests:

        # Check if the guest is a VIP.
        if guest_type == "VIP":

            # Invite the VIP to the party.
            print(f"Inviting {guest_name} (VIP) to the party.")
            num_invited += 1

        # Check if the guest is a Regular guest.
        elif guest_type == "Regular":

            # Check if there is still time left to invite Regular guests.
            if num_invited < 5:

                # Invite the Regular guest to the party.
                print(f"Inviting {guest_name} (Regular) to the party.")
                num_invited += 1

            # If there is no more time left, break out of the loop.
            else:
                break

    # Return the number of guests invited to the party.
    return num_invited

# Test the party function.
guests = [
    ("John", "VIP"),
    ("Mary", "Regular"),
    ("Bob", "VIP"),
    ("Alice", "Regular"),
    ("Tom", "Regular"),
    ("Susan", "VIP"),
    ("David", "Regular"),
]
num_invited = party(guests)
print(f"{num_invited} guests were invited to the party.")

```

RAR- GPT4
You're focusing on ensuring that your guest invitation process at your party doesn't exceed the allotted time, specifically by managing the decrementing of the `time_left` variable correctly. The challenge here is that you might invite one extra guest because the decrement of `time_left` happens after a guest is already welcomed, and the check for whether `time_left` has reached zero isn't optimally placed to preemptively prevent this.

To address this, you need to adjust the placement and condition of the `time_left` check. This involves making sure you have enough time left before you invite each guest. Here's a refactored version of your loop to ensure `time_left` is checked properly before welcoming any guest, and the loop exits correctly when no more time is left:

python

Copy code

```python

guests = [('Alice', 'VIP'), ('Bob', 'VIP'), ('Charlie', 'Regular'), ('Daisy', 'Unwanted'), ('Eve', 'VIP'), ('Frank', 'Regular'), ('Marcelo', 'VIP')]
time_left = 5

for guest in guests:
    # Check if we should skip inviting unwanted guests.
    if guest[1] == 'Unwanted':
        print("Sorry,", guest[0], ", we cannot invite you this time!")
        continue  # Skip the rest of the loop for unwanted guests.

    # Pre-check time_left before inviting to ensure we do not exceed the limit.
    if time_left > 0:
        print("Welcome,", guest[0], "!")
        time_left -= 1  # Decrement time only after ensuring the guest can be welcomed.
    else:
        break  # Stop inviting once we run out of time.

print("Time left after all invitations:", time_left)```
output

```python

Welcome, Alice !  
Welcome, Bob !  
Welcome, Charlie !  
Sorry, Daisy , we cannot invite you this time!  
Welcome, Eve !  
Welcome, Frank !

```

### 「practice」Adjusting Invitations for VIP Guests Only
Great job, Cosmic Voyager!

Now, let's fine-tune our party invitation system a bit more.

Alter the code to ensure that a guest receives an invitation only if they are classified as a `'VIP'`. Non-VIP guests should receive a decline message, specifying their name and that they can't enter the party.

You've got the drill!

```python

guests = [('Obi-Wan', 'VIP'), ('Anakin', 'Regular'), ('Yoda', 'VIP'), ('Jar Jar', 'Unwanted'), ('Leia', 'Regular'), ('Han', 'VIP')]

for guest in guests:

print("Welcome, Master", guest[0], ", we've been expecting you!")

```

自动生成

```python

guests = [('Obi-Wan', 'VIP'), ('Anakin', 'Regular'), ('Yoda', 'VIP'), ('Jar Jar', 'Unwanted'), ('Leia', 'Regular'), ('Han', 'VIP')]

for guest in guests:
  if guest[1] == 'VIP':
    print("Welcome, Master", guest[0], ", we've been expecting you!")
  else:
    print("Sorry", guest[0], "you're not on the VIP list and cannot enter the party")

```

output

```python

Welcome, Master Obi-Wan , we've been expecting you!  
Sorry Anakin you're not on the VIP list and cannot enter the party  
Welcome, Master Yoda , we've been expecting you!  
Sorry Jar Jar you're not on the VIP list and cannot enter the party  
Sorry Leia you're not on the VIP list and cannot enter the party  
Welcome, Master Han , we've been expecting you!

```

### 「practice」Cosmic Party Guest Greetings Issue
Hold your horses, Space Explorer! Something has gone haywire in our greeting system at the Cosmic party. The current code was intended to generate a different _greeting_ based on the length of the guest's _name_, but that just isn't happening.

Can you help us fix the greeting machine's logic? We need it to provide longer, more formal greetings to guests with names longer than `4` letters and shorter, more casual greetings to guests with names that are `4` letters or shorter.

```python

guests = ['Alice', 'Bob', 'Charlie', 'Daisy', 'Eve', 'Frank']

for guest in guests:

if guest > 4:

print("Welcome to the party,", guest, "!")

elif guest <= 4:

print("Hey", guest, ", welcome!")

```

自动生成

```python

guests = ['Alice', 'Bob', 'Charlie', 'Daisy', 'Eve', 'Frank']

for guest in guests:

if len(guest) > 4:

print("Welcome to the party,", guest, "!")

elif len(guest) <= 4:

print("Hey", guest, ", welcome!")

```

output

```python

Welcome to the party, Alice !  
Hey Bob , welcome!  
Welcome to the party, Charlie !  
Welcome to the party, Daisy !  
Hey Eve , welcome!  
Welcome to the party, Frank !

```

### 「practice」Write Conditions for Party Guest Entry
Great job, Voyager! It's time to kick things up a notch. I aim to send different messages to my party guests based on the number of star fruits they contribute. Could you assist me in completing the code to make this possible?

TODO comments can guide you through!

```python

# Let's allow only those party guests who bring at least 10 fruits.

guests = [('Alice', 15), ('Bob', 5), ('Charlie', 8), ('Daisy', 20), ('Eve', 0), ('Frank', 18)]

  

for guest in guests:

# TODO: add an if-else condition to control guest entry based on the number of star fruits they bring.

# If they brought less than 10 fruits, they are not allowed in.

```

自动生成

```python

guests = [('Alice', 15), ('Bob', 5), ('Charlie', 8), ('Daisy', 20), ('Eve', 0), ('Frank', 18)]

  
for guest in guests:

    # TODO: add an if-else condition to control guest entry based on the number of star fruits they bring.

    if guest[1] < 10:
        print(f"{guest[0]} cannot enter the party.")
    else:
        print(f"{guest[0]} is allowed in.")

```

output

```

Alice is allowed in.  
Bob cannot enter the party.  
Charlie cannot enter the party.  
Daisy is allowed in.  
Eve cannot enter the party.  
Frank is allowed in.

```

### 「practice」Preparing Personalized Messages for Space Party Guests
Great job, Cosmic Explorer! There's just one final task before we move on. How about trying to write the logic for the party guest list from scratch?

We should utilize the for loop and conditionals to send individualized messages to the guests based on their `RSVP` status.

```python

# You are hosting a party, and you have a list of guests.

# Some guests confirmed their attendance with "Yes", some didn't reply with "No Reply", and some declined your invite with "No".

# As part of the preparation, let's go through the list of guests and check who's coming for the party!

  

guest_list = [('Alice', 'Yes'), ('Bob', 'No Reply'), ('Charlie', 'No'), ('Daisy', 'Yes'), ('Eve', 'No Reply'), ('Frank', 'No')]

  

# TODO: Loop through the guest list

# TODO: If the guest confirmed their attendance, print a welcome message.

# TODO: If the guest didn't reply, print a message of uncertain attendance.

# TODO: If the guest declined the invite, print a message of unavailability.

```

```python

# You are hosting a party, and you have a list of guests.

# Some guests confirmed their attendance with "Yes", some didn't reply with "No Reply", and some declined your invite with "No".

# As part of the preparation, let's go through the list of guests and check who's coming for the party!

  

guest_list = [('Alice', 'Yes'), ('Bob', 'No Reply'), ('![[404.html]]

Charlie', 'No'), ('Daisy', 'Yes'), ('Eve', 'No Reply'), ('Frank', 'No')]

  

for guest in guest_list:
  name, rsvp = guest[0], guest[1]

  if rsvp == 'Yes':
    print(f"{name} is coming to the party!")
  elif rsvp == 'No Reply':
    print(f"{name} hasn't replied yet.")
  else:
    print(f"{name} is not coming to the party.")

```

# [Lesson 5: Unmasking Nested Loops: Navigating Advanced Looping Structures in Python](https://learn.codesignal.com/preview/lessons/152)

## Introduction and Overview

Welcome, Python astronauts, to the intergalactic tour of **nested loops in Python**! Just like spaceships in formation, nested loops tackle layered problems. Our mission today is to understand the syntax and applications of nested loops, all of which will be enriched with a practical example.

##### Starry Dive into Nested Loops

**Nested loops** are simply loops within loops. They function much like stars and planets in the cosmos. Each celestial body (an outer loop `star`) has smaller bodies (inner loop `planets`) revolving around it. Similarly, for each iteration of an outer loop, an inner loop executes completely.

##### Syntax and Structure of Nested Loops in Python

Nested loops follow a hierarchical structure. For each iteration of an outer loop, an inner loop executes fully:

```python

for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # Inner loop statements

```

Here's an example of a nested loop using Python's `range()` function. In this example, `i` represents different types of spaceships, and `j` represents various spaceship features:

```python

for i in range(1, 4):  # Outer loop
    print('Start', i)
    for j in range(1, 4):  # Inner loop
        print(i, j)  # Prints spaceship type `i` and its attribute `j`
    print('End', i)

```

The code prints:

```python

Start 1
1 1
1 2
1 3
End 1
Start 2
2 1
2 2
2 3
End 2
Start 3
3 1
3 2
3 3
End 3

```

##### Traversing the Cosmos with the While Loop in Python

Nested `while` loops also use an outer-inner structure:

```python

while outer_condition:  # Outer loop condition
    while inner_condition:  # Inner loop condition
        # Inner loop statements

```

Here's an example with nested `while` loops:

```python

i = 1  # Outer loop variable, representing spaceship types
while i <= 3: 
    print('Start', i)  # Start of each spaceship type iteration
    j = 1  # Inner loop variable, signifying spaceship features
    while j <= 3:  # Inner loop runs three iterations for each spaceship type
        print(i, j)  # Prints spaceship type `i` and its feature `j`
        j += 1  # Increase `j` by 1
    print('End', i)  # End of each spaceship type iteration
    i += 1  

```

The code prints:

```python

Start 1
1 1
1 2
1 3
End 1
Start 2
2 1
2 2
2 3
End 2
Start 3
3 1
3 2
3 3
End 3

```

##### Deeper Dive: Complex Nested Loop Scenarios

Nested loops are not necessarily limited by just two-level nesting. In fact, there can be any number of nested loops. Here is a simple example with three nested loops:

```python

##### Deeper Dive: Complex Nested Loop Scenarios

Nested loops are not necessarily limited by just two-level nesting. In fact, there can be any number of nested loops. Here is a simple example with three nested loops:

```

While analyzing three-dimensional data can be more informative, it's crucial to ensure the computational effort doesn't exceed the capacity of your hardware. But don't worry if that doesn't make too much sense right now, you'll learn more about it in the next courses!

##### Lesson Summary

Congratulations, astronaut! You've successfully journeyed through nested loops. We've navigated the landscape of nested loops, their syntax, and practical, celestial-themed examples. Up next are some practice exercises! Buckle up for a thrilling ride through the nested loops cosmos!

### 「practice」Spaceships and Planets: Traversing with Nested Loops
Guess what, Space Voyager? We have an array of spaceships heading towards various planetary systems! We will employ the power of **nested loops** in Python to determine which spaceship is directed to which planetary system.

Everything is programmed; you just need to press the `Run` key to obtain the details!

```python

planet_systems = ['Mercury', 'Earth', 'Mars']

  

spaceships = ['Voyager', 'Discovery', 'Challenger']

  

for planet in planet_systems:

for spaceship in spaceships:

print("Spaceship", spaceship, "is heading to the", planet, "system.")

```

```

Spaceship Voyager is heading to the Mercury system.  
Spaceship Discovery is heading to the Mercury system.  
Spaceship Challenger is heading to the Mercury system.  
Spaceship Voyager is heading to the Earth system.  
Spaceship Discovery is heading to the Earth system.  
Spaceship Challenger is heading to the Earth system.  
Spaceship Voyager is heading to the Mars system.  
Spaceship Discovery is heading to the Mars system.  
Spaceship Challenger is heading to the Mars system.

```

### 「practice」Navigating Through Nested Loops in the Cosmo System
Well done, Space Explorer! Our interstellar neighborhood, _Cosmo_, is home to three planets. Each planet, in turn, has five orbits. In the provided code, you will journey through each orbit of every planet in _Cosmo_. Once you press the `Run` button, the details of your excursion will be displayed. Embark on this exploration through nested loops now!

```python

# Cosmo has 3 planets, each planet has 5 orbits. Let's explore them with nested loops:

  

cosmo_id = 1

planet_limit = 4

orbit_limit = 6

  

while cosmo_id < planet_limit:

print('Cosmo', cosmo_id)

orbit_id = 1

while orbit_id < orbit_limit:

print('Orbit:', orbit_id, 'of Cosmo:', cosmo_id)

orbit_id += 1

cosmo_id += 1

```

Title: 03_Python_Iterations and Loops in Python
  
Starred Blocks: 
	  
Well done, Space Explorer! Our interstellar neighborhood, _Cosmo_, is home to three planets. Each planet, in turn, has five orbits. In the provided code, you will journey through each orbit of every planet in _Cosmo_. Once you press the `Run` button, the details of your excursion will be displayed. Embark on this exploration through nested loops now!

```python

# Cosmo has 3 planets, each planet has 5 orbits. Let's explore them with nested loops:
 

cosmo_id = 1

planet_limit = 4

orbit_limit = 6

  

while cosmo_id < planet_limit:

    print('Cosmo', cosmo_id)

    orbit_id = 1

    while orbit_id < orbit_limit:

        print('Orbit:', orbit_id, 'of Cosmo:', cosmo_id)

        orbit_id += 1

    cosmo_id += 1

```

Output:

```

Cosmo 1
Orbit: 1 of Cosmo: 1
Orbit: 2 of Cosmo: 1
Orbit: 3 of Cosmo: 1
Orbit: 4 of Cosmo: 1
Orbit: 5 of Cosmo: 1
Cosmo 2
Orbit: 1 of Cosmo: 2
Orbit: 2 of Cosmo: 2
Orbit: 3 of Cosmo: 2
Orbit: 4 of Cosmo: 2
Orbit: 5 of Cosmo: 2
Cosmo 3
Orbit: 1 of Cosmo: 3
Orbit: 2 of Cosmo: 3
Orbit: 3 of Cosmo: 3
Orbit: 4 of Cosmo: 3
Orbit: 5 of Cosmo: 3

``````

You've presented a Python script and a description that illustrates a scenario of traversing through orbits of planets within a fictional system named _Cosmo_. It seems that you're using this example to demonstrate how nested loops can simulate traversing through multiple layers of a system, such as planets and their orbits.

Your code snippet is set to iterate over these entities, and you've set it up with a couple of variables (`cosmo_id`, `planet_limit`, `orbit_limit`) to control the looping process. Specifically, your outer loop represents the planets (labelled as `Cosmo` with IDs), and the inner loop represents the orbits around each planet.

However, your description mentions that _Cosmo_ contains three planets, each with five orbits, but your code is set to loop through four planets (`planet_limit = 4`) and six orbits (`orbit_limit = 6`). This discrepancy might lead to confusion about the actual structure of _Cosmo_ based on your narrative. To align the code with your description:

- You might want to adjust `planet_limit` to `4` (since counting starts from 1 and it should stop before hitting 4 to encompass three planets).
- Similarly, adjust `orbit_limit` to `6` to correctly iterate through five orbits per planet.

Here's how your code would look if you match it with the narrative description you've provided, ensuring that it will accurately reflect the journey through three planets and five orbits per planet:

python

复制代码

```python

# Cosmo has 3 planets, each planet has 5 orbits. Let's explore them with nested loops:
cosmo_id = 1 # Start with the first 
planetplanet_limit = 4  # We need to visit 3 planets (stop before 4)
orbit_limit = 6 # Each planet has 5 orbits (stop before 6)
while cosmo_id < planet_limit: # Iterate through each planet print('Cosmo', cosmo_id) # Print the current planet
	print('Cosmo', cosmo_id) # Print the current planet orbit_id = 1 # Start with the first orbit
	 while orbit_id < orbit_limit: # Iterate through each orbit of the current planet 
	 print('Orbit:', orbit_id, 'of Cosmo:', cosmo_id) # Print the current orbit
	  orbit_id += 1 # Move to the next orbit
	   cosmo_id += 1 # Move to the next planet

```

This corrected script will now reflect your narrative more closely and provide a clear demonstration of nested loops functioning as intended. Once run, this script will iterate through each of the three planets, exploring all five orbits around each one, exactly as you described in your setup.翻译成中文

> 此更正后的脚本现在将更准确地反映您的叙述，并清晰地演示了嵌套循环按预期正常运行。一旦运行，该脚本将遍历三个行星中的每一个，探索每个行星周围的全部五个轨道，这与您在设置中的描述完全一致。

### 「practice」Planet Gazing from Stars: Changing Print Statements
Excellent work, Space Explorer! Now let's make a change. Instead of having _planets_ witness _stars_, we'll switch it around. Change the `print` statement in the code so it displays which _planet_ is seen from each _star_. Let's go!翻译成中文

> 干得好，太空探险家！现在我们做个更改。不再让 _planets_ 见证 _stars_，而是反过来。更改代码中的 `print` 语句，使其显示从每个 _star_ 看到的 _planet_。让我们开始吧！

```python

stars = ["Alpha Centauri", "Betelgeuse", "Capella"]

planets = ["Earth", "Mars", "Venus"]

  

print("Welcome to our celestial tour! Here is a list of stars witnessed by each planet.")

for planet in planets:

print(planet + " sees:", end=' ')

for star in stars:

print(star, end=', ')

print()

```

```python

stars = ["Alpha Centauri", "Betelgeuse", "Capella"]

planets = ["Earth", "Mars", "Venus"]

  

print("Welcome to our celestial tour! Here is a list of planets seen from each star.")

for star in stars:

print(star + " is seen by:", end=' ')

for planet in planets:

print(planet, end=', ')

print()

``````

I can help explain technical concepts, clarify doubts regarding practices, guide you through solving coding challenges without giving away the direct solution, and check your solutions to ensure they're on the right path. If you're stuck or need a hint on refining your code, just let me know how I can assist you!

Notice the error message regarding indentation. Python is strict about indentation as it defines the block of code that belongs to a loop or condition. In your code, the `print` statement inside the loop should be indented. Try adjusting the indentation for the line inside your `for` loop like this:

```python

for star in stars:
    print(star + " is seen by:", end=' ')
    for planet in planets:
        print(planet, end=', ')
    print()

```

This keeps your code structured and solves the indentation error. Give it a try and see if it resolves the issue!
output

```markdown

> Welcome to our celestial tour! Here is a list of planets seen from each star.  
Alpha Centauri is seen by: Earth, Mars, Venus,   
Betelgeuse is seen by: Earth, Mars, Venus,   
Capella is seen by: Earth, Mars, Venus,

```

### 「practice」Stellar Constellation Corrections
Admirable work, **Star-tracker**! We've just received a report detailing a slight turbulence in the Python code controlling our _star-tracking system_. The code is designed to log questions about stars and their corresponding constellations; however, there appears to be an issue. Could you help us identify and rectify the problem?

太棒了，**Star-tracker**！我们刚刚收到了一份报告，详细说明了控制我们_恒星追踪系统_的 Python 代码中出现了一些轻微的紊乱。该代码旨在记录有关恒星及其对应星座的问题；然而，似乎存在一个问题。你能帮助我们找出并纠正这个问题吗？

```python

# Initializing the stars and constellations

stars_in_sky = ['Alpha', 'Beta', 'Gamma', 'Delta']

constellations = ['Orion', 'Cancer', 'Gemini']

  

# Nested loop representation of stars and their constellations

for constellation in constellations:

for stars_in_sky in constellations:

print("Does star", stars_in_sky, "belong to the", constellation, "constellation?")

```

It seems you're attempting to create a Python script that checks whether certain stars belong to specified constellations by using nested loops. However, there is a confusion in your loop structure and variable naming that needs to be addressed to make the script functional.

### Original Script Problem

1. **Variable Overlap**: In your nested loop, you're using `stars_in_sky` as both the list of stars and as the iterating variable for the inner loop. This causes the list `stars_in_sky` to be overwritten by the string values of `constellation`, which disrupts the intended logic of iterating over stars.

### Corrected Version

You should maintain separate variables for iterating over the list of stars and the list of constellations. Here is a corrected version of your code:

```python

# Lists of stars and constellations
stars_in_sky = ['Alpha', 'Beta', 'Gamma', 'Delta']
constellations = ['Orion', 'Cancer', 'Gemini']

# Nested loop to check if each star belongs to each constellation
for constellation in constellations:
    for star in stars_in_sky:
        print("Does star", star, "belong to the", constellation, "constellation?")

```

### Explanation

- **Outer Loop**: Iterates through each constellation.
- **Inner Loop**: Iterates through each star in the `stars_in_sky` list without modifying the list itself.
- **Print Statement**: Outputs a question for each combination of star and constellation, which seems to be your original intent.

This correction ensures that each star is checked against each constellation without any overlap in variable names or unintended overwriting of data.

output

```python

Does star Alpha belong to the Orion constellation?  
Does star Beta belong to the Orion constellation?  
Does star Gamma belong to the Orion constellation?  
Does star Delta belong to the Orion constellation?  
Does star Alpha belong to the Cancer constellation?  
Does star Beta belong to the Cancer constellation?  
Does star Gamma belong to the Cancer constellation?  
Does star Delta belong to the Cancer constellation?  
Does star Alpha belong to the Gemini constellation?  
Does star Beta belong to the Gemini constellation?  
Does star Gamma belong to the Gemini constellation?  
Does star Delta belong to the Gemini constellation?

```

### 「practice」Space Mission Assignment
Great job, Space Voyager! Now, let's see if you can chart your own course.

Your task is to fill in the code to assign each **astronaut** to each **planet** in the mission plan.

```python

# Imagine we have 3 astronauts ready for the mission to 3 different planets

astronauts = ['Buzz', 'Neil', 'Michael']

planets = ['Mars', 'Venus', 'Jupiter']

  

# Let's use nested loops to assign each astronaut to each planet

for astronaut in astronauts:

# TODO: Write a nested for loop and print statement to assign each astronaut to each planet

```

> To achieve the task of assigning each astronaut to each of the planets, we'll need to create a nested loop structure within your existing code. Here’s how to think about it: You have a list of astronauts and a list of planets, and you want to pair each astronaut with every planet. This means for each astronaut, you will loop through all the planets and print a statement that assigns them to a planet.

Here's the detailed approach and the completed code:

1. **Outer Loop** - This loop will go through each astronaut in the list `astronauts`.
2. **Inner Loop** - Inside the outer loop, this loop will iterate over each planet in the list `planets`.
3. **Print Statement** - Within the inner loop, you'll print a statement that assigns the current astronaut from the outer loop to the current planet from the inner loop.

Here is how you can fill in the code:

```python

# List of astronauts ready for the mission
astronauts = ['Buzz', 'Neil', 'Michael']

# List of planets they will visit
planets = ['Mars', 'Venus', 'Jupiter']

# Using nested loops to assign each astronaut to each planet
for astronaut in astronauts:
    for planet in planets:
        print(f"{astronaut} is assigned to {planet}.")

```

This code will result in each astronaut being printed alongside each planet, effectively simulating the scenario where each astronaut is tasked with visiting each of the three planets.
output

```

Buzz is assigned to Mars.  
Buzz is assigned to Venus.  
Buzz is assigned to Jupiter.  
Neil is assigned to Mars.  
Neil is assigned to Venus.  
Neil is assigned to Jupiter.  
Michael is assigned to Mars.  
Michael is assigned to Venus.  
Michael is assigned to Jupiter.

```

### 「practice」Adding Orbits to Our Universe
Great work, Stellar Navigator!

Next, you will enhance your universe. For each planet, you will illustrate its orbits. You need to implement the **innermost loop** specifically for the orbits. Using the knowledge you've acquired thus far, can you figure that out?

```python

# Cosmos, planets, and orbits.

cosmos = 1 # The cosmos
  
while cosmos <= 3: # For each cosmos

print("Cosmos: ", cosmos)

planet = 1 # Each cosmos has planets

while planet <= 3: # For each planet in the cosmos

print("Planet: ", planet)

# TODO: Implement an innermost loop for the orbits of each planet.

# Assume that each planet has 3 orbits

# For each orbit, print it.

planet += 1 # Move to the next planet

cosmos += 1 # Move to the next cosmos

```

output
> Cosmos:  1  
Planet:  1  
Planet:  2  
Planet:  3  
Cosmos:  2  
Planet:  1  
Planet:  2  
Planet:  3  
Cosmos:  3  
Planet:  1  
Planet:  2  
Planet:  3

```python

# Cosmos, planets, and orbits.

cosmos = 1 # The cosmos
  
while cosmos <= 3: # For each cosmos

print("Cosmos: ", cosmos)

planet = 1 # Each cosmos has planets

while planet <= 3: # For each planet in the cosmos

print("Planet: ", planet)

# Implement an innermost loop for the orbits of each planet.

orbit = 1 # Each planet has orbits

while orbit <= 3: # For each orbit of the planet

print("Orbit: ", orbit)

orbit += 1 # Move to the next orbit

planet += 1 # Move to the next planet

cosmos += 1 # Move to the next cosmos

```

> You're seeking to enhance a Python script to simulate a universe with multiple cosmos, planets, and orbits. In the existing script, you have already set up the framework for cosmos and planets, and now you want to expand this structure to include orbits for each planet. To do this, you will need to add another nested loop that iterates through each orbit of a planet, printing out the orbit number for every planet in each cosmos.

Here's an expanded and modified version of your script that includes the implementation of orbits for each planet:

```python

cosmos = 1  # The cosmos

while cosmos <= 3:  # For each cosmos
    print("Cosmos: ", cosmos)
    planet = 1  # Each cosmos has planets

    while planet <= 3:  # For each planet in the cosmos
        print("  Planet: ", planet)
        orbit = 1  # Each planet has orbits

        while orbit <= 3:  # For each orbit in the planet
            print("    Orbit: ", orbit)
            orbit += 1  # Move to the next orbit

        planet += 1  # Move to the next planet

    cosmos += 1  # Move to the next cosmos

```

This script now includes a third loop nested within the planet loop, which handles the orbits. For each planet, it iterates three times, representing three orbits. This structure allows you to simulate a universe where each of three cosmos contains three planets, and each planet has three orbits. The indentation increases with each level to visually separate the different levels of the simulation, making it easier to understand the hierarchy and flow of cosmos, planets, and orbits.

> Great! Let's break down the task and work on implementing the orbit loop step-by-step within the structure of your existing code.

Your task is to create an innermost loop that handles the orbits for each planet. Here's the skeleton code with annotations explaining each part:

1. **Initialize the orbit variable**: Just like you initialize the `planet` variable before starting its loop, you'll need to initialize the `orbit` variable before you start the orbit loop.
2. **Start the orbit loop**: This loop should iterate three times since each planet has three orbits.
3. **Set a condition for the loop**: This will ensure that the loop iterates the correct number of times (three in this case).
4. **Print the orbit inside the loop**: This is where you'll show the number of each orbit.
5. **Increment your orbit counter**: This is crucial to avoid creating an infinite loop and ensure the loop progresses to the next iteration.

Here is how you can integrate these steps into your existing code:

```python

cosmos = 1  # Initialize the cosmos variable

while cosmos <= 3:  # Start the cosmos loop (up to 3)
    print("Cosmos: ", cosmos)
    planet = 1  # Initialize the planet variable inside the cosmos loop

    while planet <= 3:  # Start the planet loop (each cosmos has 3 planets)
        print("  Planet: ", planet)
        orbit = 1  # Initialize the orbit variable here, inside the planet loop

        while orbit <= 3:  # Start the orbit loop (each planet has 3 orbits)
            print("    Orbit: ", orbit)
            orbit += 1  # Increment the orbit counter to move to the next orbit

        planet += 1  # Increment the planet counter to move to the next planet

    cosmos += 1  # Increment the cosmos counter to move to the next cosmos

```

This structure makes sure that for each planet in each cosmos, three orbits are printed, demonstrating the nested looping technique in Python. With this setup, each `while` loop handles a specific level of the hierarchy: cosmos, planets, and orbits.

Would you like to run this code to see how it outputs, or do you need further explanations on any of these parts?

debug

It appears there isn't any code in your current submission. This could happen if you accidentally deleted your code or didn't save your changes before running your code.

Let's try this step by step again:

1. Make sure you're starting with the initial snippet provided in the practice.
2. Then, add the inner loop for orbits as discussed before.

Here's a refresher on the structure to help guide you:

```python

# Cosmos, planets, and orbits.
cosmos = 1  # The cosmos

while cosmos <= 3:  # For each cosmos 
    print("Cosmos: ", cosmos)
    planet = 1  # Each cosmos has planets
    while planet <= 3:  # For each planet in the cosmos
        print("Planet: ", planet)
        orbit = 1  # Start with the first orbit
        while orbit <= 3:  # For each orbit around a planet
            print("Orbit: ", orbit)  # Print the orbit number
            orbit += 1  # Move to the next orbit
        planet += 1  # Move to the next planet
    cosmos += 1  # Move to the next cosmos

```

Please make sure to carefully copy your code, including the orbit loop, into the IDE. After you've added your code, remember to hit "Save" or ensure it's saved, then run it again. If you face any specific challenges or errors, let me know, and I'll be more than happy to help you debug!

output

```python

Cosmos:  1  
Planet:  1  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Planet:  2  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Planet:  3  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Cosmos:  2  
Planet:  1  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Planet:  2  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Planet:  3  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Cosmos:  3  
Planet:  1  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Planet:  2  
Orbit:  1  
Orbit:  2  
Orbit:  3  
Planet:  3  
Orbit:  1  
Orbit:  2  
Orbit:  3

```

### 「practice」Orbiting through Cosmos: Nested Loops in Action
Well done, Space Explorer! Now, it's your turn to implement the same concept from scratch! In the cosmos, each _planet_ has a varying number of _satellites_.

Your mission is to write a program that uses _nested loops_ to traverse each `planet`, along with each respective `satellite`.

```python

# Imagine we have 3 planets in a cosmos that have different numbers of satellites.

satellites = {'Earth': 1, 'Mars': 2, 'Neptune': 14}

  

# TODO: For each planet, print its name along with the number of satellites it has.

```

  翻译

```

# TODO: For each satellite of a planet, print its order around that planet.

# For example: Satellite 1 around Earth

# For example: Satellite 12 around Neptune

假设我们在宇宙中有3个行星，它们拥有不同数量的卫星。

卫星 = {'地球': 1, '火星': 2, '海王星': 14}

# TODO：对于每个行星，打印其名称以及其拥有的卫星数量。

# TODO：对于一个行星的每颗卫星，打印其围绕该行星的顺序。

# 例如：第1颗围绕地球运转的卫星

# 例如：第12颗围绕海王星运转的卫星

```

```python

# Imagine we have 3 planets in a cosmos that have different numbers of satellites.

satellites = {'Earth': 1, 'Mars': 2, 'Neptune': 14}

# For each planet, print its name along with the number of satellites it has.

for planet, num_satellites in satellites.items():
    print(f"{planet} has {num_satellites} satellites.")

# For each satellite of a planet, print its order around that planet.

for planet, num_satellites in satellites.items():
    for satellite_order in range(1, num_satellites + 1):
        print(f"Satellite {satellite_order} around {planet}")

```

> 当然可以解释。这段代码的目标是遍历每个行星及其相应的卫星。

- `for planet, num_satellites in satellites.items():` 这个循环通过遍历 `satellites` 字典的项 (`items`) 来进行。每一次迭代，它都会提取键值对`planet`（行星名字）和 `num_satellites`（相应的卫星数量）。
    
- 对于字典中的每个行星（`planet`），内嵌循环 `for satellite_order in range(1, num_satellites + 1):` 将会执行。这个内部循环用于遍历从 `1` 到 `num_satellites`（行星的卫星数量）的每一个数字，表示卫星的顺序。
    
- `print(f"Satellite {satellite_order} around {planet}")` 这一行会在内部循环中为每个卫星打印其顺序和它所围绕的行星。`f`在`print`函数前面表示这是一个格式化字符串，允许你将变量直接插入字符串中。所以每次循环时，`{satellite_order}` 会被替换成当前的卫星顺序，`{planet}` 会被替换成当前行星的名字。
    

简单来说，这段代码首先遍历所有行星，并且对于每个行星，它会遍历其所有卫星，并为每个卫星打印一个包含其顺序和所属行星名字的消息。

output

```python

Earth has 1 satellites.  
Mars has 2 satellites.  
Neptune has 14 satellites.  
Satellite 1 around Earth  
Satellite 1 around Mars  
Satellite 2 around Mars  
Satellite 1 around Neptune  
Satellite 2 around Neptune  
Satellite 3 around Neptune  
Satellite 4 around Neptune  
Satellite 5 around Neptune  
Satellite 6 around Neptune  
Satellite 7 around Neptune  
Satellite 8 around Neptune  
Satellite 9 around Neptune  
Satellite 10 around Neptune  
Satellite 11 around Neptune  
Satellite 12 around Neptune  
Satellite 13 around Neptune  
Satellite 14 around Neptune

```

# [Lesson 6: Commanding Loops: Mastery of Break and Continue in Python](https://learn.codesignal.com/preview/lessons/153)

##### Setting the Stage: Control Over Loops with Break and Continue

Hello, and welcome to this stimulating session! Today, you will delve into Python loops' governing principles with `break` and `continue`. These potent tools can halt a loop mid-way or bypass an iteration.

Sounds thrilling? Let's dive in!

##### Break: The Loop Controller in For Loops

The `break` keyword ends a loop before it exhausts all iterations:

```python

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet)
    if planet == 'Earth':
        print("Found Earth!")
        break

```

The code prints:

```

Mercury
Venus
Earth
Found Earth!

```

In this `for` loop, once we reach Earth, `break` terminates the loop. We avoid unnecessary iterations over the remaining planets.

##### Break: The Loop Controller in While Loops

The `break` command works similarly in a `while` loop:

```python

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1
    if countdown == 5:
        print("Time to stop!")
        break

```

The code prints:

```python

10
9
8
7
6
Time to stop!

```

##### Continue: The Loop Skipper

The `continue` keyword omits a part of the current loop iteration and proceeds to the next:

```python

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    if planet == 'Mars':
        continue
    print(planet)

```

The code prints:

```

Mercury
Venus
Earth
Jupiter
Saturn
Uranus
Neptune

```

After encountering Mars, `continue` skips the printing command and jumps to the next planet.

##### Nested Loops and Loop Control

`break` and `continue` also operate within nested loops. In them, `break` only stops the innermost loop it operates in:

```python

celestial_objects_data = [
    ["star", ["observed", "unobserved", "observed"]],
    ["planet", ["unobserved", "unobserved", "observed"]],
    ["galaxy", ["observed", "observed", "observed"]],
    ["comet", ["unobserved", "unobserved", "unobserved", "unexpected"]]
]

for item in celestial_objects_data:
    obj, observations = item
    print('Object:', obj)
    for observation in observations:
        if observation == "unobserved":
            print("An object was missed!")
            break
        if observation != "observed" and observation != "unobserved":
            # Skipping unexpected input
            continue
        print('Status:', observation)

```

The code prints:

```

Object: star
Status: observed
An object was missed!
Object: planet
An object was missed!
Object: galaxy
Status: observed
Status: observed
Status: observed
Object: comet
An object was missed!

```

##### Lesson Summary

Give yourself a pat on the back; you've just overcome a significant hurdle in your Python learning journey! You've deciphered how to control loops using `break` and `continue`. You have understood their roles in single and nested loops. Upcoming hands-on exercises will further refine these concepts. Brace yourselves, and let's dive in!

### 「practice」Observing Celestial Bodies with Safety Measures

### 「practice」Preserving Telescope Battery Power in Space
Woof-woof! Excellent job, _Space Explorer_! In the starter code, we are observing the **visibility** of some famous constellations. Your job is to skip the `Orion` visibility processing, thus saving some battery power on our telescope.

Ready? Let's go!

```python

constellation_data = [
["scutum", ["visible", "visible", "not visible"]],

["cassiopeia", ["visible", "visible", "visible"]],

["orion", ["not visible", "not visible", "visible"]],

["cygnus", ["visible", "not visible", "visible"]]

]

for constellation in constellation_data:

name, visibility = constellation

print('Constellation:', name)

for status in visibility:

print('Visibility:', status)

```

```

To skip the visibility processing for `Orion` and save some battery power, you need to insert a condition to check when the name is "Orion" and then use `continue` to skip the rest of the current iteration in the loop. Here's a hint to get you started on modifying the loop:

Before printing the constellations, check if the name is "Orion". If it is, you can skip the current iteration without printing its visibility statuses.

Can you think of a way to implement this using a conditional statement and the `continue` keyword you learned about in the lesson?

```

### 「practice」Fixing the Visibility Check in the Astronomy Observation Code
To skip the visibility processing for `Orion` and save some battery power, you need to insert a condition to check when the name is "Orion" and then use `continue` to skip the rest of the current iteration in the loop. Here's a hint to get you started on modifying the loop:

Before printing the constellations, check if the name is "Orion". If it is, you can skip the current iteration without printing its visibility statuses.

Can you think of a way to implement this using a conditional statement and the `continue` keyword you learned about in the lesson?

```python

constellation_data = [

["scutum", ["visible", "visible", "not visible"]],

["cassiopeia", ["visible", "visible", "visible"]],

["orion", ["not visible", "not visible", "visible"]],

["cygnus", ["visible", "not visible", "visible"]]

]

  

for constellation in constellation_data:

name, visibility = constellation

print('Constellation:', name)

for status in visibility:

print('Visibility:', status)

```

```python

constellation_data = [
["scutum", ["visible", "visible", "not visible"]], ["cassiopeia", ["visible", "visible", "visible"]], ["orion", ["not visible", "not visible", "visible"]], ["cygnus", ["visible", "not visible", "visible"]] 
] 
for constellation in constellation_data: 
name, visibility = constellation 
if name == "orion": # Check if the name is "Orion" 
continue # Skip the rest of the current iteration 
print('Constellation:', name) 
for status in visibility:
print('Visibility:', status)

```

```

Constellation: scutum  
Visibility: visible  
Visibility: visible  
Visibility: not visible  
Constellation: cassiopeia  
Visibility: visible  
Visibility: visible  
Visibility: visible  
Constellation: cygnus  
Visibility: visible  
Visibility: not visible  
Visibility: visible

```

### 「practice」Adding a Break Condition to Conserve Energy
Nicely done, Star-gazer! It seems there's a small hiccup in our next data observing session.

Try running the provided code and identify the issue that prevents us from correctly traversing astronomical objects based on their visibility statuses - when we detect the invisible object, we should leave it immediately! Are you able to correct it?

```python

astronomy_objects_data = [

["stars", ["visible", "visible", "invisible"]],

["planets", ["visible", "invisible", "invisible"]],

["galaxies", ["invisible", "visible", "visible"]],

["comets", ["visible", "invisible", "visible"]],

]

  

for astro_object in astronomy_objects_data:

object_type, visibility = astro_object

print('Exploring object:', object_type)

for status in visibility:

if status == "invisible":

print("Invisible object detected, we should leave the object immediately!")

continue

print('Visibility:', status)

```

```python

astronomy_objects_data = [ 
["stars", ["visible", "visible", "invisible"]],
 ["planets", ["visible", "invisible", "invisible"]], 
["galaxies", ["invisible", "visible", "visible"]],
 ["comets", ["visible", "invisible", "visible"]], 
] 
for astro_object in astronomy_objects_data: 
object_type, visibility = astro_object print('Exploring object:',
 object_type) for status in visibility: 
if status == "invisible": 
print("Invisible object detected, we should leave the object immediately!") break 
print('Visibility:', status)

```

```

Visibility: visible  
Invisible object detected, we should leave the object immediately!  
Exploring object: planets  
Visibility: visible  
Invisible object detected, we should leave the object immediately!  
Exploring object: galaxies  
Invisible object detected, we should leave the object immediately!  
Exploring object: comets  
Visibility: visible  
Invisible object detected, we should leave the object immediately!

```

> 这段代码的目的是处理一个包含天文对象数据的列表。每个天文对象有两个属性：类型（如星星、行星等）和可见性状态的列表（可见或不可见）。这个程序会遍历每个天文对象，然后再遍历它们的可见性状态。

- 首先，我们定义了一个名为 `astronomy_objects_data` 的列表，其中包含了不同天文对象的数据。每个对象都是一个包含两个元素的列表：天文对象的类型（`object_type`）和一个表示可见性状态的列表（`visibility`）。
    
- 使用第一个 `for` 循环，我们遍历 `astronomy_objects_data` 列表中的每个天文对象。在每次迭代中，我们通过解构来获取天文对象的类型和它的可见性状态列表。
    
- 接着，我们打印出正在探索的天文对象类型。
    
- 然后，使用第二个 `for` 循环，我们遍历当前天文对象的每个可见性状态。在每次迭代中，我们检查状态是否为 `invisible`（不可见）。
    
    - 如果状态为 `invisible`，我们打印出“Invisible object detected, we should leave the object immediately!”（检测到不可见对象，我们应立即离开此对象！），然后使用 `break` 语句立即退出当前正在遍历的可见性状态列表的循环。这意味着如果我们遇到一个不可见的对象，我们将不会继续检查该天文对象的其他可见性状态。
        
    - 如果状态不是 `invisible`（即可见），我们打印出可见性状态。
        

使用 `break` 替换原代码中的 `continue` 改变了程序的行为。`continue` 会跳过当前迭代的其余部分并继续下一个迭代，而 `break` 会完全结束循环。这样，当遇到不可见对象时，我们不会继续检查同一天文对象的其余状态，符合题目的要求。

> `break` 和 `continue` 是Python中控制循环流程的两个关键字，它们的用法和作用有明显的区别：

- `break` 用于完全结束当前循环，无论是 `for` 循环还是 `while` 循环。当 `break` 被执行时，循环将停止迭代，且退出循环体，继续执行循环后面的代码。
    
- `continue` 用于跳过当前循环的剩余代码，并直接进入下一次迭代。它只影响当前迭代的执行，循环本身不会被终止，而是继续从下一次迭代开始执行。
    

简单地说，`break` 是“立即停止循环”，而 `continue` 是“跳过当前迭代”。

当然，我来通过一个简化的例子，详细解释 `break` 和 `continue` 的区别。

假设我们有一组数字，并且我们想对它们进行一些检查。

### 示例：数字列表的遍历

#### 列表：

```python

1numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]`

```

#### 目标：

- 当我们遇到数字 `5` 时，打印一条消息并完全停止遍历（使用 `break`）。
- 当我们遇到数字 `3` 时，仅跳过这个数字并继续遍历其他数字（使用 `continue`）。

### 使用 `continue`：

```python

for number in numbers:
    if number == 3:
        print("Skipping:", number)
        continue
    print("Number:", number)

# 输出将会跳过3，但是会继续打印其他数字直到结束。```

```

输出：

```python

Number: 1
Number: 2
Skipping: 3
Number: 4
Number: 5
Number: 6
...

```

在这里，`continue` 让我们跳过了数字 `3`，但没有停止整个循环。

### 使用 `break`：

```python

for number in numbers:
    if number == 5:
        print("Stopping at:", number)
        break
    print("Number:", number)

# 当遇到5时，输出将停止，不会打印5或之后的数字。

```

输出：

```python

Number: 1
Number: 2
Number: 3
Number: 4
Stopping at: 5

```

在这里，`break` 让我们在数字 `5` 出现的时候立即停止遍历列表，即使列表中还有其他数字。

这个例子展现了 `continue` 用于跳过某些条件下的迭代，但允许循环继续；而 `break` 用于在满足某个条件时完全终止循环。

# 「practice」Navigating Celestial Bodies: Observations in Space
Splendid work, Cosmic Coder! Now, let's see if we can take a closer look at these galaxies. Could you modify the code to break the loop when we find the first `'invisible'` galaxy? Doing so would help us conserve energy.

```python

galaxy_visibility = ['visible', 'visible', 'invisible', 'visible', 'invisible', 'visible', 'visible']

  

for index, status in enumerate(galaxy_visibility):

# TODO: Write a condition to check the status of the galaxy and break the loop as required

print(f"Galaxy number {index + 1} is {status}.")

if status == 'invisible':

break

```

```python

galaxy_visibility = ['visible', 'visible', 'invisible', 'visible', 'invisible', 'visible', 'visible']

for index, status in enumerate(galaxy_visibility):
    print(f"Galaxy number {index + 1} is {status}.")
    if status == 'invisible':
        break

```

输出

```

Galaxy number 1 is visible.  
Galaxy number 2 is visible.  
Galaxy number 3 is invisible.

```

Alright, Space Galactic Pioneer! Your final challenge awaits! You have everything in place; it's time to fetch some data and iterate over it using _loops_.

Remember to print the name of each celestial body. However, if a body is unobserved, print the warning message and proceed to the next one. Just like in real-life data processing, not every piece of data is useful or safe.

Let's get started!

```python

# Defining an array with some celestial bodies and their observed status

celestial_bodies = [('Star 1', "observed"), ('Star 2', "unobserved"), ('Star 3', "observed"), ('Star 4', "unobserved")]

  

# TODO: Iterate over each celestial body in "celestial_bodies"

# TODO: print a message saying that we are observing the current celestial body

  

# TODO: add a condition that checks if the current celestial body is unobserved

# If the body is unobserved, print a warning message

# and skip to the next iteration of the loop

  

# TODO: print a message saying the current celestial body and its observed status

```

```python

# Defining an array with some celestial bodies and their observed status

celestial_bodies = [('Star 1', "observed"), ('Star 2', "unobserved"), ('Star 3', "observed"), ('Star 4', "unobserved")]

# Iterate over each celestial body in "celestial_bodies"
for body, status in celestial_bodies:
    print(f"Observing {body}...")
    
    # Add a condition that checks if the current celestial body is unobserved
    if status == "unobserved":
        print(f"Warning: {body} is unobserved. Skipping...")
        continue
    
    # Print a message saying the current celestial body and its observed status
    print(f"{body} is {status}.")
    print()

```

让我们一步步解释代码的含义：

**定义星体数组**

`celestial_bodies = [('Star 1', "observed"), ('Star 2', "unobserved"), ('Star 3', "observed"), ('Star 4', "unobserved")]`

这里定义了一个名为 `celestial_bodies` 的数组，包含四个星体，每个星体是一个 tuple，包含星体的名称和观测状态（observed 或 unobserved）。

**遍历星体数组**

`for body, status in celestial_bodies:`

这里使用了一个 for 循环来遍历 `celestial_bodies` 数组。每次循环都会将当前星体的名称和观测状态赋值给 `body` 和 `status` 变量。

**观测星体**

`print(f"Observing {body}...")`

在每次循环中，首先打印出当前星体的名称，表示我们正在观测这个星体。

**检查星体是否未观测**

`if status == "unobserved":`

这里检查当前星体的观测状态是否为 "unobserved"。

**警告未观测星体**

`print(f"Warning: {body} is unobserved. Skipping...")`

如果星体未观测，我们打印出一个警告信息，表示我们将跳过这个星体。

`continue`

使用 `continue` 语句跳过当前循环，继续下一个星体。

**打印星体信息**

`print(f"{body} is {status}.")`

如果星体已经观测，我们打印出星体的名称和观测状态。

`print()`

最后，我们打印出一个空行，以便与下一个星体的信息分开。

总的来说，这个代码遍历了星体数组，对每个星体进行观测，如果星体未观测，就打印出警告信息并跳过；否则，打印出星体的名称和观测状态。

> Looking at your code, I see you're on the right track but a little adjustment is needed. Let's focus on two main areas:

1. **Where you've placed the `continue` statement:** Currently, the `continue` is outside the `if` block and will always be executed, which isn't the intention. You want to only skip the rest of the loop's body when a celestial body is "unobserved".
    
2. **Printing the observed status:** The final `print` statement for displaying the body's observed status is outside the loop. It should be part of the loop but only executed if the celestial body is not skipped.
    

Here's a hint:

- Ensure the `continue` statement is part of the condition that checks if the celestial body is unobserved. This will correctly skip the unobserved bodies.
- For bodies that are not being skipped, ensure your next `print` statement about the celestial body being observed is within the loop but after your condition checking for "unobserved" status. This way, it only prints this information for bodies that do not meet the "unobserved" condition.

Try adjusting your code with these hints, and remember to closely check your loop and conditional block syntax to make sure each action happens where and when you intend it to.

```python

# Defining an array with some celestial bodies and their observed status

celestial_bodies = [('Star 1', "observed"), ('Star 2', "unobserved"), ('Star 3', "observed"), ('Star 4', "unobserved")]

# Iterate over each celestial body in "celestial_bodies"
for body, status in celestial_bodies:
    print(f"Observing {body}...")
    
    if status == "unobserved":
        print(f"Warning: {body} is unobserved. Skipping...")
        continue
    
    print(f"{body} is {status}.")
    print()

```

输出

```

Observing Star 1...  
Star 1 is observed.  
  
Observing Star 2...  
Warning: Star 2 is unobserved. Skipping...  
Observing Star 3...  
Star 3 is observed.  
  
Observing Star 4...  
Warning: Star 4 is unobserved. Skipping...

```