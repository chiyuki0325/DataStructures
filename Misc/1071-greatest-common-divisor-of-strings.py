class Solution:
    # 暴力穷举
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 确保 str2 是比较短的那个
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        max_pfx = ""
        for end in range(1, len(str2) + 1):
            pfx = str2[0:end]
            # 穷举！

            meet2 = True
            end2 = end * 2
            while end2 <= len(str2):
                if str2[end2 - end : end2] != pfx:
                    meet = False
                    break
                end2 += end
            end2 -= end
            meet2 = meet2 and end2 == len(str2)

            meet1 = True
            end1 = end
            while end1 <= len(str1):
                if str1[end1 - end : end1] != pfx:
                    meet = False
                    break
                end1 += end
            end1 -= end
            meet1 = meet1 and end1 == len(str1)

            if meet1 and meet2:
                max_pfx = pfx

        return max_pfx


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 题解做法
        def gcd(a: int, b: int) -> int:
            while b > 0:
                a, b = b, a % b
            return a

        # 设两字符串存在最大公约子串 X，则必然
        # str1 = X + X + X + ... + X = m * X
        # str2 = X + X + ... + X = n * X
        # 所以 str1 + str2 = (m+n) * X
        # 反转亦然

        # 题解证明看不懂 直接背

        if str1 + str2 != str2 + str1:
            return ""

        len_gcd = gcd(*sorted((len(str1), len(str2))))
        return str1[:len_gcd]
