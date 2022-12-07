
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

class iNode:
    def __init__(self, name, _type, parent_node=None, size=0, childs=None):
        self.name = name
        self.type = _type
        self.size = size
        self.childs = []
        if childs:
            self.childs = childs
        if parent_node:
            self.parent_node = parent_node

    def add_child(self, child):
        for existing_child in self.childs:
            if existing_child.name == child.name:
                return
        self.childs.append(child)

    def __str__(self,):
        return self.type
    
    def get_size(self):
        if self.type == "file":
            return self.size
        else:
            _size = 0
            for child_node in self.childs:
                _size += child_node.get_size()
            return _size


def main():
    input_file_path = os.path.join(current_dir, "input.test")
    _input = open(input_file_path, "r").read()
    input_lines = _input.split("\n")

    # Parse input stack
    root_node = current_node = iNode("/", "dir")
    for line in input_lines[1:]:
        parts = line.strip().split(" ")
        if parts[0] == "$":
            # command
            if parts[1] == "ls":
                # ls command
                pass
            elif parts[1] == "cd":
                # cd command
                cd_into = parts[2]
                cd_into = cd_into.strip()
                if cd_into == "..":
                    # go 1 step back
                    current_node = current_node.parent_node
                else:
                    # cd into the directory
                    for child_node in current_node.childs:
                        if child_node.name == cd_into:
                            current_node = child_node
        else:
            # stats
            if parts[0] == "dir":
                # directory
                dir_name = parts[1]
                dir_node = iNode(dir_name, "dir", parent_node=current_node)
                current_node.add_child(dir_node)
            else:
                # file
                size = int(parts[0])
                file_name = parts[1]
                file_node = iNode(file_name, "file", size=size, parent_node=current_node)
                current_node.add_child(file_node)

    # iterate the directory structure and calculate size of each directory
    dir_size_map = {}
    _next_dirs = [root_node,]
    while _next_dirs:
        _next_dir = _next_dirs.pop(0)
        dir_size_map[_next_dir] = _next_dir.get_size()
        for child_node in _next_dir.childs:
            if child_node.type == "dir":
                _next_dirs.append(child_node)
    
    total = 0
    for i, k in dir_size_map.items():
        if k <= 100000:
            total += k
    print(total)


if __name__ == "__main__":
    main()
