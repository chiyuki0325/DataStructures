from typing import List


class SolutionBruteForce:
    # 暴力解法，枚举出所有递增序列
    # 时间复杂度过高，不可通过
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        next_start = 0
        next_start_changed = False
        while next_start < len(temperatures)-1:
            next_start_changed = False
            days = []
            for i in range(next_start, len(temperatures)):
                if not days or temperatures[i] > temperatures[days[-1]]:
                    days.append(i)
                elif not next_start_changed:
                    next_start = i
                    next_start_changed = True
            if not next_start_changed:
                next_start = i
            for j in range(1, len(days)):
                result[days[j-1]] = days[j]-days[j-1]
        return result


class Solution:
    # 看了题解后的版本
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            # 确保栈中元素单调递增
            while stack and temperatures[stack[-1]] < v:
                # 边弹栈边计算差值，这样可以覆盖所有低谷部分
                prev_i = stack.pop()
                result[prev_i] = i-prev_i
            stack.append(i)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1, 1, 4, 2, 1, 1, 0, 0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
