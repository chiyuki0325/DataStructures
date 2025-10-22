class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 先做的 II，那显然是 I 更简单
        for line in matrix:
            if line[0] <= target <= line[-1]:
                l = 0
                r = len(line) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if line[mid] < target:
                        l = mid + 1
                    elif line[mid] > target:
                        r = mid - 1
                    else:
                        return True
                return False
        return False
