import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        ipv4 = re.compile(r"(^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$)")
        if ipv4.fullmatch(queryIP): return "IPv4" 
        
        ipv6 = re.compile(r"((([0-9a-fA-F]){1,4})\:){7}([0-9a-fA-F]){1,4}")
        if ipv6.fullmatch(queryIP) : return "IPv6"
        
        return "Neither"
 
		
        
        