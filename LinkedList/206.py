# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
