class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        pow_2=set()
        root=int(c**0.5)
        
        for num in range(root+1):
            pow_2.add(c-(num*num))
            if num*num in pow_2 :
                return True
        return False
    
if __name__=="__main__":
    c=0
    print(Solution().judgeSquareSum(c))