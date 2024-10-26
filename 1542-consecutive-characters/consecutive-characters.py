class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx = 1
        change = []
        prev = ""
        for c in range(len(s)) :

            if s[c] == prev :
                mx += 1
                if c == len(s) - 1 :
                    change.append(mx)
            else :
                change.append(mx)
                mx = 1
            prev = s[c]
        return max(change)