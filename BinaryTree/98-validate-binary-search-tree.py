from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def flatten(node: Optional[TreeNode]) -> list[int]:
            # 把二叉树使用中序遍历展平为数组
            result = []
            if node.left:
                result.extend(flatten(node.left))
            result.append(node.val)
            if node.right:
                result.extend(flatten(node.right))
            return result

        flattened = flatten(root)
        # 检查展平后的数组是否有序
        for i in range(len(flattened) - 1):
            if flattened[i] >= flattened[i+1]:
                return False
        return True
