import pytest

from src import stack
from src.queue import Queue

def test_queue_without_errors() -> None:
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    assert len(queue) == 2
    assert queue.front() == 1

    assert queue.dequeue() == 1
    assert len(queue) == 1


def test_stack_on_errors() -> None:
    queue = Queue()

    with pytest.raises(ValueError):
        queue.enqueue("new")

    with pytest.raises(IndexError):
        queue.dequeue()

    with pytest.raises(IndexError):
        queue.front()