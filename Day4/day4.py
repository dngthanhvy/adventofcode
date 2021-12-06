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


def main():
    passports = [parse_passport(passport) for passport in read_input("input.txt")]
    valid_passports = sum([validate_passport(passport) for passport in passports])
    print(valid_passports)


if __name__ == "__main__":
    main()