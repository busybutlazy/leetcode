from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows ==1:
            return [[1]]
        else:
            last_row=self.generate(numRows-1)
            last_row.append([1]+[last_row[-1][i]+last_row[-1][i+1] for i in range(len(last_row[-1])-1)]+[1])
            return last_row

s=Solution()
print(s.generate(100))