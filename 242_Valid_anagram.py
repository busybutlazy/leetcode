from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def make_dict(s):
            result=defaultdict(int)
            for c in s :
                result[c]+=1
            return result
        s_dict,t_dict=make_dict(s),make_dict(t)
        if len(s_dict)!=len(t_dict):
            return False
        for ele in s_dict :
            if ele not in t_dict:
                return False
            if s_dict[ele]!=t_dict[ele]:
                return False
        return True
    
