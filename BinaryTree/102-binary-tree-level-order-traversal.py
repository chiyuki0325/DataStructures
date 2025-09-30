from collections import deque


class Solution1:
    # 刚学 BFS 的时候 以前写的
    # 一坨屎 毫无可读性
    def traverse(self, it: Optional[TreeNode], depth: int):
        if it is None:
            return
        if it.left is not None:
            self.traverse(it.left, depth + 1)
        while len(self.data) <= depth:
            self.data.append([])
        self.data[depth].append(it.val)
        if it.right is not None:
            self.traverse(it.right, depth + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.data = []
        self.traverse(root, 0)
        return self.data


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 参考 101 题 flatten 函数写法，一次写出
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
        return result
