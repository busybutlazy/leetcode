from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # winner_candidates=set([i  for i in range(n)])
        # for edge in edges:
        #     if edge[1] in winner_candidates:
        #         winner_candidates.remove(edge[1])
        # if len(winner_candidates)==1:
        #     return winner_candidates.pop()
        # else:
        #     return -1
        winner_candidates=[0]*n
        for edge in edges:
            winner_candidates[edge[1]]+=1
        
        champ=-1
        champ_count=0

        for i in range(len(winner_candidates)):
            if winner_candidates[i]==0:
                champ=i
                champ_count+=1
        return champ if champ_count==1 else -1


            

if __name__ == "__main__":
    solution=Solution()
    n = 4
    edges = [[0,2],[1,3],[1,2]]
    print(solution.findChampion(n,edges))