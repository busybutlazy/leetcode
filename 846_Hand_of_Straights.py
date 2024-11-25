from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If groupSize ==1 all arr can fit.
        if groupSize==1:
            return True
        

        # In these two situation. It's impossible to fit.
        if len(hand)%groupSize!=0 or len(hand)<groupSize:
            return False
        
        # Sort the list. Time complexity = BigO(n*lg n)
        hand.sort()

        # List to put cardpiles which len < groupSize. 
        undone_lists=[]

        # Test all card
        for i in range(len(hand)):
            used=False
            # record the cardpile which len=groupSize.
            to_remove=[]
            
            for undone in undone_lists:
                # If the cardpile need a card smaller then this card. It means this cardpile will never fit in groupSize.
                if hand[i]>undone[0]+groupSize-1:
                    return False

                if hand[i]==undone[-1]+1:
                    undone.append(hand[i])
                    if len(undone)==groupSize:
                        to_remove.append(undone)
                    used=True
                    break
            
            for rm in to_remove:
                undone_lists.remove(rm)
            
            # If this card didn't match every cardpile in undone_lists. It must be the new head of cardpile.
            if not used:
                undone_lists.append([hand[i]])



        return len(undone_lists)==0

        




if __name__=="__main__":
    solution=Solution()
    hand=[1]
    groupSize=1
    print(solution.isNStraightHand(hand,groupSize))