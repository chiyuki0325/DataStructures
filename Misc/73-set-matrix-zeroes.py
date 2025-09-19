from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 能通过 OJ 测试的暴力解法
        # 利用 Python 的灵活性，尝试使用 None 当作占位符
        # 遍历两次二维数组，很慢
        # C++ 做不到系列
        for m in range(len(matrix)):
            line = matrix[m]
            for n in range(len(line)):
                el = matrix[m][n]
                if el == 0:
                    for _m in range(len(matrix)):
                        el = matrix[_m][n]
                        if el != 0:
                            matrix[_m][n] = None
                    for _n in range(len(line)):
                        el = matrix[m][_n]
                        if el != 0:
                            matrix[m][_n] = None

        # 把 None 替换为 0
        for m in range(len(matrix)):
            line = matrix[m]
            for n in range(len(line)):
                el = matrix[m][n]
                if el is None:
                    matrix[m][n] = 0
        # print(matrix)


if __name__ == "__main__":
    s = Solution()
    mtx = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(mtx)
    assert mtx == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    mtx = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(mtx)
    assert mtx == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
