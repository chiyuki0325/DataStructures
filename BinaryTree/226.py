# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        new_left = self.invertTree(root.left)
        new_right = self.invertTree(root.right)
        root.left = new_right
        root.right = new_left
        return root
