#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def strStr(self,haystack:str, needle:str)->int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1




s=Solution()
print(s.strStr("leetcode","leeto"))