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
