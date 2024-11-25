class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=self.skipper(s)
        t=self.skipper(t)
        if s==t:
            return True
        else:
            return False
    
    def skipper(self,str):
        c_list1=[]
        for i in range(len(str)):
            if str[i]=="#":
                if len(c_list1):
                    c_list1.pop(-1)
            else:
                c_list1.append(str[i])
        return "".join(c_list1)
            
            

    
solution=Solution()
s = "bxj##tw"
t = "bxo#j##tw"
print(solution.backspaceCompare(s,t))