from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * (n)
        for i in range(n):
            if color[i] != 0:
                continue 
            q = deque()
            color[i] = 1
            q.append(i)

            while q:
                node = q.popleft()
                for nd in graph[node]:
                    if color[nd] == 0:
                        color[nd] = -color[node]
                        q.append(nd)
                    elif color[nd] != -color[node]:
                        return False
        return True