class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) >len(s2):
            return False
        s1count,s2count = {},{}
        
        for c in s1:
            s1count[c] = s1count.get(c,0)+1
        for c in s2[:len(s1)]:
            s2count[c] = s2count.get(c,0)+1
        
        if s1count == s2count:
            return True
        for r in range(len(s1),len(s2)):
            c = s2[r]
            s2count[c] = s2count.get(c,0)+1

            l = r-len(s1)
            c = s2[l]

            s2count[c] -= 1

            if s2count[c] == 0:
                del s2count[c]
            if s1count == s2count:
                return True
        return False
        


