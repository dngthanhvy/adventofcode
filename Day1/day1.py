def read_input(filename):
    numbers = []
    with open(filename, 'r') as f:
        for file in f.readlines():
            numbers.append(int(file.rstrip()))
    return numbers


def find_two_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i] * numbers[j]


def find_three_numbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]


def main():
    numbers = read_input('input.txt')
    print(f"Part 1: {find_two_numbers(numbers)}")
    print(f"Part 2: {find_three_numbers(numbers)}")


if __name__ == "__main__":
    main()