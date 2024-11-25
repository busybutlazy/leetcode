from typing import List
from collections import defaultdict
from queue import Queue

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target :return 0
        dis_dic=defaultdict(list)
        traveled=[]
        q=Queue()
        # make map
        for route in routes:
            for i in range(len(route)):
                dis_dic[route[i]]+=route[:i]
                dis_dic[route[i]]+=route[i+1:]
        q.put(target)
        # to_check=[]
        now,next,counter=1,0,1
        while q.qsize()>0:
            root=q.get()
            print("root=",root)
            print("now=",now,"next=",next,"counter=",counter)
            traveled.append(root)
            now-=1
            if source in dis_dic[root]:
                print("now check",dis_dic[root])
                return counter
            else:
                for node in dis_dic[root]:
                    if node not in traveled:
                        q.put(node)
                        next+=1
            if now==0:
                now,next=next,0
                counter+=1
                print("count +1")
        return -1

    
    
            
        
    
routes = [[1,2],[3,2],[6,5],[3,6,7]]
source = 3
target = 6

sol=Solution()
print(sol.numBusesToDestination(routes, source, target))