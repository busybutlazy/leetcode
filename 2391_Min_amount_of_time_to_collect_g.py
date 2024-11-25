from typing import List
from collections import defaultdict
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g_loc=defaultdict(int)
        g_count=0
        for i,g in enumerate(garbage):
            for c in "MPG":
                if c in g:
                    g_loc[c]=i
            g_count+=len(g)
        min_sum=g_count
        for i in g_loc.values():
            min_sum+=sum(travel[:i])
        return min_sum
                    
    
garbage = ["MMM","PGM","GP"]
travel = [3,10]
sol=Solution()
print(sol.garbageCollection(garbage,travel))