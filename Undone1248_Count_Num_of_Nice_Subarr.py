from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        amount_of_even=[1]
        counter=0
        
        for n in nums:
            if n%2==0:
                amount_of_even[counter]+=1
            else:
                amount_of_even.append(1)
                counter+=1
        result=0
        for i in range(k,len(amount_of_even)):
            result+=amount_of_even[i-k]*amount_of_even[i]
        
        return result

if __name__=="__main__":
    nums,k= [2,2,2,1,2,2,1,2,2,2],2
    print(Solution().numberOfSubarrays(nums,k))