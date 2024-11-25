from typing import List
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if len(relations)==0:
            return max(time)
        
        self.dp_cost=defaultdict(int)
        ele_pre=set()
        ele_next=set()
        self.dict_relations={}
        self.time=time
        for i in range(len(relations)):
            ele_pre.add(relations[i][0])
            ele_next.add(relations[i][1])
            if relations[i][0] not in self.dict_relations:
                self.dict_relations.update({relations[i][0]:[relations[i][1]]})
            else:
                self.dict_relations[relations[i][0]].append(relations[i][1])
        ele_all=set([i for i in range(1,n+1)])
        self.heads=ele_all.difference(ele_next)
        self.ends=ele_all.difference(ele_pre)
        
        return max(self.get_time(i) for i in self.heads)
        
        
    def print_result(self):
        print("head=",self.heads)
        print("ends=",self.ends)
        print(self.dp_cost)    

        
    def get_time(self,head):
        cost=0
        tmp=head
        cost+=self.time[tmp-1]
        print("tmp=",tmp, "cost=",cost)
        if tmp in self.ends:
            return cost
        if tmp not in self.dp_cost:
            cost+=max([self.get_time(n) for n in self.dict_relations[tmp]])
            self.dp_cost[tmp]=cost
        return self.dp_cost[tmp]
            
                



    
s=Solution()
n = 3
relations = [[2,3]]
time = [3,1,1]
print(s.minimumTime(n,relations,time))
s.print_result()
