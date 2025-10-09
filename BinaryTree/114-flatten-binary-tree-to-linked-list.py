from typing import Optional


class Solution:
    # 正经递归版
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root

        def _flatten(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            nonlocal cur
            l = node.left
            r = node.right

            if cur != node:
                cur.right = node
                cur.left = None
                cur = cur.right

            if l:
                _flatten(l)
            if r:
                _flatten(r)

        _flatten(root)


class Solution:
    # 用列表耍赖版
    def flatten(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def insert_nodes(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            l = node.left
            r = node.right

            nodes.append(node)

            if l:
                insert_nodes(l)
            if r:
                insert_nodes(r)

        insert_nodes(root)

        if nodes:
            cur = nodes[0]
            for i in range(1, len(nodes)):
                cur.right = nodes[i]
                cur.left = None
                cur = cur.right
