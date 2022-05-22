
def main():
    with open("input", "r") as fh:
        positions = []

        line = fh.readline()
        while line:
            data = line.strip("\n")
            data = tuple([int(i) for i in data])
            positions.append(data)
            # print(data)
            line = fh.readline()

        total_rows = len(positions)
        total_columns = len(positions[0])
        sum_of_lows = 0
        for x, row in enumerate(positions):
            for y, element in enumerate(row):
                up_x, up_y = x-1, y
                if 0 <= up_x < total_rows:
                    val = positions[up_x][up_y]
                    if element >= val:
                        continue
                
                down_x, down_y = x+1, y
                if 0 <= down_x < total_rows:
                    val = positions[down_x][down_y]
                    if element >= val:
                        continue
                
                left_x, left_y = x, y-1
                if 0 <= left_y < total_columns:
                    val = positions[left_x][left_y]
                    if element >= val:
                        continue
                
                right_x, right_y = x, y+1
                if 0 <= right_y < total_columns:
                    val = positions[right_x][right_y]
                    if element >= val:
                        continue
                sum_of_lows += element+1
                print(element)
        print(sum_of_lows)


if __name__ == "__main__":
    main()