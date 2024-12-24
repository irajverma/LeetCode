class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wall_prefix = []

        M, N = len(wall), -1 # num of rows, # length of wall
        for i, w in enumerate(wall):
            curr_sum = 0
            for b in w:
                curr_sum += b
                wall_prefix.append(curr_sum)
            N = curr_sum

        dic = collections.Counter(wall_prefix)
        least_amount = M

        for edge,occurence in dic.items():
            if edge != N: # check that it's not right edge
                least_amount = min(least_amount, M - occurence)
        
        return least_amount