class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        l_str = ""
        for char in s:
            ascii_val = ord(char)
            if 65 <= ascii_val <= 90:
                l_str += chr(ascii_val + 32)
            else:
                l_str += char
        return l_str