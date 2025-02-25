class Solution:
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]):
        # 由于传入的left和right一定是sortList后的结果，所以一定有序
        # 逐个插入后，即为排序好的合并链表
        new_head = ListNode(0)
        cur = new_head
        while left and right:
            if left.val < right.val:
                # 左进
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        # 左边或右边有一个是None时循环结束
        # 此时另外一边肯定只有一个节点
        if left is not None:
            cur.next = left
        else:
            cur.next = right
        return new_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head  # 只有一个
        # 分割成左链表和右链表
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left, right = head, slow.next
        slow.next = None
        # 从中间断开
        return self.merge(self.sortList(left), self.sortList(right))
