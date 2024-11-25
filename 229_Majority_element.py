from typing import List
from collections import defaultdict

class Solution:    
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1,count2=0,0
        candidates1,candidates2 =0,0
        
        for n in range(nums):
            counter=defaultdict(int)
            result=set()
            length=len(nums)
        for n in nums:
            if n in result:
                continue
            counter[n]+=1
            if counter[n]*3>length:
                result.add(n)
        return list(result)
    
    
s=Solution()
nums=[3,2,3]
print(s.majorityElement(nums))