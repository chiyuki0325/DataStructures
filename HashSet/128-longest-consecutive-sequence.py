from typing import List


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        max_length = 1
        nums = set(nums)
        nums2 = set()
        for num in nums:
            if num not in nums2:
                tmp = num+1
                length = 1
                while tmp in nums:
                    tmp += 1
                    length += 1
                    nums2.add(tmp)
                nums2.add(num)
                max_length = max(length, max_length)
        return max_length


class Solution:
    # 题解版，确保进入循环时一定是序列中最大的元素，去重更加高效
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        longest_length = 1
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                length = 1
                while num+1 in nums:
                    num += 1
                    length += 1
                longest_length = max(length, longest_length)
        return longest_length


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([1, 0, 1, 2]) == 3
    # 特例
    assert s.longestConsecutive([]) == 0
