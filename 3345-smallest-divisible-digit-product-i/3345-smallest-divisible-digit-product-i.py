class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num=n
        while True:
            temp=num
            p=1
            while temp>0:
                r=temp%10
                p*=r
                temp//=10
            if p%t==0:
                return num
            num+=1
            
      