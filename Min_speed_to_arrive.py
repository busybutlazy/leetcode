from typing import List 
import math
class Solution:
    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        self.dist=dist
        self.hour=hour
        dis_sum=sum(dist)
        self.max_available_speed = max(dist)
        if len(dist)-hour>1:
            return -1
        if (dis_sum)<=hour:
            return 1
        if len(dist)-hour<1:
            # print(hour-len(dist)+1)
            # print(dist[-1])
            need_speed=int(dist[-1]/(hour-len(dist)+1))
            self.max_available_speed = max(need_speed,max(dist))
        if self.max_available_speed==1:return 1
        return self.recursion_fun(self.max_available_speed//2)
        
        
    def recursion_fun(self,speed_now):
        # print("speed_now=",speed_now)
        # print("max_available_speed=",self.max_available_speed)
        if speed_now==self.max_available_speed:return self.max_available_speed
        if self.speed_cal(speed_now):
            self.max_available_speed=speed_now
            return self.recursion_fun(speed_now//2)
        else:
            speed_next=int(self.max_available_speed/2+(speed_now/2))
            if speed_next==speed_now or speed_now+1==self.max_available_speed: return self.max_available_speed
            return self.recursion_fun(speed_next)
    
    def speed_cal(self,speed:int):
        total_time=0
        for d in range(len(self.dist)):
            if d==len(self.dist)-1:
                total_time += self.dist[d]/speed
                break
            if self.dist[d]%speed==0:
                total_time+=self.dist[d]/speed
            else:
                total_time+=(self.dist[d]//speed)+1
        if total_time>self.hour:
            return False
        return True
    
    
s=Solution()
dist=[40,86,53,42,52,90,38,71,17,25,54,86,49,87,96,23,79,73,39,52,71,1,39,37,27,56,75,78,84,42,60,57,57,87,28,66,61,95,22,85,11,37,66,85,82,80,43,12,97,31,87,40,29,26,19,4,6,32,61,79,99,10,59,54,81,74,25,92,90,50,64,52,32,19,84,89,1,97,99,14,100,55]
hour=364.83
print(s.minSpeedOnTime(dist, hour))