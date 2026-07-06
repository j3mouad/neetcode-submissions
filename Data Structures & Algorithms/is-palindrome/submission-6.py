class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [elt for elt in s if elt.isalnum()]
        return s == s[::-1]