class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        visited = [False] * len(is_connected)

        def dfs(i):
            visited[i] = True
            for j in range(len(is_connected)):
                if is_connected[i][j] and not visited[j]:
                    dfs(j)

        count = 0
        for i, i_vis in enumerate(visited):
            if not i_vis:
                dfs(i)
                count += 1

        return count


if __name__ == "__main__":
    assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
