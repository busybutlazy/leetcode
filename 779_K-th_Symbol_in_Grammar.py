class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # def power_of_two(n):
        #     if n==0:
        #         return 1
        #     elif n>0:
        #         return 2*power_of_two(n-1)
        k-=1
        same=True
        while k>1:
            half_len=2**(n-1)
            if k>half_len:
                same=not same
                k=k%half_len
            n=n-1
        if same:
            return int("01"[k])
        else:
            return int("10"[k])

                
                
    
        
        
    
    
    
    
    
s=Solution()
n=3
k=3
print(s.kthGrammar(n,k))
