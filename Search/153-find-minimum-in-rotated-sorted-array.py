class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 这道题应该放在 33 前面的
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
