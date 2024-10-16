class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for char in s:
			if char != 'i':
				result = result + char
			else:
				result = result[::-1]
        return result