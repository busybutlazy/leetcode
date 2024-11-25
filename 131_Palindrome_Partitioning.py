class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.final_ans=[]
        if len(s)==1:
            return [s]
        else:
            self.wide(s,[])
        return self.final_ans
    
    def check_palin(self,sub_str):
        if len(sub_str)==0: return False
        if len(sub_str)==1: return True
        if len(sub_str)%2!=0:
            sub_str=sub_str[:len(sub_str)//2]+sub_str[len(sub_str)//2+1:]
        for i in range(len(sub_str)//2):
            if sub_str[i]==sub_str[len(sub_str)-i-1]:
                continue
            else:
                return False
        return True
    
    def wide(self,sub_str,ans_to_add):
        if len(sub_str)==0:
            self.final_ans.append(ans_to_add)
        elif len(sub_str)==1:
            ans_to_add.append(sub_str)
            self.final_ans.append(ans_to_add)
        else:
        # print("get para1=",sub_str,"para2=",ans_to_add)
            for i in range(1,len(sub_str)+1):
            # print(i,":",sub_str[:i])
                if self.check_palin(sub_str[:i]):
                    self.deep(sub_str[i:],ans_to_add+[sub_str[:i]])

            


    def deep(self,sub_str,ans_to_add):
        if len(sub_str)==0:
            self.final_ans.append(ans_to_add)
        elif len(sub_str)==1:
            ans_to_add.append(sub_str)
            self.final_ans.append(ans_to_add)
        else:    
            for i in range(1,len(sub_str)+1):
                if self.check_palin(sub_str[:i]):
                    self.wide(sub_str[i:],ans_to_add+[sub_str[:i]])

             


if __name__=="__main__":
    to_test="cdd"
    s=Solution()
    print(s.partition(to_test))