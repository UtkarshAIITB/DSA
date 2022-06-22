# link: https://leetcode.com/problems/merge-sorted-array/solution/

nums1 = [0]
m = 0
nums2 = [1]
n = 1

if (m!=0 and n!=0):
    nums1Copy = nums1[:m]
    p1 = 0
    p2 = 0
    p = 0
    for p in range(m+n): 
        if (p1<m and nums1Copy[p1]<=nums2[p2]) or (p2>=n):
            nums1[p] = nums1Copy[p1]
            p1+=1
        else:
            nums1[p] = nums2[p2]
            p2+=1

if(m==0 and n!=0):
    nums1 = nums2

print(nums1)

# time complexity = O(m+n)