import random

class Solution:
    def quicksort(self, nums, k):
        pivot=random.choice(nums)
        lt,gt=[],[]
        for num in nums:
            if num>pivot:
                gt.append(num)
            elif num<pivot:
                lt.append(num)
        
        # print(pivot,lt,gt)
        # [lt][eq][gt]
        len_right_part=len(nums)-len(lt)
        # 右半部分的长度 eq+gt
        if k<=len(gt):
            # [gt]
            return self.quicksort(gt, k)
        elif k>len_right_part:
            # [lt]
            return self.quicksort(lt,k-len_right_part)
        else:
            # [eq]
            return pivot

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return nums[0]
        return self.quicksort(nums,k)
        
