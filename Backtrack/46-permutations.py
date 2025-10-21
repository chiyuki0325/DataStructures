from typing import List


class Solution:
    # 回溯版块的第一题，递归的后劲还没过，因此用递归做出
    # 用取末尾元素 / 列表切片来写应该更快，但这个做法更直观

    def rotate(self, nums: List[int]):
        # [1,2,3]->[2,3,1]
        tmp = nums[0]
        for i in range(len(nums)-1):
            nums[i] = nums[i+1]
        nums[-1] = tmp

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            result.extend(
                list(map(lambda x: [nums[0]] + x, self.permute(nums[1:])))
            )
            self.rotate(nums)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
