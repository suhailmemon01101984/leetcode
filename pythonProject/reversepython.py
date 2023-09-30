#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self,x:int)->int:
        s=str(x)
        len_s=len(s)
        reversed_s=s[::-1]
        if(reversed_s[len_s-1]=='-'):
            reversed_s='-'+reversed_s[:len_s-1]
        int_reversed=int(reversed_s)
        if(int_reversed>=-2**31 and int_reversed<=(2**31)-1):
            return int(reversed_s)
        else:
            return 0


s=Solution()
print(s.reverse(2147483649))