class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        init=set()
        for letter in s:
            if letter not in init:
                init.add(letter)
                if s.count(letter)!=t.count(letter): return False

        return True