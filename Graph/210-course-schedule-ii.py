from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses

        for v, u in prerequisites:
            adj[u].append(v)
            in_deg[v] += 1

        toposort = []

        queue = deque(i for i, d in enumerate(in_deg) if d == 0)

        while queue:
            i = queue.popleft()
            toposort.append(i)

            for j in adj[i]:
                in_deg[j] -= 1
                if in_deg[j] == 0:
                    queue.append(j)

        if len(toposort) != numCourses:
            return []

        return toposort
