from typing import List


class Solution:
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        tmp = 0
        while l < r:
            tmp = nums[r]
            nums[r] = nums[l]
            nums[l] = tmp
            l += 1
            r -= 1

    def search(self, nums: List[int], target: int) -> int:
        # 找到违反单调的点
        # 第二版：更改为二分查找，严格遵循时间复杂度要求
        rotate = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        rotate = l

        # 用之前灵神那招来旋转数组
        self.reverse(nums, 0, rotate - 1)
        self.reverse(nums, rotate, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

        # print(rotate, nums)

        # 接下来就是普通二分查找
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return (mid + rotate) % len(nums)

        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([5, 1, 3], 5) == 0
