class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 哈基表耍赖法
        a = head
        memory = set()
        while a and a.next:
            memory.add(a)
            a = a.next
            if a in memory:
                return True
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针法
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
