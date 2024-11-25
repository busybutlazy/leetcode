from collections import defaultdict
class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.pow_dic=defaultdict(float)

        self.pow_dic[0]=1/1
        self.pow_dic[1]=x/1
        
        nagetive=False
        if n <0:
            n=-n
            nagetive=True
            
        def helper(x,n):
            while n not in self.pow_dic:
                print(n)
                self.pow_dic[n]=self.pow_dic[max(self.pow_dic)]*self.pow_dic[n-max(self.pow_dic)]
            return self.pow_dic[n]
        
        ans = helper(x,n)
        if nagetive:
            ans=1/ans
        return self.pow_dic

s=Solution()
print(s.myPow(2,3))
# print(max({1:5,2:3,4:8}))
