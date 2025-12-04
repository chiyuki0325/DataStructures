class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1  # 总和为 0 时，只有一种情况：一个数字都不选

        for i in range(1, target+1):
            for step in nums:
                if i-step >= 0:
                    dp[i] += dp[i-step]

        return dp[-1]
