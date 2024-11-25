from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        front=[]
        back=[]
        for n in nums:
            if n%2==0:
                front.append(n)
            else:
                back.append(n)
        return front+back



s=Solution()
nums=[3,1,2,4]
sabp=s.sortArrayByParity

print(sabp(nums))
# print(nums.pop(0))