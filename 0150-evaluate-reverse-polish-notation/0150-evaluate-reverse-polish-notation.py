class Solution:
    def evalRPN(self, tokens):
        stack = []

        for x in tokens:
            if x in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if x == "+":
                    stack.append(a + b)
                elif x == "-":
                    stack.append(a - b)
                elif x == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(x))

        return stack[0]