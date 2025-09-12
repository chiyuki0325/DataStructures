class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list2 or list1
        if list1.val < list2.val:
            _target = list1
            insert = list2
        else:
            _target = list2
            insert = list1

        target = _target
        while target.next is not None:
            while insert is not None and insert.val <= target.next.val:
                backup = target.next
                backup2 = insert.next
                target.next = insert
                insert.next = backup
                insert = backup2
            target = target.next

        target.next = insert

        return _target
