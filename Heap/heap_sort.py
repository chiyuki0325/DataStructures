from typing import Annotated, Optional


# 改自 max_heap.py


def heap_sort(nums: list[int]):
    Index = Annotated[int, "索引", "越界则为 -1"]

    def left(i: Index) -> Index:
        return i * 2 + 1

    def right(i: Index) -> Index:
        return i * 2 + 2

    def parent(i: Index) -> Index:
        return (i - 1) // 2

    def swap(a: Index, b: Index):
        nums[a], nums[b] = nums[b], nums[a]

    def max_child(i: Index, bound: Index = -1) -> Index:
        l = left(i)
        r = right(i)

        if bound == -1:
            bound = len(nums) - 1
        l_out = l > bound
        r_out = r > bound
        if l_out and r_out:
            return -1
        elif l_out:
            return r
        elif r_out:
            return l

        if nums[l] > nums[r]:
            return l
        else:
            return r

    def sink_down(i: Index, bound: Index = -1):
        # 使较小的元素下沉使之恢复堆序性
        while True:
            mc = max_child(i, bound)
            if mc == -1 or nums[mc] < nums[i]:
                break
            swap(i, mc)
            i = mc

    # 第一步: 建堆
    start_index = parent(len(nums) - 1)
    for i in range(start_index, -1, -1):
        # 自底向上的迭代做法
        sink_down(i)

    # 第二步: 出堆（但不删除元素。已被视为出堆的元素即已排序区间）
    for i in range(len(nums) - 1, 0, -1):
        # i: “堆底”
        swap(0, i)
        sink_down(0, i - 1)

    return nums


if __name__ == "__main__":
    heap = heap_sort([1, 5, 7, 8, 2, 9, 4, 3, 10, 6, 13, 14, 12, 11])
    print(heap)
