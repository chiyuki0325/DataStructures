class SolutionHard:
    # 双指针版
    def trap(self, height: List[int]) -> int:
        l = 0  # 左指针
        r = len(height)-1  # 右指针
        hlw = 0
        hrw = 0
        water = 0  # 总水量

        # 变量说明：
        # hl：当前左指针地面高度
        # hr：当前右指针地面高度
        # hlw：当前左侧墙壁最大高度
        # hrw：当前右侧墙壁最大高度
        # hlw-hl=当前左指针可接水量
        # hrw-hr...

        while l < r:
            hl = height[l]
            hr = height[r]
            hlw = max(hlw, hl)
            hrw = max(hrw, hr)
            if hlw < hrw:
                water += hlw-hl
                l += 1
            else:
                water += hrw-hr
                r -= 1

        return water


class Solution:
    # 左扫一遍右扫一遍版
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left_scan = [0]*l  # 从右向左扫
        right_scan = [0]*l  # 从左向右扫
        final = 0

        for right in range(l):
            left = l-right-1

            if right > 0:
                right_scan[right] = max(right_scan[right-1], height[right])
            else:
                right_scan[right] = height[right]

            if left < len(height)-1:
                left_scan[left] = max(left_scan[left+1], height[left])
            else:
                left_scan[left] = height[left]

        for i in range(l):
            final += min(left_scan[i], right_scan[i])-height[i]

        return final
