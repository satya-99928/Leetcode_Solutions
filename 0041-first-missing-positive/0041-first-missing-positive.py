class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present=set(nums)
        miss=1
        while miss in present:
            miss+=1
        return miss
        