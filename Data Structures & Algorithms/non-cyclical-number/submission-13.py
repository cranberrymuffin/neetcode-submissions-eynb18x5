class Solution:
    def replace(self, n:int) -> int:
        result = 0
        for c in str(n):
            result += int(c) * int(c)
        return result

    def isHappy(self, n: int) -> bool:
        return self.isHappyHelper(n, set())

    def isHappyHelper(self, n: int, seen: set) -> bool:
        if n == 1:
            return True;
        if n in seen:
            return False;
        seen.add(n)
        return self.isHappyHelper(self.replace(n), seen)