class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        tmp_max=0
        for i in s:
            if i not in stack:
                stack.append(i)
            else:
                if i == stack[-1]:
                    stack=[i]
                    continue
                for j in range(len(stack)):
                    if stack[j] == i:
                        stack=stack[j+1:]+[i]
                        break
            tmp_max=max(tmp_max,len(stack))
        return tmp_max
            
sol=Solution()
s="abcabcbb"
print(sol.lengthOfLongestSubstring(s))