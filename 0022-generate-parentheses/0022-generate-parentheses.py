class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
#         n - pairs of par. - n amt of open par and n amt of closed par
#         well- formed par = order of  my open and closed par matters   
#         "(" -  first
#         to generate the valid par. Backtracking and stack
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                print("before return")
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                 
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()                 
                

        backtrack(0, 0)
        return res
        
#  [] -> 0 < 3 -> ["("] -> backtrakc(1,0) -> 1 < 3 -> ['(','('] -> bt(2,0) -> 2 < 3 -> ['(','(','(']
# bt(3,0) -> 3 < 3