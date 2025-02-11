class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        moneys = [0] * (len(nums) + 1)
        moneys[1] = nums[0]
        for i in range(2, len(nums) + 1):
            moneys[i] = max(moneys[i - 1], moneys[i - 2] + nums[i - 1])
        return moneys[-1]
