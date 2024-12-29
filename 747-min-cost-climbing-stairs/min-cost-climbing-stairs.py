class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp =[0]* (len(cost)+1)
        dp[1] = cost[0]
        dp[2] = cost[1]
        for i in range(3, len(cost)+1):
            dp[i] = dp[i-2] + cost[i-1] if dp[i-2] < dp[i-1] else dp[i-1] + cost[i-1]
        if dp[-1] < dp[-2]:
            return dp[-1] 
        else:
            return dp[-2]
        

        