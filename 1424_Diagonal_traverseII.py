from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        li_map=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                li_map.append((i+j,j,nums[i][j]))
        li_map.sort()
        result=[]
        for tu in li_map:
            result.append(tu[2])
        return result
                

nums = [[1,2,3],[4,5,6],[7,8,9]]
sol=Solution()
print(sol.findDiagonalOrder(nums))        