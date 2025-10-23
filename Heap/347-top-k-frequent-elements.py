from collections import defaultdict
import heapq
from typing import List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogk)

        # 首先统计各个元素的出现频率
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        # 之后就是普通 top-k 问题
        # 这次直接用 Python 自带的堆了
        # 不然时间稀烂

        heap: List[Tuple[Int, Int]] = []
        counter = 0

        for num, freq in frequency.items():
            if counter < k:
                heapq.heappush(heap, (freq, num))
                counter += 1
            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))

        return [num for (freq, num) in heap]
