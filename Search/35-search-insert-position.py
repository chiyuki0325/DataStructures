class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 基础二分查找
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        if target <= nums[l]:
            return l
        else:
            return l + 1
