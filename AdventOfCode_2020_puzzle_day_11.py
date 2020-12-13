def cycle(lines_list):
    current_state = []
    for i in range(len(lines_list)):
        current_state.append(list(lines_list[i]))
    list_of_about_to_become_empty_seats_locations = []
    list_of_about_to_become_occupied_seats_locations = []
    for i in range(len(lines_list)):
        for j in range(len(lines_list[0])):
            if lines_list[i][j] == 'L':
                if i == 0:
                    if j == 0:
                        if (lines_list[i][j+1] == 'L' or lines_list[i][j+1] == '.') and (lines_list[i+1][j] == 'L' or lines_list[i+1][j] == '.') and (lines_list[i+1][j+1]== 'L' or lines_list[i+1][j+1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    elif j == len(lines_list[0]) - 1:
                        if (lines_list[i][j-1]== 'L' or lines_list[i][j-1] == '.') and (lines_list[i+1][j]== 'L' or lines_list[i+1][j] == '.') and (lines_list[i+1][j-1]== 'L' or lines_list[i+1][j-1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    else:
                        if (lines_list[i][j-1]== 'L' or lines_list[i][j-1] == '.') and (lines_list[i][j+1] == 'L' or lines_list[i][j+1] == '.') and (lines_list[i+1][j]== 'L' or lines_list[i+1][j] == '.') and (lines_list[i+1][j-1]== 'L' or lines_list[i+1][j-1] == '.') and (lines_list[i+1][j+1]== 'L' or lines_list[i+1][j+1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                elif i == len(lines_list) - 1:
                    if j == 0:
                        if (lines_list[i][j+1]== 'L' or lines_list[i][j+1] == '.') and (lines_list[i-1][j]== 'L' or lines_list[i-1][j] == '.') and (lines_list[i-1][j+1]== 'L' or lines_list[i-1][j+1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    elif j == len(lines_list[0]) - 1:
                        if (lines_list[i][j-1]== 'L' or lines_list[i][j-1] == '.') and (lines_list[i-1][j]== 'L' or lines_list[i-1][j] == '.') and (lines_list[i-1][j-1]== 'L' or lines_list[i-1][j-1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    else:
                        if (lines_list[i][j-1]== 'L' or lines_list[i][j-1] == '.') and (lines_list[i][j+1]== 'L' or lines_list[i][j+1] == '.') and (lines_list[i-1][j]== 'L' or lines_list[i-1][j] == '.') and (lines_list[i-1][j-1]== 'L' or lines_list[i-1][j-1] == '.') and (lines_list[i-1][j-1]== 'L' or lines_list[i-1][j-1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                else:
                    if j == 0:
                        if (lines_list[i][j+1]== 'L' or lines_list[i][j+1] == '.') and (lines_list[i+1][j] == 'L' or lines_list[i+1][j] == '.') and (lines_list[i+1][j+1]== 'L' or lines_list[i+1][j+1] == '.') and (lines_list[i-1][j]== 'L' or lines_list[i-1][j] == '.') and (lines_list[i-1][j+1]== 'L' or lines_list[i-1][j+1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    elif j == len(lines_list[0]) - 1:
                        if (lines_list[i][j-1]== 'L' or lines_list[i][j-1] == '.') and (lines_list[i+1][j] == 'L' or lines_list[i+1][j] == '.') and (lines_list[i+1][j-1] == 'L' or lines_list[i+1][j-1] == '.') and (lines_list[i-1][j]== 'L' or lines_list[i-1][j] == '.') and (lines_list[i-1][j-1]== 'L' or lines_list[i-1][j-1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    else:
                        if (lines_list[i][j-1]== 'L' or lines_list[i][j-1] == '.') and (lines_list[i][j+1]== 'L' or lines_list[i][j+1] == '.') and (lines_list[i+1][j]== 'L' or lines_list[i+1][j] == '.') and (lines_list[i+1][j-1]== 'L' or lines_list[i+1][j-1] == '.') and (lines_list[i+1][j+1]== 'L' or lines_list[i+1][j+1] == '.') and (lines_list[i-1][j]== 'L' or lines_list[i-1][j] == '.') and (lines_list[i-1][j-1]== 'L' or lines_list[i-1][j-1] == '.') and (lines_list[i-1][j+1]== 'L' or lines_list[i-1][j+1] == '.'):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
            elif lines_list[i][j] == '#':
                counter = 0
                if (i == 0 or i == len(lines_list) - 1) and (j == 0 or j == len(lines_list[0]) - 1):
                    pass
                else:
                    if i == 0:
                        if lines_list[i][j-1] == '#':
                            counter += 1
                        if lines_list[i][j+1] == '#':
                            counter += 1
                        if lines_list[i+1][j] == '#':
                            counter += 1
                        if lines_list[i+1][j-1] == '#':
                            counter += 1
                        if lines_list[i+1][j+1] == '#':
                            counter += 1
                    elif i == len(lines_list) - 1:
                        if lines_list[i][j-1] == '#':
                            counter += 1
                        if lines_list[i][j+1] == '#':
                            counter += 1
                        if lines_list[i-1][j] == '#':
                            counter += 1
                        if lines_list[i-1][j-1] == '#':
                            counter += 1
                        if lines_list[i-1][j+1] == '#':
                            counter += 1
                    elif j == 0:
                        if lines_list[i][j+1] == '#':
                            counter += 1
                        if lines_list[i-1][j] == '#':
                            counter += 1
                        if lines_list[i-1][j+1] == '#':
                            counter += 1
                        if lines_list[i+1][j] == '#':
                            counter += 1
                        if lines_list[i+1][j+1] == '#':
                            counter += 1
                    elif j == len(lines_list[0]) - 1:
                        if lines_list[i][j-1] == '#':
                            counter += 1
                        if lines_list[i-1][j] == '#':
                            counter += 1
                        if lines_list[i-1][j-1] == '#':
                            counter += 1
                        if lines_list[i+1][j] == '#':
                            counter += 1
                        if lines_list[i+1][j-1] == '#':
                            counter += 1
                    else:
                        if lines_list[i][j-1] == '#':
                            counter += 1
                        if lines_list[i][j+1] == '#':
                            counter += 1
                        if lines_list[i-1][j] == '#':
                            counter += 1
                        if lines_list[i-1][j-1] == '#':
                            counter += 1
                        if lines_list[i-1][j+1] == '#':
                            counter += 1
                        if lines_list[i+1][j] == '#':
                            counter += 1
                        if lines_list[i+1][j-1] == '#':
                            counter += 1
                        if lines_list[i+1][j+1] == '#':
                            counter += 1
                    if counter >= 4:
                        list_of_about_to_become_empty_seats_locations.append([i,j])
    for i in list_of_about_to_become_empty_seats_locations:
        lines_list[i[0]][i[1]] = 'L'
    for i in list_of_about_to_become_occupied_seats_locations:
        lines_list[i[0]][i[1]] = '#'
    if lines_list == current_state:
        return lines_list, False
    else:
        return lines_list, True
    
def cycle2(lines_list):
    current_state = []
    for i in range(len(lines_list)):
        current_state.append(list(lines_list[i]))
    list_of_about_to_become_empty_seats_locations = []
    list_of_about_to_become_occupied_seats_locations = []
    for i in range(len(lines_list)):
        for j in range(len(lines_list[0])):
            if lines_list[i][j] == 'L':
                if i == 0:
                    if j == 0:
                        if right_check(i,j,lines_list) and down_check(i,j,lines_list) and diag_down_right_check(i,j,lines_list):                             
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    elif j == len(lines_list[0]) - 1:
                        if left_check(i,j,lines_list) and down_check(i,j,lines_list) and diag_down_left_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    else:
                        if left_check(i,j,lines_list) and right_check(i,j,lines_list) and down_check(i,j,lines_list) and diag_down_left_check(i,j,lines_list) and diag_down_right_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                elif i == len(lines_list) - 1:
                    if j == 0:
                        if up_check(i,j,lines_list) and right_check(i,j,lines_list) and diag_up_right_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    elif j == len(lines_list[0]) - 1:
                        if up_check(i,j,lines_list) and left_check(i,j,lines_list) and diag_up_left_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    else:
                        if up_check(i,j,lines_list) and right_check(i,j,lines_list) and diag_up_right_check(i,j,lines_list) and left_check(i,j,lines_list) and diag_up_left_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                else:
                    if j == 0:
                        if up_check(i,j,lines_list) and diag_up_right_check(i,j,lines_list) and  right_check(i,j,lines_list) and diag_down_right_check(i,j,lines_list) and down_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    elif j == len(lines_list[0]) - 1:
                        if up_check(i,j,lines_list) and diag_up_left_check(i,j,lines_list) and  left_check(i,j,lines_list) and diag_down_left_check(i,j,lines_list) and down_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
                    else:
                        if up_check(i,j,lines_list) and diag_up_right_check(i,j,lines_list) and  right_check(i,j,lines_list) and diag_down_right_check(i,j,lines_list) and down_check(i,j,lines_list) and diag_up_left_check(i,j,lines_list) and  left_check(i,j,lines_list) and diag_down_left_check(i,j,lines_list):
                            list_of_about_to_become_occupied_seats_locations.append([i,j])
            elif lines_list[i][j] == '#':
                counter = 0
                if (i == 0 or i == len(lines_list) - 1) and (j == 0 or j == len(lines_list[0]) - 1):
                    pass
                else:
                    if i == 0:
                        if not left_check(i, j, lines_list):
                            counter += 1
                        if not right_check(i, j, lines_list):
                            counter += 1
                        if not down_check(i, j, lines_list):
                            counter += 1
                        if not diag_down_left_check(i, j, lines_list):
                            counter += 1
                        if not diag_down_right_check(i, j, lines_list):
                            counter += 1
                    elif i == len(lines_list) - 1:
                        if not left_check(i, j, lines_list):
                            counter += 1
                        if not right_check(i, j, lines_list):
                            counter += 1
                        if not up_check(i, j, lines_list):
                            counter += 1
                        if not diag_up_left_check(i, j, lines_list):
                            counter += 1
                        if not diag_up_right_check(i, j, lines_list):
                            counter += 1
                    elif j == 0:
                        if not up_check(i, j, lines_list):
                            counter += 1
                        if not right_check(i, j, lines_list):
                            counter += 1
                        if not down_check(i, j, lines_list):
                            counter += 1
                        if not diag_up_right_check(i, j, lines_list):
                            counter += 1
                        if not diag_down_right_check(i, j, lines_list):
                            counter += 1
                    elif j == len(lines_list[0]) - 1:
                        if not left_check(i, j, lines_list):
                            counter += 1
                        if not up_check(i, j, lines_list):
                            counter += 1
                        if not down_check(i, j, lines_list):
                            counter += 1
                        if not diag_down_left_check(i, j, lines_list):
                            counter += 1
                        if not diag_up_left_check(i, j, lines_list):
                            counter += 1
                    else:
                        if not left_check(i, j, lines_list):
                            counter += 1
                        if not right_check(i, j, lines_list):
                            counter += 1
                        if not down_check(i, j, lines_list):
                            counter += 1
                        if not up_check(i, j, lines_list):
                            counter += 1
                        if not diag_down_left_check(i, j, lines_list):
                            counter += 1
                        if not diag_down_right_check(i, j, lines_list):
                            counter += 1
                        if not diag_up_right_check(i, j, lines_list):
                            counter += 1
                        if not diag_up_left_check(i, j, lines_list):
                            counter += 1
                    if counter >= 5:
                        list_of_about_to_become_empty_seats_locations.append([i,j])
    for i in list_of_about_to_become_empty_seats_locations:
        lines_list[i[0]][i[1]] = 'L'
    for i in list_of_about_to_become_occupied_seats_locations:
        lines_list[i[0]][i[1]] = '#'
    if lines_list == current_state:
        return lines_list, False
    else:
        return lines_list, True

def left_check(i_input, j_input, input_puzzle):
    left = 'v'
    for l in range(j_input - 1, -1, -1):
        if input_puzzle[i_input][l] == '#':
            left = 'x'
            break
        elif input_puzzle[i_input][l] == 'L':
            break
    if left == 'v':
        return True
    else:
        return False
    
def right_check(i_input, j_input, input_puzzle):
    right = 'v'
    for r in range(j_input + 1, len(input_puzzle[0])):
        if input_puzzle[i_input][r] == '#':
            right = 'x'
            break
        elif input_puzzle[i_input][r] == 'L':
            break
    if right == 'v':
        return True
    else:
        return False

def up_check(i_input, j_input, input_puzzle):
    up = 'v'
    for u in range(i_input - 1, -1, -1):
        if input_puzzle[u][j_input] == '#':
            up = 'x'
            break
        elif input_puzzle[u][j_input] == 'L':
            break
    if up == 'v':
        return True
    else:
        return False

def down_check(i_input, j_input, input_puzzle):
    down = 'v'
    for d in range(i_input + 1, len(input_puzzle)):
        if input_puzzle[d][j_input] == '#':
            down = 'x'
            break
        elif input_puzzle[d][j_input] == 'L':
            break
    if down == 'v':
        return True
    else:
        return False

def diag_up_right_check(i_input, j_input, input_puzzle):
    diag_u_r = 'v'
    for d_u_r in range(min(i_input,len(input_puzzle[0]) - 1 - j_input)):
        if input_puzzle[i_input - (d_u_r + 1)][(d_u_r + 1) + j_input] == '#':
            diag_u_r = 'x'
            break
        elif input_puzzle[i_input - (d_u_r + 1)][(d_u_r + 1) + j_input] == 'L':
            break
    if diag_u_r == 'v':
        return True
    else:
        return False

def diag_up_left_check(i_input, j_input, input_puzzle):
    diag_u_l = 'v'
    for d_u_l in range(min(i_input, j_input)):
        if input_puzzle[i_input - (d_u_l + 1)][j_input - (d_u_l + 1)] == '#':
            diag_u_l = 'x'
            break
        elif input_puzzle[i_input - (d_u_l + 1)][j_input - (d_u_l + 1)] == 'L':
            break
    if diag_u_l == 'v':
        return True
    else:
        return False
        
def diag_down_right_check(i_input, j_input, input_puzzle):
    diag_d_r = 'v'
    for d_d_r in range(min((len(input_puzzle) - 1 - i_input),(len(input_puzzle[0]) - 1 - j_input))):
        if input_puzzle[(d_d_r + 1) + i_input][(d_d_r + 1) + j_input] == '#':
            diag_d_r = 'x'
            break
        elif input_puzzle[(d_d_r + 1) + i_input][(d_d_r + 1) + j_input] == 'L':
            break
    if diag_d_r == 'v':
        return True
    else:
        return False

def diag_down_left_check(i_input, j_input, input_puzzle):
    diag_d_l = 'v'
    for d_d_l in range(min((len(input_puzzle) - 1 - i_input), j_input)):
        if input_puzzle[i_input + (d_d_l + 1)][j_input - (d_d_l + 1)] == '#':
            diag_d_l = 'x'
            break
        elif input_puzzle[i_input + (d_d_l + 1)][j_input - (d_d_l + 1)] == 'L':
            break
    if diag_d_l == 'v':
        return True
    else:
        return False

def main():
    with open('day11input.txt','r') as string:
        file = string.read()
    input_list = file.splitlines()
    for i in range(len(input_list)):
        input_list[i] = list(input_list[i])
    do_a_seat_cycle = True
    while do_a_seat_cycle:
        input_list, do_a_seat_cycle = cycle(input_list)
    print('\n\t--Seat cycle has been stabilized!--\n')
    occupied_counter = 0
    for i in input_list:
        for j in i:
            if j == '#':
                occupied_counter += 1
    print(f'-PART 1- There are {occupied_counter} occupied seats finally!')
    
    # Part 2
    
    input_list = file.splitlines()
    for i in range(len(input_list)):
        input_list[i] = list(input_list[i])
    do_a_seat_cycle = True
    while do_a_seat_cycle:
        input_list, do_a_seat_cycle = cycle2(input_list)
    print('\n\t--Seat cycle has been stabilized!--\n')
    occupied_counter = 0
    for i in input_list:
        for j in i:
            if j == '#':
                occupied_counter += 1
    print(f'-PART 2- There are {occupied_counter} occupied seats finally!')
    input()
            
if __name__ == "__main__":
    main()
