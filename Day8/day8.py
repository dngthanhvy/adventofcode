def read_input(filename):
  signals = []
  outputs = []
  with open(filename, "r") as f:
    for line in f.readlines():
      signal, output = line.strip().split(" | ")
      signals.append(signal)
      outputs.append(output)
  return signals, outputs


def count_unique_segments(output):
  result = []
  for num in output.split(" "):
    if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
      result.append(num)
  return len(result)


def part1(outputs):
  return sum([count_unique_segments(output) for output in outputs])


def main():
  signals, outputs = read_input("input.txt")
  print(f"Part 1: {part1(outputs)}")

if __name__ == "__main__":
  main()

"""
Test input:
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""