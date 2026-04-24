class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = [(0, [0])]
        target = len(graph) - 1
        result = []

        while queue:
            node, path = queue.pop(0)

            if node == target:
                result.append(path)
                continue

            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

        return result