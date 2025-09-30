class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        new_left = self.invertTree(root.left)
        new_right = self.invertTree(root.right)
        root.left = new_right
        root.right = new_left
        return root
