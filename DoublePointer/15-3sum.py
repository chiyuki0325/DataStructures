class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 看了题解后的版本
        nums = sorted(nums)
        # result=set()
        result = []
        first = 0
        while nums[first] <= 0 and first < len(nums)-2:  # 写<0的话[0,0,0]会不过
            second = first+1
            third = len(nums)-1
            while second < third:
                three_sum = nums[first]+nums[second]+nums[third]
                if three_sum > 0:
                    third -= 1
                elif three_sum < 0:
                    second += 1
                else:
                    # result.add((nums[first],nums[second],nums[third]))
                    result.append([nums[first], nums[second], nums[third]])
                    # break
                    # 重点：剔除重复项
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    while second < third and nums[third] == nums[third-1]:
                        third -= 1
                    second += 1
                    third -= 1
            first += 1
        # return list(map(lambda x: list(x), result))
        return result
