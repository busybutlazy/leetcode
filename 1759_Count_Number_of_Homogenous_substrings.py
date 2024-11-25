from collections import defaultdict

class Solution:
    def countHomogenous(self, s: str) -> int:
        M=1000000007
        self.count_dp=defaultdict(int)
        self.count_dp[0]=0
        head=""
        result=0
        counter=0
        for i in range(len(s)):
            if s[i] != head:
                head=s[i]
                result+=self.counting(counter)
                result=int(result%M)
                counter=1
            else:
                counter+=1
        result+=self.counting(counter)
        result=int(result%M)
        return result
                
    
    
    def counting(self,n:int):
        if n not in self.count_dp:
            self.count_dp[n]=(n*(n+1))/2
        return self.count_dp[n]
            
        
s = "abbcccaa"
sol=Solution()
print(sol.countHomogenous(s))
