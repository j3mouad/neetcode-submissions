class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2 : return len(nums)
        setNums = set(nums)
        testedNums = set()
        longestChain = 1
        for num in nums:
            if num in testedNums:
                continue
            else:
                testedNums.add(num)
                starter = num
                pointerEnd = num+1 
                pointerStart = num-1
                while pointerEnd in setNums :
                    testedNums.add(pointerEnd)
                    pointerEnd += 1 
                while pointerStart in setNums : 
                    testedNums.add(pointerStart)
                    pointerStart -= 1 
                chain = pointerEnd -pointerStart -1
                if chain > longestChain:
                    longestChain = chain
        return longestChain