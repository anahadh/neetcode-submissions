class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        n = len(operations)

        for i in range(n):
            if (operations[i] == "+"):
                sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif (operations[i] == "D"):
                sum += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif (operations[i] == "C"):
                sum -= stack.pop()
            else:
                stack.append(int(operations[i]))
                sum += int(operations[i])
        
        return sum