from typing import List
import time

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise=0
        hare=0
        while True:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]
            if tortoise==hare:
                break
        hare=0
        while tortoise!=hare:
            tortoise=nums[tortoise]
            hare=nums[hare]
        return tortoise

    
    
nums = [1,2,3,4,7,8,6,5,2]
s=Solution()
print(s.findDuplicate(nums))