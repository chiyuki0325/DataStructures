class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        gain = [0] * (len(nums) + 1)
        gain[1] = nums[0]  # 前 1 栋房子里，只能偷第一栋
        gain[2] = max(nums[0], nums[1])  # 前 2 栋房子里，只能二选一

        for n in range(1, len(nums)):
            gain[n] = max(gain[n - 1], gain[n - 2] + nums[n - 1])

        max1 = gain[len(nums)-1]

        gain[1] = 0  # 第二波遍历时不偷第一间
        gain[2] = nums[1]

        for n in range(2, len(nums)+1):
            gain[n] = max(gain[n - 1], gain[n - 2] + nums[n - 1])

        max2 = gain[len(nums)]

        return max(max1, max2)
