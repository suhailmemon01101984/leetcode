#https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeElement(self,nums:list[int],val:int)->int:
        k=0
        for item in range(0,len(nums)):
            if nums[item]==val:
                nums[item]=9999999
            else:
                k=k+1
        nums.sort()
        return k


s=Solution()
nums=[0,1,2,2,3,0,4,2]
print(s.removeElement(nums,2))
print(nums)

