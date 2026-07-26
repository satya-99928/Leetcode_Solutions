class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[]
        res.extend(nums)
        for i in nums: 
            res.append(i)
        return res
        
        