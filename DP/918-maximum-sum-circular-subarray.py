from itertools import accumulate
from collections import deque


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        buf = nums*2
        prefix_sum = list(accumulate(buf))

        max_ans = float('-inf')

        # 存储窗口内最小前缀和的索引
        min_l_sums = deque()

        for i in range(n*2):
            if min_l_sums and i - min_l_sums[0] > n:
                # 移除失效元素
                min_l_sums.popleft()

            if min_l_sums:
                max_ans = max(
                    max_ans, prefix_sum[i] - prefix_sum[min_l_sums[0]])
            else:
                max_ans = max(max_ans, prefix_sum[i])

            # 维护单调增队列
            while min_l_sums and prefix_sum[min_l_sums[-1]] >= prefix_sum[i]:
                min_l_sums.pop()

            min_l_sums.append(i)

        return max_ans


if __name__ == "__main__":
    assert Solution().maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert Solution().maxSubarraySumCircular([5, -3, 5]) == 10
    assert Solution().maxSubarraySumCircular([3, -2, 2, -3]) == 3
    assert Solution().maxSubarraySumCircular([3, 1, 3, 2, 6]) == 15
