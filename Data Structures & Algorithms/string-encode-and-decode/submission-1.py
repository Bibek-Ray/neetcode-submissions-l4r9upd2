class Solution:

    def encode(self, strs: list[str]) -> str:
        codec = ""
        for val in strs:
            codec += str(len(val)) + '#' + val

        return codec

    def decode(self, s: str) -> list[str]:
        codec = []
        k = ""
        i = 0
        while i < len(s):
            if s[i] != '#' and s[i].isdigit():
                k += s[i]
                i += 1
            else:
                i += 1
                codec.append(s[i: i + int(k)])
                i += int(k)
                k = ""

        return codec