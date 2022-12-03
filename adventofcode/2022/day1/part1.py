
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    input_file_path = os.path.join(current_dir, "input")
    with open(input_file_path, "r") as fh:
        max_calories = 0

        calories_sum = 0
        line = fh.readline()
        while line:
            if line.strip() == "":
                if calories_sum > max_calories:
                    max_calories = calories_sum
                calories_sum = 0
            else:
                calories_sum += int(line.strip())
            line = fh.readline()

        if calories_sum > max_calories:
            max_calories = calories_sum

        print(max_calories)
