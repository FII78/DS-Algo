class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        val = int("".join(map(str, num))) + k
        return map(int, list(str(val)))
        