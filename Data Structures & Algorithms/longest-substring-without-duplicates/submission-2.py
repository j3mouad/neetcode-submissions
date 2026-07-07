class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictOfOccurences = {}
        counter = 0
        maxCounter = 0 
        for idx, char in enumerate(s): 
            if char not in dictOfOccurences or (idx- dictOfOccurences[char] > counter):
                counter +=1 
                if counter > maxCounter:
                    maxCounter = counter
                dictOfOccurences[char] = idx
            else :
                lastAppearance = dictOfOccurences[char]
                counter = min(idx - lastAppearance, counter)
                dictOfOccurences[char] = idx
        return maxCounter
