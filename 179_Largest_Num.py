from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_helper(target,standard)->bool:
            """
            target is the number you want to put.
            standard is the number already in list.
            return True if the target is a better choice to put forward.
            on the other hand, return False if the target is not a better num to put forward. 
            """
            # if target==standard or target[0]>standard[0]:
            #     return True
            # elif target[0]<standard[0]:
            #     return False
            # return sort_helper2(target,standard)
            return target+standard>standard+target

        def sort_helper2(target,standard):
            if target=="" or standard=="":
                return True
            
            t_len,s_len=len(target),len(standard)
            if t_len==s_len:
                return int(target)>int(standard)
            else:
                flag=True
                shorter,longer=target,standard
                
                if t_len>s_len:
                    flag=False
                    shorter=standard
                    longer=target
                
                while len(longer)>=len(shorter):
                    print("here")
                    if int(shorter)>int(longer[:len(shorter)]):
                        return True==flag
                    elif int(shorter)<int(longer[:len(shorter)]):
                        return False==flag
                    longer=longer[len(shorter):]
                
                print(f"longer={longer} , shorter={shorter}")
                return sort_helper2(shorter if flag else longer,longer if flag else shorter)

        def binary_sort(li,new_num):
            l,r=0,len(li)
            m=(l+r)//2
            while l<r:
                if sort_helper(new_num,li[m]):
                    r=m
                else:
                    l=m+1
                m=(l+r)//2
            return m


        for i in range(len(nums)):
            nums[i]=str(nums[i])

        result=[]
        
        for n in nums:
            loc=binary_sort(result,n)
            print(f"loc={loc}, result[:loc]={result[:loc]}, [n]={[n]}, result[loc:]={result[loc:]}")
            
            result=result[:loc]+[n]+result[loc:]
        
        return str(int("".join(result)))


if __name__=="__main__":
    sol=Solution()
    nums = [3,30,34,5,9]#992534330
    print(sol.largestNumber(nums))