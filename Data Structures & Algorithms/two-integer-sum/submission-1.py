class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {target - nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if nums[i] in targetDict:
                j = targetDict[nums[i]]
                if j != i:
                    return  [i,j]