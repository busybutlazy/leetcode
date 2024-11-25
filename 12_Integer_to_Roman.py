class Solution:
    def intToRoman(self, num: int) -> str:
        int2roman={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",900:"CM",400:"CD",90:"XC",40:"XL",9:"IX",4:"IV"}
        num_to_check=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result=""
        for i in range(len(num_to_check)):
            print("num=",num,"num_to_check[i]=",num_to_check[i])
            times=num//num_to_check[i]
            num=num%num_to_check[i]
            result+=int2roman[num_to_check[i]]*times
        
        return result

if __name__=="__main__":
    solution=Solution()
    num=1994
    print(solution.intToRoman(num))