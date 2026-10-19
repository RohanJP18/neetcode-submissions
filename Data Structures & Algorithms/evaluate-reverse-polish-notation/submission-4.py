class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack
        # array - push (append), pop (pop), peek (stack[-1])
        stack = []
        for ch in tokens:
            if ch not in "+*-/":
                stack.append(int(ch))
            else:
                top2 = int(stack[-1])
                stack.pop()
                top1 = int(stack[-1])
                stack.pop()
                if ch == '+':
                    result = top1 + top2
                elif ch == '-':
                    result = top1 - top2
                elif ch == '*':
                    result = top1 * top2
                elif ch == '/':
                    result = int(top1 / top2)
                stack.append(result)
        return stack[-1]



        
