from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def recursive(i,s):
            s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
            if i != 0 :
                recursive(i-1,s)
    
        recursive((len(s)//2)-1,s)

if __name__=="__main__":
    solution=Solution()
    s=list("apple")
    solution.reverseString(s)
    print(s)