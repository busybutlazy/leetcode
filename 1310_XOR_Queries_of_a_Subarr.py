from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre=[-1]*len(arr)
        for i in range(len(arr)):
            if i == 0:
                tmp=0
            tmp=tmp^arr[i]
            pre[i]=tmp

        ans=[-1]*len(queries)
        for i in range(len(queries)):
            if queries[i][0]==0:
                ans[i]=pre[queries[i][1]]
            else:
                ans[i]=pre[queries[i][1]]^pre[queries[i][0]-1]
        return ans
        


if __name__=="__main__":
    sol=Solution()
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]
    print(sol.xorQueries(arr,queries))
    print(7^2^7)