class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]: return - 1
        elif target == nums[0] : return 0 
        elif target == nums[-1] : return len(nums) - 1
        leftPtr = nums[0]
        rightPtr = nums[-1]
        while rightPtr > leftPtr +1:
            middlePoint = (leftPtr + rightPtr)//2
            if nums[middlePoint] == target : return middlePoint
            elif nums[middlePoint] > target : 
                rightPtr = middlePoint
            else: 
                leftPtr = middlePoint
        return -1