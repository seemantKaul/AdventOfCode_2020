# Problem: https://adventofcode.com/2020/day/6
# Solution: Read the file row by row. Keep adding to a set.
# When a \n is reached add the set to a list
# count the size of each set in list and then sum those numbers


if __name__ == "__main__":
    with open("Data/Problem6.txt") as file:
        list_input_6 = file.readlines()
        list_input_6 = [x.strip() for x in list_input_6]
    set_form = set()
    list_forms = []
    skip_flag = False
    for line in list_input_6:
        if line == '':
            if not skip_flag:
                list_forms.append(set_form)
            set_form = set()
            skip_flag = False
        else:
            s = set(line)
            # If the set is empty (first time) update instead of intersect
            if len(set_form) == 0:
                set_form.update(s)
            else:
                # Use Intersect from next time onwards
                set_form.intersection_update(s)

                # If the intersection ever reach 0, break out so we don't start over again
                if len(set_form) == 0:
                    skip_flag = True
    # For the final set in case there is no last line to end the set
    list_forms.append(set_form)
    # print(list_forms)
    sum_ans = 0
    for form in list_forms:
        print(len(form))
        sum_ans = sum_ans + len(form)
    print(sum_ans)
