class Solution:
    def scoreOfString(self, s: str) -> int:
        front=ord(s[0])
        result=0
        for i in range(1,len(s)):
            back=ord(s[i])
            if back>front:
                result+=back-front
            else:
                result+=front-back
            front=back
        return result


if __name__=="__main__":
    solition=Solution()
    s="zaz"
    print(solition.scoreOfString(s))