class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # 给出的是邻接表

        paths: List[List[int]] = []
        n = len(graph)
        target = n - 1

        def dfs(i, path):
            if i == target:
                paths.append(path.copy())
                return

            for j in graph[i]:
                if j not in path:
                    # 回溯思路，避免复制太多的 path
                    path.append(j)
                    dfs(j, path)
                    path.pop()

        dfs(0, [0])
        return paths
