from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        tmp_max=0
        l=0
        r=len(height)-1
        while r>l:
            curr_area=min(height[l],height[r])*(r-l)
            if curr_area > tmp_max:
                tmp_max=curr_area
            if height[r] > height[l]:
                l+=1
            else:
                r-=1
        return tmp_max
    
height = [1,8,6,2,5,4,8,3,7]
AreaCalc=Solution().maxArea
print(AreaCalc(height))