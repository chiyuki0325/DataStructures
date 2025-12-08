from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        counter = defaultdict(int)  # 子数组中每个数字的计数
        for i in range(k):
            counter[nums[i]] += 1
        partial_sum = sum(nums[:k])
        max_sum = partial_sum if len(counter) >= m else 0

        left = 0
        for right in range(k, len(nums)):
            nr, nl = nums[right], nums[left]
            partial_sum += nr
            partial_sum -= nl
            counter[nr] += 1
            counter[nl] -= 1
            if counter[nl] == 0:
                counter.pop(nl)
            max_sum_new = partial_sum if len(counter) >= m else 0
            max_sum = max(max_sum, max_sum_new)
            left += 1

        return max_sum
