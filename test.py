# x,y=1,0

# def turn (x,y):
#     x,y=y*-1,x
#     return x,y



# x,y=turn(x,y)
# print(x,y)
# x,y=turn(x,y)
# print(x,y)
# x,y=turn(x,y)
# print(x,y)

# def find_GCD(n1,n2):
#     if n2>=n1:
#         n1,n2=n2,n1
#     n1=n1-n2
#     if n1==n2:
#         return n1
#     else:
#         return find_GCD(n1,n2)
    
# print(find_GCD(10,6))

# def get_min_min(tps,new_tp:int):
#     l,r=0,len(tps)
#     m=(l+r)//2
#     while l<r:
        
#         if tps[m]>new_tp:
#             r=m-1
#         else:
#             l=m+1
#         m=(l+r)//2
#     return m,m+1
# li=[1,2,5,8,7,5,2,3,4,8,6,45,89,53,24,8532,452,865,452]
# li.sort()
# print(get_min_min(li,8531))
import time

def test1(num):
    for _ in range(num):
        li=[0]*num

def test2(num):
    for _ in range(num):
        s=set([0 for _ in range(num)])

def time_tester(fun,num):
    start_time = time.time()
    fun(num)
    end_time=time.time()
    execution_time = end_time - start_time

    print(f"Execution time : {execution_time} seconds")
num=50000
time_tester(test1,num)
time_tester(test2,num)

#3432 34