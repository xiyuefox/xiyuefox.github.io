#!/usr/bin/env python3
"""
ark-code-latest 模型在不同场景的使用示例
"""

import os
from call_ark_code import call_ark_code_model, print_response


def get_environment_variables():
    """获取环境变量配置"""
    api_key = os.getenv("ANTHROPIC_AUTH_TOKEN")
    base_url = os.getenv("ANTHROPIC_BASE_URL")
    model = os.getenv("ANTHROPIC_MODEL")

    if not all([api_key, base_url, model]):
        print("错误：未正确设置环境变量")
        print("请确保已设置以下环境变量：")
        print("  ANTHROPIC_AUTH_TOKEN")
        print("  ANTHROPIC_BASE_URL")
        print("  ANTHROPIC_MODEL")
        return None

    return api_key, base_url, model


def example_1_javascript_optimization():
    """JavaScript 代码优化示例"""
    print("=== JavaScript 代码优化示例 ===")
    print()

    original_code = """
function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

function calculate() {
    var result = [];
    for (var i = 0; i < 10; i++) {
        result.push(fibonacci(i));
    }
    return result;
}
    """.strip()

    messages = [
        {
            "role": "user",
            "content": f"""
你是一位资深的 JavaScript 代码优化专家。请分析以下 JavaScript 代码，并进行优化。

优化要求：
1. 提高执行效率
2. 提升代码可读性
3. 修复潜在的性能问题
4. 加入适当的注释说明
5. 使用现代 JavaScript 语法

原始代码：
```javascript
{original_code}
```

请提供优化后的代码，并详细说明修改点。
"""
        }
    ]

    return messages


def example_2_java_optimization():
    """Java 代码优化示例"""
    print("=== Java 代码优化示例 ===")
    print()

    original_code = """
import java.util.ArrayList;
import java.util.List;

public class DataProcessor {
    public static List<Integer> processData(List<String> input) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < input.size(); i++) {
            String s = input.get(i);
            if (s != null && !s.isEmpty()) {
                try {
                    int num = Integer.parseInt(s);
                    if (num > 0) {
                        result.add(num * 2);
                    }
                } catch (NumberFormatException e) {
                    System.err.println("Invalid number: " + s);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        List<String> input = new ArrayList<>();
        input.add("1");
        input.add("2");
        input.add("abc");
        input.add("4");
        input.add(null);

        List<Integer> output = processData(input);
        System.out.println(output);
    }
}
    """.strip()

    messages = [
        {
            "role": "user",
            "content": f"""
你是一位资深的 Java 代码优化专家。请分析以下 Java 代码，并进行优化。

优化要求：
1. 提高执行效率
2. 提升代码可读性
3. 修复潜在的性能问题
4. 加入适当的注释说明
5. 使用现代 Java 语法和最佳实践

原始代码：
```java
{original_code}
```

请提供优化后的代码，并详细说明修改点。
"""
        }
    ]

    return messages


def example_3_code_explanation():
    """代码解释示例"""
    print("=== 代码解释示例 ===")
    print()

    code_to_explain = """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    data = [3, 6, 8, 10, 1, 2, 1]
    print(f"排序前: {data}")
    sorted_data = quicksort(data)
    print(f"排序后: {sorted_data}")

if __name__ == "__main__":
    main()
    """.strip()

    messages = [
        {
            "role": "user",
            "content": f"""
你是一位代码解释专家。请详细解释以下 Python 代码的功能和工作原理。

代码：
```python
{code_to_explain}
```

请解释：
1. 代码的整体功能
2. 每个函数的作用
3. 算法的工作原理
4. 时间复杂度分析
5. 空间复杂度分析
"""
        }
    ]

    return messages


def example_4_bug_fix():
    """代码调试和修复示例"""
    print("=== 代码调试和修复示例 ===")
    print()

    buggy_code = """
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

def main():
    test_data = [1, 2, 3, 4, 5]
    print(f"平均值: {calculate_average(test_data)}")

    test_data2 = []
    print(f"空列表平均值: {calculate_average(test_data2)}")

if __name__ == "__main__":
    main()
    """.strip()

    messages = [
        {
            "role": "user",
            "content": f"""
你是一位代码调试专家。请分析以下 Python 代码，找出其中的 bug 并修复它。

代码：
```python
{buggy_code}
```

请：
1. 找出代码中的错误
2. 解释错误产生的原因
3. 修复代码
4. 优化代码质量
5. 添加适当的错误处理

请提供修复后的代码，并详细说明修改点。
"""
        }
    ]

    return messages


def example_5_cpp_optimization():
    """C++ 代码优化示例"""
    print("=== C++ 代码优化示例 ===")
    print()

    original_code = """
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<int> processNumbers(vector<string> input) {
    vector<int> result;
    for (int i = 0; i < input.size(); i++) {
        string s = input[i];
        if (!s.empty()) {
            try {
                int num = stoi(s);
                if (num > 0) {
                    result.push_back(num * 2);
                }
            } catch (invalid_argument& e) {
                cerr << "Invalid number: " << s << endl;
            }
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main() {
    vector<string> input = {"1", "2", "abc", "4", "", "3"};
    vector<int> output = processNumbers(input);

    cout << "Processed numbers: ";
    for (int num : output) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
    """.strip()

    messages = [
        {
            "role": "user",
            "content": f"""
你是一位资深的 C++ 代码优化专家。请分析以下 C++ 代码，并进行优化。

优化要求：
1. 提高执行效率
2. 提升代码可读性
3. 修复潜在的性能问题
4. 加入适当的注释说明
5. 使用现代 C++ 语法和最佳实践

原始代码：
```cpp
{original_code}
```

请提供优化后的代码，并详细说明修改点。
"""
        }
    ]

    return messages


def main():
    config = get_environment_variables()
    if not config:
        return

    api_key, base_url, model = config

    examples = [
        ("JavaScript 代码优化", example_1_javascript_optimization),
        ("Java 代码优化", example_2_java_optimization),
        ("代码解释", example_3_code_explanation),
        ("代码调试和修复", example_4_bug_fix),
        ("C++ 代码优化", example_5_cpp_optimization)
    ]

    print("ark-code-latest 模型使用示例")
    print("==============================")
    print()

    for i, (title, example_func) in enumerate(examples):
        print(f"{i + 1}. {title}")

    print()

    try:
        choice = int(input("请选择示例 (1-5): "))
        if choice < 1 or choice > 5:
            raise ValueError("无效的输入")

        selected_example = examples[choice - 1]
        print()
        print(f"运行示例: {selected_example[0]}")

        messages = selected_example[1]()
        response = call_ark_code_model(api_key, base_url, model, messages, max_tokens=3000)
        print_response(response)

    except ValueError as e:
        print(f"错误: {e}")
    except KeyboardInterrupt:
        print("\n程序被用户中断")


if __name__ == "__main__":
    main()
