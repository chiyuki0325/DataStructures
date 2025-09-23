from node import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建占位头节点方便操作
        virtual_head = ListNode(None)
        virtual_head.next = head

        cursor = virtual_head

        while True:
            # 简单地模拟整个过程即可
            # 只是检查None比较麻烦而已
            pre_node = cursor
            first = cursor.next
            if first is None:
                break
            second = first.next
            if second is None:
                break
            next_node = second.next
            pre_node.next = second
            second.next = first
            first.next = next_node
            cursor = first

        return virtual_head.next
