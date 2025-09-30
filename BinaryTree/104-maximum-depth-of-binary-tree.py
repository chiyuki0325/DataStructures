class Solution:
    # 参考 94 题
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(1, root)]
        while stack:
            depth, node = stack.pop()
            if node is None:
                continue
            if isinstance(node, TreeNode):
                max_depth = max(max_depth, depth)
                stack.append((depth+1, node.right))
                stack.append((depth+1, node.left))
        return max_depth
