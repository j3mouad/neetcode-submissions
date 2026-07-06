class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        opening_set = {"[","(","{"}
        match = {"[":"]", "(":")", "{":"}"}
        for element in s:
            if element in opening_set:
                Stack.append(element)
            else:
                if len(Stack) == 0: return False
                if match[Stack.pop()] != element:
                    return False
        return len(Stack) == 0

