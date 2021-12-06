import math


def read_input(filename):
    with open(filename) as f:
        boarding_passes = [line.strip() for line in f]
    return boarding_passes


def get_row_number(boarding_pass):
    rows = [x for x in range(128)]
    lower_bound = min(rows)
    upper_bound = max(rows)
    for letter in boarding_pass[:7]:
        if letter == 'F':
            upper_bound = math.floor(lower_bound + (upper_bound - lower_bound) / 2)
        elif letter == 'B':
            lower_bound = math.ceil(lower_bound + (upper_bound - lower_bound) / 2)
        rows = [x for x in range(lower_bound, upper_bound + 1)]
    return rows[0]


def get_column_number(boarding_pass):
    columns = [x for x in range(8)]
    lower_bound = min(columns)
    upper_bound = max(columns)
    for letter in boarding_pass[7:]:
        if letter == 'L':
            upper_bound = math.floor(lower_bound + (upper_bound - lower_bound) / 2)
        elif letter == 'R':
            lower_bound = math.ceil(lower_bound + (upper_bound - lower_bound) / 2)
        columns = [x for x in range(lower_bound, upper_bound + 1)]
    return columns[0]


def get_seat_id(row, column):
    return row * 8 + column


def part1(boarding_passes):
    seat_ids = [get_seat_id(get_row_number(boarding_pass), get_column_number(boarding_pass)) for boarding_pass in boarding_passes]
    return max(seat_ids)



def main():
    boarding_passes = read_input("input.txt")
    print(f"Part 1: {part1(boarding_passes)}")


if __name__ == "__main__":
    main()