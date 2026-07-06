class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        leftPtr = 0
        rightPtr = n-1
        currentTarget = numbers[leftPtr] + numbers[rightPtr]
        while currentTarget != target:
            if currentTarget > target: 
                rightPtr -= 1 
            else: 
                leftPtr += 1
            currentTarget = numbers[leftPtr] + numbers[rightPtr]
        return [leftPtr+1, rightPtr+1]