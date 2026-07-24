class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr=[]
        max_l=0
        for i in s:
            if  i in curr:
                dup=curr.index(i)
                curr=curr[dup+1:]
            curr.append(i)
            max_l=max(max_l,len(curr))
        return max_l
            



        