from typing import List
from collections import defaultdict
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n=n
        self.org_dp=[[float("inf") for _ in range(n)]for _ in range(n)]
        self.data_change=False
        self.changed=[]
        for edge in edges:
            self.org_dp[edge[0]][edge[1]]=edge[2]
        for i in range(n):
            self.org_dp[i][i]=0
        
    def Dijkstra(self,n1,n2):
        table=[[False,float("inf"),-1]for _ in range(self.n)]
        table[n1]=[True,0,-1]
        pass_list=[0,float("inf")]
        node=n1
        while not table[n2][0]:
            table[node][0]=True
            for i in range(self.n):
                if self.org_dp[node][i]not in pass_list:
                    if table[i][1]>self.org_dp[node][i]+table[node][1]:
                        table[i][1]=self.org_dp[node][i]+table[node][1]
                        table[i][2]=node
            tmp_dis=float("inf")
            for i in range(self.n):
                if table[i][0]!=True:
                    if tmp_dis>=table[i][1]:
                        tmp_dis=table[i][1]
                        node=i
            
        return table
        
        
                            


    def addEdge(self, edge: List[int]) -> None:
        self.org_dp[edge[0]][edge[1]]=edge[2]

    def shortestPath(self, node1: int, node2: int) -> int:
        table=self.Dijkstra(node1,node2)
        return -1 if table[node2][1]==float("inf") else table[node2][1]
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
obj=Graph(4,[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(obj.shortestPath(3,2))
print(obj.shortestPath(0,3))
obj.addEdge([1,3,4])
print(obj.shortestPath(0,3))
