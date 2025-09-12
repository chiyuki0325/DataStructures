class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        hlw=0
        hrw=0
        water=0

        while l<r:
            hl=height[l]
            hr=height[r]
            hlw=max(hlw,hl)
            hrw=max(hrw,hr)
            if hlw<hrw:
                water+=hlw-hl
                l+=1
            else:
                water+=hrw-hr
                r-=1

        return water
