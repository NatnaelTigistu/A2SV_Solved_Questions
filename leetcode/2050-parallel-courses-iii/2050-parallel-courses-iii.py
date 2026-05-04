class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree = [0] * n
        completionTime = [0] * n
        for u, v in relations:
            adj[u-1].append(v-1)
            indegree[v-1] += 1

        q = deque([])
        for u in range(n):
            if indegree[u] == 0: # if no prerequisite add it to queue
                q.append(u)
                completionTime[u] = time[u]

        while len(q) != 0:
            u = q.popleft()
            for v in adj[u]:
                completionTime[v] = max(completionTime[u] + time[v], completionTime[v]) 
                indegree[v] -= 1
                if indegree[v] == 0: # when all prerequisite are complete add the next course
                    q.append(v)
        return max(completionTime)