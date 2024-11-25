def stand_triangle():
    for i in range(5):
        for j in range(5):
            if i>=j :
                print("*",end="")
        print("\n")
    
def upright_triangle():
    for i in range(5):
        for j in range(5):
            if i<5-j:
                print("*",end="")
        print("\n")

def num_triangle():
    n=0
    for i in range(5):
        for j in range(5):
           if i>=j:
               n+=1
               print(n," ",end="")
        print("\n")
        
        
def recursion_triangle(n):
    if n == 1 :
        print("*"*n)
    else :
        # print("*"*n)
        recursion_triangle(n-1)
        print("*"*n)

def recursion_num_triangle(n):
    if n==1:
        print(n)
        return 1
    else:
        count=recursion_num_triangle(n-1)
        for i in range(n):
            count+=1
            print(count,end="")
        print("")
        return count

recursion_num_triangle(5)