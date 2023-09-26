class Solution:
    def romanToInt(self, s: str) -> int:
        str1 = s.replace("IV",",4,")
        str1 = str1.replace("IX", ",9,")
        str1 = str1.replace("XL", ",40,")
        str1 = str1.replace("XC", ",90,")
        str1 = str1.replace("CD", ",400,")
        str1 = str1.replace("CM", ",900,")
        str1 = str1.replace("I", ",1,")
        str1 = str1.replace("V", ",5,")
        str1 = str1.replace("X", ",10,")
        str1 = str1.replace("L", ",50,")
        str1 = str1.replace("C", ",100,")
        str1 = str1.replace("D", ",500,")
        str1 = str1.replace("M", ",1000,")
        str1 = str1.replace(",,", ",0,")
        str1 = str1.removesuffix(",")
        str1 = str1.removeprefix(",")
        nums = [int(n) for n in str1.split(",")]
        return sum(nums)

s=Solution()
print(s.romanToInt("MCMXCIV"))

