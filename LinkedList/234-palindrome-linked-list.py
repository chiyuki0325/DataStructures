class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Python 列表耍赖法
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a, b = head, head
        while b and b.next:
            a = a.next
            b = b.next.next

        # 此时a 是中点，b是以巴

        # 翻转后半部分链表
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
