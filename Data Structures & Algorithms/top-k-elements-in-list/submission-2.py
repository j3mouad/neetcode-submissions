from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurencesDict = defaultdict(int)
        for num in nums:
            occurencesDict[num]+= 1 
        occurences = [[None] for i in range(len(nums))]
        for key, value in occurencesDict.items(): 
            if occurences[value-1][0] is None:
                occurences[value-1] = [key]
            else:
                occurences[value-1].append(key)
        counter = 0 
        output = []
        for idx in range(len(nums)-1,-1,-1):
            if occurences[idx][0] is not None:
                output.extend(occurences[idx])
                counter+= len(occurences[idx])
                if counter == k:
                    return output 
                
