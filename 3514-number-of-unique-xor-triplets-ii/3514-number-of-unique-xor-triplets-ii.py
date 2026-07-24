class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniq_nums=set(nums)
        pair_xors=set()
        for num1 in uniq_nums:
            for num2 in uniq_nums:
                pair_xors.add(num1^num2)
        triplet_xors=set()
        for pair_val in pair_xors:
            for num3 in uniq_nums:
                triplet_xors.add(pair_val^num3)
        return len(triplet_xors)

        