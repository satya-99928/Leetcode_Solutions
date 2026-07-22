class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones=s.count('1')
        t="1"+s+"1"
        runs=[]
        chars=[]
        i=0
        while i<len(t):
            j=i
            while j<len(t) and t[j]==t[i]:
                j+=1
            chars.append(t[i])
            runs.append(j-i)
            i=j
        gain=0
        for i in range(1,len(runs)-1):
            if chars[i]=='1' and chars[i-1]=='0' and chars[i+1]=='0':
                gain=max(gain,runs[i-1]+runs[i+1])
        return ones+gain


        