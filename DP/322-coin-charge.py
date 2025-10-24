class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        inf = float("inf")

        # 凑出 n 元所需的最小硬币个数
        counts: List[int] = [inf] * (amount+1)
        for coin in coins:
            if coin < len(counts):
                counts[coin] = 1

        def get(i: int) -> int:
            if i > 0:
                return counts[i]
            else:
                return inf

        for amt in range(1, amount+1):
            count = get(amt)
            for coin in coins:
                count = min(count, get(amt-coin)+1)
            counts[amt] = count

        return counts[amount] if counts[amount] != inf else -1
