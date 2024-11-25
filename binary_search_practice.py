import math
li=[i *3 for i in range(10)]*3
li.sort()
print(f"li : {li}")
# def bi_search(li,high,low,target):
#     if high<low:
#         return False
#     mid = (high + low)//2
#     if li[mid]==target:
#         return True
#     elif li[mid]>target:
#         return bi_search(li,mid-1,low,target)
#     elif li[mid]<target:
#         return bi_search(li,high,mid+1,target)

# print(bi_search(li,len(li),0,11))

def bi_search_head(li,target,exact=False):
    l,r=0,len(li)-1
    mid = (l+r)//2
    while l < r :
        if li[mid]>= target:
            r = mid
        else:
            l = mid +1
        mid = (l+r)//2
        
    if exact and li[mid]!=target:
        raise ValueError(f"Cant find target {target}")
    
    return mid 

def bi_search_tail(li,target,exact=False):
    l,r=0,len(li)-1
    mid = (l+r)//2
    while l < r:
        if li[mid]<=target:
            l = mid
        else:
            r = mid-1
        mid = math.ceil((l+r)/2)
    
    if exact and li[mid]!=target:
        raise ValueError(f"Cant find target {target}")
    return mid 

ans = bi_search_head(li, 5,exact=True)
print(f"Search head | loc : {ans} , value : {li[ans]} , windows : {li[max(ans-1,0):min(ans+2,len(li))]}")

ans = bi_search_tail(li, 24,exact=True)
print(f"Search tail | loc : {ans} , value : {li[ans]} , windows : {li[max(ans-1,0):min(ans+2,len(li))]}")