class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针法 2: 严书做法
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast is None or fast.next is None or fast.next.next is None:
            # 链表无环
            return None

        # fast 和 slow 已在圈里，再转一圈拿到圈的长度
        fast = fast.next
        length = 1
        while fast != slow:
            fast = fast.next
            length += 1

        fast = head
        slow = head

        for _ in range(length):
            fast = fast.next

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
