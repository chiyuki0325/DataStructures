class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 问号
        # nlogn
        nums.sort()
        return nums[-k]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序做法，nlogn
        # 改自 heap_sort.py

        def left(i: int) -> int:
            return i * 2 + 1

        def right(i: int) -> int:
            return i * 2 + 2

        def parent(i: int) -> int:
            return (i - 1) // 2

        def swap(a: int, b: int):
            nums[a], nums[b] = nums[b], nums[a]

        def max_child(i: int, bound: int) -> int:
            l = left(i)
            r = right(i)

            if l > bound:
                return -1
            elif r > bound:
                return l
            elif nums[l] > nums[r]:
                return l
            else:
                return r

        def sink_down(i: int, bound: int):
            # 使较小的元素下沉使之恢复堆序性
            while True:
                mc = max_child(i, bound)
                if mc == -1 or nums[mc] <= nums[i]:
                    break
                swap(i, mc)
                i = mc

        # 第一步: 建堆
        n = len(nums)
        start_index = parent(n - 1)
        for i in range(start_index, -1, -1):
            # 自底向上的迭代做法
            sink_down(i, n - 1)

        # 第二步: 出堆（但不删除元素。已被视为出堆的元素即已排序区间）
        for i in range(n - 1, n - 1 - k, -1):
            # i: “堆底”
            swap(0, i)
            sink_down(0, i - 1)

        return nums[-k]
