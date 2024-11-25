from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        ideal_sum,realistic_sum=0,0
        no_magic_power_result=0
        max_different=0

        for i in range(len(customers)):
            if grumpy[i]==0:
                no_magic_power_result+=customers[i]
                realistic_sum+=customers[i]
            ideal_sum+=customers[i]
            

            # Magic can only maintain n minutes. 
            # If run out of minutes. Delete the front of realistic sum and ideal sum.
            if i >=minutes:
                if grumpy[i-minutes]==0:
                    realistic_sum-=customers[i-minutes]
                ideal_sum-=customers[i-minutes]

            # Calculate the difference between ideal and realistic and save the maximum value of all results.
            max_different=max(max_different,ideal_sum-realistic_sum)

        return no_magic_power_result+max_different

if __name__=="__main__":
    customers,grumpy,minutes = [1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1], 3
    print(Solution().maxSatisfied(customers,grumpy,minutes))