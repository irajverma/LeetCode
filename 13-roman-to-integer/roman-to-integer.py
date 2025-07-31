class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        while len(s) > 0:
            for j in range(len(val)):
                if s.startswith(syb[j]):
                    i += val[j]
                    s = s[len(syb[j]):]
                    break
        return i