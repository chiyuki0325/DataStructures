from itertools import accumulate


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pfx = list(accumulate(nums))

        """
        要求的 abs(pfx[i] - pfx[j-1]) =
        if pfx[i] > pfx[j-1]:
            pfx[i] - pfx[j-1]
        else:
            pfx[j-1] - pfx[i]
        需要求它的最大值

        在遍历的过程中，pfx[i] 是固定的
        所以需要维护最小和最大两份 pfx[j-1]
        """

        min_pfx = max_pfx = 0
        max_abs_sum = 0

        for i in range(len(nums)):
            max_abs_sum = max(max_abs_sum, pfx[i] - min_pfx, max_pfx - pfx[i])
            min_pfx = min(min_pfx, pfx[i])
            max_pfx = max(max_pfx, pfx[i])

        return max_abs_sum


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 看了题解后的做法，我草，这也行？？？？
        pfx = [0] + list(accumulate(nums))
        return max(pfx) - min(pfx)
