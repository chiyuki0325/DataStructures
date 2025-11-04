from typing import List


class Solution1:
    # 暴力穷举法，不能通过测试
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        def dfs(index: int, plus: int) -> bool:
            if plus == 0:
                return False
            if index >= len(nums)-1:
                return True
            next_index = index+plus
            if next_index >= len(nums)-1:
                return True
            return any(dfs(next_index, n) for n in range(nums[next_index]+1))

        return any(dfs(0, n) for n in range(nums[0]+1))


class Solution:
    # 题解方法：维护最右可到达距离
    def canJump(self, nums: List[int]) -> bool:
        max_distance = nums[0]
        for i, n in enumerate(nums):
            if i > max_distance:
                # 当前距离与“可到达”的条件冲突
                return False
            max_distance = max(max_distance, i + n)
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False
    assert s.canJump([0]) == True
    assert s.canJump([2, 0, 0]) == True
