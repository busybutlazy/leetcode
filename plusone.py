
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    nine_num=0
    for i in reversed(digits):
        if i==9:
            nine_num+=1
        else:
            break
    
    
    if nine_num!=0:
        if(nine_num==len(digits)):
            digits.insert(0, 0)
        for i in range(nine_num):
            digits[-(i+1)]=0
    digits[-(nine_num+1)]+=1

    return digits


print(plusOne([1,2,3]))

alist=[1,2,3,5,6,7,8,9]
alist[-5:]=[0,0,0,0,0]
print(alist)