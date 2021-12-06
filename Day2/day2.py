def read_input(filename):
    passwords = []
    with open(filename) as f:
        for line in f.readlines():
            passwords.append(parse_input(line))
    return passwords


def parse_input(line):
    criteria, password = line.split(':')
    password = password.strip()
    password_range, letter = criteria.split(' ')
    password_min, password_max = password_range.split('-')
    return int(password_min), int(password_max), letter, password


def is_password_valid(line):
    password_min, password_max, letter, password = line
    letter_count = password.count(letter)
    return password_min <= letter_count <= password_max


def is_password_valid_again(line):
    def xor(x, y):
        return bool((x and not y) or (not x and y))

    position_1, position_2, letter, password = line
    letter_1 = password[position_1 - 1]
    letter_2 = password[position_2 - 1]
    return xor(letter_1 == letter, letter_2 == letter)


def main():
    passwords = read_input("input.txt")
    print(f"Part 1: {sum([is_password_valid(line) for line in passwords])}")
    print(f"Part 2: {sum([is_password_valid_again(line) for line in passwords])}")


if __name__ == "__main__":
    main()