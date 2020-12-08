def main():
    with open('D:\ztmDevelop\AdventOfCode_2020\day8input.txt','r') as string:
        file = string.read()
    commands_list = file.splitlines()
    for i in range(len(commands_list)):
        commands_list[i] = [commands_list[i][0:3], commands_list[i][4:], '-']
    accumulator = 0
    index = 0
    while commands_list[index][2] == '-':
        commands_list[index][2] = '+'
        if commands_list[index][0] == 'acc':
            accumulator += int(commands_list[index][1])
            index += 1
        elif commands_list[index][0] == 'jmp':
            index += int(commands_list[index][1])
        else:
            index += 1
        
    print("Part 1's answer: %d" % accumulator)
    
    # part 2
    
    accumulator = 0
    index = 0
    corrupted_instruction_counter = 0
    while index < len(commands_list):
        commands_list = file.splitlines()
        for i in range(len(commands_list)):
            commands_list[i] = [commands_list[i][0:3], commands_list[i][4:], '-']
        for i in range(corrupted_instruction_counter, len(commands_list)):
            if commands_list[i][0] == 'jmp':
                commands_list[i][0] = 'nop'
                corrupted_instruction_counter = i + 1
                break
            elif commands_list[i][0] == 'nop':
                commands_list[i][0] = 'jmp'
                corrupted_instruction_counter = i + 1
                break
        accumulator = 0
        index = 0
        while commands_list[index][2] == '-':
            commands_list[index][2] = '+'
            if commands_list[index][0] == 'acc':
                accumulator += int(commands_list[index][1])
                index += 1
            elif commands_list[index][0] == 'jmp':
                index += int(commands_list[index][1])
            else:
                index += 1
            if index >= len(commands_list):
                break
    print("Part 2's answer: %d" % accumulator)
    
    
    
    input()
if __name__ == "__main__":
    main()
