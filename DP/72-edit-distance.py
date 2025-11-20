def print_2d_list(mtx):
    for line in mtx:
        print(line)
    print()


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word2)+1):
            dp[0][i] = i
        for j in range(len(word1)+1):
            dp[j][0] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # print_2d_list(dp)
                    # 往左上：编辑一个字母
                    # 往上/左：插入/删除一个字母
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1

        #print_2d_list(dp)
        return dp[-1][-1]


if __name__ == "__main__":
    assert Solution().minDistance("horse", "ros") == 3
