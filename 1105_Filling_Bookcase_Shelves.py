from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        height=0
        tmp_height=0
        tmp_wid=0
        for book in books:
            print("tmp_height=",tmp_height,"  tmp_wid=",tmp_wid,"  height=",height)
            print("book=",book)
            if tmp_wid+book[0]<=shelfWidth:
                tmp_wid+=book[0]
                tmp_height=max(tmp_height,book[1])
            else:
                print("add",tmp_height)
                height+=tmp_height
                tmp_wid=book[0]
                tmp_height=book[1]
        height+=tmp_height
        return height

if __name__=="__main__":
    sol=Solution()
    books=[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    print(sol.minHeightShelves(books,shelfWidth))