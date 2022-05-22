from collections import defaultdict


class BingoBoard:
    def __init__(self, x_dim, y_dim, elements):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.board = []
        self.marked = []
        self.marked_number = []
        if not (elements and isinstance(elements, list)):
            elements = [0] * x_dim * y_dim
        iter_elements = iter(elements)
        for i in range(x_dim):
            self.board.append([0] * y_dim)
            for j in range(y_dim):
                val = next(iter_elements)
                # print(elements)
                self.board[i][j] = int(val)

    def mark_bingo(self, num):
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.board[i][j] == num:
                    self.marked.append([i, j])
        self.marked_number.append(num)

    def is_bingo(self,):
        marked_x_count = defaultdict(int)
        marked_y_count = defaultdict(int)
        for i, j in self.marked:
            marked_x_count[i] += 1
            marked_y_count[j] += 1
        for x, count in marked_x_count.items():
            if count == x_dim:
                print(self, x, count)
                return True
        for y, count in marked_y_count.items():
            if count == y_dim:
                print(self, y, count)
                return True
        return False

    def sum_of_unmarked(self,):
        unmarked_sum = 0
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.board[i][j] not in self.marked_number:
                    unmarked_sum += self.board[i][j]
        return unmarked_sum
    
    def __str__(self,):
        return str(self.board)


x_dim = 5
y_dim = 5
grid_num = x_dim*y_dim


input_s = [72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5]
# input_s = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    
def main():
    with open("input", "r") as fh:
        bingo_boards = []
        elements = []
        line = fh.readline()
        while line or elements:
            values = line.strip("\n").split(" ")
            values = [v for v in values if v.isnumeric()]
            if len(elements) >= grid_num:
                bingo_board = BingoBoard(x_dim, y_dim, elements[0:grid_num])
                bingo_boards.append(bingo_board)
                elements = elements[grid_num:]
            elif values:
                elements.extend(values)
            line = fh.readline()
        print(len(bingo_boards))
        # print(bingo_boards[0])
        # print(bingo_boards[-1])

        for inp in input_s:
            for board in bingo_boards:
                board.mark_bingo(int(inp))
                if board.is_bingo():
                    unmarked_sum = board.sum_of_unmarked()
                    # print(board)
                    print(f"{unmarked_sum} --> {inp} --> {unmarked_sum * inp}") 
                    return

if __name__ == "__main__":
    main()