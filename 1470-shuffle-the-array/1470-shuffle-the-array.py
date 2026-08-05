class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [val for pairs in zip(nums[:n],nums[n:])for val in pairs]

        




