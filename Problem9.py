# Problem: https://adventofcode.com/2020/day/9

# Solution:
# find sum pair: sort the input list, iterate through each item adding the items ahead of it
# one by one and checking if sum is = desired or > desired. If > desired, break loop because
# list is sorted and no number after that is going to result in desired.

# find_sum_contiguous: Iterate over the list using a range of 0 to length of list.
# Keep adding until the running sum is equal to or > desired. Break loop if running sum
# is > desired and start next loop starting from next item. 

def find_sum_pair(list_inp, sum_val):
    list.sort(list_inp)
    for i in range(len(list_inp)):
        for j in range(i+1, len(list_inp)):
            s = int(list_inp[i]) + int(list_inp[j])
            if s == sum_val:
                return True
            elif s > sum_val:
                # print(f"Sum exceeded 2020: Skipping the loop.")
                break
    return False


def find_sum_contiguous(list_inp, sum_val):
    for x in range(len(list_inp)):
        running_sum = 0
        counter = 0
        while running_sum < sum_val:
            running_sum += list_inp[x + counter]
            counter += 1
        if running_sum == sum_val:
            print(f"found a contiguous series {list_inp[x:x+counter]}")
            code = min(list_inp[x:x+counter]) + max(list_inp[x:x+counter])
            print(f"code is {code}")
            return code
    print("No contiguous series found")


PREAMBLE = 25
if __name__ == '__main__':
    # with open('Data/Test.txt') as file:
    with open('Data/Problem9.txt') as file:
        list_input_9 = file.readlines()
        list_input = [int(x.strip()) for x in list_input_9]
    for index in range(PREAMBLE, len(list_input)):
        if find_sum_pair(list_input[index - PREAMBLE:index], list_input[index]):
            pass
        else:
            print(f"{list_input[index]} is the answer")
            print(f"The Preamble was {list_input[index - PREAMBLE:index]}")
            break
    find_sum_contiguous(list_input, list_input[index])
