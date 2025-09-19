from typing import List

MARK = 2002
MARK_CMP = 1000


class Solution:
    # 灵感来源于 189-rotate-array

    def rotate_position(self, y: int, x: int, size: int) -> (int, int):
        # 返回旋转后的坐标 (y, x)
        return (x, size-y-1)

    def next_position(self, y: int, x: int, size: int) -> (int, int):
        if x == size - 1:
            return (y+1, 0)
        else:
            return (y, x+1)

    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        initial_y = 0
        initial_x = 0
        while initial_y < size:
            if matrix[initial_y][initial_x] < MARK_CMP:
                x = initial_x
                y = initial_y
                force = True
                tmp = matrix[y][x]
                tmp2 = matrix[y][x]
                while (x != initial_x or y != initial_y) or force:
                    next_y, next_x = self.rotate_position(y, x, size)
                    if next_y == y and next_x == x:
                        break
                    tmp2 = matrix[next_y][next_x]
                    matrix[next_y][next_x] = tmp + MARK
                    tmp = tmp2
                    y, x = next_y, next_x
                    force = False
                # print()
                # for line in matrix:
                #    print(line)
            initial_y, initial_x = self.next_position(
                initial_y, initial_x, size)
        x = 0
        y = 0
        while y < size:
            if matrix[y][x] > MARK_CMP:
                matrix[y][x] -= MARK
            y, x = self.next_position(y, x, size)


if __name__ == "__main__":
    s = Solution()
    mtx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(mtx)
    assert mtx == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
