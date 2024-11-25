class Solution:
        def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
            tmp_row=[poured]
            for row in range(1,query_row+1):
                next_row=[0 for _ in range(row+1)]
                for i,cup in enumerate(tmp_row):
                    if cup >1:
                        tmp=(tmp_row[i]-1)/2
                        next_row[i+1]+=tmp
                        next_row[i]+=tmp
                        tmp_row[i]=1.0
                tmp_row=next_row
            return tmp_row
    
    
poured = 2
query_row = 1
query_glass = 1
s=Solution()
print(s.champagneTower(poured,query_row,query_glass))