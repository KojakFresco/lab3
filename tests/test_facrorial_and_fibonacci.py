from src.fibonacci import fibo, fibo_recursive
from src.factorial import factorial, factorial_recursive

def test_fibo():
    assert fibo(1) == 1
    assert fibo(100) == 354_224_848_179_261_915_075

    assert fibo_recursive(1) == 1
    assert fibo_recursive(10) == 55


def test_factorial():
    assert factorial(0) == 1
    assert factorial(10) == 3628800


def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(10) == 3628800