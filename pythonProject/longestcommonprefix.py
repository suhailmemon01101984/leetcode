#https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution:
    def longestCommonPrefix(self,strs: list[str]) -> str:
        min_len=len(min(strs, key=len))
        itr1=0
        break_ind=0
        longestprefix=""
        #print(min_len)
        while itr1<min_len and break_ind==0:
            new_list = [item[itr1] for item in strs]
            result = new_list.count(new_list[0]) == len(new_list)
            if(result):
                longestprefix=longestprefix+new_list[0]
            else:
                break_ind=1
            itr1=itr1+1
            #print(f"itr1:{itr1},break_ind={break_ind},longestprefix={longestprefix},new_list={new_list},result={result}")
        return longestprefix



s=Solution()
l=["flower","flow","flight"]
print(s.longestCommonPrefix(l))
