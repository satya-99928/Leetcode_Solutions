class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        fin=[]
        for i in range(n):
            fin.append(nums[i])
            fin.append(nums[i+n])
        return fin




