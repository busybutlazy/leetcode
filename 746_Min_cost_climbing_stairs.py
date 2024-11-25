from typing import List

class Solution:
    def __init__(self):
        self.dp=None
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost=cost+[0]
        self.dp=[0]*(len(cost))
        
        for i in range(len(cost)):
            if i <2:
                continue
            self.dp[i]=min(self.dp[i-2]+cost[i-2],self.dp[i-1]+cost[i-1])
        return self.dp
        
        
    
    
cost=[1,100,1,1,1,100,1,1,100,1]
s=Solution()


print(s.minCostClimbingStairs(cost))