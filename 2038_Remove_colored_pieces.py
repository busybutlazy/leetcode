class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) <3:
            return False
        
        colors+="C"
        
        i,j=1,1
        turn=True
        while i+1 < len(colors) and j+1 < len(colors):
            if turn:
                if colors[i+1]=="A" and colors[i-1]=="A" and colors[i]=="A":
                    turn = False
                i+=1
            else:
                if colors[j+1]=="B" and colors[j-1]=="B" and colors[j]=="B":
                    turn = True
                j+=1
        return i<j
        
        
s=Solution()
wog=s.winnerOfGame
colors = "ABBBAAA"
if wog(colors):
    print("A win")
else:
    print("B win")