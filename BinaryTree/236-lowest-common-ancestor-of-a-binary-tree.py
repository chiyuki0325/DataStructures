class Solution:
    # 20251013 更清晰的版本
    def find_path(self, node: TreeNode, p: TreeNode) -> list[TreeNode]:
        # 通过递归方式整理出一条从根节点到指定节点的路径
        if node == p:
            return [node]
        l = None
        r = None
        if node.left:
            l = self.find_path(node.left, p)
        if node.right:
            r = self.find_path(node.right, p)
        if l:
            return [node, *l]
        if r:
            return [node, *r]
        return []

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 找路
        p_path = self.find_path(root, p)
        q_path = self.find_path(root, q)
        min_length = min(len(p_path), len(q_path))
        # 找出共同祖先
        i = 0
        while i < min_length and p_path[i] == q_path[i]:
            i += 1
        return p_path[i-1]
