class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m==n==1:
            return int(matrix[0][0])
        if m==1 or n==1:
            return 1 if any('1' in row for row in matrix) else 0


        states = [[int(i) for i in row] for row in matrix]
        line = max(max(row) for row in states)
        for i in range(1,m):
            for j in range(1,n):
                if states[i][j]:
                    if states[i-1][j] and states[i][j-1] and states[i-1][j-1]:
                        current_state=min(min(states[i-1][j],states[i][j-1]), states[i-1][j-1])+1
                        # 既然它能跑就不去动它
                        states[i][j]=current_state
                        if current_state>line:
                            line=current_state
        print(states)
        return line*line
