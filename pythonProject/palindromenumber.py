#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self,x:int)->bool:
        str_x=str(x)
        str_reverse=str_x[::-1]
        if(str_x==str_reverse):
            return True
        else:
            return False



s=Solution()
print(s.isPalindrome(121))