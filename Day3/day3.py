def read_input(filename):
    with open(filename) as f:
        map_ = [line.strip() for line in f.readlines()]
    return map_


def counting_trees(map_, slope):
    slope_x, slope_y = slope
    x = 0
    trees = 0
    for y in range(0, len(map_), slope_y):
        if map_[y][x] == '#':
            trees += 1
        x = (x + slope_x) % len(map_[0])
    return trees


def main():
    map_ = read_input('input.txt')
    print(f"Part 1: {counting_trees(map_, (3,1))}")
    print(f"Part 2: {counting_trees(map_, (1,1)) * counting_trees(map_, (3,1)) * counting_trees(map_, (5,1)) * counting_trees(map_, (7,1)) * counting_trees(map_, (1,2))}")


if __name__ == '__main__':
    main()