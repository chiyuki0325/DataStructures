from polyfunctional_heap import MaxHeap, MinHeap
# 为什么 Python 标准库里只有最大堆没有最小堆
# 干脆一起搓一遍吧


class MedianFinder:
    # 看了题解后的做法
    # 一开始本来想着用 BST 做
    # 结果是堆

    def __init__(self):
        # 初始化一个最小堆和一个最大堆
        # 一个放在左侧，一个放在右侧
        # [ [l_max_heap max] [min r_min_heap] ]
        self.l_max_heap = MaxHeap()
        self.r_min_heap = MinHeap()

    def addNum(self, num: int) -> None:
        lh = self.l_max_heap
        rh = self.r_min_heap

        if not rh.size() or num <= rh.peek():
            lh.push(num)
            if lh.size() > rh.size() + 1:
                rh.push(lh.pop())
        else:
            rh.push(num)
            if rh.size() > lh.size():
                lh.push(rh.pop())

    def findMedian(self) -> float:
        lh = self.l_max_heap
        rh = self.r_min_heap

        if lh.size() == rh.size():
            return (lh.peek()+rh.peek())/2
        else:
            return float(lh.peek())
