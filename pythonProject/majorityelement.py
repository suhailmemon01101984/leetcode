import math
from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
       a = Counter(nums)
       b = math.ceil(len(nums)/2)
       for i in nums:
           if a[i]>=b:
               return i

s=Solution()
print(s.majorityElement([1,2,1,1,2,1,2]))