from node import ListNode


class Solution:
    # 简单方法，由 24 题的解法修改而来
    # 编译器优化完 0 秒跑完，那还说啥了
    # O(2n)，空间复杂度 O(k)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        virtual_head = ListNode(None)
        virtual_head.next = head

        group_prev = virtual_head

        group = [None] * k
        looping = True

        while looping:
            # 简单地模拟整个过程即可
            # 只是检查 None 比较麻烦而已

            node = group_prev

            # 把下面的 k 个节点加入 group
            for i in range(k):
                group[i] = node.next
                node = node.next
                if node is None:
                    looping = False
                    break
            if not looping:
                break

            group_next = node.next

            node = group_prev

            # 翻转当前组
            # group_prev -> [group] -> group_next

            for cursor in reversed(group):
                node.next = cursor
                node = cursor

            node.next = group_next
            group_prev = group[0]

        return virtual_head.next


class Solution:
    # 复杂方法，O(1) 空间复杂度，复杂在检测 None 比较烦人

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        virtual_head = ListNode(None)
        virtual_head.next = head

        group_prev = virtual_head

        looping = True

        while looping:

            # 派一个指针去前方打探敌情
            # 如果到头了就 looping=False
            pioneer = group_prev
            for i in range(k):
                pioneer = pioneer.next
                if pioneer is None:
                    looping = False
                    break
            if not looping:
                break

            # 变量名乱了套了
            # 也不准备后续读了
            # 还是上一种好读

            # group_prev -> [要插入的 node] -> neck -> [... 操作完的区域] -> tail -> group_next
            # 逻辑大概是这么个逻辑

            group_next = pioneer.next

            node = group_prev.next.next
            tail = group_prev.next
            neck = tail

            while node != group_next:
                # 备份原本的 next
                next_node = node.next
                # 把 node 薅过来插在 group_prev 和 neck 中间
                group_prev.next = node
                node.next = neck
                # neck 跟进，往左移动一格
                neck = node
                # 寻找下一个受害者
                node = next_node

            tail.next = group_next

            # 移动 group_prev
            group_prev = tail

        return virtual_head.next
