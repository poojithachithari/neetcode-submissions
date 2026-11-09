class Solution:
    def isValid(self, s: str) -> bool:
        resmap = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for c in s:
            if c in resmap:
                if stack and stack[-1] == resmap[c]:
                    stack.pop()
                else:
                    return False
            else:
               stack.append(c)
        return True if not stack else False
        