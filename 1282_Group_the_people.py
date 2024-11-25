from typing import List
class Solution:
    def __init__(self):
        self.results=[]
    
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        tmp_dict={}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in tmp_dict:
                tmp_dict.update({groupSizes[i]:[i]})
            else:
                tmp_dict[groupSizes[i]].append(i)
            if len(tmp_dict[groupSizes[i]])==groupSizes[i]:
                self.results.append(tmp_dict.pop(groupSizes[i]))
        print(tmp_dict)
        return self.results
    
s=Solution()
gtp=s.groupThePeople
groupSizes = [3,3,3,3,3,1,3]
print(gtp(groupSizes))