class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        a = headA
        b = headB
        while a is not None and b is not None:
            a = a.next
            b = b.next

        if a is None:
            longer = b
            longer_head = headB
        else:
            longer = a
            longer_head = headA

        # 计算两个链表的长度之差
        length_delta = 0
        while longer is not None:
            longer = longer.next
            length_delta += 1

        # 回到起点，确保 a 和 b 的指针离终点距离相同
        a = headA
        b = headB
        if longer_head == headA:
            for i in range(length_delta):
                a = a.next
        else:
            for i in range(length_delta):
                b = b.next

        while a != b and a is not None and b is not None:
            a = a.next
            b = b.next

        return a
