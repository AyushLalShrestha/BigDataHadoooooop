
OPERATOR_PRECEDENCE = {
    "e": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 3,
}


def execute(operand1, operand2, operator):
    if operator == "+":
        return int(operand1) + int(operand2)
    elif operator == "-":
        return int(operand1) - int(operand2)
    elif operator == "*":
        return int(operand1) * int(operand2)
    elif operator == "/":
        return int(operand1) // int(operand2)
    else:
        return operand2


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand1 = None
        operand2 = None
        operator = None

        for l in s:
            if l == " ":
                continue
            elif l in OPERATOR_PRECEDENCE:
                if not operator:
                    if not operand1:
                        operand1 = operand2
                        operand2 = None
                elif OPERATOR_PRECEDENCE[l] > OPERATOR_PRECEDENCE[operator]:
                    stack.append([operand1, operator])
                    operand1 = operand2
                elif operand1 is not None and operand2 is not None:
                    operand2 = execute(operand1, operand2, operator)
                    if stack:
                        last = stack.pop()
                        operand1 = last[0]
                        operator = last[1]
                        operand1 = execute(operand1, operand2, operator)
                    else:
                        operand1 = operand2
                operand2 = None
                operator = l
            elif l.isdigit():
                if operand2 is None:
                    operand2 = int(l)
                elif operand2 is not None:
                    operand2 = operand2 * 10 + int(l)
        # print(f"{operand1}, {operator}, {operand2}, {stack}")
        if operand2 is not None and operand1 is not None:
            operand1 = execute(operand1, operand2, operator)
        while stack:
            operand2 = operand1
            last = stack.pop()
            operand1 = last[0]
            operator = last[1]
            operand1 = execute(operand1, operand2, operator)
            operand2 = None
            operator = None
        return operand1
