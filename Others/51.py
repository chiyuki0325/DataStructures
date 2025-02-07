class Solution:
    def is_valid(self, row, col, queens):
        for row2 in range(row):
            # 列
            if queens[row2] == col:
                return False
            # 斜对角线
            d = abs(row - row2)
            d2 = abs(col - queens[row2])
            if d == d2:
                return False
        return True

    def output(self, queens, n):
        return list(map(lambda col: "." * col + "Q" + "." * (n - col - 1), queens))

    def solveNQueens(self, n) -> List[List[str]]:
        queens = [-1] * n  # row->col
        solutions = []

        def solve_row(row):
            if row == n:
                solutions.append(self.output(queens, n))
                return

            for col in range(n):
                if self.is_valid(row, col, queens):
                    queens[row] = col
                    solve_row(row + 1)

        solve_row(0)
        return solutions
