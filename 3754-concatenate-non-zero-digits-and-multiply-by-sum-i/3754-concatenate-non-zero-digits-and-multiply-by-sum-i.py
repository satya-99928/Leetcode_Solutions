class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        r=""
        su=0
        for i in s:
            if i!="0":
                r+=i
            su+=int(i)
        if r=="":
            return 0
        return int(r)*su
