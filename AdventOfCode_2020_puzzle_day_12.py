def rotate_ship(current_direction, rotate_direction, degrees):
    if current_direction == 'east':
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'north'
            elif degrees == '180':
                current_direction = 'west'
            else:
                current_direction = 'south'
        else:
            if degrees == '90':
                current_direction = 'south'
            elif degrees == '180':
                current_direction = 'west'
            else:
                current_direction = 'north'
    elif current_direction == 'west':
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'south'
            elif degrees == '180':
                current_direction = 'east'
            else:
                current_direction = 'north'
        else:
            if degrees == '90':
                current_direction = 'north'
            elif degrees == '180':
                current_direction = 'east'
            else:
                current_direction = 'south'
    elif current_direction == 'north':
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'west'
            elif degrees == '180':
                current_direction = 'south'
            else:
                current_direction = 'east'
        else:
            if degrees == '90':
                current_direction = 'east'
            elif degrees == '180':
                current_direction = 'south'
            else:
                current_direction = 'west'
    else:
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'east'
            elif degrees == '180':
                current_direction = 'north'
            else:
                current_direction = 'west'
        else:
            if degrees == '90':
                current_direction = 'west'
            elif degrees == '180':
                current_direction = 'north'
            else:
                current_direction = 'east'
    return current_direction

def rotate_ship_2(current_direction, rotate_direction, degrees):
    if current_direction == 'east':
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'north'
            elif degrees == '180':
                current_direction = 'west'
            else:
                current_direction = 'south'
        else:
            if degrees == '90':
                current_direction = 'south'
            elif degrees == '180':
                current_direction = 'west'
            else:
                current_direction = 'north'
    elif current_direction == 'west':
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'south'
            elif degrees == '180':
                current_direction = 'east'
            else:
                current_direction = 'north'
        else:
            if degrees == '90':
                current_direction = 'north'
            elif degrees == '180':
                current_direction = 'east'
            else:
                current_direction = 'south'
    elif current_direction == 'north':
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'west'
            elif degrees == '180':
                current_direction = 'south'
            else:
                current_direction = 'east'
        else:
            if degrees == '90':
                current_direction = 'east'
            elif degrees == '180':
                current_direction = 'south'
            else:
                current_direction = 'west'
    else:
        if rotate_direction == 'L':
            if degrees == '90':
                current_direction = 'east'
            elif degrees == '180':
                current_direction = 'north'
            else:
                current_direction = 'west'
        else:
            if degrees == '90':
                current_direction = 'west'
            elif degrees == '180':
                current_direction = 'north'
            else:
                current_direction = 'east'
    return current_direction

def direction_checker_and_adder(current_waypoint, direction, value):
    if direction == 'N':
        if current_waypoint[0][0] == 'north':
            current_waypoint[0][1] += value
        elif current_waypoint[1][0] == 'north':
            current_waypoint[1][1] += value
        elif current_waypoint[0][0] == 'south':
            current_waypoint[0][1] -= value
        elif current_waypoint[1][0] == 'south':
            current_waypoint[1][1] -= value
    elif direction == 'S':
        if current_waypoint[0][0] == 'north':
            current_waypoint[0][1] -= value
        elif current_waypoint[1][0] == 'north':
            current_waypoint[1][1] -= value
        elif current_waypoint[0][0] == 'south':
            current_waypoint[0][1] += value
        elif current_waypoint[1][0] == 'south':
            current_waypoint[1][1] += value
    elif direction == 'E':
        if current_waypoint[0][0] == 'east':
            current_waypoint[0][1] += value
        elif current_waypoint[1][0] == 'east':
            current_waypoint[1][1] += value
        elif current_waypoint[0][0] == 'west':
            current_waypoint[0][1] -= value
        elif current_waypoint[1][0] == 'west':
            current_waypoint[1][1] -= value
    else:
        if current_waypoint[0][0] == 'east':
            current_waypoint[0][1] -= value
        elif current_waypoint[1][0] == 'east':
            current_waypoint[1][1] -= value
        elif current_waypoint[0][0] == 'west':
            current_waypoint[0][1] += value
        elif current_waypoint[1][0] == 'west':
            current_waypoint[1][1] += value
    return current_waypoint

