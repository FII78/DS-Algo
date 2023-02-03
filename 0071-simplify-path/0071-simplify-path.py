class Solution:
    def simplifyPath(self, path: str) -> str:
#         why stack = for the double dot problem [edge case]
#         when to pop() = when we see double dot
#         when to push() = when we see file name [ A-z and triple dots]
        stack = []
        curr = ""
        
        for c in path + "/":
            if c == "/":
                if curr == "..":
                  
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
                 
        
        return "/" + "/".join(stack)