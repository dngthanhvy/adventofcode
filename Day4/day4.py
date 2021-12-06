valid_keys = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


def read_input(filename):
    passports = []
    with open(filename, 'r') as f:
        passport = []
        for line in f.readlines():
            if line != '\n':
                temp = line.strip().split(' ')
                for t in temp:
                    passport.append(t)
            else:
                passports.append(passport)
                passport = []
        passports.append(passport)
    return passports


def parse_passport(passport):
    passport_dict = {}
    for element in passport:
        key, value = element.split(':')
        passport_dict[key] = value
    return passport_dict


def validate_passport(passport):
    result = []
    for key in valid_keys:
        if key not in passport:
            result.append(False)
        else:
            result.append(True)
    return all(result)


def part1():
    passports = [parse_passport(passport) for passport in read_input("input.txt")]
    valid_passports = sum([validate_passport(passport) for passport in passports])
    return valid_passports


def validate_fields(passport):
    result = []
    for key, value in passport.items():
        result.append(
            (key == "byr" and 1920 <= int(value) <= 2002) or
            (key == "iyr" and 2010 <= int(value) <= 2020) or
            (key == "eyr" and 2020 <= int(value) <= 2030 and len(value) >= 4) or
            (key == "hgt" and (value.endswith("cm") and 150 <= int(value[:-2]) <= 193) or (value.endswith("in") and 59 <= int(value[:-2]) <= 76)) or
            (key == "hcl" and value.startswith("#") and len(value) == 7 and all(c in "0123456789abcdef" for c in value[1:])) or
            (key == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) or
            (key == "pid" and len(value) == 9) or
            (key == "cid")
        )
    return all(result)


def valid_passports(passports):
    return [passport for passport in passports if validate_passport(passport)]


def part2():
    passports = [parse_passport(passport) for passport in read_input("input.txt")]
    return sum([validate_fields(passport) for passport in valid_passports(passports)])


def main():
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()