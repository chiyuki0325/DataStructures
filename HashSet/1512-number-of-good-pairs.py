class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # “枚举右，维护左”
        result = 0
        count = defaultdict(int)
        for i in nums:
            result += count[i]
            count[i] += 1
        return result
