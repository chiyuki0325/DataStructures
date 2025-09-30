class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0  # 最大直径

        # 学着竞赛代码的写法把函数名定义成了 dfs
        # 其实是想不出函数名了
        def dfs(depth: int, node: Optional[TreeNode]) -> int:
            # 获取左节点和右节点的最大深度，并返回
            # 顺便更新 max_d

            nonlocal max_d
            if not node:
                # 终点，递转归
                return depth-1

            left_depth = dfs(depth+1, node.left)
            right_depth = dfs(depth+1, node.right)
            # 路径长度计算：左边深度 + 右边深度 - 2 * 当前深度
            # 按照本题场景不需要 + 1
            d = left_depth+right_depth-2*depth
            max_d = max(max_d, d)
            return max(left_depth, right_depth)

        dfs(1, root)
        return max_d
