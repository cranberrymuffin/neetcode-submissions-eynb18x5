class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#"+ s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        print(s)
        isPrefix = True
        length = ""
        strs = []
        for c in s:
            if isPrefix:
                if c != '#':
                    length += c
                else:
                    isPrefix = False
                    length = int(length)
                    strs.append("")
            elif length > 0:
                strs[len(strs) - 1] += c
                length -= 1
            if isinstance(length, int) and length <= 0:
                isPrefix = True
                length = ""

        return strs