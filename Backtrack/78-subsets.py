from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 采用“状态树”的思想，依旧递归
        end = len(nums)
        result = []

        def _subsets(path: List[int], depth: int):
            if depth == end:
                result.append(path)
                return
            _subsets(path, depth+1)
            _subsets(path + [nums[depth]], depth+1)

        _subsets([], 0)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
