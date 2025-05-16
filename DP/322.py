class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # 存储子问题的解
        counts = [-1] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                counts[coin] = 1  # 肯定只需要一枚该面值的就可以
        for i in range(amount + 1):
            if i == 0:
                continue
            # 尝试每一种 amount，从 1 开始自底向上解题
            temp = []
            if counts[i] != -1:
                temp.append(counts[i])
            for coin in coins:
                index = i - coin
                if index > 0 and counts[index] != -1:
                    temp.append(counts[index] + 1)
            if len(temp) > 0:
                counts[i] = min(temp)
            # print(i, temp, counts)
        return counts[amount]
