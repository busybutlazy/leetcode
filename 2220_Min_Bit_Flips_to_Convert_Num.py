class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return format(start^goal,'b').count("1")
        
        # bi1=format(start,'b')
        # bi2=format(goal,'b')
        # if len(bi2)>=len(bi1):
        #     bi1,bi2=bi2,bi1
        # counter=0
        # for i in range(len(bi1)):            
        #     if i<len(bi1)-len(bi2):
        #         if bi1[i]=="1":
        #             counter+=1
        #         continue
        #     else:
        #         if bi1[i]!=bi2[i-(len(bi1)-len(bi2))]:
        #             counter+=1
        # return counter



if __name__=="__main__":
    sol=Solution()
    start,goal=99,29
    print(sol.minBitFlips(start,goal))