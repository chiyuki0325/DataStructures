class Solution:
    # 用 94 题代码修改而来
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        stack = [root]
        while stack:
            stack_top = stack.pop()
            if stack_top is None:
                continue
            if isinstance(stack_top, int):
                result.append(stack_top)
                # 提前返回
                if len(result) == k:
                    return result[-1]
            else:
                stack.append(stack_top.right)
                stack.append(stack_top.val)
                stack.append(stack_top.left)
