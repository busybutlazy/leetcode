from typing import List
from queue import deque

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        work_que=deque()
        hash_map={}
        for i in range(len(difficulty)):
            if difficulty[i] not in hash_map:
                hash_map[difficulty[i]]=0
            hash_map[difficulty[i]]=max(profit[i],hash_map[difficulty[i]])
        difficulty.sort()
        curr_max=0
        for dif in difficulty:
            if hash_map[dif]>curr_max:
                curr_max=hash_map[dif]
                work_que.append((dif,curr_max))
        
        total_profit=0
        curr_task=work_que.popleft()
        next_task=None

        worker.sort()
        if work_que:
            next_task=work_que.popleft()

        for w in worker:
            if next_task:
                while next_task and next_task[0]<=w:
                    curr_task=next_task
                    next_task=None if not work_que else work_que.popleft()
            if w>=curr_task[0]:
                total_profit+=curr_task[1]

        return total_profit


if __name__=="__main__":
    difficulty = [13,37,58]
    profit = [4,90,96]
    worker = [34,73,45]
    print(Solution().maxProfitAssignment(difficulty,profit,worker))