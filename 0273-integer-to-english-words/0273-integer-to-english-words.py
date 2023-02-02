class Solution:
    def numberToWords(self, num: int) -> str:
        """        
        maximum = 2 147 483 647
        "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
        
        Less than thousand:
            1. under twenty
            2. tens - case 1
            3. digit - hundered - case 2
            
        Greater than thousand - process in chunks of 3
        
        """
        
        under_twenty = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen",
        ]
        
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"
        ]
        
        groups = ["Thousand", "Million", "Billion"]
        
        def english_word(num):
            if num == 0:
                return []
            
            if num < 20:
                return [under_twenty[num]] 
            
            if num < 100:
                return [tens[num // 10]] + english_word(num % 10)
            
            if num < 1000:
                quotient, remainder = num // 100, num % 100
                return [under_twenty[quotient], "Hundred"] + english_word(remainder)
            
            for power, group in enumerate(groups, 1):
                if num < 1000 ** (power + 1):
                    quotient, remainder = num // 1000 ** power, num % 1000 ** power
                    return english_word(quotient) + [group] + english_word(remainder)
            
        return ' '.join(english_word(num)) or "Zero"     
                    
            
        
        
        
