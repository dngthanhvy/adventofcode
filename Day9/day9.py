from math import prod

def read_input(filename):
  heightmap = []
  with open(filename, "r") as file:
    for line in file.readlines():
      heightmap.append([int(x) for x in list(line.strip())])
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


def find_basin(heightmap, x, y):
  basin_count = 0

  # if the location was already visited or equal to 9
  if heightmap[y][x] == 9 or heightmap[y][x] == "X":
    return basin_count

  # mark it as already visited
  heightmap[y][x] = "X"

  # check neighbours
  if y + 1 < len(heightmap):
    basin_count += find_basin(heightmap, x, y + 1)

  if y - 1 >= 0:
    basin_count += find_basin(heightmap, x, y - 1)

  if x + 1 < len(heightmap[0]):
    basin_count += find_basin(heightmap, x + 1, y)

  if x - 1 >= 0:
    basin_count += find_basin(heightmap, x - 1, y)

  return 1 + basin_count


def part2(heightmap):
  basins = []
  for y in range(len(heightmap)):
      for x in range(len(heightmap[0])):
          basins.append(find_basin(heightmap, x, y))
  top_three = sorted(basins, reverse=True)[:3]
  return prod(top_three)


def main():
  heightmap = read_input("input.txt")
  res1 = part1(heightmap)
  print(f"Part 1: {res1}")
  res2 = part2(heightmap)
  print(f"Part 2: {res2}")


if __name__ == "__main__":
  main()
