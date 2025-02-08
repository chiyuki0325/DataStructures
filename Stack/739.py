class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        if length == 1:
            return [0]

        result = [0] * length
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                smaller = stack.pop()
                result[smaller] = i - smaller

            stack.append(i)

        return result
