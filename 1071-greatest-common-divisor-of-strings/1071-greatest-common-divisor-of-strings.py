class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not ((str1 + str2) == (str2+str1)):
            return ""
        
        def gcd(a,b):
            while b != 0:
                return gcd(b, a%b)
            return a
        
        gcd = gcd(len(str1), len(str2))
        return str1[0:gcd]
            
     