class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(digits)
        if len(digits) == 0:
            return [1]
        if digits[len(digits) - 1] == 9:
            if len(digits) == 1:
                return [1, 0]
            else:
                return self.plusOne(digits[0:len(digits) - 1]) + [0]
        else:
            return digits[:len(digits) - 1] + [digits[len(digits) - 1] + 1]

        