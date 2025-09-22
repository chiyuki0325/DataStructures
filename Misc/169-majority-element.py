class Solution:
    # 面向结果编程，一次通过
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
