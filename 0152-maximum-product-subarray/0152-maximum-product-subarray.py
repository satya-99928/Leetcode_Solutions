class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans,cmax,cmin=nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            temp=cmax
            cmax=max(x,x*cmax,x*cmin)
            cmin=min(x,x*temp,x*cmin)
            ans=max(ans,cmax)
        return ans
        