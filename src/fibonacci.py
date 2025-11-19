def fibo(n: int) -> int:
    """
    Вернуть число n-ое число Фибоначчи
    """
    if n < 2:
        return n
    f1, f2 = 1, 1
    while n > 1:
        n -= 1
        f1, f2 = f2, f1 + f2
    return f1


def fibo_recursive(n: int) -> int:
    """
    Вернуть число n-ое число Фибоначчи (считается рекурсивно)
    """
    if n < 2:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)