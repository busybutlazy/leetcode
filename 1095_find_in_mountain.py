from collections import defaultdict

class MountainArray:
   def __init__(self,arr):
       self.arr=arr
   
   def get(self, index: int) -> int:
       return self.arr[index]
   
   def length(self) -> int:
       return len(self.arr)




class Solution:
    def __init__(self):
        self.dp=defaultdict(int)
        self.m_arr=None
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        self.m_arr=mountain_arr
        if target<self.get_height(0) and target<self.get_height(mountain_arr.length()-1):
            return -1
        # find top
        top=self.m_arr.length()//2
        to_move=max(top//2,1)
        while True:
            l,m,r=self.get_three_height(top)
            if l<m and m<r:
                top+=to_move
            elif l>m and m>r:
                top-=to_move
            else:
                break
            to_move=to_move//2
        if target>self.get_height(top):
            return -1
        
        if target==self.get_height(top):
            return top
        
        
        left,right=0,top-1
        while left<=right:
            mid=(left+right)//2
            if target==self.get_height(mid):
                return mid
            elif target>self.get_height(mid):
                left=mid+1
            elif target<self.get_height(mid):
                right=mid-1
        

        left,right=top+1,mountain_arr.length()-1
        while left<=right:
            print("left=",left," right=",right)
            mid=(left+right+1)//2
            if target==self.get_height(mid):
                return mid
            elif target>self.get_height(mid):
                right=mid-1
            elif target<self.get_height(mid):
                left=mid+1
        return -1

        
        
    
    def get_height(self,index):
        if index not in self.dp:
            self.dp[index]=self.m_arr.get(index)
        return self.dp[index]
    
    def get_three_height(self,index):
        return self.get_height(index-1),self.get_height(index),self.get_height(index+1)
        


m=MountainArray([0,2,4,3,2,1])
s=Solution()
print(s.findInMountainArray(3,m))