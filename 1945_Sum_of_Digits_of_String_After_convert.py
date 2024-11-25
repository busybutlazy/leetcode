class Solution:
    def getLucky(self,s,k)->int:
        

        def convert(s)->int:
            num_string=""
            
            for w in s:
                num_string+=str(ord(w)-96)
            return int(num_string)
        

        def transform(num_string)->int:
            num_string=str(num_string)
            sum_of_num=0
            for w in num_string:
                sum_of_num+=int(w)
            return sum_of_num
        
        num_string=convert(s)
        for _ in range(k):
            num_string=transform(num_string)

        return int(num_string)


if __name__=="__main__":
    solution= Solution()
    s="leetcode"
    k=2
    print(solution.getLucky(s,k))