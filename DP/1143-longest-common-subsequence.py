class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        h = len(text1)
        w = len(text2)
        dp = [[0] * w for _ in range(h)]

        def get(y, x):
            if y < 0 or x < 0:
                return 0
            else:
                return dp[y][x]

        for y in range(h):
            for x in range(w):
                if text1[y] == text2[x]:
                    dp[y][x] = get(y-1, x-1)+1
                else:
                    dp[y][x] = max(get(y-1, x), get(y, x-1))

        return dp[-1][-1]
