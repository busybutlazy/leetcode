from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        result=0
        for i in range(len(seats)):
            result+=abs(seats[i]-students[i])
        
        return result

if __name__=="__main__":
    seats=[2,2,6,6]
    students=[1,3,2,6]
    print(Solution().minMovesToSeat(seats,students))