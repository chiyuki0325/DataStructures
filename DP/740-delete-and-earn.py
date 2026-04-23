from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 官方题解
        max_num = max(nums)
        sums = [0] * (max_num + 1)
        for i in nums:
            sums[i] += i
        gain = [0] * (max_num+1)
        for n in range(1, max_num+1):
            gain[n] = max(gain[n - 1], gain[n - 2] + sums[n])
        return gain[-1]




if __name__ == "__main__":
    assert Solution().deleteAndEarn([3, 4, 2]) == 6
    assert Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
