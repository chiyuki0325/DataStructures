# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a, b = head, head
        while b and b.next:
            a = a.next
            b = b.next.next

        # 此时a 是中点，b是以巴

        pre = None
        b = None
        while a is not None:
            b = a.next
            a.next = pre
            pre = a
            a = b

        l, r = head, pre

        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
