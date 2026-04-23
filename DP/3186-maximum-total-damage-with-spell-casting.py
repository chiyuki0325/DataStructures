from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        dmg = sorted(cnt.keys())
        n = len(dmg)

        total = [0]*(n+1)
        j = 0

        for i, x in enumerate(dmg):
            # 找到 dmg[j] < x-2 的最大值
            while dmg[j] < x-2:
                j += 1
            total[i+1] = max(total[i], total[j]+x*cnt[x])
        return total[-1]


if __name__ == "__main__":
    assert Solution().maximumTotalDamage([1, 1, 3, 4]) == 6
    assert Solution().maximumTotalDamage([7, 1, 6, 6]) == 13
