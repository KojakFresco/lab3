def fibo(n: int) -> int:
    if n < 2:
        return n
    f1, f2 = 1, 1
    while n > 1:
        n -= 1
        f1, f2 = f2, f1 + f2
    return f1


def fibo_recursive(n: int) -> int:
    if n < 2:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)