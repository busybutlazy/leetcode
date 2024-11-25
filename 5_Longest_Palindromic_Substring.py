class Solution:
    def check_palindrome(self,s)-> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i]==s[j]:
                i,j=i+1,j-1
                continue
            return False
        return True
        
    def longestPalindrome(self, s: str) -> str:
        longest=""
        i,j=0,len(s)-1
        while i<=j:
            while i<=j:
                if s[i]==s[j] and self.check_palindrome(s[i:j+1]):
                    if len(s[i:j+1])>len(longest):
                        longest=s[i:j+1]
                i+=1                    
            i=0
            j-=1
            if len(longest)>j-i:
                break
        return longest




lonPal=Solution().longestPalindrome
# strs="babad"
# strs="cbbbbd"
# strs="acbbda"
strs="acacabab"
strs="a"
print(lonPal(strs))
# print(7//2)
