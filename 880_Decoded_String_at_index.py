
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        k-=1
        if ord(s[-1])>57:s=s+"1"
        to_mul,to_add=[],[]
        tmp=""
        for c in s:
            if ord(c) >57:
                tmp=tmp+c
            else:
                to_add.append(tmp)
                tmp=""
                to_mul.append(int(c))        
        sum=self.counter(to_mul,to_add)
        
        for i in range(len(to_add)-1,-1,-1):
            k=k%sum[i]
            if i==0:
                return to_add[0][k]
            elif k>=sum[i-1]*to_mul[i-1]:
                return to_add[i][k-(sum[i-1]*to_mul[i-1])]
            
        
            
    def counter(self,to_mul,to_add):
        tmp,sum=0,[]
        for i in range(len(to_mul)):
            tmp+=len(to_add[i])
            sum.append(tmp)
            tmp*=to_mul[i]
        return sum
        

sol=Solution()
dai=sol.decodeAtIndex

s = "a93829"
k = 2

print(dai(s,k))