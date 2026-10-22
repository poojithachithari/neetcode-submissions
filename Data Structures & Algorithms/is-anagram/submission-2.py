from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Approch 1
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False

        #Approch 2
        #using Builtin Counter 
        s = Counter(s)
        t = Counter(t)
        if s == t:
            return True
        else:
            return False
        
        