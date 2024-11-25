def bulb(n):
    on_num=0
    for i in range(1,n+1):
        if (find_factor(i)%2==1):
            on_num+=1
    return on_num          
    
def find_factor(n):
    factors=0
    tmp=0
    for i in range(1,int(n**0.5)+1):
        if (n%i==0):
            factors+=1
            tmp=i
    if (tmp**2==n):
        return factors*2-1
    return factors*2

for i in range(40):
    print(i,"->",bulb(i))