class Solution:
    can_finish = {}
    def visit(self, a: int, visited: Set[int], prereqs):
        if a in self.can_finish:
            return self.can_finish[a]
        if a in visited:
            self.can_finish[a] = False
            return False
        if a in prereqs:
            visited.add(a)
            for course in prereqs[a]:
                if not self.visit(course, visited, prereqs):
                    self.can_finish[course] = False
                    return False
            visited.remove(a)
        self.can_finish[a] = True
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.can_finish = {}
        prereqs = {}
        for a, b in prerequisites:
            if a not in prereqs:
                prereqs[a] = []
            prereqs[a].append(b)

        for course in prereqs.keys():
            if not self.visit(course, set(), prereqs):
                return False

        return True