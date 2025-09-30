class Solution1:
    # 笨方法：递归
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))
        return result


class Solution:
    # 题解方法：用栈实现迭代
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]
        while stack:
            stack_top = stack.pop()
            if stack_top is None:
                continue
            if isinstance(stack_top, int):
                result.append(stack_top)
            else:
                stack.append(stack_top.right)
                stack.append(stack_top.val)
                stack.append(stack_top.left)
        return result
