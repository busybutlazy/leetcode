from typing import List
import time
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        record=len(nums)
        if len(nums) <3:
            return len(nums)
        i=1
        while i<len(nums)-1 and nums[i+1] != None:
            print("i=",i)
            print("i-2=",nums[i-1],"i+1=",nums[i+1])
            if nums[i-1]==nums[i+1]:
                record-=1
                nums.append(None)
                nums.remove(nums[i])
                i-=1
                print("nums=",nums)
            i+=1
            time.sleep(1)
        print(nums)
        return record        

s=Solution()
nums=[0,0,0,0,0]
print(s.removeDuplicates(nums))
# print(None==0)