class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_pre = [1] * len(nums)
        nums_suf = list(nums_pre)
        result = [0] * len(nums)
        for i in range(1, len(nums)):
            nums_pre[i] = nums_pre[i - 1] * nums[i - 1]

            i2 = -1 - i
            nums_suf[i2] = nums_suf[i2 + 1] * nums[i2 + 1]

        for i in range(len(nums)):
            result[i] = nums_pre[i] * nums_suf[i]
        return result
