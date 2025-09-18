from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []

        for [st, en] in intervals:
            if len(result) != 0 and st <= result[-1][1]:
                result[-1][1] = max(result[-1][1], en)
            else:
                result.append([st, en])

        # print(result)
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[4, 7], [1, 4]]) == [[1, 7]]
