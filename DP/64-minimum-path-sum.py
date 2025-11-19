class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def in_grid(y, x):
            # 此题目只有向右和向下两种移动方法
            # 因此不用判断右边界和下边界
            return y >= 0 and x >= 0

        m = len(grid)
        n = len(grid[0])

        for y in range(m):
            for x in range(n):
                if in_grid(y-1, x) and in_grid(y, x-1):
                    grid[y][x] += min(grid[y-1][x], grid[y][x-1])
                elif in_grid(y, x-1):
                    grid[y][x] += grid[y][x-1]
                elif in_grid(y-1, x):
                    grid[y][x] += grid[y-1][x]

        return grid[-1][-1]
