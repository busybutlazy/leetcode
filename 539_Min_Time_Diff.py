from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints))!=len(timePoints):
            return 0
        def to_minutes(tp):
            return int(tp[0:2])*60+int(tp[3:])
        
        for i in range(len(timePoints)):
            timePoints[i]=to_minutes(timePoints[i])

        def count_min(t1,t2):
            return min(abs(t1-t2),1440-abs(t1-t2))

        timePoints.sort()
        mm=1440
        for i in range(len(timePoints)):
            if i == 0:
                tmp=count_min(timePoints[-1],timePoints[0])
            else:
                tmp=count_min(timePoints[i-1],timePoints[i])
            mm=min(tmp,mm)
        return mm
        # def get_min_min(tps,new_tp:int):
        #     l,r=0,len(tps)
        #     m=(l+r)//2
        #     while l<r:
        #         if tps[m]>new_tp:
        #             r=m-1
        #         else:
        #             l=m+1
        #         m=(l+r)//2


if __name__=="__main__":
    sol=Solution()
    timePoints = ["00:00","23:59"]
    print(sol.findMinDifference(timePoints))