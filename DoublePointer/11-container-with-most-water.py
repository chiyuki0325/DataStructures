class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0
        def calc(left,right):
            nonlocal water
            l=height[left]
            r=height[right]
            water=max(water,(right-left)*min(l,r))
            #print(water)

        calc(left,right)
        while left<right:
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
            calc(left,right)
        return water
