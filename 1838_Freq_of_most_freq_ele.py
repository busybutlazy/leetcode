from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ceil=nums[0]
        max_win_size=0
        win_size=0
        left=0
        total_dif=0
        while left+win_size<len(nums):
            if ceil==nums[left+win_size]:
                win_size+=1
                continue
            max_win_size=max(max_win_size,win_size)
            ceil+=1
            total_dif+=win_size
            while total_dif>k:
                total_dif-=ceil-nums[left]
                left+=1
                win_size-=1
        return max(max_win_size,win_size)

    
sol=Solution()
nums=[1,2,4]
k = 5
print(sol.maxFrequency(nums,k))