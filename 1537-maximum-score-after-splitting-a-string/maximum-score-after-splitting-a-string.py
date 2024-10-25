class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        z = 0
        ans = 0
        o = 0
        for i in range(n):
            if s[i] == '1':
                o += 1
        for i in range(n - 1):
            if s[i] == '0':
                z += 1
            else:
                o -= 1
            ans = max(ans, z + o)
        return ans