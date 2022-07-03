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


class Solution:
    """
    реализация для случая, когда не гарантируется верность входного выражения и 
    tokens может содредать не только числа и занки операций
    """
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operands:
                if token == "+" and len(stack) >= 2:
                    stack.append(stack.pop() + stack.pop())
                elif token == "-" and len(stack) >= 2:
                    second = stack.pop()
                    stack.append(stack.pop() - second)
                elif token == "*" and len(stack) >= 2:
                    stack.append(stack.pop() * stack.pop())
                elif token == "/" and len(stack) >= 2:
                    second = stack.pop()
                    stack.append(int(stack.pop() / second))
                else:
                    print("Error in input data! Missing one or two operation arguments!")
                    return
            else:
                try:
                    stack.append(int(token))
                except ValueError:
                    print("Error in input data! Impossible to parse number!")
                    return
        if len(stack) == 1:
            return stack.pop()
        print("Error in input data! Too many arguments passed!")


func = Solution().evalRPN
print(func(['1']))
assert func(['1', '2', '+']) == 3
assert func(['1', '2', '3']) == None
assert func(['1']) == 1
assert func(['+']) == None
assert func(['1', '2', '+', '-7', '-']) == 10
