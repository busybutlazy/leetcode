class Solution:
    def merge(self, nums1:list, m: int, nums2:list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if (n!=0 and m!=0):
            p1,p2=0,0
            tmp=nums1.copy()
            tmp_num=0
            while(p1<m or p2<n):
                if(p1>=m):
                    tmp_num=nums2[p2]
                    p2+=1
                elif(p2>=n):
                    tmp_num=tmp[p1]
                    p1+=1
                elif(tmp[p1]>nums2[p2]):
                    tmp_num=nums2[p2]
                    p2+=1
                else:
                    tmp_num=tmp[p1]
                    p1+=1
                nums1[p1+p2]=tmp_num
        elif(m==0):
            for i in range(len(nums2)):
                nums1[i]=nums2[i]
        return nums1

merge=Solution().merge
print(merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))