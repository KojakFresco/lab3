def bubble_sort(a: list[int]) -> list[int]:
    """
    Применить сортировку пузырьком к списку
    """
    for i in range(len(a)-1):
        is_sorted = True
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                is_sorted = False
        if is_sorted:
            break
    return a


def quick_sort(a: list[int]) -> list[int]:
    """
    Применить быструю сортировку к списку
    """
    if len(a) <= 1:
        return a
    pivot = a[-1]
    i = -1

    for j in range(len(a) - 1):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[-1] = a[-1], a[i]

    return quick_sort(a[:i]) + [pivot] + quick_sort(a[i + 1:])


def counting_sort(a: list[int]) -> list[int]:
    """
    Применить сортировку подсчетом к списку
    """
    cnt = [0]*(max(a) + 1)

    for i in range(len(a)):
        cnt[a[i]] += 1
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    res = [0]*len(a)
    for i in a:
        cnt[i] -= 1
        res[cnt[i]] = i

    return res


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Применить поразрядную сортировку к списку
    """
    digits = len(str(max(a)))
    for n in range(0, digits):
        cnt = [0] * base

        for i in range(len(a)):
            cnt[a[i] // base**n % base] += 1

        for i in range(1, base):
            cnt[i] += cnt[i - 1]

        res = [0] * len(a)
        for i in range(len(a) - 1, -1, -1):
            d = a[i] // base**n % base
            cnt[d] -= 1
            res[cnt[d]] = a[i]
        a = res
    return a


def insertion_sort(a: list[float]) -> list[float]:
    """
    Применить вспомогательную сортировку вставками к списку
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i
        while j > 0 and a[j - 1] > key:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


def bucket_sort(a: list[float], buckets_cnt: int | None = None) -> list[float]:
    """
    Применить блочную сортировку к списку
    """
    if buckets_cnt is None:
        buckets_cnt = 10

    buckets = [[] for _ in range(buckets_cnt)]
    for i in range(len(a)):
        buckets[int(a[i] * buckets_cnt)].append(a[i])

    res = []
    for bucket in buckets:
        res.extend(insertion_sort(bucket))
    return res


def max_heapify(a: list[int], i: int, n: int) -> None:
    """
    Поставить эл-т с индексом i на правильное место в куче
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[i]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, n)


def heap_sort(a: list[int]) -> list[int]:
    """
    Применить пирамидальную сортировку к списку
    """
    n = len(a)
    for i in range(n - 1, -1, -1):
        max_heapify(a, i, n)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        max_heapify(a, 0, i)

    return a