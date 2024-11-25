from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        
        def default_sort(heights)->int:
            s=sorted(heights)
            counter=0
            for i in range(len(heights)):
                if heights[i]!=s[i]:
                    counter+=1
            return counter

        def count_sort(heights:List[int])->List[int]:
            count=[0]*101
            for num in heights:
                count[num]+=1
            count_sum=[0]*101
            for i in range(1,len(count_sum)):
                count_sum[i]=count[i]+count_sum[i-1]
            print("count_sum=",count_sum)
            counter=0

            for i in range(len(heights)):
                print("i=",i)
                print("count_sum[heights[i]]-1=",count_sum[heights[i]]-1)
                
                print(count_sum[heights[i]]-1>=i)
                print(count_sum[heights[i]]-count[heights[i]]<=i)
                print("count_sum[heights[i]]-count[heights[i]]=",count_sum[heights[i]]-count[heights[i]])
                if count_sum[heights[i]]-1>=i and count_sum[heights[i]]-count[heights[i]]<=i:
                    pass
                else:
                    counter+=1

            return counter
        return count_sort(heights)


if __name__=="__main__":
    heights=[1,1,4,2,1,3]
    
    
    print(Solution().heightChecker(heights))