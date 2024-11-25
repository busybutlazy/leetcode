from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        len_of_arr=len(original)
        if len_of_arr!=m*n:
            return []
        result=[original[i*n:(i+1)*n] for i in range(m)]

        return result



if __name__=="__main__":
    solution=Solution()
    f=solution.construct2DArray
    original=[1,2,3,4]
    m=1
    n=4
    print(f(original,m,n))