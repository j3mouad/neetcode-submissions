class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedString = s.replace(" ","")
        strippedString = strippedString.replace("?","")
        strippedString = strippedString.replace(",","")
        strippedString = strippedString.replace("!","")
        strippedString = strippedString.replace("'","")
        strippedString = strippedString.replace(".","")
        strippedString = strippedString.replace(":","")
        strippedString = strippedString.lower()
        print(strippedString)
        return strippedString == strippedString[::-1]