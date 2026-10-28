class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        str1 = {} 
        str2  = {}

        for i in range(len(s)):
            str1[s[i]] = str1.get(s[i],0)+1
            str2[t[i]] = str2.get(t[i],0)+1

        for n in str1:
            if str1[n] != str2.get(n,0):
                return False
        return True
            
        