def factorial(n: int) -> int:
    """
    Вычислить факториал числа n
    """
    if n == 0:
        return 1
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    return ans


def factorial_recursive(n: int) -> int:
    """
    Вычислить факториал числа n рекурсивно
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)