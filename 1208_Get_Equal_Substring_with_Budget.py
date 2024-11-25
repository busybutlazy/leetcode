class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs=[0]+[ord(s[i])-ord(t[i]) if ord(s[i])-ord(t[i])>=0 else ord(t[i])-ord(s[i]) for i in range(len(s))]
        print(costs)
        max_len=0
        now_cost=0
        start=0
        end=1
        
        while end<len(costs):
            now_cost+=costs[end]
            while now_cost>maxCost and end>start:
                start+=1
                now_cost-=costs[start]
            max_len=max(max_len,end-start)
            end+=1

        
        
        
        # for end in range(1,len(s)):
        #     if max_len>=len(costs)-end:
        #         break
        #     now_cost+=costs[end]
        #     print("start=",start,"end=",end,"now_cost=",now_cost,"costs[i]=",costs[end],"now_len=",end-start)
        #     if now_cost<=maxCost:
        #         max_len=max(max_len,end-start)
        #     while now_cost>maxCost and end>=start:
        #         now_cost-=costs[start+1]
        #         start+=1
        # max_len=max(max_len,end-start)
        
        return max_len
        
        
                

        
        
       

if __name__ == '__main__':
    solution=Solution()
    s="krrgw"
    t ="zjxss"
    maxCost = 19
    print(solution.equalSubstring(s, t, maxCost))