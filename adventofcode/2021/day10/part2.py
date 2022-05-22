
def main():
    illegal_characters = []
    total_error_sum = 0
    remaining_chars_sum = []
    with open("input", "r") as fh:
        line = fh.readline()
        while line:
            line = line.strip("\n")
            stack = []
            
            for char in line:
                if char == '}':
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        illegal_characters.append(char)
                        total_error_sum += 1197
                        break
                elif char == ')':
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        illegal_characters.append(char)
                        total_error_sum += 3
                        break
                elif char == ']':
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        illegal_characters.append(char)
                        total_error_sum += 57
                        break
                elif char == '>':
                    if stack[-1] == "<":
                        stack.pop()
                    else:
                        illegal_characters.append(char)
                        total_error_sum += 25137
                        break
                else:
                    stack.append(char)
            else:
                remaining_chars = []
                remaining_chars_total = 0
                # print(stack, stack.reverse())
                for char in reversed(stack):
                    if char == '{':
                        remaining_chars.append("}")
                        remaining_chars_total = remaining_chars_total * 5 + 3
                    elif char == '[':
                        remaining_chars.append("]")
                        remaining_chars_total = remaining_chars_total * 5 + 2
                    elif char == '(':
                        remaining_chars.append(")")
                        remaining_chars_total = remaining_chars_total * 5 + 1
                    elif char == '<':
                        remaining_chars.append(">")
                        remaining_chars_total = remaining_chars_total * 5 + 4
                
                remaining_chars_sum.append(remaining_chars_total)
            line = fh.readline()
    remaining_chars_sum = sorted(remaining_chars_sum)
    length = len(remaining_chars_sum)
    
    print(remaining_chars_sum[length//2])
    

if __name__ == "__main__":
    main()