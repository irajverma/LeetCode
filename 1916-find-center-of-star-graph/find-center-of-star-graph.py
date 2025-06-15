from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = defaultdict(int)
        for edge in edges:
            nodea = edge[0]
            nodeb = edge[1]
            nodes[nodea] += 1
            nodes[nodeb] += 1

            if nodes[nodea] > 1:
                return nodea
            if nodes[nodeb] > 1:
                return nodeb
        