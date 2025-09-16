from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 前缀乘积
        # 时间复杂度 O(3n) == O(n)

        l = len(nums)
        prefix = nums.copy()
        suffix = nums.copy()
        result = [1]*l

        for i in range(1, l):
            prefix[i] *= prefix[i-1]
            j = l-i-1
            suffix[j] *= suffix[j+1]

        for i in range(l):
            if i > 0:
                result[i] *= prefix[i-1]
            if i < l-1:
                result[i] *= suffix[i+1]

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
