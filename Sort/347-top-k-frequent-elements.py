from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 题解做法，桶排序，O(n)

        # 首先统计各个元素的出现频率
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        max_freq = max(frequency.values())

        # 把出现次数相同的元素放到同一个桶中
        buckets: List[List[int]] = [[] for _ in range(max_freq + 1)]
        for num, freq in frequency.items():
            buckets[freq].append(num)

        result = []
        for bucket in reversed(buckets):
            result.extend(bucket)
            if len(result) == k:
                return result
