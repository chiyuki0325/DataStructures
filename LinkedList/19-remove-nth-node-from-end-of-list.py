from typing import Optional
from node import ListNode
from node import build_linked, linked_to_arr


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 经典龟兔赛跑

        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next

        # 特例处理：n==len(head)，删除头结点
        if fast is None:
            return head.next

        slow_pre = slow
        while fast:
            fast = fast.next
            slow_pre = slow
            slow = slow.next
        # slow 即为要删除的节点
        slow_pre.next = slow.next
        return head


if __name__ == "__main__":
    s = Solution()
    assert linked_to_arr(s.removeNthFromEnd(
        build_linked([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
