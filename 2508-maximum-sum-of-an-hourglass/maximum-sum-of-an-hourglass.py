class Solution:
    def maxSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        if n < 3 or m < 3:
            return -1
    
        res = float('-inf')
    
        for i in range(n - 2):
            for j in range(m - 2):
                
                sum = mat[i][j] + mat[i][j+1] + mat[i][j+2] +mat[i+1][j+1] +mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
            
                res = max(res, sum)
    
        return res
