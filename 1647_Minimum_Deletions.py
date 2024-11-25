class Solution:
    def minDeletions(self, s: str) -> int:
        c_map={}
        for c in s:
            if c not in c_map:
                c_map.update({c:1})
            else:
                c_map[c]+=1
        freq=list(c_map.values())
        dp=[0]*(len(freq)+1)
        final_set=set()
        for i in range(1,len(freq)+1):
            if freq[i-1] not in final_set:
                final_set.add(freq[i-1])
                dp[i]=dp[i-1]
            else:
                minus=self.helper(final_set,freq[i-1])
                if minus<freq[i-1]:
                    final_set.add(freq[i-1]-minus)
                    dp[i]=dp[i-1]+minus
                else:
                    dp[i]=dp[i-1]+freq[i-1]
        return dp[-1]
            
    def helper(self,final,freq):
        if freq in final:
            return self.helper(final,freq-1)+1
        else:
            return 0
                
    
    

min_d=Solution().minDeletions
s="aab"
print(min_d(s))