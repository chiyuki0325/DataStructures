from typing import Optional
from node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        pre = None
        b = None

        while a is not None:
            b = a.next
            a.next = pre
            pre = a
            a = b
        return pre
