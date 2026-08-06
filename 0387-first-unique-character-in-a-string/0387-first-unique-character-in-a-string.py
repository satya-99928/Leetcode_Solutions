class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1
        for ind,c in enumerate(s):
            if freq[c]==1:
                return ind
        return -1