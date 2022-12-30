class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        min_str, max_str = min(strs), max(strs)
        for idx, ch in enumerate(min_str):
            if ch != max_str[idx]:
                return min_str[:idx]
        return min_str