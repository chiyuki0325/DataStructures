class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substring = ""
        lbound = -1
        rbound = len(s)

        for center in range(len(s)):
            l = center
            r = center

            # 首先解决奇偶长度的问题
            while l-1 > lbound and s[l-1] == s[l]:
                l -= 1
            while r+1 < rbound and s[r+1] == s[r]:
                r += 1

            # 之后慢慢往两侧扩散
            while True:
                new_l = l-1
                new_r = r+1
                if new_l > lbound and new_r < rbound and s[new_l] == s[new_r]:
                    l = new_l
                    r = new_r
                else:
                    break

            if len(max_substring) < r-l+1:
                max_substring = s[l:r+1]

        return max_substring
