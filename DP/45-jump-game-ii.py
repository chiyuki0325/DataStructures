from typing import List
from functools import cache

inf = float('inf')


class Solution1:
    def jump(self, nums: List[int]) -> int:
        # 暴力解法
        min_count = len(nums)
        target = len(nums)-1

        @cache
        def dfs(pos: int, jumped_count: int):
            nonlocal min_count
            if pos == target:
                min_count = min(min_count, jumped_count)
                return
            if jumped_count >= min_count:
                return
            for step in range(1, nums[pos] + 1):
                dfs(pos+step, jumped_count+1)

        dfs(0, 0)
        return min_count


class Solution2:
    def jump(self, nums: List[int]) -> int:
        # 动态？规划？

        n = len(nums)
        dp = [inf] * n
        dp[0] = 0

        for pos in range(n):
            rbound = min(pos+nums[pos]+1, n)
            for new_pos in range(pos+1, rbound):
                dp[new_pos] = min(dp[new_pos], dp[pos]+1)

        return dp[-1]


if __name__ == "__main__":
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
