class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        last = {}
        for i in range(len(s)):
            char = s[i]  
            last[char] = i  


        for i, char in enumerate(s):
            if char in stack:
                continue
                
            while stack and char < stack[-1] and i < last[stack[-1]]:
                stack.pop()
                
            stack.append(char)
            
        return ''.join(stack)