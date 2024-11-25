from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        tmp=0
        
        for ant in left:
            if ant-0>tmp:
                tmp=ant-0
        for ant in right:
            if n-ant>tmp:
                tmp=n-ant
        return tmp
    
n = 4 
left = [4,3]
right = [0,1]