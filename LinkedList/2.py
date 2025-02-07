class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_head = ListNode(0)
        a = l1
        b = l2
        c = new_head
        while True:
            leftval = a.val if a else 0
            rightval = b.val if b else 0
            c.val += leftval + rightval
            a = a.next if a else None
            b = b.next if b else None
            if c.val > 9:
                c.val -= 10
                c.next = ListNode(1)

            if a is None and b is None:
                return new_head

            if c.next is None:
                c.next = ListNode(0)
            c = c.next
