from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i=0
        tmp=None
        for num in nums:
            if i==0:
                tmp=num
                i+=1
            elif tmp==num:
                i+=1
            else:
                i-=1
        return tmp
        
        # if len(nums)<3:
        #     return nums[0]
        # map_of_nums={}
        # for n in nums:
        #     if n not in map_of_nums:
        #         map_of_nums.update({n:1})
        #     else:
        #         map_of_nums[n]+=1
        #         if map_of_nums[n]>=len(nums)*2:
        #             return n
        # tmp=nums[0]
        # for num in map_of_nums:
        #     if map_of_nums[num]>map_of_nums[tmp]:
        #         tmp=num
        # print(map_of_nums)
        # return tmp

nums=[3,2,3,2,1,2,2]

print(Solution.majorityElement(Solution,nums))