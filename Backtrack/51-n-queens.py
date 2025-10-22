from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 这道题不能递推了...!

        # 根据题解的做法，把状态压缩成一维数组
        # .Q..
        # ...Q
        # Q...
        # ..Q.
        # -> [2,4,1,3]
        # 会省很多脑子

        # 状态定义: row 和 col 均为 [1,n]

        def output(state: List[int]) -> List[str]:
            # 把状态变成打印格式
            return ["." * (col - 1) + "Q" + "." * (n - col) for col in state]

        def is_available(row: int, col: int, state: List[int]) -> bool:
            # 判断某个格子是否可以落子
            for i in range(row - 1):
                # 如果判断第三行，就要找 1~2 行有没有，也就是 index 0~1

                # 检查纵向
                if state[i] == col:
                    return False

                # 检查对角
                # 行数之差等于列数之差
                if row - 1 - i == abs(col - state[i]):
                    return False

            return True

        results: List[List[str]] = []

        def dfs(row: int, col: int, state: List[int]):
            state[row - 1] = col
            if row == n:
                results.append(output(state))
                return

            for c in range(1, n + 1):
                if is_available(row + 1, c, state):
                    dfs(row + 1, c, state)

            # 死亡回溯，“还原现场”
            state[row - 1] = -1

        for c in range(1, n + 1):
            dfs(1, c, [-1] * n)

        return results


if __name__ == "__main__":
    print(Solution().solveNQueens(4))
