from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        len_list=[] #數字區間
        cost_set=set() #長度集合
        tmp=0
        for i in cuts:
            len_list.append(i-tmp)
            cost_set.add(i-tmp)
            tmp=i
        len_list.append(n-tmp)
        cost_set.add(n-tmp)
        
        to_del=[]
        for i in range(len(len_list)-1):
            if len_list[i]+len_list[i+1] in cost_set:
                len_list[i]+=len_list[i+1]
                to_del.append(i+1)
                i+=1
                continue
        return len_list
        
        
        

        
        
        
        
        
    


mC=Solution().minCost

print(mC(7, [1,3,4,5]))#16