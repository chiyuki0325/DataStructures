class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 哈基表耍赖法
        a = head
        memory = set()
        while a and a.next:
            memory.add(a)
            a = a.next
            if a in memory:
                return a
        return None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针法
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                target = head
                while target != slow:
                    target = target.next
                    slow = slow.next
                return target
        return None
