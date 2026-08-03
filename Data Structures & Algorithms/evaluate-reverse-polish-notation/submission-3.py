class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ope = ('+','-','*','/')
        for i in tokens:
            if i in ope:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '+': stack.append(b+a)
                if i == '-': stack.append(b-a)
                if i == '*': stack.append(b*a)
                if i == '/': stack.append(b/a)
            else:
                stack.append(i)
        return int(stack[-1])  