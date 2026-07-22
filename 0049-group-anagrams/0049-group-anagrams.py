class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrm_map=defaultdict(list)
        for s in strs:
            sorted_key="".join(sorted(s))
            anagrm_map[sorted_key].append(s)
        return list(anagrm_map.values())