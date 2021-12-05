def read_file(filename):
    numbers = []
    with open(filename) as file:
        while number := file.readline().rstrip():
            numbers.append(number)
    return numbers


def complementary(binary_number):
    return (bin(int(binary_number, 2) ^ (int("1"*len(binary_number), 2))))[2:]


def get_gamma(numbers):
    count_zero = 0
    count_one = 0
    length = len(numbers)
    gamma = ""
    for column in range(len(numbers[0])):
        for row in range(length):
            if numbers[row][column] == "0":
                count_zero += 1
            else:
                count_one += 1

        if count_zero > count_one:
            gamma += "0"
        else:
            gamma += "1"

        count_zero = 0
        count_one = 0

    return gamma


def remove_number_that_starts_with(numbers, x, position):
    for number in numbers:
        if number[position] == x:
            numbers.remove(number)
    return numbers


def get_oxygen(numbers):
    for j in range(len(numbers[0])):
        count_zero = 0
        count_one = 0
        for i in range(len(numbers)):
            if int(numbers[i][j]) == 1:
                count_one += 1
            else:
                count_zero += 1
        if count_zero > 0 and count_one > 0:
            if count_one >= count_zero:
                numbers = list(filter(lambda a: int(a[j]) == 1, numbers))

            if count_zero > count_one:
                numbers = list(filter(lambda a: int(a[j]) == 0, numbers))
    return numbers


def get_carbon_dioxide(numbers):
    for j in range(len(numbers[0])):
        count_zero = 0
        count_one = 0
        for i in range(len(numbers)):
            if int(numbers[i][j]) == 1:
                count_one += 1
            else:
                count_zero += 1
        if count_zero > 0 and count_one > 0:
            if count_one >= count_zero:
                numbers = list(filter(lambda a: int(a[j]) == 0, numbers))
            if count_zero > count_one:
                numbers = list(filter(lambda a: int(a[j]) == 1, numbers))
    return numbers


def main():
    numbers = read_file("input.txt")
    gamma = get_gamma(numbers)
    oxygen = get_oxygen(numbers)
    carbon_dioxide = get_carbon_dioxide(numbers)
    print("Part 1: " + str(int(gamma, 2) * int(complementary(gamma), 2)))
    print("Part 2: " + str(int(oxygen[0], 2) * int(carbon_dioxide[0], 2)))


if __name__ == "__main__":
    main()