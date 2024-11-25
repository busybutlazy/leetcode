class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        s+=s
        
        for i in range(len(s)):
            flag=True
            for j in range(len(goal)):
                if i+j>len(s)-1:
                    return False
                
                if s[i+j]!=goal[j]:
                    flag=False
                    break
            if flag:
                return True
        return False
                
if __name__ == '__main__':
    sol=Solution()
    s,goal="abcde","deabc"
    print(sol.rotateString(s, goal))