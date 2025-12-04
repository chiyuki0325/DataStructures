from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        min_sum = [0] * (n+1)

        for j in range(1, n+1):
            cur_min = float('inf')
            for step in range(1, 4):
                if j-step >= 0:
                    cur_min = min(
                        cur_min,
                        min_sum[j-step] + costs[j-1] + step*step
                    )
            min_sum[j] = cur_min

        # print(min_sum)
        return min_sum[-1]


if __name__ == "__main__":
    assert Solution().climbStairs(4, [1, 2, 3, 4]) == 13
