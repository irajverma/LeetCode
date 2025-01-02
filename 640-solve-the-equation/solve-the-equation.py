class Solution:
    def solveEquation(self, equation: str) -> str:
        
        left, right = equation.split('=')
        left_side, right_side = 0, 0

        # solving for left side equation
        i, n = 0, len(left)
        while i < n:
            curr = ""
            if left[i] in ['+', '-']:
                curr += left[i]
                i += 1
            
            while i < n and left[i].isdigit():
                curr += left[i]
                i += 1

            # for x literals, i.e. only x, -x or +x
            if curr in ["", "-", "+"]:
                curr += "1"

            curr = int(curr)

            if i < n and left[i] == 'x':
                left_side += curr
                i += 1
            else:
                right_side -= curr
        


        # solving for right side equation
        i, n = 0, len(right)
        while i < n:
            curr = ""
            if right[i] in ['+', '-']:
                curr += right[i]
                i += 1
            
            while i < n and right[i].isdigit():
                curr += right[i]
                i += 1


            # for x literals:
            if curr in ["", "-", "+"]:
                curr += "1"

            curr = int(curr)

            if i < n and right[i] == 'x':
                left_side -= curr
                i += 1
            else:
                right_side += curr
            
        if left_side == 0 and right_side == 0:
            return "Infinite solutions"
        
        if left_side == 0:
            return "No solution"
        
        
        right_side = right_side // left_side
        return f'x={right_side}'