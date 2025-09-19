from typing import List


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        # 简单计数法，遍历两次数组
        # O(2*len(nums))
        count = [0, 0, 0]
        for i in nums:
            count[i] += 1
        index = 0
        for i in range(len(count)):
            c = count[i]
            for j in range(c):
                nums[index] = i
                index += 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        # 交换法，遍历两次数组
        # 遍历第一次数组把所有 2 放到右边
        # O(count(0)+2*count(1))
        two_start = len(nums)-1
        while two_start >= 0 and nums[two_start] == 2:
            two_start -= 1
        cursor = 0
        while cursor < two_start:
            if nums[cursor] == 2:
                nums[cursor], nums[two_start] = nums[two_start], nums[cursor]
                while nums[two_start] == 2:
                    two_start -= 1
            cursor += 1

        # 遍历第二次把所有 0 放到左边
        zero_end = 0
        while zero_end < len(nums) and nums[zero_end] == 0:
            zero_end += 1
        while cursor > zero_end:
            if nums[cursor] == 0:
                nums[cursor], nums[zero_end] = nums[zero_end], nums[cursor]
                while nums[zero_end] == 0:
                    zero_end += 1
            cursor -= 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 双指针法
        # 遍历一次数组
        # O(count(0)+count(1))
        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]

        left = 0
        right = len(nums) - 1

        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
                i += 1
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
            else:
                i += 1


if __name__ == "__main__":
    s = Solution()
    a = [2, 0, 2, 1, 1, 0]
    s.sortColors(a)
    assert a == [0, 0, 1, 1, 2, 2]
    a = [0]
    s.sortColors(a)
    assert a == [0]
    import random
    a = [random.choice([0, 1, 2]) for _ in range(20)]
    s.sortColors(a)
    print(a)
    assert a == sorted(a)
