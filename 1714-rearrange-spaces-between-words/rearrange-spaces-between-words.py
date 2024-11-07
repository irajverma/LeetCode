class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        blanks = text.count(" ")
        string = text.split()
        if len(string) == 1: 
			return string[0] + " " * blanks
        else:
            gaps = len(string) - 1
            q = blanks // gaps
            r = blanks % gaps
            # print(q, r, gaps, string)
            return (" " * q).join(string) + " " * r