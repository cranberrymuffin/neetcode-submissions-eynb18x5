class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += "start" + str(len(s)) + "end" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while len(s)>0:
            length = s[s.index("start") + 5:s.index("end")]
            s = s[len("start") + len(length) + len("end"):]
            length =int(length)
            string = s[0:length]
            result.append(string)
            s = s[length:]
        return result
