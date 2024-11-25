def merge(arr1,arr2):
        sorted=[]
        while len(arr1) and len(arr2):
            if arr1[0]<arr2[0]:
                sorted.append(arr1.pop(0))
            else:
                sorted.append(arr2.pop(0))
        if len(arr1)==0:
            sorted+=arr2
        else:
            sorted+=arr1
        return sorted

def merge_sort(arr):
    if len(arr)<2:
        return arr
    else:
        return merge(merge_sort(arr[:len(arr)//2]),merge_sort(arr[len(arr)//2:]))






print(merge_sort([1,5,6,7,23,4,3,22]))
