from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result=0
        records=[]
        for i in range(len(arr)-1):
            xor_val=arr[i]
            for j in range(i+1,len(arr)):
                xor_val=xor_val^arr[j]
                if xor_val==0:
                    records.append((i,j))
                    result+=j-i
        return result


if __name__=="__main__":
    solution=Solution()
    arr=[1,3,5,7,9]
    print(solution.countTriplets(arr))