from typing import List
from collections import defaultdict
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        num_dic=defaultdict(int)
        for n in nums:
            num_dic[n]+=1
        l=len(num_dic)
        result=0
        num_li=list(num_dic.keys())
        num_li.sort()
        for i,val in enumerate(num_li):
            result+=(i)*num_dic[val]
        return result

sol=Solution()
print(sol.reductionOperations([1,3,5,3]))