from collections import defaultdict
from typing import List


class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        operation = nums.copy()
        for i in range(1, len(nums)):
            operation[i] += operation[i-1]
        # 生成操作台数组
        # operation: [a1, a1+a2, a1+a2+a3]
        # print(operation)
        count = 0

        for left in range(len(nums)):
            if left > 0:
                to_delete = nums[left-1]
                for i in range(left, len(nums)):
                    operation[i] -= to_delete
                # e.g. left=1
                # 操作前: [a1, a1+a2, a1+a2+a3]
                # 操作后: to_delete=a1, [a1, | a2, a2+a3] (a1被删除)
            for i in range(left, len(nums)):
                if operation[i] == k:
                    # print(left, i)
                    count += 1
        # print(count)
        return count


class Solution2:
    # 优化版 O(n^2)
    def subarraySum(self, nums: List[int], k: int) -> int:
        operation = nums.copy()
        for i in range(1, len(nums)):
            operation[i] += operation[i-1]
        # 生成操作台数组
        # operation: [a1, a1+a2, a1+a2+a3]
        # print(operation)
        count = 0
        minus = 0
        for left in range(len(nums)):
            if left > 0:
                minus += nums[left-1]
            for i in range(left, len(nums)):
                if operation[i]-minus == k:
                    # operation[i]-minus==k
                    # operation[i]==k+minus
                    # print(left, i)
                    count += 1
        # print(count)
        return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # 题解给的
        # 之所以这么设置，是因为可能有一个 a1+...+an 就等于 k
        # 此时 += prefix_sum_count[...] 会少一种可能
        # 而如果对结果直接 +1 的话，没 a1+...+an=k 的情况就会多算一种

        prefix_sum = 0
        count = 0

        for i in range(len(nums)):
            # 当前 prefix_sum = a1+a2...+ai
            prefix_sum += nums[i]
            count += prefix_sum_count[prefix_sum-k]
            # prefix_sum-k
            # = a1+a2+...+ai-k
            # 如果 prefix_sum_count 中存在这个数
            # 说明 a1+a2+...+an = a1+a2+...+ai-k
            # k = a(n+1)+...+ai
            prefix_sum_count[prefix_sum] += 1

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([], 1) == 0
    assert s.subarraySum([1], 0) == 0
