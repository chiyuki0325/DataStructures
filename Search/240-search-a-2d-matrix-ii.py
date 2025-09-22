from typing import List, Optional


class SolutionFailed:
    # 此为翻车版本，我注意力起飞了导致的
    # 根本跑不通
    # 勿看
    # 请直接看下方 Solution 类
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 一些斜向访问用的工具函数

        height = len(matrix)
        width = len(matrix[0])

        def diagonal_count_rows() -> int:
            # matrix 总行数
            return height + width - 1

        def diagonal_row_length(row: int) -> int:
            # 获取某个斜行的长度
            if width <= height:
                # 宽度 <= 高度（瘦高矩阵）
                if row < width:
                    return row + 1
                elif row < height:
                    return width
                else:
                    return width - (row - height + 1)
            else:
                # 宽度 > 高度（扁平矩阵）
                if row < height:
                    return row + 1
                elif row < width:
                    return height
                else:
                    return height - (row - width + 1)

        def diagonal_access(row: int, index: int) -> Optional[int]:
            # row: 从左上到右下第几斜行 (0 开始)
            # index: 从左下到右上的个数 (0 开始)
            if row < height:
                y = row
                x = 0
            else:
                y = height - 1
                x = row - height + 1
            # 此时 y x 为这一斜行的起始坐标
            y -= index
            x += index
            if y < height and x < width:
                return matrix[y][x]
            else:
                return None

        # 这个版本已经足够快了，再优化就要牺牲可读性，或者预先计算所有坐标了

        def test():
            for i in range(diagonal_count_rows()):
                print(f"第 {i} 斜行")
                for j in range(diagonal_row_length(i)):
                    print(diagonal_access(i, j), end=" ")
                print()

        # 1  4  7  11 15
        # 2  5  8  12 19
        # 3  6  9  16 22
        # 10 13 14 17 24

        # =>

        #     1
        #    2 4
        #   3 5 7
        # 10 6 8 11
        # 13 9 12 15
        #  14 16 19
        #    17 22
        #     24

        # 不难看出，把二维数组倾斜过来
        # 每一斜行都是有序的
        # 且每一斜行的起始和终止元素都比上一行大
        # 现在正式开始搜索算法

        test()

        for row in range(diagonal_count_rows()):
            l = 0
            r = diagonal_row_length(row) - 1
            l_el = diagonal_access(row, l)
            r_el = diagonal_access(row, r)
            if l_el <= r_el:
                if l_el <= target <= r_el:
                    # 在这一行内进行二分查找
                    while l <= r:
                        mid = (l+r) // 2
                        mid_el = diagonal_access(row, mid)
                        if mid_el < target:
                            l = mid+1
                        elif mid_el > target:
                            r = mid-1
                        else:
                            return True
            else:
                if r_el <= target <= l_el:
                    # 复制粘贴
                    while l <= r:
                        mid = (l+r) // 2
                        mid_el = diagonal_access(row, mid)
                        if mid_el > target:
                            l = mid+1
                        elif mid_el < target:
                            r = mid-1
                        else:
                            return True

        # Game Over
        return False


class SolutionBinarySearch:
    # 应该能跑，吧。
    # ：能跑。
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        found_range = False

        for row in range(height):
            # 每一行都是升序
            if matrix[row][0] <= target <= matrix[row][-1]:
                # 在这一行内开展二分查找
                l = 0
                r = width-1
                while l <= r:
                    mid = (l+r)//2
                    mid_el = matrix[row][mid]
                    if mid_el == target:
                        return True
                    elif mid_el < target:
                        l = mid+1
                    else:  # mid_el>target:
                        r = mid-1

        return False


class Solution:
    # 看了题解之后的版本，被一下点通。
    # ：怎么比上个版本还慢啊！
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix 类似于二叉搜索树
        # 从右上节点开始移动，如果元素较大就往左移动，元素较小就往下移动
        y = 0
        x = len(matrix[0]) - 1
        while x >= 0 and y < len(matrix):
            el = matrix[y][x]
            if el > target:
                x -= 1
            elif el < target:
                y += 1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [
                          10, 13, 14, 17, 24]], 5) == True
    assert s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [
                          10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5) == True
    assert s.searchMatrix([[-1], [-1]], 0) == False
    assert s.searchMatrix([[1, 4], [2, 5]], 4) == True
    assert s.searchMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [
                          16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 15) == True
    assert s.searchMatrix([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19], [
                          12, 14, 16, 18, 20], [21, 22, 23, 24, 25]], 8) == True
