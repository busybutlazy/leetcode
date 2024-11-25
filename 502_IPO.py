from typing import List
from queue import deque
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hash_map={}
        for i in range(len(capital)):
            if capital[i] not in hash_map:
                hash_map[capital[i]]=profits[i]
            else:
                hash_map[capital[i]]=max(hash_map[capital[i]],profits[i])
        capital.sort()
        
        my_que=deque()
        
        curr_profit=0
        for c in capital:
            if hash_map[c]>curr_profit:
                curr_profit=hash_map[c]
                my_que.append((c,curr_profit))

        
        now_project=my_que.popleft()
        next_project=None
        print("my_que=",my_que)
        if my_que:
            next_project=my_que.popleft()

        

        while k>0:
            print("now_project=",now_project)
            print("next_project=",next_project)
            
            if next_project==None:
                # do now project
                pass
            # elif w>=now_project[0] and w<next_project[0]:
            #     # do now project
            #     pass
            elif w<now_project[0]:
                return w
            elif w>=next_project[0]:
                # switch project
                if my_que:
                    now_project,next_project=next_project,my_que.popleft()
                else:
                    now_project,next_project=next_project,None
                continue
            w+=now_project[1]
            k-=1


        return w

if __name__=="__main__":
    k = 3
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]
    print(Solution().findMaximizedCapital(k,w,profits,capital))