class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, elt in enumerate(nums):
            if target-elt in seen:
                target_idx = seen[target-elt]
                return [target_idx,idx]
            else:
                seen[elt] = idx