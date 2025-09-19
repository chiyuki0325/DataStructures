from typing import List


# 当前光标移动的方位
RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4

# 数据范围是 [-100,100]
# 找一个范围之外的数当作已访问的标记位
MARK = 114


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 初始坐标和方位
        x = 0
        y = 0
        direction = RIGHT
        result = []

        while True:
            result.append(matrix[y][x])
            matrix[y][x] = MARK

            next_x, next_y = self.next_position(x, y, direction)
            if self.is_block(matrix, next_x, next_y, direction):
                direction = self.next_direction(direction)
                next_x, next_y = self.next_position(x, y, direction)
                if self.is_block(matrix, next_x, next_y, direction):
                    return result

            x, y = next_x, next_y

    def next_direction(self, direction: int) -> int:
        # 撞壁拐弯逻辑
        if direction == UP:
            return RIGHT
        else:
            return direction + 1

    def next_position(self, x: int, y: int, direction: int) -> (int, int):
        # 移动逻辑
        if direction == RIGHT:
            return (x + 1, y)
        elif direction == DOWN:
            return (x, y + 1)
        elif direction == LEFT:
            return (x - 1, y)
        else:  # UP
            return (x, y - 1)

    def is_block(self, matrix: List[List[int]], next_x: int, next_y: int, direction: int) -> bool:
        # 撞壁检测逻辑
        return next_y >= len(matrix) or next_x >= len(matrix[0]) or matrix[next_y][next_x] == MARK


if __name__ == "__main__":
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 6, 9, 8, 7, 4, 5]
