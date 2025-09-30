import heapq
from node import ListNode


class Solution:
    # 严《数据结构 (C)》2.24 题目
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        # 初始化光标为各个链表的头
        cursors: list[ListNode] = [None] * n
        for i in range(n):
            cursors[i] = lists[i]

        head = ListNode(1145)
        cur = head

        while True:
            min_cursor_idx = -1
            for i in range(n):
                if cursors[i]:
                    if min_cursor_idx == -1 or cursors[i].val < cursors[min_cursor_idx].val:
                        min_cursor_idx = i

            if min_cursor_idx != -1:
                # 当前 cursors 里的最小节点已找到
                node = cursors[min_cursor_idx]
                cur.next = node
                cur = cur.next
                # 右移这个光标
                cursors[min_cursor_idx] = cursors[min_cursor_idx].next
            else:
                # 所有光标都已推到头
                break

        return head.next


class SolutionOptimized:
    # 使用“最小堆”优化
    # 拒绝当吊车尾！
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        head = ListNode(1145)
        cur = head

        min_heap = []
        remaining_cursors = 0

        # 遍历所有表头，初始化上述变量
        for i in range(n):
            if lists[i]:
                remaining_cursors += 1
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

        while remaining_cursors:
            # 把当前最小的节点插到 cur 后面
            val, i, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next
            # 右移这个光标
            next_node = node.next
            if next_node:
                heapq.heappush(min_heap, (next_node.val, i, next_node))
            else:
                remaining_cursors -= 1

        return head.next
