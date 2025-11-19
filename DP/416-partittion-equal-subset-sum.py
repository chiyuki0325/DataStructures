class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 特解
        s = sum(nums)
        if s % 2 == 1:
            return False

        # 之前想了好久都没想到，遂采用题解做法
        # 使用“选或不选”思路

        @cache
        def dfs(right: int, partial_sum: int) -> bool:
            if right == 0:
                # 到头了
                return partial_sum == nums[0]
            if partial_sum < 0:
                return False
            return dfs(right-1, partial_sum) or dfs(right-1, partial_sum-nums[right])

        return dfs(len(nums)-1, s / 2)
