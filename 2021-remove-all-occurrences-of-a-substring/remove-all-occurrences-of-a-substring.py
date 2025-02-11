class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        word = list(s)
        i = 0
        targetLength = len(part)
        
        while i < len(word):
            if self.getMatch(word, part, i):
                del word[i:i+targetLength]
                i = max(0, i - targetLength)
            else:
                i += 1
        
        return "".join(word)
    
    def getMatch(self, word, part, i):
        if len(word) < len(part): 
            return False
        for j in range(len(part)):
            if i + j >= len(word) or word[i + j] != part[j]: 
                return False
        return True