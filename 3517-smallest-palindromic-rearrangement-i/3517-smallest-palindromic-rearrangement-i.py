class Solution:
    def smallestPalindrome(self, s: str) -> str:
        left,mid="",""
        for c in sorted(set(s)):
            if s.count(c)%2==1:
                mid=c
            left+=c*(s.count(c)//2)
        return left+mid+left[::-1]




        