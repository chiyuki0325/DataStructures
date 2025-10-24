from typing import Optional, Callable


class Heap:
    def __init__(self, comparator: Callable[[int, int], bool]):
        self.arr = []
        self.comparator = comparator

    def left(self, i: int) -> int:
        return i*2+1

    def right(self, i: int) -> int:
        return i*2+2

    def parent(self, i: int) -> int:
        return (i-1)//2

    def size(self) -> int:
        return len(self.arr)

    def swap(self, a: int, b: int):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def peek(self) -> Optional[int]:
        return self.arr[0] if self.arr else None

    def float_up(self, i: Optional[int] = None):
        if i is None:
            i = self.size()-1
        while True:
            pa = self.parent(i)
            if pa < 0 or self.comparator(self.arr[pa], self.arr[i]):
                break
            self.swap(i, pa)
            i = pa

    def push(self, n: int):
        self.arr.append(n)
        self.float_up(self.size()-1)

    def child_to_swap(self, i: int) -> Optional[int]:
        l = self.left(i)
        r = self.right(i)

        if l >= self.size():
            return None
        elif r >= self.size():
            return l
        else:
            return l if self.comparator(self.arr[l], self.arr[r]) else r

    def sink_down(self, i: int):
        while True:
            mc = self.child_to_swap(i)
            if mc is None or not self.comparator(self.arr[mc], self.arr[i]):
                break
            self.swap(i, mc)
            i = mc

    def pop(self) -> Optional[int]:
        if not self.arr:
            return None

        self.swap(0, self.size() - 1)
        result = self.arr.pop()
        self.sink_down(0)
        return result


def MaxHeap(): return Heap(lambda a, b: a >= b)
def MinHeap(): return Heap(lambda a, b: a <= b)
