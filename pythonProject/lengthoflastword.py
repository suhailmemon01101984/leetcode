#https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLastWord(self,s:str)->int:
        word_list=s.split()
        for i in word_list[-1:]:
            return len(i)



s=Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))