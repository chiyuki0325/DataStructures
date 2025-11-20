class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 动态规划夏季把规划一年不如栈选手灵机一动
        stack = []
        marks = [False] * len(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    lbr = stack.pop()
                    marks[lbr] = True
                    marks[i] = True
        # 这样当每有右括号时，可以把它和对应的左括号一起标记为有效

        # print(" ".join(list(s)))
        # print(" ".join(map(str, map(int, marks))))

        max_len = cur_len = 0
        for i in range(len(s)):
            if marks[i]:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 0

        max_len = max(max_len, cur_len)
        return max_len


if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(")()())"))
