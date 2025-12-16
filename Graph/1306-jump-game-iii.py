from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        n = len(arr)
        vis = [False] * n

        while queue:
            i = queue.pop()
            vis[i] = True

            if arr[i] == 0:
                return True

            for j in [i+arr[i], i-arr[i]]:
                if j >= 0 and j < n and not vis[j]:
                    queue.append(j)

        return False


if __name__ == "__main__":
    assert Solution().canReach([4, 2, 3, 0, 3, 1, 2], 5) == True
