from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurencesDict = defaultdict(int)
        for num in nums:
            occurencesDict[num]+= 1 
        occurences = [[] for i in range(len(nums))]
        for key, value in occurencesDict.items(): 
            if len(occurences[value-1]):
                occurences[value-1].append(key)
            else:
                occurences[value-1] = [key]
        counter = 0 
        output = []
        for idx in range(len(nums)-1,-1,-1):
            if len(occurences[idx]):
                output.extend(occurences[idx])
                counter+= len(occurences[idx])
                if counter == k:
                    return output 
                
