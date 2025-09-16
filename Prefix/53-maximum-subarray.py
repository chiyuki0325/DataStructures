from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 看了题解后的版本

        # 特解
        if len(nums) == 1:
            return nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            """
            想想“单调队列”
            sum[i] = nums[i] + sum[i-1]
            如果相加之后 sum[i] 还没有 nums[i] 大
            那么前面的全不要，只留 nums[i]

            然后进行空间优化：sum 数组可以优化成一个变量 result
            """

            """
            if nums[i-1]+nums[i] < nums[i]:
                # start=i
                pass
            else:
                nums[i] += nums[i-1]
            """

            # 消元，移项
            if nums[i-1] >= 0:
                nums[i] += nums[i-1]

            result = max(result, nums[i])

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([1, 2]) == 3
