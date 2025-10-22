class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 怎么你文件名字那么长
        # 拆解成两步：找到小于 target 的最后一个元素
        # 和大于 target 的第一个元素

        l = 0
        r = len(nums) - 1
        candidate = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                candidate = mid
                l = mid + 1
            else:
                r = mid - 1

        lbound = candidate

        l = 0
        r = len(nums) - 1
        candidate = len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                candidate = mid
                r = mid - 1
            else:
                l = mid + 1

        rbound = candidate

        if rbound - lbound == 1:
            return [-1, -1]

        return [lbound + 1, rbound - 1]
