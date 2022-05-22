
def main():
    illegal_characters = []
    total_error_sum = 0
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
                
            line = fh.readline()
         
    print(total_error_sum)
    

if __name__ == "__main__":
    main()