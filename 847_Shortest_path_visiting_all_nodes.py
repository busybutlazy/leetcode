from typing import List

class Solution:    
    def two_point_length(self,graph):
        dp=[[1 if i in graph[j] else 999 for i in range(len(graph))] for j in range(len(graph))]
        for i in range(len(graph)):dp[i][i]=0
        for k in range(len(graph)):
            for i in range(len(graph)):
                for j in range(len(graph)):
                    if i == k or j==k or i==j:continue
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
        return dp
        
    
    
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        pass




    
s=Solution()
spl=s.shortestPathLength
graph=[[1],[0,2,4],[1,3,4],[2],[1,2]]
# print(spl(graph))
print(s.two_point_length(graph))
