class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # words=sentence.split(" ")
        # for i in range(len(words)-1):
        #     if words[i][-1]!=words[i+1][0]:
        #         return False
        # return words[0][0]==words[-1][-1]
        memo_char=""
        for i in range(len(sentence)):
            if sentence[i+1]==" ":
                memo_char=sentence[i]
            
        

if __name__ == '__main__':
    sol=Solution()
    sentence = "leetcode exercises sound delightful"
    print(sol.isCircularSentence(sentence))