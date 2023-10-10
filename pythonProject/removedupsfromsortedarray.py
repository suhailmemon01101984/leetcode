#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def removeDuplicates(self,nums:list[int])->int:
        i=0
        l=len(nums)
        while i < len(nums)-1:
            #print(f"before->i:{i},l={len(nums)},nums_i={nums[i]},nums_ip1={nums[i+1]}")
            if nums[i]==nums[i+1] and i!=len(nums)-1:
                del nums[i]
                i=i-1
            #print(f"after->i:{i},l={len(nums)},nums_i={nums[i]},nums_ip1={nums[i+1]}")
            i=i+1
        return(len(nums))

s=Solution()
nums1=[0,0,1,1,1,2,2,3,3,4]
print(nums1)
print(s.removeDuplicates(nums1))
print(nums1)