class Solution:
    def reverseWords(self, s: str) -> str:
        result=""
        tmp=""
        for c in s:
            if c==" ":
                result = result+tmp+" "
                tmp=""
            else:
                tmp=c+tmp
        return result