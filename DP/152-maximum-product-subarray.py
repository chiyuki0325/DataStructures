# 诡计多端的 0 导致不可以维护前缀乘积

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 依然是从暴力穷举上手，先确保结果正确
        # O(N^3)
        max_prod = -float('inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = 1
                for index in range(i, j+1):
                    prod *= nums[index]
                max_prod = max(prod, max_prod)

        return max_prod


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 加上缓存呢（二维数组 / 哈希表）

        # 缓存太大，超出了内存限制
        max_prod = -float('inf')
        cache = {}
        for i in range(len(nums)):
            cache[(i, i)] = nums[i]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (i, j) in cache:
                    max_prod = max(max_prod, cache[(i, j)])
                else:
                    if (i, j-1) in cache:
                        cache[(i, j)] = cache[(i, j-1)] * nums[j]
                        max_prod = max(max_prod, cache[(i, j)])
                    else:
                        raise ValueError()

        return max_prod


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 没招了，看题解了

        # 状态定义：以 i 结尾的最大 / 最小子数组乘积
        # 原因：负负得正。
        # 乘法是很特殊的，之前的最小值，乘以一个很小的负数
        # 就会变成新的最大值
        # 反过来同理

        # 之后涉及到乘法的题，都可以从负负得正的思路去想

        n = len(nums)
        prod_max = [0] * n
        prod_min = [0] * n
        prod_max[0] = prod_min[0] = nums[0]

        for i in range(1, n):
            ni = nums[i]
            prod_max[i] = max(prod_max[i-1] * ni, prod_min[i-1] * ni, ni)
            prod_min[i] = min(prod_max[i-1] * ni, prod_min[i-1] * ni, ni)

        return max(prod_max)
