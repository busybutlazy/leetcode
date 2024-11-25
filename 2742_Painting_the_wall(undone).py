from typing import List


class Solution:
    def __init__(self):
        self.dp=None
    
    
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        cost=[0]+cost
        time=[0]+time
        total_time=0
        for t in time:
            total_time+=t
        self.dp=[[float("inf") for _ in range(total_time+1)] for _ in range(len(time))]
        for i in range(len(time)):
            for wall_amount in range(len(self.dp[0])):
                tmp1=float("inf")
                tmp2=float("inf")
                if wall_amount-time[i]<=time[i]:
                    tmp1=cost[i]
                if i > time[i]:
                    tmp2=self.dp[i-tmp1]
                
        return self.dp
        
        
        # tmp_min=float("inf")
        # for i in range(len(time)):
        #     for j in range(total_time+1):
        #         tmp1=float("inf")
        #         tmp2=float("inf")
        #         if j==time[i]:
        #             tmp1=cost[i]
        #         if j>time[i]:
        #             tmp2=self.dp[j-time[i]]+cost[i]              
        #         self.dp[j]=min(self.dp[j],tmp1,tmp2)
        #         if i==len(time)-1 and j>len(time)-j:
        #             if tmp_min>self.dp[j]:
        #                 tmp_min=self.dp[j]
        # return tmp_min
        
                
                
        
cost = [2,4,3,2]
time = [1,1,1,1]    
    
# cost = [1,2,3,2]
# time = [1,2,3,2]
s=Solution()
print(s.paintWalls(cost,time))