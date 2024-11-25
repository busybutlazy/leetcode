from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        bloomDay:The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]. \n
        m:You want to make m bouquets.  \n
        k:To make a bouquet,need k adjacent flowers from the garden.
        """
        
        if len(bloomDay)<m*k:
            return -1
        elif len(bloomDay)==m*k:
            return max(bloomDay)
        
        def check_legal(n):
            tmp_m=m
            cur_count=0            
            for bd in bloomDay:
                if bd<=n:
                    cur_count+=1
                else:
                    tmp_m-=cur_count//k
                    cur_count=0
                    if tmp_m<=0:
                        return True
            tmp_m-=cur_count//k
            return tmp_m<=0

        days=[0]+list(set(bloomDay.copy()))
        days.sort()

        l,r=0,len(days)-1
        mid=(l+r)//2
        memory=[None]*len(days)


        while l<r:
            if memory[mid]==None:
                memory[mid]=check_legal(days[mid])
            
            if memory[mid-1]==None:
                memory[mid-1]=check_legal(days[mid]-1)
            
            if memory[mid] and memory[mid-1]:
                r=mid
                mid=(l+r)//2
            elif not memory[mid] and not memory[mid-1]:
                l=mid+1
                mid=(l+r)//2
            else:
                break

        print(memory)
        return days[mid]
    
if __name__=="__main__":
    bloomDay = [7,7,7,7,12,7,7]
    m = 2
    k = 2
    print(Solution().minDays(bloomDay,m,k))