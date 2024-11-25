class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        tmp,heightest=0,0
        for i in gain:
            tmp+=i
            if tmp>heightest:
                heightest=tmp       
        return heightest



la=Solution().largestAltitude
gain=[-5,1,5,0,-7]
print(la(gain))


gain=[-4,-3,-2,-1,4,3,2]
print(la(gain))
