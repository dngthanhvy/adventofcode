from copy import deepcopy

def read_input(filename):
  with open(filename, "r") as file:
    timers = [int(x) for x in file.readline().split(',')]
  return timers

def countdown_timer(timers):
  temp = timers.copy()
  for i in range(len(temp)):
    if temp[i] != 0:
      temp[i] -= 1
    else:
      temp[i] = 6
      temp.append(8)
  return temp


def timers_after_days(timers, number_of_days):
  temp = timers.copy()
  for i in range(1, number_of_days + 1):
    temp = countdown_timer(temp)
  return temp


def timers_after_days_faster(timers_dict, number_of_days):
    for day in range(number_of_days):
        temp = {x: 0 for x in range(9)}
        for i in range(9):
            if i == 0:
                temp[6] = timers_dict[0]
                temp[8] = timers_dict[0]
            else:
                temp[i - 1] += timers_dict[i]
            print(temp)
        timers_dict = deepcopy(temp)
    return timers_dict


def main():
  timers = read_input("input.txt")
  timers_dict = {a: 0 for a in range(9)}

  # Part 2 : generates a dictionary for each value count 0-8
  for timer in timers:
      timers_dict[timer] += 1

  # part1 = timers_after_days(timers, 80)
  part2 = timers_after_days_faster(timers_dict, 5)
  # print("Part 1: ", len(part1))
  print("Part 2: ", sum(part2.values()))


if __name__ == "__main__":
  main()