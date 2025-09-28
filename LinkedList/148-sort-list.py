from node import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def split_list(head: ListNode) -> (ListNode, ListNode):
            # 采用快慢指针法把链表分割成两部分
            fast = head.next
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            left, right = head, slow.next
            slow.next=None
            return left, right
            # return[1] 为 None 时代表链表只有一节

        def merge_sorted_lists(head1: ListNode, head2: ListNode) -> ListNode:
            # 合并两个有序列表
            # head1 和 head2 长度为 1 时默认有序
            dummy_head=ListNode(None)
            node1=head1
            node2=head2
            cur=dummy_head
            while node1 or node2:
                if not node1:
                    cur.next=node2
                    node2=node2.next
                elif not node2:
                    cur.next=node1
                    node1=node1.next
                else:
                    if node1.val < node2.val:
                        cur.next=node1
                        node1=node1.next
                    else:
                        cur.next=node2
                        node2=node2.next
                cur=cur.next
            return dummy_head.next


        if head is None or head.next is None:
            return head

        left, right = split_list(head)
        return merge_sorted_lists(self.sortList(left), self.sortList(right))
