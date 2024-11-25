class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return -self.do_r(-x,n=True)
        elif x<10:
            return x
        else:
            return self.do_r(x)
        
    def do_r(self,x,n=False):
        s=str(x)
        s=s[::-1]
        ans=int(s)
        if (ans>2**31-1 and n==True)or(ans>2**31 and n==False):
            return 0
        return ans
        
        
        

s=Solution()
x=123
print(f"{x} is ",s.reverse(x))
x=-123
print(f"{x} is ",s.reverse(x))
x=120
print(f"{x} is ",s.reverse(x))