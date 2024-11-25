from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        rest=k%sum(chalk)
        for i in range(len(chalk)):
            if rest<chalk[i]:
                return i
            else :
                rest-=chalk[i]


if __name__=="__main__":
    solution=Solution()
    chalk,k = [3,4,1,2],25
    print(solution.chalkReplacer(chalk,k))