class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        left = 0
        center = k

        # 结果数组
        avgs = [-1] * len(nums)

        d = k * 2 + 1
        if k > len(nums) or d > len(nums):
            return avgs

        # 长度为 d 的子数组的部分和
        partial_sum = sum(nums[:d])
        avgs[center] = partial_sum // d

        for right in range(d, len(nums)):
            center += 1
            partial_sum += nums[right]
            partial_sum -= nums[left]
            avgs[center] = partial_sum // d
            left += 1
        return avgs
