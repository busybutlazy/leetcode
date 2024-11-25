class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:return s
        r_point=len(s)-1
        result=s[0]
        while r_point>=1:
            print("while 1")
            l_point=0
            if r_point<len(result):
                print("break")
                break
            tmp_l,tmp_r=l_point,r_point
            while l_point<r_point:
                print("while 2")
                print("tmp_l=",tmp_l," tmp_r=",tmp_r)
                if s[tmp_l]!=s[tmp_r]:
                    l_point+=1
                    tmp_l,tmp_r=l_point,r_point
                    continue
                else:
                    tmp_l+=1
                    tmp_r-=1
                    if tmp_l>=tmp_r:
                        if len(result)<r_point+1-l_point:
                            result=s[l_point:r_point+1]
                        break
            r_point-=1
        return result
    
sol=Solution()
s="aa"
print(sol.longestPalindrome(s))