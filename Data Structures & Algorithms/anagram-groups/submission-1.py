from collections import defaultdict

class Solution:
    def freq_map(self, word: str) -> tuple:
        mapp = [0] * 26

        for ch in word:
            mapp[ord(ch)-97] += 1

        return tuple(mapp)


    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = defaultdict(list)
        
        for wrd in strs:
            seen[self.freq_map(wrd)].append(wrd)

        return list(seen.values())