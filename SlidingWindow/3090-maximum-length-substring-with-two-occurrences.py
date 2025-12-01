class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right = 0, 1  # 左闭右开区间
        rbound = len(s)
        counter = [0] * 26

        # 返回某字符在 counter 里的索引
        def c_idx(char: str) -> int:
            return ord(char) - 97

        counter[c_idx(s[0])] += 1

        max_len = 1

        while right < rbound:
            new_char = s[right]
            new_idx = c_idx(new_char)
            if counter[new_idx] == 2:
                while s[left] != new_char:
                    counter[c_idx(s[left])] -= 1
                    left += 1
                left += 1
                counter[new_idx] -= 1
            counter[new_idx] += 1
            right += 1
            # print(s[left:right])
            max_len = max(right-left, max_len)
        return max_len


if __name__ == "__main__":
    assert Solution().maximumLengthSubstring("bcbbbcba") == 4
    assert Solution().maximumLengthSubstring("eebadadbfa") == 9
    assert Solution().maximumLengthSubstring("eddabbdbc") == 6
