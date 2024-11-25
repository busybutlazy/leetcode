from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows>=2:
            tmp=Solution().generate(numRows-1)
            tmp.append([1])
            for i in range(len(tmp[-2])-1):
                tmp[-1].append(tmp[-2][i]+tmp[-2][i+1])
            tmp[-1].append(1)
            return tmp
        
print(Solution().generate(10))