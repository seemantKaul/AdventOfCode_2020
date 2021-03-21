# find the two entries that sum to 2020 and then multiply those two numbers together.
# what is the product of the three entries that sum to 2020?

def problem_1_part1(list_input1):
    print("Solving Problem 1 part 1")
    print(f"input size is {len(list_input1)}")
    list.sort(list_input1)
    # print(list_input1)
    for i in range(len(list_input1)):
        for j in range(i+1, len(list_input1)):
            # print(list_input1[i])
            s = int(list_input1[i])+int(list_input1[j])
            # print(f"the sum is {s}")
            if s == 2020:
                print(f"found the match! \n{list_input1[i]} + {list_input1[j]}\n{int(list_input1[i]) * int(list_input1[j])}")
                return int(list_input1[i]) * int(list_input1[j])
            elif s > 2020:
                # print(f"Sum exceeded 2020: Skipping the loop")
                break


def problem_1_part2(list_input1):
    print("Solving Problem 1 part 2")
    print(f"input size is {len(list_input1)}")
    list.sort(list_input1)
    # print(list_input1)
    for i in range(len(list_input1)):
        for j in range(i + 1, len(list_input1)):
            for k in range(j + 1, len(list_input1)):
                # print(list_input1[i])
                s = int(list_input1[i]) + int(list_input1[j]) + int(list_input1[k])
                # print(f"the sum is {s}")
                if s == 2020:
                    print(f"found the match! \n"
                          f"{list_input1[i]} + {list_input1[j]} + {list_input1[k]}\n"
                          f"{int(list_input1[i]) * int(list_input1[j])*int(list_input1[k])}")
                    return int(list_input1[i]) * int(list_input1[j]) * int(list_input1[k])
                elif s > 2020:
                    # print(f"Sum exceeded 2020: Skipping the loop")
                    break


if __name__ == '__main__':
    with open('Data/Problem1.txt') as input1:
        # Open file for reading into List
        list_inp1 = list(input1.readlines())

        # Strip the spaces and \n and convert to Int
        list_inp1 = [int(x.strip()) for x in list_inp1]

        # Call the function, pass the input
        problem_1_part1(list_inp1)
        problem_1_part2(list_inp1)

