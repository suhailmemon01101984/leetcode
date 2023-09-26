#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        itr1=0
        longestpdsubstr=""
        while itr1<len(s):
            itr2 = len(s)
            while itr2>itr1+1:
                substr1=s[itr1:itr2]
                if(substr1==substr1[::-1] and len(substr1)>len(longestpdsubstr)):
                    longestpdsubstr=substr1
                itr2=itr2-1
            itr1=itr1+1
        if(longestpdsubstr=="" and len(s)>=1):
            return s[0:1]
        else:
            return longestpdsubstr

s=Solution()
print(s.longestPalindrome("aacabdkacaa"))
