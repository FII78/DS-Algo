class Solution:
    def convert(self, s: str, numRows: int) -> str:
        initi = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        result = [''] * numRows
        for i, char in enumerate(s):
            result[initi[i % len(initi)]] += char
        return ''.join(result)
        