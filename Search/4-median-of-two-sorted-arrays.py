from typing import List
from math import ceil


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 合并后的完整有序数组:
        # [ nums1[:m1] ][ nums2[:m2] ] | [ nums1[m1:] ][ nums2[m2:] ]

        # m1+m2 = ceil((len(nums1)+len(nums2)) / 2)
        # 只需要找合并点 m1 即可

        # 找的方法，判断 m1 正确的条件: 看棍子 |
        # nums2[m2-1] < nums1[m1]

        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        first_part_len = ceil((l1 + l2) / 2)

        l = 0
        r = l1
        while l < r:  # l!=r
            m1 = (l + r) // 2
            m2 = first_part_len - m1
            if nums1[m1] < nums2[m2 - 1]:
                # 不正确的
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = first_part_len - m1
        # print("found m1", m1, "m2", m2)
        # 最不能理解的部分，开始背
        c1 = max(
            nums1[m1 - 1] if m1 > 0 else float("-inf"),
            nums2[m2 - 1] if m2 > 0 else float("-inf"),
        )
        if (l1 + l2) % 2 == 1:
            return c1
        c2 = min(
            nums1[m1] if m1 < l1 else float("inf"),
            nums2[m2] if m2 < l2 else float("inf"),
        )
        return (c1 + c2) / 2


if __name__ == "__main__":
    assert (
        Solution().findMedianSortedArrays(
            [1, 2, 5, 6], [3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        )
        == 8.5
    )
    # [1,2,5,6] [3,4,7,8,9,10,11,12]
    # [ 1,2 ][ 3,4 ][ 5,6 ]|[ 7,8,9,10,11,12 ]
    # 特殊测试样例，nums1 被整个放在左边

    # [1,2,5,6] [3,4,7,8,9,10,11,12,13,14,15,16]
    # 更特殊的测试样例
    # [ 1,2 ][ 3,4 ][ 5,6 ][ 7,8, | 9,10,11,12,13,14,15,16 ]
    # 分割线左边已经有四块了
