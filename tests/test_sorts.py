import pytest
from src import sorts
from src import arrays_generation as generate


def test_bubble_sort():
    a = generate.rand_int_array(100, 1, 100, distinct=True, seed=42)
    assert sorts.bubble_sort(a) == sorted(a)

    a = generate.many_duplicates(100, 10, seed="pPrive")
    assert sorts.bubble_sort(a) == sorted(a)


def test_quick_sort():
    a = generate.rand_int_array(100, 1, 100, distinct=True, seed=42)
    assert sorts.quick_sort(a) == sorted(a)

    a = generate.many_duplicates(100, 10, seed="pPrive")
    assert sorts.quick_sort(a) == sorted(a)


def test_counting_sort():
    a = generate.many_duplicates(1000, 10, seed="pPrive")
    assert sorts.counting_sort(a) == sorted(a)


def test_radix_sort():
    a = generate.rand_int_array(100, 1, 100, distinct=True, seed=42)
    assert sorts.radix_sort(a) == sorted(a)

    a = generate.many_duplicates(100, 10, seed="pPrive")
    assert sorts.radix_sort(a) == sorted(a)


def test_bucket_sort():
    a = generate.rand_float_array(1000, seed=42)
    assert sorts.bucket_sort(a) == sorted(a)


def test_heap_sort():
    a = generate.rand_int_array(100, 1, 100, distinct=True, seed=42)
    assert sorts.heap_sort(a) == sorted(a)

    a = generate.many_duplicates(100, 10, seed="pPrive")
    assert sorts.heap_sort(a) == sorted(a)