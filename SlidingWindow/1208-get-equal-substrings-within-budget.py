class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        diffs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        # diffs[i] 为第 i 个字符的价格

        # 初始化左闭右开区间
        left = 0
        right = 0
        max_length = 0
        cost = 0

        while right < len(diffs):
            cost += diffs[right]
            right += 1

            while cost > max_cost:
                cost -= diffs[left]
                left += 1

            max_length = max(max_length, right - left)

        return max_length

if __name__ == "__main__":
    assert Solution().equalSubstring("abcd", "bcdf", 3) == 3
    assert Solution().equalSubstring("abcd", "cdef", 3) == 1
