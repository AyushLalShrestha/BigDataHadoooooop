

import os

current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    with open(input_file_path, "r") as fh:
        top_three = [0, 0, 0]

        calories_sum = 0
        line = fh.readline()
        while line:
            if line.strip() == "":
                for top in top_three:
                    if calories_sum > top:
                        top_three.remove(top)
                        top_three.append(calories_sum)
                        break
                calories_sum = 0
            else:
                calories_sum += int(line.strip())
            line = fh.readline()

        # :P
        for top in top_three:
            if calories_sum > top:
                top_three.remove(top)
                top_three.append(calories_sum)
                break

        print(sum(top_three))
