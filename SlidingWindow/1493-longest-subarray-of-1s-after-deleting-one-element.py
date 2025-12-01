class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
        # 可以理解成，返回的区间内，最多只能包含一个 0

        left, right = 0, 1  # 左闭右开区间
        zeros = 1 if nums[0] == 0 else 0
        rbound = len(nums)
        max_len = 1

        while right < rbound:
            if nums[right] == 0:
                if zeros == 1:
                    # 不能再增加 0 了
                    while nums[left] != 0:
                        left += 1
                    left += 1
                    zeros -= 1

                zeros += 1

            right += 1
            max_len = max(right - left, max_len)

        return max_len - 1
