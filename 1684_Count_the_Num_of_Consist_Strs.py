from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set(allowed)
        counter=0
        for word in words:
            if set(word).issubset(allowed_set):
                counter+=1
        return counter

if __name__=="__main__":
    sol=Solution()
    allowed="ab"
    words=["ad","bd","aaab","baa","badab"]
    print(sol.countConsistentStrings(allowed,words))