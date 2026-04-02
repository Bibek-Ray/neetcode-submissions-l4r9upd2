from collections import defaultdict

class Solution:
    def freq_map(self, word: str) -> tuple:
        mapp = {}

        for ch in word:

            if ch in mapp:
                mapp[ch] += 1
            else:
                mapp[ch] = 1

        return tuple(mapp.items())


    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = defaultdict(list)
        
        for wrd in strs:
            
            if frozenset(self.freq_map(wrd)) in seen:
                seen[frozenset(self.freq_map(wrd))].append(wrd)
            else:
                seen[frozenset(self.freq_map(wrd))].append(wrd)

        return list(seen.values())