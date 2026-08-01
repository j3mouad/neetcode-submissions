class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2 : return len(nums)
        setNums = set(nums)
        longestChain = 1
        for num in nums:
            if num-1 in setNums :
                continue
            else:
                pointer =  num+1 
                while pointer in setNums :
                    pointer += 1 
                chain = pointer - num 
                if chain > longestChain:
                    longestChain = chain
        return longestChain