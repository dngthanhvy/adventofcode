def read_input(filename):
    with open(filename, "r") as file:
        heightmap = []
        for line in file:
            heightmap.append([int(x) for x in line.strip()])
    return heightmap


def part1(heightmap):
    risk_level = 0
    low_heights = []
    for row in range(len(heightmap)):
        for column in range(len(heightmap[row])):
            adjacent_heights = []

            if column - 1 >= 0:
                adjacent_heights.append(heightmap[row][column - 1])

            # DOWN
            if column + 1 < len(heightmap):
                adjacent_heights.append(heightmap[row][column + 1])

            # LEFT
            if row - 1 >= 0:
                adjacent_heights.append(heightmap[row - 1][column])

            # RIGHT
            if row + 1 < len(heightmap):
                adjacent_heights.append(heightmap[row + 1][column])

            if all(ap > heightmap[row][column] for ap in adjacent_heights):
                low_heights.append(heightmap[row][column])
                risk_level += 1 + heightmap[row][column]

    return risk_level


def main():
    heightmap = read_input("input.txt")
    print(f"Part 1: {part1(heightmap)}")


if __name__ == "__main__":
    main()