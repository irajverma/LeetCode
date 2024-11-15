class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<2:
            return s
            
        sub = s[0]
        curr = 1

        for i in range(n):
            
            #if the string length is odd
            start , end = i , i
            while ( start >=0 and end < n) and s[start] == s[end]:
                if end-start+1 > curr:
                    sub = s[start:end+1]
                    curr = end-start+1
                start -=1
                end +=1

            start , end = i , i+1
            while ( start >=0 and end < n) and s[start] == s[end]:
                if end-start+1 > curr:
                    sub = s[start:end+1]
                    curr = end-start+1
                start -=1
                end +=1
            
        return sub