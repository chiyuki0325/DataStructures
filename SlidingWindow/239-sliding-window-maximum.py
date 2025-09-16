from collections import deque
from typing import List


class Solution1:
    # 淘汰版本
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 特殊值
        if k == 1:
            return nums

        # 初始状态，“窗口”是数组中的前k个值，直接用max()计算
        # 此时右侧边界为k-1
        max_val = max(nums[0:k])
        result = [max_val]

        for r in range(k, len(nums)):
            # r 为窗口的新右侧边界，从k开始
            l_val = nums[r-k]
            if l_val == max_val:
                # 之前的最大值被移出窗口
                max_val = max(nums[r-k+1:r+1])
                # 超时点，当窗口过长时很容易超时
            else:
                max_val = max(max_val, nums[r])
            result.append(max_val)

        return result


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 特殊值
        if k == 1:
            return nums

        queue = deque()
        # 规定最左边的元素（0）为最大元素

        # “单调队列”
        def add_to_queue(el: int):
            nonlocal queue
            while len(queue) > 0 and queue[-1] < el:
                queue.pop()
            queue.append(el)
            # e.g. [5,4,2,1], el=3
            # 删除右半部分至 [5,4]
            # 插入 3
            # 作用：大的元素保留，更小的元素无用，删除

        def out_of_window(el: int):
            # el 被移出窗口时调用
            # 如果当前最大的元素是 el，则删除，然后[0]即为第二大的元素
            nonlocal queue
            if queue[0] == el:
                queue.popleft()

        # 初始化
        for i in range(k):
            add_to_queue(nums[i])

        result = [queue[0]]

        for r in range(k, len(nums)):
            out_of_window(nums[r-k])
            add_to_queue(nums[r])
            result.append(queue[0])

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.maxSlidingWindow(
        [1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert s.maxSlidingWindow([5, 3, 4], 1) == [5, 3, 4]
    assert s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
