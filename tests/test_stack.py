import pytest
from src.stack import Stack

def test_stack_without_errors() -> None:
    stack = Stack()

    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    assert stack.peek() == 2

    assert stack.pop() == 2
    assert len(stack) == 1

    stack.push(-1)
    assert stack.min() == -1

    stack.push(3)
    assert stack.min() == -1


def test_stack_on_errors() -> None:
    stack = Stack()

    with pytest.raises(ValueError):
        stack.push("l")

    with pytest.raises(IndexError):
        stack.pop()

    with pytest.raises(IndexError):
        stack.peek()
