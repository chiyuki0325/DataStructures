class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 只能靠背题了

        # 寻找“较小数”
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # 寻找“较大数”
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i],nums[j]=nums[j],nums[i]
        
        def reverse(nums, l, r):
            while l<r:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            
        reverse(nums, i+1, len(nums)-1)



