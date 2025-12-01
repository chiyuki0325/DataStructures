class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 傻逼写法，不用动脑子版
        # 首先左右翻转整棵右子树

        def dfs_reverse(node: Optional[TreeNode]):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            dfs_reverse(node.left)
            dfs_reverse(node.right)

        dfs_reverse(root.right)

        # 之后检查左右子树是否相等即可
        def dfs_check(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is not None:
                return False
            if node2 is None and node1 is not None:
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return dfs_check(node1.left, node2.left) and dfs_check(node1.right, node2.right)
            else:
                return True

        return dfs_check(root.left, root.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 长脑子版，边走边检查，提前返回
        def dfs_check(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is not None:
                return False
            if node2 is None and node1 is not None:
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return dfs_check(node1.left, node2.right) and dfs_check(node1.right, node2.left)
            else:
                return True

        # 不对我草，怎么直接用不带脑子版的 dfs_check 改一下就行了
        # 要长脑子了

        return dfs_check(root.left, root.right)
