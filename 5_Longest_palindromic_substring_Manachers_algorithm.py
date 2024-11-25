class Solution:
    def longestPalindrome(self, s: str) -> str:
        # add delimiters
        new_s="*"
        for char in s:
            new_s+=char+"*"
        length = len(new_s)
        self.dp=[0 for _ in range(length)]
        for center in range(length):
            if new_s[center] =="*":
                continue
            for i in range(2,min(center,length-1-center),2):
                if new_s[center-i] ==new_s[center+i]:
                    self.dp[center]+=1
                else:
                    break
            
        
        return self.dp
    
sol=Solution()
s="aabbccb"
print(sol.longestPalindrome(s))