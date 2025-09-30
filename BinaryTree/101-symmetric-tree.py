from typing import List, Optional
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # 把二叉树逐层压平为数组形式，方便比较
        def flatten(node: TreeNode, rtl: bool) -> List[Optional[int]]:
            queue = deque([node])
            result = []
            while queue:
                n = queue.popleft()
                if n:
                    result.append(n.val)
                    if rtl:
                        queue.append(n.right)
                        queue.append(n.left)
                    else:
                        queue.append(n.left)
                        queue.append(n.right)
                else:
                    result.append(None)
            return result

        if root.left or root.right:
            if root.left and root.right:
                # 比较压平后的左子树和右子树
                l = flatten(root.left, False)
                r = flatten(root.right, True)
                return l == r
            else:
                return False
        else:
            return True
