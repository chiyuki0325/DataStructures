from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        partial_sum = sum(nums[:k])
        partial_set = defaultdict(int)
        for i in nums[:k]:
            partial_set[i] += 1
        partial_distinct_sum = partial_sum if len(partial_set) == k else 0
        left = 0

        for right in range(k, len(nums)):
            nr = nums[right]
            nl = nums[left]
            partial_sum += nr
            partial_sum -= nl

            partial_set[nr] += 1
            partial_set[nl] -= 1
            if partial_set[nl] == 0:
                del partial_set[nl]

            partial_distinct_sum = max(partial_distinct_sum, partial_sum if len(partial_set) == k else 0)

            left += 1

        return partial_distinct_sum
