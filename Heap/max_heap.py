from typing import Annotated, Optional

Index = Annotated[int, "索引", "越界则为 -1"]


class MaxHeap:
    def __init__(self, nums: list[int]):
        self.arr = nums[:]
        start_index = self.parent(len(self.arr) - 1)
        for i in range(start_index, -1, -1):
            # 自底向上的迭代做法
            self.sink_down(i)

    # 元素访问相关方法

    def left(self, i: Index) -> Index:
        return i * 2 + 1

    def right(self, i: Index) -> Index:
        return i * 2 + 2

    def parent(self, i: Index) -> Index:
        return (i - 1) // 2

    def max(self, i: Index) -> Optional[int]:
        return self.arr[0] if self.arr else None

    def swap(self, a: Index, b: Index):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def max_child(self, i: Index) -> Index:
        l = self.left(i)
        r = self.right(i)

        bound = len(self.arr) - 1
        l_out = l > bound
        r_out = r > bound
        if l_out and r_out:
            return -1
        elif l_out:
            return r
        elif r_out:
            return l

        if self.arr[l] > self.arr[r]:
            return l
        else:
            return r

    # 堆基本操作

    def sink_down(self, i: Index):
        # 使较小的元素下沉使之恢复堆序性
        while True:
            mc = self.max_child(i)
            if mc == -1 or self.arr[mc] < self.arr[i]:
                break
            self.swap(i, mc)
            i = mc

    def float_up(self, i: Index = -1):
        # 使过大的元素上浮使之恢复堆序性
        if i == -1:
            i = len(self.arr) - 1
        while True:
            pa = self.parent(i)
            if pa < 0 or self.arr[pa] >= self.arr[i]:
                break
            self.swap(pa, i)
            i = pa

    def push(self, n: int):
        # 把元素添加到堆中
        self.arr.append(n)
        self.float_up(len(self.arr) - 1)

    def pop(self) -> Optional[int]:
        # 把堆顶的最大元素移除

        # 操作流程:
        # 1、把堆顶元素与可以安全移除的最后一个元素交换
        # 2、使移过来的堆顶元素下沉

        if not self.arr:
            return None

        self.swap(0, len(self.arr) - 1)
        result = self.arr.pop()
        self.sink_down(0)
        return result


if __name__ == "__main__":
    heap = MaxHeap([1, 5, 7, 8, 2, 9, 4, 3, 10, 6, 13, 14, 12, 11])
    print(heap.arr)
