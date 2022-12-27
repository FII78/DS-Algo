class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        i = 0
        while i < len(s):
            if s[i].isalnum():
                temp.append(s[i].lower())
            i += 1
        return temp == temp[::-1] 
        
        