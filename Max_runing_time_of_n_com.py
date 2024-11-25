from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        counter=0
        while len(batteries)>=n:
            for i in range(n):
                batteries[i]-=1          
            while 0 in batteries:batteries.remove(0)
            batteries.sort(reverse=True)
            counter+=1
            print(batteries)
        return counter
                
            
                
                
                
            
s=Solution()
n=5

batteries=[2,5,20,90,5,5]
print(sum(batteries)//n)
print(s.maxRunTime(n,batteries))
# dic1={"a":12}
# dic2={"a":-5}
# dic3={**dic1,**dic2}
# print(dic3)