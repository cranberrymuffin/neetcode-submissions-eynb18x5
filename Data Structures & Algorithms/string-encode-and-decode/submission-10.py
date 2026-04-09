class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += "s" + str(len(s)) + "e" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0:
            length = ""
            s = s[1:]
            while s[0] != "e":
                length += s[0]
                s = s[1:]

            length = int(length)
            s = s[1:]
            string = ""
            while length > 0:
                string += s[0]
                s = s[1:]
                length -= 1
            result.append(string)
        return result
