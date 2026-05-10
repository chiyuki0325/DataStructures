class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        assert len(nums) == len(colors)
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(2, n+2):
            if colors[i-2] != colors[i-3]:
                # 颜色不同，可以拿相邻的
                dp[i] = max(dp[i-2]+nums[i-2], dp[i-1]+nums[i-2])
            else:
                dp[i] = max(dp[i-2]+nums[i-2], dp[i-1])
        return dp[-1]


if __name__ == "__main__":
    assert Solution().rob([1, 4, 3, 5], [1, 1, 2, 2]) == 9
    assert Solution().rob(nums=[3, 1, 2, 4], colors=[2, 3, 2, 2]) == 8
