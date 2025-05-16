class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 针对特殊情况处理
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]

        longest = s[0]
        lbound = 0
        ubound = len(s) - 1

        # 初始化“最长的回文字符串”数组
        strings = []
        for i in range(len(s)):
            strings.append([])
            for j in range(len(s)):
                strings[i].append("")

        def debug():
            for i in range(len(s)):
                print(strings[i])

        # 先初始化长度为 1 的
        for i in range(len(s)):
            strings[i][i] = s[i]

        # 再初始化长度为 2 的
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                strings[i][i + 1] = s[i] * 2
                if len(strings[i][i + 1]) > len(longest):
                    longest = strings[i][i + 1]

        # 按顺序遍历整个字符串
        for k in range(1, len(s)):
            for i in range(len(s) - k):
                j = i + k
                # 坐标为 [i,j] 左闭右闭

                # 两边
                if s[i] == s[j]:
                    # 确保上个子问题有解
                    if strings[i + 1][j - 1] != "":
                        new = s[i] + strings[i + 1][j - 1] + s[j]
                        strings[i][j] = new
                        if len(new) > len(longest):
                            longest = new

        # debug()
        return longest