def forward_instruction_multiplier_north_south_set(value, current_waypoint):
    if current_waypoint[0][0] == 'north':
        return current_waypoint[0][1] * value
    elif current_waypoint[1][0] == 'north':
        return current_waypoint[1][1] * value
    elif current_waypoint[0][0] == 'south':
        return current_waypoint[0][1] * value * -1
    else:
        return current_waypoint[1][1] * value * -1

def forward_instruction_multiplier_east_west_set(value, current_waypoint):
    if current_waypoint[0][0] == 'east':
        return current_waypoint[0][1] * value
    elif current_waypoint[1][0] == 'east':
        return current_waypoint[1][1] * value
    elif current_waypoint[0][0] == 'west':
        return current_waypoint[0][1] * value * -1
    else:
        return current_waypoint[1][1] * value * -1

def main():
    with open('day12input.txt','r') as string:
        file = string.read()
    instruction_list = file.splitlines()
    north_south_set = 0
    east_west_set = 0
    F_direction = 'east'
    for i in range(len(instruction_list)):
        if instruction_list[i][0] == 'N':
            north_south_set += int(instruction_list[i][1:])
        elif instruction_list[i][0] == 'S':
            north_south_set -= int(instruction_list[i][1:])
        elif instruction_list[i][0] == 'E':
            east_west_set += int(instruction_list[i][1:])
        elif instruction_list[i][0] == 'W':
            east_west_set -= int(instruction_list[i][1:])
        elif instruction_list[i][0] == 'L' or instruction_list[i][0] == 'R':
            F_direction = rotate_ship(F_direction, instruction_list[i][0], instruction_list[i][1:])
        elif instruction_list[i][0] == 'F':
            if F_direction == 'north':
                north_south_set += int(instruction_list[i][1:])
            elif F_direction == 'south':
                north_south_set -= int(instruction_list[i][1:])
            elif F_direction == 'east':
                east_west_set += int(instruction_list[i][1:])
            else:
                east_west_set -= int(instruction_list[i][1:])
    distance = abs(north_south_set) + abs(east_west_set)
    print(f'--PART 1-- The distance is: {distance}\n')
    
    # Part 2
    
    north_south_set = 0
    east_west_set = 0
    waypoint = [['east', 10],['north', 1]]
    for i in range(len(instruction_list)):
        if instruction_list[i][0] == 'L' or instruction_list[i][0] == 'R':
            waypoint[0][0] = rotate_ship_2(waypoint[0][0], instruction_list[i][0], instruction_list[i][1:])
            waypoint[1][0] = rotate_ship_2(waypoint[1][0], instruction_list[i][0], instruction_list[i][1:])
        if instruction_list[i][0] == 'N':
            waypoint = direction_checker_and_adder(waypoint, 'N', int(instruction_list[i][1:]))
        elif instruction_list[i][0] == 'S':
            waypoint = direction_checker_and_adder(waypoint, 'S', int(instruction_list[i][1:]))
        elif instruction_list[i][0] == 'E':
            waypoint = direction_checker_and_adder(waypoint, 'E', int(instruction_list[i][1:]))
        elif instruction_list[i][0] == 'W':
            waypoint = direction_checker_and_adder(waypoint, 'W', int(instruction_list[i][1:]))
        elif instruction_list[i][0] == 'F':
            north_south_set += forward_instruction_multiplier_north_south_set(int(instruction_list[i][1:]), waypoint)
            east_west_set += forward_instruction_multiplier_east_west_set(int(instruction_list[i][1:]), waypoint)
    distance = abs(north_south_set) + abs(east_west_set)
    print(f'--PART 2-- The distance is: {distance}')
    
    input()
if __name__ == "__main__":
    main()
