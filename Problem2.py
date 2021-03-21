def problem2(list_input_2):
    valid_count = 0
    for entry in list_input_2:
        min_count = 0
        max_count = 0
        actual_count = 0
        char_to_check = ''
        password_string = ''
        count_str, char_to_check, password_string = entry.split()
        min_count, max_count = [int(x) for x in count_str.split('-')]
        char_to_check = char_to_check[0]
        actual_count = password_string.count(char_to_check)
        if min_count <= actual_count <= max_count:
            valid_count += 1
    print(f"Found {valid_count} valid passwords for part 1")


def problem2_part2(list_input_2):
    valid_count = 0
    for entry in list_input_2:
        index_1 = 0
        index_2 = 0
        char_to_check = ''
        password_string = ''
        count_str, char_to_check, password_string = entry.split()
        index_1, index_2 = [int(x) - 1 for x in count_str.split('-')]
        char_to_check = char_to_check[0]
        if (password_string[index_1] == char_to_check and password_string[index_2] != char_to_check) or (
                password_string[index_2] == char_to_check and password_string[index_1] != char_to_check):
            valid_count += 1
    print(f"Found {valid_count} valid passwords for part 2")


if __name__ == '__main__':
    with open('Data/Problem2.txt') as file:
        list_input2 = file.readlines()
        list_input2 = [x.strip() for x in list_input2]
        print(f"Running Problem 2 with {len(list_input2)} input size")
        problem2(list_input2)
        problem2_part2(list_input2)
