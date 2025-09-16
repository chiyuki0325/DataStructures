from typing import List


class SolutionOld:
    def moveZeroes(self, nums: List[int]) -> None:
        # 特解
        if len(nums) == 1:
            return
        i = 0
        fnz = 0  # first_not_zero
        while fnz < len(nums) and nums[fnz] == 0:
            fnz += 1
        while i < len(nums) and fnz < len(nums):
            if nums[i] == 0:
                fnz = max(i, fnz)
                while fnz < len(nums) and nums[fnz] == 0:
                    fnz += 1
                if fnz<len(nums):
                    # print(i, fnz)
                    nums[i], nums[fnz] = nums[fnz], nums[i]
            i += 1


class Solution:
    # 换一种角度：从“不等于零“来思考
    # 避免跳来跳去
    def moveZeroes(self, nums: List[int]) -> None:
        # 特解
        if len(nums) == 1:
            return
        tail = 0
        for i in range(len(nums)):
            # 每遇到一个非0元素，就把它放到数组的左侧
            # ”不难看出“tail一定小于等于i
            if nums[i] != 0:
                nums[tail] = nums[i]
                tail += 1
        for i in range(tail, len(nums)):
            nums[i] = 0
        # 剩下的肯定都应该放0



if __name__ == "__main__":
    s = Solution()
    i = [0, 1, 0, 3, 12]
    s.moveZeroes(i)
    print(i)
    assert i == [1, 3, 12, 0, 0]
    i = [0]
    s.moveZeroes(i)
    print(i)
    assert i == [0]
    i = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    s.moveZeroes(i)
    print(i)
    assert i == [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
    i = [0, 1]
    s.moveZeroes(i)
    print(i)
    assert i == [1, 0]
    i = [1, 0, 1]
    s.moveZeroes(i)
    print(i)
    assert i == [1, 1, 0]
