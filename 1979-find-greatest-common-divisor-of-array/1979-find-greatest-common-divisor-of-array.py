class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        sm=nums[0]
        lg=nums[-1]
        while lg !=0:
            sm,lg=lg,sm%lg
        return sm

        