import time
from typing import Callable


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Измерить и вернуть время выполнения функции func
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    """
    Вернуть бенчмарк алгоритмов сортировки
    """
    res = {}
    for algo_name, algo in algos.items():
        res[algo_name] = {}
        for array_name, array in arrays.items():
            res[algo_name][array_name] = timeit_once(algo, array)
    return res