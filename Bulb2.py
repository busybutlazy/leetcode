def bulb(n):
    i=0
    while n>0:
        n-=(2*(i+1))+1
        i+=1
    return i

def bulb2(n):
    return int(n**0.5)

for i in range(40):
    print(i,"->",bulb(i))
    print(i,"->",bulb2(i))