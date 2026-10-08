class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total = 0
        for i in range(len(operations)):
            operation = operations[i]
            if operation == "+":
                s = res[-1] + res[-2]
                total += s
                res.append(s)
            elif operation == "D":
                s = res[-1] * 2
                total += s
                res.append(s)
            elif operation == "C":
                total -= res.pop()
            else:
                s = int(operation)
                total += s
                res.append(s)
        return total