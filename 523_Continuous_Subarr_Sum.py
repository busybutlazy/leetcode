from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        
        tmp_sum=0
        for i in range(len(nums)):
            tmp_sum+=nums[i]
            nums[i]=tmp_sum%k
        
        appeared=set()


        pre_remainder,remainder=0,0
        for i in range(len(nums)):
            remainder=nums[i]%k
            if i ==0:
                pre_remainder=remainder
                continue
            
            if remainder==0:
                return True
            
            if remainder in appeared:
                return True
            else:
                appeared.add(pre_remainder)
                pre_remainder=remainder
        return False




if __name__=="__main__":
    solution=Solution()
    nums=[0,1,0,3,0,4,0,4,0]
    k=5
    print(solution.checkSubarraySum(nums,k))