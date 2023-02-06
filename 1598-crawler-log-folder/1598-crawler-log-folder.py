class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = ["Main"]
            
        for log in logs:
            if log == "../" and stack:
                if stack[-1] != "Main":
                    stack.pop()
            elif log == "./":
                continue
            else: 
                stack.append(log)
        return len(stack) - 1
        