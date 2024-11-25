from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)<2:
            return pref
        result=[pref[0]]
        for i in range(1,len(pref)):
            result.append(pref[i]^pref[i-1])
        return result

s=Solution()
pref=[5,2,0,3,1]
print(s.findArray(pref))
print(0^2)