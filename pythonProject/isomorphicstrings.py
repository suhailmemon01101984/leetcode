class Solution:
    def isIsomorphic(self,s:str,t:str)->bool:
        #print(f"{s},{t}")
        dict1={}
        i=0
        if len(s)!=len(t):
            return False

        for letter in s:
            if letter in dict1 and dict1[letter][0]==t[i]:
                pass
            elif letter in dict1 and dict1[letter][0]!=t[i]:
                return False
            else:
                dict1.setdefault(letter, []).append(t[i])

            if len({j for j in dict1 if dict1[j][0]==t[i]})>1:
                return False
            i=i+1
            #print(dict1)
        return True


s=Solution()
#print(s.isIsomorphic("foo","bar"))
#print(s.isIsomorphic("badc","baba"))
#print(s.isIsomorphic("paper","title"))
print(s.isIsomorphic("egg","add"))



