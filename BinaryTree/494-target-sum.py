class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 暴力
        n = len(nums)

        @cache
        def dfs(right: int, partial_sum: int):
            if right == n:
                return int(partial_sum == target)
            else:
                return dfs(right+1, partial_sum+nums[right])+dfs(right+1, partial_sum-nums[right])

        return dfs(0, 0)
