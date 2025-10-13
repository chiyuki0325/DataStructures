# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def searchFor(a: TreeNode, target: TreeNode, _path: list[TreeNode]):
            if a is None:
                return False
            _path.append(a)
            if a.val == target.val:
                return True
            result1 = searchFor(a.left, target, _path)
            result2 = searchFor(a.right, target, _path)
            if result1 or result2:
                return True
            _path.pop()
            return False

        path1 = []
        path2 = []
        searchFor(root, p, path1)
        searchFor(root, q, path2)
        print(list(i.val for i in path1))
        print(list(i.val for i in path2))

        i = 0
        while True:
            if i >= len(path1) or i >= len(path2):
                return path1[i - 1]
            if path1[i] != path2[i]:
                return path1[i - 1]
            i += 1
