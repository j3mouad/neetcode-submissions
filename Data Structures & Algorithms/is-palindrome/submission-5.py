class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        end_pointer = len(s) - 1
        start_pointer = 0
        while end_pointer > start_pointer:
            if not (s[start_pointer].isalnum()):
                start_pointer += 1
                continue
            if not (s[end_pointer].isalnum()):
                end_pointer -=1
                continue
            if s[start_pointer] != s[end_pointer]:
                return False
            else:
                start_pointer+=1
                end_pointer-=1
        return True