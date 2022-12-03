OPERATORS = ["+", "-"]


def execute(operand1, operand2, operator):
    if operator == "+":
        return int(operand1) + int(operand2)
    elif operator == "-":
        return int(operand1) - int(operand2)
    else:
        return operand2


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        weight = 0
        operator = ""
        operand1 = None

        for l in s:
            if operand1 is not None:
                if l.isdigit():
                    operand1 = operand1 * 10 + int(l)
                    continue
                else:
                    if operator:
                        weight = execute(weight, operand1, operator)
                    else:
                        weight = operand1
                    operand1 = None

            if l == " ":
                continue
            elif l in OPERATORS:
                operator = l
            elif l == "(":
                if not operator:
                    stack.append([0, "+"])
                else:
                    stack.append([weight, operator])
                    weight = 0
                    operator = ""
            elif l == ")":
                last = stack.pop()
                last_weight = last[0]
                last_operator = last[1]
                print(f"{last_weight}, {last_operator}, {weight}")
                weight = execute(last_weight, weight, last_operator)
                operator = ""
            elif l.isdigit():
                if not operand1:
                    operand1 = int(l)

        if operand1:
            weight = execute(weight, operand1, operator)
        return weight
