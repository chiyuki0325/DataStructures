from typing import List


class Solution1:
    # 题解法
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        tmp = 0
        while l < r:
            tmp = nums[r]
            nums[r] = nums[l]
            nums[l] = tmp
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)


class Solution:
    # 一种更快的循环做法
    """
    1 2 3 4 5 6 7  1
    1 2 3 1 5 6 7  4
    1 2 3 1 5 6 4  7
    1 2 7 1 5 3 4  6
    1 6 7 1 5 3 4  2
    1 6 7 1 2 3 4  5
    5 6 7 1 2 3 4  1
    """

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        count = 0
        start_index = 0

        while count < len(nums):
            index = start_index
            tmp = nums[start_index]
            while True:
                next_index = (index + k) % len(nums)
                tmp, nums[next_index] = nums[next_index], tmp
                index = next_index
                count += 1

                if index == start_index:
                    break
                # print(nums)
            start_index += 1


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(a, 3)
    print(a)
    assert a == [5, 6, 7, 1, 2, 3, 4]
    a = [-1, -100, 3, 99]
    s.rotate(a, 2)
    print(a)
    assert a == [3, 99, -1, -100]
