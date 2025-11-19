class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 特解
        if m == 1 or n == 1:
            return 1

        # m 为高，n 为宽
        paths = [[0] * n for _ in range(m)]
        paths[0][1] = paths[1][0] = 1

        def in_grid(y, x):
            # 此题目只有向右和向下两种移动方法
            # 因此不用判断右边界和下边界
            return y >= 0 and x >= 0

        for y in range(m):
            for x in range(n):
                if (y, x) in [(0, 0), (0, 1), (1, 0)]:
                    continue
                p = 0
                if in_grid(y-1, x):
                    p += paths[y-1][x]
                if in_grid(y, x-1):
                    p += paths[y][x-1]
                paths[y][x] = p

        return paths[-1][-1]
