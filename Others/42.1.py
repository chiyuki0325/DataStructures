class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        water_l=[0]*len(height)
        water_r=[0]*len(height)
        l_height=0
        for i in range(len(height)):
            l_height=max(l_height,height[i])
            water_l[i]=l_height-height[i]
        r_height=0
        for j in range(len(height)):
            i=len( height)-j-1
            r_height=max(r_height,height[i])
            water_r[i]=r_height-height[i]
        # 计算两部分的交集
        for i in range(len(height)):
            water+=min(water_l[i], water_r[i])
        return water
