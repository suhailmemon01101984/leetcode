#https://leetcode.com/problems/zigzag-conversion/description/
class Solution:
    def convert(self,s:str,numRows:int)->str:
        matrix=[[] for x in range(numRows)]
        if(numRows>=len(s) or numRows==1 or numRows==0):
            return s
        index=0
        step=1
        for char in s:
            matrix[index].append(char)
            if(index==0):
                step=1
            elif(index==numRows-1):
                step=-1
            index=index+step
        i=0
        output=''
        while i<len(matrix):
            output=output+''.join(matrix[i])
            i=i+1
        return output



s=Solution()
print(s.convert("PAYPALISHIRING",3))