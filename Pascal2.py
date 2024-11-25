from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex>=1:
            current_list=self.getRow(rowIndex-1)
            tmp=[1]
            for i in range(len(current_list)-1):
                tmp.append(current_list[i]+current_list[i+1])
            tmp.append(1)
            return tmp
        
print(Solution().getRow(3))