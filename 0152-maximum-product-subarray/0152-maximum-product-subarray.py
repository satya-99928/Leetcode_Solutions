class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=max(nums)
        curr_min,curr_max=1,1
        for n in nums:
            if n==0:
                curr_min,curr_max=1,1
                continue
            tmp=curr_max*n
            curr_max=max(tmp,n*curr_min,n)
            curr_min=min(tmp,n*curr_min,n)
            res=max(res,curr_max)
        return res

        