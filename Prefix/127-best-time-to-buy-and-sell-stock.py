# 本质是寻找某两个价格之间最大的差（后-前）

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 尝试暴力枚举，验证思路是否正确
        # O(n^2)
        result = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                result = max(result, prices[j]-prices[i])

        return result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 优化版：预先计算好第 i 个价格之后的最大值
        # O(2n) = O(n)
        max_price_after = [prices[-1]] * len(prices)
        for i in range(len(prices)-2, -1, -1):
            max_price_after[i] = max(max_price_after[i+1], prices[i+1])

        result = 0
        for i in range(len(prices)):
            result = max(result, max_price_after[i] - prices[i])

        return result


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 题解方法，时间复杂度 O(n)，空间复杂度 O(1)
        # 其实是我想复杂了
        cost, profit = float('inf'), 0

        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)

        return profit
