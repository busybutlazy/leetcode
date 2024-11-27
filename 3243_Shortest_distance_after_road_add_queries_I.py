from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:        
        self.roads=[[i+1] for i in range(n-1)]
        self.goal=n-1
        ans=[]
        for path in queries:
            self.roads[path[0]].append(path[1])
            ans.append(self.bfs_find_shortest())
        
        return ans
    
    def bfs_find_shortest(self):
        step=1
        queue=self.roads[0].copy()
        next_queue=set()
        went_before=set()
        while queue:
            
            arrived_this_turn=set()
            loc=queue.pop()
            if loc == self.goal:
                return step
            
            if loc not in went_before:
                arrived_this_turn.add(loc)
                next_queue.update(set(self.roads[loc]))

            if not queue:
                went_before.update(arrived_this_turn)
                queue=next_queue
                next_queue=set()
                step+=1
        
        return -1


if __name__=="__main__":
    solution=Solution()
    n = 500
    queries = [[0,2]]
    print(solution.shortestDistanceAfterQueries(n,queries))