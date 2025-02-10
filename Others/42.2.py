class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        l=0
        r=len(height)-1
        l_height=r_height=0
        while l<r:
            l_height=max(l_height, height[l])
            r_height=max(r_height, height[r])
            if l_height<r_height:
                """
                [ ] [ ] [x]
                [x] [ ] [x]
                [x] [x] [x]
                """
                water+= (l_height-height[l])
                l+=1
            else:
                water+= (r_height-height[r])
                r-=1
        return water
