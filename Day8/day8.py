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


def generate_7s_dict():
  numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  return { x: "" for x in numbers }


def find_unique_patterns(signal, display):
  signal = signal.split(" ")
  for num in signal:
    if len(num) == 2:
      display["one"] = set(num)
    elif len(num) == 3:
      display["seven"] = set(num)
    elif len(num) == 4:
      display["four"] = set(num)
    elif len(num) == 7:
      display["eight"] = set(num)
  return display


def decode_six_digits(candidates, display):
  for i, value in enumerate(candidates):
    if len(display["one"].difference(value)) == 1:
      display["six"] = value
    elif len(display["four"].difference(value)) == 1 and value is not display["six"]:
      display["zero"] = value
    else:
      display["nine"] = value
  return display


def decode_five_digits(candidates, display):
  for i, value in enumerate(candidates):
    if len(display["six"].difference(value)) == 1:
      display["five"] = value
    elif len(display["nine"].difference(value)) == 1 and value is not display["five"]:
      display["three"] = value
    else:
      display["two"] = value
  return display


def decode_output(output, display):
  result = []
  for value in output.split(" "):
    found_index = list(display.values()).index(set(value))
    key = list(display.keys())[found_index]
    found_index_in_keys = list(display.keys()).index(key)
    result.append(found_index_in_keys)
  return int("".join(map(str, result)))


def decode(signals, outputs):
  decoded = []
  unique = []
  for (signal, output) in zip(signals, outputs):
    display = generate_7s_dict()
  
    display = find_unique_patterns(signal, display)
    unique.append(count_unique_segments(output))

    six_digits = [set(x) for x in signal.split(" ") if len(x) == 6]
    display = decode_six_digits(six_digits, display)

    five_digits = [set(x) for x in signal.split(" ") if len(x) == 5]
    display = decode_five_digits(five_digits, display)

    decoded.append(decode_output(output, display))
  return sum(unique), sum(decoded)


def main():
  signals, outputs = read_input("input.txt")
  part1, part2 = decode(signals, outputs)
  print(f"Part 1: {part1}")
  print(f"Part 2: {part2}")


if __name__ == "__main__":
  main()