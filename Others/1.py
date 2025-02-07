class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}  # num -> idx
        for i in range(0, len(nums)):
            if not nums[i] in cache:
                cache[nums[i]] = i
            left = target - nums[i]
            if left in cache:
                if i != cache[left]:
                    return [i, cache[left]]
