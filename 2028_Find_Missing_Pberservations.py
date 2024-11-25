from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total=mean*(len(rolls)+n)
        ans=[]
        sum_of=sum(rolls)
        print("total=",total," sum_of=",sum_of)
        if sum_of<=total-n and sum_of >=total-n*6:
            num_to_share=total-sum_of
            mode=num_to_share//n
            k=num_to_share-(mode*n)
            print("k=",k)
            ans = [mode]*n
            for i in range(k):
                ans[i]+=1
            # ans=[mode+1 if i<k else mode for i in range(n) ]         
            # left=total-sum_of
            # while left>0:
            #     to_add=left//n
            #     ans.append(to_add)
            #     left-=to_add
            #     n-=1

        return ans

if __name__=="__main__":
    solution=Solution()
    rolls=[4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5]
    mean=4
    n=40
    print(solution.missingRolls(rolls,mean,n))