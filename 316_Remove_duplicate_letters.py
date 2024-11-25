from collections import defaultdict
class Solution:
    
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        last_location=defaultdict(int)
        for i in range(len(s)):
            last_location[s[i]]=i
        
        for i in range(len(s)):
            print(stack)
            if s[i] in stack:
                continue
            for j in range(len(stack)-1,-1,-1):
                if stack[j]>s[i] and last_location[stack[j]]>i:
                    stack.remove(stack[j])
                else:
                    break
            stack.append(s[i])
        return "".join(stack)
        

        
        
            
        
        
    
s=Solution()
rdl=s.removeDuplicateLetters
strs = "cbbeecdab"

# strs="cbcbac"
# dict_test={"a":12,"b":13,"c":10}
print(rdl(strs))
# print(min(dict_test))