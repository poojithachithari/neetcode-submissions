class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str1 = dict()
        str2 =dict()
        for i in range(len(s)):
            str1[s[i]] = str1.get(s[i],0)+1
            str2[t[i]] = str2.get(t[i],0)+1
        for c in str1:
            if str1[c] != str2.get(c,0):
               return False

        
        
        return True
        
        