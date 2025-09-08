class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.height = 0

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"

    def update_height(self):
        if self.left is None and self.right is None:
            # 叶子节点高度为 0
            self.height = 0
        else:
            l = self.left.height if self.left else -1
            r = self.right.height if self.right else -1
            self.height = max(l, r)+1

    @property
    def balance_factor(self) -> int:
        l = self.left.height if self.left else -1
        r = self.right.height if self.right else -1
        return l - r


class AVLTree:
    def __init__(self):
        self.root: TreeNode | None = None

    @staticmethod
    def right_rotate(unbalanced_node: TreeNode) -> TreeNode:
        # 最简单的右旋情况
        #   3 -> unbalanced_node
        #  2  -> left_child
        # 1
        left_child = unbalanced_node.left

        # 复杂的右旋情况: left_child.right 有内容
        #   3 -> unbalanced_node
        #  2  -> left_child
        # 1 4 -> grand_child (要被移走)
        grand_child = left_child.right
        unbalanced_node.left = grand_child
        # 右子节点被移走

        left_child.right = unbalanced_node

        # update_height 需要自底向上进行
        # 而旋转之后 unbalanced_node 在下面
        unbalanced_node.update_height()
        left_child.update_height()
        return left_child

    @staticmethod
    def left_rotate(unbalanced_node: TreeNode) -> TreeNode:
        # 左旋，与右旋相同
        right_child = unbalanced_node.right
        grand_child = right_child.left
        unbalanced_node.right = grand_child
        right_child.left = unbalanced_node
        unbalanced_node.update_height()
        right_child.update_height()
        return right_child

    @staticmethod
    def left_right_rotate(unbalanced_node: TreeNode) -> TreeNode:
        # 更复杂的右旋情况：
        #   3 -> unbalanced_node
        #  1  -> left_child
        #   2
        left_child = unbalanced_node.left

        # 先对 left_child 做一次左旋操作
        # 把 grand_child 转到左边去，使方向一致
        unbalanced_node.left = AVLTree.left_rotate(left_child)

        #   3 -> unbalanced_node
        #  2  -> left
        # 1     (和 right_rotate 下所给例子一致)
        # 可以进行右旋了
        return AVLTree.right_rotate(unbalanced_node)

    @staticmethod
    def right_left_rotate(unbalanced_node: TreeNode) -> TreeNode:
        # 更复杂的左旋情况，同上
        right_child = unbalanced_node.right
        unbalanced_node.right = AVLTree.right_rotate(right_child)
        return AVLTree.left_rotate(unbalanced_node)

    @staticmethod
    def rotate(node: TreeNode) -> TreeNode:
        # balance_factor = l.h - r.h
        if node.balance_factor > 1:
            # 左偏
            if node.left.balance_factor >= 0:
                return AVLTree.right_rotate(node)
            else:
                return AVLTree.left_right_rotate(node)
        elif node.balance_factor < -1:
            # 右偏
            if node.right.balance_factor <= 0:
                return AVLTree.left_rotate(node)
            else:
                return AVLTree.right_left_rotate(node)
        else:
            return node

    def insert(self, val: int):
        self.root = AVLTree._insert(self.root, val)

    @staticmethod
    def _insert(node: TreeNode, val: int) -> TreeNode:
        if node is None:
            # 递到底了，开始归
            return TreeNode(val)

        # 开始递
        if node.val < val:
            # 往右
            node.right = AVLTree._insert(node.right, val)
        elif node.val > val:
            # 往左
            node.left = AVLTree._insert(node.left, val)
        else:
            return node

        # left / right 时的情形
        node.update_height()
        return AVLTree.rotate(node)

    def search(self, val: int) -> TreeNode | None:
        # 与常规二叉搜索树一致
        return AVLTree._search(self.root, val)

    @staticmethod
    def _search(node: TreeNode | None, val: int) -> TreeNode | None:
        if node is None:
            return node

        if node.val < val:
            # 往右
            return AVLTree._search(node.right, val)
        elif node.val > val:
            # 往左
            return AVLTree._search(node.left, val)
        else:
            return node

    def remove(self, val: int):
        return AVLTree._remove(self.root, val)

    @staticmethod
    def _remove(node: TreeNode | None, val: int) -> TreeNode | None:
        if node is None:
            return node

        if node.val < val:
            # 往右
            node.right = AVLTree._remove(node.right, val)
        elif node.val > val:
            # 往左
            node.left = AVLTree._remove(node.left, val)
        else:
            # 找到了
            if node.left is None and node.right is None:
                return None
            elif node.left is None or node.right is None:
                node = node.left or node.right  # 跳过原本的 node
            else:
                # 左右两侧都有节点
                # 按照二叉搜索树的方法删除
                target = node.right
                while target.left is not None:
                    target = target.left
                node.right = AVLTree._remove(node.right, target.val)
                node.val = target.val

        node.update_height()
        return AVLTree.rotate(node)
