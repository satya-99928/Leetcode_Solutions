class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        nz=[ch for ch in s if ch!="0"]
        if not nz:
            x=0
        else:
            x=int("".join(nz))
        dig_sum=sum(int(ch) for ch in nz)
        return x*dig_sum
