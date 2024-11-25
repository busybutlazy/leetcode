from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        weight_to_sort={}
        for i in range(len(arr2)):
            weight_to_sort[arr2[i]]=i
        
        for i in range(len(arr1)):
            if arr1[i] not in weight_to_sort:
                weight_to_sort[arr1[i]]=1000+arr1[i]
        arr1.sort(key=lambda x:weight_to_sort[x])

        return arr1
        
        
        
        
        
        
        
        
        # weight_to_sort={}
        # for i in range(len(arr2)):
        #     weight_to_sort.update({arr2[i]:i})


        # count=[0]*(len(arr2))
        # tail_list=[]
        # for num in arr1:
        #     if num in arr2:
        #         count[weight_to_sort[num]]+=1
        #     else:
        #         tail_list.append(num)
        # tail_list.sort()
        # result=[]
        # for i in range(len(arr2)):
        #     result+=[arr2[i]]*count[i]

        # return result+tail_list
    

if __name__=="__main__":
    arr1=[2,3,1,3,2,4,6,7,9,2,19]
    arr2=[2,1,4,3,9,6]
    
    print(Solution().relativeSortArray(arr1,arr2))