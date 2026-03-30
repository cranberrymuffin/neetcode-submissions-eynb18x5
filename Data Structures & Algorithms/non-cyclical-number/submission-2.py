class Solution:
    def replace(self, n: int) -> int:
        result = 0
        for c in str(n):
            result += int(c) * int(c)
        return result

    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while True:
            if n == 1:
                return True;
            n = self.replace(n)
            if n in seen:
                return False;
            seen.add(n)




        