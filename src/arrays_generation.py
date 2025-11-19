import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Генерирует массив n случайных целых чисел от lo до hi включительно
    distinct=True - все числа различные
    """

    if seed:
        random.seed(seed)

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError("Недостаточно уникальных чисел в диапазоне")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует почти отсортированный массив n случайных целых чисел
    swap - кол-во обменов эл-тов, чтобы отсортировать массив
    """
    if seed:
        random.seed(seed)

    lst = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Генерирует массив n случайных целых чисел
    k_unique - кол-во уникальных элементов
    """
    if seed:
        random.seed(seed)

    lst = list(range(k_unique))
    return [random.choice(lst) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Генерирует перевернутый массив n целых чисел
    """
    lst = list(range(n))
    lst.reverse()
    return lst


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Генерирует массив n случайных вещественных чисел от lo до hi включительно
    """
    if seed:
        random.seed(seed)

    return [random.uniform(lo, hi) for _ in range(n)]