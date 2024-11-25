class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n <3:
            return n*5
        
        def fit(num: int)-> int:
            M=1000000007
            if num<M:
                return num
            else:
                return num%M
        
        def count(li,n):
            if n==1:
                return fit(sum(li))
            else:
                li=[fit(li[1]),fit(li[0]+li[2]),fit(sum(li)-li[2]),fit(li[2]+li[4]),fit(li[0])]
                return count(li,n-1)
        
        return count([1,1,1,1,1],n)

s=Solution()
n=5
print(s.countVowelPermutation(n))