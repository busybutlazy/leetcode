class Solution:
    def isValid(self, s: str) -> bool:
        parenthese_dict={"{":"}","(":")","[":"]"}
        stack=[]
        for i in range(len(s)):
            if s[i] in parenthese_dict:
                stack.append(s[i])
            else:
                if len(stack)==0 or parenthese_dict[stack.pop()]!=s[i]:
                    return False
        
        
        return True if len(stack)==0 else False


if __name__=="__main__":
    solution=Solution()
    s= ")"
    print(solution.isValid(s))