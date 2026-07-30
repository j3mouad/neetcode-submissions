class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for chars in strs:
            lenght = len(chars)
            code += str(lenght) + "@" + chars
        return code

    def decode(self, s: str) -> List[str]:
        pointer = 1
        start = 0
        code = []
        while pointer < len(s):
            if s[pointer] == "@":
                charsLen = int(s[start:pointer])
                code.append(s[pointer+1:pointer+1+charsLen])
                pointer += 2+charsLen
                start = pointer -1 
            else:
                pointer+= 1
        return code