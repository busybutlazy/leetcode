from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for n in nums:
            result.append([n])
        if len(result)<2:
            return result
        
        def helper(nums,li,count):
            new_list=[]
            for l in li:
                for n in nums:
                    if n not in l:
                       new_list.append(l+[n])
            if count >1:
                return helper(nums,new_list,count-1)
            else:
                return new_list
        
        return helper(nums,result,len(nums)-1)
         
        
        
        
        
    
nums=[1,2,3,8,9,10]
s=Solution()
print(s.permute(nums))