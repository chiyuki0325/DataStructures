from typing import List


# 初版，有点快
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def check(mark, grid, x, y):
            # print("check",mark,x,y)
            nonlocal count
            if y >= 0 and x >= 0:
                if len(grid) > y and len(grid[0]) > x:
                    if grid[y][x] == "1":
                        if mark:
                            # print(x,y)
                            count += 1
                        grid[y][x] = "0"
                        check(False, grid, x - 1, y)
                        check(False, grid, x + 1, y)
                        check(False, grid, x, y - 1)
                        check(False, grid, x, y + 1)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                check(True, grid, x, y)
                # print(grid)
        return count


# 优化版，这么快
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        count = 0

        def check(x, y):
            if 0 <= y < height and 0 <= x < width:
                if grid[y][x] == '1':
                    grid[y][x] = '0'
                    # 向四个方向扩散
                    check(x - 1, y)
                    check(x + 1, y)
                    check(x, y - 1)
                    check(x, y + 1)

        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1':
                    count += 1
                    check(x, y)

        return count
