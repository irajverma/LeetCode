class Solution:
    def dfs(self, node, isConnected, visited):
        visited[node] = 1

        for i in range(len(isConnected[node])):
            if isConnected[node][i] == 1 and not visited[i]:
                self.dfs(i, isConnected, visited)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [0] * n
        count = 0  

        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(i, isConnected, visited)

        return count