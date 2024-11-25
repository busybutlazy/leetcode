from time import sleep 

class Solution:
    def numSteps(self, s: str) -> int:
        if s=="1":
            return 0
        
        self.result=0
        self.ss="a"+s
        self.port(self.ss[-1],1)
        
        
        return self.result
        
    def port(self,char,idx):
        if char=="0":
            self.tail_is_0(idx)
        else:
            self.tail_is_1(idx,idx)


        
    def tail_is_1(self,start,now):
        print("now at tail_is_1")
        print("self.ss[-(now+1)]=",self.ss[-(now+1)])
        print("start=",start,"  now=",now)
        if self.ss[-(now+1)]=="a":
            self.result+=now-start+2
            print("1 result=",self.result)
            print("==="*20)
            print("end point1")
            return
        elif self.ss[-(now+1)]=="1":
            self.tail_is_1(start,now+1)
        else:
            self.result+=now-start+2
            print("2 result=",self.result)
            print("==="*20)
            self.tail_is_1(now+1,now+1)
            
        

    def tail_is_0(self,idx):
        print("now at tail_is_0")
        print("self.ss[-idx]=",self.ss[-idx])
        self.result+=1
        idx+=1
        if self.ss[-(idx+1)]=="a":
            print("end point2")
            return
        print("3 result=",self.result)
        print("==="*20)
        self.port(self.ss[-idx],idx)
        


if __name__=="__main__":
    solution=Solution()
    s="1011001"
    print(solution.numSteps(s))