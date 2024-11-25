class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_len=len(s)
        t_len=len(t)
        
    
        def recursive(idx_of_s,idx_of_t):
            if idx_of_t==t_len:
                return idx_of_t
            while idx_of_s<s_len:
                if s[idx_of_s]==t[idx_of_t]:
                    return recursive(idx_of_s+1,idx_of_t+1)
                else:
                    idx_of_s+=1
                    continue
            return idx_of_t

        result=recursive(0,0)
        
        return t_len-result
    
    
if __name__ == '__main__':
    solution=Solution()
    s="coaching"
    t="coding"
    print(solution.appendCharacters(s, t))