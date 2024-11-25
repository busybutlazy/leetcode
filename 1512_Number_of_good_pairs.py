from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums_dict=defaultdict(int)
        for n in nums:
            nums_dict[n]+=1
        result=0
        for i in nums_dict:
            if nums_dict[i]>1:
                result+=self.count_c(nums_dict[i])
        return result

    def count_c(self,x):
        if x<2:
            return 0
        else:
            return x*(x-1)//2
        