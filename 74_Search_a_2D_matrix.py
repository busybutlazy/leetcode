from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target<matrix[0][0] or target>matrix[-1][-1]:return False
        
        def outer_search(mat,high,low,target):
            if high<low:
                return mat[min(high,low)]
            mid = (high + low)//2
            if mat[mid][0]==target:return mat[mid]
            elif mat[mid][0]>target:
                return outer_search(mat,mid-1,low,target)
            else:
                return outer_search(mat,high,mid+1,target)
        
        def inner_search(li,high,low,target):
                if high<low:
                    return False
                mid = (high + low)//2
                if li[mid]==target:
                    return True
                elif li[mid]>target:
                    return inner_search(li,mid-1,low,target)
                elif li[mid]<target:
                    return inner_search(li,high,mid+1,target)
        
        if target>matrix[-1][0]:return inner_search(matrix[-1],len(matrix[0]),0,target)
        
        return inner_search(outer_search(matrix,len(matrix),0,target),len(matrix[0]),0,target)
            
    
s=Solution()
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
print(s.searchMatrix(matrix,target))