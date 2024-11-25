class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows==1):return s
        unit_num=(numRows-1)*2
        strs={i:"" for i in range(numRows)}
        for i in range(len(s)):
            if i%unit_num<numRows:
                strs[i%unit_num]+=s[i]
            else:
                strs[unit_num-i%unit_num]+=s[i]
        ans=""
        for i in range(numRows):
            ans+=strs[i]
        return ans
        
        
        
        
sol=Solution()
# s = "PAYPALISHIRING" 
# numRows = 3

s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s,numRows))