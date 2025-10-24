class Solution:
    def climbStairs(self, n: int) -> int:
        methods: list[int] = [0] * max(3, n + 1)
        methods[1] = 1
        methods[2] = 2

        for i in range(3, n + 1):
            methods[i] = methods[i - 1] + methods[i - 2]

        return methods[n]
