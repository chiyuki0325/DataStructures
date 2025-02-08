class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = head
        memory = set()
        while a and a.next:
            memory.add(a)
            a = a.next
            if a in memory:
                return True
        return False
