from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}  # num -> index
        for i in range(len(nums)):
            second = target-nums[i]
            if second in cache:
                return [cache[second], i]
            cache[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
