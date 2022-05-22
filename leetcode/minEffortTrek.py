import math

def get_valid_siblings(x, y, len_x, len_y):
    valid_siblings = []
    if 0 <= y-1 < len_y:
        valid_siblings.append([x, y-1])
    if 0 <= y+1 < len_y:
        valid_siblings.append([x, y+1])
    if 0 <= x-1 < len_x:
        valid_siblings.append([x-1, y])
    if 0 <= x+1 < len_x:
        valid_siblings.append([x+1, y])
    return valid_siblings


def minimumEffortPath(heights):
    len_x = len(heights)
    len_y = len(heights[0])
    if len_x * len_y == 1:
        print(1)
    end_node = [len(heights)-1, len(heights[0])-1]

    final_paths = []

    all_possible_paths = [[[0, 0], ], ]

    while all_possible_paths:
        new_all_possible_paths = []
        for path in all_possible_paths:
            last_node = path[-1]

            for sibling_node in get_valid_siblings(*last_node, len_x, len_y):
                if sibling_node in path:
                    continue
                new_path = path+ [sibling_node]
                if sibling_node == end_node:
                    final_paths.append(new_path)
                else:
                    new_all_possible_paths.append(new_path)
        all_possible_paths = new_all_possible_paths

    minEffort = math.inf
    for path in final_paths:
        maxEffortPath = 0
        for i, node in enumerate(path):
            if i+1 == len(path):
                break
            next_node = path[i+1]
            # print(heights)
            # print(node)
            # print(next_node)
            hop_distance = heights[node[0]][node[1]] - heights[next_node[0]][next_node[1]]
            hop_distance = abs(hop_distance)
            if hop_distance > maxEffortPath:
                maxEffortPath = hop_distance
        if maxEffortPath < minEffort:
            minEffort = maxEffortPath
    print(minEffort)

if __name__ == "__main__":
    heights = [
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5],
    ]
    heights = [[1,2,3],[3,8,4],[5,3,5]]
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    heights = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
    minimumEffortPath(heights)
