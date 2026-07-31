class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2 : return len(nums)
        setNums = set(nums)
        longestConsecutiveChain = {}
        longestChain = 1
        for num in nums:
            if num in longestConsecutiveChain:
                continue
            else: 
                start = num
                pointer =  start+1 
                offset = 0
                while pointer in setNums:
                    if pointer in longestConsecutiveChain:
                        offset = longestConsecutiveChain[pointer]
                        break
                    else :
                        pointer += 1
                counter = 1 
                for idx in range (pointer-1, start-1, -1):
                    longestConsecutiveChain[idx] = counter + offset 
                    counter += 1 
                if longestConsecutiveChain[start] >= longestChain:
                    longestChain = longestConsecutiveChain[start]
        return longestChain
                