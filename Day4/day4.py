def read_input(filename):
    with open(filename, "r") as f:
        numbers = [int(num) for num in f.readline().split(',')]
        f.readline()
        boards = []
        while True:
            boards.append(parse_board(f))
            try:
                next(f)
            except StopIteration:
                break
    return boards, numbers


def parse_board(f):
    board = []
    for i, line in zip(range(5), f):
        board += map(int, line.strip().split())
    return board


def does_board_win(board):
    if any(sum(board[i*5:(i + 1)*5]) == -5 or sum(board[i::5]) == -5 for i in range(5)):
        return True
    else:
        return False


def part1(boards, numbers):

    for number in numbers:
        for board in boards:
            try:
                board[board.index(number)] = -1
            except ValueError:
                continue

            if does_board_win(board):
                return sum([val for val in board if val != -1])*number


def part2(boards, numbers):
    winning_boards = []
    for number in numbers:
        for board_index, board in enumerate(boards):
            if board_index in winning_boards:
                continue
            try:
                board[board.index(number)] = -1
            except ValueError:
                continue

            if does_board_win(board):
                winning_boards.append(board_index)
                if len(winning_boards) == len(boards):
                    return sum([val for val in board if val != -1])*number


def main():
    boards, numbers = read_input("input.txt")
    print("Part 1:", part1(boards, numbers))
    print("Part 2:", part2(boards, numbers))


if __name__ == "__main__":
    main()
