from typing import List
from collections import deque

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_maps=[]
        for word in words:
            temp_map={}
            for c in word:
                if c not in temp_map:
                    temp_map.update({c:1})
                else:
                    temp_map[c]+=1
            word_maps.append(temp_map)
        
        result=[]
        for c in word_maps[0]:
            flag=True
            for i in range(1,len(word_maps)):
                if flag:
                    if c not in word_maps[i]:
                        flag=False
                        break
                    else:
                        word_maps[0][c]=min(word_maps[i][c],word_maps[0][c])
            if flag:
                result+=[c]*word_maps[0][c]

        return result


if __name__=="__main__":
    solution=Solution()
    words=["bella","label","roller"]
    print(solution.commonChars(words))