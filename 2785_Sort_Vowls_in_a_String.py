class Solution:
    def sortVowels(self, s: str) -> str:
        t=[0]*len(s)
        t_v=[]
        vowls="AEIOUaeiou"
        for i in range(len(s)):
            if s[i] in vowls:
                t[i]="*"
                t_v.append(s[i])
            else:
                t[i]=s[i]
        t_v.sort()
        flag=0
        for i in range(len(t)):
            if t[i]=="*":
                t[i]=t_v[flag]
                flag+=1
        return "".join(t)


s="lEetCOde"
sol=Solution()
print(sol.sortVowels(s))