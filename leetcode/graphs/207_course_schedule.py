class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.buildAdjList(numCourses, prerequisites)
        state = [0] * numCourses
        
        def hasCycle(v):
            if state[v] == -1:
                return True
            if state[v] == 1:
                return False
            state[v] = -1
            for c in adj[v]:
                if hasCycle(c):
                    return True
            state[v] = 1
            return False

        for c in range(numCourses):
            if hasCycle(c):
                return False
        return True
    
    def buildAdjList(self, n, prereqs):
        res = [[] for _ in range(n)]
        for p, c in prereqs:
            res[c].append(p)
        return res
