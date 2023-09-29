#link:https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s:str) -> bool:
        stack=[]
        pairs={"(":")",
               "{":"}",
               "[":"]"}
        break_ind=0
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif stack==[] or bracket!=pairs[stack.pop()]:
                break_ind=1

        if(len(stack)==0) and break_ind==0:
            return True
        else:
            return False


s=Solution()
print(s.isValid("]"))