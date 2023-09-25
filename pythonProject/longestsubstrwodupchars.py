#https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str2 = list(s)
        itr1 = 0
        len_values = []
        while itr1 < len(str2):
            itr2 = itr1
            break_ind = 0
            longestsubstr = ""
            while itr2 < len(str2) and break_ind == 0:
                if (str2[itr2] in longestsubstr):
                    break_ind = 1
                else:
                    longestsubstr = longestsubstr + str2[itr2]
                itr2 = itr2 + 1
            len_values.append(len(longestsubstr))
            itr1 = itr1 + 1
        if(len_values==[]):
            return 0
        else:
            return max(len_values)


s=Solution()
print(s.lengthOfLongestSubstring(" "))
