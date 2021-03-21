# Problem - https://adventofcode.com/2020/day/4
# Solution
# Read input
#     read line
#         split by space, add dictionary to set
#         when blank line found, add set to list
#         [(a1:v1, a2:v2, a3:v3), (a1:v1, a2:v2, a3:v3), (a1:v1, a2:v2, a3:v3)]
#         iterate over the list, call function to check all keys
#             If all keys found, increase valid passport count
#         return count

def check_passport(passport_to_check, set_keys_to_check):
    # Returns true if passport has all the keys in the list_keys_to_check
    set_keys = set(passport_to_check.keys())
    if set_keys.issuperset(set_keys_to_check):
        # print(f"{passport_to_check['byr']}\t{passport_to_check['iyr']}\t{passport_to_check['eyr']}\t{passport_to_check['hgt']}\t{passport_to_check['hcl']}\t{passport_to_check['ecl']}\t{passport_to_check['pid']}")
        if check_values(passport_to_check):
            return True

        else:
            return False
    else:
        return False


def check_values(passport_to_validate):
    import re
    # Check byr - (Birth Year) - four digits; at least 1920 and at most 2002.
    patt_number_4 = re.compile("[0-9]{4}")
    if patt_number_4.match(passport_to_validate['byr']):
        pass
    else:
        # print(f"byr - {passport_to_validate['byr']}")
        return False
    if 1920 <= int(passport_to_validate['byr']) <= 2002:
        pass
    else:
        # print(f"byr - {passport_to_validate['byr']}")
        return False

    # Check iyr - (Issue Year) - four digits; at least 2010 and at most 2020.
    patt_number_4 = re.compile("[0-9]{4}")
    if patt_number_4.match(passport_to_validate['iyr']):
        pass
    else:
        # print(f"iyr - {passport_to_validate['iyr']}")
        return False
    if 2010 <= int(passport_to_validate['iyr']) <= 2020:
        pass
    else:
        # print(f"iyr - {passport_to_validate['iyr']}")
        return False

    # Check eyr - (Expiration Year) - four digits; at least 2020 and at most 2030.
    patt_number_4 = re.compile("[0-9]{4}")
    if patt_number_4.match(passport_to_validate['eyr']):
        if 2020 <= int(passport_to_validate['eyr']) <= 2030:
            pass
        else:
            # print(f"eyr - {passport_to_validate['eyr']}")
            return False
    else:
        # print(f"eyr - {passport_to_validate['eyr']}")
        return False

    # Check hgt - (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    patt_height_cm = re.compile("[0-9]{3}cm")
    patt_height_in = re.compile("[0-9]{2}in")
    if patt_height_cm.match(passport_to_validate['hgt']):
        if 150 <= int(passport_to_validate['hgt'][:3]) <= 193:
            pass
        else:
            # print(f"hgt - {passport_to_validate['hgt']}")
            return False
    elif patt_height_in.match(passport_to_validate['hgt']):
        if 59 <= int(passport_to_validate['hgt'][:2]) <= 76:
            pass
        else:
            # print(f"hgt - {passport_to_validate['hgt']}")
            return False
    else:
        # print(f"hgt - {passport_to_validate['hgt']}")
        return False

    # Check hcl - (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    patt_color_hair = re.compile(r"#[\da-f]{6}$")
    if patt_color_hair.match(passport_to_validate['hcl']):
        pass
    else:
        # print(f"hcl - {passport_to_validate['hcl']}")
        return False

    # Check ecl - (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    patt_color_eye = re.compile("amb|blu|brn|gry|grn|hzl|oth")
    if patt_color_eye.match(passport_to_validate['ecl']):
        pass
    else:
        # print(f"ecl - {passport_to_validate['ecl']}")
        return False

    # Check pid - (Passport ID) - a nine-digit number, including leading zeroes.
    patt_pid = re.compile("[0-9]{9}$")
    if patt_pid.match(passport_to_validate['pid']):
        pass
    else:
        # print(f"pid - {passport_to_validate['pid']}")
        return False

    # If we have reached this point, then none of the return False was triggered, hence return True
    # print(f"validPassport {passport_to_validate['pid']}")
    return True


if __name__ == '__main__':
    list_passports = []
    passport = {}
    valid_passport_count = 0
    keys_to_check = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    with open("Data/Problem4.txt") as file:
        lines = file.readlines()
    for line in lines:
        keys = {}
        if line == '\n':
            # If blank line found, then working passport is done. Append the working passport dictionary to list
            # and reset the dictionary
            list_passports.append(passport)
            passport = {}
        else:
            # reading next line of the same passport
            # first split the keys by space
            list_str_keys = [x.strip() for x in line.split(' ')]
            # iterate through all keys, split by : and create dictionary for each attribute
            for passport_item in list_str_keys:
                key, value = passport_item.split(':')
                d = dict({key: value})
                # Add the attributes to working passport
                passport.update(d)
    # adding the final passport to list. This is because there is no \n at the end of input file
    list_passports.append(passport)
    for passport_item in list_passports:
        # print(passport_item)
        if check_passport(passport_item, keys_to_check):
            valid_passport_count += 1
    print(f"found {valid_passport_count} valid passports")


