class MinStack:
    def __init__(self):
        self.stk = []  # list[tuple[int,int]]

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.stk.append((val, val))
            return
        topmin = self.getMin()
        if val < topmin:
            self.stk.append((val, val))
        else:
            self.stk.append((val, topmin))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
