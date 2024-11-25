from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx=0
        flag=True
        while flag:
            now_c=None
            print("idx=",idx,"flag=",flag,"now_c=",now_c)
            for word in strs:
                if idx==len(word):
                    
                    flag=False
                    print("break")
                    break
                
                if not now_c:
                    now_c=word[idx]
                
                if now_c!=word[idx]:
                    print("now_c=",now_c,"word[idx]",word[idx])
                    flag=False
                    break
            idx+=1

        return strs[0][:idx-1]
        
if __name__ == '__main__':
    solution=Solution()
    strs = ["flower","flow","flight","fl",""]
    print(solution.longestCommonPrefix(strs))