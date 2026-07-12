def calculateOperations(number1 : int, number2 : int, operation : str):
    if operation == '+' : return number1 + number2 
    elif operation == '-' : return number1 - number2
    elif operation == '*' : return number1 * number2
    else : return int(number1/number2)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+','-','/','*'}
        counter = 1
        numbers = []
        for token in tokens:
            if token in operations:
                number2 = int(numbers.pop())
                number1 = int(numbers.pop())
                numbers.append(calculateOperations(number1,number2,token))
            else:
                numbers.append(token)           
        return int(numbers[0])