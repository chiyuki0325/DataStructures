class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = 0

        def search_left_right(node: Optional[TreeNode], sums: List[int]):
            nonlocal counter
            if node is None:
                return

            sums = list(map(lambda c: c + node.val, sums))
            sums.append(node.val)

            counter += sums.count(targetSum)

            search_left_right(node.left, sums)
            search_left_right(node.right, sums)

        search_left_right(root, [])
        return counter
