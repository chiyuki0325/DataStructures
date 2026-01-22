class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp: list[int] = [0] * (high + 1)

        dp[0] = 1  # 最重要的一行，但我暂时理解不了。。。

        for i in range(1, high + 1):
            i0 = i - zero
            i1 = i - one

            dp[i] = (dp[i0] if i0 >= 0 else 0) + (dp[i1] if i1 >= 0 else 0)

        count = 0
        for i in range(low, high + 1):
            count += dp[i]

        return count % (10**9 + 7)


assert Solution().countGoodStrings(3, 3, 1, 1) == 8
assert Solution().countGoodStrings(2, 3, 1, 2) == 5
