import os

def read_from_file(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    rows= []
    with open(file_path) as fh:
        rows = fh.read().split('\n')
        rows = [r.strip() for r in rows if r]
    return rows

def main():
    map_data = read_from_file("input.txt")
    max_seat_id = 0
    for row in map_data:
        row_part = row[0:7]
        column_part = row[7:10]

        row_range = list(range(0, 128))
        for rval in row_part:
            middle = int(len(row_range)/2)
            if rval == 'F':
                row_range = row_range[0:middle]
            elif rval == 'B':
                row_range = row_range[middle:]
        row_no = row_range[0]

        column_range = list(range(0, 8))
        for cval in column_part:
            middle = int(len(column_range)/2)
            if cval == 'L':
                column_range = column_range[:middle]
            elif cval == 'R':
                column_range = column_range[middle: ]
        column_no = column_range[0]

        seat_id = row_no * 8 + column_no
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print(max_seat_id)
if __name__ == "__main__":
    main()

