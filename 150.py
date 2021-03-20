class Solution:
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c in '+-*/':
                n = stack.pop()
                nn = stack.pop()
                if c == '+':
                    stack.append(nn + n)
                elif c == '-':
                    stack.append(nn - n)
                elif c == '*':
                    stack.append(nn * n)
                elif c == '/':
                    stack.append(int(nn / n))
            else:
                stack.append(int(c))
        return stack.pop()
