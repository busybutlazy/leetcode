from typing import List
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter_map=defaultdict(int)
        temp=0

        for i in range(len(nums)):
            if i==0:
                temp=nums[i]%k
            else:
                temp=(nums[i]+temp)%k
            counter_map[temp]+=1
        
        result=0

        def cal_helper(n:int):
            return (n+1)*n//2
        
        for k in counter_map:
            if k ==0:
                result+=cal_helper(counter_map[k])
            else:
                result+=cal_helper(counter_map[k]-1)

        return result
    

if __name__=="__main__":
    solution=Solution()
    nums=[4,5,0,-2,-3,1]
    k=5
    print(solution.subarraysDivByK(nums,k))