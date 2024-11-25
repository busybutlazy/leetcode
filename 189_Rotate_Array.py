from typing import List
def reverse_list(nums,k):
    nums[:k],nums[k:]=nums[-k:],nums[:-k]
            
class Solution:
    
    
    
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)<2 or k == len(nums):
            return
        elif k>len(nums):
            k=k%len(nums)
        
        
        
        # if len(nums)<2 or k == len(nums):
        #     return
        # elif k>len(nums):
        #     k=k%len(nums)
        
        # stored=[]
        # for _ in range(k):
        #     stored.append(nums.pop())
        # for _ in range(k):
        #     nums.append(0)
        # for i in range(len(nums)-1,-1,-1):
        #     if i <k:
        #         nums[i] = stored[k-i-1]
        #     else:
        #         nums[i] = nums[i-k]
                
        
s=Solution()
nums=[1,2,3,4,5,6,7]
k=3
reverse_list(nums,4)
print(nums)
# s.rotate(nums,k)
# print(nums)