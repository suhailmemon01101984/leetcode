#https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self,s:str,t:str)->bool:
        i=0
        issub_ind=0
        if s in t:
            return True
        for j in s:
            idx=t.find(j)
            if idx==-1:
                return False
            else:
                issub_ind=issub_ind+1
                t = t[idx + 1:]

            i=i+1
        if issub_ind==len(s):
            return True
        else:
            return False

s=Solution()
print(s.isSubsequence("axc","ahbgdcx"))