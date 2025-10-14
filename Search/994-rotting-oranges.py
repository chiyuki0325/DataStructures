from typing import List
from collections import deque

EMPTY = 0
FRESH = 1
ROTTEN = 2
INFEASIBLE = -1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def is_grid(y, x) -> bool:
            return y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0])

        def gen_tmp_grid() -> List[List[bool]]:
            return [[False] * len(grid[0]) for _ in range(len(grid))]

        max_path = 0  # 某一颗新鲜橘子距离最近的腐烂橘子的最远路径长度
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # 遍历所有格子
                if grid[y][x] == FRESH:
                    # 参考 200-number-of-islands.py
                    # 使用广度优先搜索，搜寻最近的腐烂橘子
                    queue = deque([(y, x, 0)])
                    path = INFEASIBLE

                    # walked 二维数组用于储存走过的格子，避免死循环
                    walked = gen_tmp_grid()
                    walked[y][x] = True

                    while queue:
                        cur_y, cur_x, cur_path = queue.popleft()
                        walked[cur_y][cur_x] = True
                        for _y, _x in [
                            (cur_y-1, cur_x),
                            (cur_y+1, cur_x),
                            (cur_y, cur_x-1),
                            (cur_y, cur_x+1)
                        ]:
                            # 试探上下左右坐标
                            if is_grid(_y, _x) and not walked[_y][_x]:
                                if grid[_y][_x] == FRESH:
                                    queue.append((_y, _x, cur_path+1))
                                elif grid[_y][_x] == ROTTEN:
                                    if path != INFEASIBLE:
                                        path = min(path, cur_path+1)
                                    else:
                                        path = cur_path+1

                    if path == INFEASIBLE:
                        return INFEASIBLE
                    else:
                        # 找到通往腐烂橘子的路线
                        max_path = max(path, max_path)

        return max_path


if __name__ == "__main__":
    s = Solution()
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0
    assert s.orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2
