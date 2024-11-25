from typing import List
from random import randint
"""
From ChatGPT
The Dutch National Flag (DNF) algorithm efficiently sorts numsays with 
three distinct types of elements by partitioning them based on a single pass-through. 
It's adaptable for numsays with more than three types, finding applications in diverse 
fields like data processing and algorithm design.

It can also be used for more than four types of items, 
but as the number of types increases, there can be greater complexity in terms of time.
"""

def dutch_national_flag_3(nums:List[int]):
    low,mid,hight=0,0,len(nums)-1
    while mid <= hight:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
            
        elif nums[mid]==1:
            mid+=1
            
        elif nums[mid]==2:
            nums[hight],nums[mid]=nums[mid],nums[hight]
            hight-=1

def dutch_national_flag_4(nums:List[int]):
    low = 0
    mid1 = 0
    mid2 = 0
    high = len(nums) - 1

    while mid2 <= high:
        if nums[mid2] == 0:
            nums[low],nums[mid1] ,nums[mid2] = nums[mid2], nums[low],nums[mid1]
            low += 1
            mid1 += 1
            mid2 += 1
        elif nums[mid2] == 1:
            nums[mid1], nums[mid2] = nums[mid2], nums[mid1]
            mid1 +=1
            mid2 += 1
        elif nums[mid2] == 2:
            mid2 += 1
        else:
            nums[mid2], nums[high] = nums[high], nums[mid2]
            high -= 1
    


if __name__=="__main__":
    nums= [randint(0,3) for _ in range(350)]
    dutch_national_flag_4(nums)
    print(nums)