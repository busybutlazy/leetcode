from typing import List

class Fib_Search():
    def __init__(self,arr:List[int]=None) -> None:
        self.arr=arr if arr else None
        if arr:
            self.update_tree(arr)
    
    def update_tree(self,arr:List[int]=None)-> None:
        arr_len=len(arr)
        self.fib_arr=[1,1]
        while self.fib_arr[-1]<arr_len:
            self.fib_arr.append(self.fib_arr[-1]+self.fib_arr[-2])
        # print("fib_arr=",self.fib_arr)
        self.start_idex=self.fib_arr[-2]-1
        self.start_level=len(self.fib_arr)-4
    
    def search_index(self,target:int,print_status:bool=False)->int:
        """
        Return the index exactly equal to target or the nearest small one.\n
        It only can success with the array is sorted and the element in the array must be unique.
        """

        if self.arr == None:
            raise Exception("Use update_tree to add array or build the Fib_Search with a array.")
        elif len(self.arr)==1:
            return 0
        
        index=self.start_idex
        k=self.start_level

        result=0
        while k>=0:
            if print_status:
                print("index=",index,"k=",k)
            if index>=len(self.arr):
                result=len(self.arr)-1
                break
                
            if self.arr[index]<=target and self.arr[index+1]>target:
                result=index
                break
            else:
                if self.arr[index]>target:
                    index-=self.fib_arr[k]
                else:
                    index+=self.fib_arr[k]
            k-=1
        if print_status:
            print("final result=",index," steps=",self.start_level-k+1)
        
        return result


if __name__=="__main__":
    from random import randint
    # arr=[n*5+randint(0,5) for n in range(int(2*1e6))]
    arr=[5,7,12,23,25,37,48,54,68,77,91,99,102,110,118,120,130,135,136,150]
    arr.sort()
    fs=Fib_Search(arr)
    result=fs.search_index(68,print_status=True)
    print(result)
    print(arr[result-2:result+3])

