# Problem - https://adventofcode.com/2020/day/5
# Solution - Create a function to decode the ticket and find the row and column and seat ID
# Seat id = multiply the row by 8, then add the column
# Part 1 - Find the ticket with max seat id


def validate_ticket(ticket_number):
    import re
    pattern = re.compile("[FB]{7}[RL]{3}")
    if pattern.match(ticket_number):
        return True
    else:
        return False


def compute_seat_id(ticket_number):
    import math
    # returns the Seat Id as number

    # Initialize for each ticket number
    min_row = 0
    max_row = MAX_ROWS
    row = 0
    min_col = 0
    max_col = MAX_COLS
    col = 0
    if validate_ticket(ticket_number):
        for token in ticket_number:
            if token == 'F':
                max_row = math.floor(max_row - (max_row - min_row) / 2)
                if min_row == max_row:
                    row = min_row
            elif token == 'B':
                min_row = math.floor(min_row + (max_row - min_row) / 2) + 1
                if min_row == max_row:
                    row = min_row
            elif token == 'R':
                min_col = math.floor(min_col + (max_col - min_col) / 2) + 1
                if min_col == max_col:
                    col = min_col
            elif token == 'L':
                max_col = math.floor(max_col - (max_col - min_col) / 2)
                if min_col == max_col:
                    col = min_col
        # print(f"{ticket_number}| row {row} | col {col}")
        return row * 8 + col

    else:
        print(f"invalid ticket {ticket_number}")


if __name__ == '__main__':
    MAX_ROWS = 127
    MAX_COLS = 7
    list_seat_id = []
    with open('Data/Problem5.txt') as file:
        list_input_5 = file.readlines()
        list_input_5 = [x.strip() for x in list_input_5]
    for ticket in list_input_5:
        seat = compute_seat_id(ticket)
        list_seat_id.append(seat)
    print(f"max seat id is {max(list_seat_id)}")
    list_seat_id.sort()
    # print(list_seat_id)

    # We prime the i as first seat number in the list
    # and then traverse the list to find a seat number that doesnt match its index.
    # since the sead numbers are sequential, the first mismatch is our seat
    i = int(list_seat_id[0])
    for seat in list_seat_id:
        if int(seat) != i:
            pass
            print(f"Your seat number is {i}")
            break
        else:
            i += 1
