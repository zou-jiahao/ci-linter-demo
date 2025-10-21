# calculator.py
def add(a, b):
    """
    返回两个数的和。
    如果输入不是数字，抛出 TypeError。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b
    