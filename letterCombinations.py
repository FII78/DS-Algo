class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def bt(idx,curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for i in dic[digits[idx]]:
                bt(idx + 1,curr + i)
        if digits:
            bt(0,"")
        return res