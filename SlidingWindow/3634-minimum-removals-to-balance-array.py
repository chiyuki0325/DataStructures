class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # 题解做法
        nums.sort()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            while nums[left] * k < nums[right]:
                left += 1
            max_len = max(max_len, right-left)

        return len(nums)-max_len-1
