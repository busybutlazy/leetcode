class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        modulo=int(1000000007)
        self.pow_of_2={}
        self.pow_of_2.update({"0":1})
        for i in range(1,n+1):
            self.pow_of_2.update({f"{i}":(self.pow_of_2[f"{i-1}"]*2)%modulo})
        
        self.record={"0":0,"1":0,"2":0,"3":1,"4":3,"5":8}
        to_minus=0
        
        for i in range(6,n+1):
            ans=(self.record[f"{i-1}"]+self.record[f"{i-2}"]+self.record[f"{i-3}"]+self.pow_of_2[f"{i-3}"])%modulo
            self.record.update({f"{i}":ans})
            
        to_minus=0
        
        for i in range(n):
            front=self.record[f"{i}"]
            back=self.record[f"{n-1-i}"]
            to_minus=(to_minus+self.pow_of_2[f"{i}"]*back+front*self.pow_of_2[f"{n-1-i}"]-front*back)%modulo
        
        return (self.pow_of_2[f"{n}"]-self.record[f"{n}"]+self.pow_of_2[f"{n-1}"]*n-to_minus)%modulo
        
    

if __name__ == '__main__':
    s=Solution()
    n=10101
    print(s.checkRecord(n))