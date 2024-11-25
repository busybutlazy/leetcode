nums=[4,10,4,3,8,9]


temp_lis=[]
position=[0 for i in range(len(nums))]

"""
LIS ( Longest Increasing Subsequence )
Robinson_Schensted_Knuth algorithm
"""

# init
temp_lis.append(nums[0])
position[0]=0

for i in range(1,len(nums)):
    if temp_lis[-1]<nums[i]:
        temp_lis.append(nums[i])
        position[i]=position[i-1]+1
    else:
        left=0
        right=len(temp_lis)-1
        while left<right:
            mid=left+(right-left)//2
            if temp_lis[mid]<nums[i]:
                left=mid+1
            else:
                right=mid
        temp_lis[left]=nums[i]
        position[i]=position[left]


print(temp_lis)
print(position)

"""
sequence : -7 10  9  2  3  8  8  1
temp LIS :
position :

sequence :(-7)10  9  2  3  8  8  1
temp LIS : -7
position :  1		// -7 在 LIS 的第一個位置

sequence : -7(10) 9  2  3  8  8  1
temp LIS : -7 10
position :  1  2	// 10 在 LIS 的第二個位置，以此類推。

sequence : -7 10 (9) 2  3  8  8  1
temp LIS : -7  9
position :  1  2  2
/* 9 成為 LIS 的潛力比 10 大, 所以以 9 代替 10 */

sequence : -7 10  9 (2) 3  8  8  1
temp LIS : -7  2
position :  1  2  2  2
/* 2 成為 LIS 的潛力比 9 大, 所以以 2 代替 9 */

sequence : -7 10  9  2 (3) 8  8  1
temp LIS : -7  2  3
position :  1  2  2  2  3

sequence : -7 10  9  2  3 (8) 8  1
temp LIS : -7  2  3  8
position :  1  2  2  2  3  4

sequence : -7 10  9  2  3  8 (8) 1
temp LIS : -7  2  3  8
position :  1  2  2  2  3  4  4
/* 8 成為 LIS 的潛力比 8 大, 所以以 8 代替 8 */

sequence : -7 10  9  2  3  8  8 (1)
temp LIS : -7  1  3  8
position :  1  2  2  2  3  4  4  2
/* 1 成為 LIS 的潛力比 2 大, 所以以 1 代替 2 */
"""