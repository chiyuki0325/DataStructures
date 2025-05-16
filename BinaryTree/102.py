class Solution:
    def traverse(self, it: Optional[TreeNode], depth: int):
        if it is None:
            return
        if it.left is not None:
            self.traverse(it.left, depth + 1)
        while len(self.data) <= depth:
            self.data.append([])
        self.data[depth].append(it.val)
        if it.right is not None:
            self.traverse(it.right, depth + 1)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.data = []
        self.traverse(root, 0)
        return self.data
