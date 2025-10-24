class Solution:
    def rob(self, nums: List[int]) -> int:
        # 你是一个专业的小偷
        # 专业在哪儿了

        # 依旧递推法
        # 状态：在前 n 栋房子里可以偷到的**最高**金额
        gain = [0] * (len(nums) + 1)
        gain[1] = nums[0]  # 前 1 栋房子里，只能偷第一栋
        if len(nums) > 1:
            gain[2] = max(nums[0], nums[1])  # 前 2 栋房子里，只能二选一

        for n in range(1, len(nums) + 1):
            gain[n] = max(gain[n - 1], gain[n - 2] + nums[n - 1])

        return gain[len(nums)]
