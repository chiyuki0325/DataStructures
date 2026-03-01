class Queue[T]:
    def __init__(self):
        self.stack: list[T] = []
        self.reverse_stack: list[T] = []

    def append(self, el: T):
        self.stack.append(el)

    def pop(self) -> T:
        if not self.reverse_stack:
            while self.stack:
                self.reverse_stack.append(self.stack.pop())
        return self.reverse_stack.pop()

    def __bool__(self) -> bool:
        return len(self.stack) > 0 or len(self.reverse_stack) > 0


def test():
    q = Queue[int]()
    q.append(1)
    q.append(2)
    q.append(3)

    result = []
    while q:
        result.append(q.pop())

    assert result == [1, 2, 3]


if __name__ == "__main__":
    test()
