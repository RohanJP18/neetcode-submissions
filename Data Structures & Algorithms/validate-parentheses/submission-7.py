class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s: 
            if i == ']' and stack:
                top = stack.pop()
                if top != '[':
                    return False
            elif i == '}' and stack:
                top = stack.pop()
                if top != '{':
                    return False
            elif i == ')' and stack:
                top = stack.pop()
                if top != '(':
                    return False
            else:
                stack.append(i)

        if len(stack) == 0:
            return True
        else:
            return False

        