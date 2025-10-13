class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 最大“总路径长度和”:“左子树最大单边路径长度和+节点值+右子树最大单边路径长度和”
        max_path_sum = -float("inf")

        def recur_find_max_single_path(node: TreeNode) -> int:
            # 寻找某节点的最大“单边路径长度和”
            if node == None:
                return 0

            # 递归法找到左右两子树的最大“单边路径长度和”
            l_single_path = recur_find_max_single_path(node.left)
            r_single_path = recur_find_max_single_path(node.right)
            paths = [
                node.val,
                node.val + l_single_path,
                node.val + r_single_path
            ]
            max_single_path = max(paths)

            # 在找的路上，顺便更新最大“总路径长度和”
            nonlocal max_path_sum
            paths.append(node.val + l_single_path + r_single_path)  # 总路径长度和
            max_path_sum = max(max_path_sum, max(paths))

            # 返回
            return max_single_path

        recur_find_max_single_path(root)

        return max_path_sum
