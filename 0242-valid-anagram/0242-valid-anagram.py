class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=list(s)
        l2=list(t)
        while len(s)==len(t):
            l1.sort()
            l2.sort()
            if l1==l2:
                return True
            else:
                return False
        else:
            return False

        