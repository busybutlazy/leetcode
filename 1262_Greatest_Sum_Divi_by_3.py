from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        num_sum=sum(nums)
        remainder_of_sum=num_sum%3
        print("remainder_of_sum=",remainder_of_sum)

        if remainder_of_sum==0:
            return num_sum
        hash_map={1:[],2:[]}
        
        for n in nums:
            remainder=n%3
            if remainder!=0:         
                hash_map[remainder].append(n)
        print("hash_map=",hash_map)
        for k in hash_map:
            hash_map[k].sort()
        
        
        if remainder_of_sum==1:
            candidate1,candidate2=num_sum,num_sum
            if len(hash_map[1])>=1:
                candidate1=hash_map[1].pop(0)
            if len(hash_map[2])>=2:
                candidate2=hash_map[2].pop(0)+hash_map[2].pop(0)
            return num_sum-min(candidate1,candidate2)
        if remainder_of_sum==2:
            candidate1,candidate2=num_sum,num_sum
            if len(hash_map[2])>=1:
                candidate1=hash_map[2].pop(0)
            if len(hash_map[1])>=2:
                candidate2=hash_map[1].pop(0)+hash_map[1].pop(0)
            return num_sum-min(candidate1,candidate2)
        
            
            

if __name__=="__main__":
    nums=[4,3]
    print(Solution().maxSumDivThree(nums))