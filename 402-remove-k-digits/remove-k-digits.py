class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for char in num:
            while stack and (stack[-1] > char) and k:
                k = k - 1
                stack.pop()
            
            stack.append(char)
        
        while k:
            k = k - 1
            stack.pop()   

        if ''.join(stack).lstrip('0'):
            return ''.join(stack).lstrip('0')
        else:
            return '0'