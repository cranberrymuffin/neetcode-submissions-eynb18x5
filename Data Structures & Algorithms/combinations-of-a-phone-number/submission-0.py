class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        letters_to_numbers = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        num_digits = len(digits)
        combos = []
        stack = []
        def helper(digits: str):
            if len(digits) == 0 and len(stack) == num_digits and num_digits > 0:
                combos.append("".join(stack))
                return
                
            
            for digit in digits:
                for letter in letters_to_numbers[digit]:
                    stack.append(letter)
                    helper(digits[1:])
                    stack.pop()
                digits = digits[1:]
            
        helper(digits)
        return combos


        