from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def recur(path: List[int], path_sum: int, start: int):
            if path_sum == target:
                results.append(path[:])
                return

            if path_sum > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                recur(path + [num], path_sum + num, i)

        recur([], 0, 0)
        return results
