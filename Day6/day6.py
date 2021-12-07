def read_input(filename):
  answers = []
  with open(filename, "r") as f:
    group_answer = []
    for line in f.readlines():
      if line != '\n':
        group_answer.append(line.strip())
      else:
        answers.append(group_answer)
        group_answer = []
    answers.append(group_answer)
  return answers


def combine_answers(group_answer):
  unique_answers = []
  for person in group_answer:
    for answer in person:
      if answer not in unique_answers:
        unique_answers.append(answer)
  return len(unique_answers)


def part1(answers):
  return sum([combine_answers(answer) for answer in answers])


def combine_answers2(group_answer):
  answers = {x: 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
  for person in group_answer:
    for answer in person:
        answers[answer] += 1
  count = 0
  for key, value in answers.items():
    if value == len(group_answer):
      count += 1
  return count


def part2(answers):
  return sum([combine_answers2(answer) for answer in answers])


def main():
  answers = read_input("input.txt")
  print(f"Part 1: {part1(answers)}")
  print(f"Part 2: {part2(answers)}")


if __name__ == "__main__":
  main()
