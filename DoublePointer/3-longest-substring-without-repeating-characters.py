class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 针对特殊情况直接返回
        if len(s) < 2:
            return len(s)

        # 记录某个字符上次出现过的坐标
        last_positions = [-1] * 128

        longest = 1
        left_position = 0

        for right_position in range(len(s)):
            # 左右都闭
            ch = ord(s[right_position])
            if left_position <= last_positions[ch]:
                # 左边界更新，往右移动，确保区间内不出现重复字符
                left_position = last_positions[ch] + 1
            last_positions[ch] = right_position
            longest = max(longest, right_position - left_position + 1)

        # print(last_positions)
        return longest
