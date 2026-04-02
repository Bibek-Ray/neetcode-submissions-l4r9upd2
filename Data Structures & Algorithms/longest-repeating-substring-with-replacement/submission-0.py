class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                # count frequencies in s[i:j+1]
                freq = {}
                for t in range(i, j + 1):
                    c = s[t]
                    if c not in freq:
                        freq[c] = 0
                    freq[c] += 1

                # find max frequency
                mx = 0
                for c in freq:
                    if freq[c] > mx:
                        mx = freq[c]

                # replacements needed
                length = j - i + 1
                need = length - mx

                if need <= k and length > ans:
                    ans = length

        return ans