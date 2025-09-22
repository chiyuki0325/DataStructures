class Solution:
    # 简单递归写法
    def decodeString(self, s: str) -> str:
        pos = 0

        def decode_string_part() -> str:
            nonlocal s, pos
            result = ""
            num = 0
            while pos < len(s):
                # 一段子串可能是 abc3[def]ghi
                # 先捋掉数字之前的字母
                while pos < len(s) and s[pos].isalpha():
                    result += s[pos]
                    pos += 1
                # 数字
                while pos < len(s) and s[pos].isdigit():
                    num *= 10
                    num += ord(s[pos])-48
                    pos += 1
                # 括号内的字母，递归，乘以数字
                if pos < len(s) and s[pos] == '[':
                    pos += 1
                    result += num * decode_string_part()
                    num = 0
                if pos < len(s) and s[pos] == ']':
                    pos += 1
                    # print(result, pos)
                    return result
            # print(result, pos)
            return result

        return decode_string_part()


if __name__ == "__main__":
    s = Solution()
    assert s.decodeString("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
