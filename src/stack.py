class Node:
    def __init__(self, val: int = None, prev: 'Node' = None, minval: int = None) -> None:
        self.val = val
        self.prev = prev
        self.minval = minval

class Stack:
    def __init__(self) -> None:
        self.tail = None
        self.length = 0

    def push(self, x: int) -> None:
        """
        Вставить эл-т x в конец стека
        """
        if type(x) is not int:
            raise ValueError('Wrong type')

        self.length += 1
        if self.tail is None:
            self.tail = Node(x, minval=x)
        else:
            self.tail = Node(x, self.tail, min(x, self.tail.val))

    def pop(self) -> int:
        """
        Удалить и вернуть верхний эл-т стека
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        self.length -= 1

        val = self.tail.val
        last_el = self.tail
        self.tail = self.tail.prev
        last_el = None

        return val

    def peek(self) -> int:
        """
        Вернуть значение последнего эл-та стека
        """
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.tail.val

    def is_empty(self) -> bool:
        """
        Вернуть True, если стек пустой
        """
        return self.tail is None

    def min(self) -> int:
        """
        Вернуть минимальный эл-т стека
        """
        return self.tail.minval # за константу для Medium

    def __len__(self) -> int:
        return self.length