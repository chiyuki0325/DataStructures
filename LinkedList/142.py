class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        memory = set()
        while a and a.next:
            memory.add(a)
            a = a.next
            if a in memory:
                return a
        return None
