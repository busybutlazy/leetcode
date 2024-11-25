from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor_result=0
        for num in nums:
            xor_result=xor_result^num
        
        distinguishing_bit=xor_result & -xor_result
        unique1=0
        unique2=0

        for num in nums:
            if num & distinguishing_bit:
                unique1^=num
            else:
                unique2^=num
        
        return (unique1,unique2)


if __name__=="__main__":
    solution=Solution()
    nums=[2,2,5,3,6,5,7,6]
    print(solution.singleNumber(nums))