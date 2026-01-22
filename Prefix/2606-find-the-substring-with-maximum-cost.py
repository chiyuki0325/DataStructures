class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # 构建“字符->价值”映射
        price = {}
        for i in range(97, 123):
            c = chr(i)
            price[c] = i - 96
        for i, c in enumerate(chars):
            price[c] = vals[i]

        # 计算前缀和
        pfx = []
        for c in s:
            last_pfx = pfx[-1] if pfx else 0
            pfx.append(last_pfx + price[c])

        # 采用单调思想解决问题
        max_subarr = 0
        min_pfx = 0

        for i in range(len(pfx)):
            max_subarr = max(max_subarr, pfx[i] - min_pfx)
            min_pfx = min(min_pfx, pfx[i])

        return max_subarr


assert Solution().maximumCostSubstring("adaa", "d", [-1000]) == 2
assert Solution().maximumCostSubstring("abc", "abc", [-1, -1, -1]) == 0
