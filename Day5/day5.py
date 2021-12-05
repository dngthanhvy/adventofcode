def read_input(filename):
    ax = []
    ay = []
    bx = []
    by = []
    with open(filename) as f:
        while line := f.readline():
            x1, y1 = list(map(int, line[:line.index('->')].strip().split(',')))
            x2, y2 = list(map(int, line[line.index('>')+1:].strip().split(',')))
            ax.append(x1)
            bx.append(x2)
            ay.append(y1)
            by.append(y2)
    return ax, ay, bx, by


def tick_coordinates(x, y, map_):
    if map_[x][y] == '.':
        map_[x][y] = 1
    else:
        map_[x][y] += 1
    return map_


def count_intersections(map_):
    count = 0
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] != '.' and map_[i][j] >= 2:
                count += 1
    return count


def part_1(ax, bx, ay, by, map_):
    for x1, y1, x2, y2 in zip(ax, ay, bx, by):
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                map_ = tick_coordinates(x1, y, map_)
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                map_ = tick_coordinates(x, y1, map_)

    return count_intersections(map_)


def part2(ax, bx, ay, by, map_):
    for x1, y1, x2, y2 in zip(ax, ay, bx, by):
        if x1 == x2 or y1 == y2:
            continue
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        m = (y1 - y2) // (x1 - x2)
        for x in range(x1, x2 + 1):
            y = y1 + m * (x - x1)
            map_ = tick_coordinates(x, y, map_)

    return count_intersections(map_)


def main():
    ax, ay, bx, by = read_input("input.txt")
    map_ = [['.' for _ in range(1000)] for _ in range(1000)]
    print("Part 1: " + str(part_1(ax, bx, ay, by, map_)))
    print("Part 2: " + str(part2(ax, bx, ay, by, map_)))


if __name__ == '__main__':
    main()