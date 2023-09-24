#https://leetcode.com/problems/median-of-two-sorted-arrays/
from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array=nums1+nums2
        return(median(sorted(merged_array)))



s=Solution()
arr1=[1,2]
arr2=[4,3]
print(s.findMedianSortedArrays(arr1,arr2))

