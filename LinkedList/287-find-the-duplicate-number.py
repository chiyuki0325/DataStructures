class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 看了题解后写出来的
        fast = nums[nums[0]]
        slow = nums[0]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        target = 0
        while target != slow:
            slow = nums[slow]
            target = nums[target]
        return target
