class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, word in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != word:
                return False
            if word in word_to_char and word_to_char[word] != c:
                return False
            
            char_to_word[c] = word
            word_to_char[word] = c
        
        return True