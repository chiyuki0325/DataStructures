from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        excluded = n+114514

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = excluded

        def replace(i):
            nonlocal nums
            target = nums[i]-1
            if target > n:
                return
            if nums[target] != nums[i]:
                nums[target], nums[i] = nums[i], nums[target]
                replace(i)

        for i in range(n):
            if nums[i] != excluded:
                replace(i)

        # print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1


if __name__ == "__main__":
    s = Solution()
    assert s.firstMissingPositive([3, 4, 1, -1]) == 2
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([1, 2, 0]) == 3

    qwq = []
    for i in range(100000, 0, -1):
        qwq.append(i)
    s = Solution()
    print(s.firstMissingPositive(qwq))
