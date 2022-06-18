class Solution:
    def isValid(self, s: str) -> bool:
        brmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            if c in brmap:
                stack.append(c)
            elif not stack or brmap[stack.pop()] != c:
                return False
        return not stack
