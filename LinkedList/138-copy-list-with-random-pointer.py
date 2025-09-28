from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution1:
    # 第一次自己写的屎山
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 建立哈希表存储原本节点和新节点的指针
        ori_to_new: dict[Node, Node] = {}
        new_to_ori: dict[Node, Node] = {}

        # 建立链表的深拷贝
        dummy_head = Node(1145)
        node = head
        new_node = dummy_head
        while node:
            new_node.next = Node(node.val)
            new_node = new_node.next
            ori_to_new[node] = new_node
            new_to_ori[new_node] = node
            node = node.next

        # 遍历完毕
        node = dummy_head.next
        while node:
            ori = new_to_ori[node]
            if ori.random:
                node.random = ori_to_new[ori.random]
            node = node.next

        return dummy_head.next


class Solution:
    # 看了题解之后的版本
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 把深拷贝的链表接在原本的链表之后
        # 即可不用哈希表，用 next 指针就可以维护原链表到新链表的关系
        # 极为节约空间
        # 也省去了计算 Node 的哈希的时间

        node = head
        while node:
            node_clone = Node(node.val)
            original_next = node.next
            node.next = node_clone
            node_clone.next = original_next
            node = node.next.next

        # 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> None

        node = head
        while node:
            if node.random:
                # 题解中的这一行简直是天才
                node.next.random = node.random.next
            node = node.next.next

        # 提取所有克隆节点
        dummy_head = Node(1145)
        cur = dummy_head
        node = head
        while node:
            cur.next = node.next
            cur = cur.next
            node = node.next.next

        return dummy_head.next
