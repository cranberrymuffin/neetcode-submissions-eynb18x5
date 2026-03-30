class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = "s" + str(len(string)) + "e"
            result += length + string
        return result

    def digestNextWord(self, s: str) -> (str, str):
        if s[0] != "s":
            raise Exception("corrupted decoding start character")
        s = s[1:]
        length = ""
        while s[0] != "e":
            length += s[0]
            s = s[1:]
        s= s[1:]
        length = int(length)
        string = ""
        while length > 0:
            string += s[0]
            s= s[1:]
            length-=1
        print(string)
        return string, s

    def decode(self, s: str) -> List[str]:
        strs = []
        while len(s) > 0:
            nextWord, s = self.digestNextWord(s)
            strs.append(nextWord)
        return strs

