from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # 简单粗暴法：把边列表转为邻接表
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        vis = [False] * n

        def dfs(i) -> bool:
            if i == destination:
                return True

            vis[i] = True

            for j in adj[i]:
                if not vis[j]:
                    if dfs(j):
                        return True

            return False

        return dfs(source)
