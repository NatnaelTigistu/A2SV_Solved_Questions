class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        directchild = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        for i,j in edges:
            directchild[i].append(j)
        for i in range(n):
            self.dfs(i,i,directchild,ans)
        return ans
    def dfs(self,x,curr,directchild,ans):
        for ch in directchild[curr]:
            if not ans[ch] or ans[ch][-1] != x:
                ans[ch].append(x)
                self.dfs(x,ch,directchild,ans)