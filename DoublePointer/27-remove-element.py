class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        index = 0
        last_equals_index = 0

        while index < len(nums):
            # print(index, last_equals_index)
            while index < len(nums) and nums[index] == val:
                # print(index)
                count += 1
                index += 1
            if index == len(nums):
                break
            nums[last_equals_index] = nums[index]
            index += 1
            last_equals_index += 1
        # print(nums)
        return len(nums) - count
