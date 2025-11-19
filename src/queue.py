class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, x: int) -> None:
        """
        Вставить эл-т x в конец очереди
        """
        if type(x) is not int:
            raise ValueError('Wrong type')
        self.items.insert(0, x)

    def dequeue(self) -> int:
        """
        Удалить и вернуть первый эл-т очереди
        """
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items.pop()

    def front(self) -> int:
        """
        Вернуть первый эл-т очереди
        """
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.items[-1]

    def is_empty(self) -> bool:
        """
        Вернуть True, если очередь пустая
        """
        return self.items == []

    def __len__(self) -> int:
        return len(self.items)