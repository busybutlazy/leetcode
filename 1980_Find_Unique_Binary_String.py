from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result=""
        for i,n in enumerate(nums):
            if n[i]=="0":
                result+="1"
            else:
                result+="0"
        return result
        
        # max=2**len(nums)
        # if max==1:
        #     return "1" if nums[0]=="0" else "0"
        # collect=set([i for i in range(max)])
        # for n in nums:
        #     print("collect=",collect,"n=",n,"int=",int(n,2))
        #     collect.remove(int(n,2))
        # rest=str(bin(collect.pop()))[2:]
        # l=len(nums)-len(rest)
        # return "0"*l+rest
    
sol=Solution()
nums=["01110","01010","11001","11100","10100"]
print(sol.findDifferentBinaryString(nums))