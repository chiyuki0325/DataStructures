import math


class Solution:
    def numSquares(self, n: int) -> int:
        """
        想想怎么递推
        如果 n 是平方数：
        nums[n] = 1
        如果 n 不是平方数:
        nums[n] = min(
            nums[n - 1],
            nums[n - 4],
            nums[n - 9],
            nums[n - 16]...
        ) + 1
        """
        nums = [float("inf")] * (n + 1)

        def is_square(i):
            root = math.isqrt(i)
            return root * root == i

        for i in range(1, n + 1):
            if is_square(i):
                nums[i] = 1
            else:
                root = 1
                while True:
                    last_idx = i - root * root
                    if last_idx < 1:
                        break
                    nums[i] = min(nums[i], nums[last_idx] + 1)
                    root += 1

        return nums[n]


class Solution:
    # 我草，查表怎么这么快，我不活了
    def numSquares(self, n: int) -> int:
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            count = 10001  # 数据范围
            j = 1
            while j * j <= i:
                count = min(count, counts[i - j * j] + 1)
                j += 1
            counts[i] = count
        return counts[n]
