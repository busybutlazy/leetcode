def merge(left_list, right_list):
    result=[]
    while len(left_list) and len(right_list):
        if left_list[0]<right_list[0]:
            result.append(left_list.pop(0))
        else:
            result.append(right_list.pop(0))
    result=result+left_list if len(left_list) else result+right_list
    return result

def merge_sort(nums):
    if len(nums)<2:
        return nums
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]
    return merge(merge_sort(left),merge_sort(right))
    
       
    
li=[1,2,6,9,14,3,-3,5,4]
print(merge_sort(li))