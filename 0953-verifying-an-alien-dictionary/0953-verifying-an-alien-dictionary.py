class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {ch: i for i, ch in enumerate(order)}
        
        prev = list(hashmap[ch] for ch in words[0])
        for i in range(1, len(words)):
            cur = list(hashmap[ch] for ch in words[i])
            if cur < prev:
                return False
            prev = cur
        return True
     