from typing import List
from math import ceil
from collections import defaultdict
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        turn_dic=defaultdict(int)
        for i in range(len(dist)):
            turn = ceil(dist[i]/speed[i])
            if turn not in turn_dic:
               turn_dic[turn]=1
            else:
                turn_dic[turn]+=1
        addition_shot=0
        count=0
        print(turn_dic)
        for i in range(1,len(dist)+1):
            if i not in turn_dic:
                addition_shot+=1
            else:
                if turn_dic[i]==1:
                    count+=1
                elif turn_dic[i]<=addition_shot+1:
                    addition_shot-=turn_dic[i]-1
                    count+=turn_dic[i]
                else:
                    count+=addition_shot+1
                    return count
            print("i=",i,"monsters=",turn_dic[i])
            print("addition_shot=",addition_shot)
        return len(dist)

    
dist = [1,3,4]
speed = [1,1,1]
s=Solution()
print(s.eliminateMaximum(dist,speed))