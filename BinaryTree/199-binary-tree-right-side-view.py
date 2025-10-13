from typing import List
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 改自 102-binary-tree-level-order-traversal.py
        result = []  # 索引: 层号, 内容: 层里的节点数值
        queue = deque([(0, root)])  # depth, node

        while queue:
            depth, node = queue.popleft()
            if depth == len(result):
                result.append([])
            if node:
                result[depth].append(node.val)
                queue.append((depth+1, node.left))
                queue.append((depth+1, node.right))

        result.pop()
        return list(map(lambda x: x[-1], result))
