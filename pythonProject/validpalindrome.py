#https://leetcode.com/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150
import re
class Solution:
    def isPalindrome(self,s:str)->bool:
        lowercasestr=s.lower()
        alphanumremovedstr=re.sub(r'[^a-zA-Z0-9]', '', lowercasestr)
        if(alphanumremovedstr==alphanumremovedstr[::-1]):
            return True
        else:
            return False

s=Solution()
print(s.isPalindrome("ab_a"))
