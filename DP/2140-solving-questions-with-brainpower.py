class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # question[i] = [points, cd]

        # AI 教的技巧：从后往前看，倒序 DP
        # 打家劫舍里限制是双向的
        # 而这道题是单向的，cd 只影响未来不影响过去

        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n - 1, -1, -1):
            [points, cd] = questions[i]
            j = i+cd+1
            if j >= n:
                gain = points
            else:
                gain = dp[j]+points
            dp[i] = max(
                dp[i+1],
                gain
            )

        return dp[0]


if __name__ == "__main__":
    assert Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
    assert Solution().mostPoints([[21, 2], [1, 2], [12, 5], [7, 2], [35, 3], [32, 2], [80, 2], [91, 5], [92, 3], [27, 3], [19, 1], [37, 3], [85, 2], [33, 4], [25, 1], [91, 4], [44, 3], [93, 3], [65, 4], [82, 3], [85, 5], [81, 3], [29, 2], [
        25, 1], [74, 2], [58, 1], [85, 1], [84, 2], [27, 2], [47, 5], [48, 4], [3, 2], [44, 3], [60, 5], [19, 2], [9, 4], [29, 5], [15, 3], [1, 3], [60, 2], [63, 3], [79, 3], [19, 1], [7, 1], [35, 1], [55, 4], [1, 4], [41, 1], [58, 5]]) == 781
