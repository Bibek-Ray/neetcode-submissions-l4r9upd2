class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_hash = self.create_map(s)
        t_hash = self.create_map(t)
        if s_hash == t_hash:
            return True
        else:
            return False

    def create_map(self, s: str) -> dict:
        dct = {}
        for ch in s:
            if ch not in dct:
                dct[ch] = 1
            else:
                dct[ch] += 1
        
        return dct