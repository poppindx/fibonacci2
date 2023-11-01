def fibonacci(n):
    """计算斐波那契数列的前n个数字"""
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# 获取用户输入
num_terms = int(input("请输入要计算的斐波那契数列的项数: "))

# 计算并输出斐波那契数列
fibonacci_sequence = fibonacci(num_terms)
print(f"斐波那契数列的前{num_terms}项为: {fibonacci_sequence}")
