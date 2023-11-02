#https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def canConstruct(self,ransomNote:str, magazine:str)->bool:
        #print(f"{ransomNote},{magazine}")
        if ransomNote in magazine:
            return True
        for letter in ransomNote:
            #print(letter)
            idx=magazine.find(letter)
            magazine=magazine[:idx]+magazine[idx+1:]
            if idx==-1:
                return False
        return True




s=Solution()
print(s.canConstruct("aa","aab"))