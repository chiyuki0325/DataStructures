from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked(arr: list) -> Optional[ListNode]:
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    node = head

    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next

    return head


def linked_to_arr(head: ListNode) -> list:
    result = []
    node = head
    while head:
        result.append(node.val)
        node = node.next
    return result
