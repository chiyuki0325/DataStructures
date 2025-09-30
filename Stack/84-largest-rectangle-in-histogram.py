from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 参考“每日温度”题目，但把顺序颠倒过来，左右扫两遍取交集

        # 修复神秘 bug
        heights.append(0)
        heights.insert(0, 0)

        next_lower_bar = [0] * len(heights)
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                prev_i = stack.pop()
                next_lower_bar[prev_i] = i-prev_i
            stack.append(i)

        prev_lower_bar = [0]*len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            v = heights[i]
            while stack and heights[stack[-1]] > v:
                prev_i = stack.pop()
                prev_lower_bar[prev_i] = prev_i-i
            stack.append(i)

        # print(heights, next_lower_bar, prev_lower_bar)

        result = 0
        for height, width_r, width_l in zip(heights, next_lower_bar, prev_lower_bar):
            s = height * (width_r + width_l - 1)
            result = max(result, s)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
