#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self,nums:list[int],k:int)->None:
        #print(f"{nums},{k}")
        #print(nums[-k:])
        #print(nums[:len(nums)-k])
        if k>len(nums):
            k=k%len(nums)
        list1=nums[-k:]+nums[:len(nums)-k]
        i=0
        while i<len(nums):
            nums[i]=list1[i]
            i=i+1







s=Solution()
nums1=[1,2]
s.rotate(nums1,3)
print(nums1)