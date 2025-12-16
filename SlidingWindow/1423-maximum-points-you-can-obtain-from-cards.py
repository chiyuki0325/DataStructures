class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        # 从左/右边拿走 k 张卡牌，行为可以理解为从中间留下 n-k 张卡牌
        # 也就是题目标签里所说的“滑动窗口”

        # max_pick_sum = sum - remaining_sum

        n = len(nums)
        remaining_sum = sum(nums[:(n-k)])
        min_remaining_sum = remaining_sum

        left = 0
        for right in range(n-k, n):
            remaining_sum += nums[right]
            remaining_sum -= nums[left]
            min_remaining_sum = min(min_remaining_sum, remaining_sum)

            left += 1

        return sum(nums) - min_remaining_sum
