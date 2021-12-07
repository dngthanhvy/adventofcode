import statistics as st


def read_input(filename):
  with open(filename, "r") as f:
    crabs = [int(number) for number in f.readline().split(',')]
  return crabs


def align_position(crabs):
  return st.median(crabs)


def get_fuel(crabs, position):
  return sum([abs(crab - position) for crab in crabs])


def triang(x):
  return x*(x+1)//2


def part_1(crabs):
  aligned_position = align_position(crabs)
  return get_fuel(crabs, aligned_position)


def part_2(crabs):
  result = []
  for i in range(min(crabs), max(crabs)):
    result.append(sum([triang(abs(crab - i)) for crab in crabs]))
  return min(result)


def main():
  crabs = read_input("input.txt")
  print(f"Part 1: {part_1(crabs)}")
  print(f"Part 2: {part_2(crabs)}")


if __name__ == "__main__":
  main()