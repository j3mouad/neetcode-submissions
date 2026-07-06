class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        leftPtr = 0
        rightPtr = n-1
        while numbers[leftPtr] + numbers[rightPtr] != target:
            if numbers[leftPtr] + numbers[rightPtr] > target: 
                rightPtr -= 1 
            else: 
                leftPtr += 1
        return [leftPtr+1, rightPtr+1]