class Solution:
    def lengthOfLongestSubsequence(self, nums: list[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(path_start, _target) -> int:
            # 优化方案：用递归栈的长度代替 path_len 参数，空间复杂度下降一个次方
            if _target == 0:
                return 0  # 递归栈栈顶
            if _target < 0 or path_start == n:
                return -1145
            return max(
                dfs(path_start + 1, _target),
                dfs(path_start + 1, _target - nums[path_start]) + 1,
            )

        return max(dfs(0, target), -1)


class Solution:
    def lengthOfLongestSubsequence(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = [[0] + [-1145] * target for _ in range(n + 1)]
        # dp[path_start][_target] = path_len

        for path_start, cost in enumerate(nums):
            for i in range(target + 1):
                if i >= cost:
                    dp[path_start + 1][i] = max(
                        dp[path_start][i], dp[path_start][i - cost] + 1
                    )
                else:
                    # 防止越界
                    dp[path_start + 1][i] = dp[path_start][i]

        return max(dp[-1][-1], -1)
