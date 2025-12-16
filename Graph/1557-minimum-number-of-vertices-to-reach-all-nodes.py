class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_child = [False] * n

        for u, v in edges:
            is_child[v] = True

        result = []
        for i, v in enumerate(is_child):
            if not v:
                result.append(i)

        return result
