# Problem: https://adventofcode.com/2020/day/8

# Solution: maintain an accumulator to calculate the  value
# A row index to determine which instruction we are on
# A change index to maintain which instruction we are changing
# Update accumulator and row index according to instructions. Add row index to a list. Before executing
# an instruction, check if the row index is already present in the list, if so we are in a loop
# Break out of loop, reset the Instruction list and change the next instruction


def process_instruction(instruction, row_index, acc, stop_execution, list_done):
    # print(f"row index:{row_index}\tacc:{acc}\tlist done:{list_done}")

    # Check condition for looping
    if row_index in list_done:
        print(f"Row index {row_index} is repeating. Acc is {acc}")
        # this will break us out of the loop
        stop_execution = True
    else:
        list_done.append(row_index)
        if instruction[0] == 'nop':
            row_index += 1
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            row_index += 1
        if instruction[0] == 'jmp':
            row_index += int(instruction[1])
    return row_index, acc, stop_execution


def run_program(lst_instructions):
    row_index = 0
    acc = 0
    list_done = []
    stop_execution = False
    max_row_index = len(lst_instructions)
    # print(list_instructions)
    while not stop_execution and row_index < max_row_index:
        row_index, acc, stop_execution = process_instruction(lst_instructions[row_index], row_index, acc, stop_execution, list_done)

    # Once out of the above loop, check if we passed through or broke out due to looping
    if row_index >= max_row_index:
        print(f"program terminated successfully with acc = {acc}")
        return "Success"
    else:
        return "Failure"


if __name__ == '__main__':
    with open('Data/Problem8.txt') as file:
        list_input_8 = [x.strip() for x in file.readlines()]
    change_index = 0
    list_instructions = [x.split() for x in list_input_8]

    # Keep running the program with different inputs until return code is Success
    while True:
        ret_code = run_program(list_instructions)
        if ret_code == 'Success':
            break
        else:
            list_instructions = [x.split() for x in list_input_8]

            # Find the next instruction that is either a 'nop' or a 'jmp'
            while True:
                if list_instructions[change_index][0] == "nop":
                    list_instructions[change_index][0] = "jmp"
                    change_index += 1
                    break
                if list_instructions[change_index][0] == "jmp":
                    list_instructions[change_index][0] = "nop"
                    change_index += 1
                    break
                change_index += 1

