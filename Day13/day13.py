def read_input(filename):
  marks = []
  folds = []
  with open(filename, "r") as file:
    for file in file.readlines():
      if file[0] == "f":
        direction, line = file.strip().split(" ")[-1].split("=")
        folds.append((direction, int(line)))
      elif file != "\n":
        marks.append(tuple(map(int, file.strip().split(","))))
  return marks, folds


def show_grid(grid):
  for line in grid:
    print(line)


def create_grid(marks):
  w = max(marks, key = lambda x:x[0])[0]
  h = max(marks, key = lambda x:x[1])[1]
  if w%2 != 0:
    w += 1
  if h%2 != 0:
    h += 1
  grid = [[0 for _ in range(w+1)] for _ in range(h+1)]
  for row,col in marks:
    grid[col][row] = 1
  return grid


def fold_grid(direction, line, grid):
  list_1 = []
  list_2 = []
  if direction == "y":
    list_1 = [x for i,x in enumerate(grid) if i < line]
    list_2 = list(reversed([x for i,x in enumerate(grid) if i > line]))
  if direction == "x":
    for row in grid:
      list_1.append(row[:line])
      list_2.append(list(reversed(row[line+1:])))
  return list_1, list_2


def merge_grids(grid_1, grid_2):
  result = []
  for j in range(len(grid_1)):
    temp = []
    for i in range(len(grid_1[0])):
      temp.append(grid_1[j][i] | grid_2[j][i])
    result.append(temp)
  return result


def stringify(grid):
  stringified = []
  for i in range(len(grid)):
    temp = ""
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        temp += "#"
      else:
        temp += "."
    stringified.append(temp)
  return stringified


def part1(grid, folds):
  first_fold = folds[0]
  grid_1, grid_2 = fold_grid(first_fold[0], first_fold[1], grid)
  folded = merge_grids(grid_1, grid_2)
  return sum([sum(x) for x in folded])


def part2(grid, folds):
  temp = grid
  for fold in folds:
    grid_1, grid_2 = fold_grid(fold[0], fold[1], temp)
    temp = merge_grids(grid_1, grid_2)
  return temp


def main():
  marks, folds = read_input("input.txt")
  grid = create_grid(marks)
  res1 = part1(grid, folds)
  print(f"Part 1: {res1}")
  res2 = part2(grid, folds)
  show_grid(stringify(res2))

if __name__ == "__main__":
  main()
