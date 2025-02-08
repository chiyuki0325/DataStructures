class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = length
        state = [[False] * length for _ in range(length)]
        for i in range(length):
            state[i][i] = True
        for j in range(length):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i == 1 or state[i + 1][j - 1]:
                        count += 1
                        state[i][j] = True
        # print(state)
        return count
