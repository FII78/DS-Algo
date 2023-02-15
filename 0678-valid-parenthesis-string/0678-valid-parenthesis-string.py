class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        astrix = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                elif astrix:
                    astrix.pop()
                else:
                    return False
            else:
                astrix.append(i)
        
        while stack and astrix:
            if stack[-1] > astrix[-1]:
                return False
            stack.pop()
            astrix.pop()
        
        return len(stack) == 0
  