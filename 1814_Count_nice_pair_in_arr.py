from typing import List
from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        M=10e9+7
        num_map=defaultdict(int)
        for n in nums:
            num_map[self.int2type(n)]+=1
        result=0
        for n in num_map.values():
            result+=n*(n-1)//2
            result=result%M
        print(num_map)
        return result
    
    def int2type(self,num):
        num_li=list(str(num))
        num_li.reverse()
        num_r=int("".join(num_li))
        return abs(num_r-num)    





def test(num1,num2):
    li1=list(num1)
    li2=list(num2)
    li1.reverse()
    li2.reverse()
    
    num1_r=int("".join(li1))
    num2_r=int("".join(li2))
    print("n1-n1r=",abs(int(num1)-num1_r))
    print("n2r-n2=",abs(num2_r-int(num2)))



    

sol=Solution()
nums = [352171103,442454244,42644624,152727101,413370302,293999243]
print(sol.countNicePairs(nums))
# print(test(str(nums[0]),str(nums[3])))