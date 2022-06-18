from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                second = stack.pop()
                stack.append(stack.pop() - second)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                second = stack.pop()
                stack.append(int(stack.pop() / second))
            else:
                stack.append(int(token))
        return stack.pop()
