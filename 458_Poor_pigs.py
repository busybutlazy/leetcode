class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        test_time=minutesToTest//minutesToDie
        base=test_time+1
        tmp=1
        pigs=0
        while buckets>tmp:
            tmp=tmp*base
            pigs+=1
        return pigs
    