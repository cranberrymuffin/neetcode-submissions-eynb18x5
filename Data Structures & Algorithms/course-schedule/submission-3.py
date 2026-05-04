class Solution:
    def visit(self, a: int, visited: Set[int], prereqs):
        if a in visited:
            return False
        if a in prereqs:
            visited.add(a)
            for course in prereqs[a]:
                if not self.visit(course, visited, prereqs):
                    return False
            visited.remove(a)
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for a, b in prerequisites:
            if a not in prereqs:
                prereqs[a] = []
            prereqs[a].append(b)

        for course in prereqs.keys():
            if not self.visit(course, set(), prereqs):
                return False

        return True