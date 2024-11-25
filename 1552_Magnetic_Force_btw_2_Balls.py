from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        position_len=len(position)
        start_point=position[0]
        for i in range(position_len):
            position[i]-=start_point
        
        print(position)

        # distance_difference=[position[i]-position[i-1] if i !=0 else 0 for i in range(position_len)]


        def binary_search(start_idx:int,last_dp:List[int],new_bucket_loc:int)->int:
            """
            Give last dp and the new bucket position.\n
            Return this dp val.
            """
            l,r=start_idx,new_bucket_loc-1
            mid=(l+r)//2

            while l<r:                
                print(f"l={l}, r={r}")
                print(f"last_dp[{mid-1}]={last_dp[mid-1]} , last_dp[{mid}]={last_dp[mid]}")
                if last_dp[mid-1]<position[new_bucket_loc]-position[mid-1] and last_dp[mid]>=position[new_bucket_loc]-position[mid]:
                    break
                elif last_dp[mid]<position[new_bucket_loc]-position[mid]:
                    l=mid+1
                elif last_dp[mid]>position[new_bucket_loc]-position[mid]:
                # else:
                    r=mid-1
                mid=(l+r)//2
            
            loc_a=(mid-1,min(last_dp[mid-1],position[new_bucket_loc]-position[mid-1]))
            loc_b=(mid,min(last_dp[mid],position[new_bucket_loc]-position[mid]))

            return loc_a if loc_a[1]>loc_b[1] else loc_b



        dp=[[0 for _ in range(len(position))]for _ in range(m-1)]
        for i in range(position_len):
            dp[0][i]=position[i]-position[0]
        # for j in range(position_len):
        #     if j <=0:
        #         continue
        #     dp[1][j]=binary_search(dp[0],position[j])
        # print(f"i={i},dp={dp}")


        for i in range(1,m-1):
            next_startpoint=i+1
            for j in range(i,position_len-(m-2)+i):
                if j==i:
                    dp[i][j]=min(dp[i-1][j-1],position[j]-position[j-1])
                    continue
                next_startpoint,dp[i][j]=binary_search(next_startpoint,dp[i-1],j)
        print(f"dp={dp}")

        return dp[-1][-1]
    
        
        
        
        
        
        
        
        # position.sort()
        # length=position[-1]-position[0]
        # print(f"sorted position : {position}")
        # if m==2:
        #     return length

        # predic_distance=length//(m-1)
        # # ball_predic_val=[predic_distance*i+position[0] for i in range(m-1)]

        # def binary_search(start_loc:int,end_loc:int,val:int)->int:
        #     l,r=start_loc,end_loc
        #     if l==r: return l
        #     mid=(l+r)//2
        #     while l<r:
        #         if position[mid]==val:
        #             break
        #         elif position[mid-1]<val and position[mid]>val:
        #             return mid if position[mid]-val<val-position[mid-1] else mid-1
        #         elif position[mid]>val:
        #             r=mid
        #         elif position[mid]<val:
        #             l=mid+1
        #         mid=(l+r)//2
        #     return mid
        # print(f"predic_distance={predic_distance}")
        # min_distance=position[-1]
        # p1_loc=0
        # for i in range(0,m-2):
        #     # find actual p2 loc
        #     pre_val=position[p1_loc]+predic_distance
        #     if position[p1_loc+1]-position[p1_loc]>=min(min_distance,predic_distance):
        #         p2_loc=p1_loc+1
        #         print("skip")
        #     else:
        #         p2_loc=binary_search(p1_loc+1,len(position)-(m-i-1)-1,pre_val)
        #         print(f"start loc={p1_loc+1},end_loc={len(position)-(m-i-1)},pre_val={pre_val}")
        #     min_distance=min(position[p2_loc]-position[p1_loc],min_distance)
        #     print(f"p2_loc={p2_loc},actual val={position[p2_loc]}, min_distance={min_distance}\n")
        #     p1_loc=p2_loc
        # min_distance=min(position[-1]-position[p1_loc],min_distance)

        # return min_distance
    
    

if __name__=="__main__":
    position,m=[1,2,3,4,7],3 #output 3
    # position,m=[79,74,57,22],4 #output 5
    # position,m=[269826447,974181916,2251871443,189215924,664652743,592895362,754562271,335067223,996014894,510353008,48640772,228945137],3 #output 461712236
    # position,m=[4784,9049,3151,7537,2734,1287,2875,6770,9565,6254,6898,2509,6583],13 #128
    position,m=[82,68,79,17,70,51,5,46,27,44,39,57,94,45,88,56],9
    
    print(Solution().maxDistance(position,m))
    