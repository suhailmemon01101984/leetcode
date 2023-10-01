#https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1:list[int], m:int, nums2:list[int], n )->None:
        nums1[m:m+n]=nums2
        nums1.sort()






s=Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)


