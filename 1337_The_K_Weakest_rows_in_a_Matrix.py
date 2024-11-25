from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        reslut=[]
        for i in range(len(mat[0])):
            for j in range(len(mat)):
                if mat[j][i]==0:
                    if j not in reslut:
                        reslut.append(j)
            if len(reslut)>=k:
                return reslut[:k]
        for i in range(len(mat)):
            if i not in reslut:
                reslut.append(i)
        return reslut[:k]
s=Solution()    
kwr=s.kWeakestRows
mat = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
k = 3
print(kwr(mat,k))