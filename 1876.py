# Substrings of Size Three with Distinct Characters
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter=0
        for i in range(len(s)-2):
            if s[i]!=s[i+1] and s[i]!=s[i+2]:
                if s[i+1]!=s[i+2]:
                    counter+=1
                else:
                    i+=2
        return counter                
    



S=Solution().countGoodSubstrings
print(S("xyzzaz"))
print(S("aababcabc"))