import os

current_dir = os.path.dirname(os.path.abspath(__file__))


def get_monkey_details(input_lines):
    monkey_details = []
    for i in range(len(input_lines) // 7):
        starting_items = input_lines[i * 7 + 1].split(",")
        starting_items[0] = starting_items[0].split(" ")[-1]
        starting_items = [int(i.strip()) for i in starting_items]

        operation = input_lines[i * 7 + 2].split(" ")[-2:]

        div_factor = int(input_lines[i * 7 + 3].split(" ")[-1])
        if_true = int(input_lines[i * 7 + 4].split(" ")[-1])
        if_false = int(input_lines[i * 7 + 5].split(" ")[-1])
        monkey_details.append(
            {
                "items": starting_items,
                "operation": operation,
                "div_factor": div_factor,
                "if_true": if_true,
                "if_false": if_false,
                "count": 0,
            }
        )
    return monkey_details


def main(input_lines):
    total_rounds = 20
    monkey_details = get_monkey_details(input_lines)
    for _ in range(total_rounds):
        for monkey_detail in monkey_details:
            operator = monkey_detail["operation"][0]
            for item in monkey_detail["items"]:
                monkey_detail["count"] += 1
                operand2 = monkey_detail["operation"][1]
                if operand2 == "old":
                    operand2 = item
                worry_level = eval(f"{item}{operator}{operand2}")
                worry_level = worry_level // 3
                if worry_level % monkey_detail["div_factor"] == 0:
                    if_true = monkey_detail["if_true"]
                    monkey_details[if_true]["items"].append(worry_level)
                else:
                    if_false = monkey_detail["if_false"]
                    monkey_details[if_false]["items"].append(worry_level)
            monkey_detail["items"] = []

    for monkey_detail in monkey_details:
        print(monkey_detail["count"])


if __name__ == "__main__":
    # input_file_path = os.path.join(current_dir, "input.test")
    input_file_path = os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    main(input_lines)
