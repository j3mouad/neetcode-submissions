class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = set()
        for i in range(len(nums) - 2):
            target = - nums[i]
            leftPtr = i+1
            rightPtr = n-1
            currentTarget = nums[leftPtr] + nums[rightPtr]
            while leftPtr < rightPtr:
                if currentTarget == target:
                    triplets.add((-target, nums[leftPtr], nums[rightPtr]))
                    leftPtr += 1
                    if leftPtr == rightPtr: 
                        break
                    currentTarget = nums[leftPtr] + nums[rightPtr]
                if currentTarget > target: 
                    rightPtr -= 1 
                else: 
                    leftPtr += 1
                currentTarget = nums[leftPtr] + nums[rightPtr]
        return list(triplets)