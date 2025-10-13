from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = preorder[0]
        left_length = inorder.index(root)
        l = self.buildTree(preorder[1: 1+left_length], inorder[:left_length])
        r = self.buildTree(preorder[1+left_length:], inorder[1+left_length:])
        return TreeNode(root, l, r)
