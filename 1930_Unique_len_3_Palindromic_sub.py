from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_map=defaultdict(list)
        for i in range(len(s)):
            char_map[s[i]].append(i)
        result=set()
        for edge in char_map:
            centers=set(list(s[char_map[edge][0]+1:char_map[edge][-1]]))
            for center in centers:
                result.add(edge+center+edge)
        return len(result)
    
    

s="abaacba"
sol=Solution()
print(sol.countPalindromicSubsequence(s))