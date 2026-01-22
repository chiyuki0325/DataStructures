from itertools import accumulate


class Solution1:
    # O(n*k)，超出时间限制
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        pfx = list(accumulate(arr))
        base = 0
        max_sum = 0
        min_pfx = 0

        for _ in range(k):
            for i in range(len(pfx)):
                pfx_i = pfx[i] + base
                max_sum = max(max_sum, pfx_i - min_pfx)
                min_pfx = min(min_pfx, pfx_i)
            base += pfx[-1]

        return max_sum % (10**9 + 7)


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        pfx = list(accumulate(arr))

        leftpart_max = 0  # 最大前缀和
        midpart_max = 0  # 最大子数组和
        rightpart_max = 0  # 最大后缀和

        # 计算三个和
        _min_pfx = 0
        for i, pfx_i in enumerate(pfx):
            leftpart_max = max(leftpart_max, pfx_i)
            midpart_max = max(midpart_max, pfx_i - _min_pfx)
            _min_pfx = min(_min_pfx, pfx_i)
        rightpart_max = pfx[-1] - _min_pfx

        if k == 1:
            return midpart_max

        whole = max(pfx[-1], 0)
        # k 个数组拼起来的结果：最大后缀和 + k-2 个整个数组和 + 最大前缀和
        result = max(midpart_max, rightpart_max + whole * (k - 2) + leftpart_max)
        return result % (10**9 + 7)


qwq = Solution().kConcatenationMaxSum
assert qwq([20, -50, 100, -40, 15], 3) == 190
assert qwq([-5, 4, -4, -3, 5, -3], 3) == 5
assert qwq([1, 2], 3) == 9
assert qwq([1, -2, 1], 5) == 2
