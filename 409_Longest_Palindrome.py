class Solution:
    def longestPalindrome(self, s: str) -> int:
        container=[]
        counter=0
        for c in s:
            if c not in container:
                container.append(c)
            else:
                counter+=2
                container.remove(c)
        
        return counter+bool(container)
    
    
    
if __name__ == '__main__':
    solution=Solution()
    s = "abccccdd"
    print(solution.longestPalindrome(s))