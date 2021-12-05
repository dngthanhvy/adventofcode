def read_file(filename):
    instructions = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            instructions.append(line)
    return instructions


def read_instruction(instruction_line):
    instruction = instruction_line[:-2]
    instruction_count = int(instruction_line[-1])
    return instruction, instruction_count


def calculate_coordinates(filename):
    instructions = read_file(filename)
    horizontal = 0
    depth = 0
    for line in instructions:
        instruction, instruction_count = read_instruction(line)
        if instruction == "forward":
            horizontal += instruction_count
        elif instruction == "down":
            depth += instruction_count
        elif instruction == "up":
            depth -= instruction_count
        else:
            print("Invalid value")
    return horizontal*depth


def calculate_coordinates_with_aim(filename):
    instructions = read_file(filename)
    horizontal = 0
    depth = 0
    aim = 0
    for line in instructions:
        instruction, instruction_count = read_instruction(line)
        if instruction == "forward":
            horizontal += instruction_count
            depth += aim*instruction_count
        elif instruction == "down":
            aim += instruction_count
        elif instruction == "up":
            aim -= instruction_count
        else:
            print("Invalid value")
    return horizontal*depth


def main():
    # PART 1
    part1 = calculate_coordinates("input.txt")
    print(part1)

    # PART 2
    part2 = calculate_coordinates_with_aim("input.txt")
    print(part2)


if __name__ == "__main__":
    main()
