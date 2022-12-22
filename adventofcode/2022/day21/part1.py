
import argparse
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

class Monkey:
    def __init__(self, name, kind, *args):
        self.name = name
        self.kind = kind
        self.res = None
        if self.kind == "number":
            self.res = args[0]
        elif self.kind == "operation":
            self.dep = [args[0], args[2]]
            self.operation = args[1]

    def __repr__(self,):
        return f"{self.name} - {self.kind}"

    def operate(self,):
        if not self.kind == "operation":
            return
        
        m1, m2 = self.dep[0], self.dep[1]
        if m1.res != None and m2.res != None:
            self.res = eval(f"{m1.res}{self.operation}{m2.res}")

def main(input_lines):
    monkey_map = {}
    root_monkey = None

    # Create monkeys
    for line in input_lines:
        p1, p2 = line.split(":")
        monkey_name = p1.strip()
        p2 = [p.strip() for p in p2.strip().split(" ")]
        if len(p2) > 1:
            monkey = Monkey(monkey_name, "operation", *p2)
            monkey_map[monkey_name] = monkey
        else:
            monkey = Monkey(monkey_name, "number", p2[0])
            monkey_map[monkey_name] = monkey
        if monkey_name == "root":
            root_monkey = monkey

    # Link dep monkeys
    for n, m in monkey_map.items():
        if m.kind == "operation":
            m1 = m.dep[0]
            m2 = m.dep[1]
            m.dep = [monkey_map[m1], monkey_map[m2]]

    while not root_monkey.res:
        for n, m in monkey_map.items():
            m.operate()

    print(root_monkey.res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    test = False
    if args.test:
        test = True

    input_file_path = os.path.join(current_dir, "input.test") if test else os.path.join(current_dir, "input")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")
    main(input_lines)

