from collections import defaultdict

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        self.words=words
        self.score=score
        self.word_count=defaultdict()
        for word in words:
            tmp=defaultdict(int)
            for char in word:
                tmp[char]+=1
            self.word_count[word]=tmp.copy()
        
        left_letters=defaultdict(int)
        for char in letters:
            left_letters[char]+=1
        
        self.result=[]
        for i in range(len(words)):
            print("~~~~~start a new chain~~~~~")
            self.recursive(i,left_letters.copy(),0)
        print("===done=== all results =  ",self.result)
        return max(self.result)
        
    
    def recursive(self,now_index,left_letters,now_score):
        print("now_index: ",now_index) 
        if now_index == len(self.words):
            self.result.append(now_score)
            print("add result:",now_score)
            return
        
        
        # check validity
        score_2_add=0
        next_left=left_letters.copy()
        valid=True
        print("now check: ",self.words[now_index])
        print("left words are :",next_left)
        for c in self.word_count[self.words[now_index]]:
            print("c=",c)
            if c not in next_left or self.word_count[self.words[now_index]][c]>next_left[c]:
                valid=False
                print("invalid")
                break
            next_left[c]-=self.word_count[self.words[now_index]][c]
            score_2_add+=self.score[ord(c)-97]*self.word_count[self.words[now_index]][c]
                    
        if valid:
            print("valid")
            self.recursive(now_index+1,next_left,now_score+score_2_add)    
        self.recursive(now_index+1,left_letters,now_score)
            
        
    



if __name__ == '__main__':
    s=Solution()
    words=["dog","cat","dad","good"]
    letters=["a","a","c","d","d","d","g","o","o"]
    score=[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    print(s.maxScoreWords(words, letters, score))