from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        M=10e9+7
        arr=[0]+arr
        arr.sort()
        self.dp=[[0 for _ in range(len(arr))] for _ in range(len(arr))]
        v_to_i={}
        for i in range(len(arr)):
            v_to_i.update({arr[i]:i})
        result=0
        for i in range(1,len(arr)):
            for j in range(1,len(arr)+1):
                if j>i:
                    print("i=",i,"j=",j)
                    continue
                print("arr[i]=",arr[i]," arr[j]=",arr[j])
                self.dp[i][j]+=self.dp[i][j-1]
                print("self.dp[i][j]=",self.dp[i][j])
                if arr[i]==arr[j]:
                    print("here")
                    self.dp[i][j]+=1
                elif arr[i]/arr[j] in v_to_i:
                    self.dp[i][j]+=int((self.dp[j][j]*self.dp[v_to_i[arr[i]//arr[j]]][v_to_i[arr[i]//arr[j]]])%M)
                if j==len(arr)-1:
                    result+=self.dp[i][-1]
                    result=int(result%M)
        return self.dp
                
    
    
    
s=Solution()
arr=[2,4,5,10,20]
print(s.numFactoredBinaryTrees(arr))