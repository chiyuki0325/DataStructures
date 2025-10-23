from random import randint


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 题解做法
        # “快速选择”，类似快速排序的分治做法
        # O(n+n/2+n/4+...)=O(n)

        def swap(a: int, b: int):
            nums[a], nums[b] = nums[b], nums[a]

        def partition(left: int, right: int) -> int:
            # 随机选择一个 pivot 进行粗略选择
            # 把大于它的元素放在左边，小于的放在右边
            # 返回 pivot 排序后的下标
            pivot_idx = randint(left, right)
            pivot = nums[pivot_idx]

            # 题解做法：先把 pivot 单独摘出来
            # 不让它参与交换
            # 这样可以简化做法
            swap(pivot_idx, left)

            l = left + 1
            r = right

            while True:
                # 从左往右找第一个大于等于 pivot 的元素
                while l <= r and nums[l] < pivot:
                    l += 1
                # 从右往左找第一个小于等于 pivot 的元素
                while l <= r and nums[r] > pivot:
                    r -= 1
                if l >= r:
                    break
                swap(l, r)
                l += 1
                r -= 1

            # [ left(pivot) | [<=pivot r] | [l >=pivot] ]
            swap(left, r)

            return r

        n = len(nums)
        target = n - k
        left = 0
        right = n - 1

        while True:
            i = partition(left, right)
            if i > target:
                right = i - 1
            elif i < target:
                left = i + 1
            else:
                return nums[i]
