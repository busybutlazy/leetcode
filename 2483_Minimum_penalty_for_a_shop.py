class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_penalty,penalty,tmp_index=0,0,len(customers)
        for i in range(len(customers)-1,-1,-1):
            if customers[i]=="Y":
                penalty-=1
            else:
                penalty+=1
            print("i=",i,"penalty=",penalty,"max_penalty=",max_penalty)
            if penalty>=max_penalty:
                max_penalty=penalty
                tmp_index=i
        return tmp_index
            
    
s=Solution()
bct=s.bestClosingTime
customers = "YN"
print(bct(customers))