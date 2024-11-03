class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        
        count = {}
        longest = 0
        for char in s:
            count[char] = count.get(char, 0) + 1
            if count[char] % 2 == 0:
                longest += 2
        
        if len(s) > longest:
            longest += 1
        
        return longest