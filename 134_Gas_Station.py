from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        l=len(gas)
        start,curr_gas=0,0
        for i in range(l):
            curr_gas+=gas[i]-cost[i]
            if curr_gas<0:
                start=i+1
                curr_gas=0
        return start
        
        
        
        # while end<l*2-1:            
        #     now_gas+=gas[end%l]-cost[end%l]
        #     end+=1
        #     if now_gas<0:
        #         start=end
        #         now_gas=0
        #     else:
        #         if end-start==l-1:
        #             return start
        # return -1
    

if __name__=="__main__":
    gas=[5,1,2,3,4]
    cost=[4,4,1,5,1]
    print(Solution().canCompleteCircuit(gas,cost))