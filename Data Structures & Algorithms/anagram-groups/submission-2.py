from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictOfDicts = {}
        for string in strs:
            dictOfOccurences = defaultdict(int)
            for idx in range(len(string)):
                dictOfOccurences[string[idx]] +=1 
            dictOfDicts[string]= dictOfOccurences
        output = [[strs[0]]]
        for idx, string in enumerate(strs):
            if idx == 0 : continue
            dictOfOccurences = dictOfDicts[string]
            isElementfound = False
            for element in output:
                if dictOfOccurences == dictOfDicts[element[0]]:
                    element.append(string)
                    isElementfound = True
                    break
            if not isElementfound:
                output.append([string])
        return output
