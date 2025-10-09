class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert_sub_array(l: int, r: int) -> Optional[TreeNode]:
            # 把 [l: r] 区域转为 BST

            # 1： 把数组切分为三块 [l1: r1] [mid] [l2: r2]
            l1 = l
            mid = (l + r) // 2
            r1 = mid - 1
            l2 = mid + 1
            r2 = r

            node = TreeNode(nums[mid])

            if r1 - l1 >= 0:
                node.left = convert_sub_array(l1, r1)
            if r2 - l2 >= 0:
                node.right = convert_sub_array(l2, r2)

            return node

        return convert_sub_array(0, len(nums)-1)
