class Solution:
    def isValid(self, s: str) -> bool:
        newmap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        res = []
        for i in s:
            if i == '{' or i == '[' or i =='(':
                res.append(i)
        
            if i == '}' or i == ']' or i ==')':
                if len(res)==0 or res[-1] != newmap[i]:
                   return False
                res.pop()
                
        return len(res) ==0

            

            
        