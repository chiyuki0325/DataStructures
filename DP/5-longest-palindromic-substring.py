class Solution:
    # 动态规划
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # 特解
        if n < 2:
            return s

        max_substring = s[0]
        max_len = 1

        # 状态定义: s[i:j+1] (i 到 j 的闭区间) 是否为回文字符串
        dp = [[False] * n for _ in range(n)]

        # [i, i] 必然是回文
        for i in range(n):
            dp[i][i] = True

        # 遍历方式：从 2 开始的字符串长度
        for substr_len in range(2, n+1):
            for l in range(n-substr_len+1):
                r = l+substr_len-1
                # l 和 r 已经确定

                if s[l] == s[r]:
                    if substr_len == 2:
                        dp[l][r] = True
                    else:
                        dp[l][r] = dp[l+1][r-1]

                if dp[l][r] and substr_len > max_len:
                    max_len = substr_len
                    max_substring = s[l:r+1]

        return max_substring


"""
这是最直观、最符合动态规划“由小到大”思想的方法。
思路：我们先计算所有长度为 1 的子串，然后是长度为 2 的，接着是 3 的... 直到整个字符串的长度 n。

如何实现？
    外层循环遍历子串的长度 L（从 1 到 n）。
    内层循环遍历子串的起始索引 i。
    通过 i 和 L 可以计算出子串的结束索引 j = i + L - 1。
"""
